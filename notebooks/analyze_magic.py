"""
Some tools to analyze spell definitions.

1. Find spells with "unknown" or missing skills
2. Write a doctest ``__test__`` case for spells.
3. Write a pytest ``test_spells()`` function for spells.
4. Extract table of effects vs. skill for a few selected books.
    This assures the ranks and difficulties align.
"""

from pathlib import Path
from pprint import pprint

from opend6_tools.magic import Spell, CompositeEffect, Effect

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

COLLECTION_FILES = ("opend6_project/opend6_spells.py",)

MIRACLE_FILES = (
    "fantasy_rulebook/spells/fantasy_miracle_DIVINATION.py",
    "fantasy_rulebook/spells/fantasy_miracle_FAVOR.py",
    "fantasy_rulebook/spells/fantasy_miracle_STRIFE.py",
)

def all_books(base: Path = Path.cwd()) -> dict[str, list[Spell]]:

    def load_spells(path: Path, global_defs: dict, local_vars: dict) -> None:
        print(path.relative_to(base))
        try:
            text = path.read_text()
            exec(text, global_defs, local_vars)
        except Exception as ex:
            depth, tb = 0, ex.__traceback__
            # Locate the string given to "exec()".
            while tb:
                if tb.tb_frame.f_code.co_filename == "<string>":
                    lines = text.splitlines()
                    begin = max(0, tb.tb_lineno-5)
                    end = min(len(lines), tb.tb_lineno+5)
                    selection = lines[begin:end]
                    for n, line in enumerate(selection, start=begin):
                        flag = '*' if n == tb.tb_lineno else ' '
                        print(f"{flag}{n:3}{flag} {line}")
                    break  # Found it.
                depth, tb = depth + 1, tb.tb_next
            print(ex)
            raise

    books: dict[str, list[Spell]] = {}

    book_paths = (base / n for n in BOOK_FILES)
    for path in book_paths:
        global_defs = {}
        local_vars = {}
        load_spells(path, global_defs, local_vars)
        books[path.stem] = local_vars["spells"]

    # OpenD6 Project unique spells; organized into a dict[str, list[Spell]].
    collection_paths = (base / n for n in COLLECTION_FILES)
    for coll_path in collection_paths:
        global_defs = {}
        local_vars = {}
        load_spells(coll_path, global_defs, local_vars)
        for name in local_vars["books"]:
            books[f"Project {name}"] = local_vars["books"][name]

    miracle_paths = (base / n for n in MIRACLE_FILES)
    for miracle_path in miracle_paths:
        global_defs = {}
        local_vars = {}
        load_spells(miracle_path, global_defs, local_vars)
        try:
            books[miracle_path.stem] = local_vars["invocations"]
        except KeyError:
            pprint(local_vars)
            raise

    return books
