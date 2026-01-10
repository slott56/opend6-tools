..  _character_module:

##########################
 ``character``
##########################

..  py:module:: opend6_tools.character
    :no-index:

The Character (and Creature) DSL
===================================

Characters (and Creatures) are defined in Python modules.
This makes testing and publication relatively straightforward.

-   An application imports the definitions and applies ordinary software testing techniques to be sure the syntax is correct. A small computation can assure the budget of dice match expectations.

-   The module is an application that emits RST-format files for publication.

The top-level organization of Character and Creature modules in the context of campaign books looks like this.
The source is a ``creatures_subsection.py`` file with the Python version of the creature definitions.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    title Campaign Documents

    package python {
        component character.py
    }

    package characters {
        component creatures_subsection.py {
            component Creature
        }
        creatures_subsection.py ..> character.py : imports
    }

    note "Validates design details" as note_1
    note_1 .. creatures_subsection.py

    package rules {
        package creature_section {
            component creatures_subsection.rst
        }
        creatures_subsection.rst <-- creatures_subsection.py : "created by running with 'display'"
    }

    note "Creates unique campaign documents" as note_2
    note_2 .. creatures_subsection.rst

    @enduml

Often, the characters or creatures are created interactively, using Jupyter Lab.
This means the :py:mod:`opend6_tools.notebook_extract` builds the module from the notebook.
For more information, see :ref:`notebook_extract_app`.

The structure within the spell definition module is a Python list object.
The structure within any creature or character definition module is a Python list object.
A book of characters (or creatures) is a ``list[Character]``.
A Character is an object with a number of other ``Attributes`` and ``Options``.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        title Character or Creature Module Components

        object "list[Creature]" as book

        object Creature {
            name
            attributes
            options
        }
        book *-- "1..m" Creature

        object Attribute {
            description
            dice
        }
        Creature *-- "6..7" Attribute

        object Option {
            description
            dice
        }
        Creature *-- "0..m" Option

        object "~_~_test~_~_" as test
        book <.. test

        object app
        book <.. app

    @enduml

The :py:class:`Character` definition is almost identical to the :py:class:`Creature` definition.

A creature can have a collection of abilities that are natural abilities. These come from the pool of Special Ability definitions, but don't have an associated cost.

Character and Creature
----------------------

A Character (and a Creature) is a collection of  :py:class:`Attribute` objects and a number of distinct :py:class:`CharacterOption` objects.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    class Character {
        name: str
        occupation: str
        race: str
        gender: str
        age: str
        height: str
        weight: str
        physical_description: str

        agility: Agility
        intellect: Intellect
        coordination: Coordination
        acumen: Acumen
        physique: Physique
        charisma: Charisma
        extranormal: Magic | Miracles

        advantages: OptionList
        disadvantages: OptionList
        special_abilities: OptionList
        equipment: str
        description: str
        realm: str
        fate_points: int
        character_points: int

        .. computable ..
        move: int
        strength_damage: DieCode
        body: int
        finds: DieCode
    }

    abstract class Attribute
    Attribute <|-- Agility
    Attribute <|-- Intellect
    Attribute <|-- Coordination
    Attribute <|-- Acumen
    Attribute <|-- Physique
    Attribute <|-- Charisma
    Attribute <|-- Magic
    Attribute <|-- Miracles

    Character *-- Agility
    Character *-- Intellect
    Character *-- Coordination
    Character *-- Acumen
    Character *-- Physique
    Character *-- Charisma
    Character *-- Magic
    Character *-- Miracles
    Character *-- OptionList

    class OptionList <<list[CharacterOption]>>

    abstract class CharacterOption
    OptionList *-- "0..m" CharacterOption

    abstract class Disadvantage
    CharacterOption <|-- Disadvantage
    abstract class Advantage
    CharacterOption <|-- Advantage
    abstract class SpecialAbility
    CharacterOption <|-- SpecialAbility

    class Creature {
        natural_abilities: OptionList
    }
    Character <|--- Creature
    Creature -- OptionList

    @enduml

The character has a wide variety of features.

Attributes
----------

The attribute model covers the six required attributes, plus the optional, Extranormal, attribute.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram


    abstract class Attribute {
        skills: dict[str, DieCode
    }

    class DieCode {
        dice: int
        pips: int
    }
    Attribute *-- DieCode

    Attribute <|-- Agility
    Attribute <|-- Intellect
    Attribute <|-- Coordination
    Attribute <|-- Acumen
    Attribute <|-- Physique
    Attribute <|-- Charisma
    Attribute <|-- Magic
    Attribute <|-- Miracles

    @enduml

The attributes (and skills) have a simple, uniform
definition.
Each skill description has a :py:class:`DieCode` cost.
Other skills default to the :py:class:`DieCode` cost of the :py:class:`Attribute`.

Options
-------

There are three distinct types of character options.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    abstract class CharacterOption {
        rank: int
        notes: str
        dice: DieCode
    }

    abstract class Disadvantage
    CharacterOption <|-- Disadvantage
    abstract class Advantage
    CharacterOption <|-- Advantage
    abstract class SpecialAbility
    CharacterOption <|-- SpecialAbility

    @enduml

Each subclass -- :py:class:`Disadvantage`, :py:class:`Advantage`, and :py:class:`SpecialAbility` -- is a flat class hierarchy.

..  uml::

    @startuml

        'https://plantuml.com/class-diagram

    abstract class CharacterOption {
        {static} rank_cost: int = 1
        rank: int
        notes: str
    }

    abstract class Disadvantage
    CharacterOption <|-- Disadvantage

    class AchillesHeel
    Disadvantage <|-- AchillesHeel

    class AdvantageFlaw
    Disadvantage <|-- AdvantageFlaw

    class MinorStigma
    Disadvantage <|-- MinorStigma

    class Age
    Disadvantage <|-- Age

    class BadLuck
    Disadvantage <|-- BadLuck

    class BurnOut
    Disadvantage <|-- BurnOut

    class CulturalUnfamiliarity
    Disadvantage <|-- CulturalUnfamiliarity

    class Debt
    Disadvantage <|-- Debt

    class Devotion
    Disadvantage <|-- Devotion

    class Employed
    Disadvantage <|-- Employed

    class Enemy
    Disadvantage <|--- Enemy

    class Hindrance
    Disadvantage <|--- Hindrance

    class Infamy
    Disadvantage <|--- Infamy

    class LanguageProblems
    Disadvantage <|--- LanguageProblems

    class LearningProblems
    Disadvantage <|--- LearningProblems

    class Poverty
    Disadvantage <|--- Poverty

    class Prejudice
    Disadvantage <|--- Prejudice

    class Price
    Disadvantage <|--- Price

    class Quirk
    Disadvantage <|--- Quirk

    class ReducedAttribute
    Disadvantage <|--- ReducedAttribute

    @enduml

Generally, the Advantages are a flat list of class definitions. The only unique features are name of the option.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    abstract class CharacterOption {
        {static} rank_cost: int = 1
        rank: int
        notes: str
    }

    abstract class Advantage
    CharacterOption <|-- Advantage

    class Authority
    Advantage <|-- Authority

    class Contacts
    Advantage <|-- Contacts

    class Cultures
    Advantage <|-- Cultures

    class Equipment
    Advantage <|-- Equipment

    class Fame
    Advantage <|-- Fame

    class Patron
    Advantage <|-- Patron

    class Size
    Advantage <|-- Size

    class TrademarkSpecialization
    Advantage <|-- TrademarkSpecialization

    class Wealth
    Advantage <|-- Wealth

    @enduml

The Special Abilities include a class-level ``rank_cost`` value that's not simply set to one. Each special ability has a distinct rank cost.

Generally, this is a flat list of class definitions. The only unique features are the rank cost and the name of the option.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    abstract class CharacterOption {
        {static} rank_cost: int
        rank: int
        notes: str
    }

    abstract class SpecialAbility {
        {static} rank_cost: int
    }
    CharacterOption <|-- SpecialAbility

    class AcceleratedHealing
    SpecialAbility <|-- AcceleratedHealing

    class Ambidextrous
    SpecialAbility <|-- Ambidextrous

    class AnimalControl
    SpecialAbility <|-- AnimalControl

    class ArmorDefeatingAttack
    SpecialAbility <|-- ArmorDefeatingAttack

    class AtmosphericTolerance
    SpecialAbility <|-- AtmosphericTolerance

    class AttackResistance
    SpecialAbility <|-- AttackResistance

    class AttributeScramble
    SpecialAbility <|-- AttributeScramble

    class Blur
    SpecialAbility <|-- Blur

    class CombatSense
    SpecialAbility <|-- CombatSense

    class Confusion
    SpecialAbility <|--- Confusion

    class Darkness
    SpecialAbility <|--- Darkness

    class Elasticity
    SpecialAbility <|--- Elasticity

    class Endurance
    SpecialAbility <|--- Endurance

    class EnhancedSense
    SpecialAbility <|--- EnhancedSense

    class EnvironmentalResistance
    SpecialAbility <|--- EnvironmentalResistance

    class ExtraBodyPart
    SpecialAbility <|--- ExtraBodyPart

    class ExtraSense
    SpecialAbility <|--- ExtraSense

    class FastReactions
    SpecialAbility <|--- FastReactions

    class Fear
    SpecialAbility <|--- Fear

    class Flight
    SpecialAbility <|---- Flight

    class GliderWings
    SpecialAbility <|---- GliderWings

    class Hardiness
    SpecialAbility <|---- Hardiness

    class Hypermovement
    SpecialAbility <|---- Hypermovement

    class Immortality
    SpecialAbility <|---- Immortality

    class Immunity
    SpecialAbility <|---- Immunity

    class IncreasedAttribute
    SpecialAbility <|---- IncreasedAttribute

    class InfravisionUltravision
    SpecialAbility <|---- InfravisionUltravision

    class Intangibility
    SpecialAbility <|---- Intangibility

    class Invisibility
    SpecialAbility <|---- Invisibility

    class IronWill
    SpecialAbility <|----- IronWill

    class LifeDrain
    SpecialAbility <|----- LifeDrain

    class Longevity
    SpecialAbility <|----- Longevity

    class LuckGood
    SpecialAbility <|----- LuckGood

    class LuckGreat
    SpecialAbility <|----- LuckGreat

    class MasterOfDisguise
    SpecialAbility <|----- MasterOfDisguise

    class MultipleAbilities
    SpecialAbility <|----- MultipleAbilities

    class NaturalArmor
    SpecialAbility <|----- NaturalArmor

    class NaturalHandWeapon
    SpecialAbility <|----- NaturalHandWeapon

    class NaturalMagick
    SpecialAbility <|----- NaturalMagick

    class NaturalRangedWeapon
    SpecialAbility <|----- NaturalRangedWeapon

    class Omnivorous
    SpecialAbility <|------ Omnivorous

    class ParalyzingTouch
    SpecialAbility <|------ ParalyzingTouch

    class PossessionLimited
    SpecialAbility <|------ PossessionLimited

    class PossessionFull
    SpecialAbility <|------ PossessionFull

    class QuickStudy
    SpecialAbility <|------ QuickStudy

    class SenseOfDirection
    SpecialAbility <|------ SenseOfDirection

    class Shapeshifting
    SpecialAbility <|------ Shapeshifting

    class Silence
    SpecialAbility <|------ Silence

    class SkillBonus
    SpecialAbility <|------ SkillBonus

    class SkillMinimum
    SpecialAbility <|------ SkillMinimum

    class Teleportation
    SpecialAbility <|------ Teleportation

    class Transmutation
    SpecialAbility <|------ Transmutation

    class UncannyAptitude
    SpecialAbility <|------ UncannyAptitude

    class Ventriloquism
    SpecialAbility <|------ Ventriloquism

    class WaterBreathing
    SpecialAbility <|------ WaterBreathing

    class YouthfulAppearance
    SpecialAbility <|------ YouthfulAppearance
    @enduml

Foundational Definitions
-------------------------

Here are some additional definitions used widely in this module.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    class Roll

    class CriticalSuccess
    Roll <|-- CriticalSuccess

    class CriticalFailure
    Roll <|-- CriticalFailure

    class DieCode

    DieCode --> Roll : "Creates"

    @enduml

The :py:class:`DieCode` is more than merely a definition of dice.
It can also roll to generate values for strength damage and body.
This includes the *OpenD6* "Wild Die" rules, creating values with a somewhat larger distribution.

Implementation
==============

..  automodule:: opend6_tools.character
