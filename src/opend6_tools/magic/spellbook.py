"""
This creates a Python Module with spell definitions.
The module will be a CLI application with a number of subcommands.

-   ``python spell_module.py display`` will display the spells in RST format.
    This is used by the publication process.

-   ``python spell_module.py debug 'name'`` will write debugging output for a spell.

..  autofunction:: build_app

..  autofunction:: make_spell_doctest

"""

import doctest
from pathlib import Path
import sys
from typing import Annotated, Literal, Any  # noqa: F401

from .output import *
from .workbook import *

import typer


def make_spell_doctest(spell_book: list[Spell], book_attr_name: str = "spells") -> None:
    """
    Given a book of spells, write a ``__test__`` definition, suitable for doctest.
    If the spells have an "other_aspect" that includes a "Difficulty" aspect,
    this can be extracted to make a target difficulty.

    :param spell_book: The book with a list of spells.
    :param book_attr_name: The attribute name for the book.
    """
    print("__test__ = {")
    for slot, spell in enumerate(spell_book):
        try:
            expected = int(spell.other_aspects["Difficulty"].format)  # type: ignore
        except KeyError:
            # Ugh. Difficulty not included.
            expected = 0
        print(
            f'    "{spell.name}": ">>> {book_attr_name}[{slot}].difficulty\\n{expected}",'
        )
    print("}")


def build_app(
    book: list[Spell],
    book_attr_name: str = "spells",
    *,
    rich_markup_mode: Literal["rich", "markdown"] | None = "rich",
) -> typer.Typer:
    spellbook_app = typer.Typer(
        help="Work with this collection of Spells.", rich_markup_mode=rich_markup_mode
    )

    @spellbook_app.command(name="display")
    def display_command(
        names: Annotated[
            list[str] | None, typer.Argument(help="Optional sell names to extract")
        ] = None,
        underline: Annotated[
            str | None, typer.Option(help="RST underline to use, default is '~'")
        ] = None,
    ):
        """Write RST-formatted details of all definitions to STDOUT."""
        options = {"spell_heading": underline} if underline is not None else {}
        if names:
            for spell in book:
                if spell.name in names:
                    detail(spell, **options)
        else:
            detail(book, **options)

    @spellbook_app.command(name="debug")
    def debug_command(
        names: Annotated[
            list[str] | None, typer.Argument(help="Spell name (or number)")
        ] = None,
        details: Annotated[bool, typer.Option(help="Show details")] = False,
    ):
        """Print debugging information for a specific definition to STDOUT"""
        debug(book, names, details)

    @spellbook_app.command(name="test")
    def run_test_command(make: bool = False, verbose: bool = False):  # pragma: no cover
        """Run the doctest examples, using the __test__ global.

        If the --make option is present, it writes a suggested __test__ definition.
        """
        module = sys.modules["__main__"]
        print(f"Testing {Path(cast(str, module.__file__)).relative_to(Path.cwd())}")
        if make:
            make_spell_doctest(book, book_attr_name)
            sys.exit()
        if not hasattr(module, "__test__"):
            print(
                "No __test__ found. If present, it must be **before** the build_app(). The --make option can be used to create a template."
            )
            sys.exit(2)
        else:
            failures, tests = doctest.testmod(module, verbose=verbose)
            sys.exit(failures)

    return spellbook_app
