"""
OpenD6 Character and Creature Definition DSL.

Example
-------

>>> from random import seed
>>> seed(42)

>>> from opend6_tools.character import *
>>> human = Character(
...     occupation="Default", race="Human"
... )
>>> human.physique.dice
DieCode(3, 0)
>>> human.extranormal.dice
DieCode(0, 0)
>>> human.budget_check(CharacterBudget.NORMAL)
{'Attributes': '18D out of 18D', 'Skills': 'Nothing out of 7D', 'Options': 'Nothing'}
>>> human.budget
{'Attributes': DieCode(18, 0), 'Skills': DieCode(0, 0), 'Options': DieCode(0, 0)}

>>> w = CharacterWriter_Literal()
>>> print(w.report(human))
<BLANKLINE>
..  rubric:: OpenD6 Fantasy
<BLANKLINE>
<BLANKLINE>
+--------------------------------------------------+
| Character Name: ________________________________ |
+--------------------------------------------------+
| Occupation: Default                              |
+-------------------------+------------------------+
| Race: Human             | Gender: ______________ |
+----------------+--------+-------+----------------+
| Age: ________  | Height: ______ | Weight: ______ |
+----------------+----------------+----------------+
| Physical Description ___________________________ |
+--------------------------------------------------+
<BLANKLINE>
<BLANKLINE>
::
<BLANKLINE>
    +----------------------+----------------------+----------------------+
    | Agility           3D | Intellect         3D |                      |
    +----------------------+----------------------+----------------------+
    | acrobatics           | cultures             |**Advantages**:       |
    | climbing             | devices              |**Disadvantages**:    |
    | combat               | healing              |**Special Abilities**:|
    | contortion           | navigation           |**Equipment**:        |
    | dodge                | reading/writing      |**Description**:      |
    | fighting             | scholar              |                      |
    | flying               | speaking             |                      |
    | jumping              | trading              |                      |
    | melee combat         | traps                |                      |
    | riding               | ____________________ |                      |
    | stealth              | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    +----------------------+----------------------+                      |
    | Coordination      3D | Acumen            3D |                      |
    +----------------------+----------------------+                      |
    | charioteering        | artist               |                      |
    | lockpicking          | crafting             |                      |
    | marksmanship         | disguise             |                      |
    | pilotry              | gambling             |                      |
    | sleight of hand      | hide                 |                      |
    | throwing             | investigation        |                      |
    | ____________________ | know-how             |                      |
    | ____________________ | search               |                      |
    | ____________________ | streetwise           |                      |
    | ____________________ | survival             |                      |
    | ____________________ | tracking             |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    +----------------------+----------------------+                      |
    | Physique          3D | Charisma          3D |                      |
    +----------------------+----------------------+                      |
    | lifting              | animal handling      |                      |
    | running              | bluff                |                      |
    | stamina              | charm                |                      |
    | swimming             | command              |                      |
    | ____________________ | intimidation         |                      |
    | ____________________ | mettle               |                      |
    | ____________________ | persuasion           |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    | ____________________ | ____________________ |                      |
    +----------------------+----------------------+----------------------+
    | Magic       ________ |                      |                      |
    +----------------------+----------------------+----------------------+
    | alteration           | Str Damage        2D | Body Points 37       |
    | apportation          | Move              10 | [ ] Stunned   22-29  |
    | conjuration          | Fate Pts      1      | [ ] Wounded   15-21  |
    | divination           | Character Pts 5      | [ ] Severe    7-14   |
    | ____________________ | Funds 3D             | [ ] Incapac'd 4-6    |
    | ____________________ | Silver 180           | [ ] Mortal    1-3    |
    |                      |                      | [ ] Dead             |
    +----------------------+----------------------+----------------------+
<BLANKLINE>

Top-Level Components
---------------------

These are functions and classes that are helpful in a Jupyter Notebook.

..  autofunction::  display

..  autofunction::  workbook_characters

..  autofunction::  workbook_groupBy

Reporting and Display
---------------------

These are the conventional top-level application components.
The :py:func:`display` function produces the useful RST output.


..  autoclass:: CharacterWriter
    :members:

..  autoclass:: CharacterWriter_Literal
    :members:

..  autoclass:: CharacterWriter_Short
    :members:

..  autoclass:: CharacterWriter_Table
    :members:

..  autofunction::  parse_param_name

..  autofunction::  sheet

..  autoclass:: CharacterBudget
    :members:

..  autoclass:: Format
    :members:

..  autofunction::  detail

..  autofunction::  summary


Characters
----------

..  autoclass:: Character
    :members:
    :undoc-members:
    :member-order:  bysource

..  autoclass:: Creature
    :members:
    :undoc-members:
    :member-order:  bysource


..  autoclass:: OptionList
    :members:

..  autoclass:: CharacterOption
    :members:

Attributes
----------------------

..  autoclass:: Attribute
    :members:

..  autoclass:: Acumen
    :show-inheritance:
    :members:

..  autoclass:: Charisma
    :show-inheritance:
    :members:

..  autoclass:: Intellect
    :show-inheritance:
    :members:

..  autoclass:: Agility
    :show-inheritance:
    :members:

..  autoclass:: Coordination
    :show-inheritance:
    :members:

..  autoclass:: Physique
    :show-inheritance:
    :members:

..  autoclass:: Magic
    :show-inheritance:
    :members:

..  autoclass:: Miracles
    :show-inheritance:
    :members:


Options: Disadvantage
--------------------------------------------------

..  autoclass:: Disadvantage
    :show-inheritance:
    :members:

..  autoclass:: AchillesHeel
    :show-inheritance:

..  autoclass:: AdvantageFlaw
    :show-inheritance:

..  autoclass:: MinorStigma
    :show-inheritance:

..  autoclass:: Age
    :show-inheritance:

..  autoclass:: BadLuck
    :show-inheritance:

..  autoclass:: BurnOut
    :show-inheritance:

..  autoclass:: CulturalUnfamiliarity
    :show-inheritance:

..  autoclass:: Debt
    :show-inheritance:

..  autoclass:: Devotion
    :show-inheritance:

..  autoclass:: Employed
    :show-inheritance:

..  autoclass:: Enemy
    :show-inheritance:

..  autoclass:: Hindrance
    :show-inheritance:

..  autoclass:: Infamy
    :show-inheritance:

..  autoclass:: LanguageProblems
    :show-inheritance:

..  autoclass:: LearningProblems
    :show-inheritance:

..  autoclass:: Poverty
    :show-inheritance:

..  autoclass:: Prejudice
    :show-inheritance:

..  autoclass:: Price
    :show-inheritance:

..  autoclass:: Quirk
    :show-inheritance:

..  autoclass:: ReducedAttribute
    :show-inheritance:

Options: Advantage
--------------------------------------------------

..  autoclass:: Advantage
    :show-inheritance:
    :members:

..  autoclass:: Authority
    :show-inheritance:

..  autoclass:: Contacts
    :show-inheritance:

..  autoclass:: Cultures
    :show-inheritance:

..  autoclass:: Equipment
    :show-inheritance:

..  autoclass:: Fame
    :show-inheritance:

..  autoclass:: Patron
    :show-inheritance:

..  autoclass:: Size
    :show-inheritance:

..  autoclass:: TrademarkSpecialization
    :show-inheritance:

..  autoclass:: Wealth
    :show-inheritance:

Options: Special Ability
--------------------------------------------------

..  autoclass:: SpecialAbility
    :show-inheritance:
    :members:

..  autoclass:: AcceleratedHealing
    :show-inheritance:

..  autoclass:: Ambidextrous
    :show-inheritance:

..  autoclass:: AnimalControl
    :show-inheritance:

..  autoclass:: ArmorDefeatingAttack
    :show-inheritance:

..  autoclass:: AtmosphericTolerance
    :show-inheritance:

..  autoclass:: AttackResistance
    :show-inheritance:

..  autoclass:: AttributeScramble
    :show-inheritance:

..  autoclass:: Blur
    :show-inheritance:

..  autoclass:: CombatSense
    :show-inheritance:

..  autoclass:: Confusion
    :show-inheritance:

..  autoclass:: Darkness
    :show-inheritance:

..  autoclass:: Elasticity
    :show-inheritance:

..  autoclass:: Endurance
    :show-inheritance:

..  autoclass:: EnhancedSense
    :show-inheritance:

..  autoclass:: EnvironmentalResistance
    :show-inheritance:

..  autoclass:: ExtraBodyPart
    :show-inheritance:

..  autoclass:: ExtraSense
    :show-inheritance:

..  autoclass:: FastReactions
    :show-inheritance:

..  autoclass:: Fear
    :show-inheritance:

..  autoclass:: Flight
    :show-inheritance:

..  autoclass:: GliderWings
    :show-inheritance:

..  autoclass:: Hardiness
    :show-inheritance:

..  autoclass:: Hypermovement
    :show-inheritance:

..  autoclass:: Immortality
    :show-inheritance:

..  autoclass:: Immunity
    :show-inheritance:

..  autoclass:: IncreasedAttribute
    :show-inheritance:

..  autoclass:: InfravisionUltravision
    :show-inheritance:

..  autoclass:: Intangibility
    :show-inheritance:

..  autoclass:: Invisibility
    :show-inheritance:

..  autoclass:: IronWill
    :show-inheritance:

..  autoclass:: LifeDrain
    :show-inheritance:

..  autoclass:: Longevity
    :show-inheritance:

..  autoclass:: LuckGood
    :show-inheritance:

..  autoclass:: LuckGreat
    :show-inheritance:

..  autoclass:: MasterOfDisguise
    :show-inheritance:

..  autoclass:: MultipleAbilities
    :show-inheritance:

..  autoclass:: NaturalArmor
    :show-inheritance:

..  autoclass:: NaturalHandWeapon
    :show-inheritance:

..  autoclass:: NaturalMagick
    :show-inheritance:

..  autoclass:: NaturalRangedWeapon
    :show-inheritance:

..  autoclass:: Omnivorous
    :show-inheritance:

..  autoclass:: ParalyzingTouch
    :show-inheritance:

..  autoclass:: PossessionLimited
    :show-inheritance:

..  autoclass:: PossessionFull
    :show-inheritance:

..  autoclass:: QuickStudy
    :show-inheritance:

..  autoclass:: SenseOfDirection
    :show-inheritance:

..  autoclass:: Shapeshifting
    :show-inheritance:

..  autoclass:: Silence
    :show-inheritance:

..  autoclass:: SkillBonus
    :show-inheritance:

..  autoclass:: SkillMinimum
    :show-inheritance:

..  autoclass:: Teleportation
    :show-inheritance:

..  autoclass:: Transmutation
    :show-inheritance:

..  autoclass:: UncannyAptitude
    :show-inheritance:

..  autoclass:: Ventriloquism
    :show-inheritance:

..  autoclass:: WaterBreathing
    :show-inheritance:

..  autoclass:: YouthfulAppearance
    :show-inheritance:

..  autoclass:: NaturalAbility
    :members:


Foundations
-----------

..  autoclass:: Roll
    :members:
    :undoc-members:

..  autoclass:: CriticalSuccess
    :show-inheritance:
    :members:

..  autoclass:: CriticalFailure
    :show-inheritance:
    :members:

..  autoclass:: DieCode
    :members:
    :undoc-members:


"""

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field, fields
import difflib
from enum import Enum
import fnmatch
from functools import singledispatchmethod, partial
from pprint import pformat
from random import randint
import sys
import textwrap
from textwrap import dedent
from types import SimpleNamespace
from typing import Annotated, Any, ClassVar, Literal, TextIO, cast

import jinja2
from jinja2 import Environment
import typer
from humre import *  # noqa: F403  # type: ignore[import-untyped]

__all__ = [
    "Character",
    "Creature",
    "D",
    "DieCode",
    "Attribute",
    "Agility",
    "Intellect",
    "Coordination",
    "Acumen",
    "Physique",
    "Charisma",
    "Miracles",
    "Magic",
    "Advantage",
    "Disadvantage",
    "SpecialAbility",
    "NaturalAbility",
    "OptionList",  # Use instead of [] or list()
    "AchillesHeel",
    "AdvantageFlaw",
    "MinorStigma",
    "Age",
    "BadLuck",
    "BurnOut",
    "CulturalUnfamiliarity",
    "Debt",
    "Devotion",
    "Employed",
    "Enemy",
    "Hindrance",
    "Infamy",
    "LanguageProblems",
    "LearningProblems",
    "Poverty",
    "Prejudice",
    "Price",
    "Quirk",
    "ReducedAttribute",
    "Authority",
    "Contacts",
    "Cultures",
    "Equipment",
    "Fame",
    "Patron",
    "Size",
    "TrademarkSpecialization",
    "Wealth",
    "AcceleratedHealing",
    "Ambidextrous",
    "AnimalControl",
    "ArmorDefeatingAttack",
    "AtmosphericTolerance",
    "AttackResistance",
    "AttributeScramble",
    "Blur",
    "CombatSense",
    "Confusion",
    "Darkness",
    "Elasticity",
    "Endurance",
    "EnhancedSense",
    "EnvironmentalResistance",
    "ExtraBodyPart",
    "ExtraSense",
    "FastReactions",
    "Fear",
    "Flight",
    "GliderWings",
    "Hardiness",
    "Hypermovement",
    "Immortality",
    "Immunity",
    "IncreasedAttribute",
    "InfravisionUltravision",
    "Intangibility",
    "Invisibility",
    "IronWill",
    "LifeDrain",
    "Longevity",
    "LuckGood",
    "LuckGreat",
    "MasterOfDisguise",
    "MultipleAbilities",
    "NaturalArmor",
    "NaturalHandWeapon",
    "NaturalMagick",
    "NaturalRangedWeapon",
    "Omnivorous",
    "ParalyzingTouch",
    "PossessionLimited",
    "PossessionFull",
    "QuickStudy",
    "SenseOfDirection",
    "Shapeshifting",
    "Silence",
    "SkillBonus",
    "SkillMinimum",
    "Teleportation",
    "Transmutation",
    "UncannyAptitude",
    "Ventriloquism",
    "WaterBreathing",
    "YouthfulAppearance",
    # Main App
    "CharacterBudget",
    "summary",
    "Format",
    "detail",
    "display",
    "sheet",
    "dedent",
    "CharacterWriter",
    "CharacterWriter_Short",
    "CharacterWriter_Literal",
    "CharacterWriter_Table",
    "parse_param_name",
    "build_app",
    "typer",
    # Some handy names
    "sys",
    "Annotated",
    "partial",
]

## Part I -- Foundational Definitions


@dataclass
class Roll:
    """A single roll of the dice."""

    die: list[int]  #: The die values
    pips: int  #: Additional pips to add
    reroll_count: int = 0  #: Only for CriticalSuccess rolls.
    success: bool = False  #: Was this a CriticalSuccess?
    fail: bool = False  #: Was this a CriticalFailure?

    @property
    def total(self) -> int:
        """Total of Die plus bonus pips"""
        return sum(self.die) + self.pips

    def __str__(self) -> str:
        return f"{self.total}"


class CriticalSuccess(Roll):
    """A single roll that was a Critical Success -- Wild Die was 6."""

    success = True

    def __str__(self) -> str:
        return f"{self.total}{'!' * self.reroll_count}"


class CriticalFailure(Roll):
    """A single roll that was a Critical Failure -- Wild Die was 1."""

    fail = True

    @property
    def low_total(self) -> int:
        return sum(self.die) - max(self.die) + self.pips

    def __str__(self) -> str:
        return f"{self.low_total}? ({self.total})"


@dataclass
class DieCode:
    """
    The definition of a set of Die.
    This includes the number of dice and bonus pips to add.

    >>> from opend6_tools.character import DieCode
    >>> D = DieCode(1)
    >>> str(3 * D)
    '3D'
    >>> str(5 * D + 1)
    '5D+1'
    >>> (6*D+2).value
    20
    >>> str(D.from_pips(20))
    '6D+2'
    >>> str(DieCode("3D + 2"))
    '3D+2'
    >>> str((5*D+1)*2)
    '10D+2'

    >>> from random import seed
    >>> seed(42)
    >>> physique = 4*D
    >>> [str(physique.roll()) for _ in range(12)]
    ['17!', '12', '12? (18)', '6? (11)', '4? (6)', '16', '20', '15', '11', '18!', '7', '11']
    """

    d: int = 1  #: Number of dice
    pips: int = 0  #: Bonus pips to add

    def __init__(self, d: int | str, pips: int = 0) -> None:
        """
        Create a Die code
        :param d:  Number of Dice to roll
        :param pips: Bonus pips to add
        """
        match d:
            case int():
                self.d = d
                self.p = pips
            # Refactor into classmethod
            # Reify with magic2.DieCode
            case str() as text:
                pattern = (
                    zero_or_more(WHITESPACE)
                    + group(one_or_more(DIGIT))
                    + zero_or_more(WHITESPACE)
                    + "D"
                    + zero_or_more(WHITESPACE)
                    + optional_noncap_group(
                        PLUS + zero_or_more(WHITESPACE) + group(one_or_more(DIGIT))
                    )
                )
                if match := re.match(pattern, text):
                    d = int(match.group(1))
                    if match.group(2):
                        pips = int(match.group(2))
                    else:
                        pips = 0
                    self.d = d
                    self.p = pips
            case _:
                raise ValueError(f"invalid {d!r}")

    def __str__(self) -> str:
        if self.d and self.p:
            return f"{self.d}D+{self.p}"
        elif self.d:
            return f"{self.d}D"
        elif self.p:
            return f"{self.p}"
        else:
            return ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.d}, {self.p})"

    @property
    def value(self) -> int:
        """Value in pips."""
        return self.d * 3 + self.p

    def __bool__(self) -> bool:
        return bool(self.d or self.p)

    @classmethod
    def from_pips(cls, pips: int) -> "DieCode":
        """
        Converts number of pips to Die + Pips.

        :param pips: pips value
        :return: DideCode
        """
        return cls(*divmod(pips, 3))

    def roll(self) -> Roll:
        """The "Wild Die" roll algorithm.

        This returns several things:

        1. Ordinary result: a :py:class:`Roll` instance.

        2. Critical Success -- at least one wild die had a 6.
            A :py:class:`CriticalSuccess` instance.

        3. Critical Failure -- the first wild die was a 1. Two totals (with and without the highest die value.)
            A :py:class:`CriticalFailure` instance.
        """
        # Die 0 as the "wild die".
        roll = [randint(1, 6) for d in range(self.d)]
        if roll[0] == 1:
            # Critical Failure -- two totals: with and without highest die value.
            return CriticalFailure(roll, self.p)
        elif roll[0] == 6:
            # Critical Success -- Reroll wild die.
            reroll_count = 0
            while roll[0] == 6:
                reroll_count += 1
                roll.insert(0, randint(1, 6))
            return CriticalSuccess(roll, self.p, reroll_count)
        else:
            # Ordinary roll.
            return Roll(roll, self.p)

    def __mul__(self, other: Any) -> "DieCode":
        match other:
            case int() as n:
                return DieCode.from_pips(self.value * n)
            case _:
                return NotImplemented

    __rmul__ = __mul__

    def __add__(self, other: Any) -> "DieCode":
        match other:
            case int() as p:
                return DieCode.from_pips(self.value + p)
            case DieCode() as d:
                return DieCode.from_pips(self.value + d.value)
            case _:
                return NotImplemented

    def __sub__(self, other: Any) -> "DieCode":
        match other:
            case int() as p:
                return DieCode.from_pips(self.value - p)
            case DieCode() as d:
                return DieCode.from_pips(self.value - d.value)
            case _:
                return NotImplemented

    def __eq__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value == other.value
            case int():
                return self.value == other
            case _:
                return NotImplemented

    def __ne__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value != other.value
            case int():
                return self.value != other
            case _:
                return NotImplemented

    def __gt__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value > other.value
            case int():
                return self.value > other
            case _:
                return NotImplemented

    def __lt__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value < other.value
            case int():
                return self.value < other
            case _:
                return NotImplemented

    def __ge__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value >= other.value
            case int():
                return self.value >= other
            case _:
                return NotImplemented

    def __le__(self, other: Any) -> bool:
        match other:
            case DieCode():
                return self.value <= other.value
            case int():
                return self.value <= other
            case _:
                return NotImplemented


D = DieCode(1)

## Part II -- Units (not used)

## Part III -- Attributes and Skills


class Attribute:
    """Map any explicitly-named skills to the DieCode for that skill.

    So far, the upper limit is about 12 distinct skills for an Attribute.

    A skill name is either a simple word or a more complicated word:specialization.

    Reserved names:

    - ``'name'``
    - ``'dice'`` (for the attribute measure)
    - ``'keys'``, ``'values'``, ``'items'`` from the ``dict`` class.

    ..  notes:

        Generally, we want to use ``character.attribute.skill``,
        but we also need to use ``character.attribute.get('skill:specialty')`` and
        ``character.attributes['skill:specialty']``.

    For character sheets, all skills are shown, even if there's no overriding dice allocation.
    (In a narrow, technical sense, the dice value for a missing skill comes from the overall attribute.)
    For character detail (in .RST), only the overriding skill values need to be shown.

    Example

    >>> from opend6_tools.character import *

    >>> class Extranormal(Attribute):
    ...     SKILL_NAMES = ("alteration", "apportation", "conjuration", "divination",)
    >>> ex = Extranormal(DieCode(3, 2), {"divination": DieCode(4)})
    >>> ex.name
    'Extranormal'
    >>> ex.alteration is None
    True
    >>> ex.divination is None
    False
    >>> str(ex['divination'])
    '4D'
    """

    SKILL_NAMES: ClassVar[list[str]]
    dice: DieCode
    skills: dict[str, DieCode]

    def __init__(
        self,
        base: DieCode | None = None,
        skills: dict[str, DieCode | int] | None = None,
    ) -> None:
        """
        Defines the Attribute's collection of skills.

        :param base: The base DieCode for this Attribute.
        :param skills: A mapping from Skill name to Die Code.
        """
        defaults = {s: 0 for s in self.SKILL_NAMES}
        self.dice = DieCode(1) if base is None else base  # Could be DieCode(0)
        self.skills = {}
        for name, code in (skills or defaults).items():
            match code:
                case DieCode() as die_code:
                    self.skills[name] = die_code
                case int():
                    self.skills[name] = DieCode(*divmod(code, 3))
        self.rows = sorted(self.skills.keys())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.dice!r}, {self.skills!r})"

    def row(self, n: int, width: int = 20) -> str:
        """
        Return a given row of text from the column in a tabular
        character sheet.

        :param n: row number
        :param width: text width of the row to pad with spaces.
        :returns: string with skill name and skill value.
        """
        if n < len(self.rows):
            skill_name = self.rows[n]
            die_code = self.skills[skill_name]
            skill_value = f"+{die_code}" if die_code else ""
            hspan = " " * (width - len(skill_name) - len(skill_value))
            return f"{skill_name}{hspan}{skill_value}"
        else:
            return ""

    @property
    def name(self) -> str:
        return self.__class__.__name__

    def __getattr__(self, name: str) -> Any:
        """Wraps skills: gets a value of a skill referenced by ``c.attribute.name``"""
        if name == "name":
            return self.__class__.__name__
        elif name in self.skills:
            return self.skills[name]
        elif hasattr(self.skills, name):
            return getattr(self.skills, name)
        else:
            return None

    def __getitem__(self, name: str) -> DieCode:
        """Wraps skills: gets a value of a skill referenced by ``c.attribute['name']``"""
        return cast(DieCode, self.skills.get(name))


class Acumen(Attribute):
    """The Acumen attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Acumen*: Your character's mental quickness, creativity, and attention to detail.
    """

    SKILL_NAMES = [
        "artist",
        "crafting",
        "disguise",
        "gambling",
        "hide",
        "investigation",
        "know-how",
        "search",
        "streetwise",
        "survival",
        "tracking",
    ]


class Charisma(Attribute):
    """The Charisma attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Charisma*: A gauge of emotional strength, physical attractiveness,
        and personality.
    """

    SKILL_NAMES = [
        "animal handling",
        "bluff",
        "charm",
        "command",
        "intimidation",
        "mettle",
        "persuasion",
    ]


class Intellect(Attribute):
    """The Intellect attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Intellect*: A measure of strength of memory and ability to learn.
    """

    SKILL_NAMES = [
        "cultures",
        "devices",
        "healing",
        "navigation",
        "reading/writing",
        "scholar",
        "speaking",
        "trading",
        "traps",
    ]


class Agility(Attribute):
    """The Agility attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Agility*: An indication of balance, limberness, quickness, and full-body motor abilities.
    """

    SKILL_NAMES = [
        "acrobatics",
        "climbing",
        "contortion",
        "dodge",
        "fighting",
        "flying",
        "jumping",
        "melee combat",
        "combat",
        "riding",
        "stealth",
    ]


class Coordination(Attribute):
    """The Coordination attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Coordination*: A quantification of hand-eye coordination and fine
        motor abilities.
    """

    SKILL_NAMES = [
        "charioteering",
        "lockpicking",
        "marksmanship",
        "pilotry",
        "sleight of hand",
        "throwing",
    ]


class Physique(Attribute):
    """The Physique attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Physique*: An estimation of physical power and ability to resist
        damage.
    """

    SKILL_NAMES = [
        "lifting",
        "running",
        "stamina",
        "swimming",
    ]


class Magic(Attribute):
    """The Extranormal magic attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Extranormal*: An assessment of your character's extraordinary
        abilities, which could include magic, miracles, or other extranormal
        talents. It is often listed by its type, rather than by the term "Extranormal."

    """

    SKILL_NAMES = ["alteration", "apportation", "conjuration", "divination"]


class Miracles(Attribute):
    """The Extranormal miracles attribute.

    See :external:ref:`fantasy.character_basics`.

    Rules:

        *Extranormal*: An assessment of your character's extraordinary
        abilities, which could include magic, miracles, or other extranormal
        talents. It is often listed by its type, rather than by the term "Extranormal."

    """

    SKILL_NAMES = ["divination", "favor", "strife"]


class CharacterOption:
    """Advantages, Disadvantages, Special Abilities, and (for creatures) Natural Abilities."""

    name: str = "Character Option"
    rank_cost: int = 1  # Unit is Die (3 pips)

    def __init__(self, rank: int, notes: str = "") -> None:
        self.rank = rank
        self.notes = notes

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(rank={self.rank!r}, notes={self.notes!r})"

    def __str__(self) -> str:
        return f"{self.name} (R{self.rank}), {self.notes}"

    @property
    def value(self) -> int:
        return self.rank * self.rank_cost


class Disadvantage(CharacterOption):
    """Base class of all disadvantages."""

    pass


class AchillesHeel(Disadvantage):
    name = "Achilles' Heel"


class AdvantageFlaw(Disadvantage):
    name = "Advantage Flaw"


class MinorStigma(Disadvantage):
    name = "Minor Stigma"


class Age(Disadvantage):
    name = "Age"


class BadLuck(Disadvantage):
    name = "Bad Luck"


class BurnOut(Disadvantage):
    name = "Burn-out"


class CulturalUnfamiliarity(Disadvantage):
    name = "Cultural Unfamiliarity"


class Debt(Disadvantage):
    name = "Debt"


class Devotion(Disadvantage):
    name = "Devotion"


class Employed(Disadvantage):
    name = "Employed"


class Enemy(Disadvantage):
    name = "Enemy"


class Hindrance(Disadvantage):
    name = "Hindrance"


class Infamy(Disadvantage):
    name = "Infamy"


class LanguageProblems(Disadvantage):
    name = "Language Problems"


class LearningProblems(Disadvantage):
    name = "Learning Problems"


class Poverty(Disadvantage):
    name = "Poverty"


class Prejudice(Disadvantage):
    name = "Prejudice"


class Price(Disadvantage):
    name = "Price"


class Quirk(Disadvantage):
    name = "Quirk"


class ReducedAttribute(Disadvantage):
    name = "Reduced Attribute"


class Advantage(CharacterOption):
    """Base class of all advantages."""

    pass


class Authority(Advantage):
    name = "Authority"


class Contacts(Advantage):
    name = "Contacts"


class Cultures(Advantage):
    name = "Cultures"


class Equipment(Advantage):
    name = "Equipment"


class Fame(Advantage):
    name = "Fame"


class Patron(Advantage):
    name = "Patron"


class Size(Advantage):
    name = "Size"


class TrademarkSpecialization(Advantage):
    name = "Trademark Specialization"


class Wealth(Advantage):
    name = "Wealth"


class SpecialAbility(CharacterOption):
    """Base class of all Special Abilities."""

    pass


class AcceleratedHealing(SpecialAbility):
    name = "Accelerated Healing"
    rank_cost = 3


class Ambidextrous(SpecialAbility):
    name = "Ambidextrous"
    rank_cost = 2


class AnimalControl(SpecialAbility):
    name = "Animal Control"
    rank_cost = 3


class ArmorDefeatingAttack(SpecialAbility):
    name = "Armor-Defeating Attack"
    rank_cost = 2


class AtmosphericTolerance(SpecialAbility):
    name = "Atmospheric Tolerance"
    rank_cost = 2


class AttackResistance(SpecialAbility):
    name = "Attack Resistance"
    rank_cost = 2


class AttributeScramble(SpecialAbility):
    name = "Attribute Scramble"
    rank_cost = 4


class Blur(SpecialAbility):
    name = "Blur"
    rank_cost = 3


class CombatSense(SpecialAbility):
    name = "Combat Sense"
    rank_cost = 3


class Confusion(SpecialAbility):
    name = "Confusion"
    rank_cost = 4


class Darkness(SpecialAbility):
    name = "Darkness"
    rank_cost = 3


class Elasticity(SpecialAbility):
    name = "Elasticity"
    rank_cost = 1


class Endurance(SpecialAbility):
    name = "Endurance"
    rank_cost = 1


class EnhancedSense(SpecialAbility):
    name = "Enhanced Sense"
    rank_cost = 3


class EnvironmentalResistance(SpecialAbility):
    name = "Environmental Resistance"
    rank_cost = 1


class ExtraBodyPart(SpecialAbility):
    name = "Extra Body Part"
    rank_cost = 0


class ExtraSense(SpecialAbility):
    name = "Extra Sense"
    rank_cost = 1


class FastReactions(SpecialAbility):
    name = "Fast Reactions"
    rank_cost = 3


class Fear(SpecialAbility):
    name = "Fear"
    rank_cost = 2


class Flight(SpecialAbility):
    name = "Flight"
    rank_cost = 6


class GliderWings(SpecialAbility):
    name = "Glider Wings"
    rank_cost = 3


class Hardiness(SpecialAbility):
    name = "Hardiness"
    rank_cost = 1


class Hypermovement(SpecialAbility):
    name = "Hypermovement"
    rank_cost = 1


class Immortality(SpecialAbility):
    name = "Immortality"
    rank_cost = 7


class Immunity(SpecialAbility):
    name = "Immunity"
    rank_cost = 1


class IncreasedAttribute(SpecialAbility):
    name = "Increased Attribute"
    rank_cost = 2


class InfravisionUltravision(SpecialAbility):
    name = "Infravision/Ultravision"
    rank_cost = 1


class Intangibility(SpecialAbility):
    name = "Intangibility"
    rank_cost = 5


class Invisibility(SpecialAbility):
    name = "Invisibility"
    rank_cost = 3


class IronWill(SpecialAbility):
    name = "Iron Will"
    rank_cost = 2


class LifeDrain(SpecialAbility):
    name = "Life Drain"
    rank_cost = 5


class Longevity(SpecialAbility):
    name = "Longevity"
    rank_cost = 3


class LuckGood(SpecialAbility):
    name = "Luck: Good"
    rank_cost = 2


class LuckGreat(SpecialAbility):
    name = "Luck: Great"
    rank_cost = 3


class MasterOfDisguise(SpecialAbility):
    name = "Master of Disguise"
    rank_cost = 3


class MultipleAbilities(SpecialAbility):
    name = "Multiple Abilities"
    rank_cost = 1


class NaturalArmor(SpecialAbility):
    name = "Natural Armor"
    rank_cost = 3


class NaturalHandWeapon(SpecialAbility):
    name = "Natural Hand-to-Hand Weapon"
    rank_cost = 2


class NaturalMagick(SpecialAbility):
    name = "Natural Magick"
    rank_cost = 5  # or more


class NaturalRangedWeapon(SpecialAbility):
    name = "Natural Ranged Weapon"
    rank_cost = 3


class Omnivorous(SpecialAbility):
    name = "Omnivorous"
    rank_cost = 2


class ParalyzingTouch(SpecialAbility):
    name = "Paralyzing Touch"
    rank_cost = 4


class PossessionLimited(SpecialAbility):
    name = "Possession: Limited"
    rank_cost = 8


class PossessionFull(SpecialAbility):
    name = "Possession: Full"
    rank_cost = 10


class QuickStudy(SpecialAbility):
    name = "Quick Study"
    rank_cost = 3


class SenseOfDirection(SpecialAbility):
    name = "Sense of Direction"
    rank_cost = 2


class Shapeshifting(SpecialAbility):
    name = "Shapeshifting"
    rank_cost = 3


class Silence(SpecialAbility):
    name = "Silence"
    rank_cost = 3


class SkillBonus(SpecialAbility):
    name = "Skill Bonus"
    rank_cost = 1


class SkillMinimum(SpecialAbility):
    name = "Skill Minimum"
    rank_cost = 4


class Teleportation(SpecialAbility):
    name = "Teleportation"
    rank_cost = 3


class Transmutation(SpecialAbility):
    name = "Transmutation"
    rank_cost = 5


class UncannyAptitude(SpecialAbility):
    name = "Uncanny Aptitude"
    rank_cost = 3


class Ventriloquism(SpecialAbility):
    name = "Ventriloquism"
    rank_cost = 3


class WaterBreathing(SpecialAbility):
    name = "Water Breathing"
    rank_cost = 2


class YouthfulAppearance(SpecialAbility):
    name = "Youthful Appearance"
    rank_cost = 1


class NaturalAbility(CharacterOption):
    rank_cost: int = 0

    def __init__(self, notes: str) -> None:
        self.notes = notes

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(notes={self.notes!r})"

    def __str__(self) -> str:
        return f"{self.notes}"


class OptionList(list[CharacterOption]):
    """Cooperates with :func:`pprint.pformat` to produce pretty content"""

    def __init__(self, *args: CharacterOption) -> None:
        super().__init__(args)

    def __str__(self) -> str:
        items = "; ".join(map(str, self))
        return items

    def __repr__(self) -> str:
        items = ", ".join(map(repr, self))
        return f"OptionList({items})"


## Part IV -- Character.


class CharacterBudget(Enum):
    """Sample budgets for normal and experienced characters."""

    NO_BUDGET = None
    NORMAL = SimpleNamespace(attributes=DieCode(18), skills=DieCode(7), options=DieCode(0))
    EXPERIENCED = SimpleNamespace(attributes=DieCode(18), skills=DieCode(22), options=DieCode(0))


@dataclass
class Character:
    """Character definition.

    Attributes have 18 dice = 54 pips
    Skills have 7 dice = 21 pips
    """

    # page 1
    name: str = ""
    occupation: str = ""
    race: str = ""
    gender: str = ""
    age: str = ""
    height: str = ""
    weight: str = ""
    physical_description: str = ""

    agility: Attribute = field(default=Agility(3 * D))
    intellect: Attribute = field(default=Intellect(3 * D))
    coordination: Attribute = field(default=Coordination(3 * D))
    acumen: Attribute = field(default=Acumen(3 * D))
    physique: Attribute = field(default=Physique(3 * D))
    charisma: Attribute = field(default=Charisma(3 * D))
    extranormal: Attribute = field(default=Magic(DieCode(0)))  # Or Miracles

    advantages: OptionList | list = field(default_factory=OptionList)
    disadvantages: OptionList | list = field(default_factory=OptionList)
    special_abilities: OptionList | list = field(default_factory=OptionList)
    equipment: str = ""
    description: str = ""
    realm: str = "Human realm"

    # Derivable values and defined default values
    move: int | str = 10
    strength_damage: DieCode | None = None  # Based on physique or physique.lifting
    body: int | None = None  # Based on physique roll
    wounds: dict[str, str] = field(default_factory=dict)  # Set by _wounds_table.
    funds: DieCode | None = (
        None  # Based on charisma, intellect, and intellect.trading*  # built by _funds_roll
    )
    silver: int | None = None  # Based on funds.

    # Given as part of the character
    fate_points: int | None = None
    character_points: int | None = None

    # Some page 2 sections...
    personality: str = ""
    objectives: str = ""
    native_language: str = ""
    other_notes: str = ""

    @property
    def attributes(self) -> DieCode:
        values = [
            getattr(self, name).dice
            for name in (
                "agility",
                "intellect",
                "coordination",
                "acumen",
                "physique",
                "charisma",
                "extranormal",
            )
        ]
        return sum(values, DieCode(0))

    @property
    def skills(self) -> DieCode:
        values = [
            skill_value
            for name in (
                "agility",
                "intellect",
                "coordination",
                "acumen",
                "physique",
                "charisma",
                "extranormal",
            )
            for skill_value in getattr(self, name).values()
        ]
        return sum(values, DieCode(0))

    @property
    def options(self) -> DieCode:
        debit_values = [
            option.value
            for name in (
                "advantages",
                "special_abilities",
            )
            for option in getattr(self, name)
        ]
        credit_values = [
            option.value for name in ("disadvantages",) for option in getattr(self, name)
        ]
        return DieCode.from_pips(sum(debit_values)) - DieCode.from_pips(sum(credit_values))

    @property
    def budget(self) -> dict[str, DieCode]:
        return {
            "Attributes": self.attributes,
            "Skills": self.skills,
            "Options": self.options,
        }

    def budget_check(self, check: CharacterBudget = CharacterBudget.NO_BUDGET) -> dict[str, str]:
        if check.value:
            return {
                "Attributes": f"{self.attributes or 'Nothing'} out of {check.value.attributes}",
                "Skills": f"{self.skills or 'Nothing'} out of {check.value.skills}",
                "Options": f"{self.options or 'Nothing'}",
            }
        return {name: f"{value or 'Nothing'}" for name, value in self.budget.items()}

    def __post_init__(self) -> None:
        """Set derived or default values."""
        if not self.strength_damage:
            lifting_dice = self.physique.lifting or self.physique.dice
            self.strength_damage = DieCode(int(lifting_dice.d / 2 + 0.5))
        if not self.body and self.physique.dice:
            self.body = self.physique.dice.roll().total + 20
        if not self.wounds:
            # Depends on body
            self.wounds = self._wounds_table()
        if self.funds is None:
            self.funds = self._funds_roll()
        if self.silver is None:
            # Depends on funds
            self.silver = self.funds.d * 60
        if self.fate_points is None:
            self.fate_points = 1
        if self.character_points is None:
            self.character_points = 5

        # Syntactic sugar for advantages, disadvantages, and special_abilities
        if self.advantages and not isinstance(self.advantages, OptionList):
            self.advantages = OptionList(*self.advantages)
        if self.disadvantages and not isinstance(self.disadvantages, OptionList):
            self.disadvantages = OptionList(*self.disadvantages)
        if self.special_abilities and not isinstance(self.special_abilities, OptionList):
            self.special_abilities = OptionList(*self.special_abilities)

    def _wounds_table(self) -> dict[str, str]:
        top_relative = {
            "Stunned": 0.8,
            "Wounded": 0.6,
            "Severe": 0.4,
            "Incapacitated": 0.2,
            "Mortal": 0.1,
        }
        if self.body:
            top_points = {
                name: int(0.5 + self.body * level) for name, level in top_relative.items()
            }
            # Prevent Overlaps.
            level = "Mortal"
            start = 1
            end = top_points[level]
            if end == start:
                end += 1
            ranges = [
                (level, (start, end)),
            ]
            for new_level in ("Incapacitated", "Severe", "Wounded", "Stunned"):
                last_level, (start, end) = ranges[-1]
                new_start = end
                new_end = top_points[new_level]
                while new_start >= new_end:
                    new_end += 1
                ranges.append((new_level, (new_start, new_end)))
            range_map = dict(ranges)
            return {r: f"{l}" if l + 1 == h else f"{l}-{h - 1}" for r, (l, h) in range_map.items()}
        else:
            return {r: f"{l:.0%}" for r, l in top_relative.items()}

    def _funds_roll(self) -> DieCode:
        def adj(dice: DieCode) -> int:
            if dice.d == 1:
                return -1
            elif dice.d >= 4:
                return +1
            else:
                return 0

        funds = [3, adj(self.charisma.dice), adj(self.intellect.dice)]
        trading_dice = [
            self.intellect[s].d for s in self.intellect.keys() if s.startswith("trading")
        ]
        funds.append(1 if sum(trading_dice) >= 8 else 0)
        return DieCode(max(1, sum(funds)))


@dataclass
class Creature(Character):
    natural_abilities: OptionList | list = field(default_factory=OptionList)
    note: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.natural_abilities and not isinstance(self.natural_abilities, OptionList):
            self.natural_abilities = OptionList(*self.natural_abilities)


## Part V -- Reporting and Display


class CharacterWriter:
    """Report a character for publication. Default is long form with table header."""

    base_template = textwrap.dedent("""\
    {%- block preface %}
    **OpenD6 Fantasy**
    
    {% endblock %}
    {%- block identity %}
    +--------------------------------------------------+
    | Character Name: {{c.name|pad(50-18)}} |
    +--------------------------------------------------+
    | Occupation: {{c.occupation|pad(50-14)}} |
    +-------------------------+------------------------+
    | Race: {{c.race|pad(25-8)}} | Gender: {{c.gender|pad(24-10)}} |
    +----------------+--------+-------+----------------+
    | Age: {{c.age|pad(16-8)}}  | Height: {{c.height|pad(16-10)}} | Weight: {{c.weight|pad(16-10)}} |
    +----------------+----------------+----------------+
    | Physical Description {{c.physical_description|pad(50-23)}} |
    +--------------------------------------------------+
    {% endblock %}
    {% block attributes %}
    :Agility ({{c.agility.dice}}):
        {% for skill in c.agility.skills %}{% if c.agility[skill] %}{{ skill }} {{c.agility[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Coordination ({{c.coordination.dice}}):
        {% for skill in c.coordination.skills %}{% if c.coordination[skill] %}{{ skill }} {{c.coordination[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Physique ({{c.physique.dice}}):
        {% for skill in c.physique.skills %}{% if c.physique[skill] %}{{ skill }} {{ c.physique[skill] }}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Intellect ({{c.intellect.dice}}):
        {% for skill in c.intellect.skills %}{% if c.intellect[skill] %}{{ skill }} {{c.intellect[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Acumen ({{c.acumen.dice}}):
        {% for skill in c.acumen.skills %}{% if c.acumen[skill] %}{{ skill }} {{c.acumen[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Charisma ({{c.charisma.dice}}):
        {% for skill in c.charisma.skills %}{% if c.charisma[skill] %}{{ skill }} {{c.charisma[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}
        
    :Extranormal ({{c.extranormal.dice}}):
        {% for skill in c.extranormal.skills %}{% if c.extranormal[skill] %}{{ skill }} {{c.extranormal[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}
        
    :Advantages:
        {{c.advantages}}
        
    :Disadvantages:
        {{c.disadvantages}}

    :Special Abilities:
        {{c.special_abilities}}

    :Strength Damage: {{c.strength_damage}}
    :Move: {{c.move}}
    :Fate Points: {{c.fate_points}}
    :Character Points: {{c.character_points}}
    :Body Points: {{c.body}}
    {% endblock %}
    """)

    character_template = '{% extends "base.rst" %}'

    character_list_template = textwrap.dedent("""\
    {% for c in book -%}
        {%- set n = c.name %}
        {%- include "character.rst" with context %}
        
    {% endfor %}
    """)

    character_dict_template = textwrap.dedent("""\
    {% for n, c in book.items() -%}
        {%- include "character.rst" with context %}
        
    {% endfor %}
    """)

    @staticmethod
    def pad(text: str, size: int, empty: str = "_") -> str:
        """Pad a line of text on the right"""
        if text:
            if len(text) <= size:
                return text + (size - len(text)) * " "
            else:
                return text
        else:
            return empty * size

    @staticmethod
    def lpad(text: str, size: int, empty: str = "_") -> str:
        """Pad a line of text on the left"""
        if text:
            if len(text) <= size:
                return (size - len(text)) * " " + text
            else:
                return text
        else:
            return empty * size

    @staticmethod
    def line(lines: list[str], num: int, width: int = 22) -> str:
        """
        Emits a single line of a multi-line block of text.

        :param lines: Block of text
        :param num: Line number
        :param width: width of the column
        :return: Always returns a string.
        """
        if num < len(lines):
            return lines[num]
        return " " * width

    @staticmethod
    def if_none(value: Any, otherwise: str) -> str:
        """
        A function that can be installed in Jinja to
        replace None values with a string.

        :param value: value to include in a template
        :param otherwise: value to include if ``value`` is ``None`` or an empty string
        :return: value or otherwise
        """
        if value is None:
            return otherwise
        if text := str(value):
            return text
        return otherwise

    @staticmethod
    def col_3(character: Character, equipment: bool = True) -> list[str]:
        """For some displays, the third column is a mix of various things.
        It does not trivially align with other attributes and skills in the first two columns.

        This is extracted from the character details, and cached within
        the character to slightly optimize the way the content is generated.
        """
        if not hasattr(character, "_col3"):
            width = 22
            text = []

            text.extend(
                textwrap.fill(
                    f"**Advantages**: {'; '.join(str(adv) for adv in character.advantages) or ''}",
                    width,
                ).splitlines()
            )
            text.extend(
                textwrap.fill(
                    f"**Disadvantages**: {'; '.join(str(dis) for dis in character.disadvantages) or ''}",
                    width,
                ).splitlines()
            )
            text.extend(
                textwrap.fill(
                    f"**Special Abilities**: {'; '.join(str(spec) for spec in character.special_abilities) or ''}",
                    width,
                ).splitlines()
            )
            # Simply text.
            if equipment:
                text.extend(
                    textwrap.fill(
                        f"**Equipment**: {character.equipment.replace('\n', ' ') or ''}",
                        width,
                    ).splitlines()
                )
            text.extend(
                textwrap.fill(
                    f"**Description**: {character.description.replace('\n', ' ') or ''}",
                    width,
                ).splitlines()
            )
            setattr(character, '_col3', text)
        return getattr(character, '_col3')

    def __init__(self) -> None:
        self.jinja_env: jinja2.Environment = Environment(
            # autoescape=select_autoescape()
        )
        self.jinja_env.filters |= {
            "pad": self.pad,
            "lpad": self.lpad,
            "line": self.line,
            "if_none": self.if_none,
        }
        self.jinja_env.globals |= {
            "col_3": self.col_3,
        }
        self.jinja_env.loader = jinja2.DictLoader(
            {
                "base.rst": self.base_template,
                "character.rst": self.character_template,
                "character_list.rst": self.character_list_template,
                "character_dict.rst": self.character_dict_template,
            }
        )

    @singledispatchmethod
    def report(self, character: Character) -> str:
        """RST-format for publication."""
        template = self.jinja_env.get_template("character.rst")
        return template.render(c=character)

    @report.register(list)
    def _(self, book: list[Character]) -> str:
        template = self.jinja_env.get_template("character_list.rst")
        return template.render(book=book)

    @report.register(dict)
    def _(self, book: dict[str, Character]) -> str:
        template = self.jinja_env.get_template("character_dict.rst")
        return template.render(book=book)


class CharacterWriter_Short(CharacterWriter):
    """Short-form -- no identity block."""

    character_template = textwrap.dedent("""\
    {%- extends "base.rst" -%}
    {%- block preface %}**{{ n }}**:{% endblock -%}
    {%- block identity %}{% endblock -%}
    {%- block attributes -%}
    Agility {{c.agility.dice}}, {% for skill in c.agility.skills %}{% if c.agility[skill] %}{{ skill }} {{c.agility[skill]}}, {% endif %}{% endfor %}
    Coordination {{c.coordination.dice}}, {% for skill in c.coordination.skills %}{% if c.coordination[skill] %}{{ skill }} {{c.coordination[skill]}}, {%endif%}{%endfor%}
    Physique {{c.physique.dice}}, {% for skill in c.physique.skills %}{% if c.physique[skill] %}{{ skill }} {{ c.physique[skill] }}, {%endif%}{%endfor%}
    Intellect {{c.intellect.dice}}, {% for skill in c.intellect.skills %}{% if c.intellect[skill] %}{{ skill }} {{c.intellect[skill]}}, {%endif%}{%endfor%}
    Acumen {{c.acumen.dice}}, {% for skill in c.acumen.skills %}{% if c.acumen[skill] %}{{ skill }} {{c.acumen[skill]}}, {%endif%}{%endfor%}
    Charisma {{c.charisma.dice}}, {% for skill in c.charisma.skills %}{% if c.charisma[skill] %}{{ skill }} {{c.charisma[skill]}}, {%endif%}{%endfor%}
    {%- if c.extranormal.dice -%}
    Extranormal {{c.extranormal.dice}}, {% for skill in c.extranormal.skills %}{% if c.extranormal[skill] %}{{ skill }} {{c.extranormal[skill]}}, {% endif %}{% endfor -%}
    {%- endif -%}
    {%- if c.advantages %}
    *Advantages*: {{c.advantages}}, 
    {%- endif %}
    {%- if c.disadvantages %}
    *Disadvantages*: {{c.disadvantages}}, 
    {%- endif %}
    {%- if c.special_abilities %}
    *Special Abilities*: {{c.special_abilities}}, 
    {%- endif %}
    *Move*: {{c.move}}, 
    *Strength Damage*: {{c.strength_damage}}, 
    *Fate Points*: {{c.fate_points}}, 
    *Character Points*: {{c.character_points}}, 
    *Body Points*: {{c.body}}
    {%- if c.equipment %}, *Equipment*: {{c.equipment}}{% endif -%}
    {%- if c.natural_abilities %}, *Natural Abilities*: {{c.natural_abilities|join("; ")}}{% endif -%}
    {%- if c.note %}, *Note*: {{c.note}}{% endif -%}.
    {% endblock %}
    """)


class CharacterWriter_Long2(CharacterWriter):
    """Long-form -- Base with no identity block."""

    character_template = textwrap.dedent("""\
    {%- extends "base.rst" -%}
    {%- block preface %}{% endblock -%}
    {%- block identity %}{% endblock -%}
    """)


class CharacterWriter_Table(CharacterWriter):
    character_template = textwrap.dedent("""\
    {% extends "base.rst" %}
    
    {% block attributes %}
    {%- set c_col_3 = col_3(c) %}
    +------------------------------+------------------------------+------------------------------+
    | Agility {{c.agility.dice|if_none("_____")|lpad(30-10)}} | Intellect {{c.intellect.dice|if_none("_____")|lpad(30-12)}} | {{" "|lpad(30-2)}} |                 
    +------------------------------+------------------------------+------------------------------+
    {%- for r in range(0, 13) %}
    | {{c.agility.row(r, 28)|lpad(28, " ")}} | {{c.intellect.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+                              +
    | Coordination {{c.coordination.dice|if_none("_____")|lpad(30-15)}} | Acumen {{c.acumen.dice|if_none("_____")|lpad(30-9)}} | {{c_col_3|line(13)|pad(28)}} |                 
    +------------------------------+------------------------------+                              +
    {%- for r in range(0, 13) %}
    | {{c.coordination.row(r, 28)|lpad(28, " ")}} | {{c.acumen.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r+14)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+                              +
    | Physique {{c.physique.dice|if_none("_____")|lpad(30-11)}} | Charisma {{c.charisma.dice|if_none("_____")|lpad(30-11)}} | {{c_col_3|line(27)|pad(28)}} |                 
    +------------------------------+------------------------------+                              +
    {%- for r in range(0, 13) %}
    | {{c.physique.row(r, 28)|lpad(28, " ")}} | {{c.charisma.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r+28)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+------------------------------+
    | Extranormal {{c.extranormal.dice|if_none("_____")|lpad(30-14)}} | {{" "|lpad(30-2)}} | {{" "|lpad(30-2)}} |                 
    +------------------------------+------------------------------+------------------------------+
    | {{c.extranormal.row(0, 28)|lpad(28, " ")}} | Str Damage {{c.strength_damage|if_none("_____")|lpad(30-13)}} | Body Points {{c.body|if_none("_____")|pad(30-13)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(1, 28)|lpad(28, " ")}} | Move {{c.move|string|lpad(30-7)}} | [ ] Stunned   {{c.wounds['Stunned']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(2, 28)|lpad(28, " ")}} | Fate Pts      {{c.fate_points|string|pad(30-16)}} | [ ] Wounded   {{c.wounds['Wounded']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(3, 28)|lpad(28, " ")}} | Character Pts {{c.character_points|string|pad(30-16)}} | [ ] Severe    {{c.wounds['Severe']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(4, 28)|lpad(28, " ")}} | Funds {{c.funds|string|pad(30-8)}} | [ ] Incapac'd {{c.wounds['Incapacitated']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(5, 28)|lpad(28, " ")}} | Silver {{c.silver|string|pad(30-9)}} | [ ] Mortal    {{c.wounds['Mortal']|string|pad(30-15)}}|
    |                              |                              |                              |
    |                              |                              | [ ] Dead                     |
    +------------------------------+------------------------------+------------------------------+
    {% endblock %}
    """)


class CharacterWriter_Literal(CharacterWriter):
    character_template = textwrap.dedent("""\
    {% extends "base.rst" %}
    {% block preface %}
    ..  rubric:: OpenD6 Fantasy
    
    {% endblock %}
    {% block attributes %}
    {%- set c_col_3 = col_3(c) %}
    ::
    
        +----------------------+----------------------+----------------------+
        | Agility {{c.agility.dice|string|lpad(22-10)}} | Intellect {{c.intellect.dice|string|lpad(22-12)}} | {{" "|lpad(22-2)}} |
        +----------------------+----------------------+----------------------+
        {%- for r in range(0, 13) %}
        | {{c.agility.row(r)|lpad(20)}} | {{c.intellect.row(r)|lpad(20)}} |{{c_col_3|line(r)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+{{c_col_3|line(13)|pad(22)}}|
        | Coordination {{c.coordination.dice|string|lpad(22-15)}} | Acumen {{c.acumen.dice|string|lpad(22-9)}} |{{c_col_3|line(14)|pad(22)}}|
        +----------------------+----------------------+{{c_col_3|line(15)|pad(22)}}|
        {%- for r in range(0, 13) %}
        | {{c.coordination.row(r)|lpad(20)}} | {{c.acumen.row(r)|lpad(20)}} |{{c_col_3|line(r+16)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+{{c_col_3|line(27)|pad(22)}}|
        | Physique {{c.physique.dice|string|lpad(22-11)}} | Charisma {{c.charisma.dice|string|lpad(22-11)}} |{{c_col_3|line(28)|pad(22)}}|
        +----------------------+----------------------+{{c_col_3|line(29)|pad(22)}}|
        {%- for r in range(0, 13) %}
        | {{c.physique.row(r)|lpad(20)}} | {{c.charisma.row(r)|lpad(20)}} |{{c_col_3|line(r+30)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+----------------------+
        | {{c.extranormal.name|pad(11)}} {{c.extranormal.dice|string|lpad(22-14)}} | {{" "|lpad(22-2)}} | {{" "|lpad(22-2)}} |
        +----------------------+----------------------+----------------------+
        | {{c.extranormal.row(0)|lpad(20)}} | Str Damage {{c.strength_damage|string|lpad(22-13)}} | Body Points {{c.body|string|pad(22-13)}}|
        | {{c.extranormal.row(1)|lpad(20)}} | Move {{c.move|string|lpad(22-7)}} | [ ] Stunned   {{c.wounds['Stunned']|string|pad(22-15)}}|
        | {{c.extranormal.row(2)|lpad(20)}} | Fate Pts      {{c.fate_points|string|pad(22-16)}} | [ ] Wounded   {{c.wounds['Wounded']|string|pad(22-15)}}|
        | {{c.extranormal.row(3)|lpad(20)}} | Character Pts {{c.character_points|string|pad(22-16)}} | [ ] Severe    {{c.wounds['Severe']|string|pad(22-15)}}|
        | {{c.extranormal.row(4)|lpad(20)}} | Funds {{c.funds|string|pad(22-8)}} | [ ] Incapac'd {{c.wounds['Incapacitated']|string|pad(22-15)}}|
        | {{c.extranormal.row(5)|lpad(20)}} | Silver {{c.silver|string|pad(22-9)}} | [ ] Mortal    {{c.wounds['Mortal']|string|pad(22-15)}}|
        |                      |                      | [ ] Dead             |
        +----------------------+----------------------+----------------------+
    {% endblock %}
    """)


type CharacterDict = dict[str, Character]


def summary(characters: list[Character], destination: TextIO = sys.stdout) -> None:
    """
    Write CSV summary.

    ..  todo:: CSV summary of characters. Not sure which attributes to show.
    """
    pass


class Format(Enum):
    # Matches class names.
    LONG = "CharacterWriter"
    LONG2 = "CharacterWriter_Long2"
    SHORT = "CharacterWriter_Short"
    TABLE = "CharacterWriter_Table"
    LITERAL = "CharacterWriter_Literal"


FORMAT_OPTIONS = Literal["LONG", "LONG2", "SHORT", "TABLE", "LITERAL"]


def detail(
    character: Character | list[Character] | CharacterDict,
    form: Format = Format.TABLE,
) -> None:
    """For publication, two forms: long and short."""
    writer_class = eval(form.value)
    w = writer_class()  # CharacterWriter() or CharacterWriter_Short()
    print(w.report(character))


def sheet(character: Character | list[Character] | CharacterDict) -> None:
    """Character sheet output for players to use."""
    w = CharacterWriter_Table()
    print(w.report(character))


## Part VI -- Testing and Debugging


# def budget_check(
#     character: Character, check: CharacterBudget = CharacterBudget.NO_BUDGET
# ) -> dict[str, str]:
#     if check.value:
#         return {
#             "Attributes": f"{character.attributes or 'Nothing'} out of {check.value.attr_target}",
#             "Skills": f"{character.skills or 'Nothing'} out of {check.value.skill_target}",
#             "Options": f"{character.options or 'Nothing'}",
#         }
#     return {
#         name: f"{value or 'Nothing'}"
#         for name, value in character.budget().items()
#     }


def display(character: Character, check: CharacterBudget | bool = CharacterBudget.NORMAL) -> str:
    """
    Creates a display a character in plain text to help designers.
    """

    dict_value = {
        field.name: getattr(character, field.name)
        for field in fields(character)
        if not (field.name.startswith("_"))
    }
    if check != CharacterBudget.NO_BUDGET:
        assert isinstance(check, CharacterBudget), "Change from True to CharacterBudget.NORMAL"
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
     'agility': Agility(DieCode(3, 0), {'acrobatics': DieCode(0, 0), 'climbing': DieCode(0, 0), 'contortion': DieCode(0, 0), 'dodge': DieCode(0, 0), 'fighting': DieCode(0, 0), 'flying': DieCode(0, 0), 'jumping': DieCode(0, 0), 'melee combat': DieCode(0, 0), 'combat': DieCode(0, 0), 'riding': DieCode(0, 0), 'stealth': DieCode(0, 0)}),
     'intellect': Intellect(DieCode(3, 0), {'cultures': DieCode(0, 0), 'devices': DieCode(0, 0), 'healing': DieCode(0, 0), 'navigation': DieCode(0, 0), 'reading/writing': DieCode(0, 0), 'scholar': DieCode(0, 0), 'speaking': DieCode(0, 0), 'trading': DieCode(0, 0), 'traps': DieCode(0, 0)}),
     'coordination': Coordination(DieCode(3, 0), {'charioteering': DieCode(0, 0), 'lockpicking': DieCode(0, 0), 'marksmanship': DieCode(0, 0), 'pilotry': DieCode(0, 0), 'sleight of hand': DieCode(0, 0), 'throwing': DieCode(0, 0)}),
     'acumen': Acumen(DieCode(3, 0), {'artist': DieCode(0, 0), 'crafting': DieCode(0, 0), 'disguise': DieCode(0, 0), 'gambling': DieCode(0, 0), 'hide': DieCode(0, 0), 'investigation': DieCode(0, 0), 'know-how': DieCode(0, 0), 'search': DieCode(0, 0), 'streetwise': DieCode(0, 0), 'survival': DieCode(0, 0), 'tracking': DieCode(0, 0)}),
     'physique': Physique(DieCode(3, 0), {'lifting': DieCode(0, 0), 'running': DieCode(0, 0), 'stamina': DieCode(0, 0), 'swimming': DieCode(0, 0)}),
     'charisma': Charisma(DieCode(3, 0), {'animal handling': DieCode(0, 0), 'bluff': DieCode(0, 0), 'charm': DieCode(0, 0), 'command': DieCode(0, 0), 'intimidation': DieCode(0, 0), 'mettle': DieCode(0, 0), 'persuasion': DieCode(0, 0)}),
     'extranormal': Magic(DieCode(0, 0), {'alteration': DieCode(0, 0), 'apportation': DieCode(0, 0), 'conjuration': DieCode(0, 0), 'divination': DieCode(0, 0)}),
     'advantages': OptionList(),
     'disadvantages': OptionList(),
     'special_abilities': OptionList(),
     'equipment': '',
     'description': '',
     'realm': 'Human realm',
     'move': 10,
     'strength_damage': DieCode(2, 0),
     'body': 29,
     'wounds': {'Mortal': '1-2',
                'Incapacitated': '3-5',
                'Severe': '6-11',
                'Wounded': '12-16',
                'Stunned': '17-22'},
     'funds': DieCode(3, 0),
     'silver': 180,
     'fate_points': 1,
     'character_points': 5,
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
        case _:
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
        case _:
            raise ValueError("unknown identifier {ident!r}")

    for name in keys:
        character = char_map[name]
        print("##", character.name)
        print(display(character))
        print()


def workbook_characters(context: dict[str, Any]) -> dict[str, Character]:
    """
    Emit sequence of Characters in a Workbook.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from ``Character`` name to ``Character`` instances
    """
    return {value.name: value for name, value in context.items() if isinstance(value, Character)}


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


def parse_param_name(all_characters: CharacterDict, arg_value: str) -> str | None:
    names_lc = {n.lower(): n for n in all_characters.keys()}
    matches = difflib.get_close_matches(arg_value, names_lc.keys(), 1)
    if matches:
        return names_lc[matches[0]]
    return None


def build_app(
    book: CharacterDict, *, rich_markup_mode: Literal["rich", "markdown"] | None = "rich"
) -> typer.Typer:
    characters_app = typer.Typer(
        help="Work with this collection of Characters (or Creatures).",
        rich_markup_mode=rich_markup_mode,
    )

    @characters_app.command(name="display")
    def display_command(
        format: Annotated[FORMAT_OPTIONS, typer.Option(case_sensitive=False)] = "TABLE",
    ):
        """Write RST-formatted details of all definitions to STDOUT."""
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

    @characters_app.command(name="blank")
    def blank_sheet_command():
        """Print a blank character sheet."""
        w = CharacterWriter_Table()
        # w = CharacterWriter_Literal()
        char = Character(
            agility=Agility(),
            intellect=Intellect(),
            coordination=Coordination(),
            acumen=Acumen(),
            physique=Physique(),
            charisma=Charisma(),
        )
        print(w.report(char, check=False))

    return characters_app
