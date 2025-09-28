# Sphinx plugin for Antlr4

Sphinx-A4Doc is deprecated, please use [Sphinx-Syntax] instead.

See [migration guide] for more info.

[Sphinx-Syntax]: https://taminomara.github.io/sphinx-syntax/

[migration guide]: https://taminomara.github.io/sphinx-syntax/sphinx-a4doc.html

<!--- cut --->

## Resources

- [Documentation](https://taminomara.github.io/sphinx-a4doc/)

## Changelog

*v1.7.0*

- End of support announcement.

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
