..  _tutorial:

############
  Tutorial
############

The point of the **OpenD6** tools project is to help designers (as well as game masters) create consistent definitions of spells and characters.
These tools handle the accounting details for spell difficulty and character dice allocations.

Background
==========

The immediate focus is publishing documents.
Glancing up at the bigger picture, these documents may be intended for sale, or to be shared with interested readers and players.

The publication process is centered around a chain of tools to allow anyone to write some text and get a slick, professionally-formatted result in a number of distinct publication formats.
This also means being able to perform these two important tasks:

-   Compute the difficulty for a Spell. (Or the dice budget for a Character or Creature.)

-   Publish the Spell. (Or Character or Creature.)

These tasks -- interestingly -- suffer from a deep conflict.
The kind of tool that facilitates one task exacerbates the other task.

Consider using WYSIAYG ("What You See Is All You Get") tools: a word processor and a spreadsheet.
We can make a spreadsheet to automatate the computation -- and recomputation -- of difficulty for a spell.
However, we don't want to publish the spreadsheet; we need some kind of nicely-formatted summary.
If, on the other hand, we focus on the published description of a spell -- a blob of words -- we are forced to do manual computations when changes are made.

Bottom-line: Automated computations and nice formatting for publication are incompatible.
This conflict between computing and publishing makes design exploration difficult.

(Copy and Paste from a spreadsheet to a book is off the table as a choice. It's too error-prone.)

It is very helpful to have tooling to support a **Change-Compute-Consider** cycle.

1.  Change the definition of a spell (or character or creature.)
2.  Compute the consequences -- spell difficulty or dice budget.
3.  Consider the change in the larger context of a world design, campaign design, or in the  details of a scenario.

This needs to happen at the click of a mouse, permitting the designer to consider multiple alternatives.

To support simple **Change-Compute-Consider** cycle, we are forced to step away from the limitations of WYSIAYG tools.
we need to switch to a Publishing Pipeline.
The pipeline is a sequence of transformation stages.
The content will flow through these transformations to create the final, published form of the book (or web site, or printed hand-out for players.)

The general approach to working with a Publishing Pipeline is this:

1.  Write the bulk of the source material using a programming text editor.
    The author use ReStructuredText (RST) markup for the structure and emphasis in the document.
    For example, **bold** text looks like this: ``**bold**``.
    It's wrapped in double ``*`` characters.
    Similarly, *italic* text looks like this: ``*italic*``.
    Headings are underlined. List items are indented.

2.  Write details of Spells, Invocations, Characters, Creatures, etc., in external files.
    These are **not** in RST format.
    The publishing pipeline tools will convert our working ideas from a computation-friendly form into RST.

3.  Edit the various external files in a rapid **Change-Compute-Consider** cycle until things look good.

4.  Use the **Publishing Pipeline** to convert the RST into HTML (or PDF or EPUB) products.
    This will include RST we wrote plus RST made from our Spells, Invocations, etc.
    Consistent editorial styling is part of the final conversion.

For advanced document designers, HTML styles can be added to alter the look, enforcing consistent styling.
The HTML templates can be changed to alter the structure of the resulting pages.

Changes are always made to the source RST; the target documents are generated from these.
The target HTML, PDF, and EPUB are **never** touched manually, they're simply distributed to the target audience.

The Big Picture
===============

The goal is to create the ``book.html`` (or PDF or EPUB).
Getting there requires creating a number of files in the ``book`` folder.
Often, there's at least one file per chapter; the diagram only shows a two files: ``magic.rst`` and ``index.rst``.

In order to allow a flexible, fast **Change-Compute-Consider** cycle, Jupyter Lab is used to create notebooks.
The diagram shows one notebook with the unhelpful name of ``example_1.ipynb``.
Any more mreaningful name can be used; we strongly encourage using lower-case letters, digits, and ``_``'s as the stem for the name. The suffix has to be ``.ipynb``.


..  uml::

    @startuml
        'https://plantuml.com/deployment-diagram

    <style>
    artifact {
        RoundCorner 5
        FontStyle Bold
        LineThickness 3
    }
    </style>

    skinparam actorStyle awesome
    actor "Designer"

    boundary "Jupyter Lab" as lab
    Designer <--> lab : "**Change**\n**Compute**\n**Consider**"

    folder notebooks {
        file example_1.ipynb
    }

    lab --> example_1.ipynb

    boundary "Spyder" as editor
    Designer <-> editor : "**Create**\n**Content**"

    editor --> book
    folder book {
        file index.rst
        file magic.rst
        folder spells {
            file example_1.txt
        }
        magic.rst ..> example_1.txt : "include"
    }

    component make {
        component opend6_tools
        component sphinx
    }

    example_1.ipynb --> opend6_tools
    opend6_tools --> example_1.txt

    component sphinx
    artifact "book.html" <<<target>>>
    note right of "book.html"
        or PDF or EPUB
    end note

    book --> sphinx
    sphinx ---> book.html

    boundary "Terminal" as cli
    Designer <-> cli : "**Publish**"
    cli --> [make]

    @enduml

The diagram shows the designer using three distinct tools.

1.  The bulk of the writing is done with a programming text editor.
    The Spyder Integrated Development Environment is helpful.
    Really, any programming editor can be used, even Jupyter Lab.

2.  The more complicated **Change-Compute-Consider** part of the work is done with Jupyter Lab.
    This will do rapid computations on the Spell and Character definitions.

3.  The final production will be done with the **make** program run from a Terminal window.
    This makes use the ``opend6_tools`` project and Sphinx to do the real work.
    It creates the final ``book.html`` from the ``book`` folder of files.

Yes, there are a lot of files.
Yes, there are also a lot of tools.
The core concept is to use "Domain Specific Languages" from the ``opend6_tools`` to facilitate the **Change-Compute-Consider** effort.
Splitting the overall job into pieces helps create more complex documents, like books of TTRPG rules.

This Tutorial
=============

This tutorial is in five parts.

..  toctree::
    :hidden:

    installing_software
    start_writing
    opend6_tools
    define_spells
    define_characters


1.  :ref:`tutorial.installing_software` covers the basics of getting started working with advanced software tools for writing. For folks new to Python or new to programming, this is essential.

2.  :ref:`tutorial.start_writing` dips into the world of ReStructuredText (RST) and how simple text files using plain-text markup are transformed into elegant HTML documents.

3.  :ref:`tutorial.openD6_tools` shows how to install the ``opend6-tools`` library in a working Python virtual environment. This will show some aspects of the **Change-Compute-Consider** cycle

4.  :ref:`tutorial.define_spells` looks closely at the Domain-Specific Language (DSL) for spells and how to incorporate a spell definition into an RST document.
    This section will look deeply at the **Change-Compute-Consider** cycle.

5.  :ref:`tutorial.define_characters` covers some features of the Domain-Specific Language (DSL) for characters and creatures and how to incorporate a creature definition into an RST document.
    This section also looks deeply at the **Change-Compute-Consider** cycle.
