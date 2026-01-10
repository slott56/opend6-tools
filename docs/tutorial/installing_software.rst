..  _tutorial.installing_software:

Installing Software
===================

Using the *OpenD6 tools* project is adjacent to computer programming.
No, we won't be writing algorithms and if-statements and that kind of thing.
We will, however, be using software tools and the syntax of the Python programming language to create Spells and Characters.

The tools are written in Python. (See https://python.org).
Think of Python as the engine in the front of a tractor-trailer rig dragging around thirty-thousand pounds of bananas.
Our interest is the produce, not the details of how the diesel engine works.
We don't even care how many wheels or axles the tractor-trailer has.
We simply want fresh fruit.

Python -- the language -- is essential, but will be largely invisible.
Our only real interaction with Python will be the formal syntax rules borrowed from this language.
The arrangement of quotation marks, parenthesis, commas, etc., will come from Python.

Adjacent to the Python language is the "ecosystem" of add-on components.
This collection of tools, applications, and library modules is vast, published on-line, and used widely.
We'll be using some of these add-on components to produce our **OpenD6** documents.

Because we're using Python, it helps to understand what Python folks call a "virtual" environment.
The qualifier -- *virtual* -- is necessary because the operating system defines the real environment.
The environment applies every time we start an application or open a terminal window.
It includes the user information (which implies certain permissions), and the user's current working directory, as well as the user's collection of available applications and libraries.
Over the decades, Python developers have learned it's best not to try to touch the real OS environment. (Why? Partly because Windows, Linux and macos have too many unique features.)
Instead, Python folks use tools to create virtual environments.

..  important::

    Python virtual environments need to be *activated*.
    One very common problem is installing software in one virtual environment and then trying to use the software from another environment.
    It's important to make sure we know which virtual environment is active before doing anything.

    For those familiar with command-line tools the virtual environment name is a prefix on the prompt. It might be ``(my-book)`` to show the active environment.

    We'll look at details in some later steps.

Since the writing process is adjacent to software development, we'll be installing new software on our computer.
This means we need administrative rights to the computer we're using.
A lot of these steps will be done using the **Terminal** (or **Powershell**) window.
Not everyone is familiar with this, so we'll start with a necessary preparation step.

Preparation
------------

We'll be using tools that have a Command-Line Interface (CLI).
We interact with these using the Terminal (or Powershell) application.

This means we need to find the Terminal (or Powershell) window on our computer.
For readers used to programming, this goes without saying.
For readers not used to using advanced software tools to help with TTRPG design, this may be something new.

In **macos** the Terminal window can be found by running the **Launchpad** and typing "Term" into the search bar at the top of the screen.
This will highlight the icon for the Terminal window.
Some folks will drag this into the dock to make a reminder.

In **Windows**, the "Powershell" window is used.
Generally, the **Start Menu** will have a way to start Powershell.
https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.5

Folks using **Linux** are generally comfortable with using the terminal window to interact with CLI tools.
Most desktop environments will open a terminal window by default.

Finding a Terminal window (or Powershell) window is essential.
We'll do software installation and run the publication tools from the terminal window.

In order to manage Python's ecosystem and our computer's virtual environments, we'll start by installing a handy tool, called **uv**.
See https://docs.astral.sh/uv/.

Step 1: Install uv
--------------------

Using **uv** helps because it can install Python, install add-on packages, and create multiple virtual environments for folks who have multiple proceects in progress at one time.

See https://docs.astral.sh/uv/getting-started/installation/.

Here's what this might look like:

..  code-block:: text

    writer@MacBook-Pro-M4 ~ % cd Documents
    writer@MacBook-Pro-M4 Documents % curl -LsSf https://astral.sh/uv/install.sh | sh
    downloading uv 0.9.17 aarch64-apple-darwin
    no checksums to verify
    installing to /Users/writer/.local/bin
      uv
      uvx
    everything's installed!

    To add $HOME/.local/bin to your PATH, either restart your shell or run:

        source $HOME/.local/bin/env (sh, bash, zsh)
        source $HOME/.local/bin/env.fish (fish)
    writer@MacBook-Pro-M4 Documents % source $HOME/.local/bin/env

At this point, the **uv** tool is available.
We'll use this to install other tools.
Before we do that, however, it helps to install a programming editor or IDE.

Step 2: Install a programming editor or IDE
-------------------------------------------

As noted above, we're avoiding the limitations of word processors.
This means using a **simpler** editor for text files.
The editor is actually simpler than a word processor; it may look confusing at first, but then, all new things look confusing at first.

Some programming editors come with a ton of tools.
These are called an Integrated Development Environment (IDE.)
The number of tools is daunting.
We won't use many of them.

There are innumerable programming editors.
It's very difficult to choose one.
We'll make two suggestions that are available for most platforms.

1. PyCharm from JetBrains. https://www.jetbrains.com/pycharm/
    This is a commercial product, but there is a community edition.

2. Spyder. https://www.spyder-ide.org.
    This is open-source.

These have similar install procedures:

-   Download the installer from the web site.

-   Run the installer by double-clicking it.
    Under **macos**, the Safari browser will launch the installer automatically, saving the two clicks.

-   In the case of Spyder, when the the installer is finished, Spyder will start, and offer a number of tours and tutorials. These are highly recommended.

Step 3: Use uv to install Python
--------------------------------

We'll use **uv** to install Python.
Enter this ``uv`` command in the Terminal (or Powershell) window.

..  code-block:: bash

    uv python install 3.14

This is the same on all platforms -- **macos**, **Windows**, or **Linux**. That's one of the reasons why installing **uv** is so helpful.

It might look like this:

..  code-block:: text

    writer@MacBook-Pro-M4 my_book % uv python install 3.14
    Installed Python 3.14.2 in 2.59s
     + cpython-3.14.2-macos-aarch64-none (python3.14)

This has put ``python3.14`` into your current environment.
Try it out.

..  code-block:: text

    writer@MacBook-Pro-M4 my_book % python3.14
    Python 3.14.2 (main, Dec  9 2025, 19:29:30) [Clang 21.1.4 ] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Your version of Python may not be ``3.14.2``.  It's likely to be a lot newer.

Enter ``exit`` at the ``>>>`` prompt and hit return to leave Python.

We don't want to be looking at the Python ``>>>`` prompt.
We want to be looking at the Terminal prompt ending with ``%`` (or ``>`` for Windows.)
For **macos**, the prompt character will have a prefix like ``writer@MacBook-Pro-M4 my_book`` which is the username, ``writer``,, the machine name, ``MacBook-Pro-M4``, and the current directory, ``my_book``. This helps provide context for the ``%`` prompt.

For **Windows**, the prefix may be ``C:\`` or something equally terse.

What's important is there's no ``(my-book)`` prefix to the prompt.
This prefix will be inserted when we've activated a virtual environment.

Step 4: Use uv to start a project
-----------------------------------

Let's say we're going to create a campaign document.
We're going call it ``my_book``.
(It's a working title; we'll change it later.)

We'll start by using ``uv`` to create the project directory.
Then we'll change to the newly-created ``my_book`` directory.

Enter this ``uv`` commands in the Terminal (or Powershell) window.

..  code-block:: bash

    uv init --app --python 3.14 my_book
    cd my_book

A few files have been created in this directory by the **uv init** command.
We can use the ``ls`` (or **Windows** ``dir``) command to list the contents of this directory.

It might look like this:

..  code-block:: bash

    writer@MacBook-Pro-M4 Documents % uv init --app --python 3.14 my_book
    Initialized project `my-book` at `/Users/writer/Documents/my_book`
    writer@MacBook-Pro-M4 Documents % cd my_book
    writer@MacBook-Pro-M4 my_book % ls
    main.py		pyproject.toml	README.md

We don't **need** these files. They can be helpful, however, so it helps to look at them.
What are they?

-   ``main.py`` is a little application that shows what a Python application looks like. In the long run, we'll often delete this.

-   ``pyproject.toml`` describes the project from a technical perspective. It lists the name, the authors, and those kinds of things.
    It also lists the components on which the project depends.
    This list of dependencies is essential for working with collaborators.
    This file lets others reconstruct a virtual environment that matches the one you're creating.

-   ``README.md`` can provide some essential background details on the project. It expands on the bare technical facts in the ``pyproject.toml`` to help a person understand what this directory contains.
    It helps to think of this as an "elevator pitch" for the project. It's a synopsis we can rattle off in an elevator ride up to the executive conference room.

A book will use a large number of files.
Since we're going to use Sphinx to produce the documents,
the next step is to install Sphinx.

Above, we noted that a virtual environment is important.
We can create one now, with a ``uv venv`` command.
Or, we can wait, and the **uv** tool will add a virtual environment automatically when it installs Sphinx.

Step 5: Use uv to add Sphinx to the project
-------------------------------------------

The next installation step is to add the central tool for creating the final document.
We'll add Sphinx to our virtual environment.
See https://sphinx-doc.org.

Enter this ``uv`` commands in the Terminal (or Powershell) window.

..  code-block:: bash

    uv add sphinx

This will add Sphinx to the project environment, allowing us to create an empty book, ready to hold our ideas.

This will **also** create a virtual environment to contain the unique tools we've added for this project.
Look for the ``Creating virtual environment`` line in the output to confirm that this happened.

The output is long, so we've truncated it. It might look like this:

..  code-block:: bash

    writer@MacBook-Pro-M4 my_book % uv add sphinx
    Using CPython 3.14.2
    Creating virtual environment at: .venv
    Resolved 24 packages in 398ms
    Prepared 22 packages in 3.22s
    Installed 22 packages in 34ms
     + alabaster==1.0.0
    ...
     + sphinx==9.0.4
     + sphinxcontrib-applehelp==2.0.0
     + sphinxcontrib-devhelp==2.0.0
     + sphinxcontrib-htmlhelp==2.1.0
     + sphinxcontrib-jsmath==1.0.1
     + sphinxcontrib-qthelp==2.0.0
     + sphinxcontrib-serializinghtml==2.0.0
     + urllib3==2.6.2
    writer@MacBook-Pro-M4 my_book %

We now have enough software that we can use **Spyder** and **Sphinx** to start writing our campaign book.

The final step is to initialize the book's directory structure.
This means adding a few more directories and files to the ``my_book`` directory.

Step 6: Use sphinx-quickstart to start a document
-------------------------------------------------

Since our plan is to produce some rather complicated documentation for a campaign, we'll need to make sure we have all the right files in the right directories.

..  sidebar::

    A word processor leaves a single, complicated file laying around.

    The tools we're using leave a lot of small, simple files laying around.
    The details are exposed.

    What's important is understanding the details always existed.
    They're no longer hidden.

To create the empty document directory -- and configuration -- we'll use **uv** to run the Sphinx ``quickstart`` script.

..  code-block:: bash

    uv run sphinx-quickstart

This will ask a few questions about the project.
Then it will create the required files.

We used the ``cd`` command to set our current working directory to be the ``my_book`` directory.
We can confirm that using the **macos** ``pwd`` or **Windows** ``cd`` commands.

(The **Windows** ``cd`` command shows the current directory.
The **macos** and **Linus** ``cd`` command changes the current directory to be our home directory.)

The quickstart shows the ``Selected root path`` for the document.
The current directory has a name of ``.``. Yes. One period.

The interactive session might look like the following example.
We've highlighted the lines where questions are asked and we had to provide an answer.

..  code-block:: text
    :emphasize-lines: 12,15,16,17,25

    writer@MacBook-Pro-M4 my_book % uv run sphinx-quickstart
    Welcome to the Sphinx 9.0.4 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]:

    The project name will occur in several places in the built documentation.
    > Project name: my_book
    > Author name(s): S.Lott
    > Project release []:

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]:

    Creating file /Users/writer/Documents/my_book/conf.py.
    Creating file /Users/writer/Documents/my_book/index.rst.
    Creating file /Users/writer/Documents/my_book/Makefile.
    Creating file /Users/writer/Documents/my_book/make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file /Users/writer/Documents/my_book/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
       make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

    writer@MacBook-Pro-M4 my_book %

The log says four files were made. This is what was done for you:

-   ``conf.py`` is a configuration for Sphinx. It has a few project details in it. We'll need to edit this to change the configuration slightly.

-   ``index.rst`` is the root of the document to be created.

-   ``Makefile`` is used by the **make** utility to rebuild the book when any of the source files change. The ``make.bat`` file is a handy proxy for this when working with **Windows** where the **make** utility may be unavailable.

Step 7: Create a Spyder project
-------------------------------

It helps to tell Spyder what we're doing.
That way, we can simple click on the Spyder icon and start work.

There's **Project** menu in the Spyder window.
This has a **New...** item.
The **Project->New** menu item will lets us pick the "my_book" folder. This will create the needed project.

Once we've created the project, the left-side of the Spyder window will fill in with the files already created as part of this project.
Feel free to click around, looking at the various files.

If you're unfamiliar with Spyder (or IDE's in general), make sure you've followed the various links for tours and tutorials.

We'll make one small change to the configuration file in the final step.

Step 8: Tweak the configuration
-------------------------------

With the current ``my_book`` project open, the left side of the Spyder window is the collection of files we've created so far.
It shows the various files created by running ``uv init``.
It also shows the files created by running ``uv run sphinx-quickstart``.

We need to change the Sphinx configuration.
This is always in a file name ``conf.py``.

To change the configuration, double the ``conf.py`` file in the list of files in the Spyder window.

This file starts with a line that looks like the following:

..  code-block:: Python

    # Configuration file for the Sphinx documentation builder.
    #
    # For the full list of built-in configuration values, see the documentation:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html

We need to add one line at the end.

..  code-block:: python

    exclude_patterns = ['.venv/*']

This will prevent Sphinx from peering around inside the ``.venv`` directory tree, looking for elements of our book.
Sphinx tries to confirm that the ``.. toctree::`` directive and the file names all match up neatly.
Excluding all of the files in the ``.venv`` directory makes it clear any ``.rst`` files that are part of the software components in the virtual environment will not be part of the document we're writing.

Step 9: Edit the index.rst file
-------------------------------

Update the ``index.rst`` file with your working title and maybe some background about your project.

Run the following command in the Terminal window:

..  code-block:: bash

    make html

This will rebuild the target HTML content from your RST.

This is the first example of the **Change-Compute-Consider** cycle:

-   Change to the ``index.rst``.

-   Compute a new target HTML document.

-   Consider the results of the change. Perhaps more changes are needed. Perhaps this is good enough.

Conclusion
----------

At this point, we have Python, Sphinx, and the editor (or IDE) of your choice.
Throughout the tutorial, we'll assume Spyder was installed, but this is **not** a requirement; any text editor will work nicely.
A word processor, on the other hand, will be trouble.

In the next section, :ref:`tutorial.start_writing`, we'll start writing our campaign book using these tools.
