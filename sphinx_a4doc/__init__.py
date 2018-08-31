import sphinx.application

from sphinx_a4doc.domain import A4Domain
from sphinx_a4doc.diagram_directive import RailroadDiagramNode, RailroadDiagram, LexerRuleDiagram, ParserRuleDiagram


def setup(app: sphinx.application.Sphinx):
    app.add_domain(A4Domain)

    app.add_node(RailroadDiagramNode,
                 html=(RailroadDiagramNode.visit_node_html,
                       RailroadDiagramNode.depart_node))

    app.add_directive('railroad-diagram', RailroadDiagram)
    app.add_directive('lexer-rule-diagram', LexerRuleDiagram)
    app.add_directive('parser-rule-diagram', ParserRuleDiagram)

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
