"""
This creates a Python Module with creature or character definitions.
The module will be a CLI application with a number of subcommands.

-   ``python creature_module.py display`` will display the spells in RST format.
    This is used by the publication process.

-   ``python creature_module.py debug 'name'`` will write debugging output for a spell.

..  autofunction:: build_app

..  autofunction:: make_character_doctest

..  autofunction::  parse_param_name

..  autoclass:: Format
    :members:

"""

import doctest
from pathlib import Path
import subprocess
from typing import cast, Literal, Annotated
import string
import sys

import typer

from .features import (
    Character,
    Creature,
    Agility,
    Intellect,
    Coordination,
    Acumen,
    Physique,
    Charisma,
    CharacterDict,
    CharacterBudget,
)
from .output import Format, FORMAT_OPTIONS, detail, parse_param_name, CharacterWriter
from .workbook import debug


def build_app(
    book: dict[str, Character | Creature],
    book_attr_name: str = "characters",
    *,
    rich_markup_mode: Literal["rich", "markdown"] | None = "rich",
) -> typer.Typer:
    characters_app = typer.Typer(
        help="Work with this collection of Characters (or Creatures).",
        rich_markup_mode=rich_markup_mode,
    )

    @characters_app.command(name="display")
    def display_command(
        format: Annotated[FORMAT_OPTIONS, typer.Option(case_sensitive=False)] = "TABLE",
    ):
        """Write details of all Character or Creature definitions.

        The default format is a markdown table that can be displayed in Jupyter Lab.
        """
        detail(book, Format[format])

    @characters_app.command(name="debug")
    def debug_command(
        names: Annotated[
            list[str] | None, typer.Argument(help="Character name (or number)")
        ] = None,
        check: bool = True,
    ):
        """Print debugging information for a specific definition to STDOUT"""
        debug(book, names)

    @characters_app.command(name="test")
    def test_command(make: bool = False, verbose: bool = False):  # pragma: no cover
        """Run the doctest examples, using the __test__ global.

        If the --make option is present, it writes a suggested __test__ definition.
        """
        module = sys.modules["__main__"]
        print(f"Testing {Path(cast(str, module.__file__)).relative_to(Path.cwd())}")
        if make:
            make_character_doctest(book, book_attr_name)
            sys.exit()
        if not hasattr(module, "__test__"):
            print(
                "No __test__ found. If present, it must be **before** the build_app(). The --make option can be used to create a template."
            )
            sys.exit(2)
        else:
            failures, tests = doctest.testmod(module, verbose=verbose)
            sys.exit(failures)

    @characters_app.command(name="blank")
    def blank_sheet_command(
        format: Annotated[
            FORMAT_OPTIONS, typer.Option(case_sensitive=False)
        ] = "PLAYER",
    ):
        """
        Print a blank character sheet in the desired format.

        The default format is HTML that can be run through **xhtml2pdf**.
        """
        blank = Character(
            agility=Agility(),
            intellect=Intellect(),
            coordination=Coordination(),
            acumen=Acumen(),
            physique=Physique(),
            charisma=Charisma(),
        )
        form = Format[format]
        detail(blank, form)

    @characters_app.command(name="pdf")
    def pdf_sheet_command(
        format: Annotated[FORMAT_OPTIONS, typer.Option(case_sensitive=False)] = "TABLE",
        names: Annotated[
            list[str] | None, typer.Argument(help="Character names")
        ] = None,
    ):
        """
        Create a PDF character sheet.

        There are several choices of formatting pipelines.

        -   RST ("TABLE" format) -> **rst2html** -> **xhtml2pdf**.

        -   HTML ("PLAYER" format) -> **xhtml2pdf**.

        -   LATEX ("LATEX" format) -> **pdflatex**.
        """

        def sanitize(filename: str) -> str:
            for char in string.punctuation + string.whitespace:
                filename = filename.replace(char, "_")
                while "__" in filename:
                    filename = filename.replace("__", "_")
            return filename

        form = Format[format]
        writer_class: type[CharacterWriter] = form.value
        w = writer_class()

        all_chars: CharacterDict
        match book:
            case Character() | Creature() as one_char:
                all_chars = {one_char.name: one_char}
            case list(list_char):
                all_chars = {c.name: c for c in list_char}
            case dict(dict_char):
                all_chars = dict_char

        for name in names or [""]:
            target_name = parse_param_name(all_chars, name)
            if not target_name:  # pragma: no cover
                sys.exit(f"Can't match {name!r} in {list(all_chars.keys())!r}")
            character = all_chars[target_name]
            if not character.name:
                filename = sanitize(target_name)
            else:
                filename = sanitize(character.name)
            match form:
                case Format.TABLE:
                    step_0 = (Path.cwd() / filename).with_suffix(".rst")
                    step_1 = Path(step_0).with_suffix(".html")
                    step_2 = Path(step_1).with_suffix(".pdf")
                    print(f"Creating {step_0}")
                    print(f"rst2html {step_0} {step_1}")
                    print(f"xhtml2pdf {step_1} {step_2}")
                    step_0.write_text(w.report(character))
                    subprocess.run(
                        ["rst2html", str(step_0), "--output", str(step_1)], check=True
                    )
                    subprocess.run(["xhtml2pdf", str(step_1), str(step_2)], check=True)
                case Format.PLAYER:
                    step_0 = (Path.cwd() / filename).with_suffix(".html")
                    step_1 = Path(step_0).with_suffix(".pdf")
                    print(f"Creating {step_0}")
                    print(f"xhtml2pdf {step_0} {step_1}")
                    step_0.write_text(w.report(character))
                    subprocess.run(["xhtml2pdf", str(step_0), str(step_1)], check=True)
                case Format.LATEX:
                    step_0 = (Path.cwd() / filename).with_suffix(".tex")
                    print(f"Creating {step_0}")
                    print(f"pdflatex {step_0}")
                    step_0.write_text(w.report(character))
                    subprocess.run(["pdflatex", str(step_0)], check=True)
                case _:  # pragma: no cover
                    sys.exit(f"not a valid format choice: {format!r}")

    return characters_app


def make_character_doctest(
    character_book: dict[str, Character | Creature],
    book_attr_name: str = "characters",
    budget: CharacterBudget = CharacterBudget.NO_BUDGET,
) -> None:
    """
    Given a book of Characters or Creatures, write a ``__test__`` definition, suitable for doctest.

    :param character_book: The book with a list of characters or creatures.
    :param book_attr_name: The attribute name for the book.
    :param budget: A CharacterBudget against which to test the character or creature.
    """
    expected = {
        "Attributes": "{budget.attributes} out of {budget.attributes}",
        "Skills": "{budget.skills} out of {budget.skills}",
        "Options": "{budget.options} out of {budget.options}",
    }
    print("__test__ = {")
    for slot, character in enumerate(character_book.values()):
        print(
            f'    "{character.name}": ">>> {book_attr_name}[{slot}].budget_check({budget})\\n{expected!r}",'
        )
    print("}")
