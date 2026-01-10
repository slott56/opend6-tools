"""
Analyze magic spell definitions.

1. Find spells with "unknown" or missing skills
2. Write a doctest ``__test__`` case for spells.
3. Write a pytest ``test_spells()`` function for spells.
4. Extract table of effects vs. skill for
"""

from collections import defaultdict
from pathlib import Path
import textwrap
from pprint import pprint

from .magic2 import Spell, CompositeEffect, Effect


def all_books(base: Path = Path.cwd()) -> dict[str, list[Spell]]:
    books: dict[str, list[Spell]] = {}

    BOOK_FILES = (
        # System rules
        "system_book/spells/system_spells.py",
        # D6 Fantasy Rulebook
        "fantasy_rulebook/spells/fantasy_CANTRIPS.py",
        "fantasy_rulebook/spells/fantasy_ALTERATION.py",
        "fantasy_rulebook/spells/fantasy_APPORTATION.py",
        "fantasy_rulebook/spells/fantasy_CONJURATION.py",
        "fantasy_rulebook/spells/fantasy_DIVINATION.py",
        # Magic Rulebook
        "magic_guide/spells/Chronomancy.py",
        "magic_guide/spells/Elemental.py",
        "magic_guide/spells/Necromancy.py",
        "magic_guide/spells/Peregrination.py",
        "magic_guide/spells/Photomancy.py",
        "magic_guide/spells/Somniomancy.py",
        "magic_guide/spells/Technomancy.py",
        "magic_guide/spells/Vitomancy.py",
        "magic_guide/spells/Wizardry.py",
        "magic_guide/spells/sample_spells.py",
        # My unique spells
        # "world_book/spells/more_spells.py",
        "world_book/spells/fw_cantrips.py",
        "world_book/spells/fw_rank2.py",
        "world_book/spells/fw_rank3.py",
        "world_book/spells/fw_rank4.py",
    )
    book_paths = (base / n for n in BOOK_FILES)
    for path in book_paths:
        global_defs = {}
        local_vars = {}
        exec(path.read_text(), global_defs, local_vars)
        books[path.stem] = local_vars["spells"]

    # OpenD6 Project unique spells; organized into a dict[str, list[Spell]].
    COLLECTION_FILES = ("opend6_project/opend6_spells.py",)
    collection_paths = (base / n for n in COLLECTION_FILES)
    for coll_path in collection_paths:
        global_defs = {}
        local_vars = {}
        exec(coll_path.read_text(), global_defs, local_vars)
        for name in local_vars["books"]:
            books[f"Project {name}"] = local_vars["books"][name]

    MIRACLE_FILES = (
        "fantasy_rulebook/spells/fantasy_miracle_DIVINATION.py",
        "fantasy_rulebook/spells/fantasy_miracle_FAVOR.py",
        "fantasy_rulebook/spells/fantasy_miracle_STRIFE.py",
    )
    miracle_paths = (base / n for n in MIRACLE_FILES)
    for miracle_path in miracle_paths:
        global_defs = {}
        local_vars = {}
        exec(miracle_path.read_text(), global_defs, local_vars)
        try:
            books[miracle_path.stem] = local_vars["invocations"]
        except KeyError:
            pprint(local_vars)
            raise

    return books


def unknown_skill(books: dict[str, list[Spell]]) -> None:
    """
    Is the skill "unknown" or missing?

    :param books:
    :return:
    """
    for name in books:
        for spell in books[name]:
            if spell.skill == "unknown":
                print(name, spell.name, spell.skill)


def make_spell_doctest(spell_book: list[Spell], book_attr_name: str = "spells") -> None:
    """
    Write the doctest block for spells.

    :param books:
    :return:
    """
    print("__test__ = {")
    for slot, spell in enumerate(spell_book):
        try:
            expected = int(spell.other_aspects["Difficulty"].format)  # type: ignore
        except KeyError:
            # Ugh. Difficulty not included.
            expected = 0
        except ValueError:
            value, *words = spell.other_aspects["Difficulty"].format.split()  # type: ignore
            low, high = value.split("/")
            expected = int(low)
        print(f'    "{spell.name}": ">>> {book_attr_name}[{slot}].difficulty\\n{expected}",')
    print("}")


def make_spell_pytest(spell_book: list[Spell], book_attr_name: str = "spells") -> None:
    """
    Write the pytest block for spells.

    :param books:
    :return:
    """
    print("SPELL_DIFFICULTIES = [")
    for spell in spell_book:
        try:
            expected = int(spell.other_aspects["Difficulty"].format)  # type: ignore
        except KeyError:
            # Ugh. Difficulty not included.
            expected = 0
        except ValueError:
            value, *words = spell.other_aspects["Difficulty"].format.split()  # type: ignore
            low, high = value.split("/")
            expected = int(low)
        print(f'    ("{spell.name}", {expected}),')
    print("]")
    print(
        textwrap.dedent(f"""\
        SPELL_MAP = {{s.name: s for s in {book_attr_name}}}
        @pytest.mark.parametrize("spell_name,difficulty", SPELL_DIFFICULTIES)
        def test_spells(spell_name, difficulty):
            assert SPELL_MAP[spell_name].difficulty == difficulty
    """)
    )


def effect_skill(book_names: list[str] | None = None) -> None:
    skills: defaultdict[str, list[Spell | Effect]] = defaultdict(list)
    books = all_books()
    for book in book_names or books:
        for spell in books[book]:
            spell.finalize()
            match spell.effect:
                case CompositeEffect() as composite:
                    skills[spell.skill].extend(composite.effects)
                case _:
                    skills[spell.skill].append(spell.effect)
    for s in skills:
        print("##", s)
        print()
        for e in sorted(skills[s], key=lambda e: e.__class__.__name__):
            print("- ", e)
        print()


def main():
    fw_books = [
        "fw_cantrips",
        "fw_rank2",
        "fw_rank3",
        "fw_rank4",
    ]
    effect_skill(fw_books)


if __name__ == "__main__":
    main()
