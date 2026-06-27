"""
A DSL for defining Spells, Invocations, Cantrips, and Items.

There are four modules in this package:

-   `The spells Module`_ covers :py:mod:`opend6_tools.magic.spells`
-   `The output Module`_ covers :py:mod:`opend6_tools.magic.output`
-   `The workbook Module`_ covers :py:mod:`opend6_tools.magic.workbook`
-   `The spellbook Module`_ covers :py:mod:`opend6_tools.magic.spellbook`

Generally, this is imported using ``from opend6_tools.magic import *``.

The ``spells`` module
=====================

..  automodule:: opend6_tools.magic.spells

The ``output`` module
======================

..  automodule:: opend6_tools.magic.output

The ``workbook`` module
=======================

..  automodule:: opend6_tools.magic.workbook

The ``spellbook`` module
=========================

..  automodule:: opend6_tools.magic.spellbook


"""

from ..dice import *
from .spells import *
from .output import *
from .spellbook import *
from .workbook import *

__all__ = [
    # Base definitions for Aggregate Root objects.
    "D",
    "Spell",
    "Miracle",
    "Cantrip",
    "Item",
    # Effects
    "Effect",
    "GenericEffect",
    "CompositeEffect",
    "DamageEffect",
    "ProtectionEffect",
    "MassEffect",
    "DistanceEffect",
    "TimeEffect",
    "VolumeEffect",  # Is this really AreaEffect?
    "SkillEffect",
    "AttributeEffect",
    "DisadvantageEffect",
    "SpecialAbilityEffect",
    "Limitation",
    "Enhancement",
    "CharacteristicType",
    "CharactersticAdjustmentType",
    "SpecialAbilityType",
    "LimitationType",
    "EnhancementType",
    "DisadvantageType",
    # Aspects
    "Aspect",
    "GenericAspect",
    "ArcaneKnowledgeAspect",
    "AreaEffectAspect",
    "CastingTimeAspect",
    "ChangeTargetAspect",
    "ChargesAspect",
    "CommunityAspect",
    "ComponentsAspect",
    "ConcentrationAspect",
    "CountenanceAspect",
    "DistanceAspect",
    "DurationAspect",
    "FeedbackAspect",
    "FocusedAspect",
    "GesturesAspect",
    "IncantationsAspect",
    "MultipleTargetAspect",
    "OtherAlterant",
    "RangeAspect",
    "SpeedAspect",
    "TimeAspect",
    "UnrealEffectAspect",
    "VariableEffectAspect",
    "VariableDurationAspect",
    "VariableMovementAspect",
    "TargetType",
    "ChargesType",
    "CommunitySizeType",
    "CommunityParticipationType",
    "ComponentRarityType",
    "ComponentQuantityType",
    "CountenanceVisibilityType",
    "GestureComplexityType",
    "IncantationComplexityType",
    "MultiTargetType",
    "UnrealDisbeliefType",
    "VariableDurationType",
    "VariableMovementType",
    "PriceDifficultyType",
    # Implementation details, rarely used by spell definitions...
    "Difficulty",
    "Measure",
    "Modifier",
    "Factor",
    "Lookup",
    "QualifiedLookup",
    "Unit",
    "Time",
    "TimeUnit",
    "Mass",
    "MassUnit",
    "Distance",
    "DistUnit",
    "Volume",  # Is this really AreaEffect?
    "VolumeUnit",  # Is this really AreaEffect?
    "AreaVolumeUnit",
    "DieCode",
    "DiceUnit",
    "ChargesUnit",
    # Output
    "TableSummary",
    "display",
    "detail",
    "debug",
    "dumps",
    # Workbook Tools
    "workbook_validation",
    "workbook_rank",
    "workbook_spells",
    # The main app, and useful names for spell book modules.
    "build_app",
    "typer",
    "Annotated",
    "Any",
]
