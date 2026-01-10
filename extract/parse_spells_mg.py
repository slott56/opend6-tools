"""
Parse magic_guide/spells.txt to create a number of documents.

Input is the (lightly edited) text from the source, D6_Magic_weg51024OGL.pdf.

An example spell.

    Chronal Fog
    Skill: Conjuration
    Arcane Knowledge: magic, time
    Difficulty: 11
    Effect: 15 (Armor Value of 5D, physical only)
    Range: Self (+0)
    Speed: Instantaneous (+0)
    Duration: 1 minute (+9)
    Casting Time: 1 round (-4)
    Other Aspects:
    Area Effect (+10): Sphere with radius of 2 meters
    Components (-8): Three grams of mica flakes (uncommon,
    destroyed)
    Focused (+4): On caster
    Gestures (-2): Twirls arms around while dispersing the mica
    flakes to form a ring around the caster (fairly simple)
    Incantations (-3): “Mists of time, clouds of fate, shield me
    now, for the hour is late!” (sentence, loud)
    Upon the dispersal of the spell component, a foglike haze
    surrounds the magic wielder. The haze is formed by the chronal
    echoes that emanate from the fluctuating temporal fields that
    the mage summons to deflect physical damage. The barrier
    is centered upon the caster and provides an Armor Value of
    5D against all types of physical (not mental) attacks. The
    fog effect of the spell offers the same visibility limitations
    of light fog for both the magic wielder and those who wish
    to peer through it.

Note the Elementals section has Templates and long blocks of subsidary text.

Outputs include:

1.  The sidebar text blocks as a ``sidebars.rst`` file.
    Some are supplemental tables for a specific spell.
    Some are introductory material for a specific school of magic.

2.  The spell-books as ``*.py`` files.
    An app can import these and produces RST-formatted content to include in the final document.
    Or ``Makefile`` can emit ``shared/whatever.txt`` files.

The final ``Spells.rst`` will be:

-   lines 1-167 of spells.txt

-   ``..    include::`` commands for the various schools of magic and their sidebars.


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


def de_sidebar(spell_text: str) -> tuple[list[slice], str]:
    """
    Drop the (((sidebar)))...(((sidebar))) blocks -- save these for later.

    Drop the (((illo))) call for an illustration.

    What remains is good spell text.
    """

    open_pat = exactly(3, OPEN_PAREN)
    close_pat = exactly(3, CLOSE_PAREN)
    marker = open_pat + one_or_more(nonchars(CLOSE_PAREN)) + close_pat

    start = 0
    regions = []
    sidebars = []
    sidebar_start = None
    for match in re.finditer(marker, spell_text, re.MULTILINE | re.DOTALL):
        if any(w in match.group() for w in {"illo", "illustration"}):
            # DROP match.start() to match.end()
            regions.append(slice(start, match.start()))
            start = match.end()
        else:
            if not sidebar_start:
                # start of (((sidebar)))
                # DROP match.start() to match.end()
                sidebar_start = match.start()
                regions.append(slice(start, match.start()))
            else:
                # end of (((sidebar)))
                # DROP up to match.end()
                sidebars.append(slice(sidebar_start, match.end()))
                start = match.end()
                sidebar_start = None
    regions.append(slice(start, len(spell_text)))

    good = "\n".join(spell_text[k] for k in regions)

    return sidebars, good


# Canvas the text to uncover the keywrods.
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
                    if line.startswith("-") and line.endswith("-"):
                        print(candidate_name)
                        print(line)
                        print()
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
                        next_candidate_name = text[-1]
                        del text[-1]
                    elif other:
                        next_candidate_name = other[-1]
                        del other[-1]
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
                        print(text[-1])
                        print(line)
                        print()
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
            asp = dict(
                format=aspect_match.group(1), base_difficulty=int(aspect_match.group(2))
            )
        else:
            asp = dict(format=value)
        aspects[label] = magic.Aspect(**asp)

    other: dict[str, dict] = {}
    for line in other_text:
        if match := re.match(other_pattern, line):
            label = match.group(1).strip()
            difficulty_text = match.group(2).strip()
            notes = match.group(3).strip()
        else:
            raise ValueError(f"{line!r} in {name!r} {other_text=!r}")
        try:
            difficulty = int(difficulty_text)
        except ValueError:
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
                raise
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
    source = Path.cwd().parent / "magic_guide" / "spells.txt"
    # Drop the first 166 lines, start with 166.
    spell_text = "\n".join(source.read_text().splitlines()[166:])

    # Extract the sidebars.
    # Remove the illustration markers.
    sidebars, clean_spell_text = de_sidebar(spell_text)

    sidebar_path = Path.cwd().parent / "magic_guide" / "sidebars.txt"
    with open(sidebar_path, "w") as sidebar_file:
        with redirect_stdout(sidebar_file):
            for drop in sidebars:
                print(spell_text[drop])
                print()

    # Split into a book for each school.

    def book_split(text: str) -> Iterator[tuple[str, slice]]:
        """Emits sequence of schools to create separate spell books."""
        title_pattern = (
            NEWLINE
            + group(one_or_more(chars(WORD)))
            + NEWLINE
            + one_or_more(chars("-"))
            + NEWLINE
        )
        title: str = ""
        previous_end: int = 0
        for heading in re.finditer(title_pattern, text, re.MULTILINE | re.DOTALL):
            if title and previous_end:
                yield title, slice(previous_end, heading.start())
            previous_end = heading.end()
            title = heading.group(1)
        yield title, slice(previous_end, len(text))

    for title, region in book_split(clean_spell_text):
        school_path = Path.cwd().parent / "tools" / f"{title}.py"
        if school_path.exists():
            print(f"Will not overwrite tools/{title}.py")
            continue
        print(f"Creating tools/{title}.py")
        with open(school_path, "w") as school_file:
            with redirect_stdout(school_file):
                spells = (
                    make_spell(*spell_line_tuple)
                    for spell_line_tuple in (parse_spell(clean_spell_text[region]))
                )
                magic.module(title, spells)
                #
                # print('"""')
                # print(f"{title}\n{'-' * len(title)}\n")
                # print('"""')
                # print("from magic1 import Aspect, Spell, SpellWriter")
                # print()
                #
                # print("spells = [")
                # for spell_line_tuple in (parse_spell(clean_spell_text[region])):
                #     spell = make_spell(*spell_line_tuple)
                #     # pprint(spell)
                #     print(f"    {spell!r},")
                # print("]")
                #
                # print("if __name__ == '__main__':")
                # print("    for spell in spells:")
                # print("        print(spell.report())")


if __name__ == "__main__":
    main()
