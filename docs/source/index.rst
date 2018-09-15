Sphinx plugin for Antlr4
========================

A4Doc is a sphinx plugin for documenting Antlr4 grammars.

It's primary target is to provide some overview for DSL users rather than
compiler developers.

See an example output: json grammar, c grammar.

.. _features:

Features
--------

- A new domain with ``grammar`` and ``rule`` directives called ``a4``.

- Directives for rendering railroad diagrams, such as this one:

  .. railroad-diagram::
     - choice:
       - terminal: 'parser'
       -
       - terminal: 'lexer '
       default: 1
     - terminal: 'grammar'
     - non_terminal: 'identifier'
     - terminal: ';'

- Directive for extracting documentation comments and rendering docs and
  diagrams from ``.g4`` source files.

- Tools for highlighting and referencing grammar source files.

Requirements
------------

A4Docs uses dataclasses to represent parsed antlr files, thus ``python >= 3.7``
is required. Also, it is only tested with ``sphinx >= 1.7.7`` so it may or may
not work with older versions of sphinx.

Installation
------------

Install ``sphinx_a4doc`` with pip:

.. code-block:: sh

    pip3 install sphinx_a4doc

Add ``sphinx_a4doc`` to the list of extensions in your ``conf.py``.
If you intend to generate documentation from sources, also specify the
location of your grammar files:

.. code-block:: python

   extensions = [
       'sphinx_a4doc',
   ]

   # Assuming conf.py is in project/docs/source/conf.py
   # and grammars are in project/project/grammars
   from os.path import dirname
   a4_base_path = dirname(__file__) + '/../../your_project/grammars'

Quickstart
----------

Use the :rst:dir:`a4:grammar` directive to declare a new grammar.
Within the grammar block, use the :rst:dir:`a4:rule` to declare a new rule:

.. code-block:: rst

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

Use :rst:role:`a4:grammar` (or :rst:role:`a4:g` as a shortcut) or
:rst:role:`a4:rule` (or :rst:role:`a4:r`) roles to refer the declared
grammars and rules:

.. code-block:: rst

   Grammar :a4:g:`MyGrammar` has a root rule :a4:r:`MyGrammar.root`.

The above code produces this output:

.. highlights::

   Grammar :a4:g:`MyGrammar` has a root rule :a4:r:`MyGrammar.root`.

Use :rst:dir:`railroad-diagram`, :rst:dir:`lexer-rule-diagram` and
:rst:dir:`parser-rule-diagram` directives to render diagrams:

.. code-block:: rst

   .. parser-rule-diagram:: 'def' ID '(' (arg (',' arg)*)? ')' ':'

The above code produces this output:

.. highlights::

   .. parser-rule-diagram:: 'def' ID '(' (arg (',' arg)*)? ')' ':'

Use :rst:dir:`a4:autogrammar` and :rst:dir:`a4:autorule` directives to generate
documentation for the grammar file located at the given path.

RST reference
-------------

Declaring objects
~~~~~~~~~~~~~~~~~

.. rst:directive:: .. a4:grammar:: name

   Declare a new grammar with the given name.

   Grammar names should be unique within the project.

   **Options:**

   .. option:: \:noindex\:
      :noindex:

      A standard sphinx option to disable indexing for this rule.

   .. option:: \:name\:
      :noindex:

      Specifies a human-readable name for this grammar.

      If given, the human-readable name will be rendered instead of the primary
      grammar name, while the primary name will be rendered next to it.

      For example this code:

      .. code-block:: rst

         .. a4:grammar:: PrimaryName
            :name: Human-readable name

      will render the next grammar description:

      .. highlights::

         .. a4:grammar:: PrimaryName
            :noindex:
            :name: Human-readable name

      Setting a human-readable name does not affect cross-referencing.

   .. option:: \:type\: lexer|parser
      :noindex:

      Specifies a grammar type, either ``lexer`` or ``parser``. The type will be
      displayed in the grammar signature.

      For example these three grammars:

      .. code-block:: rst

         .. a4:grammar:: Grammar1

         .. a4:grammar:: Grammar2
            :type: lexer

         .. a4:grammar:: Grammar3
            :type: parser

      will be rendered differently:

      .. highlights::

         .. a4:grammar:: Grammar1
            :noindex:

         .. a4:grammar:: Grammar2
            :noindex:
            :type: lexer

         .. a4:grammar:: Grammar3
            :noindex:
            :type: parser

   .. option:: \:imports\: <str>[ <str>[ ...]]
      :noindex:

      Specifies a list of imported grammars, comma or whitespace separated.

      This option affect name resolution process for rule cross-references.
      That is, if there is a reference to ``grammar.rule`` and there is no
      ``rule`` found in the ``grammar``, the imported grammars will be searched
      as well.

.. rst:directive:: .. a4:rule:: name

   Declare a new production rule with the given name.

   If placed within an :rst:dir:`a4:grammar` body, the rule will be added to
   that grammar. It can then be referenced by a full path which will include
   the grammar name and the rule name concatenated with a dot symbol.

   If placed outside any grammar directive, the rule will be added to
   an implicitly declared "default" grammar. In this case, the rule's full
   path will only include its name.

   In either case, the rule name should be unique within its grammar.

   **Options:**

   .. option:: \:noindex\:
      :noindex:

      A standard sphinx option to disable indexing for this rule.

   .. option:: \:name\: <str>
      :noindex:

      Specifies a human-readable name for this rule. Refer to the corresponding
      :rst:dir:`a4:grammar`'s option for more info.

Cross-referencing objects
~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst:role:: any
   :noindex:

   All ``a4`` objects can be cross-referenced via the :rst:role:`any` role.

   If given a full path, e.g. ``:any:`grammar_name.rule_name```,
   :rst:role:`any` will search a rule called ``rule_name`` in the
   grammar called ``grammar_name`` and then, should this search fail, in all
   grammars that are imported from ``grammar_name``, recursively.

   If given a relative path, e.g. ``:any:`name```,
   :rst:role:`any` will perform a global search for a rule or a grammar with the
   corresponding name.

.. rst:role:: a4:grammar
              a4:g

   Cross-reference a grammar by its name.

   There's nothing special about this role, just specify the grammar name.

.. rst:role:: a4:rule
              a4:r

   Cross-reference a grammar by its name or full path.

   If given a full path, e.g. ``:a4:r:`grammar_name.rule_name```,
   the rule will be first searched in the corresponding grammar, then in
   all imported grammars, recursively.

   If given a rule name only, e.g. ``:a4:r:`rule_name```, the behavior depends
   on context:

   - when used in a grammar declaration body, the rule will be first searched
     in that grammar, then in any imported grammar, and at last, in the default
     grammar.

   - when used without context, the rule will only be searched
     in the default grammar.

   Prepending full path with a tilde works as expected.

Rendering diagrams
~~~~~~~~~~~~~~~~~~

.. rst:directive:: railroad-diagram

   The most flexible directive for rendering railroad diagrams.

   This example renders a diagram from the :ref:`features <features>` section:

   .. code-block:: rst

      .. railroad-diagram::
         - choice:
           - terminal: 'parser'
           -
           - terminal: 'lexer '
           default: 1
         - terminal: 'grammar'
         - non_terminal: 'identifier'
         - terminal: ';'

   which translates to:

   .. highlights::

      .. railroad-diagram::
         - choice:
           - terminal: 'parser'
           -
           - terminal: 'lexer '
           default: 1
         - terminal: 'grammar'
         - non_terminal: 'identifier'
         - terminal: ';'

   **Options:**

   .. option:: \:padding\:
      :noindex:

   .. option:: \:vertical-separation\:
      :noindex:

   .. option:: \:horizontal-separation\:
      :noindex:

   .. option:: \:arc-radius\:
      :noindex:

   .. option:: \:diagram-class\:
      :noindex:

   .. option:: \:translate-half-pixel\:
      :noindex:

   .. option:: \:internal-alignment\:
      :noindex:

   .. option:: \:character-advance\:
      :noindex:

   .. option:: \:end-class\:
      :noindex:

.. rst:directive:: lexer-rule-diagram

   The body of this directive should contain a valid Antlr4 lexer rule
   description.

   For example

   .. code-block:: rst

      .. lexer-rule-diagram:: ('+' | '-')? [1-9] [0-9]*

   translates to:

   .. highlights::

      .. lexer-rule-diagram:: ('+' | '-')? [1-9] [0-9]*

   **Options:**

   Options are inherited from the :rst:dir:`railroad-diagram` directive.

.. rst:directive:: parser-rule-diagram

   The body of this directive should contain a valid Antlr4 parser rule
   description.

   For example

   .. code-block:: rst

      .. parser-rule-diagram::

         SELECT DISTINCT?
         ('*' | expression (AS row_name)?
                (',' expression (AS row_name)?)*)

   translates to:

   .. highlights::

      .. parser-rule-diagram::

         SELECT DISTINCT?
         ('*' | expression (AS row_name)?
                (',' expression (AS row_name)?)*)


   **Options:**

   Options are inherited from the :rst:dir:`railroad-diagram` directive.

Autodoc directives
~~~~~~~~~~~~~~~~~~

.. rst:directive:: a4:autogrammar

.. rst:directive:: a4:autorule

Configuration
-------------

Python API reference
--------------------

This section describes A4Doc python API. It may come in handy for any extension
that wishes to reuse or extend A4Doc's functionality.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
