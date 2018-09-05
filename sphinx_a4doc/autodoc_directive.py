import os
import docutils.parsers.rst
import sphinx.util.logging
import docutils.parsers.rst.directives

from sphinx_a4doc.model.model import ModelCache

logger = sphinx.util.logging.getLogger(__name__)


class A4Autogrammar(docutils.parsers.rst.Directive):
    required_arguments = 1
    optional_arguments = 1
    has_content = True
    option_spec = {
        'only-reachable': docutils.parsers.rst.directives.flag,
        'only-reachable-from': str,
        'no-lexer-rules': docutils.parsers.rst.directives.flag,
        'add-lexer-rules': docutils.parsers.rst.directives.flag,
        'no-parser-rules': docutils.parsers.rst.directives.flag,
        'add-parser-rules': docutils.parsers.rst.directives.flag,
        'no-fragments': docutils.parsers.rst.directives.flag,
        'add-fragments': docutils.parsers.rst.directives.flag,
        'show-undocumented': docutils.parsers.rst.directives.flag,
        'hide-undocumented': docutils.parsers.rst.directives.flag,
        'ordering': lambda v: docutils.parsers.rst.directives.choice(
            v, ['source', 'dfs', 'bfs', 'name']),
        'grouping': lambda v: docutils.parsers.rst.directives.choice(
            v, ['mixed', 'lexer-first', 'parser-first']),
        'root-rule-position': lambda v: docutils.parsers.rst.directives.choice(
            v, ['first', 'in-order']),
    }

    def run(self):
        env = self.state.document.settings.env
        base_path = env.config.a4_base_path
        path = os.path.join(base_path, self.arguments[0])

        model = ModelCache.instance().from_file(path)

        print(model.lookup('grammarSpec'))

        return []
