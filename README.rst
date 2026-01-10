# Tools to support designing spells and characters in OpenD6 games

## Usage

This is a set of tools to help publish OpenD6 world books, campaign books, scenarios, and even generate details for an encounter.

[!IMPORTANT]
This isn't an application. It's a collection of tools.
If you're new to Python, the usage section of the documentation  provides some step-by-step guidance for newbies.

## Usage

Generally, you'll be creating a collection of tiny Python applications. Each application will define one (or more) Characters, Creatures, Spells, Items, etc.
The tiny applications do a few things:

1. Produce output suitable for inclusion into a Sphinx-based publication workflow.

2. Produce "debugging" output with lots of details about the thing you defined.

Often, you'll want to start with an easy-to-use interactive environment.
We suggest using ``jupyter lab`` to create ``notebooks`` with the definition.
These tools can then create the tiny applications from your notebooks.

See the documentation for the details on how to make use of these tools.

## Developer Notes

Use ``make`` to perform software updates.

-   Unit-test.

    ..  code-block:: bash

        make test

-   Docs.

    ..  code-block:: bash

        make docs

-   Bump version.

    ..  code-block:: bash

        uv version --bump dev

    OR, for a big, new change. Please us CALVER version control.

    ..  code-block:: bash

        uv version YYYY.mm.dd

-   Build the new release for your own purposes.

    ..  code-block:: bash

        make build

You can then make a GIT pull request to include this in the main distribution.
