..  _tutorial.start_writing:


Start Writing
=============

Each writing session reflects the **Change-Compute-Consider** cycle.

-      It will involve changing the ``.rst`` (and other) files in the project directory.

-      Compute a new target document by running ``make html`` at the command line.
       This builds HTML-format web pages built from the source files.

-      Consider the resulting web site.

Step 1: Activate the virtual environment
----------------------------------------

Each time we sit down to a fresh, new Terminal window (or Powershell prompt) we'll need to make sure our virtual environment is active.
The OS prompt provides a little hint.

- If the prompt starts with ``(my-book)`` then the virtual environment is active. Nothing more needs to be done.
    Skip the rest of this step.

- Otherwise, the virtual environment is not active, and needs to be activated.

In order to run ``make``, the virtual environment needs to be active.
Here's the command to activate the virtual environment.

..  code-block:: bash

    source .venv/bin/activate

For **Windows** the command is slightly simpler.

..  code-block:: bash

    .venv\Scripts\Activate.ps1

This will make all the Python scripts and tools into first-class parts of the current working environment.

The prompt will change to include ``(my-book)`` as a reminder that the virtual environment is now active.

Step 2: Write
-------------

Open Spyder.

Open the ``index.rst`` file. It should look something like this.

..  code-block:: rst

    .. my_book documentation master file, created by
       sphinx-quickstart on Thu Dec 11 15:10:08 2025.
       You can adapt this file completely to your liking, but it should at least
       contain the root `toctree` directive.

    my_book documentation
    =====================

    Add your content using ``reStructuredText`` syntax. See the
    `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
    documentation for details.


    .. toctree::
       :maxdepth: 2
       :caption: Contents:

This shows a number of RST features.

-   The line starting with ``..`` is a "comment" or "note".
    The indented lines that follow are part of the note.
    This is private material, for the author's eyes only.
    It's not included in the output.

-   The title is ``my_book documentation``.
    We know this is some kind of heading because it is followed by an underline that has the same length as the line above it.
    A heading **must** have this two-line structure.

    RST headings are underlined using any of a variety of characters.
    We suggest the following pattern:

    -   Book Title has ``#`` as the underline character.
    -   Chapter titles have ``=`` as the underline character.
    -   Section titles have ``-`` as the underline.
    -   Subsections can have ``~`` as the underline.

    If you need subsubsections, use ``*``.

    Consistency matters.

-   The use of the `````` character pairs to surround text that's shown in "terminal" font.
    The ``index.rst`` example doesn't show using ``**`` for strong emphasis, and ``*`` for emphasis. Strong emphasis often uses a **bold** style. Emphasis often uses an *italic* style.

-   There's a two-part hyperlink: ```text <URL>`_``.
    Note the use of single ````` characters to surround the hyperlink, and the use of ``_`` at the end to show that this link leads away from this document to another site on the internet.
    The text is what the reader will see.
    The part in ``<`` ... ``>`` is the Uniform Resource Locator (URL) to which they can be directed if they click.

-   The ``.. toctree::`` is a "directive".
    A directive is not part of the text, but is an instruction to Sphinx to do something here.
    This specific directive tells Sphinx to locate the files named within the directive and create a table of contents from them.
    Right now, there are no files inside this directive.

Two changes are important here:

-   Change the title to something more interesting.
    Change the line of ``=`` to a line of ``#`` that matches your more interesting title.

-   Add five empty chapters:

    -   Introduction
    -   Key Terms
    -   Character Basics
    -   Character Options
    -   Improving Characters

What's involved in adding a chapter?

1.  Create a new ``.rst`` file for the chapter.
    We might create a file named ``introduction.rst``.

2.  Put the title in the chapter.
    The first two lines of the ``introduction.rst`` file can be

    ..  code-block:: rst

        Introduction
        ============

    Feel free to leave a blank line after the underline and write anything that looks interesting as part of this chapter.

3.  Update the ``.. toctree::`` directive in ``index.rst`` to include the stem of the new file's name. Use ``introduction``, because the suffix (``.rst``) is part of the default configuration, and doesn't need to be included in the the ``.. toctree::`` directive's content.

    It might look like this:

    ..  code-block:: rst

        .. toctree::
           :maxdepth: 2
           :caption: Contents:

            introduction

    What's important is the file name is **indented** within the ``.. toctree::`` directive's content.

These three steps should be repeated for each of the five new chapters.
This will add five new files.
It will add five filenames to the ``.. toctree::`` directive.

Separating the book into chapter files like this makes editing slightly simpler.
It's possible to have all of the files open at once in Spyder, and move text around as needed.
It's possible to decompose the chapter files into section files, too.

For more information on how this works, see https://www.sphinx-doc.org/en/master/usage/index.html.

Step 3: Run Make
----------------

Outside Spyder, at the **Terminal** window, run the following command

..  code-block:: bash

    make html

This will make a nice HTML version of our draft book.
Look inside the ``_build`` directory for the ``html`` sub-directory.
Inside here, there's an ``index.html`` that is the resulting web site.

Spyder can open a browser to display the ``index.html`` file.

It also works to open the OS file management window and double click the ``index.html`` file to see it in a browser.


Conclusion
----------

At this point, we have used Sphinx, and our editor (or IDE) to create some elements of our campaign book.
We can write and publish complex TTRPG material with (relative) ease.
We can decompose the book into multiple files.
We can easily have several files open at once to make sure sections are consistent.

We've seen the **Change-Compute-Consider** cycle up close.

-      Change an ``.rst`` (and other) files in the project directory.

-      Compute a new target document by running ``make html`` at the command line.

-      Consider the resulting web site.

To move onto the complicated parts -- Spells and Characters -- we need a few more tools. In the next part of the tutorial, :ref:`tutorial.opend6_tools`, we'll add the ``opend6-tools`` package to our working virtual environment. We'll also pause to explore Jupyter Lab as a kind of IDE for working with code.
