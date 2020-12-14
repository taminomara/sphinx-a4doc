# Sphinx plugin for Antlr4

A4Doc is a sphinx plugin for documenting Antlr4 grammars.

It’s primary target is to provide some overview for DSL users
(generated documentation may not include some nuances essential
for compiler developers).

A4Doc's features are:

- a new domain with grammar and rule directives called ``a4``;
- directives for rendering railroad diagrams;
- directive for extracting documentation comments and rendering docs and
  diagrams from `.g4` source files.

<!--- cut --->

## Resources

- [Documentation](https://amatanhead.github.io/sphinx-a4doc/)
- [Installation](https://amatanhead.github.io/sphinx-a4doc/#installation)
- [Quickstart](https://amatanhead.github.io/sphinx-a4doc/#quickstart)
- [Example output](https://amatanhead.github.io/sphinx-a4doc/#example-output)

## Requirements

- python >= 3.7
- sphinx >= 1.8.0

## Installation

```sh
pip3 install sphinx-a4doc
```

## Use cases

- [7zip format specification](https://py7zr.readthedocs.io/en/latest/archive_format.html)

## Changelog

*v1.2.2, v1.2.3, v1.2.4*

- No functional changes, just setting up CI to push PyPI releases automatically.

*v1.2.1*

- Fixed integration with intersphinx.

*v1.2.0*:

- Renamed `conf.py` settings: `a4_autodoc_*` became `a4_autogrammar_*`.
- Added support for section comments in grammar files.
- Added flexible settings to control how literal lexer rules are rendered.
- Added setting to convert rule names from ``CamelCase`` to ``dash-case``.
- Fixed documentation comments are parsed incorrectly in some cases.

*v1.0.1*:

- Fixed absence of `.css` file for railroad diagrams.

*v1.0.0*:

- Initial release.
