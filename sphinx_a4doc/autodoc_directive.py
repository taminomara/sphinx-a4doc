import os

import docutils.nodes
import docutils.parsers.rst
import docutils.statemachine
import sphinx.addnodes
import sphinx.util.docutils
import sphinx.util.logging
import docutils.parsers.rst.directives

from sphinx_a4doc.model.model import ModelCache, Model, RuleBase
from sphinx_a4doc.model.model_renderer import Renderer
from sphinx_a4doc.model.visitor import RuleContentVisitor
from sphinx_a4doc.diagram_directive import RailroadDiagramNode

from sphinx_a4doc.domain import Grammar, Rule

from typing import *

logger = sphinx.util.logging.getLogger(__name__)


class A4Autogrammar(docutils.parsers.rst.Directive):
    required_arguments = 1
    has_content = True
    option_spec = {
        'only-reachable-from': str,
        'name': str.strip,
        'no-lexer-rules': docutils.parsers.rst.directives.flag,
        'add-lexer-rules': docutils.parsers.rst.directives.flag,
        'no-parser-rules': docutils.parsers.rst.directives.flag,
        'add-parser-rules': docutils.parsers.rst.directives.flag,
        'no-fragments': docutils.parsers.rst.directives.flag,
        'add-fragments': docutils.parsers.rst.directives.flag,
        'no-undocumented': docutils.parsers.rst.directives.flag,
        'add-undocumented': docutils.parsers.rst.directives.flag,
        'ordering': lambda v: docutils.parsers.rst.directives.choice(
            v, ['by-source', 'by-name']),
        'grouping': lambda v: docutils.parsers.rst.directives.choice(
            v, ['mixed', 'lexer-first', 'parser-first']),
    }

    def load_model(self, name: str) -> Model:
        # TODO: use grammar resolver
        env = self.state.document.settings.env
        base_path = env.config.a4_base_path
        path = os.path.join(base_path, name + '.g4')

        return ModelCache.instance().from_file(path)

    def run(self):
        model = self.load_model(self.arguments[0])

        grammar_dir = Grammar(
            name='a4:grammar',
            arguments=[model.get_name()],
            options={
                'imports': [
                    i.get_name() for i in model.get_imports()
                    if i.get_name() is not None
                ],
                'type': model.get_type(),
                'name': self.options.get('name')
            },
            content=self.content,
            lineno=self.lineno,
            content_offset=self.content_offset,
            block_text=self.block_text,
            state=self.state,
            state_machine=self.state_machine
        )

        nodes = grammar_dir.run()

        # TODO: need model.has_errors()
        if model.get_name() is None:  # parsing error
            return nodes

        desc_content = None

        rule_nodes = {}

        for node in nodes:
            if not isinstance(node, sphinx.addnodes.desc):
                continue

            for content_node in node.children:
                if isinstance(content_node, sphinx.addnodes.desc_content):
                    desc_content = content_node
                    break
            else:
                raise RuntimeError('no desc_content can be found')
            for rule_node in node.traverse(
                lambda x: (
                    isinstance(x, sphinx.addnodes.desc) and
                    x['domain'] == 'a4' and
                    x['objtype'] == 'rule'
                )
            ):
                sig = rule_node.next_node(sphinx.addnodes.desc_signature)

                if sig is None:
                    continue

                prefix = f'a4.{model.get_name()}.'

                for ident in sig['ids']:
                    if ident.startswith(prefix):
                        rule_nodes[ident[len(prefix):]] = rule_node
                        rule_node.replace_self([])
                        break

        assert desc_content is not None

        grammar_dir.before_content()
        try:
            self.render_docs(
                model.get_path(), model.get_model_docs(), desc_content)

            for rule in self.make_order(model):
                if rule.name in rule_nodes:
                    desc_content.append(rule_nodes.pop(rule.name))
                else:
                    desc_content.extend(self.make_rule(rule))
            for rule in sorted(rule_nodes.values(), key=lambda x: x.line):
                desc_content.append(rule)
        finally:
            grammar_dir.after_content()

        return nodes

    def make_order(self, model: Model) -> List[RuleBase]:
        need_lexer_rules = True
        if 'no-lexer-rules' in self.options:
            need_lexer_rules = False
        if 'add-lexer-rules' in self.options:
            need_lexer_rules = True

        need_parser_rules = True
        if 'no-parser-rules' in self.options:
            need_parser_rules = False
        if 'add-parser-rules' in self.options:
            need_parser_rules = True

        need_fragments = False
        if 'no-fragments' in self.options:
            need_fragments = False
        if 'add-fragments' in self.options:
            need_fragments = True

        need_undocumented = False
        if 'no-undocumented' in self.options:
            need_undocumented = False
        if 'add-undocumented' in self.options:
            need_undocumented = True

        lexer_rules = []
        if need_lexer_rules:
            lexer_rules = model.get_terminals()
            if not need_fragments:
                lexer_rules = filter(lambda r: not r.is_fragment, lexer_rules)
            if not need_undocumented:
                lexer_rules = filter(lambda r: r.documentation, lexer_rules)
        lexer_rules = list(lexer_rules)

        parser_rules = []
        if need_parser_rules:
            parser_rules = model.get_non_terminals()
            if not need_undocumented:
                parser_rules = filter(lambda r: r.documentation, parser_rules)
        parser_rules = list(parser_rules)

        ordering = self.options.get('ordering', 'by-source')
        precedence = {
            'by-source': lambda rule: rule.position,
            'by-name': lambda rule: rule.name.lower(),
        }[ordering]

        grouping = self.options.get('grouping', 'mixed')
        if grouping == 'mixed':
            all_rules = sorted(lexer_rules + parser_rules, key=precedence)
        elif grouping == 'lexer-first':
            all_rules = sorted(lexer_rules, key=precedence) + sorted(parser_rules, key=precedence)
        elif grouping == 'parser-first':
            all_rules = sorted(parser_rules, key=precedence) + sorted(lexer_rules, key=precedence)
        else:
            raise RuntimeError('invalid grouping parameter')

        if 'only-reachable-from' in self.options:
            rule_name = self.options['only-reachable-from']
            rule_model = model
            if '.' in rule_name:
                model_name, rule_name = rule_name.split('.', 1)
                rule_model = self.load_model(model_name)
            rule = rule_model.lookup(rule_name)
            if rule is None:
                return all_rules
            reachable = {rule} | ReachableFiner().visit(rule.content)
            return [r for r in all_rules if r in reachable]

        return all_rules

    def make_rule(self, rule: RuleBase) -> List[docutils.nodes.Node]:
        if rule.is_doxygen_nodoc or rule.is_doxygen_inline:
            return []  # implicitly disabled
        if not rule.documentation and rule.content is None:
            return []  # nothing to document

        rule_dir = Rule(
            name='a4:rule',
            arguments=[rule.name],
            options={
                'name': rule.display_name
            },
            content=docutils.statemachine.StringList(),
            lineno=self.lineno,
            content_offset=self.content_offset,
            block_text=self.block_text,
            state=self.state,
            state_machine=self.state_machine
        )

        nodes = rule_dir.run()

        for node in nodes:
            if not isinstance(node, sphinx.addnodes.desc):
                continue

            for content_node in node.children:
                if isinstance(content_node, sphinx.addnodes.desc_content):
                    desc_content = content_node
                    break
            else:
                raise RuntimeError('no desc_content can be found')

            if rule.documentation:
                self.render_docs(rule.position.file, rule.documentation[:1],
                                 desc_content)
                docs = rule.documentation[1:]
            else:
                docs = rule.documentation

            if (
                not rule.is_doxygen_no_diagram and
                node.next_node(RailroadDiagramNode) is None
            ):
                env = self.state.document.settings.env
                grammar = env.ref_context.get('a4:grammar', '__default__')
                dia = Renderer().visit(rule.content)
                desc_content.append(RailroadDiagramNode(dia, {}, grammar))

            self.render_docs(rule.position.file, docs, desc_content)

            break

        return nodes

    def render_docs(self, path: str, docs: List[Tuple[int, str]], node):
        docs = docs or []

        for line, doc in docs:
            lines = doc.splitlines()
            items = [(path, line + i - 1) for i in range(len(lines))]

            content = docutils.statemachine.StringList(lines, items=items)

            with sphinx.util.docutils.switch_source_input(self.state, content):
                self.state.nested_parse(content, 0, node)


class ReachableFiner(RuleContentVisitor[Set[RuleBase]]):
    def __init__(self):
        self._seen = set()

    def visit_literal(self, r) -> Set[RuleBase]:
        return set()

    def visit_range(self, r) -> Set[RuleBase]:
        return set()

    def visit_charset(self, r) -> Set[RuleBase]:
        return set()

    def visit_reference(self, r: RuleBase.Reference) -> Set[RuleBase]:
        ref = r.get_reference()
        if ref is None:
            return set()
        elif ref in self._seen:
            return set()
        else:
            self._seen.add(ref)
            return {ref} | self.visit(ref.content)

    def visit_wildcard(self, r: RuleBase.Wildcard) -> Set[RuleBase]:
        return set()

    def visit_negation(self, r: RuleBase.Negation) -> Set[RuleBase]:
        return self.visit(r.child)

    def visit_zero_plus(self, r: RuleBase.ZeroPlus) -> Set[RuleBase]:
        return self.visit(r.child)

    def visit_one_plus(self, r: RuleBase.OnePlus) -> Set[RuleBase]:
        return self.visit(r.child)

    def visit_maybe(self, r: RuleBase.Maybe) -> Set[RuleBase]:
        return self.visit(r.child)

    def visit_sequence(self, r: RuleBase.Sequence) -> Set[RuleBase]:
        return set().union(*[self.visit(c) for c in r.children])

    def visit_alternative(self, r: RuleBase.Alternative) -> Set[RuleBase]:
        return set().union(*[self.visit(c) for c in r.children])
