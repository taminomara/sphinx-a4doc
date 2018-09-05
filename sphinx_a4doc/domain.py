import re
import sphinx.addnodes
import sphinx.util.logging
import sphinx.util.nodes

from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.roles import XRefRole
from sphinx.locale import l_

from typing import *


WS_RE = re.compile(r'\s+', re.UNICODE)
ID_RE = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$', re.UNICODE)


logger = sphinx.util.logging.getLogger(__name__)


def check_imports_string(value):
    if value is None:
        return []
    result = value.split()
    for grammar in result:
        if ID_RE.match(grammar) is None:
            raise ValueError(f'invalid grammar name {grammar}')
    return result


def check_grammar_type(value):
    if value is None:
        return None
    value = value.lower()
    if value not in ['lexer', 'parser']:
        raise ValueError(f'invalid grammar type {value}')
    return value


class A4ObjectDescription(ObjectDescription):
    def handle_signature(self, sig, signode):
        if ID_RE.match(sig) is None:
            msg = f'entity name {sig!r} is invalid'
            self.state_machine.reporter.warning(msg, line=self.lineno)
            raise ValueError(msg)

        ann = self.objtype
        if self.objtype == 'grammar':
            grammar_type = self.options.get('type', '')
            if grammar_type:
                ann = grammar_type + ' ' + ann
        if self.options.get('name', ''):
            signode += sphinx.addnodes.desc_annotation(ann, ann)
            signode += sphinx.addnodes.desc_name(
                f' {self.options["name"]} ',
                f' {self.options["name"]} ',
            )
            signode += sphinx.addnodes.desc_annotation(
                f'({sig})',
                f'({sig})',
            )
        else:
            signode += sphinx.addnodes.desc_annotation(ann + ' ', ann + ' ')
            signode += sphinx.addnodes.desc_name(sig, sig)

        return sig

    def add_target_and_index(self, name, sig, signode):
        qualname = self.make_qualname(name)
        targetname = 'a4.' + qualname
        if targetname not in self.state.document.ids:
            signode['names'].append(targetname)
            signode['ids'].append(targetname)
            signode['first'] = not self.names
            self.state.document.note_explicit_target(signode)
            domaindata = self.env.domaindata['a4']
            inv = domaindata['objects']
            if qualname in inv:
                self.state_machine.reporter.warning(
                    'duplicate Antlr4 object description of %s, ' % name +
                    'other instance in ' + self.env.doc2path(inv[qualname][0]),
                    line=self.lineno)
            self.add_index(domaindata, qualname)

        grammar_type = self.options.get('type', '')
        if self.objtype == 'rule':
            indextext = f'{name} (Antlr4 production rule)'
        elif grammar_type:
            indextext = f'{name} (Antlr4 {grammar_type} grammar)'
        else:
            indextext = f'{name} (Antlr4 grammar)'
        if indextext:
            self.indexnode['entries'].append(
                ('single', indextext, targetname, '', None)
            )

    def add_index(self, domaindata, qualname):
        domaindata['objects'][qualname] = (self.env.docname, self.objtype)

    def before_content(self):
        if self.names:
            self.env.ref_context['a4:' + self.objtype] = self.names[0]

    def after_content(self):
        if self.names:
            self.env.ref_context.pop('a4:' + self.objtype)

    def make_qualname(self, name):
        return name


class Grammar(A4ObjectDescription):
    option_spec = dict(A4ObjectDescription.option_spec, **{
        'imports': check_imports_string,
        'type': check_grammar_type,
        'name': str.strip
    })

    def handle_signature(self, sig, signode):
        if 'a4:grammar' in self.env.ref_context:
            msg = 'defining nested grammars is not allowed'
            self.state_machine.reporter.warning(msg, line=self.lineno)
            raise ValueError(msg)

        return super().handle_signature(sig, signode)

    def add_index(self, domaindata, qualname):
        super().add_index(domaindata, qualname)
        domaindata['relations'][qualname] = self.options.get('imports', [])


class Rule(A4ObjectDescription):
    option_spec = dict(A4ObjectDescription.option_spec, **{
        'name': str.strip
    })

    def handle_signature(self, sig, signode):
        if 'a4:rule' in self.env.ref_context:
            msg = 'defining nested rules is not allowed'
            self.state_machine.reporter.warning(msg, line=self.lineno)
            raise ValueError(msg)

        return super().handle_signature(sig, signode)

    def make_qualname(self, name):
        grammar = self.env.ref_context.get('a4:grammar', '__default__')
        return grammar + '.' + name


class A4XRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['a4:grammar'] = env.ref_context.get('a4:grammar', '__default__')
        target = target.lstrip('~')
        if not has_explicit_title:
            if title[0:1] == '~':
                title = title[1:]
                dot = title.rfind('.')
                if dot != -1:
                    title = title[dot + 1:]
        return title, target


class A4Domain(Domain):
    name = 'a4'

    label = 'Antlr4'

    object_types = {
        'grammar': ObjType(l_('grammar'), 'grammar', 'g'),
        'rule': ObjType(l_('production rule'), 'rule', 'r'),
    }

    directives = {
        'grammar': Grammar,
        'rule': Rule,
    }

    roles = {
        'grammar': A4XRefRole(),
        'g': A4XRefRole(),
        'rule': A4XRefRole(),
        'r': A4XRefRole(),
    }

    initial_data: Dict[str, Dict[str, Tuple[str, Any]]] = {
        'objects': {},  # fullname -> docname, objtype
        'relations': {},  # fullname -> list of imported grammars
    }

    def clear_doc(self, docname):
        for fullname, (fn, objtype) in list(self.data['objects'].items()):
            if fn == docname:
                self.data['objects'].pop(fullname)
                self.data['relations'].pop(fullname, None)

    def merge_domaindata(self, docnames, otherdata):
        for fullname, (fn, objtype) in otherdata['objects'].items():
            if fn in docnames:
                self.data['objects'][fullname] = (fn, objtype)
                self.data['relations'][fullname] = otherdata['relations'][fullname]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if typ in ['grammar', 'g']:
            resolver = self.resolve_grammar
        elif typ in ['rule', 'r']:
            resolver = self.resolve_rule
        else:
            raise RuntimeError(f'unknown object type {typ}')

        return resolver(env, fromdocname, builder, target, node, contnode)

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        results = []

        as_grammar = self.resolve_grammar(env, fromdocname, builder, target, node, contnode)
        if as_grammar is not None:
            results.append(('a4:grammar', as_grammar))

        as_rule = self.resolve_rule(env, fromdocname, builder, target, node, contnode)
        if as_rule is not None:
            results.append(('a4:rule', as_rule))

        return results

    def resolve_grammar(self, env, fromdocname, builder, target, node, contnode):
        if target not in self.data['objects']:
            return None
        obj = self.data['objects'][target]
        if obj[1] != 'grammar':
            return None
        return sphinx.util.nodes.make_refnode(builder, fromdocname, obj[0], 'a4.' + target, contnode, target)

    def resolve_rule(self, env, fromdocname, builder, target, node, contnode):
        relations = self.data['relations']
        if '.' not in target:
            grammar, rule = node['a4:grammar'], target
            grammars = ['__default__', grammar]
        else:
            grammar, rule = target.rsplit('.', 1)
            grammars = [grammar]

        seen = set()
        while grammars:
            grammar = grammars.pop()
            if grammar in seen:
                continue
            seen.add(grammar)
            fullname = f'{grammar}.{rule}'
            if fullname not in self.data['objects']:
                if grammar in relations:
                    grammars.extend(relations[grammar])
                continue
            obj = self.data['objects'][fullname]
            if obj[1] != 'rule':
                return None
            return sphinx.util.nodes.make_refnode(builder, fromdocname, obj[0], 'a4.' + fullname, contnode, fullname)

        return None

    def get_objects(self):
        for refname, (docname, objtype) in list(self.data['objects'].items()):
            yield (refname, refname, objtype, docname, 'a4.' + refname, 1)
