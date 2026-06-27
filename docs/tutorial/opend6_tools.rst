..  _tutorial.opend6_tools:

OpenD6 Tools
==============

We need to tackle the complicated problems of spells and characters (as well as creatures and items.)

We're going to extend the **Change-Compute-Consider** cycle.
Here's one aspect:

-      Change the Spell definition (or Character definition) files.

-      Compute new values for the character dice budget or the spell difficulty.

-      Consider the resulting Spell or Character or Creature.

This cycle of changes is followed by the **Publish** operation:

-   Compute revised RST from the revised Spell (or Character) definition files.

-   Compute revised HTML from the revised RST.

-   Consider (or Share) the resulting target document.

The detailed computations depend on the ``opend6-tools`` project.
This project provides two Domain-Specific Languages (DSLs).
One language help define Spells, Invocations, and Magical Items.
The second defines Characters, and Creatures.

We'll also show how to use **Jupyter Lab**.
This is an interactive computing environment where we can define and modify these DSL statements.
It supports an almost instantaneous **Change-Compute-Consider** cycle.

..     admonition:: More Advanced Configuration

       More advanced users may also want to add ``spyder-kernels`` to help Spyder work with the version of Python we installed using **uv**.
       The Spyder "preferences" editor (a wrench icon) has a ``Python Interpreter`` panel.
       On this panel, select the Selected Interpreter option and fill in the path to the ``Python`` run-time installed in the earlier part of the tutorial.


Step 1: Activate the virtual environment
----------------------------------------

Each time we sit down to a Terminal window (or Powershell prompt) we'll need to make sure our virtual environment is active.
The OS prompt should provide hints as to what environment is active.
There are two parts to this:

-   The current working directory. The book directory, ``campaign_book`` needs to be current.
    If the prompt doesn't show the directory, there are OS commands to print the working directory: ``pwd`` (or **Windows** ``cd``).

    If the directory isn't correct, use the ``cd`` (or ``chdir``) command to navigate to the correct working directory.

-   The virtual environment. If the prompt starts with ``(my-book)`` then the virtual environment is active. Nothing more needs to be done.

    If the virtual environment isn't active, use one of the following commands to activate it.

    ..  code-block:: bash

        source .venv/bin/activate

    For **Windows** the command is slightly different.

    ..  code-block:: bash

        .venv\Scripts\Activate.ps1

The prompt will have a prefix of ``(my-book)`` as a reminder that the virtual environment is now active.

Step 2: Start Jupyter Lab
--------------------------

Before we show the command to start the lab environment, it's important to note that
Jupyter Lab has two active ingredients:

-   The "jupyter lab" service, simmering slowly on a back-burner.

-   A browser window that the designer uses to create Spells and Characters. This will interacts with the service.

Here's a picture of what will be going on:

..  uml::

    @startuml
    scale 2/3
    skinparam actorStyle awesome

    title Using Jupyter Lab

    actor "Designer"
    node "Computer" {
        boundary Browser
        component "jupyter lab" as svc
        Browser <--> svc : "3. Presents"
        boundary Terminal
        svc <-- Terminal : "2. Starts"

        folder "my_book" {
        folder "notebooks" {
            artifact spells_1.ipynb
        }
        }
        svc -> spells_1.ipynb : "Change & Compute"
    }
    Designer <--> Terminal : "1. Initially"
    Designer <-> Browser : "4. Everything else"
    @enduml

Because there is both a browser **and** a service, we need to have two windows open:

-   The Browser window with the interesting interactive parts of Jupyter lab.

-   A Terminal (or Powershell) window with the Jupyter lab log.
    This is used to start the service and the browser.
    After that, it can be safely ignored.

We've belabored this to make it clear why starting Jupyter Lab involves the following sequence of steps:

1.  Open a fresh, new Terminal window.

2.  Follow the steps from :ref:`tutorial.start_writing` to navigate to your project and activate the virtual environment.

    These commands are typical for **macos** and **Linux**.
    These are not for **Windows**.

    1.  Change to the ``campaign_book`` working directory.

        ..  code-block:: bash

            cd ~/Documents/campaign_book

    2.  Activate your virtual environment.

        ..  code-block:: bash

            source .venv/bin/activate

To start Jupyter Lab, use this command.

..  code-block:: bash

    jupyter lab

When Jupyter lab starts, it sprays a ton of information into the Terminal window.

More importantly, it **also** launches a browser window that looks like this:

..  figure:: lab_1.png

    Jupyter Lab window in the browser.

Yes. Jupyter Lab is an IDE. Double click on the ``index.rst`` or ``conf.py`` files and edit them here.
Or use **Spyder** to edit them.

Yes. You can do **all** of your writing and editing in Jupyter Lab.
Here's the comparison between Jupyter and Spyder.

..  csv-table::
    :header: Tool, Text Edit, Edit Notebooks, Startup

    Jupyter Lab, Primitive, Wow!, Annoying to Start
    Spyder, Power-tool, With a plug-in, Easy to Start

There are numerous other IDE's, some of which can do both: edit files and edit notebooks.
We need to focus on OpenD6 tools, however, not the innumerable alternative development environments.

We'll finish this part of the tutorial by creating a simple Notebook.

Step 3: Create a Notebooks Folder
----------------------------------

The left-most edge of the Jupyter Lab window looks like this.

..  figure:: left_side.png
    :scale: 33%

    The four icons on the left-most edge of a Jupyter Lab window,
    the File Browser is selected.

It has these four icons down the side of the window:

-   The "File Browser" has a file folder icon. Selecting this  shows files in the working directory.
    This is generally what's shown initially, and we'll use this heavily as we create files.

-   The "Running Terminals and Kernels" has an icon with a circle with a small square inside. If we select this, we'll see some details of the Jupyter services. This includes open tabs, processing kernels, language servers, recently-closed notebooks, workspaces, and terminal sessions.
    We rarely need to care what's running in the background.

-   The "Table of Contents" shows a three-item bullet list icon. This is used to visualize the structure of the currently open Notebook. With no notebook open, this isn't very helpful.
    However, once we start creating notebooks, this can be handy for looking at the structure of the notebook.

-   At the bottom, the "Extension Manager" has a puzzle piece icon.
    This is used to add extension components to Jupyter Lab.

When the file folder is active on the left edge, the pane next to this is filled with the folders and files of our project.

The top of the File Browser panel has five icons and looks like this:

..  figure:: top_row.png
    :scale: 33%

    Five icons for controlling the File Browser.

Here is what these five icons do:

-   A highlighted blue rectangle with a "+" sign to create a new Launcher tab.
    The Launcher tab (which fills most of the window) has icons to launch notebooks, consoles, or "other" file editors.

-   A small file folder with a "+" sign to create new directories in the current directory.

-   An upward arrow, used to upload files to this notebook.

-   A little clockwise circle for refreshing the display.
    This is useful if we make changes to the directory using OS tools or Spyder and need to force Jupyter Lab to synchronize with those changes.

-   A little funnel to allow a filtered view.
    This can be helpful in the cases where there are a **lot** of files and the display is cluttered with irrelevancies.

We need to create a ``notebooks`` folder, and put a new Notebook in that folder.
Do the following three steps to create an empty notebook in a new folder.

1.  Click the icon of a file folder with the "+".
    This will add a new folder to the list of files.
    Then, fill in ``notebooks`` as the name of this folder.
    It's helpful to keep the notebooks sequestered, since they're not **really** part of the final document.
    They're files we'll create as part of doing design work.

2.  Double-click the new ``notebooks`` folder in the left side to focus on that folder only.
    The top of the left panel will show the folder and `` / notebooks`` to show the current directory.
    Also, the top of the center panel will have the word ``notebooks`` to emphasize the current directory.

3.  In the center panel, under the "Notebook" banner, click the ``Python 3 (ipykernel)`` icon to create a new Notebook in the ``notebooks`` folder.

..  figure:: click_this.png
    :scale: 33%

    The icon for starting a new notebook.

This will open a new notebook with the name "Untitled".
The center panel will change from the Launcher to the new notebook.
It will look like this:

..  figure:: lab_2.png

    Jupyter Lab with a new, empty notebook.

We can put some Python stuff into this notebook.
For fun, put ``355 / 113`` into the cell.
Either use Shift-Return (on some keyboards it's Shift-Enter) to execute the cell.
Or click the ▶︎ button to execute the Python code in the cell.

The results of this Python expression are displayed below the cell.
This is about all the computer programming we're going to do.
In the next section, :ref:`tutorial.spell_dsl`, we'll look closely at the Spell DSL.

Step 4: Experiment with the notebook
------------------------------------

.. |save| image:: icon_save.png
         :alt: Save
         :height: 12pt

.. |new| image:: icon_new.png
         :alt: Insert New
         :height: 12pt

.. |cut| image:: icon_cut.png
         :alt: Cut this cell
         :height: 12pt

.. |copy| image:: icon_copy.png
         :alt: Copy this cell
         :height: 12pt

.. |paste| image:: icon_paste.png
         :alt: Paste from clipboard
         :height: 12pt

.. |run| image:: icon_run.png
         :alt: Run and advance
         :height: 12pt

.. |interrupt| image:: icon_interrupt.png
         :alt: Interrupt the kernel
         :height: 12pt

.. |restart| image:: icon_restart.png
         :alt: Restart the kernel
         :height: 12pt

.. |restart-run| image:: icon_restart_run_all.png
         :alt: Restart the kernel and run all cells
         :height: 12pt

.. |cell-type| image:: icon_cell_type.png
         :alt: Select the cell type menu
         :height: 12pt

.. |debug| image:: icon_debug.png
         :alt: Enable debugging
         :height: 12pt

.. |kernel| image:: icon_kernel.png
         :alt: Change to a different kernel
         :height: 12pt

.. |status| image:: icon_status.png
         :alt: The current status of the kernel: computing vs. idle
         :height: 12pt


On the top row of the "Untitled.ipynb" panel are string of icons for updating the notebook's content.

Here are the images:

..  figure:: notebook_panel.png
    :scale: 33%

    Icons for editing a notebook.

From left to right, here's what the icons mean:

-   |save| Save and create checkpoint
-   |new| Insert a cell below
-   |cut| Cut this cell
-   |copy| Copy this cell
-   |paste| Paste this cell from the clipboard
-   |run| Run this cell and advance
-   |interrupt| Interrupt the kernel
-   |restart| Restart the kernel
-   |restart-run| Restart the kernel and run all cells
-   |cell-type| Select the cell type from a drop-down menu with three choices: ``Code``, ``Markdown``, ``Raw``
-   |debug| Enable Debugger
-   |kernel| Switch kernel. This may have some alternative kernels listed.
-   |status| Kernel status. The open, empty circle means it's idle, waiting for something to run.

The first five of these -- |save|, |new|, |cut|, |copy|, and |paste| --  match word processing and text editing applications.

The rest are unique to Jupyter Lab.
Of these, the two that seem most useful are |run| and |restart-run| to run the various cells, executing the Python code, and creating the Spell definitions.

The |cell-type| menu has three values.

-   ``Code`` is the ordinary DSL statements we'll see in the next part of the tutorial. Spell and Character definitions.

-   ``Markdown`` is a language, like RST, allowing someone to write plain text and have a nicely formatted block of text in the cell.
    These cells are a good place to keep notes, comments, ideas, and other tidbits of information.

-   ``Raw`` cells simply have text, neither code to be evaluated nor markdown to be formatted. These, too, are places to keep notes, comments, ideas, and other tidbits of background or plans.

There's little reason to run the debugger, or change kernels.
The right-most icon, |status| will change sometimes.
Since the amount of computation is small, this won't change much.

Here are some things to do  to help build some skills with Jupyter Notebooks.

1.  Change the first cell to look like this:

    ..  code-block:: python

        pi = 355 / 113

    When it runs, there's no output. The value was stuffed into a variable.

2.  Add a second cell that looks like this:

    ..  code-block:: python

        print(pi)

This will have some output we can look at. Use the |restart-run| icon to run both cells and confirm that one creates an object, ``pi``, and the second cell prints the object.

This precisely parallels the way we'll work with Spell definitions.

Step 5: Save and Shutdown
-------------------------

When a notebook has a good spell definition, it needs to be saved.

A title of ``Untitled`` isn't really the best plan.

Right-click on the notebook name.
Either on the left, in the File Browser panel, or at the top of the notebook pabel.
A menu will pop up that has an item to Rename the notebook.

Pick a more useful name.

..  important::

    In the long run, the name needs to be one word composed of letters, digits, and ``_``'s, starting with a letter.

    The OS allows more complex names, but they can present obscure difficulties when working with other tools.

    It helps to think about the book being written, and the place the spells will occupy in that book.
    There may be multiple collections of spells and incantations.
    The collections may be organized by skill or rank.

    Perhaps a name like ``spells_alteration`` or ``spells_rank2`` would clearly identify the contents of the file.

When we're done with Notebooks, look at the ``File`` menu.
The last item is ``Shut Down``.

Use this menu item to stop the service. After the service stops, the browser window can be closed.

Conclusion
-----------

We've got a suite of sophisticated tools:

-   Sphinx
-   Spyder
-   Jupyter Lab

We've extended our Python environment with the ``opend6_tools`` with DSL's to help create Spells, Invocation, Items, Creatures, and Characters.

These tools support the **Change-Compute-Consider** cycle on two scales.

-   The individual Spell or Character scale: Use Jupyter Lab to change-compute-consider.

-   The document as a whole scale: Use Terminal command ``make html`` to rebuild the web page (or PDF or EPUB) with revised content.

In order to define spells, there's a Domain-Specific Language (DSL) that formalizes what's permitted in a spell.
It's time to learn :ref:`tutorial.spell_dsl` so we can define new spells.
