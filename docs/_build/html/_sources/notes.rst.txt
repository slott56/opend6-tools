..  _dsl_design:

#######################
  Notes on DSL Design
#######################

Table-Top Role-Playing Games (TTRPG's) like *OpenD6*
are examples of semi-structured data.
There is a spectrum of "structure" for data.
At one end of the structure spectrum is highly structured schema-based data.
For this, automated validation checks are practical.
JSON Schema and XSD are ways to describe structured data.

At the other end of the structure spectrum is unstructured data: prose and poetry.
This kind of data cannot be validated.
(One can argue -- at length -- over nuances.)

TTRPG rules are called semi-structured because there are some contraints and some goals subject to validation.
In some cases tests can be performed to make sure a statement in a game context is consistent with other rules.
In other case, however, it can be difficult to create a clear test case for consistency among statements.
While the rules often describe the general flow of a role-playing game, they rarely specify how play works in the kind of detail that permits automation; there are often numerous unstated assumptions about the nature of role-playing games.

As a general observation, the *OpenD6* rules seem to partition play into two modes:

-   Combat. This mode of play is defined by **Rigorous Rules**. These include structured data with a formal schema. A DSL flows directly from the rules with little additional interpretation required.

-   Non-Combat. This mode of play involves rules with less rigor than combat. The rules have semi-structured data without a clear schema.  This is where magic and invocations appear. The DSL isn't very clear.

Before looking at the DSL for magical spells, it's important to look at the rules more broadly.

The Combat mode involves those situations where characters are fighting and the outcome includes loss of body points.
When body points are reduced to zero, the character is dead.
In this mode of play, a great deal is at stake.

The non-combat mode involves use of skills and attributes distinct from those used in combat.
In some game scenarios, the non-combat situations serve to create a context where combat is inevitable because combat is how the story advances.
In other scenarios, however, combat may be incidental or avoidable, and the non-combat situations drive the story forward.

In order to better understand DSL, we need to look at
combat mode, and what makes it unique.
We can then turn to non-combat mode, magic, and the complications of a DSL.

Combat Mode
-----------

Before we can look at DSL complications, we need to look at two questions related to the combat mode of play:

-   What makes combat mode unique?

-   What is the schema that defines a DSL for combat?

The question of "What's at stake?" seems like it might be central.
In combat, the character's life is on the line.

The non-combat mode doesn't entirely avoid loss of a character's body points.
Starvation, dehydration, asphyxiation, disease, etc., are all non-combat situations that can damage a character.
Death is still possible, and perhaps even likely, in a scenario devoid of combat.
For this reason, the loss of body points is not what makes combat distinct from non-combat.

A more useful central question appears to be "How well-defined are the actions?"
The rules for combat involve weapons and armor with narrowly-defined features.
The attack and defense moves are (in principle) well-understood.
Consider the various olympic sports (fencing, javelin, discus, shot-put, etc.) that evolved from combat to sport.
Fencing, in particular, involves both attack and defense.
There are defined ways to use a foil or epée; with distinct ways to use a sabre.
The target lines lead to specific attack and defense techniques.
This careful formalization around these weapons has reached a level where fencing attack areas have simple numeric designations: sixte, quarte, octave, and septieme.

The deep analysis of combat via sports like fencing leads to TTRPG combat rules that involve three mechanics:

-   Can the attacker hit the defender?
    In the *OpenD6* rules, there are two parts to hitting.

    -   **Initiative**. The characters roll handfuls of dice based on their Acumen attribute and related skills.

    -   **Attack**. The attacher has a handful of dice based on their Agility and related skills. This may be modified by weapon choice, and any defensive actions.

-   **Damage**. What is the magnitude of the damage subtracted from the defender's body.
    The attacker rolls a handful of dice based on Physique and the weapon being used.
    The net damage depends on Physique, weapon, armor, and any defensive actions.
    The outcome reduces a character's body; there may be additional complications like being disabled or knocked unconscious.

The effect of weapon and armor choices are characterized by structured data (in tables) that lead to relatively simple handfuls of dice and numeric comparisons.
The tabular structure is the schema.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

    title Combat Mode Data Model

    class Character {
        agility: Attribute
        coordination: Attribute
        physique: Attribute
        intellect: Attribute
        acumen: Attribute
        charisma: Attribute
        body: int
        weapon: Weapon
        armor: Armor
        shield: Armor
        combat_damage(int)
    }

    class Attribute {
        base: D
        roll(): int
    }
    Character *-- Attribute

    class Skill {
        bonus: D
        roll(): int
    }
    Attribute *-- Skill

    class Weapon {
        damage: D
    }
    Character o-- Weapon

    class Missile_Thrown {
        short: int
        medium: int
        long: int
    }
    Weapon <|-- Missile_Thrown

    class Armor {
        damage resistance: D
    }
    Character o-- Armor

    @enduml

The values for attributes and skills are -- in effect -- purchased by the player to create the character in the *OpenD6* system.
There's a finite budget of dice that can be applied to create a character.

The weapons and armor are defined by the rules.
They are chosen from a menu of alternatives.
Weapons and amor have a price; a character has a probability of being able to meet the price.
The damage effect for manual weapons are enumerated.
The range difficulty offsets and damage effect for missiles are also   enumerated in the rules.

Creating a DSL for weapons and armor is straight-forward.
A CSV-format table contains the source data.
This can be restated in a variety of useful formats.

Creating a DSL for the combat aspects of characters is as trivial as a DSL for weapons.
There are few complications.

The rules are clear enough that formalization into software seems like a possibility.
Creating an application for combat -- generally -- isn't necessary.
The structure of the dice mechanics make the use of software more trouble than help.
Combat situations are fluid, and players make clever last-minute choices that a gamemaster must handle smoothly and equitably.


Non-Combat Mode
---------------

For non-combat play mode, the interactions are less rigorously defined than for combat.
They do, however, follow a similar pattern that expands on the combat pattern.

..  uml::

    @startuml
        'https://plantuml.com/sequence-diagram

    title Non-Combat Mode Sequence of Interactions

    actor player
    actor GM
    collections rules as "Rules"
    collections state as "Game State"

    player -> GM : intended action and skill(s) used
    GM -> rules : Difficulties?
    rules -> GM : base threshold
    GM -> player : disclose base difficulty threshold
    GM -> state : Extra Difficulties?
    state -> GM : extra difficulties
    opt optional
        player -> GM : spend character or fate points for extra dice
    end
    player -> GM : rolls dice
    GM -> player : disclose difficulties and result action

    opt if needed
        player -> GM : roll for magnitude of result
    end

    @enduml


-   The player describes an **intended action**, specifying the character's skills that will be employed.

    -   The GM will disclose the obvious level of difficulty to the player.

    -   The GM will know of additional difficulties based on game state or other information private to the GM, and may -- or may not -- disclose these.

-   The player may invest character points or fate points to boost the number of dice rolled to overcome the difficulties.
    There are other adjustments, including getting help, using better tools, taking more time that can improve the number of dice being rolled.

-   The roll for success is much like the roll to hit in combat.
    If the roll exceeds the difficulty threshold, the GM describes the **actual result**, which may or may not match the **intended action**.

-   The result may involve more dice-rolling to determine the magnitude of the effect.
    This parallels computing combat damage.
    However, it also *fails* to parallel combat damage, because the changes to character state and game state are not limited to loss of body points.

An essential complication for non-combat mode is the open-ended nature of the results.

Some skills -- e.g., healing -- reverse combat damage, making them relatively simple to map to the rigorous combat-mode rules.
Other skills -- e.g., persuasion -- will modify the behavior of another character (often a non-player character).

Beyond the normal effects of actions like persuading a character, there are the extra-normal effects of magic.
For the most part, the rules of the *OpenD6* system attempt to map extranormal effects to concrete effects that update the game state.

..  uml::

    @startuml
        'https://plantuml.com/class-diagram

        title Effect Class Diagram

        scale 750 width

        abstract class Unit
        Unit <|-- DieUnit
        Unit <|-- TimeUnit
        Unit <|-- DistUnit
        Unit <|-- MassUnit
        Unit <|-- VolumeUnit

        abstract class Effect
        'Aspect <|-- Effect'

        abstract class MeasureEffect
        Effect <|-- MeasureEffect
        MeasureEffect --- DieUnit

        class DamageEffect
        MeasureEffect <|-- DamageEffect
        DamageEffect --- DieUnit

        class ProtectionEffect
        MeasureEffect <|-- ProtectionEffect
        ProtectionEffect --- DieUnit

        class SkillEffect
        MeasureEffect <|-- SkillEffect
        SkillEffect --- DieUnit

        class AttributeEffect
        SkillEffect <|-- AttributeEffect

        class SpecialAbilityEffect
        Effect <|-- SpecialAbilityEffect

        class DisadvantageEffect
        Effect <|-- DisadvantageEffect

        class TimeEffect
        MeasureEffect <|-- TimeEffect
        TimeEffect -- TimeUnit

        class MassEffect
        MeasureEffect <|-- MassEffect
        MassEffect -- MassUnit

        class VolumeEffect
        MeasureEffect <|-- VolumeEffect
        VolumeEffect -- VolumeUnit

        class CompositeEffect {
            list[Effect]
        }
        CompositeEffect *-- Effect
        Effect <|-- CompositeEffect

    @enduml

While there are a lot of effects, they mostly fall into the following categories that map directly to the well-defined combat rules.

-   Combat-related:

    -   ``DamageEffect`` -- does Body damage

    -   ``ProtectionEffect`` -- reduces Body damage

-   Character-related:

    -   ``SkillEffect`` -- boosts or reduces a character's skill.

    -   ``AttributeEffect`` -- boosts or reduces an character's attribute and all skills related to that attribute.

    -   ``SpecialAbilityEffect`` -- adds or prevents use of a special ability.
        The rules define a number of special abilities; for the most part, these are extranormal.

    -   ``DisadvantageEffect`` -- adds or removes a disadvantage.
        The rules define a number of disadvantages; these, however, are open-ended.

There are other yet more magical effects; without the kind of clarity that combat mode provides.
These often have to do with divination or time travel or some other extranormal phenomenon.
In some cases, the effect is a limit on what a special ability can do.
These have generic names:

-   ``MassEffect``

-   ``TimeEffect``

-   ``DistanceEffect``

-   ``VolumeEffect``

Finally, there's a purely technical consideration: a ``CompositeEffect`` class.
This **can** be a simple ``list[Effect]`` structure, or it can be a more specialized container that includes ``Effect`` instances.

DSL Syntax
===========

There are two syntax approaches to a Domain-Specific Language (DSL.)

-   Invent your own.  This requires writing a lexical scanner and parser.

-   Use an existing syntax.
    This has a number of alternatives.

    -   TOML (or HUML, or HCL: an established, generic markup language)
        In this case, common libraries are available.

    -   Python. In this case, parsing can be ignored, since the DSL is code, parsed by the Python run-time.

While both work nicely, the Python version means the Spell definition **is** Python.
No additional processing is required to define a Spell or Character.
Using TOML means the spell definition must be ingested and transformed into Python objects for validation, testing, and publication.

For parsing documents and understanding the basics of spell design, TOML can be useful.
Avoiding Python means semantics of constructs can be left flexible as one comes to understand how the rules need to be implemented.

For the long-term development of spells, and the publication of rules using spells, the Python syntax is a bit simpler and more direct.
The flexible semantics become undesirable once a body of spells has been defined.
(It also saves us from defining parsers for strings and numbers; they're already part of Python.)


Two-Phase DSL Design
====================

Given a corpus of spells in legacy rule books, we want a DSL to represent spells, and help a GM create new spells.
The formal DSL statements have two goals:

-   Validate the difficulty computation. This aso validates the representation of rules in the DSL.

-   Present the spell in details to help debug representation issues.
    This also helps to debug game design problems.

-   Present the spell in a form suitable for for publication.

If the DSL representation captures **all** of the details, then the difficulty value will match the published difficulty.

The DSL for the *OpenD6* TTRPG rules has a mixture of combat and non-combat situations.

Further, a DSL designer won't have a proper perspective on the problem domain defined by semi-structured and unstructured data.
It's easy for the designer to get overwhelmed with one feature of one spell,  imposing needless complexities on other spells because of vague or incomplete rules.

A workable strategy seems to be this:

1. Create a minimal DSL to capture some initial base of knowledge.

2. Refine the initial DSL to create v2, improving the quality of the language as the understanding of the problem domain matures.

There are a few grammar and syntax issues that need to be addressed as part of creating a DSL.

Phase I -- Capture
==================

The initial Phase of DSL design captures the spell definitions in a format useful to confirm the details have been parsed well enough to do two things:

-   to reproduce a version of the difficulty computation.

-   to emit a formatted representation for publication.

This minimal language can be dataclass definitions that  hold some text.
Since the source documents include a published difficulty value, this can be simply parsed and included.
The rules for computing this, however, will be a bit mysterious, and require more work as part of creating subsequent versions of the DSL.

There are a few variations in how parts of the spell are displayed.
These *should* be handled cleanly by using templates for the output.

What's important is to create a unit test suite.
This assures that the DSL statements are valid, and the difficulty computations are complete and reasonably consistent with the published rules.

Errors and problems will be uncovered. The *OpenD6* rounding rules are generally clear. It appears they are not checked carefully during editing and play-testing, leading to DSL computations that differ from published results in inconsistent ways.

Phase II -- Expressiveness
==========================

The first phase of spell definition wrapped a great deal of detail into data structures that will (generally) prove to be too simple.
The initial structures often fail to capture details that aren't initially visible.
There are several examples of places where details are elided.

-   Spell effects can be quite complicated.
    Some effects are composites, but the difficulty was summarized as a single value in the published summary.

-   Spell aspects have a number of unique attributes, and unique computations of difficulty.
    Again, the Phase I data model relied on the difficulties shown in the text, and did not define the difficulty computations.

This is an important distinction, summarized as:

-   Phase 1 had difficulties captured from source, provided as literal values.

-   Phase 2 needs to compute difficulties from the rules.

Additionally, there are some other changes required:

-   A "composite effect" is required to combine several individual effects.
    This is not a feature of the rules, but a technical necessity to capture rule details.

-   Some aspects are derived from the difficulties of other aspects (or the effect).
    These computations imply a dependency ordering among the apects of a spell.

Additionally, the phase 1 definition omitted important relationships between **measure**, **value**, and **modifier**.
A **measure** is given in physical units: kilograms, meters, seconds, etc.
A difficuly **value** is derived from a measure, :math:`v = \lceil 5
\times \log_{10}(m) \rceil`.
A **modifier** is difficulty value adjustment, applied after any measure-to-value conversion is done.

(Further, there are multiplicative **factors** that can apply to values and modifiers. Fortunately, these are rarely used.)

This leads to a much richer (and more complicated) set of class definitions.
It also means there needs to be explicit migration from phase 1 definitions to phase 2 definitions.

Phase III -- Optimization
=========================

During the development of content using the phase 2 definitions, a large number
of fixed keywords with specific measures, values, or modification values were uncovered.
These started as strings.
They can be replaced with enumerations of strings, creating a strongly-typed data model.

As part of game design, more subtle issues of spell "template" were uncovered.
