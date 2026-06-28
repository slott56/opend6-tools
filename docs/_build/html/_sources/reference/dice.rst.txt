..  _`dice_module`:

############
  ``dice``
############

The :py:mod:`opend6_tools.dice` module is a small DSL for dice specifications.
This is shared by the :py:mod:`opend6_tools.magic` and :py:mod:`opend6_tools.character` modules.

A class definition implements operators to support
*n* ``*D`` and ``D+`` *n*, where *n* is a number.
It will also support more complex operations like ``3*D + 4*D + 2``.



..  uml::

    @startuml
    'https://plantuml.com/component-diagram

    title ""dice"" module

    class DieCode {
    __mul__(int) -> DiceCode
    __add__(int) -> DiceCode
    roll() -> Roll
    measure() -> int
    {static} from_pips() -> DieCode
    {static} parse_str() -> DieCode
    }

    object D

    D --> DieCode : "Instance of"

    class Roll {
        total: int
        success: bool
        fail: bool
    }

    DieCode ..> Roll : "Creates"

    class CriticalSuccess {
        rolls: int
        success = True
    }
    class CriticalFailure {
        fail = True
    }

    Roll <|-- CriticalSuccess : "Wild Die = 6"
    Roll <|-- CriticalFailure : "Wild Die = 1"

    @enduml

The global object ``D`` is the essential ingredient here.
It permits an expression like::

    DamageEffect("Attack", 3*D+2)


Additionally, this module also offers a command-line interface: an ``dice`` command.

::

    (opend6-tools) % dice --help

     Usage: dice [OPTIONS] [EXPR]

     Roll the handful of dice described by a dice expression. Use the --count
     option to roll multiple times.

     ? is a critical failure showing a total with the largest die value excluded, and, in ()'s, the total of all dice.

     ! is a critical success followed by the number of re-rolls.

    ╭─ Arguments ───────────────────────────────────────────────────────────────╮
    │   expr      [EXPR]  Dice expression, example: '2*D6+3' (quotes are        │
    │                     *required*)                                           │
    ╰───────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ─────────────────────────────────────────────────────────────────╮
    │ --count               -c      INTEGER  number of times to roll            │
    │                                        [default: 1]                       │
    │ --install-completion                   Install completion for the current │
    │                                        shell.                             │
    │ --show-completion                      Show completion for the current    │
    │                                        shell, to copy it or customize the │
    │                                        installation.                      │
    │ --help                                 Show this message and exit.        │
    ╰───────────────────────────────────────────────────────────────────────────╯


Implementation
==============

..  automodule:: opend6_tools.dice
