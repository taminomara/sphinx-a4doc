from contrib.railroad_diagrams import *


if __name__ == '__main__':
    with open('out.html', 'w') as f:
        def add(name, diagram):
            f.write('<h1>{0}</h1>\n'.format(e(name)))
            Diagram(diagram).write_svg(f.write)
            f.write('\n')

        f.write('<!doctype html><title>Test</title><body>')
        add(
            'MODULE',
            Sequence(
                Optional(OneOrMore(Terminal('EOL')), True),
                Optional(
                    Sequence(
                        OneOrMore(NonTerminal('MODULE ITEM'), OneOrMore(Terminal('EOL'))),
                        Optional(OneOrMore(Terminal('EOL')), True)
                    )
                ),
                Terminal('EOF')
            )
        )
        add(
            'MODULE ITEM',
            Choice(
                0,
                NonTerminal('MODULE ANNOTATION'),
                NonTerminal('IMPORT'),
                NonTerminal('DOC'),
                NonTerminal('VERSION DECLARATION'),
                Sequence(
                    Optional(OneOrMore(Sequence(
                        NonTerminal('STATEMENT ANNOTATION'),
                        Optional(OneOrMore(Terminal('EOL')), True))
                    ), True),
                    Optional(
                        NonTerminal('VERSION DECLARATION'),
                        True
                    ),
                    Choice(
                        0,
                        NonTerminal('STRUCT'),
                        NonTerminal('ENUM')
                    ),
                )
            )
        )
        add(
            'MODULE ANNOTATION',
            Sequence(
                Terminal('#!['),
                NonTerminal('ANNOTATION CONTENT'),
                Terminal(']'),
            )
        ),
        add(
            'STATEMENT ANNOTATION',
            Sequence(
                Terminal('#['),
                NonTerminal('ANNOTATION CONTENT'),
                Terminal(']'),
            )
        )
        add(
            'ANNOTATION CONTENT',
            ZeroOrMore(
                Choice(
                    0,
                    Sequence(Terminal('ID')),
                    Sequence(Terminal('ID'), Terminal('='), Terminal('BOOL')),
                    Sequence(Terminal('ID'), Terminal('='), Terminal('INT')),
                    Sequence(Terminal('ID'), Terminal('='), Terminal('FLOAT')),
                    Sequence(Terminal('ID'), Terminal('='), Terminal('STRING')),
                    Sequence(Terminal('ID'), Terminal('('),
                             NonTerminal('ANNOTATION CONTENT'), Terminal(')')),
                ),
                Terminal(',')
            )
        )
        f.write('</body></html>')
