"""
OpenD6 Character and Creature Features for the DSL.


Example
-------

>>> from random import seed
>>> seed(42)

>>> from opend6_tools.character import *
>>> human = Character(
...     occupation="Default", race="Human"
... )
>>> human.physique.dice
3*D
>>> human.extranormal.dice
0*D
>>> human.budget_check(CharacterBudget.NORMAL)
{'Attributes': '18D out of 18D', 'Skills': 'Nothing out of 7D', 'Options': 'Nothing'}
>>> human.budget
{'Attributes': 18*D, 'Skills': 0*D, 'Options': 0*D}

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
    | alteration           | Str Damage        2D | Body Points 28       |
    | apportation          | Move              10 | [ ] Stunned   17-21  |
    | conjuration          | Fate Pts      1      | [ ] Wounded   11-16  |
    | divination           | Character Pts 5      | [ ] Severe    6-10   |
    | ____________________ | Funds 3D             | [ ] Incapac'd 3-5    |
    | ____________________ | Silver 180           | [ ] Mortal    1-2    |
    |                      |                      | [ ] Dead             |
    +----------------------+----------------------+----------------------+
<BLANKLINE>

Top-Level Things
----------------

..  autoclass:: Character
    :members:
    :undoc-members:
    :member-order:  bysource

..  autoclass:: Creature
    :members:
    :undoc-members:
    :member-order:  bysource

..  autoclass:: Sword
    :members:
    :undoc-members:
    :member-order:  bysource


..  autoclass:: OptionList
    :members:

..  autoclass:: CharacterOption
    :members:

..  autoclass:: CharacterBudget
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


"""

from dataclasses import dataclass, field
from enum import Enum
from functools import partial
import re
import sys
from textwrap import dedent
from types import SimpleNamespace
from typing import Annotated, Any, ClassVar, cast

from humre import *  # noqa: F403  # type: ignore[import-untyped]

from ..dice import DieCode, D
from ..magic.spells import (
    DISADVANTAGE_RULES,
    SPECIALABILITY_RULES,
    parse_rule_table,
)

__all__ = [
    "Character",
    "Creature",
    "Sword",
    # Base definitions
    "D",
    "DieCode",
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
    # Attributes
    "Attribute",
    "Agility",
    "Intellect",
    "Coordination",
    "Acumen",
    "Physique",
    "Charisma",
    "Miracles",
    "Magic",
    # Other Features
    "Advantage",
    "Disadvantage",
    "SpecialAbility",
    "NaturalAbility",
    "OptionList",  # Use instead of [] or list()
    "NoteList",
    "AchillesHeel",  # type: ignore
    "AdvantageFlaw",  # type: ignore
    "MinorStigma",
    "Age",  # type: ignore
    "BadLuck",  # type: ignore
    "BurnOut",  # type: ignore
    "CulturalUnfamiliarity",  # type: ignore
    "Debt",  # type: ignore
    "Devotion",  # type: ignore
    "Employed",  # type: ignore
    "Enemy",  # type: ignore
    "Hindrance",  # type: ignore
    "Infamy",  # type: ignore
    "LanguageProblems",  # type: ignore
    "LearningProblems",  # type: ignore
    "Poverty",  # type: ignore
    "Prejudice",  # type: ignore
    "Price",  # type: ignore
    "Quirk",  # type: ignore
    "ReducedAttribute",  # type: ignore
    "Authority",  # type: ignore
    "Contacts",  # type: ignore
    "Cultures",  # type: ignore
    "Equipment",  # type: ignore
    "Fame",  # type: ignore
    "Patron",  # type: ignore
    "Size",  # type: ignore
    "TrademarkSpecialization",  # type: ignore
    "Wealth",  # type: ignore
    "AcceleratedHealing",  # type: ignore
    "Ambidextrous",  # type: ignore
    "AnimalControl",  # type: ignore
    "ArmorDefeatingAttack",  # type: ignore
    "AtmosphericTolerance",  # type: ignore
    "AttackResistance",  # type: ignore
    "AttributeScramble",  # type: ignore
    "Blur",  # type: ignore
    "CombatSense",  # type: ignore
    "Confusion",  # type: ignore
    "Darkness",  # type: ignore
    "Elasticity",  # type: ignore
    "Endurance",  # type: ignore
    "EnhancedSense",  # type: ignore
    "EnvironmentalResistance",  # type: ignore
    "ExtraBodyPart",  # type: ignore
    "ExtraSense",  # type: ignore
    "FastReactions",  # type: ignore
    "Fear",  # type: ignore
    "Flight",  # type: ignore
    "GliderWings",  # type: ignore
    "Hardiness",  # type: ignore
    "Hypermovement",  # type: ignore
    "Immortality",  # type: ignore
    "Immunity",  # type: ignore
    "IncreasedAttribute",  # type: ignore
    "InfravisionUltravision",  # type: ignore
    "Intangibility",  # type: ignore
    "Invisibility",  # type: ignore
    "IronWill",  # type: ignore
    "LifeDrain",  # type: ignore
    "Longevity",  # type: ignore
    "LuckGood",  # type: ignore
    "LuckGreat",  # type: ignore
    "MasterOfDisguise",  # type: ignore
    "MultipleAbilities",  # type: ignore
    "NaturalArmor",  # type: ignore
    "NaturalHandWeapon",
    "PainTolerance",
    "NaturalMagick",  # type: ignore
    "NaturalRangedWeapon",  # type: ignore
    "Omnivorous",  # type: ignore
    "ParalyzingTouch",  # type: ignore
    "PossessionLimited",  # type: ignore
    "PossessionFull",  # type: ignore
    "QuickStudy",  # type: ignore
    "SenseOfDirection",  # type: ignore
    "Shapeshifting",  # type: ignore
    "Silence",  # type: ignore
    "SkillBonus",  # type: ignore
    "SkillMinimum",  # type: ignore
    "Teleportation",  # type: ignore
    "Transmutation",  # type: ignore
    "UncannyAptitude",  # type: ignore
    "Ventriloquism",  # type: ignore
    "WaterBreathing",  # type: ignore
    "YouthfulAppearance",  # type: ignore
    # Main App
    "CharacterBudget",
    # Some handy names
    "sys",
    "Annotated",
    "partial",
]

## Part I, Foundational Definitions (not used)

## Part II, Units (not used)

## Part III, character DSL, Attributes and Skills

R1 = 1
R2 = 2
R3 = 3
R4 = 4
R5 = 5
R6 = 6


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
                case _:  # pragma: no cover
                    raise ValueError(f"must be DieCode or int, not {type(code)}")
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
            skill_value = f"{die_code}" if die_code else ""
            hspan = " " * (width - len(skill_name) - len(skill_value))
            return f"{skill_name}{hspan}{skill_value}"
        else:
            return ""

    @property
    def name(self) -> str:
        return self.__class__.__name__

    def __getattr__(self, name: str) -> Any:
        """Wraps skills: gets a value of a skill referenced by ``c.attribute.name``"""
        if name in self.skills:
            return self.skills[name]
        elif hasattr(self.skills, name):
            return getattr(self.skills, name)
        else:
            return None

    def __getitem__(self, name: str) -> DieCode:
        """Wraps skills: gets a value of a skill referenced by ``attribute['name']``."""
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


def classify(text: str) -> str:
    """Make a Python class name from a word or phrase.
    This is lossy and not fully reversible.

    >>> classify("Possession: Limited")
    'PossessionLimited'
    >>> classify("Infravision/Ultravision")
    'InfravisionUltravision'
    """
    words = re.split(r"\W+", text.strip().lower())
    return "".join(map(lambda w: w.title(), words))


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

    def __eq__(self, other: Any) -> bool:
        match other:
            case CharacterOption() as option:
                return self.rank == option.rank and self.notes == option.notes
            case _:  # pragma: no cover
                return NotImplemented

    @property
    def value(self) -> int:
        return self.rank * self.rank_cost


class Disadvantage(CharacterOption):
    """Base class of all disadvantages.

    >>> disad = Disadvantage(2, "some details")
    >>> str(disad)
    'Disadvantage (R2), some details'
    """

    name = "Disadvantage"

    pass


# Parse the source text table to create the types
for label, rank_cost in parse_rule_table(DISADVANTAGE_RULES):
    class_name = classify(label)
    globals()[class_name] = type(class_name, (Disadvantage,), {"name": label})


# Added in unpublished Magic rules, not in the Fantasy rules table being parsed.
class MinorStigma(Disadvantage):
    name = "Minor Stigma"


# class AchillesHeel(Disadvantage):
#     name = "Achilles' Heel"
#
#
# class AdvantageFlaw(Disadvantage):
#     name = "Advantage Flaw"
#
#
# class MinorStigma(Disadvantage):
#     name = "Minor Stigma"
#
#
# class Age(Disadvantage):
#     name = "Age"
#
#
# class BadLuck(Disadvantage):
#     name = "Bad Luck"
#
#
# class BurnOut(Disadvantage):
#     name = "Burn-out"
#
#
# class CulturalUnfamiliarity(Disadvantage):
#     name = "Cultural Unfamiliarity"
#
#
# class Debt(Disadvantage):
#     name = "Debt"
#
#
# class Devotion(Disadvantage):
#     name = "Devotion"
#
#
# class Employed(Disadvantage):
#     name = "Employed"
#
#
# class Enemy(Disadvantage):
#     name = "Enemy"
#
#
# class Hindrance(Disadvantage):
#     name = "Hindrance"
#
#
# class Infamy(Disadvantage):
#     name = "Infamy"
#
#
# class LanguageProblems(Disadvantage):
#     name = "Language Problems"
#
#
# class LearningProblems(Disadvantage):
#     name = "Learning Problems"
#
#
# class Poverty(Disadvantage):
#     name = "Poverty"
#
#
# class Prejudice(Disadvantage):
#     name = "Prejudice"
#
#
# class Price(Disadvantage):
#     name = "Price"
#
#
# class Quirk(Disadvantage):
#     name = "Quirk"
#
#
# class ReducedAttribute(Disadvantage):
#     name = "Reduced Attribute"

ADVANTAGE_RULES = dedent("""\
    Authority (R1, R2, R3)
    Contacts (R1, R2, R3, R4)
    Cultures (R1, R2, R3, R4)
    Equipment (R1, R2, R3, R4)
    Fame (R1, R2, R3)
    Patron (R1, R2, R3)
    Size (R1 or more)
    Trademark Specialization (R1)
    Wealth (R1 or more)
    """)


class Advantage(CharacterOption):
    """Base class of all advantages."""

    name = "Advantage"

    pass


# Parse the source text table to create the types

for label, rank_cost in parse_rule_table(ADVANTAGE_RULES):
    class_name = classify(label)
    globals()[class_name] = type(class_name, (Advantage,), {"name": label})

# class Authority(Advantage):
#     name = "Authority"
#
#
# class Contacts(Advantage):
#     name = "Contacts"
#
#
# class Cultures(Advantage):
#     name = "Cultures"
#
#
# class Equipment(Advantage):
#     name = "Equipment"
#
#
# class Fame(Advantage):
#     name = "Fame"
#
#
# class Patron(Advantage):
#     name = "Patron"
#
#
# class Size(Advantage):
#     name = "Size"
#
#
# class TrademarkSpecialization(Advantage):
#     name = "Trademark Specialization"
#
#
# class Wealth(Advantage):
#     name = "Wealth"


class SpecialAbility(CharacterOption):
    """Base class of all Special Abilities."""

    name = "SpecialAbility"
    pass


# Parse the source text table to create the types

for label, rank_cost in parse_rule_table(SPECIALABILITY_RULES):
    class_name = classify(label)
    number, *words = rank_cost.split()  # type: ignore
    globals()[class_name] = type(
        class_name, (SpecialAbility,), {"name": label, "rank_cost": int(number)}
    )


# An alias introduced in the previous version
class NaturalHandWeapon(NaturalHandToHandWeapon):  # type: ignore
    pass


# A new special ability, introduced in Fantasy Locations
class PainTolerance(SpecialAbility):
    name = "Pain Tolerance"
    rank_cost = 2


# class AcceleratedHealing(SpecialAbility):
#     name = "Accelerated Healing"
#     rank_cost = 3
#
#
# class Ambidextrous(SpecialAbility):
#     name = "Ambidextrous"
#     rank_cost = 2
#
#
# class AnimalControl(SpecialAbility):
#     name = "Animal Control"
#     rank_cost = 3
#
#
# class ArmorDefeatingAttack(SpecialAbility):
#     name = "Armor-Defeating Attack"
#     rank_cost = 2
#
#
# class AtmosphericTolerance(SpecialAbility):
#     name = "Atmospheric Tolerance"
#     rank_cost = 2
#
#
# class AttackResistance(SpecialAbility):
#     name = "Attack Resistance"
#     rank_cost = 2
#
#
# class AttributeScramble(SpecialAbility):
#     name = "Attribute Scramble"
#     rank_cost = 4
#
#
# class Blur(SpecialAbility):
#     name = "Blur"
#     rank_cost = 3
#
#
# class CombatSense(SpecialAbility):
#     name = "Combat Sense"
#     rank_cost = 3
#
#
# class Confusion(SpecialAbility):
#     name = "Confusion"
#     rank_cost = 4
#
#
# class Darkness(SpecialAbility):
#     name = "Darkness"
#     rank_cost = 3
#
#
# class Elasticity(SpecialAbility):
#     name = "Elasticity"
#     rank_cost = 1
#
#
# class Endurance(SpecialAbility):
#     name = "Endurance"
#     rank_cost = 1
#
#
# class EnhancedSense(SpecialAbility):
#     name = "Enhanced Sense"
#     rank_cost = 3
#
#
# class EnvironmentalResistance(SpecialAbility):
#     name = "Environmental Resistance"
#     rank_cost = 1
#
#
# class ExtraBodyPart(SpecialAbility):
#     name = "Extra Body Part"
#     rank_cost = 0
#
#
# class ExtraSense(SpecialAbility):
#     name = "Extra Sense"
#     rank_cost = 1
#
#
# class FastReactions(SpecialAbility):
#     name = "Fast Reactions"
#     rank_cost = 3
#
#
# class Fear(SpecialAbility):
#     name = "Fear"
#     rank_cost = 2
#
#
# class Flight(SpecialAbility):
#     name = "Flight"
#     rank_cost = 6
#
#
# class GliderWings(SpecialAbility):
#     name = "Glider Wings"
#     rank_cost = 3
#
#
# class Hardiness(SpecialAbility):
#     name = "Hardiness"
#     rank_cost = 1
#
#
# class Hypermovement(SpecialAbility):
#     name = "Hypermovement"
#     rank_cost = 1
#
#
# class Immortality(SpecialAbility):
#     name = "Immortality"
#     rank_cost = 7
#
#
# class Immunity(SpecialAbility):
#     name = "Immunity"
#     rank_cost = 1
#
#
# class IncreasedAttribute(SpecialAbility):
#     name = "Increased Attribute"
#     rank_cost = 2
#
#
# class InfravisionUltravision(SpecialAbility):
#     name = "Infravision/Ultravision"
#     rank_cost = 1
#
#
# class Intangibility(SpecialAbility):
#     name = "Intangibility"
#     rank_cost = 5
#
#
# class Invisibility(SpecialAbility):
#     name = "Invisibility"
#     rank_cost = 3
#
#
# class IronWill(SpecialAbility):
#     name = "Iron Will"
#     rank_cost = 2
#
#
# class LifeDrain(SpecialAbility):
#     name = "Life Drain"
#     rank_cost = 5
#
#
# class Longevity(SpecialAbility):
#     name = "Longevity"
#     rank_cost = 3
#
#
# class LuckGood(SpecialAbility):
#     name = "Luck: Good"
#     rank_cost = 2
#
#
# class LuckGreat(SpecialAbility):
#     name = "Luck: Great"
#     rank_cost = 3
#
#
# class MasterOfDisguise(SpecialAbility):
#     name = "Master of Disguise"
#     rank_cost = 3
#
#
# class MultipleAbilities(SpecialAbility):
#     name = "Multiple Abilities"
#     rank_cost = 1
#
#
# class NaturalArmor(SpecialAbility):
#     name = "Natural Armor"
#     rank_cost = 3
#
#
# class NaturalHandWeapon(SpecialAbility):
#     name = "Natural Hand-to-Hand Weapon"
#     rank_cost = 2
#
#
# class NaturalMagick(SpecialAbility):
#     name = "Natural Magick"
#     rank_cost = 5  # or more
#
#
# class NaturalRangedWeapon(SpecialAbility):
#     name = "Natural Ranged Weapon"
#     rank_cost = 3
#
#
# class Omnivorous(SpecialAbility):
#     name = "Omnivorous"
#     rank_cost = 2
#
#
# class ParalyzingTouch(SpecialAbility):
#     name = "Paralyzing Touch"
#     rank_cost = 4
#
#
# class PossessionLimited(SpecialAbility):
#     name = "Possession: Limited"
#     rank_cost = 8
#
#
# class PossessionFull(SpecialAbility):
#     name = "Possession: Full"
#     rank_cost = 10
#
#
# class QuickStudy(SpecialAbility):
#     name = "Quick Study"
#     rank_cost = 3
#
#
# class SenseOfDirection(SpecialAbility):
#     name = "Sense of Direction"
#     rank_cost = 2
#
#
# class Shapeshifting(SpecialAbility):
#     name = "Shapeshifting"
#     rank_cost = 3
#
#
# class Silence(SpecialAbility):
#     name = "Silence"
#     rank_cost = 3
#
#
# class SkillBonus(SpecialAbility):
#     name = "Skill Bonus"
#     rank_cost = 1
#
#
# class SkillMinimum(SpecialAbility):
#     name = "Skill Minimum"
#     rank_cost = 4
#
#
# class Teleportation(SpecialAbility):
#     name = "Teleportation"
#     rank_cost = 3
#
#
# class Transmutation(SpecialAbility):
#     name = "Transmutation"
#     rank_cost = 5
#
#
# class UncannyAptitude(SpecialAbility):
#     name = "Uncanny Aptitude"
#     rank_cost = 3
#
#
# class Ventriloquism(SpecialAbility):
#     name = "Ventriloquism"
#     rank_cost = 3
#
#
# class WaterBreathing(SpecialAbility):
#     name = "Water Breathing"
#     rank_cost = 2
#
#
# class YouthfulAppearance(SpecialAbility):
#     name = "Youthful Appearance"
#     rank_cost = 1


class NaturalAbility(CharacterOption):
    name = "NaturalAbility"
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


class NoteList(list[str]):
    """
    A collection of notes that can be exploded by line (like an ``OptionList``),
    or collapsed into a blob of text.
    """

    def __init__(self, *args: str) -> None:
        if len(args) == 1 and isinstance(args[0], str):
            # Parse a ";" separated string of items.
            items = (arg.strip() for arg in args[0].split(";"))
            super().__init__(items)
        else:
            super().__init__(args)

    def __str__(self) -> str:
        items = "; ".join(map(str, self))
        return items

    def __repr__(self) -> str:
        items = ", ".join(map(repr, self))
        return f"NoteList({items})"


## Part IV, Character DSL


class CharacterBudget(Enum):
    """Sample budgets for normal and experienced characters."""

    NO_BUDGET = None
    NORMAL = SimpleNamespace(
        attributes=DieCode(18), skills=DieCode(7), options=DieCode(0)
    )
    EXPERIENCED = SimpleNamespace(
        attributes=DieCode(18), skills=DieCode(22), options=DieCode(0)
    )


@dataclass
class Character:
    """Character definition.

    Attributes have 18 dice = 54 pips
    Skills have 7 dice = 21 pips
    """

    # Identification Block
    name: str = ""
    occupation: str = ""
    race: str = ""
    gender: str = ""
    age: str = ""
    height: str | None = ""  # Use None to force a computation.
    weight: str | None = ""
    physical_description: str = ""

    # Features
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

    # Special case for simple characters shown in the text.
    description: str = ""

    # Extension used for Creatures in Kingdom of the East.
    realm: str = "Human realm"

    # Features with derivable values and defined default values
    move: int | str = 10
    strength_damage: DieCode | None = None  # Based on physique or physique.lifting
    body: int | DieCode | None = None  # Based on physique roll + 20
    wounds: dict[str, str] = field(default_factory=dict)  # Set by _wounds_table.
    funds: DieCode | None = (
        None  # Based on charisma, intellect, and intellect.trading*  # built by funds_roll
    )
    silver: int | None = None  # Based on funds.

    # Given as part of the character
    fate_points: int | None = None
    character_points: int | None = None

    # Some page 2 sections...
    equipment: NoteList = field(default_factory=NoteList)  #: type, notes; ...
    armor: NoteList = field(default_factory=NoteList)  #: type, AV, notes; ...
    weapons: NoteList = field(
        default_factory=NoteList
    )  #: type, dmg, range (S, M, L), ammo; ...
    spells: NoteList = field(default_factory=NoteList)  #: name, difficulty, notes; ...

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
            option.value
            for name in ("disadvantages",)
            for option in getattr(self, name)
        ]
        debit = DieCode.from_pips(sum(debit_values))
        credit = DieCode.from_pips(sum(credit_values))
        return debit - credit

    @property
    def budget(self) -> dict[str, DieCode]:
        return {
            "Attributes": self.attributes,
            "Skills": self.skills,
            "Options": self.options,
        }

    def budget_check(
        self, check: CharacterBudget = CharacterBudget.NO_BUDGET
    ) -> dict[str, str]:
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
        if self.body and isinstance(self.body, DieCode):
            self.body = self.body.roll().total
        elif self.body is None and self.physique.dice:
            self.body = self.physique.dice.roll().total + 20
        elif self.body == 0:
            # Special case for using wound-levels.
            pass
        else:
            # Ordinary case -- body was provided and is non-zero.
            pass
        if not self.wounds:
            # Depends on body being zero or non-zero
            self.wounds = self._wounds_table()
        if self.funds is None:
            # Depends on charisma, intellect, and trading skill
            self.funds = self.funds_roll()
        if self.silver is None:
            # Depends on funds
            self.silver = self.funds.d * 60
        if self.fate_points is None:
            self.fate_points = 1
        if self.character_points is None:
            self.character_points = 5
        if self.height is None or self.weight is None:
            # Depends on Physique and gender
            # Implicitly, it also depends on the symmetry parameter
            h, w = self.height_weight_roll()
            if self.height is None:
                self.height = h
            if self.weight is None:
                self.weight = w

        # Syntactic sugar for OptionList and NoteList attributes.
        # TODO: Look for fields with type OptionList
        for nm in "advantages", "disadvantages", "special_abilities":
            attr_value = getattr(self, nm)
            if attr_value and not isinstance(attr_value, OptionList):
                setattr(self, nm, OptionList(*attr_value))

        # TODO: Look for fields with type NoteList
        for nm in "equipment", "armor", "weapons", "spells":
            attr_value = getattr(self, nm)
            if attr_value and isinstance(attr_value, str):
                setattr(self, nm, NoteList(attr_value))
            elif attr_value and not isinstance(attr_value, NoteList):
                setattr(self, nm, NoteList(*attr_value))

    def _wounds_table(self) -> dict[str, str]:
        top_relative = {
            "Stunned": 0.8,
            "Wounded": 0.6,
            "Severe": 0.4,
            "Incapacitated": 0.2,
            "Mortal": 0.1,
        }
        if self.body and isinstance(self.body, DieCode):  # pragma: no cover
            # Should be handled by ``__post_init__()``.
            self.body = self.body.roll().total
        if self.body:
            # Non-zero, the typical case.
            top_points = {
                name: int(0.5 + cast(int, self.body) * level)
                for name, level in top_relative.items()
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
            return {
                r: f"{l}" if l + 1 == h else f"{l}-{h - 1}"
                for r, (l, h) in range_map.items()
            }
        else:
            # body=None (or zero, which seems unlikely)
            return {r: f"{l:.0%}" for r, l in top_relative.items()}

    def funds_roll(self) -> DieCode:
        """
        From the Character Basics rules, Funds section.

            'All characters start with a base of 3 in Funds. Use the accompanying table to adjust this number.'
        """

        def adj(dice: DieCode) -> int:
            if dice.d == 1:
                return -1
            elif dice.d >= 4:
                return +1
            else:
                return 0

        funds = [3, adj(self.charisma.dice), adj(self.intellect.dice)]
        trading_dice = [
            self.intellect[s].d
            for s in self.intellect.keys()
            if s.startswith("trading")
        ]
        funds.append(1 if sum(trading_dice) >= 8 else 0)
        return DieCode(max(1, sum(funds)))

    def height_weight_roll(self, symmetric: bool = False) -> tuple[str, str]:
        """
        Some notes...

        - Female characters

          - Mass (kg): 48 + 3 × Physique roll

          - Height (cm): 155 + Physique roll

        - Male characters

          - Mass (kg): 70 + 2 × Physique roll

          - Height (cm): 169 + Physique roll

        :param symmetric: If True, one roll is used to limit variability.
            If False, separate height and weight rolls are used.
            The default is False, no height-weight symmetry.
        :return: tuple of height and weight strings.
        """
        if "female" in self.gender.lower():
            mass_base, mass_scale, height_base = 48, 3, 155
        else:
            mass_base, mass_scale, height_base = 78, 2, 169
        if symmetric:
            roll = self.physique.dice.roll().total
            weight = mass_base + mass_scale * roll
            height = height_base + roll
        else:
            weight = mass_base + mass_scale * self.physique.dice.roll().total
            height = height_base + self.physique.dice.roll().total
        return f"{height}cm", f"{weight}kg"


@dataclass
class Creature(Character):
    natural_abilities: OptionList | list = field(default_factory=OptionList)
    note: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.natural_abilities and not isinstance(
            self.natural_abilities, OptionList
        ):
            self.natural_abilities = OptionList(*self.natural_abilities)


@dataclass
class Sword(Character):
    natural_abilities: OptionList | list = field(default_factory=OptionList)
    note: str = ""

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.natural_abilities and not isinstance(
            self.natural_abilities, OptionList
        ):
            self.natural_abilities = OptionList(*self.natural_abilities)


type CharacterDict = dict[str, Character]
