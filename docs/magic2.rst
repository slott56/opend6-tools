..  _magic_module:

#######################
 ``magic2``
#######################

..  py:module:: opend6_tools.magic2
    :no-index:

The Spell (and Miracle) DSL
===================================

Spells are defined in Python modules.
This makes testing and publication relatively straightforward.

-   An application imports the definitions and applies ordinary software testing techniques to be sure the syntax is correct. A small computation can assure the difficulties match expectations.

-   The module is an application that emits RST-format files for publication.

The top-level organization of Spell modules in the context of campaign books looks like this.
The source is a ``spells_subsection.py`` file with the Python version of the spell definitions.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Campaign Documents

    package python {
        package opend6_tools {
            component magic2.py
        }
    }

    package document_source {
        artifact magic.rst <<RST>>
        package spells {
            component spells_subsection.py <<app>> {
                component SomeSpell
            }
            artifact spells_subsection.txt <<RST>>
            spells_subsection.py ..> magic2.py : import
        }
        spells_subsection.txt <- spells_subsection.py : "Run with 'display'"
        magic.rst --> spells_subsection.txt : """include::"" directive"
    }

    @enduml

Often, the spells are created interactively, using Jupyter Lab.
This means the :py:mod:`opend6_tools.notebook_extract` builds the module from the notebook.
For more information, see :ref:`notebook_extract_app`.

The structure within the spell definition module is a Python list object.
A book of spells is a ``list[Spell]``.
A Spell (or a Miracle) is an object with an ``Effect`` and a number of other ``Aspects``.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        title Spell Module Components

        object "list[Spell]" as book

        object Spell {
            name: str
            effect: Effect
            duration: Aspect
            range: Aspect
            speed: Aspect
            casting_time: Aspect
            other_aspects: dict[str, Aspect]
            other_conditions: list[Aspect]
        }
        book *-- "1..m" Spell

        object Effect {
            description
            difficulty
        }
        Spell -- "1" Effect

        object Aspect {
            description
            difficulty
        }
        Spell *-- "4..m" Aspect

        object "~_~_test~_~_" as test
        book <.. test

        object app
        book <.. app

    @enduml

The details of ``Effect`` and ``Aspect`` objects are rather complicated.
We'll start by looking at the top-level class, :py:class:`Spell`.


Spell
------

A Spell definition (and a Miracle and a Cantrip) is a collection of an :py:class:`Effect` object and a number of distinct :py:class:`Aspect` objects.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    class Spell {
        name: str
        notes: str
        skill: str
        effect: Effect
        duration: DurationAspect
        range: RangeAspect
        casting_time: CastingTimeAspect
        speed: SpeedAspect
        other_aspects: OtherAspects
        other_conditions: list[GenericAspect]
        .. computed ..
        difficulty: int
        --
        finalize() -> int
    }

    Spell -- Effect
    Spell -- DurationAspect
    Spell -- RangeAspect
    Spell -- CastingTimeAspect
    Spell -- SpeedAspect
    Spell -- OtherAspects
    OtherAspects *-- Aspect
    Spell *-- GenericAspect

    class OtherAspects <<TypedDict>>

    abstract class Aspect {
        description
        difficulty
    }
    Aspect <|-- DurationAspect
    Aspect <|-- RangeAspect
    Aspect <|-- CastingTimeAspect
    Aspect <|-- SpeedAspect
    Aspect <|-- GenericAspect

    abstract class Effect {
        description
        difficulty
    }

    class Miracle
    Spell <|--- Miracle

    class Cantrip
    Spell <|--- Cantrip

    @enduml

There are a lot of specializations of the :py:class:`Aspect` class.
There are also a number of specializations of the :py:class:`Effect` class.
What's important is that each specialization has unique rules for the units of measure that are permitted for that aspect or effect.

We'll start by looking at the possible Effects of a spell.

Effects
-------

There are a surprising variety of effect definitions.
Any of a character's attributes or skills can be changed magically.
Doing damage (and protecting from damage) are specialized combat-like
magical properties.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        interface IncreasesDifficulty

        class Spell {
            effect: Effect
        }

        abstract class Aspect {
            difficulty() -> int
            points() -> int
            description() -> str
        }

        abstract class Effect {
            skill() -> str
        }
        IncreasesDifficulty <|--- Effect
        Aspect <|-- Effect

        Spell *--- Effect

        abstract class MeasureEffect
        Effect <|-- MeasureEffect

        class DamageEffect
        MeasureEffect <|-- DamageEffect
        DieUnit <|--- DamageEffect

        class ProtectionEffect
        MeasureEffect <|-- ProtectionEffect
        DieUnit <|--- ProtectionEffect

        class SkillEffect
        MeasureEffect <|-- SkillEffect
        DieUnit <|--- SkillEffect

        class AttributeEffect
        SkillEffect <|-- AttributeEffect

        class SpecialAbilityEffect
        Effect <|-- SpecialAbilityEffect
        SpecialAbilityLookup <|--- SpecialAbilityEffect

        class SpecialAbilityLookup
        AbilityLookup <|-- SpecialAbilityLookup

        class AbilityLookup
        Lookup <|-- AbilityLookup

        class DisadvantageEffect
        Effect <|-- DisadvantageEffect

        class TimeEffect
        MeasureEffect <|-- TimeEffect
        TimeUnit <|--- TimeEffect

        class DistanceEffect
        MeasureEffect <|-- DistanceEffect
        DistUnit <|-- DistanceEffect

        class MassEffect
        MeasureEffect <|-- MassEffect
        MassUnit <|--- MassEffect

        class VolumeEffect
        MeasureEffect <|-- VolumeEffect
        VolumeUnit <|--- VolumeEffect

        class CompositeEffect
        IncreasesDifficulty <|-- CompositeEffect
        Aspect <|-- CompositeEffect
        CompositeEffect *-- "2..n" Effect

        class Unit
        Lookup <|-- Unit
        class DieUnit
        Unit <|-- DieUnit
        class TimeUnit
        Unit <|-- TimeUnit
        class MassUnit
        Unit <|-- MassUnit
        class DistUnit
        Unit <|-- DistUnit
        class VolumeUnit
        Unit <|-- VolumeUnit

    @enduml

The central idea is that all effects have two common features:

-   They all increase the difficulty of a spell.

-   They all have a difficulty and a description.

This commonality stems from all effects actually being based on the a general foundational definition of :py:class:`Aspect`.

The effect details differ in the details of how the difficulty is computed from the description.
There are two parts to this:

-   The general :py:class:`MeasureEffect` defines effect difficulty based on some measure in standard Kilogram-Meter-Second physical units.
    This is a two-step computation.
    Given descriptive text, :math:`t`, the measure, :math:`m`, is derived from the description, :math:`m(t)`.
    The difficulty, :math:`d`, is computed from the measure, :math:`d(m(t))`.

-   A specific :py:class:`Unit` converts unit text to standardized measure values.

For subclasses of :py:class:`Unit`, there is a unit of measure, and a value associated with that.

For subclass of :py:class:`Lookup`, there is a fixed list of valid values.

The :py:class:`CompositeEffect` is a container for two or more individual :py:class:`Effect` instances.


Aspects
-------

The aspects are based on a hierarchy of classes, rooted at :py:class:`Aspect`.
There are three groupings of :py:class:`Aspect` subclasses:

-   The four core Aspects. Three of these increase the overall difficulty, while one -- :py:class:`CastingTimeAspect` decreases the overall difficulty.

-   Other Aspects that increase the difficulty.

-   Aspects that decrease the difficulty.

First, the "Core Aspects".
Most of these increase difficulty.
The exception is :py:class:`CastingTimeAspect`.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    interface IncreasesDifficulty
    interface DecreasesDifficulty

    class Spell {
        effect: Effect
        duration: DurationAspect
        range: RangeAspect
        speed: SpeedAspect
        casting_time: CastingTimeAspect
    }

    abstract class Aspect {
        difficulty() -> int
        points() -> int
        description() -> str
    }

    abstract class TimeAspect
    Aspect <|-- TimeAspect
    TimeUnit <|-- TimeAspect

    abstract class DistanceAspect
    Aspect <|-- DistanceAspect
    DistUnit <|-- DistanceAspect

    class RangeAspect
    DistanceAspect <|-- RangeAspect
    IncreasesDifficulty <|-- RangeAspect

    class SpeedAspect
    TimeAspect <|-- SpeedAspect
    IncreasesDifficulty <|-- SpeedAspect

    class DurationAspect
    TimeAspect <|-- DurationAspect
    IncreasesDifficulty <|-- DurationAspect

    class CastingTimeAspect
    TimeAspect <|-- CastingTimeAspect
    DecreasesDifficulty <|-- CastingTimeAspect

    Spell *--- DurationAspect
    Spell *--- RangeAspect
    Spell *--- SpeedAspect
    Spell *--- CastingTimeAspect

    @enduml

These four core aspects are required for every Spell.
The duration, range, and speed increase the difficulty.
The casting time decreases the difficulty.

These are the "Other Aspects" that will increase the difficulty of a spell.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    interface IncreasesDifficulty
    'interface DecreasesDifficulty

    class ChoiceStringMatch {
        parse_str()
    }
    class ChoiceStringPattern{
        parse_str()
    }

    abstract class BaseLookup {
        choices
        parse()
    }
    class Lookup {
        parse()
        value()
    }
    ChoiceStringMatch <|-- Lookup
    BaseLookup <|-- Lookup

    class Modifier {
        values()
    }
    Lookup <|-- Modifier
    note "modifies difficulty directly;\nno measure conversion" as note_1
    note_1 .. Modifier

    abstract class Aspect {
        difficulty() -> int
        points() -> int
        description() -> str
    }

    class GenericAspect
    Aspect <|-- GenericAspect
    GenericAspect --|> IncreasesDifficulty

    /' abstract class TimeAspect
    Aspect <|-- TimeAspect
    TimeUnit <|-- TimeAspect
    '/

    /' abstract class DistanceAspect
    Aspect <|-- DistanceAspect
    DistUnit <|-- DistanceAspect
    '/

    class AreaModifier
    Modifier <|-- AreaModifier
    ChoiceStringPattern <|-- AreaModifier

    class AreaEffectAspect
    AreaEffectAspect --|> IncreasesDifficulty
    AreaModifier <|-- AreaEffectAspect
    Aspect <|-- AreaEffectAspect

    class TargetModifier
    Modifier <|-- TargetModifier

    class ChangeTargetAspect
    ChangeTargetAspect --|> IncreasesDifficulty
    TargetModifier <|-- ChangeTargetAspect
    Aspect <|-- ChangeTargetAspect

    class ChargesUnit
    Unit <|-- ChargesUnit

    class ChargesAspect
    ChargesAspect --|> IncreasesDifficulty
    ChargesUnit <|-- ChargesAspect
    Aspect <|-- ChargesAspect

    'Community
    'Component
    'Concentration
    'Countenance
    'Feedback

    class FocusedAspect
    FocusedAspect --|> IncreasesDifficulty
    Aspect <|-- FocusedAspect

    'Gestures
    'Incantations

    class MultiTargetsModifier
    Modifier <|-- MultiTargetsModifier

    class MultipleTargetAspect
    MultipleTargetAspect --|> IncreasesDifficulty
    MultiTargetsModifier <|-- MultipleTargetAspect
    Aspect <|-- MultipleTargetAspect

    'UnrealEffect

    class VariableDurationModifier
    Modifier <|-- VariableDurationModifier

    class VariableDurationAspect
    VariableDurationAspect --|> IncreasesDifficulty
    VariableDurationModifier <|-- VariableDurationAspect
    Aspect <|-- VariableDurationAspect

    class VariableEffectAspect
    VariableEffectAspect --|> IncreasesDifficulty
    Aspect <|-- VariableEffectAspect

    class VariableMovementModifier
    Modifier <|-- VariableMovementModifier

    class VariableMovementAspect
    IncreasesDifficulty  <|--- VariableMovementAspect
    VariableMovementModifier  <|-- VariableMovementAspect
    Aspect <|-- VariableMovementAspect

    class ArcaneKnowledgeAspect
    GenericAspect <|-- ArcaneKnowledgeAspect

    @enduml

There is little commonality among these aspects of a spell.

These are the "Other Aspects" that will decrease the difficulty of a spell.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    ' interface IncreasesDifficulty
    interface DecreasesDifficulty

    abstract class Aspect {
        difficulty() -> int
        points() -> int
        description() -> str
    }

    class Lookup {
        parse()
        value()
    }
    class Factor
    Lookup <|-- Factor

    class CommunityAspect
    Aspect <|-- CommunityAspect
    CommunityAspect ---|> DecreasesDifficulty

    class CommunityModifier
    Unit <|-- CommunityModifier
    class CommunityDifficulty
    Unit <|-- CommunityDifficulty
    class CommunityParticipationFactor
    Factor <|-- CommunityParticipationFactor

    CommunityAspect -- CommunityModifier
    CommunityAspect -- CommunityDifficulty
    CommunityAspect -- CommunityParticipationFactor


    class ComponentsModifier
    Modifier <|-- ComponentsModifier

    class ComponentsFactor
    Factor <|-- ComponentsFactor
    ComponentsAspect -- ComponentsFactor

    class ComponentsAspect
    Aspect <|-- ComponentsAspect
    ComponentsAspect ---|> DecreasesDifficulty

    class ConcentrationAspect
    Aspect <|-- ConcentrationAspect
    ConcentrationAspect ---|> DecreasesDifficulty

    class CountenanceModifier
    Modifier <|-- CountenanceModifier

    class CountenanceAspect
    Aspect <|-- CountenanceAspect
    CountenanceModifier <|-- CountenanceAspect
    CountenanceAspect  ---|> DecreasesDifficulty

    class FeedbackAspect
    Aspect <|-- FeedbackAspect
    Modifier <|-- FeedbackAspect
    FeedbackAspect  ---|> DecreasesDifficulty

    class GesturesModifier
    Modifier <|-- GesturesModifier

    class GesturesAspect
    Aspect <|-- GesturesAspect
    GesturesModifier <|-- GesturesAspect
    GesturesAspect ---|> DecreasesDifficulty

    class IncantationsModifier
    Modifier <|-- IncantationsModifier

    class IncantationsAspect
    Aspect <|-- IncantationsAspect
    IncantationsModifier <|-- IncantationsAspect
    IncantationsAspect ---|> DecreasesDifficulty

    class UnrealFactor
    Factor <|-- UnrealFactor

    class UnrealEffectAspect
    Aspect <|-- UnrealEffectAspect
    UnrealFactor <|-- UnrealEffectAspect
    UnrealEffectAspect ---|> DecreasesDifficulty

    @enduml

There is little commonality among these aspects of a spell.

Foundational Definitions
------------------------

These are classes for the atomic attributes of an ``Aspect`` or ``Effect``.

First, the ubiquitous mixin class definitions to increase or decrease the difficulty.
Each of these adds a single attribute value to a class definition.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        enum Sign {
            Increase
            Decrease
        }

        interface DifficultyAdjustment {
            incr_decr: Sign
        }
        class IncreasesDifficulty {
            incr_decr = Sign.Increase
        }
        class DecreasesDifficulty {
            incr_decr = Sign.Decrease
        }
        DifficultyAdjustment <|-- IncreasesDifficulty
        DifficultyAdjustment <|-- DecreasesDifficulty
        Sign --- IncreasesDifficulty
        Sign --- DecreasesDifficulty

        class Aspect
        class Effect

        IncreasesDifficulty <|-- Effect
        IncreasesDifficulty <|-- Aspect
        DecreasesDifficulty <|-- Aspect

        class Spell {
            finalize()
        }
        Spell -- Effect
        Spell *-- "4..m" Aspect

    @enduml

The :py:meth:`Spell.finalize` method makes use of this to compute the final difficulty.

In essence, the algorithm for the difficulty of a spell, :math:`d(S)`, is this:

..  math::

    E &= \{d(a) | a \in S \textbf{ and $\operatorname{sign}(a) = \texttt{Increase}$}\} \\
    A &= \{d(a) | a \in S \textbf{ and $\operatorname{sign}(a) = \texttt{Decrease}$}\} \\
    d(S) &= \frac{(\sum E - \sum A)}{2}

This examines all of the Aspects of a Spell, including the Effect, the core Aspects, the Other Aspects and the Other Conditions.
It classifies each difficulty based on the enumerated value of the :py:class:`Sign`.
It sums the difficulty of each aspect, :math:`d(a)`, to get the Spell Total, :math:`E`, and a Negative Modifiers, :math:`A`.
From this, the net difficulty is computed.

Here are some additional foundational class definitions.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        abstract class BaseLookup {
            choices
            parse(text)
        }

        abstract class Lookup {
            choices: dict[name, Any]
            parse(text)
            value(measure)
        }

        class ChoiceStringMatch {
            parse_str(text)
        }

        ChoiceStringMatch <|-- Lookup
        BaseLookup <|-- Lookup

        class Modifier {
            value(measure)
        }
        Lookup <|-- Modifier

        class Factor
        Lookup <|-- Factor

        class Unit {
            value(measure)
        }
        Lookup <|-- Unit

    @enduml

A Unit is a measure (kilogram, meter, second-based).
There's a transformation from the measure to a difficulty value.
This is approximately :math:`v = \lceil 5 \log_{10}(m) \rceil`.

A Modifier is a difficulty value provided by the rules.

A Factor is a multiplier applied to a difficulty modifier or the value created from a measure.

A DieUnit is a special unit that maps DieCodes to values.
Each ``1D`` has a value of 3.

Units: Mass, Distance, Time
-----------------------------

The Measures have three specific Units for mass, distance, and time.
These are based on kilograms, meters, and seconds.
We can define specific subclasses for the *OpenD6* rules.

These measures are part of a number of Aspects.
They also figure into many of the Effects.
Here are the Aspect relationships:

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        interface DifficultyAdjustment {
            incr_decr: Sign
        }

        abstract class Lookup {
            choices: dict[name, Any]
            parse(text)
            value(measure)
        }

        class Unit {
            value(measure)
        }
        Lookup <|-- Unit

        class TimeUnit {
            choices: dict[name, Any]
        }
        Unit <|-- TimeUnit

        class DistUnit {
            choices: dict[name, Any]
        }
        Unit <|-- DistUnit

        DifficultyAdjustment <|-- Aspect  : "Mixin"
        Aspect -- Factor : "Strategy"

        class TimeAspect
        TimeUnit <|-- TimeAspect : "Mixin"
        Aspect <|-- TimeAspect

        class DistanceAspect
        DistUnit <|-- DistanceAspect : "Mixin"
        Aspect <|-- DistanceAspect

    @enduml

Mass (in kilograms) and distance (in meters) have a very regular structure.
Time (in seconds) has some irregularities. Many time units,
including minutes, hours, days, and weeks have easy-to-understand values.
Months are a mess.
Years -- on average -- are less of a mess than months; it makes sense to ignore Gregorian Laap Year
computations and simply treat all years as 365.25 days long.

For effects, there are some more units than time and distance.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        abstract class Lookup {
            choices: dict[name, Any]
            parse(text)
            value(measure)
        }

        class Unit {
            value(measure)
        }
        Lookup <|-- Unit

        class DieUnit
        Unit <|-- DieUnit

        class TimeUnit {
            choices: dict[name, Any]
        }
        Unit <|-- TimeUnit

        class DistUnit {
            choices: dict[name, Any]
        }
        Unit <|-- DistUnit

        class MassUnit {
            choices: dict[name, Any]
        }
        Unit <|-- MassUnit

        class VolumeUnit {
            choices: dict[name, Any]
        }
        Unit <|-- VolumeUnit

        IncreasesDifficulty <|-- Effect  : "Mixin"
        Effect -- Factor : "Strategy"
        Effect -- Modifier : "Strategy"
        Unit <|-- Effect : "Mixin"

    @enduml

What's important here is that the :py:class:`Unit` parsing is a matter of splitting the text into a number and a unit string.
The string uses the parent :py:class:`Lookup` to locate the scaling factor.

The :py:class:`DieUnit` is special because it doesn't have a Kilogram-Meter-Second physical unit, but instead uses a ``nD+p`` pattern.

A very few spells reference Volume.
This is typically cubic meters, to remain consistent with other measures.
A liter is :math:`\frac{1}{100}` of a cubic meter.

..  _magic_module.implementation:

Implementation
===============

..  automodule:: opend6_tools.magic2
