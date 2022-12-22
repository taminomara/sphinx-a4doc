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

- [Documentation](https://taminomara.github.io/sphinx-a4doc/)
- [Installation](https://taminomara.github.io/sphinx-a4doc/#installation)
- [Quickstart](https://taminomara.github.io/sphinx-a4doc/#quickstart)
- [Example output](https://taminomara.github.io/sphinx-a4doc/#example-output)

## Requirements

- python >= 3.7
- sphinx >= 1.8.0

## Installation

```sh
pip3 install sphinx-a4doc
```

## Use cases

- [Solidity specification](https://docs.soliditylang.org/en/latest/grammar.html)
- [7zip format specification](https://py7zr.readthedocs.io/en/latest/archive_format.html)

## Changelog

*v1.6.0*

- Support LaTeX builder.

*v1.5.0*

- Fixed position of text in diagram nodes in Firefox.
- Added an option to set custom classes to diagram nodes: `//@ doc:css-class`.

*v1.4.0*

- Fixed compatibility with `singlehtml` mode (see [#15](https://github.com/taminomara/sphinx-a4doc/issues/15)).

*v1.3.0*

- Fixed python 3.9 compatibility issue (by [@sandrotosi](https://github.com/sandrotosi)).

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
