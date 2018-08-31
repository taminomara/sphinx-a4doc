import re
import io
import math

from dataclasses import dataclass, field
from enum import Enum

from typing import *

try:
    from typing.io import TextIO
except ImportError:
    from typing import TextIO


__all__ = [
    'e',
    'InternalAlignment',
    'EndClass',
    'Settings',
    'Diagram',
    'DEFAULT_SETTINGS',
]


T = TypeVar('T')


ESCAPE_RE = re.compile(r"[*_`\[\]<&]", re.UNICODE)


def e(text):
    return ESCAPE_RE.sub(lambda c: f'&#{ord(c[0])};', str(text))


def get_default_css():
    return {
        'path': {
            'stroke-width': 1,
            'stroke': 'black',
            'fill': 'none',
        },
        'text': {
            'font': '14px monospace',
            'text-anchor': 'middle',
            'alignment-baseline': 'central',
        },
        'rect': {
            'stroke-width': 1,
            'stroke': 'black',
            'fill': 'none',
        }
    }


class InternalAlignment(Enum):
    """
    Controls how to align nodes within a single railroad.

    """

    CENTER = 'CENTER'
    """
    Nodes are centered.
    
    Example:
    
    .. parser-rule-diagram:: (A B | C D E) (',' (A B | C D E))*
       :render.internal_alignment: CENTER
    
    """

    LEFT = 'LEFT'
    """
    Nodes are flushed to left in all cases.
    
    Example:
    
    .. parser-rule-diagram:: (A B | C D E) (',' (A B | C D E))*
       :render.internal_alignment: LEFT
    
    """

    RIGHT = 'RIGHT'
    """
    Nodes are flushed to right in all cases.
    
    Example:
    
    .. parser-rule-diagram:: (A B | C D E) (',' (A B | C D E))*
       :render.internal_alignment: RIGHT
    
    """

    AUTO_LEFT = 'AUTO_LEFT'
    """
    Nodes in choice groups are flushed left, all other nodes are centered.
    
    Example:
    
    .. parser-rule-diagram:: (A B | C D E) (',' (A B | C D E))*
       :render.internal_alignment: AUTO_LEFT
    
    """

    AUTO_RIGHT = 'AUTO_RIGHT'
    """
    Nodes in choice groups are flushed right, all other nodes are centered.
    
    Example:
    
    .. parser-rule-diagram:: (A B | C D E) (',' (A B | C D E))*
       :render.internal_alignment: AUTO_RIGHT
    
    """


class EndClass(Enum):
    """
    Controls how diagram start and end look like.

    """

    SIMPLE = 'SIMPLE'
    """
    A simple `T`-shaped ending.
    
    Example:
    
    .. parser-rule-diagram:: X
       :render.end_class: SIMPLE
    
    """

    COMPLEX = 'COMPLEX'
    """
    A `T`-shaped ending with vertical line doubled.
    
    Example:
    
    .. parser-rule-diagram:: X
       :render.end_class: COMPLEX

    """


@dataclass(frozen=True)
class Settings:
    padding: Tuple[int, int, int, int] = (1, 1, 1, 1)
    """Padding between diagram and root SVG component"""

    vertical_separation: int = 8
    """Space between railroads"""

    horizontal_separation: int = 10
    """Space between nodes"""

    arc_radius: int = 10
    """Radius for railroad arcs"""

    diagram_class: str = 'railroad-diagram'
    """CSS class that will be added to the top-level element"""

    translate_half_pixel: bool = False
    """Move diagram half pixel in both directions.
    Set to `True` if using odd pixel lengths for 'stroke'."""

    internal_alignment: InternalAlignment = InternalAlignment.AUTO_LEFT
    """How to align nodes within diagram"""

    character_advance: int = 8.4
    """Width of a single symbol in the monospace font"""

    end_class: EndClass = EndClass.SIMPLE
    """How diagram ends look like"""

    css: Dict[str, Dict[str, Any]] = field(default_factory=get_default_css)
    """CSS styles to embed into diagram"""


DEFAULT_SETTINGS = Settings()


@dataclass
class Diagram:
    settings: Settings = DEFAULT_SETTINGS
    """Settings used to render a diagram"""

    def element(self, name: str, **kwargs) -> 'Element':
        return Element(self, name, **kwargs)

    def path(self, x: int, y: int) -> 'Path':
        return Path(self, x, y)

    def style(self, css: Dict[str, Dict[str, Any]]) -> 'Style':
        return Style(self, css)

    def sequence(self, *items: 'DiagramItem') -> 'DiagramItem':
        return Sequence(self, list(items))

    def choice(self, *items: 'DiagramItem', default: int = 0):
        return Choice(self, default, list(items))

    def optional(self, item: 'DiagramItem', skip: bool = False) -> 'DiagramItem':
        return self.choice(self.skip(), item, default=0 if skip else 1)

    def one_or_more(self, item: 'DiagramItem', repeat: Optional['DiagramItem'] = None) -> 'DiagramItem':
        return OneOrMore(self, item, repeat)

    def zero_or_more(self, item: 'DiagramItem', repeat: Optional['DiagramItem'] = None) -> 'DiagramItem':
        return self.optional(self.one_or_more(item, repeat))

    def start(self) -> 'DiagramItem':
        return Start(self)

    def end(self) -> 'DiagramItem':
        return End(self)

    def node(self, text: str, href: Optional[str] = None, css_class: str = '', radius: int = 0, padding: int = 20) -> 'DiagramItem':
        return Node(self, text, href, css_class, radius, padding)

    def terminal(self, text: str, href: Optional[str] = None):
        return self.node(text, href, 'terminal', 10, 20)

    def non_terminal(self, text: str, href: Optional[str] = None):
        return self.node(text, href, 'non-terminal', 0, 20)

    def comment(self, text: str, href: Optional[str] = None):
        return self.node(text, href, 'comment', 0, 5)

    def skip(self) -> 'DiagramItem':
        return Skip(self)

    def from_dict(self, structure) -> 'DiagramItem':
        if isinstance(structure, str):
            return self.terminal(structure)

        if not isinstance(structure, dict):
            raise ValueError(f'node description should be string or object, '
                             f'got {type(structure)} instead')

        if 'type' not in structure:
            raise ValueError('required field "type" not found')

        structure = structure.copy()

        node_type = structure.pop('type')

        if not isinstance(node_type, str):
            raise ValueError('field "type" should be string')

        constructors = {
            'sequence': self.sequence,
            'choice': self.choice,
            'optional': self.optional,
            'one_or_more': self.one_or_more,
            'zero_or_more': self.zero_or_more,
            'node': self.node,
            'terminal': self.terminal,
            'non_terminal': self.non_terminal,
            'comment': self.comment,
            'skip': self.skip,
        }

        if node_type not in constructors:
            raise ValueError(f'unknown node type {node_type!r}')

        items = list(structure.pop('items', []))

        if not isinstance(items, (list, tuple)):
            raise ValueError('items field should be list')

        if not items and 'item' in structure:
            items.append(structure.pop('item'))
        elif 'item' in structure:
            raise ValueError('"items" and "item" keys are mutual exclusive')

        if node_type in ['optional', 'one_or_more', 'zero_or_more']:
            if len(items) > 1:
                raise ValueError(f'only one item allowed for node {node_type}')
            if len(items) == 0:
                raise ValueError(f'one item is mandatory for node {node_type}')
        elif node_type in ['node', 'terminal', 'non_terminal', 'comment', 'skip']:
            if len(items) > 0:
                raise ValueError(f'no items allowed for node {node_type}')

        items = [self.from_dict(it) for it in items]

        if node_type in ['one_or_more', 'zero_or_more']:
            if 'repeat' in structure and structure['repeat'] is not None:
                structure['repeat'] = self.from_dict(structure['repeat'])

        return constructors[node_type](*items, **structure)

    @overload
    def render(self, root: 'DiagramItem', output: None = None) -> str: ...

    @overload
    def render(self, root: 'DiagramItem', output: TextIO) -> None: ...

    def render(self, root, output=None):
        root = self.sequence(
            self.style(self.settings.css),
            self.start(),
            root,
            self.end()
        )

        # Root reference point
        x = self.settings.padding[3]
        y = self.settings.padding[2] + root.up

        # SVG dimensions
        width = self.settings.padding[1] + self.settings.padding[3] + root.width
        height = self.settings.padding[0] + self.settings.padding[2] + root.height + root.up + root.down

        svg = self.element('svg')
        svg.attrs['width'] = str(width)
        svg.attrs['height'] = str(height)
        svg.attrs['viewBox'] = f'0 0 {width} {height}'
        svg.attrs['class'] = self.settings.diagram_class
        svg = svg.format()

        g = self.element('g')
        if self.settings.translate_half_pixel:
            g.attrs['transform'] = 'translate(.5 .5)'
        g = g.format().add_to(svg)

        root.format(x, y, root.width, False, self.settings.internal_alignment).add_to(g)

        if output is None:
            output = io.StringIO()
            svg.write_svg(output)
            output.seek(0)
            return output.read()
        else:
            svg.write_svg(output)

    def __repr__(self):
        return super().__repr__()


@dataclass
class FormattedItem:
    diagram_item: 'DiagramItem'
    """Node that this element is formatted from"""

    children: List[Union['FormattedItem', str]] = field(default_factory=list)
    """Children SVG nodes"""

    def add_to(self, parent: 'FormattedItem') -> 'FormattedItem':
        parent.children.append(self)
        return self

    def write_svg(self, f: TextIO):
        f.write(f'<{self.diagram_item.name}')
        for name, value in sorted(self.diagram_item.attrs.items()):
            f.write(f' {name}="{e(value)}"')
        f.write('>')
        for child in self.children:
            if isinstance(child, FormattedItem):
                child.write_svg(f)
            else:
                f.write(e(child))
        f.write(f'</{self.diagram_item.name}>')


# TODO: make diagram items frozen

@dataclass
class DiagramItem:
    diagram: Diagram
    """Diagram that this item is attached to"""

    name: str
    """Name of SVG node"""

    width: int = 0
    """Total width of the item"""

    height: int = 0
    """Distance between the entry/exit lines"""

    up: int = 0
    """Distance it projects above the entry line"""

    down: int = 0
    """Distance it projects below the exit line"""

    attrs: Dict[str, str] = field(default_factory=dict)
    """SVG node attributes"""

    needs_space: bool = False
    """Add extra space around this element"""

    @property
    def settings(self) -> Settings:
        return self.diagram.settings

    @property
    def dia(self) -> Diagram:
        return self.diagram

    def format(self, x, y, width, reverse, alignment_override) -> FormattedItem:
        """
        Prepare the component for rendering, populate children array.

        - `x` and `y` determine the reference (top-left) point of the component.
        - `width` determine total width available for rendering the component.
        - `reverse` is true if the component should be mirrored along y axis.

        For normal rendering (the reference point is marked with `#`)::

            |<-----width----->|

                +---------+      ---
                |         |       up
            --->#-------\ |      ---        < y
                | /-----/ |       height
                | \-------|--->  ---
                |         |       down
                +---------+      ---

                ^
                x

        For reverse rendering (the reference point is marked with `#`)::

            |<-----width----->|

                +---------+      ---
                |         |       up
                # /-------|<---  ---        < y
                | \-----\ |       height
            <---|-------/ |      ---
                |         |       down
                +---------+      ---

                ^
                x

        """
        raise NotImplementedError()

    def determine_gaps(self, outer, internal_alignment):
        if internal_alignment == InternalAlignment.AUTO_LEFT:
            internal_alignment = InternalAlignment.LEFT
        elif internal_alignment == InternalAlignment.AUTO_RIGHT:
            internal_alignment = InternalAlignment.RIGHT
        diff = outer - self.width
        if internal_alignment == InternalAlignment.LEFT:
            return 0, diff
        elif internal_alignment == InternalAlignment.RIGHT:
            return diff, 0
        else:
            return diff / 2, diff / 2

    def alignment_override_center(self):
        if self.settings.internal_alignment == InternalAlignment.AUTO_RIGHT:
            return InternalAlignment.CENTER
        if self.settings.internal_alignment == InternalAlignment.AUTO_LEFT:
            return InternalAlignment.CENTER
        return self.settings.internal_alignment


@dataclass
class Element(DiagramItem):
    def format(self, *args, **kwargs):
        return FormattedItem(self)


@dataclass
class Path(DiagramItem):
    def __init__(self, dia: Diagram, x: int, y: int):
        super().__init__(dia, 'path')

        self.attrs = {'d': f'M{x} {y}'}

    def m(self, x, y):
        self.attrs['d'] += f'm{x} {y}'
        return self

    def h(self, val):
        self.attrs['d'] += f'h{val}'
        return self

    def right(self, val):
        return self.h(max(0, val))

    def left(self, val):
        return self.h(-max(0, val))

    def v(self, val):
        self.attrs['d'] += f'v{val}'
        return self

    def arc(self, sweep):
        arc_radius = self.settings.arc_radius

        x = arc_radius
        y = arc_radius
        if sweep[0] == 'e' or sweep[1] == 'w':
            x *= -1
        if sweep[0] == 's' or sweep[1] == 'n':
            y *= -1
        cw = 1 if sweep in ['ne', 'es', 'sw', 'wn'] else 0
        self.attrs['d'] += f'a{arc_radius} {arc_radius} 0 0 {cw} {x} {y}'
        return self

    def format(self, *args, **kwargs):
        return FormattedItem(self)


@dataclass
class Style(DiagramItem):
    @dataclass
    class StyleFormattedItem(FormattedItem):
        diagram_item: 'Style'

        def write_svg(self, f):
            # Write included stylesheet as CDATA.
            # See https://developer.mozilla.org/en-US/docs/Web/SVG/Element/style
            f.write('<style>/* <![CDATA[ */\n')
            for k, v in self.diagram_item.css.items():
                for cls in k.split(','):
                    f.write(f'svg.{self.diagram_item.settings.diagram_class} ')
                    f.write(cls.strip())
                    f.write(' ')
                f.write('{\n')
                for k2, v2 in v.items():
                    f.write(f'  {k2}: {v2};\n')
                f.write('}\n')
            f.write('\n/* ]]> */\n</style>')

    css: Dict[str, Dict[str, Any]] = None

    def __init__(self, dia: Diagram, css: Dict[str, Dict[str, Any]]):
        super().__init__(dia, 'style')

        self.css = css

    def format(self, *args, **kwargs):
        return self.StyleFormattedItem(self)


@dataclass
class Sequence(DiagramItem):
    items: List[DiagramItem] = None

    def __init__(self, dia: Diagram, items: List[DiagramItem]):
        super().__init__(dia, 'g')

        self.items = items
        self.needs_space = True

        for item in self.items:
            self.width += item.width
            if item.needs_space:
                self.width += self.settings.horizontal_separation * 2
            self.up = max(self.up, item.up - self.height)
            self.height += item.height
            self.down = max(self.down - item.height, item.down)
        if self.items[0].needs_space:
            self.width -= self.settings.horizontal_separation
        if self.items[-1].needs_space:
            self.width -= self.settings.horizontal_separation

        self.width = math.ceil(self.width)

    def format(self, x, y, width, reverse, alignment_override):
        fmt = FormattedItem(self)

        left_gap, right_gap = self.determine_gaps(width, alignment_override)

        alignment_override = self.alignment_override_center()

        # Input line y coordinate
        y_in = y
        # Output line y coordinate
        y_out = y + self.height

        if reverse:
            y_in, y_out = y_out, y_in

        self.dia.path(x, y_in) \
            .h(left_gap) \
            .format() \
            .add_to(fmt)
        self.dia.path(x + left_gap + self.width, y_out) \
            .h(right_gap) \
            .format() \
            .add_to(fmt)

        x += left_gap

        current_x = x
        current_y = y_in

        for i, item in enumerate(self.items[::-1 if reverse else 1]):
            if item.needs_space and i > 0:
                self.dia.path(current_x, current_y) \
                    .h(self.settings.horizontal_separation) \
                    .format() \
                    .add_to(fmt)
                current_x += self.settings.horizontal_separation

            if reverse:
                ref_x = current_x
                ref_y = current_y - item.height
            else:
                ref_x = current_x
                ref_y = current_y

            item.format(ref_x, ref_y, item.width, reverse, alignment_override) \
                .add_to(fmt)

            current_x += item.width

            if reverse:
                current_y -= item.height
            else:
                current_y += item.height

            if item.needs_space and i < len(self.items) - 1:
                self.dia.path(current_x, current_y) \
                    .h(self.settings.horizontal_separation) \
                    .format() \
                    .add_to(fmt)
                current_x += self.settings.horizontal_separation

        return fmt


@dataclass
class Choice(DiagramItem):
    def __init__(self, dia: Diagram, default: int, items: List[DiagramItem]):
        assert default < len(items)
        assert len(items) >= 1

        super().__init__(dia, 'g')

        self.default = default
        self.items = items

        self.width = max(item.width for item in self.items)
        self.width += self.settings.arc_radius * 4

        self.height = self.items[default].height

        #        +------+      - <- top border
        #     /-># 0    |      -
        #     |  |      |->\   -
        #     |  +------+  |   -
        #     |            |
        #     |  +------+  |   -
        #     /-># 1    |  |   -
        #     |  |      |->\   -
        #     |  +------+  |   -
        #     |            |
        #     |  +------+  |   -
        # ----+-># 2    |  |   - <- main line
        #     |  | def  |->+-  -
        #     |  +------+  |   -
        #     |            |
        #     |  +------+  |   -
        #     \-># 3    |  |   -
        #     |  |      |->/   -
        #     |  +------+  |   -
        #     |            |
        #     |  +------+  |   -
        #     \-># 4    |  |   -
        #        |      |->/   -
        #        +------+      -

        self.up += self.items[0].up

        # Reference points along y axis for each child, relative to top border
        child_refs = []

        for i, item in enumerate(self.items):
            if i in [default - 1, default + 1]:
                arcs = self.settings.arc_radius * 2
            else:
                arcs = self.settings.arc_radius

            if i < default:
                child_refs.append(self.up)
                up = self.items[i + 1].up + self.settings.vertical_separation + item.down
                up = max(arcs, up)
                up += item.height
                self.up += up
            elif i == default:
                child_refs.append(self.up)
            else:
                down = self.items[i - 1].down + self.settings.vertical_separation + item.up
                down = max(arcs, down)
                # woof... that's asymmetric =(
                child_refs.append(self.up + self.down + down + self.height)
                down += item.height
                self.down += down

        self.down += self.items[-1].down

        # Reference points along y axis for each child, relative to main line
        self.child_refs = [c - self.up for c in child_refs]

        self.width = math.ceil(self.width)

    def format(self, x, y, width, reverse, alignment_override):
        fmt = FormattedItem(self)

        left_gap, right_gap = self.determine_gaps(width, alignment_override)

        alignment_override = self.settings.internal_alignment

        # Input line y coordinate
        y_in = y
        # Output line y coordinate
        y_out = y + self.height

        if reverse:
            y_in, y_out = y_out, y_in

        self.dia.path(x, y_in) \
            .h(left_gap) \
            .format() \
            .add_to(fmt)
        self.dia.path(x + left_gap + self.width, y_out) \
            .h(right_gap) \
            .format() \
            .add_to(fmt)

        x += left_gap

        inner_width = self.width - self.settings.arc_radius * 4

        for i, (ref_y_rel, item) in enumerate(zip(self.child_refs, self.items)):
            # Input line of the component
            child_y_in = ref_y_rel + y
            # Output line of the component
            child_y_out = child_y_in + item.height
            # Reference point of the component
            ref_x = x + self.settings.arc_radius * 2
            ref_y = child_y_in

            if reverse:
                child_y_in, child_y_out = child_y_out, child_y_in

            if i == self.default:
                self.dia.path(x, y_in) \
                    .right(self.settings.arc_radius * 2) \
                    .format() \
                    .add_to(fmt)
                self.dia.path(ref_x + inner_width, y_out) \
                    .right(self.settings.arc_radius * 2) \
                    .format() \
                    .add_to(fmt)
            else:
                if i < self.default:
                    arcs = ['se', 'wn', 'ne', 'ws']
                    arcs_size = -self.settings.arc_radius * 2
                else:
                    arcs = ['ne', 'ws', 'se', 'wn']
                    arcs_size = self.settings.arc_radius * 2
                self.dia.path(x, y_in) \
                    .arc(arcs[0]) \
                    .v(child_y_in - y_in - arcs_size) \
                    .arc(arcs[1]) \
                    .format() \
                    .add_to(fmt)
                self.dia.path(ref_x + inner_width, child_y_out) \
                    .arc(arcs[2]) \
                    .v(y_out - child_y_out + arcs_size) \
                    .arc(arcs[3]) \
                    .format() \
                    .add_to(fmt)

            item.format(ref_x, ref_y, inner_width, reverse, alignment_override) \
                .add_to(fmt)

        return fmt


@dataclass
class OneOrMore(DiagramItem):
    item: DiagramItem = None
    repeat: DiagramItem = None

    def __init__(self, dia: Diagram, item: DiagramItem, repeat: Optional[DiagramItem]=None):
        super().__init__(dia, 'g')

        self.item = item
        self.repeat = repeat = repeat or self.dia.skip()

        self.needs_space = True

        self.width = max(item.width, repeat.width)
        self.width += self.settings.arc_radius * 2

        self.height = item.height

        self.up = item.up

        self.down = item.down + self.settings.vertical_separation + repeat.up
        self.down = max(self.settings.arc_radius * 2, self.down)
        self.down += repeat.height + repeat.down

        self.width = math.ceil(self.width)

    def format(self, x, y, width, reverse, alignment_override):
        fmt = FormattedItem(self)

        left_gap, right_gap = self.determine_gaps(width, alignment_override)

        alignment_override = self.alignment_override_center()

        inner_width = self.width - self.settings.arc_radius * 2

        #     +------+      -
        # -/->#      |      - <- input line of the main component    -------
        #  |  |      |->\-  - <- output line of the main component   ---  ^
        #  |  +------+  |   -                                         ^   |
        #  |            |                                       d_out=|   |=d_in
        #  |  +------+  |   -                                         v   |
        #  |  #      |<-/   - <- input line of the repeat component  ---  v
        #  \<-|      |      - <- output line of the repeat component -------
        #     +------+      -

        # Input line y coordinate
        y_in = y
        # Output line y coordinate
        y_out = y + self.height
        # Distance between input line of the main component
        # and output line of the repeat component
        d_in = self.height + self.down - self.repeat.down
        # Distance between output line of the main component
        # and input line of the repeat component
        d_out = self.down - self.repeat.down - self.repeat.height
        # Reference point of the main component
        main_ref_x = x + self.settings.arc_radius + left_gap
        main_ref_y = y
        # Reference point of the repeat component
        repeat_ref_x = x + self.settings.arc_radius + left_gap
        repeat_ref_y = y_out + d_out

        if reverse:
            y_in, y_out = y_out, y_in
            d_in, d_out = d_out, d_in
            # note that reference points are not changed

        self.dia.path(x, y_in) \
            .h(left_gap) \
            .format() \
            .add_to(fmt)
        self.dia.path(x + left_gap + self.width, y_out) \
            .h(right_gap) \
            .format() \
            .add_to(fmt)

        x += left_gap

        # Draw main item
        self.dia.path(x, y_in) \
            .right(self.settings.arc_radius) \
            .format() \
            .add_to(fmt)
        self.dia.path(x + self.width - self.settings.arc_radius, y_out) \
            .right(self.settings.arc_radius) \
            .format() \
            .add_to(fmt)
        self.item.format(main_ref_x, main_ref_y, inner_width, reverse, alignment_override) \
            .add_to(fmt)

        # Draw repeat item
        self.dia.path(x + self.settings.arc_radius, y_in) \
            .arc('nw') \
            .v(d_in - 2 * self.settings.arc_radius) \
            .arc('ws') \
            .format() \
            .add_to(fmt)
        self.dia.path(x + self.width - self.settings.arc_radius, y_out) \
            .arc('ne') \
            .v(d_out - 2 * self.settings.arc_radius) \
            .arc('es') \
            .format() \
            .add_to(fmt)
        self.repeat.format(repeat_ref_x, repeat_ref_y, inner_width, not reverse, alignment_override) \
            .add_to(fmt)

        return fmt


@dataclass
class Start(DiagramItem):
    end_class: EndClass = None

    def __init__(self, dia: Diagram, end_class: Optional[EndClass] = None):
        super().__init__(dia, 'g')

        self.end_class = end_class or self.settings.end_class

        self.width = 20
        self.up = 10
        self.down = 10

    def format(self, x, y, width, reverse, alignment_override):
        path = self.dia.path(x, y)

        path.h(20)

        if self.end_class == EndClass.SIMPLE:
            path.m(-20, -10).v(20)
        else:
            path.m(-10, -10).v(20)
            path.m(-10, -20).v(20)

        return path.format()


@dataclass
class End(DiagramItem):
    end_class: EndClass = None

    def __init__(self, dia: Diagram, end_class: Optional[EndClass] = None):
        super().__init__(dia, 'g')

        self.end_class = end_class or self.settings.end_class

        self.width = 20
        self.up = 10
        self.down = 10

    def format(self, x, y, width, reverse, alignment_override):
        path = self.dia.path(x, y)

        path.h(20)

        if self.end_class == EndClass.SIMPLE:
            path.m(0, -10).v(20)
        else:
            path.m(0, -10).v(20)
            path.m(-10, -20).v(20)

        return path.format()


@dataclass
class Node(DiagramItem):
    text: str = None
    href: Optional[str] = None
    radius: int = None

    def __init__(self, dia: Diagram, text, href=None, css_class='', radius=0, padding=20):
        super().__init__(dia, 'g')

        self.text = text
        self.href = href
        self.radius = radius

        self.attrs = {'class': css_class}
        self.needs_space = True
        self.up = 11
        self.down = 11

        self.width = len(text) * self.settings.character_advance + padding

        self.width = math.ceil(self.width)

    def format(self, x, y, width, reverse, alignment_override):
        fmt = FormattedItem(self)

        left_gap, right_gap = self.determine_gaps(width, alignment_override)

        self.dia.path(x, y).h(left_gap).format().add_to(fmt)
        self.dia.path(x + left_gap + self.width, y).h(right_gap).format().add_to(fmt)

        rect_attrs = {
            'x': x + left_gap,
            'y': y - self.up,
            'width': self.width,
            'height': self.up + self.down,
            'rx': self.radius,
            'ry': self.radius
        }

        self.dia.element('rect', attrs=rect_attrs).format().add_to(fmt)

        text_attrs = {
            'x': x + left_gap + self.width / 2,
            'y': y
        }

        text = self.dia.element('text', attrs=text_attrs).format()
        text.children.append(self.text)

        if self.href is not None:
            a = self.dia.element('a', attrs={'xlink:href': self.href}).format()
            a.children.append(text)
            a.add_to(fmt)
            text.add_to(a)
        else:
            text.add_to(fmt)

        return fmt


@dataclass
class Skip(DiagramItem):
    def __init__(self, dia: Diagram):
        super().__init__(dia, 'g')

    def format(self, x, y, width, reverse, alignment_override):
        return self.dia.path(x, y).right(width).format()
