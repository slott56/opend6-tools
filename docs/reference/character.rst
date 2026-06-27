..  _character_package:

..  py:module:: opend6_tools.character
    :no-index:

#########################
  ``character`` Package
#########################


The :py:mod:`opend6_tools.character` module provides the DSL definitions for characters and creatures.
The module has a number of features for creating formatted displays of characters, working with creature or character definitions as command-line application, and extracting definitions from a Jupyter Lab notebook.

Here's an illustration of the structure of this package:

..  uml::

    @startuml
    'https://plantuml.com/component-diagram

    title character package components

    package opend6_tools {

    component dice

    package character {
        component features
        component output
        component workbook
        component monsterbook
        component cli
        component "~__main__"

        features ..> dice
        workbook ..> features
        output ..> features
        cli ..> features
        "~__main__" ..> cli
        monsterbook ..> features
        monsterbook ..> workbook
    }
    }

    package jinja2
    package typer

    output ..> jinja2
    cli ..> typer
    monsterbook ..> typer

    component character_sheet

    character_sheet ..> "~__main__"

    @enduml


..  py:module:: opend6_tools.character.features
    :no-index:

Defining Characters and Creatures
=================================

The :py:mod:`opend6_tools.character` module provides the definitions for the Character (and Creature) DSL.
We'll start by looking at the overall context in which characters (or creatures) are defined.
Then we can look at the details of how the :py:class:`Character` class is designed.

Because the **make** tool relies on file definitions,
it helps to isolate creature and character definitions into distinct Python modules.
Any of a number of organizing principles could be used for creatures, including likely environments in which they are found, or the number of dice in their budget.
The top-level organization of Character and Creature modules in the context of campaign books is what a software architect might call an "aggregate root."

Often, the characters or creatures are created interactively, using Jupyter Lab.
This means the :py:mod:`opend6_tools.notebook_extract` builds the module from the notebook.
For more information, see :ref:`notebook_extract_app`.

The structure within the character or creature definition module is often a Python list object.
A Character is an object with a number of other ``Attributes`` and ``Options``.
Here is the essential structure:

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Creature Book overview

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

    object app {
        display
        debug
    }
    book <.. app

    @enduml

The :py:class:`Character` definition is almost identical to the :py:class:`Creature` definition.

A creature can have a collection of abilities that are natural abilities. These come from the same pool as the Special Ability definitions, but don't have an associated cost.

The Character Class
--------------------

A Character (and a Creature) is a collection of descriptive strings.
For the purposese of computing the dice budget, there are :py:class:`Attribute` objects and a number of distinct :py:class:`OptionList` objects.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Character or Creature class structure

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
        equipment: NoteList
        armor: NoteList
        weapons: NoteList
        spells: NoteList
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
    Attribute <|-- Coordination
    Attribute <|-- Physique
    Attribute <|--- Intellect
    Attribute <|--- Acumen
    Attribute <|--- Charisma
    Attribute <|---- Magic
    Attribute <|---- Miracles

    Character *-- "{6..7}" Attribute
    /'Character *-- Agility
    Character *-- Intellect
    Character *-- Coordination
    Character *-- Acumen
    Character *-- Physique
    Character *-- Charisma
    Character *-- Magic
    Character *-- Miracles
    '/

    class OptionList <<list[CharacterOption]>>
    abstract class CharacterOption
    OptionList *-- "0..m" CharacterOption
    Character *-- OptionList : "advantages\ndisadvantages\nspecial_abilities"

    class NoteList <<list[str]>>
    Character *-- NoteList : "equipment\narmor\nweapons\nspells"

    abstract class Disadvantage
    CharacterOption <|-- Disadvantage
    abstract class Advantage
    CharacterOption <|-- Advantage
    abstract class SpecialAbility
    CharacterOption <|-- SpecialAbility

    class Creature {
        natural_abilities: OptionList
    }
    Character <|-- Creature
    Creature -- OptionList : "natural abilities"

    @enduml

A Character has a wide variety of features.
The mandatory few are attributes with their associated skills.
A number of values have derived default values (like body and funds).
Other features are optional.
And yet more features are descriptive text.

Attribute Classes
-----------------

A Character (and most creatures) have six required Attribute values.
There are three physical and three mental attributes.
Optionally, some characters or creatures may have an *Extranormal*, attribute.

While the game play consequence of each attribute are profound,
from the perspective of defining a character, they're all essentially identical.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Character or Creature Attributes

    abstract class Attribute {
        skills: dict[str, DieCode]
    }

    class DieCode {
        dice: int
        pips: int
    }
    Attribute *- DieCode

    Attribute <|-- Agility
    Attribute <|-- Coordination
    Attribute <|-- Physique
    Attribute <|--- Intellect
    Attribute <|--- Acumen
    Attribute <|--- Charisma
    Attribute <|---- Magic
    Attribute <|---- Miracles

    @enduml

The attributes (and skills) have a simple, uniform
definition.
Each skill description has a name and a :py:class:`DieCode` cost.

During game play, the skill defines how many dice are rolled
to overcome difficulties.
Any skill without a specific budget defaults to the :py:class:`DieCode` cost of the controlling :py:class:`Attribute` for that skill.

Options
-------

Beyond the core attributes, a character or creature may have
options.
There are three distinct types of character options.

For creatures (and some non-human characters) an option
may be identified as a "natural ability".
This small shift in terminology permits pigs to fly, by
calling the special ability of flight a natural ability.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Character or Creature Advantages and Limitations

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

Each of these subclasses -- :py:class:`Disadvantage`, :py:class:`Advantage`, and :py:class:`SpecialAbility` -- is the parent of  a flat collection of subclasses.
The only unique feature to each subclass is the costs-per-rank of the option.

Here are the subclasses of ``Disadvantage``:

-   AchillesHeel
-   AdvantageFlaw
-   Age
-   BadLuck
-   BurnOut
-   CulturalUnfamiliarity
-   Debt
-   Devotion
-   Employed
-   Enemy
-   Hindrance
-   Infamy
-   LanguageProblems
-   LearningProblems
-   Poverty
-   Prejudice
-   Price
-   Quirk
-   ReducedAttribute

Outside the Fantasy rules, this additional disadvantage is added in the unpublished Magic rules.

-   MinorStigma


Here are the subclasses of ``Advantage``:

-   Authority
-   Contacts
-   Cultures
-   Equipment
-   Fame
-   Patron
-   Size
-   TrademarkSpecialization
-   Wealth

The Special Abilities include a class-level ``rank_cost`` value that's not simply set to one.
Each special ability has a distinct rank cost.

Here are the subclasses of ``SpecialAbility``:

-   AcceleratedHealing
-   Ambidextrous
-   AnimalControl
-   ArmorDefeatingAttack
-   AtmosphericTolerance
-   AttackResistance
-   AttributeScramble
-   Blur
-   CombatSense
-   Confusion
-   Darkness
-   Elasticity
-   Endurance
-   EnhancedSense
-   EnvironmentalResistance
-   ExtraBodyPart
-   ExtraSense
-   FastReactions
-   Fear
-   Flight
-   GliderWings
-   Hardiness
-   Hypermovement
-   Immortality
-   Immunity
-   IncreasedAttribute
-   InfravisionUltravision
-   Intangibility
-   Invisibility
-   IronWill
-   LifeDrain
-   Longevity
-   LuckGood
-   LuckGreat
-   MasterOfDisguise
-   MultipleAbilities
-   NaturalArmor
-   NaturalHandWeapon
-   NaturalMagick
-   NaturalRangedWeapon
-   Omnivorous
-   ParalyzingTouch
-   PossessionLimited
-   PossessionFull
-   QuickStudy
-   SenseOfDirection
-   Shapeshifting
-   Silence
-   SkillBonus
-   SkillMinimum
-   Teleportation
-   Transmutation
-   UncannyAptitude
-   Ventriloquism
-   WaterBreathing
-   YouthfulAppearance

Display and Output
==================

The output features of this module perform a number of output conversions for characters and creature definitions.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title character output

    class CharacterWriter {
        base_template: str
        list_template: str
        dict_template: str
        report(spell | book) -> str
    }

    class CharacterWriter_Short
    CharacterWriter <|-- CharacterWriter_Short

    class CharacterWriter_Long2
    CharacterWriter <|-- CharacterWriter_Long2

    class CharacterWriter_Table
    CharacterWriter <|-- CharacterWriter_Table

    class CharacterWriter_Literal
    CharacterWriter <|-- CharacterWriter_Literal

    class CharacterWriter_HTML
    CharacterWriter <|-- CharacterWriter_HTML

    class CharacterWriter_LaTeX
    CharacterWriter <|-- CharacterWriter_LaTeX


    class "detail(character | creature)" as detail << (F,orchid) Function >>
    hide detail empty members

    detail --> CharacterWriter

    class "sheet(character)" as sheet << (F,orchid) Function >>
    hide sheet empty members

    sheet --> CharacterWriter

    @enduml

Plus functions summary(), detail(), sheet()
And display(), debug()

Workbook Support
==================

This module has a few functions for extracting characters or creatures from a Jupyter Lab Notebook.
Generally, these functions are designed to be part of a notebook, and introspect the notebook by looking at the ``globals()`` mapping.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title character workbook

    class "workbook_characters(context)" as workbook_characters << (F,orchid) Function >>
    hide workbook_characters empty members


    class "display(character | book)" as display << (F,orchid) Function >>
    hide display empty members

    class "debug(character | book)" as debug << (F,orchid) Function >>
    hide debug empty members

    debug --> display

    @enduml


Application Wrapper
===========================

This module has a few functions to build elements of a spellbook application.
These functions serve to create a CLI application using the ``typer`` library.

Generally, these are used as follows:

..  code-block:: python

    from opend6_tools.character import *

    # Character or Creature definitions
    creatures = [...]

    if __name__ == "__main__":
        app = build_app(creatures)
        app()

This will -- when run from the command line -- build the application around spells (or items) defined in the module.
It will then launch the application.
This will parse command-line parameters and execute one various alternative sub-commands: ``test``, ``debug``, or ``display``.


Implementation
==============

..  automodule:: opend6_tools.character
