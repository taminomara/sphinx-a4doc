import dataclasses
import textwrap

import sphinx.util.docfields
from docutils.parsers.rst.languages import en
import docutils.statemachine
import docutils.nodes
import sphinx.util.docutils
import sphinx.ext.autodoc
import sphinx.errors
import sphinx.domains.rst
import sphinx.addnodes
import sphinx.application

from sphinx.locale import _
from sphinx.pycode import ModuleAnalyzer

from .configurator import Namespace, NamespaceHolder, ManagedDirective, make_converter

from typing import *


@dataclasses.dataclass
class AutoDirectiveSettings:
    options: bool = True
    """
    Generate documentation for directive options.
    
    """

    prefixed_options: bool = False
    """
    Generate documentation for directive options with non-empty prefix.
    
    """

    prefix_filter: Optional[List[str]] = None
    """
    Filter options documentation by option prefix.
    
    """


namespace = Namespace('configurator', AutoDirectiveSettings)


class AutoDirective(sphinx.domains.rst.ReSTDirective, ManagedDirective):
    """
    Generates documentation for rst directives, including documentation for
    its options.

    """

    settings = namespace.for_directive()

    def run(self):
        self.name = 'rst:directive'

        nodes = super().run()

        try:
            directive = self.load_directive()
        except sphinx.errors.ExtensionError as e:
            return [
                self.state_machine.reporter.error(
                    str(e),
                    line=self.content_offset
                )
            ]

        if not issubclass(directive, ManagedDirective):
            return [
                self.state_machine.reporter.error(
                    'cannot autodocument a directive that is not derived '
                    'from ManagedDirective',
                    line=self.content_offset
                )
            ]

        if not issubclass(directive, sphinx.util.docutils.SphinxDirective):
            return [
                self.state_machine.reporter.error(
                    'cannot autodocument a directive that is not derived '
                    'from SphinxDirective',
                    line=self.content_offset
                )
            ]

        for node in nodes:
            if isinstance(node, sphinx.addnodes.desc):
                for content_node in node.children:
                    if isinstance(content_node, sphinx.addnodes.desc_content):
                        self.render_directive(directive, content_node)
                        return nodes
                else:
                    raise RuntimeError('no desc_content node can be found')
        else:
            raise RuntimeError('no desc node can be found')

    def load_directive(self):
        if len(self.names) < 1:
            raise sphinx.errors.ExtensionError(
                'should provide at least one signature'
            )

        directive_name = self.names[0]
        if ':' in directive_name:
            domain_name, directive_name = directive_name.split(':', 1)

            if domain_name not in self.env.domains:
                raise sphinx.errors.ExtensionError(
                    f'unknown domain {domain_name!r}'
                )

            domain = self.env.domains[domain_name]

            if directive_name not in domain.directives:
                raise sphinx.errors.ExtensionError(
                    f'unknown directive {directive_name!r} '
                    f'within domain {domain_name!r}'
                )

            return domain.directives[directive_name]
        else:
            directive, messages = sphinx.util.docutils.directives.directive(
                directive_name,
                en,
                self.state.document
            )

            if directive is None:
                raise sphinx.errors.ExtensionError(
                    f'unknown directive {directive_name!r}'
                )

            return directive

    def render_directive(self, directive, nodes):
        if getattr(directive, '__doc__', None):
            doc = self.canonize_docstring(directive.__doc__)
            lines = docutils.statemachine.StringList(doc.splitlines())
            self.state.nested_parse(lines, self.content_offset, nodes)

        if not self.settings.options:
            return

        holders: Set[NamespaceHolder] = getattr(
            directive,
            '_namespace_attrs_',
            set()
        )

        options: List[Tuple[str, Any, List[dataclasses.Field]]] = []

        for holder in holders:
            if holder.prefix:
                if not self.settings.prefixed_options:
                    continue
                if (self.settings.prefix_filter is not None and
                        holder.prefix not in self.settings.prefix_filter):
                    continue
                prefix = holder.prefix
            else:
                prefix = ''

            fields = holder.namespace.fields()
            cls = holder.namespace.get_cls()

            if fields:
                options.append((prefix, cls, fields))

        if not options:
            return

        p = docutils.nodes.paragraph('', '')
        p += docutils.nodes.strong('Options:', _('Options:'))
        nodes += p

        for p, cls, fields in sorted(options, key=lambda x: x[0]):
            fields = [
                (self.resolve_arg_doc_and_index(field.name, cls), field)
                for field in fields
            ]
            for (i, doc), field in sorted(fields):
                if p:
                    p += '-'

                name = field.name.replace('_', '-')
                names = [p + name]
                if 'converter' in field.metadata:
                    value_desc = str(field.metadata['converter'])
                elif field.type is bool:
                    value_desc = ''
                    names.append(p + 'no-' + name)
                else:
                    value_desc = str(make_converter(field.type))

                nodes += self.render_option(names, value_desc, doc)

    def render_option(self, names, value_desc, doc):
        node = sphinx.addnodes.desc()
        node['domain'] = 'rst'
        node['objtype'] = node['desctype'] = 'option'
        node['noindex'] = True

        for i, name in enumerate(names):
            sig = f':{name}: '
            signode = sphinx.addnodes.desc_signature(sig, '')
            signode['first'] = i == 0
            signode += sphinx.addnodes.desc_name(sig, sig)
            signode += sphinx.addnodes.desc_addname(value_desc, value_desc)

            node.append(signode)

        contentnode = sphinx.addnodes.desc_content()
        node.append(contentnode)

        if names:
            # needed for association of version{added,changed} directives
            self.env.temp_data['object'] = names
        self.before_content()
        lines = docutils.statemachine.StringList(doc.splitlines())
        self.state.nested_parse(lines, self.content_offset, contentnode)
        sphinx.util.docfields.DocFieldTransformer(self).transform_all(contentnode)
        self.env.temp_data['object'] = None
        self.after_content()

        return node

    @staticmethod
    def canonize_docstring(description):
        if description is None:
            return description

        lines = description.split('\n')
        lines = list(map(str.rstrip, lines))

        # Handle trivial cases:
        if len(lines) <= 1:
            return '\n'.join(lines) + '\n\n'

        # Ensure there is a blank line at the end of description:
        if lines[-1]:
            lines.append('')

        # The first line is a line that follows immediately after the triple quote.
        # We need to dedent the other lines but we don't need to dedent
        # the first one.
        body = lines[0] + '\n' + textwrap.dedent('\n'.join(lines[1:]))

        # Remove any leading newlines and ensure that
        # there is only one trailing newline.
        body = body.strip('\n') + '\n\n'

        return body

    @classmethod
    def resolve_arg_doc_and_index(cls, name, dataclass: type) -> Tuple[Tuple[int, int], str]:
        for i, base in enumerate(dataclass.__mro__):
            analyzer = ModuleAnalyzer.for_module(base.__module__)
            docs = analyzer.find_attr_docs()
            if (dataclass.__name__, name) in docs:
                tag = analyzer.tagorder[f'{dataclass.__name__}.{name}']
                return (i, tag), cls.canonize_docstring(
                    '\n'.join(docs[dataclass.__name__, name])
                )
        return (1000, 1000), ''


def setup(app: sphinx.application.Sphinx):
    namespace.register_settings(app)
    app.add_directive_to_domain('rst', 'autodirective', AutoDirective)
