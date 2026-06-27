..  _`notes.opend6_challenges`:

##############################
  The Source Extraction Saga
##############################

The source material took a variety of forms.
We'll look at the overall workflow for capturing details from *OpenD6* source documents.
There are a variety of challenges to working with  TTRPG rules in general and the *OpenD6* rules in particular.
These include:

-   `Draft Documents`_.
-   `Design for Human Consumption`_.
-   `Colorful Prose`_.

Draft Documents
===============

The *OpenD6 Magic Guide* was never formally published; the available source document is a draft.
This means the spell difficulty computations are not completely trustworthy.
Indeed, a few of them make precious little sense.

Further, the OCR processing is extremely rough.
The document's text content is -- at best -- an approximation of the original.
Manual rework is required to create usable content from the sources.

For example, ``lOD+l`` is the OCR version of ``10D+1``. A great deal of patience is required to create something useful from some of the source documents.

Design for Human Consumption
============================

Generally, all of the *OpenD6* books are published for human consumption.
The display of a spell is helpful for a GM or player to understand the difficulty and the effects.
While this design helps players enjoy the game, it leads to ambiguities.

Creating automated tools is difficult when the baseline information is designed to present a lot of technical material in ways that aren't overpoweringly dull.
It helps the reader if the book introduces a subset of rules, followed by details, with examples scattered throughout.
Ideally, the subset is *not* contradicted by the details.
Further, there's no guarantee that all examples fully match the detailed rules.

It's difficult to be **sure** all of the cases stated in the rules are covered by a software implementation.
The examples, generally, serve as good test cases.
Except when the draft document seems to have errors.

Colorful Prose
==============

A great deal of the text is colorful and exciting.
It's not always clear or rigorous.

The most frustrating part is a few spells with poorly articulated effects.
For an example, see the *OpenD6 Fantasy Rules*, the "Open Lock" cantrip.

It's not at all clear what this effect really is.
The rules assign difficulty of 18.
But. How do we map this spell's effect to other rules?

-   One interpretation is the spell does (temporary) physical damage to the lock. This would be Alteration, not Apportation.

-   Another interpretation is the spell creates a new skill in lockpicking.
    This doesn't fit the description well, but, the effect is easy to define as a Skill Modifier of  +4D *lock picking*.
    This has a difficulty of :math:`4 \times 3 \times 1.5` which fits the difficulty perfectly. Except, this seems like it would  be Alteration not Apportation.

-   To focus on Apportation magic, perhaps the lock's internals are rearranged.
    Most apportation of an object weighing 1 kg or less is trivial. In this case, the spell difficulty would be under 5.
    This is nowhere near 18.

    Maybe there's some additional -- unstated -- difficulty doing some kind of "skilled apportation" of selected parts of the lock?
    There's no provision for this in the rules.

This makes it clear that in some cases, the effects were not carefully mapped against other parts of the rules.
Indeed, because some of the rules are a draft, the presence of errors seems likely.

The capture of source documents created draft versions of Spells, Characters, and Creatures based on the version 1 definitions.
These could then be tested -- to the extent possible -- to confirm the spell definition difficulties were reasonably close to correct.

This effort exposed a number of considerations that became non-functional requirements for the design of the OpenD6 tools.
