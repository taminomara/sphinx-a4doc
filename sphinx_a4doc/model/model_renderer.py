from dataclasses import dataclass
from enum import Enum

from typing import *

from sphinx_a4doc.model.model import RuleBase, LexerRule, ParserRule
from sphinx_a4doc.model.visitor import *


class ImportanceProvider(CachedRuleContentVisitor[int]):
    """
    Given a rule content item, returns True if this item is important.

    """

    def visit_literal(self, r: LexerRule.Literal) -> int:
        return 1

    def visit_range(self, r: LexerRule.Range) -> int:
        return 1

    def visit_charset(self, r: LexerRule.CharSet) -> int:
        return 1

    def visit_reference(self, r: RuleBase.Reference) -> int:
        rule = r.get_reference()
        if rule is None:
            return 1
        else:
            return rule.importance

    def visit_wildcard(self, r: RuleBase.Wildcard) -> int:
        return 1

    def visit_negation(self, r: RuleBase.Negation) -> int:
        return self.visit(r.child)

    def visit_zero_plus(self, r: RuleBase.ZeroPlus) -> int:
        return self.visit(r.child)

    def visit_one_plus(self, r: RuleBase.OnePlus) -> int:
        return self.visit(r.child)

    def visit_maybe(self, r: RuleBase.Maybe) -> int:
        return self.visit(r.child)

    def visit_sequence(self, r: RuleBase.Sequence) -> int:
        return max(self.visit(c) for c in r.children)

    def visit_alternative(self, r: RuleBase.Alternative) -> int:
        return max(self.visit(c) for c in r.children)


class HrefProvider:
    """
    Giver a rule provides href to the rule's documentation.

    """

    default_href: Optional[str] = None

    def get_href(self, _: RuleBase) -> Optional[str]:
        return self.default_href


class LiteralNaming(Enum):
    FORCE_LITERAL = 'FORCE_LITERAL'
    FORCE_NAME = 'FORCE_NAME'
    DO_NOT_FORCE = 'DO_NOT_FORCE'


@dataclass(frozen=True)
class StyleProvider:
    """
    Provides all settings for svg rendering.

    """

    literal_naming: LiteralNaming = LiteralNaming.FORCE_LITERAL

    # The following variables control properties for individual diagram node.
    # Tuple items are (css_class, border_radius, horizontal_padding):
    T = Tuple[str, int, int]

    literal: T = ('node lexer literal', 10, 20)
    range: T = ('node lexer range', 10, 20)
    charset: T = ('node lexer charset', 10, 20)
    wildcard: T = ('node lexer wildcard', 10, 20)
    negation: T = ('node lexer negation', 10, 20)

    important_terminal: T = ('node lexer terminal important', 10, 20)
    unimportant_terminal: T = ('node lexer terminal unimportant', 10, 20)
    unresolved_terminal: T = ('node lexer terminal unresolved', 10, 20)

    important_non_terminal: T = ('node lexer non-terminal important', 0, 20)
    unimportant_non_terminal: T = ('node lexer non-terminal unimportant', 0, 20)
    unresolved_non_terminal: T = ('node lexer non-terminal unresolved', 0, 20)

    def get_literal(self, _: LexerRule.Literal) -> T:
        return self.literal

    def get_range(self, _: LexerRule.Range) -> T:
        return self.range

    def get_charset(self, _: LexerRule.CharSet) -> T:
        return self.charset

    def get_wildcard(self, _: RuleBase.Wildcard) -> T:
        return self.wildcard

    def get_wildcard_text(self, _: RuleBase.Wildcard) -> str:
        return '.'

    def get_negation(self, _: RuleBase.Negation) -> T:
        return self.negation

    def get_terminal(self, r: LexerRule) -> T:
        if r.importance:
            return self.important_terminal
        else:
            return self.unimportant_terminal

    def get_non_terminal(self, r: ParserRule) -> T:
        if r.importance:
            return self.important_non_terminal
        else:
            return self.unimportant_non_terminal

    def get_unresolved_terminal(self) -> T:
        return self.unresolved_terminal

    def get_unresolved_non_terminal(self) -> T:
        return self.unresolved_non_terminal


class Renderer(CachedRuleContentVisitor[dict]):
    def __init__(
        self,
        importance_provider: ImportanceProvider = ImportanceProvider(),
        href_provider: HrefProvider = HrefProvider(),
        style_provider: StyleProvider = StyleProvider()
    ):
        super().__init__()

        self.importance_provider = importance_provider
        self.href_provider = href_provider

        self.style_provider = style_provider

    @staticmethod
    def _sequence(*items):
        return dict(type='sequence', items=items, autowrap=True)

    @staticmethod
    def _stack(*items):
        return dict(type='stack', items=items)

    @staticmethod
    def _choice(*items, default: int = 0):
        return dict(type='choice', items=items, default=default)

    @staticmethod
    def _optional(item, skip: bool = False):
        return dict(type='optional', item=item, skip=skip)

    @staticmethod
    def _one_or_more(item, repeat=None):
        return dict(type='one_or_more', item=item, repeat=repeat)

    @staticmethod
    def _zero_or_more(item, repeat=None):
        return dict(type='zero_or_more', item=item, repeat=repeat)

    @staticmethod
    def _node(text: str, href: Optional[str]=None, css_class: str= '', radius: int=0, padding: int=20):
        return dict(type='node', text=text, href=href, css_class=css_class, radius=radius, padding=padding)

    @staticmethod
    def _terminal(text: str, href: Optional[str]=None):
        return dict(type='terminal', text=text, href=href)

    @staticmethod
    def _non_terminal(text: str, href: Optional[str]=None):
        return dict(type='non_terminal', text=text, href=href)

    @staticmethod
    def _comment(text: str, href: Optional[str]=None):
        return dict(type='comment', text=text, href=href)

    @staticmethod
    def _skip():
        return dict(type='skip')

    def visit_literal(self, r: LexerRule.Literal):
        css, radius, padding = self.style_provider.get_literal(r)
        return self._node(r.content, None, css, radius, padding)

    def visit_range(self, r: LexerRule.Range):
        css, radius, padding = self.style_provider.get_range(r)
        return self._node(f'{r.start}..{r.end}', None, css, radius, padding)

    def visit_charset(self, r: LexerRule.CharSet):
        css, radius, padding = self.style_provider.get_charset(r)
        return self._node(r.content, None, css, radius, padding)

    def visit_reference(self, r: RuleBase.Reference):
        rule = r.get_reference()
        if rule is None:
            if r.name[0].isupper() or r.name[0] == "'":
                css, radius, padding = self.style_provider.get_unresolved_terminal()
            else:
                css, radius, padding = self.style_provider.get_unresolved_non_terminal()
            return self._node(r.name, None, css, radius, padding)
        elif rule.is_doxygen_inline:
            return self.visit(rule.content)
        elif isinstance(rule, LexerRule):
            literal_naming = self.style_provider.literal_naming
            if not rule.is_literal:
                name = rule.display_name or rule.name
            elif literal_naming == LiteralNaming.FORCE_LITERAL:
                name = str(rule.content)
            elif literal_naming == LiteralNaming.FORCE_NAME:
                name = rule.display_name or rule.name
            else:
                name = r.name
            css, radius, padding = self.style_provider.get_terminal(rule)
            href = self.href_provider.get_href(rule)
            return self._node(name, href, css, radius, padding)
        elif isinstance(rule, ParserRule):
            name = rule.display_name or rule.name
            css, radius, padding = self.style_provider.get_non_terminal(rule)
            href = self.href_provider.get_href(rule)
            return self._node(name, href, css, radius, padding)
        else:
            assert False

    def visit_wildcard(self, r: RuleBase.Wildcard):
        css, radius, padding = self.style_provider.get_wildcard(r)
        text = self.style_provider.get_wildcard_text(r)
        return self._node(text, None, css, radius, padding)

    def visit_negation(self, r: RuleBase.Negation):
        css, radius, padding = self.style_provider.get_negation(r)
        return self._node(str(r), None, css, radius, padding)

    def visit_zero_plus(self, r: RuleBase.ZeroPlus):
        skip = not self.importance_provider.visit(r.child)
        return self._optional(self._one_or_more(self.visit(r.child)), skip=skip)

    def visit_one_plus(self, r: RuleBase.OnePlus):
        return self._one_or_more(self.visit(r.child))

    def visit_maybe(self, r: RuleBase.Maybe):
        if (
            isinstance(r.child, RuleBase.Alternative) and
            len(r.child.children) == 2 and
            self.importance_provider.visit(r.child.children[0]) ==
            self.importance_provider.visit(r.child.children[1])
        ):
            return self._choice(
                self.visit(r.child.children[0]),
                self._skip(),
                self.visit(r.child.children[1]),
                default=1,
            )

        skip = not self.importance_provider.visit(r.child)
        return self._optional(self.visit(r.child), skip=skip)

    def visit_sequence(self, r: RuleBase.Sequence):
        return self._optimize_sequence(list(r.children))

    def visit_alternative(self, r: RuleBase.Alternative):
        default = max(enumerate(r.children),
                      key=lambda x: self.importance_provider.visit(x[1]))[0]
        return self._choice(*[self.visit(c) for c in r.children], default=default)

    def _optimize_sequence(self, seq: List[RuleBase.RuleContent]):
        # We are trying to find a sub-sequence of form `x y z (A B x y z)*`
        # and replace it with a single 'OneOrMore(Seq(x, y, z), Seq(A, B))'.
        for i in range(len(seq) - 1, -1, -1):
            # Our ZeroPlus rule with a sequence inside:
            star = seq[i]

            if not isinstance(star, RuleBase.ZeroPlus):
                continue
            if not isinstance(star.child, RuleBase.Sequence):
                continue

            nested_seq = list(star.child.children)

            for j in range(len(nested_seq) - 1, -1, -1):
                k = i + j - len(nested_seq)
                if k < 0 or seq[k] != nested_seq[j]:
                    # Index of the seq after which our sub-sequence start
                    # (e.g. 0 if the first element of our sub-sequence
                    # is the first element of the sequence):
                    seq_start = k + 1
                    # Index of the nested_seq which splits main part
                    # and the repeat part (e.g. for [A, B, x, y, z]
                    # the index is 2):
                    nested_seq_start = j + 1
                    break
            else:
                seq_start = i - len(nested_seq)
                nested_seq_start = 0

            if seq_start == i:
                # matched no elements from the nested sequence
                continue

            repeat = self._optimize_sequence(nested_seq[:nested_seq_start])
            main = self._optimize_sequence(nested_seq[nested_seq_start:])

            item = self._one_or_more(main, repeat)

            seq[seq_start:i + 1] = [item]

            return self._optimize_sequence(seq)

        return self._sequence(*[
            e if isinstance(e, dict) else self.visit(e) for e in seq
        ])
