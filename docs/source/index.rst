Sphinx plugin for Antlr4
========================

A4Doc is a sphinx plugin for documenting Antlr4 grammars.

See an example output: json grammar, c grammar.

Features
--------

- A new domain with `grammar` and `rule` directives called `a4`.

- Directives for rendering railroad diagrams, such as this one:

  .. railroad-diagram::
     type: sequence
     items:
     - type: choice
       default: 1
       items:
       - type: terminal
         text: 'parser'
       - type: skip
       - type: terminal
         text: 'lexer '
     - type: terminal
       text: 'grammar'
     - type: non_terminal
       text: identifier
     - type: terminal
       text: ';'

- Directive for extracting documentation comments and rendering docs and
  diagrams from `.g4` source files.

- Tools for highlighting and referencing grammar source files.

Requirements
------------

A4Docs uses dataclasses to represent parsed antlr files, thus `python >= 3.7`
is required. Also, it is only tested with `sphinx > 1.7.7` so it may or may not
work with older versions of sphinx.

Installation
------------

Install `sphinx_a4doc` with pip::

    $ pip3 install sphinx_a4doc

Add `sphinx_a4doc` to the list of extensions in your `conf.py`.
If you intend to generate documentation from sources, also specify the
location of your grammar files::

    extensions = [
        'sphinx_a4doc',
    ]

    # Assuming conf.py is in project/docs/source/conf.py
    # and grammars are in project/project/grammars
    from os.path import dirname
    a4_base_path = dirname(__file__) + '/../../your_project/grammars'

Quickstart
----------

Use the `a4:grammar` directive to declare a new grammar. Within the grammar
block, use the `a4:rule` to declare a new rule::

    .. a4:grammar:: MyGrammar

       A grammar for my DSL.

       .. a4:rule:: root

          The root grammar rule.

The above code produces this output:

.. highlights::

   .. a4:grammar:: MyGrammar

      A grammar for my DSL.

      .. a4:rule:: root

         The root grammar rule.

Use `a4:grammar` (or `a4:g` as a shortcut) or `a4:rule` (or `a4:r`) roles to
refer the declared rules::

    Grammar :a4:g:`MyGrammar` has a root rule :a4:r:`MyGrammar.root`.

The above code produces this output:

.. highlights::

   Grammar :a4:g:`MyGrammar` has a root rule :a4:r:`MyGrammar.root`.

Use `railroad-diagram`, `lexer-rule-diagram` and `parser-rule-diagram`
directives to render diagrams::

    .. parser-rule-diagram:: 'def' ID '(' args ')' ':' body

The above code produces this output:

.. highlights::

    .. parser-rule-diagram:: 'def' ID '(' args ')' ':' body

Use `a4:autogrammar` and `a4:autorule` directives to generate documentation
for the grammar file located at the given path.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

