"""
OpenD6 Character and Creature Definition DSL.
Some handy workbook functions.

..  autofunction:: workbook_characters

..  autofunction:: workbook_groupBy

..  autofunction:: display

..  autofunction:: debug


"""

from collections import defaultdict
from collections.abc import Callable
from dataclasses import fields
import fnmatch
from pprint import pformat
from typing import Any

from .features import Character, CharacterBudget, Creature, CharacterDict


def workbook_characters(context: dict[str, Any]) -> dict[str, Character]:
    """
    Emit sequence of Characters in a Workbook.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from ``Character`` name to ``Character`` instances
    """
    return {
        value.name: value
        for name, value in context.items()
        if isinstance(value, Character)
    }


def workbook_groupBy(
    context: dict[str, Any], group_rule: Callable[[Character], str] = lambda c: ""
) -> dict[str, list[Character]]:
    r"""Transform a dict[name: str, Character] of spells into a dictionary: dict[some_attr: str, list[Character]].
    This is often used to partition by realm, but any other string attribute is possible.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from rank number to lists of ``Spell`` instances
    """
    grouped: defaultdict[str, list[Character]] = defaultdict(list)
    for name, char in workbook_characters(context).items():
        group = group_rule(char)
        grouped[group].append(char)
    return grouped


def display(
    character: Character, check: CharacterBudget | bool = CharacterBudget.NORMAL
) -> str:
    """
    Creates a display a character in plain text to help designers.
    """

    dict_value = {
        field.name: getattr(character, field.name)
        for field in fields(character)
        if not (field.name.startswith("_"))
    }
    if check != CharacterBudget.NO_BUDGET:
        assert isinstance(check, CharacterBudget), (
            "Change from True to CharacterBudget.NORMAL"
        )
        dict_value |= {"Check": character.budget_check(check)}
    return pformat(dict_value, sort_dicts=False)


def debug(
    characters: list[Character | Creature] | CharacterDict,
    ident: int | str | None | list[str] = None,
) -> None:
    """
    Prints details of a Character to STDOUT.
    Uses :py:func:`display`.

    >>> from opend6_tools.character import *
    >>> human = Character(
    ...     occupation="Default", race="Human"
    ... )
    >>> book = [human]
    >>> debug(book, 0) # doctest: +NORMALIZE_WHITESPACE
    ##
    {'name': '',
     'occupation': 'Default',
     'race': 'Human',
     'gender': '',
     'age': '',
     'height': '',
     'weight': '',
     'physical_description': '',
     'agility': Agility(3*D, {'acrobatics': 0*D, 'climbing': 0*D, 'contortion': 0*D, 'dodge': 0*D, 'fighting': 0*D, 'flying': 0*D, 'jumping': 0*D, 'melee combat': 0*D, 'combat': 0*D, 'riding': 0*D, 'stealth': 0*D}),
     'intellect': Intellect(3*D, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),
     'coordination': Coordination(3*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),
     'acumen': Acumen(3*D, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),
     'physique': Physique(3*D, {'lifting': 0*D, 'running': 0*D, 'stamina': 0*D, 'swimming': 0*D}),
     'charisma': Charisma(3*D, {'animal handling': 0*D, 'bluff': 0*D, 'charm': 0*D, 'command': 0*D, 'intimidation': 0*D, 'mettle': 0*D, 'persuasion': 0*D}),
     'extranormal': Magic(0*D, {'alteration': 0*D, 'apportation': 0*D, 'conjuration': 0*D, 'divination': 0*D}),
     'advantages': OptionList(),
     'disadvantages': OptionList(),
     'special_abilities': OptionList(),
     'description': '',
     'realm': 'Human realm',
     'move': 10,
     'strength_damage': 2*D,
     'body': 31,
     'wounds': {'Mortal': '1-2',
                'Incapacitated': '3-5',
                'Severe': '6-11',
                'Wounded': '12-18',
                'Stunned': '19-24'},
     'funds': 3*D,
     'silver': 180,
     'fate_points': 1,
     'character_points': 5,
     'equipment': NoteList(),
     'armor': NoteList(),
     'weapons': NoteList(),
     'spells': NoteList(),
     'personality': '',
     'objectives': '',
     'native_language': '',
     'other_notes': '',
     'Check': {'Attributes': '18D out of 18D',
               'Skills': 'Nothing out of 7D',
               'Options': 'Nothing'}}
    <BLANKLINE>

    :param spells: Spell Book
    :param ident: Identifier for a spell, a number, or a name, or a list of names.
        Shell-style wild-cards are used to match names.
    """
    match characters:
        case list():
            char_map = {c.name: c for c in characters}
        case dict():
            char_map = characters
        case _:  # pragma: no cover
            raise ValueError(f"invalid type for {characters=!r}")

    keys: list[str]
    match ident:
        case None:
            keys = list(char_map.keys())
        case str():
            try:
                keys = [list(char_map.keys())[int(ident)]]
            except (ValueError, TypeError):
                keys = [ident]
        case int() as index:
            keys = [list(char_map.keys())[index]]
        case list() as ident_list:
            keys = [
                n
                for key_pat in ident_list
                for n in char_map.keys()
                if fnmatch.fnmatch(n.lower(), key_pat.lower())
            ]
        case _:  # pragma: no cover
            raise ValueError("unknown identifier {ident!r}")

    for name in keys:
        character = char_map[name]
        print("##", character.name)
        print(display(character))
        print()
