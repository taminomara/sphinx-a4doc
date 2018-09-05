from dataclasses import replace

import docutils.parsers.rst
import docutils.nodes
import docutils.parsers.rst.directives
import sphinx.writers.html
import sphinx.util.logging

import yaml
import yaml.error

from sphinx_a4doc.contrib.railroad_diagrams import (
    Diagram, Settings, InternalAlignment, EndClass
)

from sphinx_a4doc.model.model import ModelCache
from sphinx_a4doc.model.model_renderer import Renderer


logger = sphinx.util.logging.getLogger(__name__)


class RailroadDiagramNode(docutils.nodes.Element, docutils.nodes.General):
    def __init__(self, diagram: dict, options: dict):
        super().__init__('', diagram=diagram, options=options)

    @staticmethod
    def visit_node_html(self: sphinx.writers.html.HTMLTranslator, node):
        dia = Diagram(replace(Settings(), **node['options']))
        try:
            data = dia.from_dict(node['diagram'])
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
        'internal-alignment': lambda x: InternalAlignment[x.strip()],
        'character-advance': docutils.parsers.rst.directives.positive_int,
        'end-class': lambda x: EndClass[x.strip()],
    }

    def run(self):
        options = {k.replace('-', '_'): v for k, v in self.options.items()}

        if 'translate_half_pixel' in options:
            options['translate_half_pixel'] = True
        return [RailroadDiagramNode(self.get_content(), options)]

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
