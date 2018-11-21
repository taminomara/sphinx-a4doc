Sphinx plugin for Antlr4
========================

A4Doc is a sphinx plugin for documenting Antlr4 grammars.

It's primary target is to provide some overview for DSL users
(generated documentation may not include some nuances essential
for compiler developers).

See an example output: :a4:g:`Json`.

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

Requirements
------------

A4Doc uses dataclasses to represent parsed antlr files, thus ``python >= 3.7``
is required. Also, this extension requires ``sphinx >= 1.8.0`` because it
relies on some features added in that release.

Installation
------------

Install ``sphinx-a4doc`` with pip:

.. code-block:: sh

    pip3 install sphinx-a4doc

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
   a4_base_path = dirname(__file__) + '/../../project/grammars'

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

Use :rst:dir:`a4:autogrammar` directive to generate documentation
from a grammar file.

RST reference
-------------

Declaring objects
~~~~~~~~~~~~~~~~~

.. rst:autodirective:: .. a4:grammar:: name

.. rst:autodirective:: .. a4:rule:: name

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

.. rst:autodirective:: railroad-diagram

.. rst:autodirective:: lexer-rule-diagram
   :no-options:

.. rst:autodirective:: parser-rule-diagram
   :no-options:

Autodoc directive
~~~~~~~~~~~~~~~~~

.. rst:autodirective:: .. a4:autogrammar:: name

Configuration
-------------

Customizing diagram style
~~~~~~~~~~~~~~~~~~~~~~~~~

Customizing process of grammar files lookup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python API reference
--------------------

This section describes A4Doc python API. It may come in handy for any extension
that wishes to reuse or extend A4Doc's functionality.

Example output
--------------

This example was generated from `Json.g4 <https://github.com/AmatanHead/sphinx-a4doc/blob/master/docs/examples/Json.g4>`_.

.. a4:autogrammar:: Json

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
