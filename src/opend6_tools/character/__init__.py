"""
OpenD6 Character and Creature Definition DSL.

There are four modules in this package:

-   `The features module`_ covers :py:mod:`opend6_tools.character.features`
-   `The output module`_ covers :py:mod:`opend6_tools.character.output`
-   `The workbook module`_ covers :py:mod:`opend6_tools.character.workbook`
-   `The monsterbook module`_ covers :py:mod:`opend6_tools.character.monsterbook`
-   `The cli module`_ covers :py:mod:`opend6_tools.character.cli` and :py:mod:`opend6_tools.character.__main__`

Generally, this is imported using ``from opend6_tools.character import *``.

The ``features`` module
========================

..  automodule:: opend6_tools.character.features


The ``output`` module
=====================

..  automodule:: opend6_tools.character.output


The ``workbook`` module
========================

..  automodule:: opend6_tools.character.workbook

The ``monsterbook`` module
===========================

..  automodule:: opend6_tools.character.monsterbook

The ``cli`` module
===================

..  automodule:: opend6_tools.character.cli

The ``__main__`` module
-----------------------

..  automodule:: opend6_tools.character.__main__

"""

from .features import *
from .output import *
from .workbook import *
from .monsterbook import *

__all__ = [
    "Character",
    "Creature",
    "Sword",
    "D",
    "DieCode",
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
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
    "OptionList",
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
    # Workbook functions
    "workbook_characters",
    "workbook_groupBy",
    # Main App
    "CharacterBudget",
    "summary",
    "Format",
    "detail",
    "display",
    "debug",
    "sheet",
    "CharacterWriter",
    "CharacterWriter_Short",
    "CharacterWriter_Literal",
    "CharacterWriter_Table",
    "CharacterWriter_HTML1",
    "CharacterWriter_HTML2",
    "CharacterWriter_LaTeX",
    "parse_param_name",
    "build_app",
    # Some handy names
    "sys",
    "Annotated",
    "partial",
]
