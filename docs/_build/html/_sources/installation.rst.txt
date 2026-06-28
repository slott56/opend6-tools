################################
  Installation and Quickstart
################################

Installation
============

The ``OpenD6_tools`` project is a library to help build OpenD6 characters.

If you are unfamiliar with `Python <https://python.org>`_ or the `Sphinx tools <https://www.sphinx-doc.org>`_, skip to the :ref:`tutorial` section.
We suggest following those more detailed instructions for installation.

If you are familiar with Python (and Sphinx), then you'll use **pip** or **uv** (or whatever) to install these tools.
There are some OS package dependencies: **make**, **pkg-config**, **cairo**, and **pdflatex**.

..  include:: ../README.rst
    :start-line: 30
    :end-line: 49

If necessary, start a project and create a virtual environment.
Using tools like **uv**, the following commands would be appropriate:

..  include:: ../README.rst
    :start-line: 58
    :end-line: 66

Activate the working virtual environment with a command similar to this:

..  code-block:: bash

    source .venv/bin/activate

Install the tools:

..  code-block:: bash

    % python -m pip install opend6_tools

Or:

..  code-block:: bash

    % uv add opend6_tools

Quick Start
===========

A collection of spell definitions, items, characters, or creatures can be written in a Python module or a Jupyter Lab Notebook.
The Python module can help with computations and can emit files in RST format suitable for publication.
A Jupyter Lab notebook is an easy-to-use interactive environment.
One of the OpenD6 tools can build a useful Python module from the notebook to support publication.

A spell-book module will be a file with the following pattern:

..  code-block:: python

    from opend6_tools.magic import *

    some_spell = Spell(name='Some Cool Name', ...)
    another_spell = Spell(name='Another Name', ...)
    ...

    spells = [some_spell, another_spell, ...]

    __test__ = {
        ...
    }

    if __name__ == "__main__":
        app = build_app(spells)
        app()

We expect this file to be named ``first_spell.py``.
What's important is to make sure the spell book module has a name
that's a valid Python symbol: letters, digits, and _'s, starting with a letter.
This means no spaces in the spell book module name.
The ``.py`` is the required suffix for a Python module.

The interesting parts of the definitions have been replaced with ``...``.

A module can have any number of spells. The Python variable names, ``some_spell``, ``another_spell`` are only visible within the module.
These are not the published names of the spell; the published names come from the
``name='...'`` attribute of the ``Spell`` definition.

It's entirely possible to use a structure like the following, also.

::

    spells = [
        Spell(...),
        Spell(...),
        ...
    ]

This avoids using Python variable names for the ``Spell`` objects.

The **OpenD6** rules require a number of characteristics for a spell.
Here's an example spell definition.

::

    charm = Spell(
        name="Charm",
        skill="Temperamental Alteration",
        notes=[
            "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
        ],
        effect=SkillEffect("charm skill", "+4D"),
        duration=DurationAspect(measure="1 minute"),
        range=RangeAspect(measure="self"),
        casting_time=CastingTimeAspect(measure="1 round"),
        speed=SpeedAspect.based_on(("range",), ""),
        other_aspects={
            "gesture": GesturesAspect(
                "Smile and make a gesture of welcome or admiration", "simple"
            ),
            "unreal_effect": UnrealEffectAspect.based_on(("effect",),
                                                         "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="May only be used on humanoids who understand the caster’s language and can hear the caster",
            ),
        ],
    )

This defines tne core characteristics of a spell.
For more about spell definitions, see the *OpenD6 Fantasy* rulebook.

The ``__test__ = {...}`` is helpful, but not required.
It allows you to define a difficulty budget for each spell, and then run a check to be sure the spell definitions meet their budget goals.

The module will be an application program with a command-line interface (CLI).
The ``app = build_app()`` creates this application, and the ``app()`` runs the app.

We'll assume the module was called ``first_spell.py``.
To run the module from the command line, use a command like this:

..  code-block:: bash

    python first_spell.py --help

The output will show all the available commands.
These commands include:

-   ``display`` to display the spell in a form suitable for publication with tools like **Sphinx**.

-   ``debug`` to display details about the spell to help correct problems.

-   ``test`` will use the ``__test__`` structure to run a test case to be sure the spell has a correct, consistent definition.

Here's how to get debugging output:

..  code-block:: bash

    python first_spell.py debug

Here's what the output looks like.
::

    ## Charm
      name                : 'Charm'
      notes               : ['With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately.']
      skill               : 'Temperamental Alteration'
      effect              : +12 SkillEffect('charm skill', '+4D')
      duration            :  +9 DurationAspect('1 minute')
      range               :  +0 RangeAspect('self')
      casting_time        :  -4 CastingTimeAspect('1 round')
      speed               :  +0 SpeedAspect.based_on('range', *('',), **{})
      other_aspects       :
      - gesture           :  -2 GesturesAspect('Smile and make a gesture of welcome or admiration', 'simple')
      - unreal_effect     :  -3 UnrealEffectAspect.based_on('effect', *('difficulty 13',), **{})
      other_conditions    :
      - May only be [...] :  +2 GenericAspect(-2, 'May only be used on humanoids who understand the caster’s language and can hear the caster')
    Effect Details        : SkillEffect based on DiceUnit [Modifier(difficulty=Decimal('12'), description='+4D')]
    Spell Total           : {'effect': 12, 'duration': 9, 'range': 0, 'speed': 0} = 21
    Negative Modifiers    : {'casting_time': 4, 'gesture': 2, 'unreal_effect': 3, 'condition: May only be used [...]': 2} = 11
    Difficulty            : ⎡(21 - 11) ÷ 2⎤ = 5

The last four lines provide details on how the overall difficulty was computed from the effect and the individual aspects.
This computation detail can be very helpful when designing new campaigns and worlds.
