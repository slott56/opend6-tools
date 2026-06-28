#################################################################
  DSLs and Tools to help with OpenD6 Spell and Character Design
#################################################################

This is a set of tools to help create OpenD6 world books, campaign books, scenarios, and even generate details for an encounter.
These tools help with spell design by computing difficulty automatically.
They also help with character design by computing the dice budget for attributes, skills, advantages, disadvantages, and special abilities.

..  important:: Not a single application

    This isn't a single "does-it-all" application; it's a collection of tools.

    Generally, the interactive computation is done in Jupyter Lab notebooks, where the designer can check computations of dice budgets and difficulties.
    The resulting character (or spell or whatever) can then be incorporated into documents written in ReStructuredText.
    The final, elegant HTML and PDF documents are produced by merging RST created by the designer with RST created by tools extracted from the notebooks.

If you're new to Python, the Usage section of the documentation provides additional step-by-step guidance for newbies.

Installation
============

There are two overall steps: adding necessary `OS Packages`_, and then installing the `OpenD6-Tools`_ software.

OS Packages
-----------

To create books and printable PDF character sheets, some additional OS components are required: **make**, **pkg-config**, **cairo**, and **pdflatex**.

(If you're a software developer, you may already have packages like **make**; if so, you don't to add them again.)

-   For **Macos**, install these with **homebrew**. See https://brew.sh to install this.

    Install the required OS packages:

    ..  code-block:: bash

        brew install make pkg-config cairo

    See https://tug.org/mactex/ for instructions on installing **pdflatex**.

-   Some **Linux** distributions include **make**, and **pkg-config**.
    Use the distribution's appropriate tools to install **make**, **pkg-config**, **cairo**.
    For details on this, see
    https://pycairo.readthedocs.io/en/latest/getting_started.html.

    See https://tug.org/texlive/ for instructions on installing **pdflatex**.

-   For **Windows**, consider using WSL to install the Linux components required.
    See https://learn.microsoft.com/en-us/windows/wsl/install.
    This provides an Ubuntu Linux in the Windows environment.
    Uwhich uses **apt** for installs. Here's the command:

    ..  code-block:: bash

        sudo apt install make libcairo2-dev pkg-config python3-dev

OpenD6-Tools
------------

To manage Python packages and virtual environments, it helps to start with the Astral **uv** tool. (https://docs.astral.sh/uv/)
Install **uv** first: https://docs.astral.sh/uv/getting-started/installation/.

With **uv**, create a project and a virtual environment, and install the ``opend6-tools``.

..  code-block:: bash

    uv init --bare --name "learning the tools"
    uv venv --prompt "mybook"
    source .venv/bin/activate

Once the environment is active, the prompt will change to include "(mybook)" to show the active virtual environment.
This final command will add the tools to the active virtual environment.

..  code-block:: bash

    uv add git+https://github.com/slott56/opend6-tools --upgrade

(Currently, this is not hosted in PyPI, only in GitHub.)

Quick Start
===========

You can play with character and spell definition using Jupyter Lab.
It helps to have some template notebooks.

Run the Python "cookiecutter" application to create an empty project with a number of handy files.

..  code-block:: bash

    uvx cookie-cutter cookiecutter-opend6-book


The cookie cutter creates a generic book directory, called ``OpenD6-Book``.
Feel free to rename it.
Change to this directory to work with the tools.

To play with the DSL's for spells and characters, start Jupyter Lab in the newly-created directory.
Open a Terminal Window, change to the newly-created directory,
and run the following command.

..  code-block:: bash

    jupyter lab


There are two templates available in the project's ``notebooks`` directory, one for characters, the other for spells.

Open these and start experimenting.

Usage
=====

Generally, spells (and characters and items) will be tiny Python applications, created using the OpenD6 Tools Domain-Specific Language (DSL).
These tiny applications do a few things:

1. Produce output suitable for inclusion into a Sphinx-based publication workflow.

2. Produce "debugging" output with lots of details about the thing you defined.

3. Have a test mode that allows you to be sure the difficulty meets expectations. This test mode can be handy when a seemingly small change has big consequences for the difficulty budget.

Often, you'll want to start with an easy-to-use interactive environment.
We suggest using ``jupyter lab`` to create ``notebooks`` with the definition.
These tools can then create the tiny applications from your notebooks.

See the documentation for the details on how to make use of these tools.

Developer Notes
===============

Use ``make`` to perform the various CI/CD tasks associated with software updates.

-   Run the unit-test suite.

    ..  code-block:: bash

        make test

-   Rebuild the documentation.

    ..  code-block:: bash

        make docs

-   Bump the version.

    ..  code-block:: bash

        uv version --bump dev

    OR, for a big, new change:

    ..  code-block:: bash

        uv version YYYY.mm.dd

    Please use CALVER version strings. See https://calver.org.

-   Build the new release for your own purposes.

    ..  code-block:: bash

        make build

You can then make a GitHub pull request to include changes into the main distribution.

If you have a copy of the tools **and** a set of TTRPG rules you're working on, you may want to build new tools and use them to publish some rules.

Generally, you can use this to upgrade the tools used for publishing.

..  code-block:: bash

    uv add git+https://github.com/slott56/opend6-tools --upgrade

If you have the repository checked-out locally, you can fetch from the filesystem location.
You might want to fetch updated tools from an adjacent directory,
or from the local clone of the github repository.

..  code-block:: bash

    uv add ../opend6-tools/ --upgrade

    uv add ~/github/local/opend6-tools --upgrade
