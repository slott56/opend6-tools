"""
Parse fantasy_rulebook/spells.txt to create a formal Spell() collection.
Also, parse fantasy_rulebook/miracles.txt to create a Miracle() collection.

Input is the (edited) text from the source, D6_Fantasy_v1.3_weg51013OGL.pdf.
This is riddled with odd problems from the OCR process.

An example spell.

    COUNTERMAGIC
    Skill Used: Alteration
    Difficulty: 19
    Effect: 29 (compare to skill total of spell countering)
    Range: 60 meters ( +9)
    Speed: +9
    Duration: 1 round (+4)
    Casting Time: 1 round (-4)
    Other Aspects:
    Concentration (-1): 3 seconds with mettle difficulty of7
    Gesture (-1): Wave hand through air as if wiping away something (simple)
    Incantation (-3): "Your hold is broken!" (sentence, said loudly)
    Other Conditions (-4): One spell, which the caster must specify when casting this spell
    Tue caster concentrates on the spell he wishes to counter, waving
    his band and shouting the required incantation. The effect's value
    plus the result points bonus are compared to the skill total used to
    create the targeted spell If the countermagic number is equal to or
    higher than the target spell's skill total, the spell is broken.


Output is the spell-books as ``*.py`` files.
An app can import these and produces RST-formatted content to include in the final document.
Or ``Makefile`` can emit ``shared/whatever.txt`` files.

The final ``Spells.rst`` will be:

-   ``..    include::`` commands for the various schools of magic and their sidebars.

-   ``..    admonition::`` for the admonition extracted from spells.txt.

The final ``Miracles.rst`` will have the miracles replaced with ``..  include::`` directives.
"""

from collections import Counter
from collections.abc import Iterator
from contextlib import redirect_stdout
from enum import Enum
from pathlib import Path
from pprint import pprint
import sys

from humre import *

import magic1 as magic


# Canvas the text to uncover the keywords.
# Other uppercase[\w ]+: patterns exist, but are singletons.
SPELL_KEYWORDS = {
    "Skill",
    "Arcane Knowledge",
    "Difficulty",
    "Effect",
    "Range",
    "Speed",
    "Duration",
    "Casting Time",
    "Other Aspects",
    "Other Conditions",
    "Wound levels",
    "Bonus",
}


def parse_spell(clean_text: str) -> Iterator[tuple[str, list[str], ...]]:
    """Overall Syntax for the collection of spell books.
    This is the line-level structure of a Spell's text.
    Further parsing is required to emit an actual Spell from this.

    The tuple has name, aspect, other, and text blocks.
    The edge between other and text is blurry because the "other" lines are not strictly single-line items.

    ..  code-block:: enbf

        book = title { spell } ;

        title = words NL underline

        spell = name { aspect } { other } { text line } ;

        name = letters-and-spaces ;

        aspect = keyword ":" [text] ;

        other =   text "(" text ")" ":" text ;

        text line = anything ;

    What's important is the ``aspect`` production is the first thing we can recognize in a spell.
    It's preceded by a name.
    A special "Other Aspects" or "Other Conditions" keyword delimits the "other" section.

    We have four states:

    -   Pre-Aspect -- each line may be a title.
    -   Aspect -- each line is an aspect
    -   Other -- each line is an other aspect or other condition
    -   Post-Other -- each line is text

    """
    keyword_pattern = starts_with(group(UPPERCASE, one_or_more(chars(WORD, " "))), ":")
    other_pattern = (
        one_or_more(chars(WORD, " -"))
        + OPEN_PAREN
        + one_or_more(nonchars(CLOSE_PAREN))
        + CLOSE_PAREN
        + ":"
        + EVERYTHING
    )
    # other_pattern = "[\w -]+\([+-/\d]+\):"

    class State(Enum):
        Pre_Aspect = 0  # Before the first meaningful line
        Aspect = 1
        Other = 2
        Post_Other = 3

    parse_state = State.Pre_Aspect
    candidate_name = ""
    aspects = []
    other = []
    text = []
    floater = ""

    for line in clean_text.splitlines():
        match parse_state:
            case State.Pre_Aspect:
                if (m := re.match(keyword_pattern, line)) and m.group(
                    1
                ) in SPELL_KEYWORDS:
                    # print(parse_state, m)
                    parse_state = State.Aspect
                    aspects = [line]
                else:
                    # if line.startswith("-") and line.endswith("-"):
                    #     print(candidate_name)
                    #     print(line)
                    #     print()
                    # print(parse_state, m)
                    candidate_name = line
            case State.Aspect:
                if m := re.match(keyword_pattern, line):
                    # print(parse_state, m)
                    if m.group(1) in SPELL_KEYWORDS:
                        if m.group(1) in {"Other Aspects", "Other Conditions"}:
                            # This line is dropped.
                            floater = ""
                            parse_state = State.Other
                        else:
                            aspects.append(line)
                else:
                    # print(parse_state, m)
                    floater = ""
                    parse_state = State.Post_Other
            case State.Other:
                if m := re.match(other_pattern, line):
                    # print(parse_state, m)
                    # Consume the previous floater.
                    if floater:
                        if other:
                            other[-1] += " " + floater
                        else:
                            other = [floater]
                        floater = ""
                    other.append(line)
                else:
                    # print(parse_state, m)
                    # Not always -- some "other" lines run on to multiple physical lines. Ugh.
                    if floater:
                        # Two lines of floater? Done with Other
                        text.append(floater)
                        text.append(line)
                        floater = ""
                        parse_state = State.Post_Other
                    else:
                        floater = line
            case State.Post_Other:
                if (m := re.match(keyword_pattern, line)) and m.group(
                    1
                ) in SPELL_KEYWORDS:
                    # print(parse_state, m)
                    # New Spell. Last line of text is candidate name.
                    if text:
                        next_candidate_name = text.pop(-1)
                    elif other:
                        next_candidate_name = other.pop(-1)
                    else:
                        print(
                            f"can't parse\n{candidate_name}\n{aspects}\n{other}\n{text}\n{line}"
                        )
                        raise ValueError()
                    yield (candidate_name, aspects, other, text)
                    candidate_name = next_candidate_name
                    aspects = []
                    other = []
                    text = []
                    parse_state = State.Aspect
                else:
                    # print(parse_state, m)
                    if line.startswith("-") and line.endswith("-"):
                        # print(text[-1])
                        # print(line)
                        # print()
                        next_candidate_name = text.pop(-1)
                        yield (candidate_name, aspects, other, text)
                        candidate_name = next_candidate_name
                        aspects = []
                        other = []
                        text = []
                        parse_state = State.Aspect
                    else:
                        text.append(line)
            case _:
                raise RuntimeError
    yield (candidate_name, aspects, other, text)


def make_spell(
    name: str, aspects_text: list[str], other_text: list[str], text: list[str]
) -> magic.Spell:
    keyword_pattern = group(one_or_more(chars(WORD, " "))) + ":" + group(EVERYTHING)

    other_pattern = (
        group(one_or_more(chars(WORD, " -")))
        + OPEN_PAREN
        + group(one_or_more(nonchars(CLOSE_PAREN)))
        + CLOSE_PAREN
        + ":"
        + group(EVERYTHING)
    )

    effect_pattern = (
        group(one_or_more(chars(DIGIT)))
        + one_or_more(WHITESPACE)
        + OPEN_PAREN
        + group(EVERYTHING)
        + CLOSE_PAREN
    )
    difficulty_pattern = (
        group(EVERYTHING)
        + zero_or_more(WHITESPACE)
        + OPEN_PAREN
        + group(one_or_more(nonchars(CLOSE_PAREN)))
        + CLOSE_PAREN
    )
    label_pattern = (
        group(one_or_more(chars(WORD, " -")))
        + chars(OPEN_PAREN, ":")
        + group(EVERYTHING)
    )

    aspects: dict[str, dict] = {}
    for line in aspects_text:
        if match := re.match(keyword_pattern, line):
            label = match.group(1).strip()
            value = match.group(2).strip()
        else:
            raise ValueError(f"{line!r} in {name!r} {aspects_text=!r}")
        if label == "Difficulty":
            asp = dict(format=value)
        elif effect_match := re.match(effect_pattern, value):
            # Special case of ``\d+\s+.*``  for Effect
            asp = dict(
                format=effect_match.group(2).strip(),
                base_difficulty=int(effect_match.group(1)),
            )
        elif aspect_match := re.match(difficulty_pattern, value):
            # Common case: Word with no ``(\d)`` or word with ``(+\d)``
            try:
                asp = dict(
                    format=aspect_match.group(1),
                    base_difficulty=int(aspect_match.group(2).replace(" ", "")),
                )
            except ValueError as ex:
                print(f"{name=}, {line=}", file=sys.stderr)
                raise ValueError(f"{ex.args} in {aspects_text}, {line=}")
        else:
            asp = dict(format=value)
        aspects[label] = magic.Aspect(**asp)

    other: dict[str, dict] = {}
    for line in other_text:
        if match := re.match(other_pattern, line):
            label = match.group(1).strip()
            difficulty_text = match.group(2).replace(" ", "")
            notes = match.group(3).strip()
        else:
            raise ValueError(f"{line!r} in {name!r} {other_text=!r}")
        try:
            difficulty = int(difficulty_text)
        except ValueError as ex:
            if "/" in difficulty_text:
                # Actually 2 distinct spells with distinct variant aspects_text.
                print(
                    f"** Problem with {line!r} in {name!r} {other_text=!r}",
                    file=sys.stderr,
                )
                values = difficulty_text.split("/")
                notes = f"{difficulty_text} {notes}"
                difficulty = int(values[0])
            else:
                print(f"{name=}, {line=}", file=sys.stderr)
                raise ValueError(f"{ex.args} in {other_text}, {line=}")
        # Create an Aspect() for word (+-\d): words
        asp = dict(format=notes, base_difficulty=difficulty)
        other[label] = magic.Aspect(**asp)

    if "Skill" in aspects:
        skill = aspects.pop("Skill").format
    else:
        skill = "unknown"
    spell = dict(
        name=name,
        effect=aspects.pop("Effect", magic.Aspect(format="template")),
        duration=aspects.pop("Duration", magic.Aspect(format="template")),
        range=aspects.pop("Range", magic.Aspect(format="template")),
        casting_time=aspects.pop("Casting Time", magic.Aspect(format="template")),
        skill=skill,
    )
    spell["other_aspects"] = aspects | other
    spell["notes"] = "\n".join(text)
    return magic.Spell(**spell)


def main():
    # source = Path.cwd().parent / "fantasy_rulebook" / "spells.txt"
    # drop = 16
    source = Path.cwd().parent / "fantasy_rulebook" / "miracles.txt"
    drop = 0

    # Drop some initial lines.
    spell_text = "\n".join(source.read_text().splitlines()[drop:])

    # Split into a book for each school.

    def book_split(text: str) -> Iterator[tuple[str, slice]]:
        """Emits sequence of schools to create separate spell books."""
        title_pattern = (
            NEWLINE
            + group(one_or_more(chars(WORD + " ")))
            + NEWLINE
            + one_or_more(chars("="))
            + NEWLINE
        )
        title: str = ""
        previous_end: int = 0
        for heading in re.finditer(title_pattern, text, re.MULTILINE | re.DOTALL):
            if title and previous_end:
                # print(title)
                yield title, slice(previous_end, heading.start())
            previous_end = heading.end()
            title = heading.group(1)
        # print(title)
        yield title, slice(previous_end, len(text))

    FORCE = False

    for title, region in book_split(spell_text):
        if not title:
            continue
        title, *_ = title.split()
        # school_path = Path.cwd().parent / "tools" / f"fantasy_{title}.py"
        school_path = Path.cwd().parent / "tools" / f"fantasy_miracle_{title}.py"
        if school_path.exists() and not FORCE:
            print(f"Will not overwrite {school_path}")
            continue
        print(f"Creating {school_path.relative_to(Path.cwd().parent)}")
        text_blocks = list((parse_spell(spell_text[region])))
        # pprint(text_blocks)
        with open(school_path, "w") as school_file:
            with redirect_stdout(school_file):
                spells = (
                    make_spell(*spell_line_tuple)
                    for spell_line_tuple in (parse_spell(spell_text[region]))
                )
                print(magic.module(title, spells))


if __name__ == "__main__":
    main()
