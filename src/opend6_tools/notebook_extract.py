"""
This application extracts Spell or Character definitions from a Jupyter Lab notebook file.
This will create a Python module that's part of the publication pipeline.

Input is a Notebook ``.ipynb`` file in which definitions have been created.
This includes ``Spell`` and all the various subclasses (``Cantrip``, ``Invocation``, etc.)
It also includes ``Character`` and all the various subclasses (``Creature``, etc.)

Output is one (or more) Python modules with the ``Spell`` or ``Creature`` assignment statements from the notebook.
Additionally, an application to emit RST is embedded as well as a unit test suite.

There are several variations on the extraction process:

-   Spells:

    -   One Python module with all ``Spell`` assignments.  The ``spellbook_app`` embedded in the module builds RST.

    -   Several Python modules, organized by the ``rank`` attribute of the ``Spell``.
        Ranks are 5-point bands centered on 5, 10, 15, 20, etc.
        The ``spellbook_app`` embedded in each output module is used to build the target RST-formatted file.

-   Characters and Creatures:

    -   One Python module with all ``Character`` assignments.
        The ``characters_app`` embedded in the module is used to build the target RST-formatted file.

    -   Several Python modules, organized by the ``realm`` attribute of the creature.

Each module extracted from a notebook is a stand-alone application, complete with imports and a typer application object.
For spells, the import is ``opend6_tools.magic2`` and the app is ``spellbook_app``.
For characters (and creatures), the import is ``opend6_tools.character`` and the app is ``characters_app``.

The extract looks for **all** cells that contain an assignment statement: ``name = TypeName(...)``.
It looks for :py:class:`opend6_tools.magic2.Spell` and all subclasses, including  ``Cantrip``, ``Miracle``, and ``Invocation``.
It also looks for :py:class:`opend6_tools.character.Character` and all subclasses, including ``Creature``.

Typical use is the following construct in a ``Makefile``.

..  code-block:: makefile

    vpath %.ipynb ../../notebooks

    # Create a Python Spell module from a Jupyter Notebook with the same name.
    %.py : %.ipynb
        python -m opend6_tools.notebook_extract spells $< > $@

The ``vpath`` directive is used because notebooks are often kept separate from the source directories for
the final document.

Help
====

Here's the help from the application:

..  code-block:: bash

    % python -m opend6_tools.notebook_extract --help

     Usage: python -m opend6_tools.notebook_extract [OPTIONS] COMMAND [ARGS]...

    ╭─ Options ─────────────────────────────────────────────────────────────────╮
    │ --install-completion          Install completion for the current shell.   │
    │ --show-completion             Show completion for the current shell, to   │
    │                               copy it or customize the installation.      │
    │ --help                        Show this message and exit.                 │
    ╰───────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ────────────────────────────────────────────────────────────────╮
    │ spells       Converts a notebook of spells to a Python module for         │
    │              publication. For ranked output, the target will have a       │
    │              "_rank_xx" suffix appended to the filename stem.             │
    │ characters   Converts a notebook of characters or creatures to a Python   │
    │              module for publication.                                      │
    ╰───────────────────────────────────────────────────────────────────────────╯

For the ``spells`` sub-command, the help looks like this::

     Usage: python -m opend6_tools.notebook_extract spells [OPTIONS] SOURCE

     Converts a notebook of spells to a Python module for publication. For
     ranked output, the target will have a "_rank_xx" suffix appended to the
     filename stem.

    ╭─ Arguments ───────────────────────────────────────────────────────────────╮
    │ *    source      PATH  notebook to convert [required]                     │
    ╰───────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────────────────────────────╮
    │ --output                          PATH  output file base name             │
    │ --book-variable                   TEXT  global variable to create with    │
    │                                         the list of spells/invocations    │
    │                                         [default: spells]                 │
    │ --ranked           --no-ranked          Organize by difficulty and rank   │
    │                                         [default: no-ranked]              │
    │ --help                                  Show this message and exit.       │
    ╰───────────────────────────────────────────────────────────────────────────╯

For the ``characters`` sub-command, here's the help output::

     Usage: python -m opend6_tools.notebook_extract characters
                [OPTIONS] SOURCE

     Converts a notebook of characters or creatures to a Python module for
     publication.

    ╭─ Arguments ───────────────────────────────────────────────────────────────╮
    │ *    source      PATH  notebook to convert [required]                     │
    ╰───────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────────────────────────────╮
    │ --output               PATH  output file base name                        │
    │ --book-variable        TEXT  global variable to create with the list of   │
    │                              characters/creatures                         │
    │                              [default: characters]                        │
    │ --groupby              TEXT  named attribute, e.g. realm                  │
    │ --help                       Show this message and exit.                  │
    ╰───────────────────────────────────────────────────────────────────────────╯


API Reference
=============

Top-Level Apps
--------------

The :py:func:`characters` function is an application that extracts Characters and Creatures from a Notebook.

..  autofunction:: characters

The :py:func:`spells` function is an application that extracts Characters and Creatures from a Notebook.

..  autofunction:: spells

Components
-----------

..  autoclass:: ModuleWriter
    :members:

..  autofunction:: subclass_iter

..  autoclass:: AssignmentVisitor
    :members:

..  autoclass:: Extractor
    :members:

..  autofunction:: eval_cell

..  autofunction:: write_spells_ranked

..  autofunction:: write_spells_unranked

..  autofunction:: write_characters

..  autofunction:: slug

..  autofunction:: write_characters_byRealm

"""

import ast
from collections.abc import Iterator, Iterable
from contextlib import redirect_stdout
from enum import StrEnum
import json
from pathlib import Path
from textwrap import dedent
from typing import Annotated
import importlib.metadata

import jinja2
import typer

from . import magic2
from . import character


class ModuleWriter:
    """Defines the templates for creating a Python module from a Jupyter Notebook extract.

    The :py:meth:`write_book` method creates the text body of a module.
    The result of this method can be written to a file with the ``.py`` extension.

    This template injects the CLI application and unit test suites into the spell module.
    """

    spell_template = dedent(
        '''\
        """
        Extract {{book_type}} from ``{{ title }}``.
        Created by V{{version}} of ``opend6_tools.notebook_extract`` 

        {% block comment %}
        When run as app with "display" argument, generates .RST-formatted details of all the {{book_type}}.
        
        With "debug" argument, prints debugging details for selected {{book_type}}.
        {% endblock %}
        """
        {% block import %}
        from opend6_tools.magic2 import *
        {% endblock %}

        {% for name, stmt in definitions %}
        {{ stmt }}
        {% endfor -%}
        
        {{ book_variable }} = [ 
            {% for name, stmt in definitions %}{{ name }}, {% endfor %}
        ]

        {% block apps %}
        if __name__ == "__main__":
            app = build_app({{ book_variable }})
            app()
        {% endblock %}

        __test__ = {
            {% if tests -%}
            {% for name, body in tests.items() %}
            {{ "{!r}".format(name) }}: {{ "{!r}".format(body) }},
            {% endfor %}
            {% else %}
            "placeholder": ">>> pass\\n\\n"
            {% endif %}
        }
        '''
    )
    character_template = dedent("""\
        {% extends "spells.py" %}
        {% block import %}
        from opend6_tools.character import *
        {% endblock %}
        {% block comment %}
        When run as app with "sheet" argument, generates .RST-formmat player character sheets for all the {{book_type}}.
        
        With "display" argument, generates .RST-formatted short-form of all the {{book_type}}.
        
        With "debug" argument, writes debugging details for selected {{book_type}}.
        {% endblock %}
    """)

    @staticmethod
    def book_slug(title: str) -> str:
        """Convert the book title to a slug without spaces.

        :param title: the Title
        :returns: string slug with spaces replaced by "_".
        """
        return title.lower().replace(" ", "_")

    def __init__(self) -> None:
        """
        Initalize a ModuleWriter instance.
        """
        self.version = importlib.metadata.version("opend6-tools")
        self.jinja_env = jinja2.Environment()
        self.jinja_env.filters["slug"] = self.book_slug
        self.jinja_env.loader = jinja2.DictLoader(
            {
                "spells.py": self.spell_template,
                "characters.py": self.character_template,
            }
        )

    def write_book(
        self,
        *,
        book_type: str = "spells",
        title: str = "Untitled",
        definitions: Iterable[tuple[str, str | None]],
        book_variable_name: str = "spells",
        tests: dict[str, str] | None = None,
    ) -> str:
        """Essential output of a book of Spells, Characters, Creatures, etc.

        :param book_type: The kind of book to be created.
        :param title: The title to include in the Template.
        :param definitions: The source text for Spells, Characters, etc.
        :param book_variable_name: a global variable to assign as the list of defined values.
        :param tests: a mapping used to  build a doctest ``__tests__`` global.

        :returns: The string to write.
        """
        template = self.jinja_env.get_template(f"{book_type.lower()}.py")
        # Render the module as Python code.
        return template.render(
            version=self.version,
            definitions=definitions,
            title=title,
            tests=tests,
            book_type=book_type.title(),
            book_variable=book_variable_name,
        )


def subclass_iter(some_class: type) -> Iterator[type]:
    """Emit a class and all it's defined subclasses."""
    yield some_class
    for sub_class in some_class.__subclasses__():
        yield from subclass_iter(sub_class)


class AssignmentVisitor(ast.NodeVisitor):
    """
    Save the assignment statements from the various cells in the notebook.

    The output from the :meth:`name_definition_iter` method is a sequence of tuples: ``("name", "name = Spell()")`` for each Spell found.
    The internal ``target_classes`` is the set class names to recognize.
    """

    def __init__(self, source: str, base_class: type = magic2.Spell) -> None:
        """
        Initialie an AssignmentVisitor instance.

        :param source: The source text for the Python module.
        :param base_class: The base class to filter on.
        """
        self.source = source
        self.statements: list[ast.Assign] = []
        self.target_classes = set(sc.__name__ for sc in subclass_iter(base_class))

    def name_definition_iter(self) -> Iterator[tuple[str, str | None]]:
        """Iterates over names and definitions found in the source code.

        :returns: sequence of tuple (variable, code block)
        """
        for stmt in self.statements:
            targets = [t.id for t in stmt.targets if isinstance(t, ast.Name)]
            yield (targets[0], ast.get_source_segment(self.source, stmt))

    def visit_Assign(self, node: ast.Assign) -> None:
        """Visits :py:class:`ast.Assign` statements.

        :param node: the node to visit.
        """
        match node.value:
            case ast.Call() as call if (
                isinstance(call.func, ast.Name) and call.func.id in self.target_classes
            ):
                self.statements.append(node)
                return
            case _:
                pass


class Extractor:
    """
    Find the code cells and extract the sequence of assignment statements.
    These are (generally) the spell definitions.

    Uses :py:class:`AssignmentVisitor` to locate the statements.
    """

    def __init__(self, source: Path, target_type: type = magic2.Spell) -> None:
        self.source = source
        self.target_type = target_type
        with open(source) as nb_file:
            self.notebook = json.load(nb_file)

    def definition_iter(self) -> Iterator[tuple[str, str | None]]:
        """Extract the DSL definition statements from an IPYNB notebook file.
        Iterates over tuples of the form ``("name", "name = Spell()")`` for each Spell found.
        The ``AssignmentVisitor`` filters to be sure these are the DSL definitions based on Spells and Characters.
        """
        code_cells = (
            (number, cell)
            for number, cell in enumerate(self.notebook["cells"])
            if cell["cell_type"] == "code"
        )
        for number, cell in code_cells:
            source_text = "".join(cell["source"])
            code = ast.parse(source_text, f"{self.source.stem}[{number}]", "exec")
            asn_visitor = AssignmentVisitor(source_text, self.target_type)
            asn_visitor.visit(code)
            yield from asn_visitor.name_definition_iter()


class EvalContext(StrEnum):
    MAGIC = "from opend6_tools.magic2 import *"
    CHARACTERS = "from opend6_tools.character import *"


def eval_cell(
    name: str, assignment: str, variety: EvalContext
) -> tuple[str, magic2.Spell | character.Character]:
    """
    Evaluate an assignment statement to a ``Spell`` (or ``Character``) object.
    This uses an explicit filter rule to check for ``Spell`` creation.
    The default rule is ``isinstance(obj, Spell)``

    :param name: variable name from the source
    :param assignment: Full assignment statement ``name = Spell()``.
    :param variety: One of the :py:class:`EvalContext` values: MAGIC or CHARACTERS.
    :returns: tuple of (name, object)
    """
    global_defs = {}
    local_vars = {}
    exec(variety.value, global_defs, local_vars)
    exec(assignment, global_defs, local_vars)
    if isinstance(local_vars[name], magic2.Spell):
        exec(f"{name}.finalize()", global_defs, local_vars)
    return name, local_vars[name]


def write_spells_ranked(
    book_variable: str,
    output: Path | None,
    source_name: str,
    spell_source: list[tuple[str, str | None]],
    writer: ModuleWriter,
) -> None:
    """Ranks spells and write multiple files.

    :param book_variable: global variable name to use
    :param output: output Path or None to write to stdout
    :param source_name: Name of source notebook
    :param spell_source: list of tuple[str, str] with spell name and assignment statement
    :param writer: ModuleWriter instance to write.
    """
    source_map = dict(spell_source)  # map variable name -> statement
    spell_context: dict[str, magic2.Spell | character.Character | None] = dict(
        eval_cell(variable, stmt, EvalContext.MAGIC)
        for variable, stmt in source_map.items()
        if stmt
    )  # map variable name -> Spell object
    spell_name_to_source = {
        spell.name: (variable, source_map[variable])
        for variable, spell in spell_context.items()
        if spell
    }  # map Spell name -> (variable, statement) source
    ranked = magic2.workbook_rank(spell_context)
    for rank, spell_list in sorted(ranked.items()):
        rank_list = [spell_name_to_source[spell.name] for spell in spell_list]
        tests = {
            name: f">>> -2 <= {name}.difficulty - {rank * 5} < +3\nTrue\n" for name, _ in rank_list
        }
        book_body = writer.write_book(
            book_type="Spells",
            title=f"{source_name} rank {rank} {book_variable}",
            definitions=rank_list,
            book_variable_name=book_variable,
            tests=tests,
        )
        if output:
            rank_name = output.with_stem(f"{output.stem}_Rank{rank}")
            with open(rank_name, "w") as target:
                with redirect_stdout(target):
                    print(book_body)
        else:
            print(f"# RANK {rank}")
            print()
            print(book_body)
            print()


def write_spells_unranked(
    book_variable: str,
    output: Path | None,
    source_name: str,
    spell_source: list[tuple[str, str | None]],
    writer: ModuleWriter,
) -> None:
    """Writes extracted spells to a single file.

    :param book_variable: global variable name to use
    :param output: output Path or None to write to stdout
    :param source_name: Name of source notebook
    :param spell_source: list of tuple[str, str] with spell name and assignment statement
    :param writer: ModuleWriter instance to write.
    """
    book_body = writer.write_book(
        book_type="Spells",
        title=source_name,
        definitions=spell_source,
        book_variable_name=book_variable,
        tests={},
    )
    if output:
        with open(output, "w") as target:
            with redirect_stdout(target):
                print(book_body)
    else:
        print(book_body)


def write_characters(
    book_variable: str,
    output: Path | None,
    source_name: str,
    character_source: list[tuple[str, str | None]],
    writer: ModuleWriter,
) -> None:
    """Writes extracted characters to a single file.

    :param book_variable: global variable name to use
    :param output: output Path or None to write to stdout
    :param source_name: Name of source notebook
    :param character_source: list of tuple[str, str] with spell name and assignment statement
    :param writer: ModuleWriter instance to write.
    """
    book_body = writer.write_book(
        book_type="Characters",  # or Creatures
        title=source_name,
        definitions=character_source,
        book_variable_name=book_variable,
        tests={},
    )
    if output:
        with open(output, "w") as target:
            with redirect_stdout(target):
                print(book_body)
    else:
        print(book_body)


def slug(group_name: str) -> str:
    """Convert a section title of a Character workbook into a summary slug.

    :param group_name: The text of the "realm" attribute of a :py:class:`character.Character` or :py:class:`character.Creature`.
    :returns: A slug without spaces or punctuation.
    """
    return group_name.lower().replace(" ", "").replace(",", "").replace("æ", "ae")


def write_characters_byRealm(
    book_variable: str,
    output: Path | None,
    source_name: str,
    character_source: list[tuple[str, str | None]],
    writer: ModuleWriter,
) -> None:
    """Groups Characters by realm attribute and write multiple files.

    :param book_variable: global variable name to use
    :param output: output Path or None to write to stdout
    :param source_name: Name of source notebook
    :param spell_source: list of tuple[str, str] with character name and assignment statement
    :param writer: ModuleWriter instance to write.
    """
    source_map = dict(character_source)  # map variable name -> statement
    char_context: dict[str, magic2.Spell | character.Character | None] = dict(
        eval_cell(variable, stmt, EvalContext.CHARACTERS)
        for variable, stmt in source_map.items()
        if stmt
    )  # map variable name -> Spell object
    char_name_to_source = {
        spell.name: (variable, source_map[variable])
        for variable, spell in char_context.items()
        if spell
    }  # map Spell name -> (variable, statement) source
    grouped = character.workbook_groupBy(char_context, group_rule=lambda char: char.realm)
    for group, char_list in sorted(grouped.items()):
        group_list = [char_name_to_source[char.name] for char in char_list]
        book_body = writer.write_book(
            book_type="Characters",
            title=f"{source_name} realm {group} {book_variable}",
            definitions=group_list,
            book_variable_name=book_variable,
        )
        if output:
            rank_name = output.with_stem(f"{output.stem}_{slug(group)}")
            with open(rank_name, "w") as target:
                with redirect_stdout(target):
                    print(book_body)
        else:
            print(f"# REALM {group}")
            print()
            print(book_body)
            print()


app = typer.Typer()


@app.command(name="spells")
def spells(
    source: Annotated[Path, typer.Argument(help="notebook to convert")],
    output: Annotated[Path | None, typer.Option(help="output file base name")] = None,
    book_variable: Annotated[
        str,
        typer.Option(help="global variable to create with the list of spells/invocations"),
    ] = "spells",
    ranked: Annotated[bool, typer.Option(help="Organize by difficulty and rank")] = False,
) -> None:
    """Converts a notebook of spells to a Python module for publication.
    For ranked output, the target will have a "_rank_xx" suffix appended to the filename stem.
    """
    writer = ModuleWriter()
    extractor = Extractor(source, target_type=magic2.Spell)
    spell_source = list(extractor.definition_iter())

    if ranked:
        write_spells_ranked(book_variable, output, source.name, spell_source, writer)
    else:
        write_spells_unranked(book_variable, output, source.name, spell_source, writer)


@app.command(name="characters")
def characters(
    source: Annotated[Path, typer.Argument(help="notebook to convert")],
    output: Annotated[Path | None, typer.Option(help="output file base name")] = None,
    book_variable: Annotated[
        str,
        typer.Option(help="global variable to create with the list of characters/creatures"),
    ] = "characters",
    groupby: Annotated[str, typer.Option(help="named attribute, e.g. realm")] = "",
) -> None:
    """Converts a notebook of characters or creatures to a Python module for publication."""
    writer = ModuleWriter()
    extractor = Extractor(source, target_type=character.Character)
    character_source = list(extractor.definition_iter())

    if groupby.lower() == "realm":
        write_characters_byRealm(book_variable, output, source.name, character_source, writer)
    else:
        write_characters(book_variable, output, source.name, character_source, writer)


if __name__ == "__main__":
    app()
