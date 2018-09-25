from dataclasses import replace

import docutils.parsers.rst
import docutils.nodes
import docutils.parsers.rst.directives
import docutils.utils
import sphinx.addnodes
import sphinx.writers.html
import sphinx.util.logging
import sphinx.environment

import yaml
import yaml.error

from sphinx_a4doc.contrib.railroad_diagrams import (
    Diagram, Settings, InternalAlignment, EndClass, HrefResolver
)

from sphinx_a4doc.model.model import ModelCache
from sphinx_a4doc.model.model_renderer import Renderer

from typing import *


logger = sphinx.util.logging.getLogger(__name__)


class DomainResolver(HrefResolver):
    def __init__(self, builder, grammar: str):
        self.builder = builder
        self.grammar = grammar

    def resolve(self, text: str, href: Optional[str], title_is_weak: bool):
        # There can be three alternative situations when resolving rules:
        # - href is not passed. In this case we resolve rule as if a role
        #   without an explicit title was invoked, i.e. we treat text as both
        #   title and target. If rule resolution succeeds, we replace title with
        #   a human-readable name assigned to the rule we've just resolved;
        # - href is passed explicitly. In this case we simulate invocation
        #   of a role with an explicit title, i.e. we use href to resolve rule
        #   and we don't mess with title at all.
        # - title_is_weak is set. This means that title comes from a nodoc rule.
        #   In this case we use title only if rule resolution fails.

        title = text
        if href is None:
            target = text
            explicit_title = False
        else:
            target = href
            explicit_title = not title_is_weak

        builder = self.builder
        env = builder.env
        domain = env.get_domain('a4')
        docname = builder.current_docname

        xref = sphinx.addnodes.pending_xref(
            '',
            reftype='rule',
            refdomain='a4',
            refexplicit=False
        )
        xref['a4:has_explicit_title'] = explicit_title
        xref['a4:grammar'] = self.grammar

        try:
            node: docutils.nodes.Element = domain.resolve_xref(
                env,
                docname,
                builder,
                'rule',
                target,
                xref,
                docutils.nodes.literal(
                    '', target.rsplit('.', 1)[-1] if title_is_weak else title)
            )
        except sphinx.environment.NoUri:
            node = None

        if node is None:
            return title, None

        reference = node.next_node(docutils.nodes.reference, include_self=True)
        assert reference is not None
        literal = node.next_node(docutils.nodes.literal, include_self=True)
        assert literal is not None

        if 'refuri' in reference:
            return literal.astext(), reference['refuri']
        else:
            return literal.astext(), '#' + reference['refid']


class RailroadDiagramNode(docutils.nodes.Element, docutils.nodes.General):
    def __init__(self, diagram: dict, options: dict, grammar: str):
        super().__init__('', diagram=diagram, options=options, grammar=grammar)

    @staticmethod
    def visit_node_html(self: sphinx.writers.html.HTMLTranslator, node):
        resolver = DomainResolver(self.builder, node['grammar'])
        dia = Diagram(replace(Settings(href_resolver=resolver), **node['options']))
        try:
            data = dia.load(node['diagram'])
            svg = dia.render(data)
        except Exception as e:
            logger.exception(f'{node.source}:{node.line}: WARNING: {e}')
        else:
            self.body.append('<p class="railroad-diagram-container">')
            self.body.append(svg)
            self.body.append('</p>')

    @staticmethod
    def depart_node(self, node):
        pass


class RailroadDiagram(docutils.parsers.rst.Directive):
    has_content = True
    option_spec = {
        'padding': docutils.parsers.rst.directives.positive_int_list,
        'vertical-separation': docutils.parsers.rst.directives.positive_int,
        'horizontal-separation': docutils.parsers.rst.directives.positive_int,
        'arc-radius': docutils.parsers.rst.directives.positive_int,
        'diagram-class': str.strip,
        'translate-half-pixel': docutils.parsers.rst.directives.flag,
        'internal-alignment': lambda x: InternalAlignment[x.strip().upper()],
        'character-advance': docutils.parsers.rst.directives.positive_int,
        'end-class': lambda x: EndClass[x.strip().upper()],
    }

    def run(self):
        options = {k.replace('-', '_'): v for k, v in self.options.items()}

        if 'translate_half_pixel' in options:
            options['translate_half_pixel'] = True

        env = self.state.document.settings.env
        grammar = env.ref_context.get('a4:grammar', '__default__')

        return [RailroadDiagramNode(self.get_content(), options, grammar)]

    def get_content(self):
        try:
            return yaml.safe_load('\n'.join(self.content))
        except (ValueError, yaml.error.YAMLError) as e:
            return self.state_machine.reporter.error(
                str(e), line=self.content_offset)


class LexerRuleDiagram(RailroadDiagram):
    def get_content(self):
        content = f'grammar X; ROOT : {" ".join(self.content)} ;'
        model = ModelCache.instance().from_text(
            content, (self.state_machine.reporter.source, self.content_offset))
        tree = model.lookup('ROOT')
        if tree is None or tree.content is None:
            return self.state_machine.reporter.error(
                'cannot parse the rule', line=self.content_offset)
        return Renderer().visit(tree.content)


class ParserRuleDiagram(RailroadDiagram):
    def get_content(self):
        content = f'grammar X; root : {" ".join(self.content)} ;'
        model = ModelCache.instance().from_text(
            content, (self.state_machine.reporter.source, self.content_offset))
        tree = model.lookup('root')
        if tree is None or tree.content is None:
            return self.state_machine.reporter.error(
                'cannot parse the rule', line=self.content_offset)
        return Renderer().visit(tree.content)
