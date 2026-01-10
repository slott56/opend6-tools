.. OpenD6 Tools documentation master file, created by
   sphinx-quickstart on Mon Sep 22 12:52:38 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OpenD6 Tools
==========================

These tools help preparing documents to support the **OpenD6** Table-Top Role-Playing Game (TTRPG).

This is focused on two Python libraries that define a Domain Specific Language (DSL) for spells and characters.
Each offers a number of helpful features:

-  These modules allow the definition of spells (and miracles) using Python syntax.
   Since the DSL is declaratory, there's no real "programming" involved: only adherence to Python syntax rules.

-  Check the math used to compute spell difficulties, and character budgets (dice or character points.)

-  Emit ReStructuredText documents that can be processed by the **Sphinx** tool (and any other **docutils** tools) to create published documents.

There are two modules that define the DSL's:

-  The :py:mod:`opend6_tools.magic2` module defines the DSL for designing spells and invocations.

-  The :py:mod:`opend6_tools.character` module defines a DSL building characters and creatures that fit within a campaign.

Additionally, the following applications are also part of publishing the rule books.

- The :py:mod:`opend6_tools.notebook_extract` module extracts Spell or Character definitions from a Jupyter Lab notebook into a Python module.
   This can be converted to RST for publication.

- The :ref:`misc_comp` section describes some modules to compute a few tables in the **OpenD6** rules from first principles.
   These include the :py:mod:`opend6_tools.die_simplification` and :py:mod:`opend6_tools.spell_measure` modules.

The :ref:`dsl_design` section describes the overall approach to creating the DSLs.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   installation
   tutorial/index
   usage
   architecture
   magic2
   character
   notebook_extract
   computations
   notes

