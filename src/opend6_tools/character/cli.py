"""
Main app to make a blank character sheet.

..  autofunction:: main

..  todo:: Consider generating random character, also.
"""

from .output import *
from .features import *

import typer


def main(
    format: Annotated[FORMAT_OPTIONS, typer.Option(case_sensitive=False)] = "TABLE",
) -> None:
    """Produce a blank character sheet."""
    blank = Character()
    form = Format[format]
    detail(blank, form)


app = typer.Typer()
app.command()(main)

if __name__ == "__main__":  # pragma: no cover
    app()
