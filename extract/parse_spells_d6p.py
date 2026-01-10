"""
Scrape OpenD6Project's "Spells | The OpenD6 Project.html"

The source file is from https://opend6project.wordpress.com/chapter-1-character-basics/spells/

WARNING: Can overwrite files.
"""

from collections import defaultdict
from contextlib import redirect_stdout
import csv
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from pprint import pprint
import re
import sys
from typing import Iterable, Iterator, Self, ClassVar, TextIO

from humre import *
from bs4 import BeautifulSoup

import magic1 as magic


class LabelValueType(Enum):
    LABEL_VALUE = auto()
    SEPARATOR = auto()
    DESCRIPTION = auto()


def label_value(line: str) -> tuple[LabelValueType, str, str]:
    """Distinguish different kinds of lines in the text.

    -  "Label : Value"
    -  "Text (difficulty)"
    -  "Text"
    -  "Label:" section header

    >>> label_value("Duration: 1.5 seconds (+1)")
    (<LabelValueType.LABEL_VALUE: 1>, 'Duration', '1.5 seconds (+1)')
    >>> label_value("Area Effect (10)")
    (<LabelValueType.LABEL_VALUE: 1>, 'Area Effect (10)', '')
    >>> label_value("Upon the dispersal...")
    (<LabelValueType.DESCRIPTION: 3>, '', 'Upon the dispersal...')
    >>> label_value("Other Aspects:")
    (<LabelValueType.SEPARATOR: 2>, 'Other Aspects', '')
    """
    aspect_text_re = starts_and_ends_with(
        either(
            group(zero_or_more(nonchars(":"))) + ":" + group(EVERYTHING),
            group(EVERYTHING),
        )
    )
    aspect_pat = re.compile(aspect_text_re)  # r"^([^:]*):(.*)|(.*)$")
    other_text_re = starts_and_ends_with(
        one_or_more(nonchars(OPEN_PAREN)) + OPEN_PAREN + EVERYTHING + CLOSE_PAREN
    )
    other_aspect_pat = re.compile(other_text_re)  # r"^[^(]+\(.*\)$")

    if match := aspect_pat.match(line):
        label, value, text = match.groups()
        if label and value:
            return LabelValueType.LABEL_VALUE, label.strip(), value.strip()
        elif text:
            # if "words (+\d)", actually a label with no value.
            if other_aspect_pat.match(line):
                return LabelValueType.LABEL_VALUE, text.strip(), ""
            # Otherwise, description
            return LabelValueType.DESCRIPTION, "", text.strip()
        elif label:
            return LabelValueType.SEPARATOR, label.strip(), ""
        else:
            raise ValueError(f"bad {line}")
    else:
        raise ValueError(f"bad {line}")


def parse_aspect(aspect_text: str | None) -> magic.Aspect:
    """
    Create Aspect() from core aspect text, which has two forms:
    -   ±one_or_more(DIGIT) + ( + Words + )
    -   one_or_more(DIGIT) (Generally only used for Difficulty)

    The alternative form for the label of "other aspects" is Words + ( + ± one_or_more(DIGIT) + ).

    >>> parse_aspect("6 (+1D bonus to one non-Extranormal attribute)")
    Aspect(format='+1D bonus to one non-Extranormal attribute', base_difficulty=6, count=1)
    >>> parse_aspect("6")
    Aspect(format='2D', base_difficulty=6, count=1)
    >>> parse_aspect("Touch (0)")
    Aspect(format='Touch', base_difficulty=0, count=1)
    """
    if not aspect_text:
        return None

    core_aspect_re = either(
        group(optional(chars("+-")) + one_or_more(DIGIT))
        + one_or_more(WHITESPACE)
        + OPEN_PAREN
        + group(EVERYTHING)
        + CLOSE_PAREN,
        group(one_or_more(DIGIT)),
    )
    core_aspect_pat = re.compile(core_aspect_re)  # r"(\d+)\s+\((.*)\)|(\d+)")
    other_aspect_re = (
        group(one_or_more(nonchars(OPEN_PAREN)))
        + OPEN_PAREN
        + group(optional(chars("+-")) + one_or_more(DIGIT))
        + CLOSE_PAREN
    )
    other_aspect_pat = re.compile(other_aspect_re)
    # Word "difficulty" precedes the actual value...
    difficulty_re = (
        EVERYTHING
        + OPEN_PAREN
        + EVERYTHING
        + chars("dD")
        + "ifficulty"
        + one_or_more(nonchars(DIGIT))
        + group(optional(chars("+-")) + one_or_more(chars(DIGIT)))
    )

    if match := core_aspect_pat.match(aspect_text):
        value, effect, only_value = match.groups()
        if value and effect:
            effect_value = int(value)
            return magic.Aspect(format=effect, base_difficulty=effect_value)
        else:
            effect_value = int(only_value)
            dice = effect_value // 3
            pips = effect_value % 3
            effect = f"{dice}D" if pips == 0 else f"{dice}D+{pips}"
            return magic.Aspect(format=effect, base_difficulty=effect_value)
    elif match := other_aspect_pat.match(aspect_text):
        effect, value = match.groups()
        effect_value = int(value)
        return magic.Aspect(format=effect.strip(), base_difficulty=effect_value)
    elif match := re.search(difficulty_re, aspect_text):
        effect_value = int(match.group(1))
        return magic.Aspect(format=aspect_text, base_difficulty=effect_value)
    else:
        # Pure text. Okay. Maybe this is part of the notes.
        return magic.Aspect(format=aspect_text, base_difficulty=0)


def parse_other_aspect(label: str, value: str) -> tuple[str, magic.Aspect]:
    base_aspect = parse_aspect(label)
    return base_aspect.format, magic.Aspect(
        format=value,
        base_difficulty=base_aspect.base_difficulty,
        count=base_aspect.count,
    )


def text_spell_parser(name: str, body: list[str]) -> magic.Spell:
    """
    Parse lines looking for Aspects, "Other Aspects:", and "Other Conditions:"
    """
    label_value_iter = (label_value(line) for line in body)
    core: list[tuple[str, str]] = []
    other: list[tuple[str, str]] = []
    descr: list[str] = []

    for lv_type, label, value in label_value_iter:
        if lv_type is LabelValueType.SEPARATOR:
            # Skip this, change state
            assert value == ""
            assert label == "Other Aspects"
            break
        elif lv_type is LabelValueType.DESCRIPTION:
            # Save this, change state
            descr.append(value)
            break
        else:
            core.append((label, value))
    for lv_type, label, value in label_value_iter:
        if lv_type is LabelValueType.DESCRIPTION:
            descr.append(value)
        elif lv_type is LabelValueType.LABEL_VALUE:
            other.append((label, value))
        else:
            # Another separator?
            raise ValueError(f"{lv_type} {label}: {value} unexpected")

    core_aspects = dict(core)

    try:
        effect = parse_aspect(core_aspects.pop("Effect"))
        duration = parse_aspect(core_aspects.pop("Duration"))
        range_ = parse_aspect(core_aspects.pop("Range"))
        casting_time = parse_aspect(
            core_aspects.pop("Casting Time", None) or core_aspects.pop("Cast Time")
        )
        difficulty = parse_aspect(core_aspects.pop("Difficulty"))
        speed = parse_aspect(core_aspects.pop("Speed", None))
        skill = core_aspects.pop("Skill Used")
    except KeyError as ex:
        print(ex)
        print(core_aspects)
        print(body)
        raise

    if core_aspects:
        raise ValueError(f"Unexpected aspects {core_aspects}")

    other_aspects = dict(parse_other_aspect(name, value) for name, value in other)

    return magic.Spell(
        name=name,
        effect=effect,
        duration=duration,
        range=range_,
        speed=speed,
        casting_time=casting_time,
        other_aspects=other_aspects,
        skill=skill,
        notes=descr,
    )


def html_spell_parser(html_path: Path) -> Iterator[tuple[str, magic.Spell]]:
    """
    Extract the spell description text from HTML framework.

    This presumes section titles are present as <h3> tags.
    Spells are <h4> tags.
    """
    html_doc = html_path.read_text()
    soup = BeautifulSoup(html_doc, "html.parser")
    article = soup.article
    header = article.header
    print(header.text)
    content = article.div

    section_name = ""
    spell_name = ""
    spell_body: list[str] = []
    for tag in content.children:
        if tag.name == "h3":
            if spell_body:
                yield section_name, text_spell_parser(spell_name, spell_body)
                spell_body = []
            section_name = tag.text
        elif tag.name == "h4":
            if spell_body:
                yield section_name, text_spell_parser(spell_name, spell_body)
                spell_body = []
            spell_name = tag.text
        elif tag.name == "p" and section_name and spell_name:
            spell_body.append(tag.text)
        elif tag.name == "p":
            print("**", tag.text)
        elif tag.text.strip():
            print("**", tag.text)
    if section_name and spell_name and spell_body:
        yield section_name, text_spell_parser(spell_name, spell_body)


def spell_book(source_path: Path) -> dict[str, list[magic.Spell]]:
    spell_list = list(html_spell_parser(source_path))
    by_section: dict[str, list[magic.Spell]] = defaultdict(list)
    for section, spell in spell_list:
        by_section[section].append(spell)
    # Force Cantrips to the front. The rest are alphabetical.
    names = ["Cantrips"] + sorted(set(by_section.keys()) - {"Cantrips"})
    book = {
        section: sorted(by_section[section], key=lambda s: s.name) for section in names
    }
    return book


def main():
    source_dir = Path.cwd().parent / "source"
    html_path = source_dir / "Spells | The OpenD6 Project.html"
    book = spell_book(html_path)

    # Create a "tools/opend6_spells.py" module.
    book_path = Path.cwd().parent / "tools" / "opend6_spells.py"
    if book_path.exists():
        print(f"Will not overwrite {book_path.relative_to(Path.cwd().parent)}")
        sys.exit(f"{book_path} exists")

    print(f"Creating {book_path.relative_to(Path.cwd().parent)}")
    with open(book_path, "w") as book_file:
        with redirect_stdout(book_file):
            print(magic.module("OpenD6 Project Spells", book))
            # pprint(book, width=256)


if __name__ == "__main__":
    main()
