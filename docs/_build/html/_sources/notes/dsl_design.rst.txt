..  _`notes.dsl_design`:

#######################
  Notes on DSL Design
#######################

Table-Top Role-Playing Games (TTRPG's) like *OpenD6*
are examples of semi-structured data.
This means some software can be written to process it, but there is the possibility of ambiguity and complexity.

Outside TTRPG's, a great many documents are semi-structured.
Contracts are often semi-structured, and a "smart contract" seeks to impose more structure.
Information security policies often start as a semi-structured statements, derived from contracts, legislation, and even case law and consent decrees.
These, often need to be refined into a DSL that makes automated security checks on software and data.

One end of the structure spectrum is highly structured, schema-based data.
An external schema defines valid data, and automated validation checks are practical.
JSON Schema (https://json-schema.org) and XSD (https://www.w3.org/XML/Schema) are ways to describe structured data.

At the other end of the structure spectrum is unstructured data; examples include prose and poetry.
This kind of data cannot be validated.
It can be discussed and debated, but there's no sensible way to establish that it's "valid."

We've called the *OpenD6* TTRPG rules semi-structured because there are some constraints and some goals that are subject to validation.
In some cases, tests can be performed to make sure a statement in a game context is consistent with a set of rules.
There remain cases where it can be difficult to create a clear test case for consistency with the rules.

Further, this TTRPG game system lacks some details that could lead directly to automation of game play or validation of extensions to the rules.
The rules are often riddled with unstated assumptions (or expectations) about the nature of role-playing games and social interaction.
An extension to *OpenD6* may not conform to the rules because of a small misunderstanding of an obscure effect; or it might fail to integrate with the essential mechanics of play.

The idea of a DSL is to codify the rules so that an extension -- a new Spell, a new Creature, a new Item -- will be valid.
A well-designed DSL can help assure that other attributes -- specifically difficulty -- are computed correctly.

Before looking at the DSL for magical spells, it's important to look at the rules more broadly.
We can partition *OpenD6* play into two modes:

-   Combat mode is defined by rigorous and detailed rules.
    These are backed by structured data with a clear schema.
    A DSL can flow directly from the rules with little additional interpretation required.

-   Non-Combat mode involves rules with less rigor and detail.
    The rules are backed by semi-structured data, much of which is pure text.

Magic spans both modes.
Magic can be used in combat, and many spells have explicit combat effects, and integrate with other rules regarding weapons and armor.
Not all spells are so clearly defined; many other spells lack the clarity of combat mode.

The rigorous definition of combat mode can help as a starting point for understanding DSL's.
We can then turn to non-combat mode, the nature of magic, and the complications of a DSL to cover these less-rigorous aspects of play.

Rigor and Modes of Play
=======================

Before we can look at DSL complications, we need to look at some additional questions related to the combat mode of play:

-   What makes combat mode unique?

-   What is the schema that defines a DSL for combat?

The question of "What's at stake?" seems like it might be central.
In combat, the character's life is on the line.

The non-combat mode doesn't entirely avoid loss of a character's body points.
Starvation, dehydration, asphyxiation, disease, etc., are all non-combat situations that can damage a character.
Death is still possible outside combat.
For this reason, the loss of body points is not what makes combat distinct from non-combat.

A more useful central question appears to be "How well-defined are the actions?"
The rules for combat involve weapons and armor with narrowly-defined features.
The attack and defense moves are (in principle) well-understood.
Consider the various olympic sports (fencing, javelin, discus, shot-put, hammer toss, etc.) that evolved from combat into sport.
Fencing, in particular, involves both attack and defense.
The fencers have well-defined ways to use a foil, epée, and sabre.
The target lines lead to specific attack and defense techniques that help someone learn the sport.
This careful formalization around these weapons has reached a level where fencing attack areas have simple numeric designations: sixte, quarte, octave, and septieme.

The deep analysis of combat via sports like fencing leads to *OpenD6* combat rules with three essential mechanics:

-   Can the attacker hit the defender?
    There are two parts to making contact with a weapon.

    -   **Initiative**. The player and GM roll handfuls of dice based on their Acumen attributes and related skills to seize the initiative.

    -   **Accuracy**. The attacker rolls a handful of dice based on their Agility and related skills to overcome the any difficulties related to completing the attack.
        Skill dice and difficulty thresholds may be modified by weapon choice, defensive actions, and overall game context (i.e., visibility, clutter, etc.)

-   **Damage**. The attacker rolls a handful of dice based on Physique and the weapon being used to determine the magnitude of damage done.
    The net damage depends on Physique, weapon, armor, and any defensive actions.
    The outcome reduces a character's body; there may be additional complications like being disabled or being knocked unconscious.

The effect of weapon and armor choices are characterized by structured data (in tables) that lead to relatively simple handfuls of dice and numeric comparisons.
The tabular structure of these tables provides a schema that looks like the following illustration:

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

The weapons and armor are defined in detail by the rules.
The damage effect for manual weapons are enumerated.
The range difficulty offsets and damage effect for missiles are also detailed in the rules.
Creating a DSL for weapons and armor is straight-forward because the data model is complete an unambiguous.
A CSV-format table can contain the source data.
This can be restated in a variety of useful formats.

Creating a DSL for the combat aspects of characters is as trivial as creating a DSL to define weapons.
There are few complications.
The structure of the dice mechanics mean software tools to expand or clarify the rules is needless overhead.

This serves as a basis for understanding non-combat mode and the less complete definition of magical spells.

Non-Combat Mode
===============

Outside combat mode, the interactions are less rigorously defined than for combat.
They do, however, follow the combat pattern.
We'll detail this general play cycle to provide some context for DSL development.

Here is the general flow for all *OpenD6* interactions:

..  uml::

    @startuml
        'https://plantuml.com/sequence-diagram

    title OpenD6 Character Action Sequence

    actor player
    actor GM
    collections rules as "Rules"
    collections state as "Game State"

    player -> GM : State action and skill(s) used
    GM -> rules : Difficulties?
    rules -> GM : base threshold
    GM -> player : base difficulty threshold
    GM -> state : Extra Difficulties?
    state -> GM : extra difficulties
    opt optional
        player -> GM : Spend character or fate points for extra dice
    end
    player -> GM : Roll dice
    GM -> player : detail difficulties and outcome

    opt if needed
        player -> GM : Roll for magnitude of effect
    end

    GM -> state : Update game state

    @enduml

Here's how play evolves:

-   The player describes an **intended action**, specifying the character's skills that will be employed.

    -   The GM will disclose the obvious level of difficulty to the player.
        This is based on the rules, and doesn't involve too much controversy or clarification.

    -   The GM will know of additional difficulties based on game state or other information private to the GM, and may -- or may not -- disclose these.

-   The player may invest character points or fate points to boost the number of dice rolled to overcome the difficulties, both disclosed and undisclosed.
    There are other adjustments, including getting help, using better tools, taking more time that can improve the number of dice being rolled.

-   The roll for success is much like the roll to hit in combat.
    If the roll exceeds the difficulty threshold, the GM may disclose additional difficulties as part of describing the **actual outcome**.
    The outcome may or may not match the **intended action**.

-   The result may involve more dice-rolling to determine the magnitude of the effect.
    This parallels computing combat damage.

What's important here is non-combat actions also *fail* to parallel combat actions in one important way.
The changes to character state and game state are not limited to loss of body points.
An essential complication for non-combat mode is the open-ended nature of the outcome.

Some skills -- e.g., healing -- reverse combat damage, making them relatively simple to map to the rigorous combat-mode rules.
Other skills -- e.g., persuasion -- will modify the behavior of another character (often a non-player character).
These are adjacent to combat, but lack the simple clarity of a body point mechanic.

Beyond the normal effects of actions like persuading a character, there are the extra-normal effects of magic.
For the most part, the rules of the *OpenD6* system attempt describe extranormal effects using concrete effects that make well-defined changes to the game  state.
The few cases where this doesn't seem to be true seem to be editorial or play-testing problems.

Here's the suite of Effects deduced from a corpus of spells.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram
    'v3 of spell definitions

    title Overview of Effect classes

    class Spell {
        effect: Effect
    }

    class Aspect {
        + difficulty: int
        + description: str
    }

    Spell *-- "1,m" Aspect

    class Effect {
        skill() -> str
    }
    Aspect <|-- Effect

    abstract class MeasureEffect
    Effect <|-- MeasureEffect

    class DamageEffect
    MeasureEffect <|-- DamageEffect

    class ProtectionEffect
    MeasureEffect <|-- ProtectionEffect

    class SkillEffect
    MeasureEffect <|-- SkillEffect

    class AttributeEffect
    MeasureEffect <|-- AttributeEffect

    class SpecialAbilityEffect
    Effect <|-- SpecialAbilityEffect

    class DisadvantageEffect
    Effect <|-- DisadvantageEffect

    class TimeEffect
    MeasureEffect <|-- TimeEffect

    class DistanceEffect
    MeasureEffect <|-- DistanceEffect

    class MassEffect
    MeasureEffect <|-- MassEffect

    /'class VolumeEffect
    MeasureEffect <|-- VolumeEffect
    VolumeUnit <|--- VolumeEffect'/

    class CompositeEffect
    Effect <|-- CompositeEffect
    CompositeEffect *-- "2..n" Effect

    @enduml


While there are a lot of effects, they mostly fall into several categories.
Some of these map directly to the well-defined combat rules.
Others map to other well-define effects.
Here's a view of these effects:

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

Now that we've seen a little of how the *OpenD6* system works, we can turn to the design of a DSL that helps define spells and their difficulties.

DSL Syntax
===========

There are two general approaches to defining the syntax for a DSL:

-   Invent your own.  This requires writing a lexical scanner and parser.

-   Use an existing syntax.
    This has a number of alternatives.

    -   TOML (HUML, HCL, YAML, JSON, or even XML): an established, generic markup language.
        In this case, libraries are available for parsing.
        From the parsed input, more useful spell definition data structures can be built.

    -   Python. In this case, parsing can be ignored, since the DSL is code, parsed by the Python run-time.

While both work nicely, the Python version means the Spell definition **is** Python.
No additional processing to create a useful data structure from parsed input.

For some aspects of parsing source document PDF files, TOML can be useful.
It's helpful when searching for an understanding of spell design
Avoiding Python means the semantics of some spell constructs can be left flexible.
Flexibility can also lead to ambiguity.
Ambiguity is already part of parsing TTRPG rules written in a natural language like English.
Too much ambiguity is the problem we're trying to solve with a DSL.

For the long-term development of spells, and the publication of rules using spells, the Python syntax offers the advantage of simplicity.
It reduces the flexibility somewhat, helping to avoid ambiguity.

(It also saves us from defining parsers for strings and numbers; they're already part of Python.)

How do we move from a pile of TTRPG rules, including narrative text and spell examples, to a DSL?

Phased DSL Design
====================

Given a corpus of spells in legacy rule books, we want a DSL to represent spells, and help a GM create new spells.
The formal DSL statements have several goals:

-   The DSL makes it possible for software tools to do computations consistently.
    In *OpenD6*, the difficulty computation is onerous.
    The corpus of published spells helps validate the representation of rules in the DSL.
    (It may also uncover errors in the published corpus.)

-   Tools can present spell details in ways that can help a designer debug game design problems.
    For example, redesigning spells that are too difficult or not difficult enough.

-   Present the spell in a format suitable for for publication without manual transformation or copy-and-paste from one tool to another.
    Manually copying from a spread-sheet to a word-processor is error prone.
    Worse, it can be overlooked: the designer may tweak a spreadsheet and fail to copy and paste the revised spell into the campaign rules.

Unless the DSL designer is also a rule author, the DSL designer won't start the effort with a deep perspective of the problem domain.
The structured data is clear, but the semi-structured and unstructured data are difficult obstacles.
It's easy for a DSL designer to get overwhelmed with a detail, imposing needless complexities on other spells because of vague or incomplete rules.
It's also easy for a DSL designer to miss some obscure feature that may have a profound impact on the entire corpus of spells.
Finally, it's easy to provide a very general solution that doesn't actually fit with the conventions and expectations of potential users.

A workable strategy seems to be this:

1.  Create a minimal (version one) DSL to capture the initial base of knowledge.
    This may involve a lot of text, and few Python-specific features.
    This can be used to represent a corpus of spells, providing confirmation that the automated computations and presentations are useful.

    As noted in :ref:`notes.opend6_challenges`, there are a number of challenges
    to getting all of the source documents into a useful form.

2.  Refine the initial DSL to create version two, with a focus on completeness of the language and the associated tooling.
    This reflects a growing understanding of the problem domain.
    This should use more Python features and less text.
    The computations and publication processing should be refined and expanded.

3.  Refine the DSL to create version three, using as many Pythonic features as practical to create a reasonably fluent DSL.
    At this point, string processing left over from version one *could* be deprecated and replaced with pure Python.
    Or, the string processing could be left in place to ease migration of content to the newer version.

We'll start with the minimal DSL to capture the corpus of spells (or items, or creatures.)

Phase I -- Capture
==================

The initial phase of DSL design captures the spell definitions in a format useful to confirm the details have been parsed.
There are two goals:

-   To reproduce a version of the difficulty computation.
    Looking at the overall use cases, this is part of the **Change-Compute-Consider** cycle.
    It's not a complete solution, since the difficulties are parsed, not computed from details.

-   To emit a formatted representation for publication.

As an example, consider this spell description from the rules:

::

    CHARM
    -----
    Skill Used: Alteration
    Difficulty: 5
    Effect: 18 (charm skill bonus of +4D)
    Range: Self (0)
    Speed:0
    Duration: 1 minute (+9)
    Casting Time: 1 round (-4)
    Other Aspects:
    Gesture (-2): Smile and make a gesture of welcome or admiration
    Unreal Effect (-9): Difficulty to disbelieve is 13
    Other Conditions (-2): May only be used on humanoids who understand the caster's language and can hear the caster
    With a smile and a friendly gesture, the caster improves his charm
    skill by for one minute. (If he no charm skill, add the bonus to the
    character's Charisma attribute.) As this is an illusory spell, if the
    intended target of the charm disbelieves it, any effect the charm
    attempt had wears off immediately.

This minimal language can be Python ``dataclass`` definitions that  hold the parsed text.
There are a number of textual variations:

-   Effect has a difficulty and a description in ()'s.

-   The "core" aspects (range, speed, duration, casting, time) mostly have a description with the difficulty in ()'s. Except Speed.

-   The other aspects have a difficulty in ()'s, a :, and then the description.

-   Finally, a large blob of text has notes about the spell.

This is reasonably consistent throughout the rules. Regular expressions can be used to tease this apart.

Since the source documents include a published difficulty value for each individual aspect of a spell, this value can be included in the detailed spell aspects.
The spell definition -- as a whole -- is limited to doing the final summary calculation from the individual aspect difficulty values.
(Some errors will be found at this level.)
The computed results can be compared with the stated difficulty attribute of the spell.

Some of the rules for computing the detailed aspect difficulties are -- initially -- a bit mysterious.
The subsequent phase will seek to resolve those mysteries to make a more complete DSL.

There are a few variations in how parts of the spell are displayed.
This *should* be handled cleanly by using templates for the output.
These templates will expand and shift as more spells are represented.
Further, moving to version 2 of the DSL means the source data for the template will change.

What's important is to create a test suite with two parts:

1.  Unit test for the Python DSL components in isolation: Spell, Aspect, Effect, etc.

2.  An acceptance test suite based on the corpus of spells with their published difficulty values.

The first part assures that the DSL language elements work, and the difficulty computations work.
The second part assures the computations are reasonably consistent with the published rules.

Errors and problems in the published rules will be uncovered.
While *OpenD6* rounding rules are generally clear, it appears the rounding was not checked carefully during editing and play-testing.
This leads to some DSL computations that differ from published results by 1 difficulty point.
Other errors will lead to bigger errors in a few places.

Phase II -- Completeness
==========================

The first phase of spell definition wrapped a great deal of detail into data structures that are dependent on pre-computed values.
This fails to capture details that aren't initially visible as part of the final, published text.
There are several examples of places where details are elided:

-   Spell effects can be quite complicated.
    Some effects are composites, but the difficulty was summarized as a single value in the published summary.

-   Spell aspects have a number of unique attributes, and unique computations of difficulty.
    The Phase I data model relied on the difficulties shown in the text, and did not define the difficulty computations.

This is an important distinction:

-   Phase 1 had difficulties captured from source, provided as literal values.
    Any change required a manual computation of the aspect's new difficulty.
    Only the overall spell difficulty was computed.

-   Phase 2 will compute detailed aspect difficulties from the rules.

Additionally, there are some other changes required:

-   A "composite effect" definition is required to combine several individual effects.
    This is not a feature of the rules, but a technical necessity to capture rule details.

-   Some aspects are derived from the difficulties of other aspects (or the effect).
    These computations imply a dependency ordering among the aspects of a spell.

Additionally, the phase 1 definition omitted important distinctions between **measure**, **value**, and **modifier**:

-   A **measure** is given in physical units: kilograms, meters, seconds, etc.

-   A difficulty **value** is derived from a measure, :math:`v = \lceil 5 \times \log_{10}(m) \rceil`.

-   A **modifier** is difficulty value adjustment, applied after any measure-to-value conversion is done.

(Further, there are multiplicative **factors** that can apply to values and modifiers. Fortunately, these are rarely used.)

..  code-block:: python

    charm = Spell(
        name="Charm",
        skill="Alteration",
        notes=[
            "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
        ],
        effect=SkillEffect("charm skill", "+4D"),  # ❶
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),  # ❷
        other_aspects={
            "gesture": GesturesAspect(
                "Smile and make a gesture of welcome or admiration", "simple"
            ),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",),
                                                         "difficulty 13"),  # ❸
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,  # ❹
                description="May only be used on humanoids who understand the caster’s language and can hear the caster",
            ),
        ],
    )

Some important things to note:

-   The ❶ line shows two pieces of text which should be replaced with Python objects.
    The various skills should be enumerated. The dice expression should be ``4 * D``, not the string ``"+4D"``.

-   The ❷ and ❸ lines use the ``based_on()`` feature to define an aspect with a difficulty derived from another aspect.
    This feature means these aspects cannot be computed until other aspects have been computed.
    This complicates the overall definition of a Spell object.

-   The ❹ line shows how to handle those cases where the difficulty isn't derived from a measure or die code.

Phase II created a much richer set of class definitions.
It also meant an explicit migration from phase 1 definitions to phase 2 definitions.
Moving to Phase III is somewhat easier.

Phase III -- Fluency
===========================

There are two fluency changes noted above.

-   Changing strings to explicit enumerations.
    This will replace ``"charm skill"`` with something like ``CharismaSkill.charm``.

-   Changing strings to Die Expressions. This replaces ``"4D"`` with ``4*D`` to make an explicit computation that doesn't require string parsing.

This isn't mandatory; in some cases, the string version is easier for spell designers to use.
However, the use of enumerations creates a DSL where a static type checker can -- to an extent -- assure that
the various combinations of values are consistent with the rules.

What's important here is the incremental nature of the change.
A mixture of legacy strings can be used adjacent to newer, explicit enumerations.

Conclusion
============

Arriving at a collection of DSLs to represent spells, items, character, and creatures is an incremental process.
It's difficult to foresee all of the features present in the published content.

The more productive approach is to define a series of languages that capture the details and support tools that support the design process as well as publication.
