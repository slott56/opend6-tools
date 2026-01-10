r"""
OpenD6 Spell Definition DSL.
Version 2.

Example
-------

    >>> from opend6_tools.magic2 import *
    >>> example = Spell(
    ...     name="Example",
    ...     notes="Mage waves their hands and says the words",
    ...     effect=SkillEffect("Acumen: testing", "+4D"),
    ...     duration=DurationAspect("1 sec"),
    ...     range=RangeAspect("1m"),
    ...     casting_time=CastingTimeAspect("5 sec"),
    ...     speed=SpeedAspect.based_on("range", description="Instantaneous"),
    ...     other_aspects = {},
    ...     other_conditions = [GenericAspect(1, "Everthing else is completed")],
    ... )
    >>> example.difficulty
    4
    >>> detail(example) # doctest: +NORMALIZE_WHITESPACE
    Example
    ~~~~~~~
    <BLANKLINE>
    :Skill: Acumen: testing
    :Difficulty: 4
    :Effect: 12 (Acumen: testing +4D)
    :Range: 1 m \(0)
    :Speed: Instantaneous \(0)
    :Duration: 1 sec \(0)
    :Casting Time: 5 sec \(4)
    <BLANKLINE>
    <BLANKLINE>
    :Other Conditions:
        (1): Everthing else is completed
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    Mage waves their hands and says the words
    <BLANKLINE>

Top-Level Components
----------------------

These are functions and classes that are helpful in a Jupyter Notebook.

..  autofunction:: display

..  autofunction:: debug

..  autofunction:: dumps

..  autofunction:: workbook_spells

..  autofunction:: workbook_rank

..  autofunction:: workbook_validation

Reporting and Display
---------------------

These are the conventional top-level application components.
The :py:func:`display` function produces the useful RST output.

..  autoclass:: TableSummary
    :members:

..  autoclass:: SpellWriter
    :members:

..  autofunction:: summary

..  autofunction:: detail


Spells (and Miracles)
-------------------------------

The essential definition of a Spell.

..  autoclass:: Spell
    :members:
    :member-order:  bysource

..  autoclass:: Miracle
    :members:

..  autoclass:: Cantrip
    :members:

..  autoclass:: OtherAspects
    :members:
    :undoc-members:

Aspects and Effects
-------------------

The base class for all aspects and effects.

..  autoclass:: Aspect
    :members:

Effects
~~~~~~~~~~~~

There are a number of effects, all derived from :py:class:`Effect`.

..  autoclass:: Effect
    :members:

..  autoclass:: CharactersticFactor
    :members:
    :undoc-members:

..  autoclass:: CharacteristicModifier
    :members:
    :undoc-members:

MeasureEffect
~~~~~~~~~~~~~

..  autoclass:: MeasureEffect
    :show-inheritance:
    :members:
    :undoc-members:

VolumeEffect
~~~~~~~~~~~~~

..  autoclass:: VolumeEffect
    :show-inheritance:
    :members:
    :undoc-members:

CompositeEffect
~~~~~~~~~~~~~~~

..  autoclass:: CompositeEffect
    :show-inheritance:
    :members:

DamageEffect
~~~~~~~~~~~~

..  autoclass:: DamageEffect

ProtectionEffect
~~~~~~~~~~~~~~~~

..  autoclass:: ProtectionEffect

SkillEffect
~~~~~~~~~~~

..  autoclass:: SkillEffect

AttributeEffect
~~~~~~~~~~~~~~~

..  autoclass:: AttributeEffect

SpecialAbilityEffect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: SpecialAbilityEffect

..  autoclass:: SpecialAbilityLookup

..  autoclass:: Enhancement
    :members:

..  autoclass:: Limitation
    :members:

DisadvantageEffect
~~~~~~~~~~~~~~~~~~

..  autoclass:: DisadvantageEffect

TimeEffect
~~~~~~~~~~~

..  autoclass:: TimeEffect

MassEffect
~~~~~~~~~~~

..  autoclass:: MassEffect

DistanceEffect
~~~~~~~~~~~~~~~

..  autoclass:: DistanceEffect

Aspects
---------

GenericAspect
~~~~~~~~~~~~~

..  autoclass:: GenericAspect
    :show-inheritance:

CompositeAspect
~~~~~~~~~~~~~~~

..  autoclass:: CompositeAspect
    :show-inheritance:
    :members:


RangeAspect
~~~~~~~~~~~

..  autoclass:: RangeAspect

SpeedAspect
~~~~~~~~~~~

..  autoclass:: SpeedAspect

DurationAspect
~~~~~~~~~~~~~~

..  autoclass:: DurationAspect

CastingTimeAspect
~~~~~~~~~~~~~~~~~

..  autoclass:: CastingTimeAspect

AreaEffectAspect
~~~~~~~~~~~~~~~~

..  autoclass:: AreaEffectAspect
..  autoclass:: AreaModifier
    :members:
    :undoc-members:

ChangeTargetAspect
~~~~~~~~~~~~~~~~~~

..  autoclass:: ChangeTargetAspect
..  autoclass:: TargetModifier
    :members:
    :undoc-members:

ChargesAspect
~~~~~~~~~~~~~~~~~~

..  autoclass:: ChargesAspect
..  autoclass:: ChargesUnit
    :members:
    :undoc-members:

CommunityAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: CommunityAspect

..  autoclass:: CommunityModifier
    :members:
    :undoc-members:

..  autoclass:: CommunityDifficulty
    :members:
    :undoc-members:

..  autoclass:: CommunityParticipationFactor
    :members:
    :undoc-members:

ComponentsAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: ComponentsAspect

..  autoclass:: ComponentsFactor
    :members:
    :undoc-members:

..  autoclass:: ComponentsModifier
    :members:
    :undoc-members:

ConcentrationAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: ConcentrationAspect

CountenanceAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: CountenanceAspect

..  autoclass:: CountenanceModifier
    :members:
    :undoc-members:

FeedbackAspect
~~~~~~~~~~~~~~~

..  autoclass:: FeedbackAspect

FocusedAspect
~~~~~~~~~~~~~~~~~~

..  autoclass:: FocusedAspect

GesturesAspect
~~~~~~~~~~~~~~~

..  autoclass:: GesturesAspect
..  autoclass:: GesturesModifier
    :members:
    :undoc-members:

IncantationsAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: IncantationsAspect
..  autoclass:: IncantationsModifier
    :members:
    :undoc-members:

MultipleTargetAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: MultipleTargetAspect
..  autoclass:: MultiTargetsModifier
    :members:
    :undoc-members:

UnrealEffectAspect
~~~~~~~~~~~~~~~~~~~

..  autoclass:: UnrealEffectAspect
..  autoclass:: UnrealFactor
    :members:
    :undoc-members:

VariableDurationAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: VariableDurationAspect
..  autoclass:: VariableDurationModifier
    :members:
    :undoc-members:

VariableEffectAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: VariableEffectAspect

VariableMovementAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: VariableMovementAspect
..  autoclass:: VariableMovementModifier
    :members:
    :undoc-members:

ArcaneKnowledgeAspect
~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: ArcaneKnowledgeAspect
    :members:

OtherAlterant
~~~~~~~~~~~~~

..  autoclass:: OtherAlterant

Supporting Classes
------------------

Foundational Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: Sign
    :members:
    :undoc-members:

..  autoclass:: DifficultyAdjustment

..  autoclass:: IncreasesDifficulty
    :show-inheritance:

..  autoclass:: DecreasesDifficulty
    :show-inheritance:

..  autoclass:: ParsedMeasure
    :members:

..  autoclass:: BaseLookup
    :members:
    :undoc-members:

..  autoclass:: Lookup
    :members:

..  autoclass:: AbilityLookup
    :members:

..  autoclass:: LimitationLookup
    :members:

..  autoclass:: Modifier
    :show-inheritance:
    :members:

..  autoclass:: Factor
    :show-inheritance:
    :members:

..  autoclass:: Unit
    :show-inheritance:
    :members:

..  autoclass:: VolumeUnit
    :show-inheritance:
    :members:

..  autoclass:: ChoiceStringMatch
    :members:

..  autoclass:: ChoiceStringPattern
    :members:

Part II: Measures, Modifiers, and Factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are implementations of specific sections of the rules.

..  autoclass:: DieCode
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: DieUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: TimeUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: DistUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: MassUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: TimeAspect
    :show-inheritance:

..  autoclass:: DistanceAspect
    :show-inheritance:

..  autofunction:: value_from_measure

Part III: Aspects and Effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some additional classes used to build spells.

..  autoclass:: DerivedAspect
    :show-inheritance:
    :members:
    :undoc-members:

"""

import abc
from collections import defaultdict
from dataclasses import dataclass, astuple
import decimal
import fnmatch
from abc import abstractmethod
from collections.abc import Iterator, Callable
from contextlib import redirect_stdout
import csv
from decimal import Decimal
from enum import Enum
from functools import singledispatchmethod
import graphlib
import io
import logging
import math
import re
import sys
from textwrap import dedent, shorten
from types import SimpleNamespace  # noqa: F401
from typing import (
    Annotated,
    Any,
    ClassVar,
    Literal,
    Match,
    Self,
    TextIO,
    TypedDict,
    cast,
)

import jinja2
from jinja2 import Environment

# import tomli  # Not currently used
import tomli_w  # WIP TOML dump
import typer
from humre import *  # noqa: F403  # type: ignore[import-untyped]

__all__ = [
    "D",
    "Spell",
    "Miracle",
    "Cantrip",
    "Effect",
    "AttributeEffect",
    "CompositeEffect",
    "DamageEffect",
    "DisadvantageEffect",
    "MassEffect",
    "DistanceEffect",
    "TimeEffect",
    "VolumeEffect",
    "ProtectionEffect",
    "SkillEffect",
    "SpecialAbilityLookup",
    "SpecialAbilityEffect",
    "LimitationLookup",
    "Limitation",
    "Enhancement",
    "ChoiceStringPattern",
    "ChoiceStringMatch",
    "Lookup",
    "Modifier",
    "Unit",
    "AreaModifier",
    "ChargesUnit",
    "CommunityDifficulty",
    "CommunityModifier",
    "CommunityParticipationFactor",
    "ComponentsFactor",
    "ComponentsModifier",
    "CountenanceModifier",
    "GesturesModifier",
    "IncantationsModifier",
    "MultiTargetsModifier",
    "TargetModifier",
    "UnrealFactor",
    "VolumeUnit",
    "VariableMovementModifier",
    "VariableDurationModifier",
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
    "GenericAspect",
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
    "CompositeAspect",
    # Rarely used
    "TimeUnit",
    "DistUnit",
    "MassUnit",
    # Workbook Tools
    "workbook_validation",
    "workbook_rank",
    "workbook_spells",
    "detail",
    "debug",
    "display",
    "dumps",
    # The main app
    "TableSummary",
    "build_app",
    "typer",
    "Annotated",
    "Any",
]

## Part I -- Foundational Definitions


class Sign(Enum):
    """
    An enumeration of the difficulty adjustments.

    The rules suggest partitioning effect and aspects
    based on their sign: increase or decrease.
    """

    Increase = +1
    Decrease = -1


class DifficultyAdjustment(abc.ABC):
    """Mixin to provide a :py:class:`Sign` enumeration value for each subclass of :py:class:`Aspect`.
    The value of this ``incr_decr`` value is used to partition :py:class:`Aspect` instances into two pools:
    "modifiers" and "negative modifiers".

    Yes, this is a mixin to provide an attribute value.

    All but one of core :py:class:`Aspect` subclasses increase difficulty.
    The :py:class:`CastingTimeAspect` decreases difficulty.
    """

    incr_decr: Sign


class IncreasesDifficulty(DifficultyAdjustment):
    incr_decr = Sign.Increase


class DecreasesDifficulty(DifficultyAdjustment):
    incr_decr = Sign.Decrease


# Conversions for complex parsing of units with multiple numbers.
MeasureFunc = Callable[[Match], Decimal]
CleanFunc = Callable[[Match], str]


# There are Several varieties of ParsedMeasure
# - Simple units with :py:func:`value_from_measure()`.
# - Simple units with other value conversions, used for modifiers and factors.
# - Unit patterns with :py:func:`value_from_measure()`.
# - Unit patterns with other value conversions, used for modifiers and factors


@dataclass
class ParsedMeasure:  # (abc.ABC):
    """Parsed measure extracted from strings or parameters.

    :clean:
        The cleaned string for the units in canonical form.

    :supplied_value:
        Either the parsed measure or None if no value was provided.

    :scale_factor:
        A scale factor to get to base KMS units.
        None means there's no scaling required.

    There are two ways to create instances:

    -   "Manually": ``ParsedMeasure("2 kg", Decimal('2'), Decimal(1)``.

    -   Using the class-level :py:meth:`parse_str` method: ``ParsedMeasure.parse_str("2 kilograms")``

    ..  TODO:: Refactor.

        -   Needs ``value()`` plug-in **Strategy** to transform supplied_value to value.

        -   Needs ``choices`` list of units (or list of patterns) and conversion functions.

        Choices for :py:meth:`value` include do nothing, :py:func`value_from_measure`,
        ``values_from_measure() + 1``, and ``2 * (value_from_measure()+1) - 2``.

    """

    clean: str
    supplied_value: Decimal | None
    scale: Decimal | None = None

    @classmethod
    # @abc.abstractmethod
    def parse_str(cls, measure: str) -> "ParsedMeasure": ...

    @classmethod
    # @abc.abstractmethod
    def value(cls, value: Decimal) -> Decimal: ...

    @property
    def value_clean(self) -> tuple[Decimal, str]:
        """Convert parsed value to string and value.

        ..  todo:: Needs value() mix-in **Strategy**.
        """
        if self.supplied_value and self.scale is not None:
            # How many decimal places?
            _, _, exponent = (
                self.supplied_value - self.supplied_value.to_integral_value()
            ).as_tuple()
            # Fiddle "- exponent" -- the number of decimal places -- into format.
            canonical = f"{self.supplied_value / self.scale:.{abs(cast(int, exponent))}f}{' ' if self.clean else ''}{self.clean}"
            return self.value(self.supplied_value), canonical
        elif self.supplied_value and self.scale is None:
            # Complex areas don't have a simple scale
            return self.value(self.supplied_value), self.clean
        else:
            # Special case for modifiers with no units
            return self.value(self.scale or Decimal(1)), self.clean


class ChoiceStringMatch:
    """
    Mixin to parse a "digits words" unit-of-measure value where units match the defined units.
    This is  the most common case, where the units are Kilogram-Meter-Second unit names.

    The :meth:`parse` method returns a tuple('units', value, scale factor)

    >>> from dataclasses import astuple
    >>> from opend6_tools.magic2 import *
    >>> csm = ChoiceStringMatch()
    >>> csm.choices = {"kilograms": 1}
    >>> astuple(csm.parse_str("1,000 kilograms"))
    ('kilograms', Decimal('1000'), Decimal('1'))
    >>> astuple(csm.parse_str("kilograms"))
    ('kilograms', None, Decimal('1'))
    """

    choices: dict[str, Decimal | tuple[MeasureFunc, CleanFunc]]  #: Must be part of base class
    unit_pat = (
        optional(WHITESPACE)
        + optional_group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS, ",")))  # +|- Number
        + optional(WHITESPACE)
        + group(zero_or_more(nonchars("(")))  # The text from choice.
        + optional_group(zero_or_more(nonchars(")")))  # Notes in ()'s.
    )

    def parse_str(self, measure: str) -> ParsedMeasure:
        """Parse measure text: "digits words (notes)".

        :param measure: the measure text to parse.
        :return: ParseMeasure(canonical unit, supplied value, scale factor)
        """
        clean: str
        base_measure: Decimal | None
        scale: Decimal | None
        if match := re.match(self.unit_pat, measure):
            if match.group(1) and match.group(2):
                # Number and Unit Name.
                clean = match.group(2).strip().lower()
                try:
                    match self.choices[clean]:
                        case Decimal() | int() as number:
                            scale = Decimal(number)
                        case _:
                            raise ValueError(f"error with {clean=!r}, {self.choices[clean]=!r}")
                    # scale = Decimal(self.choices[clean])
                except KeyError:
                    raise ValueError(f"invalid units {clean!r}")
                base_measure = scale * Decimal(match.group(1).replace(",", ""))
            elif match.group(1):
                # Number Only
                # Pick first of available units as default
                base_unit = cast(str, list(self.choices.keys())[0])
                clean = base_unit
                scale = Decimal(1)
                base_measure = Decimal(match.group(1).replace(",", ""))
            else:
                # No number, only a unit word.
                # value is implicitly 1.
                assert match.group(2)
                clean = match.group(2).strip().lower()
                try:
                    match self.choices[clean]:
                        case Decimal() | int() as number:
                            scale = Decimal(number)
                        case _:
                            raise ValueError
                    # scale = Decimal(self.choices[clean])
                except KeyError:
                    raise ValueError(
                        f"invalid units {clean!r}, not found in {list(self.choices.keys())}"
                    )
                base_measure = None

            if match.group(3):
                # Notes?
                clean = f"{clean} ({match.group(3)[1:]})"
            return ParsedMeasure(clean, base_measure, scale)
        else:
            raise ValueError(f"invalid {measure=!r}")


class ChoiceStringPattern:
    """Mixin to parse using arbitrary value patterns and apply more complicated conversion functions.
    This is  the most general case, where patterns are multi-dimensional.

    The :meth:`parse_str` method returns a tuple (tuple of match groups from the pattern, parsed value. None)

    The ``choices`` attribute is a mapping from a pattern to a pair of tuples to compute the value and the canonical text.
    The alternative type of float isn't used; it's for a distinct parsing mixin.

    >>> from dataclasses import astuple
    >>> from decimal import Decimal
    >>> from opend6_tools.magic2 import *

    >>> csp = ChoiceStringPattern()
    >>> csp.choices = {r"(\\d+) words": (lambda m: Decimal(m.group(1)), lambda m: repr(m.groups()))}
    >>> astuple(csp.parse_str("42 words"))
    ("('42',)", Decimal('42'), None)
    """

    choices: dict[str, Decimal | tuple[MeasureFunc, CleanFunc]]  #: Must be part of base class

    def parse_str(self, measure: str) -> ParsedMeasure:
        """Parse choice text.

        :param measure: the text to parse
        :return: ParseMeasure(canonical unit, supplied value, scale factor)
        """
        for pattern in self.choices:
            if match := re.search(pattern, measure):
                match self.choices[pattern]:
                    case Decimal() as base_measure:
                        return ParsedMeasure(match.group(), base_measure)
                    case tuple() as func_pair:
                        measure_func, clean_func = func_pair
                        # **must** normalize this to meters; a single scale doesn't make sense.
                        base_measure = measure_func(match)
                        clean = clean_func(match)
                        return ParsedMeasure(clean, base_measure)
        raise ValueError(f"could not parse {measure!r}")


class BaseLookup(abc.ABC):
    """Abstract base class for Lookup, Modifier, Factor, etc."""

    choices: dict[str, Decimal | tuple[MeasureFunc, CleanFunc]]  #: Must be part of base class

    @abstractmethod
    def parse(
        self, measure: str | float | int, unit: str | None = None
    ) -> tuple[Decimal | None, str]: ...


class Lookup(ChoiceStringMatch, BaseLookup):
    """
    Parse a string value with a name that maps to a value.
    There are three subclasses:

    - Factor -- multiplicative factors, applied to difficulty modifiers.

    - Modifier -- difficulty modifiers.

    - Unit -- also called "Measure" where the measure maps to a value.
        The value is the difficulty.

    Full syntax is ``[number] unit ["(" text ")"]``.

    For a unit, the number is required. Examples: ``2m``, ``3 sec``, ``5 kg``.
    The leading number is a signed Decimal value.
    Factors and modifier don't have a leading number, only the unit.
    The ``(text)`` is often some supplemental information often providing
    details of additional skill rolls required.

    For more general lookup of Factors and Modifiers,
    the number can be omitted, and 1 is the default.

    Examples:

    >>> from decimal import Decimal
    >>> from opend6_tools.magic2 import *
    >>> class ExampleLookup(Lookup):
    ...     choices = {
    ...     "example": 1,
    ...     "doubled": 2,
    ...     "modifier": Decimal("0.75"),
    ...     "improved modifier": Decimal("1.50"),
    ...     }
    >>> ExampleLookup().parse("1 Example")
    (Decimal('1'), '1 example')
    >>> ExampleLookup().parse("2 modifier")
    (Decimal('1.50'), '2.00 modifier')
    >>> ExampleLookup().parse("-3 example")
    (Decimal('-3'), '-3 example')
    >>> ExampleLookup().parse(4, "doubled")
    (Decimal('8'), '4 doubled')
    >>> ExampleLookup().parse("5 improved modifier")
    (Decimal('7.50'), '5.00 improved modifier')

    Subclases :py:class:`Factor` and :py:class:`Modifier`
    will have a :py:meth:`value` implementation that passes
    looked-up value through, untouched.

    The :py:class:`Unit` subclass has a :py:meth:`value` implementation that
    conversion from measure to value..
    Unit subclasses introduce commonly-used units: DieCodes, distance, time, mass.

    ..  todo:: Refactor to use @classmethod -- there's no need for an instance.
    """

    def value(self, measure: Decimal) -> Decimal:
        """Lookup does no translation.
        One subclass (i.e. :py:class:`Unit`) does a transformation.

        :param measure: the measure
        :returns: the measure.
        """
        return measure

    def parse(self, measure: str | float | int, unit: str | None = None) -> tuple[Decimal, str]:
        """
        Parses measure of string "2sec", as well as parameters (measure, unit) of (2, 'sec').
        Creates a tuple of (value, canonical string).

        ..  todo:: This is really an overloaded definition.

            parse(str)
            parse(float | int, str)
            parse(DieCode)

        :param measure: The measure to parse
        :param unit: the units, in those cases where it's not one big string
        :returns: tuple of parsed measure and unit string.
        """
        # First unit name in ``units`` is assumed to have a value of 1.
        # When unit is omitted, this unit is assumed.
        base_unit = list(self.choices.keys())[0]

        # Find the measure supplied and the scale (from the unit)
        match measure:
            case str():
                # Text with number and unit (and maybe even extra details.)
                parsed = self.parse_str(measure)
            case float() | int():
                # Number with unit as second positional parameter
                if unit:
                    # What about unit (details)?
                    if (clean := unit.strip().lower()) in self.choices:
                        match self.choices[clean]:
                            case Decimal() | int() as number:
                                scale = Decimal(number)
                                base_measure = scale * Decimal(measure)
                                parsed = ParsedMeasure(clean, base_measure, scale)
                            case _:
                                raise ValueError(f"invalid {measure=!r}, {unit!r}")
                    else:
                        raise ValueError(f"invalid {measure=!r}, {unit!r}")
                else:
                    parsed = ParsedMeasure(base_unit, Decimal(measure), Decimal(1))
            case _:
                raise ValueError(f"invalid {measure=!r}")

        # return parsed.value_clean()
        clean, base_measure, scale = astuple(parsed)
        if base_measure and scale is not None:
            # How many decimal places?
            _, _, exponent = (base_measure - base_measure.to_integral_value()).as_tuple()
            # Fiddle "- exponent" -- the number of decimal places -- into format.
            canonical = (
                f"{base_measure / scale:.{abs(cast(int, exponent))}f}{' ' if clean else ''}{clean}"
            )
            return self.value(base_measure), canonical
        elif base_measure and scale is None:
            # Complex areas don't have a simple scale
            return self.value(base_measure), clean
        else:
            # Special case for modifiers with no units
            return self.value(scale), clean


class Modifier(Lookup):
    """
    A difficulty modifier.

    A lookup without a measure-to-value transformation.

    As a degenerate case, an Aspect can
    provide a difficutly modifier without an supplemental unit information.

    >>> from opend6_tools.magic2 import *
    >>> Modifier().parse("3")
    (Decimal('3'), '3')
    """

    choices = {"": Decimal(1)}

    def value(self, measure: Decimal) -> Decimal:
        """Modifier does no translation from measure to value.
        The values are direct difficulty values.

        :param measure: the measure provided in the Aspect or Effect.
        :returns: the measure.
        """
        return measure


class Factor(Lookup):
    """
    A difficulty factor (a multiplier; not an adder).
    Like a unit, but, without a measure-to-value transformation.
    """

    pass


def value_from_measure(measure: Decimal) -> Decimal:
    r"""
    The core conversion of a Measure, :math:`m`, to Difficulty Value, :math:`v`.

    See the *OpenD6 Fantasy Rulebook*, "Magic" chapter.
    This is the *Spell Measures* table.

    For measures from 1 to 5, the mapping is slightly different than all others.
    [1, 1.5, 2.5, 3.5, 5] map to [0, 1, 2, 3, 4].
    Everything else follows s [1, 1.5, 2, 2.5, 4, 6] pattern.

    ..  math::

        v = \begin{cases}
         &\lceil 5 \log_{10}(m) \rceil_{u} \textbf{ if $m < 10$}\\
         &\lceil 5 \log_{10}(m) \rceil \textbf{ if $m \geq 10$}
        \end{cases}

    Where :math:`\rceil_{u}` uses ``decimal.ROUND_UP``, and :math:`\rceil` uses ``decimal.ROUND_HALF_UP``.

    Two alternate interpretations for the cutoff. :math:`m \leq 5` or :math:`m < 10`.
    Both fit the available data.

    The rules are ambiguous.

        If the desired amount is greater than one number but less than
        another, either lower your amount or select the bigger number.

    :param measure: in one of the base units: seconds, kilograms, meters, liters.
    :return: value for the given measure.
    """
    try:
        if measure < 10:
            # value = int(5 * math.log(measure, 10) + .51)
            value = (Decimal("5.0") * measure.log10()).quantize(
                Decimal(1), rounding=decimal.ROUND_UP
            )
        else:  # measure >= 10:
            # value = int(round(5 * math.log(measure, 10)))
            value = (Decimal("5.0") * measure.log10()).quantize(
                Decimal(1), rounding=decimal.ROUND_HALF_UP
            )
        return value
    except (ValueError, decimal.InvalidOperation):
        raise ValueError(f"invalid measure, {measure} <= 0")


class Unit(Lookup):
    """
    Parse a string value with measure and unit name into value and a canonical string.

    Base cases: ``2m``, ``3 sec``, ``5 kg`` kinds of strings.

    This works with signed :py:class:`Decimal` values.
    The rules are generally focused on integers, but, any value can be used.

    Examples:

    >>> from typing import ClassVar
    >>> from opend6_tools.magic2 import *
    >>> class ExampleUnit(Unit):
    ...     choices: ClassVar[dict[str, float]] = {
    ...         "example": 1,
    ...         "doubled": 2,
    ...         "megaexample": (1024*1024)
    ...     }
    >>> ExampleUnit().parse("1 Example")
    (Decimal('0'), '1 example')
    >>> ExampleUnit().parse("2 megaexample")
    (Decimal('32'), '2 megaexample')
    >>> ExampleUnit().parse("-3 example")
    Traceback (most recent call last):
    ...
    ValueError: invalid measure, -3 <= 0
    >>> ExampleUnit().parse(4, "megaexample")
    (Decimal('33'), '4 megaexample')
    >>> ExampleUnit().parse("5.5 doubled")
    (Decimal('5'), '5.5 doubled')

    Subclasses introduce specific units: DieCodes, distance, time, mass.
    Note that **Modifiers** lack the ``value()`` computation.
    These have more elaborate modifiers with direct effects on difficulty.

    ..  todo:: Rename to ``Measure``.
    """

    # choices: ClassVar[dict[str, Decimal]]

    def value(self, measure: Decimal) -> Decimal:
        """
        Converts measure to a difficulty value.
        Uses :py:func:`value_from_measure`.

        :param measure: The measure
        :returns: The difficulty value for the given measure.
        """
        return value_from_measure(measure)


## Part II -- Units: Mass, Distance, and Time


class DieCode:
    """
    Can be used instead of text for Dice.

    >>> from opend6_tools.magic2 import DieCode
    >>> D = DieCode()
    >>> r = 3*D+2
    >>> r.measure
    Decimal('11')
    """

    def __init__(self, n: int = 1, adj: int = 0, faces: int = 6) -> None:
        self.n = n
        self.adj = adj
        self.faces = faces  # Open D6, faces **should** be 6.

    def __repr__(self) -> str:
        return f"{int(self.n):+d}D+{self.adj}" if self.adj else f"{int(self.n):+d}D"

    def __mul__(self, other: Any) -> "DieCode":
        match other:
            case int() | Decimal():
                return DieCode(int(self.n * other), self.adj, self.faces)
            case _:
                pass
        return NotImplemented

    __rmul__ = __mul__

    def __add__(self, other: Any) -> "DieCode":
        match other:
            case int() | Decimal():
                dice, pips = divmod(self.adj + other, 3)
                return DieCode(int(self.n + dice), int(pips), self.faces)
            case _:
                pass
        return NotImplemented

    __radd__ = __add__

    @property
    def measure(self) -> Decimal:
        return Decimal(self.n * 3 + self.adj)


D = DieCode(faces=6)


class DieUnit(Unit):
    """
    Parse Dice-roll DSL, ``[+|-]?nD[+a|-a]?``, and transform to value and canonical string.

    >>> from opend6_tools.magic2 import DieCode, DieUnit
    >>> D = DieCode()

    # Preferred styles

    >>> DieUnit().parse(2*D)
    (Decimal('6'), '+2D')
    >>> DieUnit().parse(2*D+1)
    (Decimal('7'), '+2D+1')
    >>> DieUnit().parse(-2)  # D is assumed; no pip values.
    (Decimal('-6'), '-2D')

    # Text Conversion

    >>> DieUnit().parse("+3D")
    (Decimal('9'), '+3D')
    >>> DieUnit().parse("3D+2")
    (Decimal('11'), '+3D+2')
    >>> DieUnit().parse("-2D")
    (Decimal('-6'), '-2D')
    >>> DieUnit().parse("+3")
    (Decimal('3'), '+1D')

    """

    def parse(
        self, measure: int | str | float | DieCode, unit: str | None = None, *, pips: int = 0
    ) -> tuple[Decimal, str]:
        """Parse Dice-Roll string. Or ``d`` and ``pips`` as two int argument values.

        :param measure: Either a dice string, ``"3D+2"``, a :py:class:`DieCode`` object, or a number of dice.
        :param unit: Not used -- included for type compatibility with the parent class.
        :param pips: If measure is an integer, pips can be provided a san integer, also.
        """
        match measure:
            case DieCode():
                die = measure
            case int():
                die = Decimal(measure) * D + pips
            case str() as text:
                # TODO: Refactor into DieCode classmethod.
                # TODO: Reify with character.DieCode
                # The pattern is an "either" with three choices  [+-]nD+n | [+-]nD | +n
                # The current ([+-]nD)?(+n)? with everything optional is a bad plan.
                pattern = (
                    zero_or_more(WHITESPACE)
                    + optional(
                        noncap_group(
                            group(
                                optional(chars(PLUS, MINUS)),
                                zero_or_more(WHITESPACE),
                                one_or_more(DIGIT),
                            ),
                            zero_or_more(WHITESPACE),
                            "D",
                            zero_or_more(WHITESPACE),
                        )
                    )
                    + optional_group(
                        optional(chars(PLUS)),
                        zero_or_more(WHITESPACE),
                        group(one_or_more(DIGIT)),
                    )
                )
                if match := re.match(pattern, text):
                    if match.group(1) is None:
                        n = 0
                    else:
                        n = int(match.group(1))
                    if match.group(2) is None:
                        pips = 0
                    else:
                        pips = int(match.group(2))
                    die = n * D + pips
                else:
                    raise ValueError(f"invalid dice expression {text!r}")
            case _:
                raise ValueError(f"invalid type {measure!r}")
        if die.measure == 0:
            # Since both parts of the text format are optional... this can happen.
            raise ValueError(f"invalid dice expression {measure!r}")
        return die.measure, repr(die)


class TimeUnit(Unit):
    """
    Parse times. This includes conversions from seconds
    to other units.

    Months don't have a fixed number of seconds.
    The Julian Year length divided by 12 provides a simple average month of 30.4375 days.

    >>> from opend6_tools.magic2 import *
    >>> TimeUnit().parse("1r")
    (Decimal('4'), '1 r')
    """

    choices = {
        "instant": Decimal(1),  # Special case for <=1s
        "instantaneous": Decimal(1),  # Special case for <=1s
        "sec": Decimal(1),
        "s": Decimal(1),
        "second": Decimal(1),
        "seconds": Decimal(1),
        "r": Decimal(5),
        "round": Decimal(5),
        "rounds": Decimal(5),
        "m": Decimal(60),
        "min": Decimal(60),
        "minute": Decimal(60),
        "minutes": Decimal(60),
        "h": Decimal(60) * 60,
        "hr": Decimal(60) * 60,
        "hrs": Decimal(60) * 60,
        "hour": Decimal(60) * 60,
        "hours": Decimal(60) * 60,
        "d": Decimal(60) * 60 * 24,
        "day": Decimal(60) * 60 * 24,
        "days": Decimal(60) * 60 * 24,
        "w": Decimal(60) * 60 * 24 * 7,
        "wk": Decimal(60) * 60 * 24 * 7,
        "week": Decimal(60) * 60 * 24 * 7,
        "weeks": Decimal(60) * 60 * 24 * 7,
        "mon": Decimal(60) * 60 * 24 * Decimal("30.4375"),  # Julian year, it's simpler.
        "month": Decimal(60) * 60 * 24 * Decimal("30.4375"),
        "months": Decimal(60) * 60 * 24 * Decimal("30.4375"),
        "y": Decimal(60) * 60 * 24 * Decimal("365.25"),
        "yr": Decimal(60) * 60 * 24 * Decimal("365.25"),
        "year": Decimal(60) * 60 * 24 * Decimal("365.25"),
        "years": Decimal(60) * 60 * 24 * Decimal("365.25"),
        "c": Decimal(60) * 60 * 24 * 36525,
        "century": Decimal(60) * 60 * 24 * 36525,
        "centuries": Decimal(60) * 60 * 24 * 36525,
    }


class MassUnit(Unit):
    """
    Parse masses.

    >>> from opend6_tools.magic2 import *
    >>> MassUnit().parse("1 ton")
    (Decimal('15'), '1 ton')
    """

    choices = {
        "kg": Decimal(1),
        "kilogram": Decimal(1),
        "kilograms": Decimal(1),
        "mg": Decimal(1000),
        "t": Decimal(1000),
        "ton": Decimal(1000),
        "metric ton": Decimal(1000),
        "gg": Decimal(1_000_000),  # giga-gram, Gg
        "kt": Decimal(1_000_000),
        "kiloton": Decimal(1_000_000),
        "pg": Decimal(1_000_000_000),  # peta-gram, Pg
        "mt": Decimal(1_000_000_000),
        "megaton": Decimal(1_000_000_000),
    }
    pass


class DistUnit(Unit):
    """
    Parse distances.

    Also. Speeds which are distance "per second"

    >>> from opend6_tools.magic2 import *
    >>> DistUnit().parse("2 km")
    (Decimal('17'), '2 km')
    """

    choices = {
        "self": Decimal(1),  # Special case for <1m.
        "touch": Decimal(1),  # Special case for <1m.
        "m": Decimal(1),
        "m per second": Decimal(1),
        "meter": Decimal(1),
        "meters": Decimal(1),
        "km": Decimal(1_000),
        "kilometer": Decimal(1_000),
        "kilometers": Decimal(1_000),
        "mm": Decimal(1_000_000),  # Mm is the actual unit
    }


class VolumeUnit(Unit):
    """
    Parse volumes.

    >>> from opend6_tools.magic2 import *
    >>> VolumeUnit().parse("100 liters")
    (Decimal('10'), '100 liters')
    """

    choices = {
        "liter": Decimal(1),
        "liters": Decimal(1),
        "l": Decimal(1),
    }


## Part III -- Aspects and Effects

def logged[T: type](cls: T) -> T:
    """Inject a properly-named logger into a class definition to permit logging prior to super().__init__()."""
    cls.logger = logging.getLogger(cls.__name__)
    return cls

@logged
class Aspect:
    """
    Abstract base class for Aspects and Effects.

    Computes a difficulty, a description summary, and details from a batch of parameters.
    Also has an increment/decrement attribute, provided by a mixin from the :py:class:`DifficultyAdjustment` class.

    Generally, the values are computed by the :py:meth:`__init__` method.

    Currently, there are explicit methods for difficulty and description,
    but they report the values computed by :py:meth:`__init__`.
    """

    incr_decr: Sign  # Set by a mixin of DifficultyAdjustment

    _difficulty: Decimal
    _description: str
    details: list[tuple[Decimal, str]]
    attr_paths: str | tuple[str, ...]

    logger: logging.Logger

    def __init__(
            self,
            difficulty: int | Decimal,
            description: str,
            *,
            attr_paths: str | tuple[str, ...] | None = None,
            source: str | None = None
    ) -> None:
        """Subclasses generally invoke this after working out the difficulty and descriptive text.
        The ``attr_paths`` are used for based-on definitions to track the origin of a derived aspect.
        """
        self._difficulty = Decimal(difficulty)
        self._description = description
        if attr_paths:
            self.attr_paths = attr_paths
        if source:
            # A Derived aspect with a source attribute or effect.
            self.source = source

    def _asdict(self) -> dict[str, Any]:
        """Emit details of this aspect or effect for a TOML dump.
        ..  todo:: Finish this -- requires a careful recursive walk.
        """
        if hasattr(self, "attr_paths"):
            return {
                self.__class__.__name__: {
                    "based_on": self.attr_paths,
                    "target": repr(self._description),
                }
            }
        else:
            return {self.__class__.__name__: repr(self._description)}

    def __repr__(self) -> str:
        """A representation that reflects the original source.

        This isn't a "complete" ``__repr__()`` value because of derived values and based-on relationships.

        For aspects created by a based-on relationship, show the original ``attr_paths``.
        """
        if hasattr(self, "attr_paths"):
            return f"{self.__class__.__name__}.based_on({self.attr_paths!r}, target={self._description!r})"
        else:
            return f"{self.__class__.__name__}({self._description!r})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self._difficulty == other._difficulty and self._description == other._description
        return NotImplemented

    @classmethod
    def based_on(cls, attr_paths: str | tuple[str, ...], *measures: Any, **kwargs: Any) -> "Aspect":
        """
        This Aspect depends on one (or more) of the aspects or effects of this :py:class:`Spell`.
        The default base for the based_on relationship is the spell is this embedded in.
        The :py:meth:`Spell.finalize` method can refer to another Spell, permitting generic templates.

        This method will create a :py:class`DerivedAspect` object, which will then build the real :py:class:`Aspect`.
        The final construction of the Aspect happens during :py:meth:`Spell.finalize` processing.
        """
        return DerivedAspect.placeholder(attr_paths, cls, *measures, **kwargs)

    @classmethod
    def based_on_spell(
        cls, attr_paths: str | tuple[str, ...], *measures: Any, **kwargs: Any
    ) -> "Aspect":
        """
        Same as :py:meth:`based_on`, but with an expectation that
        another Spell will be used as the basis for derived Aspects.

        ..  todo:: Finish this.
        """
        return DerivedAspect.placeholder(attr_paths, cls, *measures, **kwargs)

    def difficulty(self) -> int:
        """This aspect's difficulty."""
        return int(self._difficulty)

    def description(self) -> str:
        """This aspect's description."""
        return self._description

    def summary(self) -> str:
        """A summary used in debugging and logging."""
        return shorten(self._description, 24)

    @staticmethod
    def normalize_measures(base_unit: str, *measures: str | int | float) -> Iterator[str]:
        """In principle, this can **almost** be refactored into :py:class:`Lookup`.

        Some Aspects subclasses have Multiple Lookup/Modifier classes, making it unclear where this goes.

        ..  todo:: This should be Iterator[DieCode | str]. Die Codes should be left intact.
        """
        for measure in measures:
            match measure:
                case DieCode() as die:
                    yield str(die)
                case str():
                    multi = measure.split(";")
                    yield from (m.strip() for m in multi)
                case int() | float():
                    if base_unit:
                        yield f"{measure} {base_unit}"
                    else:
                        yield str(measure)
                case _:
                    raise ValueError(f"invalid type {type(measure)}: {measure!r}")


class GenericAspect(DecreasesDifficulty, Aspect):
    """
    Generic Aspect with simple description and difficulty.
    This is designed for the various items that show up in ``other_conditions`` of a Spell.
    These, generally, reduce the difficulty.

    (See :external:ref:`fantasy.magic.other_conditions`.)

    >>> from opend6_tools.magic2 import *
    >>> generic = GenericAspect(2, "Not too hard")
    >>> generic.difficulty()
    2
    >>> generic.description()
    'Not too hard'
    >>> repr(generic)
    "GenericAspect(Decimal('2'), 'Not too hard')"
    """

    def __init__(self, difficulty: int, description: str) -> None:
        super().__init__(difficulty, description)
        self.details = [(self._difficulty, self._description)]

    def _asdict(self) -> dict[str, Any]:
        return {
            self.__class__.__name__: {
                "difficulty": self._difficulty,
                "description": self._description,
            }
        }

    def __repr__(self) -> str:
        """A representation that reflects the original source."""
        return f"{self.__class__.__name__}({self._difficulty!r}, {self._description!r})"

@logged
class DerivedAspect(Aspect):
    """
    A proxy for an :py:class:`Aspect` that's based on another Aspect or Effect.
    This will build the final Aspect (or Effect) when the dependencies are in place.

    As a general design principle, all computations are done in :meth:`Aspect.__init__`.
    This is tricky when one :py:class:`Aspect` instance depends on others, since the other aspects may not be part of the Spell.

    A :py:class:`DerivedAspect` is transformed by the :meth:`Spell.finalize` method into the final :py:class:`Aspect`.
    This will set all the attributes of the derived :py:class:`Aspect` instance.
    Once the pre-requisite aspects have been built, then the derived aspect can be built.
    """
    target_class: type[Aspect]
    measures: tuple[Any, ...]
    kwargs: dict[str, Any]

    @classmethod
    def placeholder(
        cls,
        attr_paths: str | tuple[str, ...],
        target_class: type[Aspect],
        *measures: Any,
        **kwargs: Any,
    ) -> "DerivedAspect":
        attr = DerivedAspect(
            0, f"based on {', '.join(attr_paths)}",
            attr_paths=attr_paths if isinstance(attr_paths, tuple) else (attr_paths,)
        )
        # self.attr_paths = attr_paths if isinstance(attr_paths, tuple) else (attr_paths,)
        # self._description = f"based on {', '.join(self.attr_paths)}"
        # self._difficulty = Decimal(0)
        attr.target_class = target_class
        attr.measures = measures
        attr.kwargs = kwargs
        return attr

    def __repr__(self) -> str:
        return (
            f"{self.target_class.__name__}.based_on({self.attr_paths!r}, *{self.measures!r}, **{self.kwargs!r})"
            if self.kwargs
            else f"{self.target_class.__name__}.based_on({self.attr_paths!r}, *{self.measures!r})"
        )

    def ready(self, spell: "Spell") -> bool:
        """Can this Aspect be derived from the given Spell? Are all the dependencies in place?"""
        return all(hasattr(spell, attr) for attr in self.attr_paths)

    def __call__(self, spell: "Spell") -> Aspect:
        """
        Build the target Aspect class based on one or more attributes of the Spell.
        """
        cls = cast(type[Aspect], self.target_class)
        difficulty = sum(getattr(spell, attr).difficulty() for attr in self.attr_paths)
        source = "; ".join(getattr(spell, attr).description() for attr in self.attr_paths)
        self.logger.debug(
            "%s(*%r, difficulty=%r, source=%r, **%r)",
            cls.__name__,
            self.measures,
            difficulty,
            source,
            self.kwargs,
        )
        aspect = cls(*self.measures, difficulty=difficulty, source=source, **self.kwargs)
        aspect.attr_paths = self.attr_paths
        return aspect


class CompositeAspect(Aspect):
    """Combines one or more Aspect details into a single Aspect.
    Example is multiple Community instances.

    The class is still (in a way) abstract, beacuse it doesn't have an ``incr_decr`` attribute.
    Pragmatically, this value is deduced from the component aspects.

    >>> from opend6_tools.magic2 import *
    >>> composite = CompositeAspect(
    ...     GenericAspect(3, "this"),
    ...     GenericAspect(5, "that"))
    >>> composite.difficulty()
    8
    >>> composite.description()
    'this; that'
    >>> repr(composite)
    "CompositeAspect(*(GenericAspect(Decimal('3'), 'this'), GenericAspect(Decimal('5'), 'that')))"
    >>> composite.append(GenericAspect(11, "another"))
    >>> composite.difficulty()
    19
    >>> composite.description()
    'this; that; another'

    """

    def __init__(self, *aspects: Aspect) -> None:
        """Build the composite Aspect from other Aspects."""
        self.aspects = aspects
        sign = set(a.incr_decr for a in self.aspects)
        if len(sign) != 1:
            raise ValueError("invalid mixture of difficulty Increment and Decrement aspects")
        self.incr_decr = sign.pop()
        super().__init__(
            sum(a.difficulty() for a in self.aspects),
            "; ".join(a.description() for a in self.aspects)
        )
        self.details = sum((a.details for a in self.aspects), start=[])

    def append(self, new_aspect: Aspect) -> None:
        """Append another Aspect to this Aspect."""
        self.aspects += (new_aspect,)
        self._difficulty += new_aspect.difficulty()
        self._description += f"; {new_aspect.description()}"
        self.details += new_aspect.details

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        return f"{self.__class__.__name__}(*{self.aspects!r})"


class Effect(IncreasesDifficulty, Aspect):
    """
    The Effect of a Spell or Miracle; a specialized Aspect.
    Effects always increase difficulty.

    This class defines a general-purpose effect, using a manually-computed difficulty.
    It should be avoided in general, because the description
    The various subclasses compute difficulty from the effects.

    >>> from opend6_tools.magic2 import *
    >>> e = Effect("something", 5)
    >>> e.difficulty()
    5
    >>> e.description()
    'something'
    >>> e.incr_decr
    <Sign.Increase: 1>
    >>> repr(e)
    "Effect(measure='something', difficulty=Decimal('5'))"
    >>> list(e.normalize_measures("", 5, 3*D, "+7D"))
    ['5', '+3D', '+7D']
    """

    _skill: str

    def __init__(self, measure: str, difficulty: int = 1) -> None:
        """Create an Effect. Note that the measure and difficulty are **REVERSED** from ``Aspect``."""
        super().__init__(difficulty, measure)
        # self._description = measure
        # self._difficulty = Decimal(difficulty)
        self.details = [(Decimal(difficulty), measure)]
        self._skill = measure

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        return f"{self.__class__.__name__}(measure={self._description!r}, difficulty={self._difficulty!r})"

    def skill(self) -> str:
        """Skill string, based (without other arrangements) on the measure."""
        return self._skill


class OtherAlterant(IncreasesDifficulty, Aspect):
    """
    Generic Aspect with simple description and difficulty.
    This is designed for the things like items that show up in the ``other_alterants`` mapping of a Spell.

    If there are more than one aspects to an alterant, they can be combined with ``CompositeAspect(Other_Alterant(), ...)``.

    (See :external:ref:`fantasy.magic.other_alterant`.)


    >>> from opend6_tools.magic2 import *
    >>> alterant = OtherAlterant(2, "An Additional Nuance")
    >>> alterant.difficulty()
    2
    >>> alterant.description()
    'An Additional Nuance'
    >>> repr(alterant)
    "OtherAlterant(Decimal('2'), 'An Additional Nuance')"
    """

    def __init__(self, difficulty: int, description: str) -> None:
        super().__init__(difficulty, description)
        # self._difficulty = Decimal(difficulty)
        # self._description = description
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        """A representation that reflects the original source."""
        return f"{self.__class__.__name__}({self._difficulty!r}, {self._description!r})"


class CharactersticFactor(Factor):
    """
    The "Characteristic Type" factors from the Die Codes sidebar.
    (See :external:ref:`Characteristic Type <fantasy.magic.die_codes>`.)

        ..  csv-table::

            Stand-alone stun damage (physical only),     0.75
            Stand-alone damage\\*,                         1
            Stand-alone protection\\*,                     1
            Protection or damage modifier\\*,              1.5
            Stand-alone die code or non-Extranormal skill, 1
            Non-Extranormal skill modifier, 1.5
            Stand-alone non-Extranormal attribute, 1.5
            Non-Extranormal attribute modifier, 2
            Stand-alone Extranormal skill, 2
            Extranormal skill modifier, 2.5
            Extranormal attribute modifier, 3

        \\* *To protect against or do damage as both mental and physical, each type, purchase each one separately.*

        Note: To have damage ignore non-magical armor, add 0.5
        to the value multiplier listed. To have protection against either
        magical or non-magical attacks (but not both), subtract 0.5 from
        the value multiplier listed.

    Also, see :external:ref:`fantasy.magic.note_attack_and_protection`.

        By default, magical and nonmagical armor can defend against
        attack spells. To ignore nonmagical armor, double the value to add
        it. Damage is either physical or mental. To do both, each kind must
        be purchased separately.

        Similarly, protection spells defend against both magical and nonmagical attacks.
        To be subject to one but not the other, half the value
        to add it (round up). The protection may be against physical or mental
        attacks. To resist both, each kind must be purchased separately.

    ..  note:: When multiple factors are present, the largest is used for difficulty computations.
    """

    # Note spelling aliases.
    choices = {
        "stun only": Decimal("0.75"),
        "protection modifier": Decimal("1.5"),
        "physical damage": Decimal(1),
        "mental damage": Decimal(1),
        "damage modifier": Decimal("1.5"),
        "only effects attack spells": Decimal("1.5"),
        "ignore nonmagical armor": Decimal("1.5"),
        "ignores nonmagical armor": Decimal("1.5"),
        "ignore all armor": Decimal("2"),
        "ignores all armor": Decimal("2"),
        "skill": Decimal(1),
        "skill modifier": Decimal("1.5"),
        "attribute": Decimal("1.5"),
        "attribute modifier": Decimal("2"),
        "extranormal skill": Decimal("2"),
        "extranormal skill modifier": Decimal("2.5"),
        "extranormal attribute modifier": Decimal(3),
    }


class CharacteristicModifier(Modifier):
    """
    Note: To have damage ignore non-magical armor, add 0.5
    to the value multiplier listed. To have protection against either
    magical or non-magical attacks (but not both), subtract 0.5 from
    the value multiplier listed.
    """

    choices = {
        "ignore non-magical armor": 0.5,
        "magical only": -0.5,
        "non-magical only": -0.5,
    }

@logged
class MeasureEffect(Effect):
    """
    Abstract Base Class for a number of effects with distinct measurement units.
    This examines the parameters to extract Measures, Modifiers, and Factors.
    It computes a net description and difficulty from the details.

    This class is generic with respect to a unit type, modifier parser, and factor parser.

    The unit must be a mixin that provides the needed :py:meth:`parse` method.

    ..  todo:: Modifiers seem to get lost and don't seem to be figured in correctly.
    """

    def __init__(self, *source_measures: str | int | float) -> None:
        modifier = CharacteristicModifier()
        factor = CharactersticFactor()
        skills: list[str] = []  # Stray text, e.g., "Blocks" or "Destroys".
        measures: list[tuple[Decimal, str]] = []
        modifiers: list[tuple[Decimal, str]] = []
        factors: list[tuple[Decimal, str]] = []
        # The errors list is used when we can't locate a measure.
        errors: list[tuple[BaseException | None, ...]] = []

        # Decompose source_measures into skills, measures, factors, and modifiers.
        for measure in self.normalize_measures("", *source_measures):
            ex_factor = ex_modifier = ex_measure = None
            # Try the parent class to parse a measure.
            try:
                measures.append(self.parse(measure))
                continue
            except ValueError as ex:
                ex_measure = ex
                self.logger.debug("Measure parse %r", ex_measure)
            # Didn't work? Try the factor class to parse a factor.
            try:
                factors.append(factor.parse(measure))
                continue
            except ValueError as ex:
                ex_factor = ex
                self.logger.debug("Factor parse %r", ex_factor)
            # Didn't work? Try the modifier class to parse a modifier.
            try:
                modifiers.append(modifier.parse(measure))
                continue
            except ValueError as ex:
                ex_modifier = ex
                self.logger.debug("Modifier parse %r", ex_modifier)

            # What's left might be a skill, or some other note.
            skills.append(measure)
            errors.append((ex_factor, ex_modifier, ex_measure))

        if not measures:
            # No measure? Invalid effect.
            raise ValueError(f"No measure recognized; possible missing ',' between argument values: {errors!r}")

        # Compute the difficulty
        base_difficulty = Decimal(sum(diff for diff, _ in measures))
        # We want the largest, which might be less than 1.
        # OR the list might be empty.
        # Append a zero; if that's the max replace it with 1
        max_factor = max([f for f, _ in factors] + [0]) or 1
        total_mod = sum(m for m, _ in modifiers)

        text_measures = " ".join(desc for _, desc in measures)
        if text_skills := " ".join(skills):
            text_measures = f"{text_skills} {text_measures}"
        if text_factors := "; ".join(desc for _, desc in factors):
            text_measures = f"{text_measures} ({text_factors})"

        super().__init__(
            text_measures,
            int((base_difficulty * (max_factor + total_mod)).quantize(
                Decimal(1), rounding=decimal.ROUND_UP
            )),
        )
        self._skill = " ".join(skills) or text_measures
        self.details = measures + factors + modifiers

    def __repr__(self) -> str:
        """Not a complete repr(); this is just enough to rebuild the initial declaration."""
        text = [repr(desc) for _, desc in self.details]
        return f"{self.__class__.__name__}({self._skill!r}, {', '.join(text)})"

    @abc.abstractmethod
    def parse(self, measure: str) -> tuple[Decimal, str]: ...


class DamageEffect(DieUnit, MeasureEffect):
    """An Effect of a Spell or Miracle that does damage.
    The units are generally :py:class:`DieCode` values or strings.

    (See :external:ref:`fantasy.magic.effect_skill_used`.)

    Rules:

        Damage spells affect character health (that is, their Body
        Points or Wounds). To hurt someone, 6D (which you can
        determine, by using the "Die Code" table, has a value of 18)
        is a safe bet. To kill someone outright, 10D (which has a value
        of 30) is usually necessary.

        Both protection and damage have a visible component (such as a
        glowing aura) that indicates their use and, if relevant, trajectory.

    >>> from opend6_tools.magic2 import *
    >>> damage = DamageEffect("Body damage", "+4D+1")
    >>> damage.difficulty()
    13
    >>> damage.description()
    'Body damage +4D+1'
    >>> damage.incr_decr
    <Sign.Increase: 1>
    >>> repr(damage)
    "DamageEffect('Body damage', '+4D+1')"
    """


class ProtectionEffect(DieUnit, MeasureEffect):
    """An Effect of a Spell or Miracle that protects from damage.
    The units are DieCode strings.
    (See :external:ref:`fantasy.magic.effect_skill_used`.)

    Rules:

        Protection spells work similarly [do damage spells], though, obviously, they
        reduce the amount of damage taken. Checking out weapon
        damage die codes can help you determine the number of dice you
        need for your spell.

        Both protection and damage have a visible component (such as a
        glowing aura) that indicates their use and, if relevant, trajectory.


    >>> from opend6_tools.magic2 import *
    >>> protection = ProtectionEffect("Damage Resistance", "+4D+1", "physical damage", "ignore all armor")
    >>> protection.difficulty()
    26
    >>> protection.description()
    'Damage Resistance +4D+1 (physical damage; ignore all armor)'
    >>> protection.incr_decr
    <Sign.Increase: 1>
    >>> repr(protection)
    "ProtectionEffect('Damage Resistance', '+4D+1', 'physical damage', 'ignore all armor')"
    """

@logged
class SkillEffect(DieUnit, MeasureEffect):
    """An Effect of a Spell or Miracle that boosts a Skill.
    It uses DieCodes for units.
    (see :external:ref:`fantasy.magic.applying_the_effect`.)

    Rules:

        Spells that increase, decrease, create, or otherwise affect attributes
        or skills are determined the same way [using the "Die Code" table]. For example, a spell to take
        over someone's mind would give the caster a persuasion of +3D or
        more with a value of at least 14.

    Example from the :external:ref:`fantasy.magic.die_codes`:

    ..  csv-table:

        Stand-alone die code or non-Extranormal skill, 1
        Non-Extranormal skill modifier, 1.5

    >>> from opend6_tools.magic2 import *
    >>> skill = SkillEffect("Physique: lifting", "+5D")
    >>> skill.difficulty()
    15
    >>> skill.description()
    'Physique: lifting +5D'
    >>> skill.incr_decr
    <Sign.Increase: 1>
    >>> repr(skill)
    "SkillEffect('Physique: lifting', '+5D')"
    """
    def __init__(self, skill: str, *measures: str) -> None:
        self.logger.debug("Creating %s, parent %s", self.__class__, super())
        super().__init__(skill, *measures)
        self._skill = skill

    def skill(self):
        return self._skill


class AttributeEffect(SkillEffect):
    """Identical to SkillEffect, except other modifiers are expected.
    (See :external:ref:`fantasy.magic.effect_skill_used`.)

    Rules:

        Spells that increase, decrease, create, or otherwise affect attributes
        or skills are determined the same way [using the "Die Code" table].
        For example, a spell to take over someone's mind would give the
        caster a persuasion of +3D or more with a value of at least 14.

    Example from the :external:ref:`fantasy.magic.die_codes`:

    ..  csv-table:

        Stand-alone non-Extranormal attribute, 1.5
        Non-Extranormal attribute modifier, 2

    >>> from opend6_tools.magic2 import *
    >>> attr = AttributeEffect("Physique", "+5D", "attribute modifier")
    >>> attr.difficulty()
    30
    >>> attr.description()
    'Physique +5D (attribute modifier)'
    >>> attr.incr_decr
    <Sign.Increase: 1>
    >>> repr(attr)
    "AttributeEffect('Physique', '+5D', 'attribute modifier')"
    """

    pass


class AbilityLookup(Lookup):
    """
    Abstract class to define lookups with distinct costs:
    Used for Special Abilities, Limitations, and Enhancements.
    """

    _rules: str

    @staticmethod
    def _name_cost(table: str) -> Iterator[tuple[str, Decimal]]:
        ability_pattern = (
            group(one_or_more_lazy(ANYCHAR))
            + zero_or_more(WHITESPACE)
            + OPEN_PAREN
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
        )
        clean = filter(None, (row.strip() for row in table.splitlines()))
        for line in clean:
            if match := re.match(ability_pattern, line):
                yield match.group(1).lower(), Decimal(match.group(2))
            else:
                raise SyntaxError(f"invalid {line!r}, doesn't match {ability_pattern!r}")


class SpecialAbilityLookup(AbilityLookup):
    """
    The defined Special Abilities, and their costs.
    (See :external:ref:`options.special_abilities`.)

    >>> from opend6_tools.magic2 import *
    >>> SpecialAbilityLookup().parse("Extra Sense")
    (Decimal('1'), 'extra sense')
    """

    _rules = dedent("""\
    Accelerated Healing (3)

    Ambidextrous (2)

    Animal Control (3)

    Armor-Defeating Attack (2)

    Atmospheric Tolerance (2)

    Attack Resistance (2)

    Attribute Scramble (4)

    Blur (3)

    Combat Sense (3)

    Confusion ( 4)

    Darkness (3)

    Elasticity (1)

    Endurance (1)

    Enhanced Sense (3)

    Environmental Resistance (1)

    Extra Body Part (0)

    Extra Sense (1)

    Fast Reactions (3)

    Fear (2)

    Flight (6)

    Glider Wings (3)

    Hardiness (1)

    Hypermovement (1)

    Immortality (7)

    Immunity (1)

    Increased Attribute (2)

    Infravision/Ultravision (1)

    Intangibility (5)

    Invisibility (3)

    Iron Will (2)

    Life Drain (5)

    Longevity (3)

    Luck: Good (2)
     
    Luck: Great (3)

    Master of Disguise (3)

    Multiple Abilities (1)

    Natural Armor (3)

    Natural Hand-to-Hand Weapon (2)

    Natural Magick (5 or more)

    Natural Ranged Weapon (3)

    Omnivorous (2)

    Paralyzing Touch (4)

    Possession: Limited (8)
    
    Possession: Full (10)

    Quick Study (3)

    Sense of Direction (2)

    Shapeshifting (3)

    Silence (3)

    Skill Bonus (1)

    Skill Minimum (4)

    Teleportation (3)

    Transmutation (5)

    Uncanny Aptitude (3)

    Ventriloquism (3)

    Water Breathing (2)

    Youthful Appearance (1)
    """)
    choices = dict(AbilityLookup._name_cost(_rules))


class LimitationLookup(AbilityLookup):
    """
    The defined Special Ability Limitations, and their costs.
    (See :external:ref:`options.special_abilities.limitations`.)

    >>> from opend6_tools.magic2 import *
    >>> LimitationLookup().parse("Restricted")
    (Decimal('1'), 'restricted')
    """

    _rules = dedent("""\
    Ability Loss (3 for 1 rank; 4 for 2 ranks)

    Allergy (3 for 1 rank; 4 for 2 ranks)

    Burn-out (1)

    Debt(3)

    Flaw(1)

    Minor Stigma (3)

    Others Only (2 for 1 rank; 3 for 2 ranks; 4 for 3 ranks)

    Price (1)

    Restricted (1)

    Side Effect (2)

    Singularity (1 per Special Ability)

    Super-science (2)
    """)
    choices = dict(AbilityLookup._name_cost(_rules))


class Limitation(LimitationLookup):
    """
    Limitations and their base values.

    These are vaguely Aspect-like -- they have a difficulty and a description.
    They are not, however, proper Aspects.
    They're part of a SpecialAbility, not an overall Spell.

    Rules:

        These Limitations can be associated with SpecialAbilities, restrict-
        ing their functionality and reducing their total cost (base cost plus
        the cost for additional ranks plus any Enhancements - not the per
        rank cost).

        Limitations may not lower a Special Ability's total cost below one,...

    >>> from opend6_tools.magic2 import *
    >>> restricted = Limitation("Restricted", 2)
    >>> restricted.difficulty()
    Decimal('2')
    >>> restricted.description()
    "Limitation('Restricted', 2, note='')"
    """

    def __init__(self, name: str, rank: int, note: str = "") -> None:
        """
        Define a limitation

        :param name: Name of the limitation
        :param rank: Rank
        :param note: Any supporting text
        """
        self.name = name
        self.rank = rank
        self.note = note
        cost, clean = self.parse(name)
        self._difficulty = self.rank * cost
        self._description = f"{self.name} (R{self.rank}) {self.note}"

    def difficulty(self) -> Decimal:
        """Difficulty, based on rank and base cost per rank."""
        return self._difficulty

    def description(self) -> str:
        """Description of the limitation."""
        return f"{self.__class__.__name__}({self.name!r}, {self.rank!r}, note={self.note!r})"


class Enhancement(Limitation):
    pass


class SpecialAbilityEffect(SpecialAbilityLookup, Effect):
    """
    When a spell confers a temporary special ability.
    The details are in the :py:class:`SpecialAbilityLookup` definition.
    (See :external:ref:`fantasy.magic.effect_skill_used`.)

    Rules:

        Some spells' effects are best reflected by a Special Ability or a
        Disadvantage. With a Special Ability, the spell effect's value equals 3
        times the Special Ability cost times the number of ranks in that Special
        Ability, plus the cost of any Enhancements and their ranks, minus
        the cost of any Limitations and their ranks. ...

        The cost of one rank of the Special Ability is included in parentheses.

    Examples:

    >>> from opend6_tools.magic2 import *
    >>> eff_1 = SpecialAbilityEffect("Extra Sense: Bugs", 3)
    >>> eff_1.difficulty()
    9
    >>> eff_1.description()
    'Extra Sense: Bugs (R3)'
    >>> repr(eff_1)
    "SpecialAbilityEffect('Extra Sense: Bugs', 3)"

    Ability cost = 1, ranks = 3, (x3) = 9

    >>> eff_2 = SpecialAbilityEffect("Accelerated Healing", 7)
    >>> eff_2.difficulty()
    63
    >>> eff_2.description()
    'accelerated healing (R7)'
    >>> repr(eff_2)
    "SpecialAbilityEffect('Accelerated Healing', 7)"

    Ability cost = 3, ranks = 7, (x3) = 63

    Syntax is unique. Often stateds as ``Ability[: Details] (R\\d)``.
    We break it into two parameters: the ``Ability[: Details]`` and the rank as a simple integer.
    The ``: Details`` suffix has one of two roles:

    -   It may be part of the ability name, or
    -   It may be an additional detail.

    BOTH options need to be checked.

    ..  todo:: Implement Enhancements and Limitations.
    """

    def __init__(
        self,
        ability: str,
        rank: str | int,
        note: str = "",
        limitations: list[Limitation] | None = None,
        enhancements: list[Enhancement] | None = None,
    ) -> None:
        self.ability = ability
        self.rank = int(rank)
        self.note = note
        self.limitations = limitations or []
        self.enhancements = enhancements or []
        ability_pattern = group(one_or_more(nonchars(":"))) + optional_noncap_group(
            ":" + one_or_more(WHITESPACE) + group(EVERYTHING)
        )
        if match := re.match(ability_pattern, ability):
            base_name = match.group(1)
            if detail := match.group(2):
                full_name = f"{base_name}: {detail}"
                try:
                    sa_cost, description = self.parse(full_name)
                except ValueError:
                    sa_cost, _ = self.parse(base_name)
                    description = full_name
            else:
                sa_cost, description = self.parse(base_name)
        else:
            raise ValueError(f"can't parse {ability!r}")
        lim_cost = sum(l.difficulty() for l in self.limitations)
        enh_cost = sum(e.difficulty() for e in self.enhancements)
        # self._difficulty = (sa_cost + enh_cost - lim_cost) * self.rank * 3
        # self._description = (
        #     f"{description} (R{self.rank}), {note}" if note else f"{description} (R{self.rank})"
        # )
        super().__init__(
            (
                f"{description} (R{self.rank}), {note}" if note else f"{description} (R{self.rank})"
            ),
            int((sa_cost + enh_cost - lim_cost) * self.rank * 3),
        )
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        params = [repr(self.ability), repr(self.rank)]
        if self.note:
            params += [f"note={self.note!r}"]
        if self.limitations:
            params += [f"limitations={self.limitations!r}"]
        if self.enhancements:
            params += [f"enhancements={self.enhancements!r}"]
        return f"{self.__class__.__name__}({', '.join(params)})"


class DisadvantageEffect(Effect):
    """
    When a spell confers a temporary Disadvantage.
    Examples "Hindrance: Initiative", "Luck: Bad", "Age: Old".
    (See :external:ref:`fantasy.magic.effect_skill_used`.)

    Rules:

        Some spells' effects are best reflected by a Special Ability or a
        Disadvantage. ... With a Disadvantage, the
        spell effect's value equals the 3 times the cost of the Disadvantage.
        Spells generally do not provide a target with Advantages or improved
        Funds, but the gamemaster may allow this in special circumstances,
        such creating a friendship spell using Contacts.

        Each rank in an Advantage or Disadvantage is worth one creation
        point (or one skill die, if you're using defined limits) per number.

    A die is 3 points when computing spell difficulties.

    Examples:

    >>> from opend6_tools.magic2 import *
    >>> eff_1 = DisadvantageEffect("Hindrance: Initiative", 5, "-10 to all initiative totals")
    >>> eff_1.difficulty()
    15
    >>> eff_1.description()
    'Hindrance: Initiative (R5), -10 to all initiative totals'
    >>> eff_1.incr_decr
    <Sign.Increase: 1>
    >>> eff_1.incr_decr.value * eff_1.difficulty()
    15
    >>> repr(eff_1)
    "DisadvantageEffect('Hindrance: Initiative', 5, note='-10 to all initiative totals')"
    """

    def __init__(self, disadvantage: str, rank: str | int, note: str = "") -> None:
        self.disadvantage = disadvantage
        self.rank = rank
        self.note = note
        # self._difficulty = Decimal(rank) * 3
        # self._description = (
        #     f"{disadvantage} (R{rank}), {note}" if note else f"{disadvantage} (R{rank})"
        # )
        super().__init__(
            f"{disadvantage} (R{rank}), {note}" if note else f"{disadvantage} (R{rank})",
            int(Decimal(rank) * 3),
        )
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        return (
            f"{self.__class__.__name__}({self.disadvantage!r}, {self.rank!r}, note={self.note!r})"
        )


class TimeEffect(TimeUnit, MeasureEffect):
    """An Effect of a Spell or Miracle based on time.
     For example, one that adjusts duration of another spell.
     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> from opend6_tools.magic2 import *
    >>> time = TimeEffect("Reduces duration", "10 min")
    >>> time.difficulty()
    14
    >>> time.description()
    'Reduces duration 10 min'
    >>> time.incr_decr
    <Sign.Increase: 1>
    >>> repr(time)
    "TimeEffect('Reduces duration', '10 min')"
    """


class DistanceEffect(DistUnit, MeasureEffect):
    """An Effect of a Spell or Miracle based on distance, usually Apportation.

     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> from opend6_tools.magic2 import *
    >>> dist = DistanceEffect("Moves something", "1 km")
    >>> dist.difficulty()
    15
    >>> dist.description()
    'Moves something 1 km'
    >>> dist.incr_decr
    <Sign.Increase: 1>
    >>> repr(dist)
    "DistanceEffect('Moves something', '1 km')"
    """


class MassEffect(MassUnit, MeasureEffect):
    """An Effect of a Spell or Miracle based on mass.
     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> from opend6_tools.magic2 import *
    >>> mass = MassEffect("Moves", "100 kilograms")
    >>> mass.difficulty()
    10
    >>> mass.description()
    'Moves 100 kilograms'
    >>> mass.incr_decr
    <Sign.Increase: 1>
    >>> repr(mass)
    "MassEffect('Moves', '100 kilograms')"
    """


class VolumeEffect(VolumeUnit, MeasureEffect):
    """An Effect of a Spell or Miracle based on volume.
     (See :external:ref:`Area Effect: Odd Shapes <magic_guide.aspects.area_odd_shapes>`.)

    >>> from opend6_tools.magic2 import *
    >>> vol = VolumeEffect("Creates", "100 liters")
    >>> vol.difficulty()
    10
    >>> vol.description()
    'Creates 100 liters'
    >>> vol.incr_decr
    <Sign.Increase: 1>
    >>> repr(vol)
    "VolumeEffect('Creates', '100 liters')"
    """


class CompositeEffect(IncreasesDifficulty, Aspect):
    """Combines two or more :py:class:`Effect` instances.
    All the Effects must be a subclass of :py:class:`IncreasesDifficulty`.

    Rules:

        A spell may contain more than one effect. Each effect is determined
        separately and added to the total. All of the effects must fall under
        the domain of the same skill. You should also list the skill used to
        cast the spell at this time. See the "Skills and Sample Effects" sidebar
        for suggestions.


    >>> from opend6_tools.magic2 import *
    >>> e_1 = SkillEffect("Coordination: marksmanship", "+2D")
    >>> e_2 = DamageEffect("Damage", "+2D")
    >>> composite = CompositeEffect("Magic Bullet", e_1, e_2)
    >>> composite.difficulty()
    12
    >>> composite.description()
    'Magic Bullet: Coordination: marksmanship +2D; Damage +2D'
    >>> composite.incr_decr
    <Sign.Increase: 1>
    >>> repr(composite)
    "CompositeEffect('Magic Bullet', SkillEffect('Coordination: marksmanship', '+2D'), DamageEffect('Damage', '+2D'))"

    """

    def __init__(self, summary: str, *effects: Effect) -> None:
        """Builds the CompositeEffect from a description and individual Effects.

        :param description: A pithy summary
        :param effects: Individual :py:class:`Effect` instances.
        """
        sign = set(a.incr_decr for a in effects)
        if len(sign) != 1:
            raise ValueError("mixture of difficulty Increment and Decrement aspects")
        self.incr_decr = sign.pop()
        self.summary_effect = summary
        self.effects = effects
        #self._difficulty = sum(e.difficulty() for e in self.effects)
        #self._description = description
        desc_text = "; ".join(e.description() for e in self.effects)
        super().__init__(
            sum(e.difficulty() for e in self.effects),
             f"{self.summary_effect}: {desc_text}"
        )
        self.details = [d for e in self.effects for d in e.details]

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        text = [repr(e) for e in self.effects]
        return f"{self.__class__.__name__}({self.summary_effect!r}, {', '.join(text)})"

    # def difficulty(self) -> int:
    #     """Compute the difficulty."""
    #     return sum(e.difficulty() for e in self.effects)
    #
    # def description(self) -> str:
    #     """The description, based on the acomponents."""
    #     details = "; ".join(e.description() for e in self.effects)
    #     return f"{self._description}: {details}"

    def skill(self) -> str:
        """The skill, based on the components."""
        details = ", ".join(e.skill() for e in self.effects)
        return details


class TimeAspect(TimeUnit, Aspect):
    """A base class for any Aspects using :py:class:`TimeUnit`.

    >>> from opend6_tools.magic2 import *

    # 2 rounds = 10 seconds
    >>> a = TimeAspect("2 rounds")
    >>> a.difficulty()
    5
    >>> a.description()
    '2 rounds'
    >>> repr(a)
    "TimeAspect('2 rounds')"

    # 1.5 rounds = 7.5 seconds
    >>> b = TimeAspect("1.5 rounds")
    >>> b.difficulty()
    5
    >>> b.description()
    '1.5 rounds'
    >>> repr(b)
    "TimeAspect('1.5 rounds')"

    """

    def __init__(self, measure: str | int | float) -> None:
        # self._difficulty, self._description = self.parse(measure)
        super().__init__(*self.parse(measure))
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        return f"{self.__class__.__name__}({self._description!r})"


class DistanceAspect(DistUnit, Aspect):
    """A base class for any Aspects using :py:class:`DistUnit`.

    >>> from opend6_tools.magic2 import *
    >>> d = DistanceAspect("10 m")
    >>> d.difficulty()
    5
    >>> d.description()
    '10 m'
    >>> repr(d)
    "DistanceAspect('10 m')"
    """

    def __init__(self, measure: str | int | float) -> None:
        # self._difficulty, self._description = self.parse(measure)
        super().__init__(*self.parse(measure))
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        """Not a complete repr() -- enough to rebuild the instance"""
        return f"{self.__class__.__name__}({self._description!r})"


class RangeAspect(IncreasesDifficulty, DistanceAspect):
    """The Range Aspect, implemented using the :py:class:`DistanceAspect`.

    (See :external:ref:`fantasy.magic.range`.)

    >>> from opend6_tools.magic2 import *
    >>> r_15 = RangeAspect("15 m")
    >>> r_15.difficulty()
    6
    >>> r_15.description()
    '15 m'
    >>> r_15.incr_decr
    <Sign.Increase: 1>
    >>> repr(r_15)
    "RangeAspect('15 m')"

    >>> r_0 = RangeAspect("1m")
    >>> r_0.difficulty()
    0
    >>> r_0.description()
    '1 m'
    >>> repr(r_0)
    "RangeAspect('1 m')"
    """


class SpeedAspect(IncreasesDifficulty, DistanceAspect):
    r"""The Speed Aspect, often based on the :py:data:`Spell.range`.

    Almost always defined as ``SpeedAspect.based_on("range")``.
    It can be provided using :py:class:`TimeAspect` as an alternative.

    (See :external:ref:`fantasy.magic.speed`.)

    ..  note::

        This aspect's name suggests it is m/s; :math:`t = \frac{d}{r}`.
        Generally, the speed (*r*) matches the distance (*d*). :math:`t=\frac{d}{d}=1`.
        Leading to a speed of "Instantaneous".

        It's always applied as a ``DistanceAspect``, with a "per-second" rate.

        What really matters is the time, which must be computed from range/speed.

    >>> from opend6_tools.magic2 import *
    >>> from types import SimpleNamespace
    >>> spell = SimpleNamespace(
    ...     range=RangeAspect("15 m"),
    ... )
    >>> based_speed = SpeedAspect.based_on("range", description="Instantaneous")
    >>> speed = based_speed(spell)
    >>> speed.difficulty()
    6
    >>> speed.description()
    'Instantaneous'
    >>> repr(speed)
    "SpeedAspect.based_on(('range',), 'Instantaneous')"
    """

    def __init__(
        self,
        measure: str | int | float | None = None,
        *,
        difficulty: int | None = None,
        **kwargs: Any,
    ) -> None:
        if difficulty is not None:
            # Created from a DerivedAspect, based on some other aspect.
            Aspect.__init__(self, difficulty, kwargs.get("description", "Instantaneous"))
            # self._difficulty = Decimal(difficulty)
            # self._description = kwargs.get("description", "Instantaneous")
            self.details = [(self._difficulty, self._description)]
        else:
            if not isinstance(measure, str):
                raise ValueError("can't parse {measure!r}")
            super().__init__(measure)
            # self._difficulty, self._description = self.parse(measure)
        self.note = kwargs.get("note", None)
        if self.note:
            self.details.append((Decimal(0), self.note))

    def __repr__(self) -> str:
        if hasattr(self, "attr_paths"):
            return f"{self.__class__.__name__}.based_on({self.attr_paths!r}, {self._description!r})"
        else:
            return (
                f"{self.__class__.__name__}(measure={self._description!r})"
                if self.note is None
                else f"{self.__class__.__name__}(measure={self._description!r}, note={self.note!r})"
            )


class DurationAspect(IncreasesDifficulty, TimeAspect):
    """The Duration Aspect implemented using :py:class:`TimeAspect`.

    (See :external:ref:`fantasy.magic.duration`.)

    >>> from opend6_tools.magic2 import *
    >>> duration = DurationAspect("1 min")
    >>> duration.difficulty()
    9
    >>> duration.description()
    '1 min'
    >>> duration.incr_decr
    <Sign.Increase: 1>
    >>> repr(duration)
    "DurationAspect('1 min')"
    """


class CastingTimeAspect(DecreasesDifficulty, TimeAspect):
    """The Casting Time Aspect implemented using :py:class:`TimeAspect`.

    (See :external:ref:`fantasy.magic.casting_time`.)

    >>> from opend6_tools.magic2 import *
    >>> casting_time = CastingTimeAspect("1 r")
    >>> casting_time.difficulty()
    4
    >>> casting_time.description()
    '1 r'
    >>> casting_time.incr_decr
    <Sign.Decrease: -1>
    >>> repr(casting_time)
    "CastingTimeAspect('1 r')"
    """


class AreaModifier(ChoiceStringPattern, Modifier):
    """
    Parse Area of Effect Unit Measures.

    >>> from opend6_tools.magic2 import *
    >>> AreaModifier().parse("2.5 m circle")
    (Decimal('5.0'), '2.5m radius circle')

    This is quite a bit more complicated than other units.

    1. The computations are not simple multiplication.

    2. Some shapes have multiple parameters.

    3. Divination

        "Look up the radius of the
        area of effect as a measure on the “Spell Measures” chart;
        double its corresponding value to get the value of the area
        of effect: divination circle aspect. Triple the “Spell Measures”
        value for three-dimensional areas."

    For now, we're using regular expression matching.
    We really should tokenize and define a higher-level grammar.
    """

    choices: dict[str, Decimal | tuple[MeasureFunc, CleanFunc]] = {
        (
            optional_group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS)))  # +|- Number
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + optional(noncap_group(either("r", "radius")))
            + zero_or_more(WHITESPACE)
            + "circle"
        ): (
            lambda m: (Decimal(m.group(1))) * 2,
            lambda m: f"{Decimal(m.group(1))}m radius circle",
        ),
        (
            optional_group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS)))  # +|- Number
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + optional(noncap_group(either("r", "radius")))
            + zero_or_more(WHITESPACE)
            + "sphere"
        ): (
            lambda m: (Decimal(m.group(1))) * 5,
            lambda m: f"{Decimal(m.group(1))}m radius sphere",
        ),
        (
            optional_group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS)))  # +|- Number
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + optional(noncap_group(either("r", "radius")))
            + zero_or_more(WHITESPACE)
            + "hemisphere"
        ): (
            lambda m: (Decimal(m.group(1))) * 5,
            lambda m: f"{Decimal(m.group(1))}m radius hemisphere",
        ),
        (
            optional_group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS)))  # +|- Number
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + optional(noncap_group(either("r", "radius")))
            + zero_or_more(WHITESPACE)
            + "divination sphere"
        ): (
            lambda m: value_from_measure(Decimal(m.group(1))) * 3,
            lambda m: f"{Decimal(m.group(1))}m radius divination sphere",
        ),
        "fluid shape": (lambda m: Decimal(6), lambda m: "fluid shape"),
        (
            group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("l", "length", "h", "height"))
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("r", "radius", "base"))
            + zero_or_more(WHITESPACE)
            + "cone"
        ): (
            lambda m: Decimal(m.group(1)) * 2 + Decimal(m.group(2)),
            lambda m: f"{Decimal(m.group(1))}m length {Decimal(m.group(2))}m radius cone",
        ),
        # Rules are vague...
        # This is a three-dimensional shape. (Volume equals
        # length times width times height.)
        #
        # Found "Cuboid with height of 1 meter and sides of 2 meters"
        # Restated "1 meter height 2 meter width and depth cuboid"
        (
            group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("h", "height"))
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("w", "width"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("and"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("d", "depth"))
            + zero_or_more(WHITESPACE)
            + "cuboid"
        ): (
            lambda m: Decimal(m.group(1)) * Decimal(m.group(2)) * Decimal(m.group(2)),
            lambda m: f"{Decimal(m.group(1))}m height {Decimal(m.group(2))}m width and depth cuboid",
        ),
        # More general form...
        (
            group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("h", "height"))
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("w", "width"))
            + zero_or_more(WHITESPACE)
            + optional(noncap_group(either("and")))
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("d", "depth"))
            + zero_or_more(WHITESPACE)
            + "cuboid"
        ): (
            lambda m: Decimal(m.group(1)) * Decimal(m.group(2)) * Decimal(m.group(3)),
            lambda m: f"{Decimal(m.group(1))}m height {Decimal(m.group(2))}m width and {Decimal(m.group(3))}m depth cuboid",
        ),
        # +1 for the first meter of length and width and +1 per
        # each additional two meters (total) of length and/or width.
        (
            group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("h", "height"))
            + zero_or_more(WHITESPACE)
            + group(one_or_more(DIGIT))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("m", "meter"))
            + zero_or_more(WHITESPACE)
            + noncap_group(either("w", "width"))
            + zero_or_more(WHITESPACE)
            + "wall"
        ): (
            lambda m: 1 + (Decimal(m.group(1)) * Decimal(m.group(2)) * Decimal("0.5")),
            lambda m: f"{Decimal(m.group(1))}m height {Decimal(m.group(2))}m width wall",
        ),
        # Some other tricky ones.
        # Blast: Area = "...1 plus the ending width, with the result multiplied
        #     by half of the length."
    }


class AreaEffectAspect(IncreasesDifficulty, AreaModifier, Aspect):
    """
    The Area of Effect Aspect.

    This can have multiple values; the spell difficulty is computed using the
    most difficult area, plus a modifier for the number of areas.

    Note "alternate shape": 3, and several alternate shapes
    are implied by a ``;`` -separated list of values.

    (See :external:ref:`fantasy.magic.area_effect`.)

    The Magic Guidebook has numerous Area of Effect rules.
    See :external:ref:`magic_guide.aspects.area_divination`,
    and :external:ref:`magic_guide.aspects.area_odd_shapes`.

    Example

    2.5m circle is difficulty 5
    3m l 1m r cone is difficulty 7
    One Alternate shape adds 1
    We *assume* the base difficulty is the most complicated shape.

    >>> from opend6_tools.magic2 import *
    >>> area_effect = AreaEffectAspect("2.5 m circle; 3m l 1m r cone")
    >>> area_effect.description()
    '2.5m radius circle; 3m length 1m radius cone; one alternate shape'
    >>> area_effect.difficulty()
    8
    >>> area_effect.details
    [(Decimal('5.0'), '2.5m radius circle'), (Decimal('7'), '3m length 1m radius cone'), (Decimal('1'), 'one alternate shape')]
    >>> repr(area_effect)
    "AreaEffectAspect('2.5m radius circle; 3m length 1m radius cone; one alternate shape')"

    >>> sandman_cone = AreaEffectAspect("3m height 3m radius cone")
    >>> sandman_cone.difficulty()
    9
    >>> sandman_cone.description()
    '3m length 3m radius cone'
    >>> repr(sandman_cone)
    "AreaEffectAspect('3m length 3m radius cone')"

    >>> wind_cone = AreaEffectAspect("8m h 4m r cone")
    >>> wind_cone.difficulty()
    20
    >>> wind_cone.description()
    '8m length 4m radius cone'
    >>> repr(wind_cone)
    "AreaEffectAspect('8m length 4m radius cone')"

    >>> portcullis_wall = AreaEffectAspect("3m h 1m w wall")
    >>> portcullis_wall.difficulty()
    2
    >>> portcullis_wall.description()
    '3m height 1m width wall'
    >>> repr(portcullis_wall)
    "AreaEffectAspect('3m height 1m width wall')"
    """

    def __init__(self, *measures: str | int | float) -> None:
        base_unit = list(self.choices.keys())[0]
        details = list(
            self.parse(detail)
            for detail in
            self.normalize_measures(base_unit, *measures)
        )
        if len(details) == 1:
            # Typical case
            super().__init__(*details[0])
            # self._difficulty, self._description = details[0]
        else:
            # Special cases for multiple alternate shapes
            if len(details) == 2:
                details += [(Decimal(1), "one alternate shape")]
            else:
                details += [(Decimal(3), "several alternate shapes")]
            d_values = [diff for diff, _ in details]
            super().__init__(max(d_values[:-1]) + d_values[-1], "; ".join(desc for _, desc in details))
            # self._description = "; ".join(desc for _, desc in details)
            # self._difficulty = max(d_values[:-1]) + d_values[-1]
        self.details = details


class TargetModifier(Modifier):
    """
    Parse Change Target Modifier.

    >>> from opend6_tools.magic2 import *
    >>> TargetModifier().parse("2 targets")
    (Decimal('10'), '2 targets')
    """

    choices = {
        "targets": 5,
        "target": 5,
        "times": 5,
    }


class ChangeTargetAspect(IncreasesDifficulty, TargetModifier, Aspect):
    """
    The Change Target Aspect.

    (See :external:ref:`fantasy.magic.change_target`.)


    >>> from opend6_tools.magic2 import *
    >>> change_target = ChangeTargetAspect("2 targets")
    >>> change_target.difficulty()
    10
    >>> change_target.description()
    '2 targets'
    >>> change_target.details
    [(Decimal('10'), '2 targets')]
    >>> repr(change_target)
    "ChangeTargetAspect('2 targets')"

    ..`todo:: This can be based_on("other_aspects.multi_target").

    """

    def __init__(self, measure: str | int | float) -> None:
        match measure:
            case str():
                pattern = (
                    one_or_more(DIGIT)
                    + one_or_more(WHITESPACE)
                    + noncap_group(either("targets|target|times"))
                )
                if match := re.search(pattern, measure, re.IGNORECASE):
                    detail = match.group(0)
                else:
                    detail = measure
                super().__init__(*self.parse(detail))
                # self._difficulty, self._description = self.parse(detail)
            case int() | float():
                super().__init__(int(measure) * 5, f"{measure} targets")
                # self._difficulty = Decimal(measure * 5)
                # elf._description = f"{measure} targets"
        self.details = [(self._difficulty, self._description)]


class ChargesUnit(Unit):
    """
    The unit for Charges.

    >>> from opend6_tools.magic2 import *
    >>> ChargesUnit().parse(5)
    (Decimal('4'), '5 charges')
    """

    choices = {
        "charges": Decimal(1),
        "improved charges": Decimal(5),
        "improved charge": Decimal(5),
    }


class ChargesAspect(IncreasesDifficulty, ChargesUnit, Aspect):
    """
    The Charges Aspect.

    (See :external:ref:`fantasy.magic.charges`.)

    (Also see :external:ref:`magic_guide.aspects.charges`.)

    ..  important::

        The Measures table is used to locate a value
        for the number of charges.

    >>> from opend6_tools.magic2 import *
    >>> charges = ChargesAspect(10)
    >>> charges.difficulty()
    5
    >>> charges.description()
    '10 charges'
    >>> repr(charges)
    "ChargesAspect('10 charges')"

    >>> ci = ChargesAspect("3 improved charges")
    >>> ci.description()
    '3 improved charges'
    >>> ci.difficulty()
    6
    >>> repr(ci)
    "ChargesAspect('3 improved charges')"

    ..  todo:: WARDS.

        1. Each condition: +10%.

        2. Optional skill to circumvent: -1 for difficulty 20
            Bigger reduction for lower difficilty.

        3. If circumvention allowed, requires speed < range.
    """

    def __init__(self, measure: str | int | float, *wards: str) -> None:
        difficulty, base_description = self.parse(measure)
        ward_text = "; ".join(wards)
        full_description = f"{base_description}, wards: {ward_text}" if wards else base_description
        super().__init__(difficulty, full_description)
        # self._description = full_description
        # self._difficulty = difficulty
        self.details = [(self._difficulty, self._description)]


class CommunityModifier(Unit):
    """
    The Number of Helpers Community Modifier.

    This is an ordinary Unit with a tweak to the value.

    >>> from opend6_tools.magic2 import *
    >>> CommunityModifier().parse("31 helpers")
    (Decimal('8'), '31 helpers')

    The example in the rules uses a Compo
    """

    choices = {
        "helpers": Decimal(1),
    }

    def value(self, measure: Decimal) -> Decimal:
        """Transform the number of helpers into a difficulty value and add 1."""
        return super().value(measure) + 1


class CommunityDifficulty(Unit):
    """
    The Number of Helpers Difficulty Modifier.

    This is an ordinary Unit with a tweak to the value.

    >>> from opend6_tools.magic2 import *
    >>> CommunityDifficulty().parse("31 helpers")
    (Decimal('14'), '31 helpers')
    """

    choices = {
        "helpers": Decimal(1),
    }

    def value(self, measure: Decimal) -> Decimal:
        """Transform the number of helpers into a value, then double it."""
        return 2 * (super().value(measure) + 1) - 2


class CommunityParticipationFactor(Factor):
    """
    The Helper Participation Community Modifier.

    >>> from opend6_tools.magic2 import *
    >>> CommunityParticipationFactor().parse("difficulty 11 action")
    (Decimal('1'), 'difficulty 11 action')
    """

    choices = {
        "simple actions": Decimal("0.5"),
        "difficulty 11 action": Decimal("1"),
        "difficulty 13 action": Decimal("1.5"),
        "difficulty 15 action": Decimal("2"),
        "difficulty 17 action": Decimal("2.5"),
        "difficulty 21 action": Decimal("3"),
    }


class CommunityAspect(DecreasesDifficulty, Aspect):
    """
    Two parts: Community Size and Difficulty Weight.

    This has two distinct effects:

    1. The Community Modifier for the spell as a whole.
        Modifiers * Helper Participation

    2. A separate difficulty applied to a mass skill roll for a large community given their skills and the inherent difficulty of the task.
       (Used for groups of NPC's.)

    Further, there will be a CommunityModifier Unit,
    a CommunityDiffiultyUnit, **and** a CommunityParticipationFactor Factor.
    This means all three Lookup instances need to touch the measures.

    (See :external:ref:`fantasy.magic.community`.)


    >>> from opend6_tools.magic2 import *
    >>> community = CommunityAspect("31 helpers", "Simple actions")
    >>> community.difficulty()
    4
    >>> community.description()
    '31 helpers; simple actions'
    >>> repr(community)
    "CommunityAspect('31 helpers', 'simple actions')"
    """

    def __init__(self, *measures: str | int | float) -> None:
        difficulty = CommunityModifier()
        community_factor = CommunityParticipationFactor()
        details = []
        factors = []
        for measure in self.normalize_measures("", *measures):
            try:
                details.append(difficulty.parse(measure))
            except ValueError:
                factors.append(community_factor.parse(measure))
        if len(factors) != 1:
            raise ValueError("one action difficulty required")
        else:
            weight, _ = factors[0]
        super().__init__(
            sum(diff for diff, _ in details) * Decimal(weight),
            "; ".join(desc for _, desc in details + factors)
        )
        # self._difficulty = sum(diff for diff, _ in self.details) * Decimal(weight)
        # self._description = "; ".join(desc for _, desc in self.details + self.factors)
        self.details = details + factors

    def __repr__(self) -> str:
        text = [repr(desc) for _, desc in self.details]
        return f"{self.__class__.__name__}({', '.join(text)})"


class ComponentsModifier(Modifier):
    """
    How rare is the component?

    >>> from opend6_tools.magic2 import *
    >>> ComponentsModifier().parse("common")
    (Decimal('3'), 'common')
    """

    choices = {
        "ordinary": 1,
        "very common": 2,
        "common": 3,
        "uncommon": 4,
        "rare": 4,
        "very rare": 5,
        "extremely rare": 6,
        "unique": 7,
    }


class ComponentsFactor(Factor):
    """
    How many distinct components? Is/Are they destroyed or consumed?

    >>> from opend6_tools.magic2 import *
    >>> ComponentsFactor().parse("destroyed")
    (Decimal('2'), 'destroyed')

    """

    choices = {
        "1-3 components": Decimal(1),
        "4-6 components": Decimal("0.75"),
        "7 or more components": Decimal("0.5"),
        "destroyed": Decimal(2),
    }


class ComponentsAspect(DecreasesDifficulty, Aspect):
    """
    The Components Aspect, based on Rarity, Quantity, and Consumabiity of the components.

    (See :external:ref:`fantasy.magic.components`.)

    >>> from opend6_tools.magic2 import *
    >>> components = ComponentsAspect("something", "uncommon; destroyed")
    >>> components.difficulty()
    8
    >>> components.description()
    'something (uncommon; destroyed)'
    >>> repr(components)
    "ComponentsAspect('something', 'uncommon')"
    """

    def __init__(self, note: str, *measures: str | int | float) -> None:
        difficulty = ComponentsModifier()
        component_factor = ComponentsFactor()
        self.details = [(Decimal(0), note)]
        self.factors = []
        for measure in self.normalize_measures("", *measures):
            try:
                self.details.append(difficulty.parse(measure))
            except ValueError:
                self.factors.append(component_factor.parse(measure))
        weight = math.prod(diff for diff, _ in self.factors)
        super().__init__(
            sum(diff for diff, _ in self.details) * weight,
            f"{note} ({'; '.join(desc for _, desc in self.details[1:] + self.factors)})"
        )
        # self._difficulty = Decimal(sum(diff for diff, _ in self.details) * weight)
        # self._description = (
        #    f"{note} ({'; '.join(desc for _, desc in self.details[1:] + self.factors)})"
        # )

    def __repr__(self) -> str:
        text = [repr(desc) for _, desc in self.details]
        return f"{self.__class__.__name__}({', '.join(text)})"


class ConcentrationAspect(DecreasesDifficulty, TimeAspect):
    """
    Concentration time.
    Frequently ``ConcentrationAspect.based_on("casting_time")``
    Alternative ``ConcentrationAspect("3 sec", note="willpower difficulty 9")``, requires casting_time be >= 3sec

    Also derives a distraction roll as part of the description.
    "mettle roll difficulty = {6+modifier}"

    (See :external:ref:`fantasy.magic.concentration`.)

    ..  todo:: Concentration distractions modifier for derived distraction roll.

    >>> from opend6_tools.magic2 import *
    >>> spell = SimpleNamespace(casting_time=CastingTimeAspect("5 sec"))
    >>> concentration_based = ConcentrationAspect.based_on("casting_time")
    >>> concentration = concentration_based(spell)
    >>> concentration.difficulty()
    4
    >>> concentration.description()
    'Concentration: 5 sec (mettle roll difficulty 10)'
    >>> repr(concentration)
    "ConcentrationAspect('5 sec')"

    >>> c_2 = ConcentrationAspect("25 sec", modifier=2)
    >>> c_2.difficulty()
    5
    >>> c_2.description()
    'Concentration: 25 sec (mettle roll difficulty 11)'
    >>> repr(c_2)
    "ConcentrationAspect('25 sec', modifier=2)"
    """

    def __init__(
        self,
        measure: str | int | float | None = None,
        modifier: int = 0,
        note: str | None = None,
        *,
        difficulty: int | None = None,
        source: str | None = None,
        **kwargs: Any,
    ) -> None:
        if difficulty is not None:
            # Based-on will provide difficulty and source directly.
            self.measure = source
            Aspect.__init__(self, difficulty, f"Concentration: {source} (mettle roll difficulty {difficulty + 6})")
            # self._difficulty = Decimal(difficulty)
            # self._description = (
            #     f"Concentration: {source} (mettle roll difficulty {self._difficulty + 6})"
            # )
            self.modifier = modifier
            self.note = note or ""
        else:
            # Measure provides difficulty and a note.
            # Optional modifier to set higher difficulty than duration measure
            if not isinstance(measure, str):
                raise ValueError("can't parse {measure!r}")
            # self.modifier = modifier
            assert not kwargs, f"unknown {kwargs}"
            value, measure = self.parse(measure)
            note = kwargs.get("note")
            computed_diff = int((value / Decimal("3.0") + modifier).quantize(
                Decimal(1), rounding=decimal.ROUND_UP))
            all_notes = [f"mettle roll difficulty {computed_diff + 6}"] + (
                [note] if note else []
            )
            # self._difficulty = (value / Decimal("3.0") + self.modifier).quantize(
            #     Decimal("1."), rounding=decimal.ROUND_UP
            # )
            # self._description = f"Concentration: {self.measure} ({'; '.join(all_notes)})"
            Aspect.__init__(self, computed_diff, f"Concentration: {measure} ({'; '.join(all_notes)})"
            )
            self.measure = measure
            self.note = note
            self.modifier = modifier
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        body = [f"{self.measure!r}"]
        if self.modifier:
            body.append(f"modifier={self.modifier!r}")
        if self.note:
            body.append(f"note={self.note!r}")
        return f"{self.__class__.__name__}({', '.join(body)})"


class CountenanceModifier(Modifier):
    """
    Modifier for Countenance.

    >>> from opend6_tools.magic2 import *
    >>> CountenanceModifier().parse("extreme")
    (Decimal('2'), 'extreme')
    """

    choices = {"noticeable": 1, "extreme": 2}


class CountenanceAspect(DecreasesDifficulty, CountenanceModifier, Aspect):
    """
    Countenance Aspect

    (See :external:ref:`fantasy.magic.countenance`.)

    >>> from opend6_tools.magic2 import *
    >>> countenance = CountenanceAspect("red eyes", "noticeable")
    >>> countenance.difficulty()
    1
    >>> countenance.description()
    'red eyes (noticeable)'
    >>> repr(countenance)
    "CountenanceAspect('red eyes', 'noticeable')"
    """

    def __init__(self, note: str, measure: str | int | float) -> None:
        difficulty, measure = self.parse(measure)
        super().__init__(difficulty, f"{note} ({measure})")
        # self._difficulty, measure = self.parse(measure)
        # self._description = f"{note} ({measure})"
        self.note = note
        self.measure = measure
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.note!r}, {self.measure!r})"
            if self.note
            else f"{self.__class__.__name__}({self.measure!r})"
        )


class FeedbackAspect(DecreasesDifficulty, Modifier, Aspect):
    """
    Lowered resistance against feedback.
    This uses the modifier value directly, it's not a ``DieUnit``.

    The description includes the damage resistance change.

    (See :external:ref:`fantasy.magic.feedback`.)

    >>> from opend6_tools.magic2 import *
    >>> feedback = FeedbackAspect(3)
    >>> feedback.difficulty()
    3
    >>> feedback.description()
    '3 lowered resistance'
    >>> repr(feedback)
    'FeedbackAspect(3)'
    """

    def __init__(self, measure: str | int | float) -> None:
        difficulty, measure = self.parse(measure)
        super().__init__(difficulty, f"{measure} lowered resistance")
        # self._difficulty, self._description = self.parse(measure)
        # self._description += " lowered resistance"
        self.measure = measure
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.measure})"


class FocusedAspect(IncreasesDifficulty, Aspect):
    """
    Focused aspect. Merely has to be present.
    Always use ``FocusedAspect.based_on(("effect", "duration"))``

    Difficulty is computed from (effect + duration)/5.

    (See :external:ref:`fantasy.magic.focused`.)

    >>> from opend6_tools.magic2 import *
    >>> based_focused = FocusedAspect.based_on(("effect", "duration"))
    >>> spell = SimpleNamespace(effect=DamageEffect("Damage", "5D"), duration=DurationAspect("10 sec"))
    >>> focused = based_focused(spell)
    >>> focused.difficulty()
    4
    >>> focused.description()
    'Focused'
    >>> repr(focused)
    "FocusedAspect.based_on(('effect', 'duration'), target='Focused')"

    ..  todo:: Multi_target weighting for Focused

    """

    def __init__(self, *, difficulty: int, source: str, target: str = "") -> None:
        super().__init__(difficulty // 5, f"Focused on {target}" if target else "Focused")
        # self._difficulty = Decimal(difficulty) // 5
        # self._description = f"Focused on {target}" if target else "Focused"


class GesturesModifier(Modifier):
    """Gestures modifier

    >>> from opend6_tools.magic2 import *
    >>> GesturesModifier().parse("simple")
    (Decimal('2'), 'simple')
    """

    choices = {
        "very simple": 1,
        "simple": 2,  # was "fairly simple"
        "complex": 3,
        "very complex": 4,
        "extremely complex": 5,
        "challenging": 6,
        "offensive": 1,
        "difficulty 23": 17,
    }


class GesturesAspect(DecreasesDifficulty, GesturesModifier, Aspect):
    """Gestures Aspect

    (See :external:ref:`fantasy.magic.gesture`.)

    >>> from opend6_tools.magic2 import *
    >>> gestures = GesturesAspect("waves hands", "simple; offensive")
    >>> gestures.difficulty()
    3
    >>> gestures.description()
    'waves hands (simple; offensive)'
    >>> repr(gestures)
    "GesturesAspect('waves hands', 'simple', 'offensive')"

    >>> gestures2 = GesturesAspect("complex hand-dance", "complex (difficulty 11)")
    >>> gestures2.difficulty()
    3
    >>> gestures2.description()
    'complex hand-dance (complex (difficulty 11))'
    >>> repr(gestures2)
    "GesturesAspect('complex hand-dance', 'complex (difficulty 11)')"
    """

    def __init__(self, note: str, *measures: str | int | float) -> None:
        self.note = note
        base_unit = list(self.choices.keys())[0]
        details = [(Decimal(0), note)] + [
            self.parse(detail) for detail in self.normalize_measures(base_unit, *measures)
        ]
        qualifiers = "; ".join(desc for _, desc in details[1:])
        super().__init__(sum(diff for diff, _ in details), f"{note} ({qualifiers})")
        # self._description = f"{note} ({qualifiers})"
        # self._difficulty = Decimal(sum(diff for diff, _ in self.details))
        self.details = details

    def __repr__(self) -> str:
        text = [repr(desc) for _, desc in self.details]
        return f"{self.__class__.__name__}({', '.join(text)})"


class IncantationsModifier(Modifier):
    """
    Modifiers for Incantations complexity.

    >>> from opend6_tools.magic2 import *
    >>> IncantationsModifier().parse("litany")
    (Decimal('4'), 'litany')
    """

    choices = {
        "word": 1,
        "short": 1,
        "phrase": 1,
        "lengthy": 2,
        "sentence": 2,
        "complex": 3,
        "litany": 4,
        "complex formula": 5,
        "extensive and complex": 6,
        "foreign tongue": 1,
        "loud": 1,
        "offensive": 1,
    }


class IncantationsAspect(DecreasesDifficulty, IncantationsModifier, Aspect):
    """Incantations aspect.
    For complex, and foreign, there's a difficulty roll involved.
    This is currently not computed.

    (See :external:ref:`fantasy.magic.incantation`.)

    ..  todo:: Compute additional difficulty roll.

    >>> from opend6_tools.magic2 import *
    >>> incantations = IncantationsAspect("Die, scum", 'phrase; loud; offensive')
    >>> incantations.difficulty()
    3
    >>> incantations.description()
    'Die, scum (phrase; loud; offensive)'
    >>> repr(incantations)
    "IncantationsAspect('Die, scum', 'phrase', 'loud', 'offensive')"
    """

    def __init__(self, note: str, *measures: str | int | float) -> None:
        self.note = note
        base_unit = list(self.choices.keys())[0]
        details = [(Decimal(0), note)] + [
            self.parse(detail) for detail in self.normalize_measures(base_unit, *measures)
        ]
        qualifiers = "; ".join(desc for _, desc in details[1:])
        super().__init__(sum(diff for diff, _ in details), f"{note} ({qualifiers})")
        # self._description = f"{note} ({qualifiers})"
        # self._difficulty = Decimal(sum(diff for diff, _ in details))
        self.details = details

    def __repr__(self) -> str:
        text = [repr(desc) for _, desc in self.details]
        return f"{self.__class__.__name__}({(', ').join(text)})"


class MultiTargetsModifier(Modifier):
    """
    Parse Multi-Target Modifier.

    >>> from opend6_tools.magic2 import *
    >>> MultiTargetsModifier().parse("3 targets")
    (Decimal('9'), '3 targets')
    """

    choices = {"targets": 3}


class MultipleTargetAspect(IncreasesDifficulty, MultiTargetsModifier, Aspect):
    """Multi-target aspect.

    (See :external:ref:`fantasy.magic.multi_target`.)

    >>> from opend6_tools.magic2 import *
    >>> multi_target = MultipleTargetAspect("3 targets")
    >>> multi_target.difficulty()
    9
    >>> multi_target.description()
    '3 targets'
    >>> repr(multi_target)
    "MultipleTargetAspect('3 targets')"
    """

    def __init__(self, measure: str | int | float) -> None:
        super().__init__(*self.parse(measure))
        # self._difficulty, self._description = self.parse(measure)
        self.details = [(self._difficulty, self._description)]


class UnrealFactor(Factor):
    """
    Factor for disbelief in an unreal effect.

    >>> from opend6_tools.magic2 import *
    >>> UnrealFactor().parse("difficulty 9")
    (Decimal('0.5'), 'difficulty 9')
    """

    choices = {
        "difficulty 0": Decimal("0.75"),
        "difficulty 9": Decimal("0.5"),
        "difficulty 13": Decimal("0.25"),
    }


class UnrealEffectAspect(DecreasesDifficulty, UnrealFactor, Aspect):
    """
    For Illusions (i.e., Unreal Effect).
    Always use ``UnrealEffectAspect.based_on("effect", "difficulty n")``

    This depends on spell ``effect`` and a difficulty factor.
    Computes the Spell effect; weighted by the factor,
    This value is the difficulty adjustment for this aspect.

    (See :external:ref:`fantasy.magic.unreal_effect`.)


    >>> from opend6_tools.magic2 import *
    >>> unreal_effect_based = UnrealEffectAspect.based_on("effect", "difficulty 9")
    >>> spell = SimpleNamespace(effect=Effect("Whatever", 8))
    >>> unreal_effect = unreal_effect_based(spell)
    >>> unreal_effect.difficulty()
    4
    >>> unreal_effect.description()
    'unreal; disbelief difficulty 9'
    >>> repr(unreal_effect)
    "UnrealEffectAspect.based_on(('effect',), target='unreal; disbelief difficulty 9')"
    """

    def __init__(self, measure: str | int | float, difficulty: int, source: str) -> None:
        self.factor, base_description = self.parse(measure)
        super().__init__((difficulty * self.factor).quantize(1),  "unreal; disbelief " + base_description)
        # self._description = "unreal; disbelief " + base_description
        # elf._difficulty = (difficulty * self.factor).quantize(1)
        self.details = [(self._difficulty, self._description)]


class VariableDurationModifier(Modifier):
    """
    A number of modifiers for duration.

    >>> from opend6_tools.magic2 import *
    >>> VariableDurationModifier().parse("on/off switch")
    (Decimal('8'), 'on/off switch')
    """

    choices = {
        "off-only": 4,
        "on/off switch": 8,
    }


class VariableDurationAspect(IncreasesDifficulty, Aspect):
    """
    Several modifier options to end a spell early, turn a spell on and off.
    Also, a Duration option via ``TimeUnit``

    (See :external:ref:`fantasy.magic.variable_duration`.)

    >>> from opend6_tools.magic2 import *
    >>> vd = VariableDurationAspect("on/off switch")
    >>> vd.difficulty()
    8
    >>> vd.description()
    'on/off switch'
    >>> repr(vd)
    "VariableDurationAspect('on/off switch')"
    """

    def __init__(self, *measures: str | int | float) -> None:
        modifier = VariableDurationModifier()
        duration = TimeUnit()
        details = []
        for measure in self.normalize_measures("", *measures):
            # TODO: We want some kind of using(modifier, duration).parse(measure)
            try:
                details.append(modifier.parse(measure))
            except ValueError:
                details.append(duration.parse(measure))

        super().__init__(sum(diff for diff, _ in details), "; ".join(desc for _, desc in details))
        # self._difficulty = Decimal(sum(diff for diff, _ in self.details))
        # self._description = "; ".join(desc for _, desc in self.details)
        self.details = details


class VariableEffectAspect(IncreasesDifficulty, Aspect):
    """
    Allows spell effects to be increased (or decreased.)

    +1 for every pip or point per direction per effect.

    See :external:ref:`fantasy.magic.variable_effect`.

    >>> from opend6_tools.magic2 import *
    >>> ve = VariableEffectAspect("Can increase", 10)
    >>> ve.difficulty()
    10
    >>> ve.description()
    'Can increase'
    >>> repr(ve)
    "VariableEffectAspect('Can increase', Decimal('10'))"
    """

    def __init__(self, description: str, difficulty: int) -> None:
        super().__init__(difficulty, description)
        # self._difficulty = Decimal(difficulty)
        # self._description = description
        self.details = [(self._difficulty, self._description)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._description!r}, {self._difficulty!r})"


class VariableMovementModifier(Modifier):
    """
    A number of modifiers for movement of the spell target.

    >>> from opend6_tools.magic2 import *
    >>> VariableMovementModifier().parse("accuracy bonus")
    (Decimal('2'), 'accuracy bonus')
    """

    choices = {
        "accuracy bonus": 2,
        "bend around smaller": 1,
        "bend around same size": 3,
        "find invisible": 4,
        "target invisible": 4,
    }


class VariableMovementAspect(IncreasesDifficulty, Aspect):
    """
    A number of modifiers to move the target of a spell.

    Accuracy and Bending modifiers from Variable Movement.
    A Speed option via ``DistanceUnit``

    (See :external:ref:`fantasy.magic.variable_movement`.)


    >>> from opend6_tools.magic2 import *
    >>> variable_movement = VariableMovementAspect("bend around same size")
    >>> variable_movement.difficulty()
    3
    >>> variable_movement.description()
    'bend around same size'
    >>> repr(variable_movement)
    "VariableMovementAspect('bend around same size')"

    >>> variable_movement_spd = VariableMovementAspect("5m")
    >>> variable_movement_spd.difficulty()
    5
    >>> variable_movement_spd.description()
    '5 m per second'
    >>> repr(variable_movement_spd)
    "VariableMovementAspect('5 m per second')"

    ..  todo:: Should have DistUnit as a Mixin.
    """

    def __init__(self, *measures: str | int | float) -> None:
        modifier = VariableMovementModifier()
        speed = DistUnit()
        details = []
        for measure in self.normalize_measures("", *measures):
            try:
                details.append(modifier.parse(measure))
            except ValueError:
                diff, desc = speed.parse(measure)
                details.append((diff + 1, desc + " per second"))
        super().__init__(sum(diff for diff, _ in details), "; ".join(desc for _, desc in details))
        # self._difficulty = Decimal(sum(diff for diff, _ in self.details))
        # self._description = "; ".join(desc for _, desc in self.details)
        self.details = details


class ArcaneKnowledgeAspect(GenericAspect):
    """
    This is generally zero-cost. It's more like the skill characteristic of a Spell,
    not a proper aspect.

    (See :external:ref:`magic_guide.skills.arcane_knowledge`, in the "Magic Guide.")

    >>> from opend6_tools.magic2 import *
    >>> arcane = ArcaneKnowledgeAspect(description="dimension, time", difficulty=0)
    >>> arcane.difficulty()
    0
    >>> arcane.description()
    'Arcane Knowledge: dimension, time'
    >>> repr(arcane)
    "ArcaneKnowledgeAspect(Decimal('0'), 'dimension, time')"
    """

    def __init__(self, difficulty: int | str = "", description: str = "") -> None:
        """
        Defines an Arcane Knowledge area

        :param difficulty: Difficulty value, generally omitted.
        :param description:  The arcane knowledge.
        """
        try:
            super().__init__(int(difficulty), description)
            # self._difficulty = Decimal(difficulty)
            # self._description = description
        except (ValueError, decimal.InvalidOperation):
            super().__init__(0, str(difficulty))
            # self._difficulty = Decimal(0)
            # self._description = str(difficulty)
        self.details = [(self._difficulty, self._description)]

    def description(self) -> str:
        """Summarize the arcane knowledge requirement."""
        return f"Arcane Knowledge: {self._description}"


## Part IV -- Spell.


class OtherAspects(TypedDict, total=False):
    """
    A typed dictionary that provides a list of
    key names for the :py:data:`Spell.other_aspects` mapping.

    Note, numerous aliases are present.
    This makes it slightly easier to convert text
    to a Spell. It also leads to some minor inconsistencies.

    (See :external:ref:`fantasy.magic.other_aspects`.)
    """

    # Positive Modifiers -- Increase Difficulty
    area_of_effect: "AreaEffectAspect"  # unique units: sphere, circle, etc.
    area_effect: "AreaEffectAspect"  # unique units: sphere, circle, etc.
    change_target: "ChangeTargetAspect"
    charges: "ChargesAspect"
    focused: "FocusedAspect"  # Always ``.based_on(("effect", "duration"))``
    focus: "FocusedAspect"
    multiple_targets: "MultipleTargetAspect"
    multi_target: "MultipleTargetAspect"
    variable_duration: "VariableDurationAspect"
    variable_effect: "VariableEffectAspect"
    variable_movement: "VariableMovementAspect"
    other_alterants: "GenericAspect"
    other_alterant: "GenericAspect"

    # Negative Modifiers -- Decrease Difficulty
    community: "CommunityAspect"
    component: "ComponentsAspect"
    components: "ComponentsAspect"
    concentration: "ConcentrationAspect"
    countenance: "CountenanceAspect"
    feedback: "FeedbackAspect"
    gesture: "GesturesAspect"
    gestures: "GesturesAspect"
    incantation: "IncantationsAspect"
    incantations: "IncantationsAspect"
    unreal_effect: "UnrealEffectAspect"  # i.e., Illusory
    arcane_knowledge: "ArcaneKnowledgeAspect"


class Spell:
    """
    Definition of a spell: an Effect and a collection of Aspects.

    Per the rules, a spell has 8 characterstics.
    See :external:ref:`fantasy.magic.characteristics`.
    This isn't enough for a complete data model, but it does help clarify intent.
    These are the charactestics defined in the rules:

    :skill:
        The essential skill used. Sometimes, this can be deduced from the effect.

    :dificulty:
        Computed from the effect and aspects.

    :effect:
        An instance of one of the :py:class:`Effect` subclasses.

    :duration:
        An instance of the :py:class:`DurationAspect` class.

    :range:
        An instance of the :py:class:`RangeAspect` class.

    :speed:
        An instance of the :py:class:`SpeedAspect` class.

    :casting_time:
        An instance of the :py:class:`CastingTimeAspect` class.

    :other_aspects:
        A mapping of aspect names to
        one of the :py:class:`Aspect` subclasses.
        Ideally, an instance of the :py:class:`OtherAspects` typed dictionary.

    This implementation adds three more essential characteristics,
    not named in the rules:

    :name:
        String

    :notes:
        String

    :other_conditions:
        A list of :py:class:`GenericAspect` instances with additional details.

    Example

    >>> from opend6_tools.magic2 import *

    >>> example = Spell(
    ...     name="Example",
    ...     notes="GIVEN Example spell WHEN difficulty THEN 4",
    ...     effect=SkillEffect("Acumen: testing", "+4D"),
    ...     duration=DurationAspect("1 sec"),
    ...     range=RangeAspect("1m"),
    ...     casting_time=CastingTimeAspect("5 sec"),
    ...     speed=SpeedAspect.based_on("range", description="Instantaneous"),
    ...     other_aspects = {},
    ...     other_conditions = [GenericAspect(1, "Everything else is completed")],
    ... )
    >>> example.difficulty
    4

    Most Spells are self-contained.
    The :py:class:`Effect` and each :py:class:`Aspect` have a distinct difficulty computation.

    There are two complications:

    -   Some :py:class:`Aspect` may depend on one or more other :py:class:`Aspect` definitions (or the :py:class:`Effect`) of this Spell instance.

    -   Spells an :py:class:`Effect` or :py:class:`Aspect` that depends on another Spell (or a creature or a thing.)

    It helps to treat dependency as the base case,
    and a self-contained Aspect as well as an entirely self-contained Spell
    as a kind of degenerate case.

    Example.

    ..  code-block:: python

        sT = Spell(
            name="Template",
            effect=SomeEffect.based_on_spell(attr_paths="effect" or "aspect" or "difficulty"),
            aspect=AnotherEffect.based_on(attr_paths="effect"),
        )

        s1 = Spell(
            name="1",
            effect=RealEffect("skill", "5D6")
        )

        s1.finalize()
        sT_1 = sT.finalize(using=s1)

    There are two distinct ways to define these dependencies:

    -   Use an Aspect's :py:meth:`Aspect.based_on` class method to get the difficulty from aspects or effect of **this** spell.

    -   Use an Aspect's :py:meth:`Aspect.based_on_spell` to get one or more attribute difficulties (or effect difficulty or overall difficulty) from another spell.

    ..  note:: Finalization Details

        A :py:meth:`TemplateSpell.__init__` cannot invoke :py:meth:`Spell.finalize` implicitly.
        It must stage the aspects. The finalize processing **requires** details to complete the template.
        In some cases it's details of another spell.
        In other cases, it's details of a summoned or created creature.

        Generally, the :py:meth:`Spell.finalize` method works out the internal dependency total order.
        It must also be given any external values (i.e. Spells or whatever)
        required to create the effect and aspects.

        Note that self-contained spells must invoke :py:meth:`Spell.finalize`.
        The ``using`` value, however, will be ignored.
    """

    # A logger for debugging difficulty computations.
    logger: ClassVar[logging.Logger] = logging.getLogger("Spell")
    core_attr: ClassVar[tuple[str, ...]] = (
        "effect",
        "duration",
        "range",
        "casting_time",
        "speed",
    )

    # Dataclass-like feature: a list of field names and class-level definitions for type-checkers.
    field_names: ClassVar[tuple[str, ...]] = (
        "name",
        "notes",
        "skill",
        "effect",
        "duration",
        "casting_time",
        "range",
        "speed",
        "other_aspects",
        "other_conditions",
    )

    # Set by finalize()
    name: str
    notes: str
    skill: str
    effect: Effect
    duration: DurationAspect
    casting_time: CastingTimeAspect
    range: RangeAspect
    speed: SpeedAspect
    other_aspects: OtherAspects
    other_conditions: list[Aspect]

    def __init__(
        self,
        *,
        name: str,
        effect: Effect,
        notes: str = "",
        skill: str = "",
        **aspects: "Aspect | dict[str, Aspect] | list[Aspect]",
    ) -> None:
        """
        Definition of a Spell

        :param name: The name
        :param notes: Additional notes
        :param skill: The core skill required
        :keyword aspects: All :py:class:`Aspect` and :py:class:`Effect` values.
        """
        self.name = name
        self.notes = notes
        self.skill = skill
        self.effect = effect
        # Source aspects; input to finalize().
        self.aspects: dict[str, Aspect | dict[str, Aspect] | list[Aspect]] = aspects

        # Other Attributes will be set by finalize()
        self._finalize = False
        self._difficulty: int
        self._difficulty_note = ""

    def finalize(
        self,
        *,
        using: "Spell | None" = None,
        other_aspects: dict[str, Aspect] | None = None,
    ) -> Self:
        """
        Set the individual attributes of the Spell (or Miracle.)

        There are three kinds of Aspects:

        -   Fully defined.

        -   Based on other aspects of **this** Spell.

        -   Based on aspects of another Spell.

        Computation of Spell difficulty value is two steps.

        1.  Compute a total ordering among the Aspects.
            This will place the fully-defined Aspects first, and the dependent Aspects last.

        2.  Compute Aspect difficulty value.

        ..  note::

            This processing may be a distinct ``SpellBuilder`` class,
            distinct from an ordinary ``Spell`` container.

        :param using: Another spell to use for effect and aspect computations.
        :param other_aspects: Values for ``other_aspects`` to be folded into a template Spell (or Miracle.)
        """
        # Reset state
        for name in ("_difficulty", "other_aspects", "other_conditions"):
            if hasattr(self, name):
                delattr(self, name)
        self._finalize = True

        # Flatten the core aspects, given other_aspects, and parameter other_aspects folded
        flat_aspects = {
            name: cast(Aspect, value)
            for name, value in self.aspects.items()
            if name not in {"other_aspects", "other_conditions"}
        } | cast(dict[str, Aspect], self.aspects.get("other_aspects") or {}).copy()
        for name, new_aspect in (other_aspects or {}).items():
            if name in flat_aspects:
                match flat_aspects[name]:
                    case CompositeAspect():
                        flat_aspects[name].append(new_aspect)
                    case _:
                        flat_aspects[name] = CompositeAspect(flat_aspects[name], new_aspect)
            else:
                flat_aspects[name] = new_aspect

        # Enumerate the dependencies for Derived Aspects
        dependencies = {
            name: () for name, value in flat_aspects.items() if not isinstance(value, DerivedAspect)
        } | {
            name: value.attr_paths
            for name, value in flat_aspects.items()
            if isinstance(value, DerivedAspect)
        }

        # Compute the ordering, if possible
        do_derivation = True
        try:
            ordering = list(graphlib.TopologicalSorter(dependencies).static_order())
        except graphlib.CycleError as ex:
            self.logger.error("template without a dependent spell (%s): {%r}", ex, self.name)
            ordering = dependencies
            do_derivation = False
            self._difficulty_note = (
                "Template spell without a concrete dependency -- difficulty can't be computed."
            )

        # Set the visible attributes
        for name in ordering:
            match flat_aspects[name]:
                case DerivedAspect() as derived if do_derivation:
                    # Compute new aspect or effect
                    aspect_or_effect = derived(self)
                case _ as selfcontained:
                    # Use as-is
                    aspect_or_effect = selfcontained
            # Assign to top-level attributes, other_aspects, and other_conditions.
            # Clean out self.aspects to update internal state.
            if name in self.aspects:
                setattr(self, name, aspect_or_effect)
            else:
                if not hasattr(self, "other_aspects"):
                    self.other_aspects = OtherAspects()
                self.other_aspects[name] = aspect_or_effect

        if not hasattr(self, "other_aspects"):
            # Put in an empty one.
            self.other_aspects = OtherAspects()
        if "other_conditions" in self.aspects:
            self.other_conditions = cast(list[Aspect], self.aspects["other_conditions"])
        else:
            self.other_conditions = []

        # Ideally, self.aspects is empty.

        if not self.skill:
            # Can only be done after the effect is present.
            self.skill = self.effect.skill()

        return self

    @property
    def difficulty(self) -> int:
        r"""
        Compute the difficulty from two groups of Aspects:
        exacerbators, :math:`E`, alleviators, :math:`A`.
        The alleviators are called Negative Modifiers (NM) in the rulebook.

        ..  math::

            d = \frac{\sum E - \sum A}{2}

        There are two groups of aspects:

        1.  **Exacerbation**: Effect, Range, Speed, Duration.
            Others: area of effect, change target, charges, focused,
            multiple targets, variable effect, variable movement, variable duration,
            and any other Alterants.

        2.  **Alleviation**: Casting Time.
            Others: Community, Components, Concentration, Countenance, Feedback,
            Gesture, Incantation, Unreal Effect, any other Conditions.

        Confusingly, the signs in the published rules appear to be all over the map.
        All difficulty modifier values *should* be unsigned;
        it's the Exacerbation/Alleviation nature of the Aspect that matters.

        This sets the ``self._difficulty`` cache value.

        This may invoke :py:meth:`Spell.finalize` if needed.
        In the common case, where a Spell has no external dependencies,
        this will compute the aspects implicitly.
        In the rare case of a template spell, the :py:meth:`Spell.finalize` method
        **must** be invoked manually to provide the external details.

        :return: Computed Difficulty
        """
        if hasattr(self, "_difficulty"):
            # Return the cached value.
            return self._difficulty

        self.logger.debug("Difficulty of %s", self.name)
        if not self._finalize:
            # If it hasn't yet been finalized, finalize().
            # For simple self-contained spells, this works.
            # For template spells, we don't want to undo an explicit finalize.
            self.finalize()

        # Flat map of all aspects.
        aspects: dict[str, Aspect] = (
            {
                name: cast(Aspect, getattr(self, name))
                for name in Spell.core_attr
                if hasattr(self, name)
            }
            | cast(dict[str, Aspect], self.other_aspects)
            | {f"condition: {oc.summary()}": oc for n, oc in enumerate(self.other_conditions)}
        )

        # Total difficulty -- effect and exacerbating attributes with Sign.Increase
        self._spell_total = {
            name: abs(aspect.difficulty())
            for name, aspect in aspects.items()
            if aspect and aspect.incr_decr == Sign.Increase
        }
        self.logger.debug(
            "  Spell Total        %r = %d",
            self._spell_total,
            sum(self._spell_total.values()),
        )

        # Negative modifiers -- alleviating attributes with Sign.Decrease
        self._negative_modifiers = {
            name: abs(aspect.difficulty())
            for name, aspect in aspects.items()
            if aspect and aspect.incr_decr == Sign.Decrease
        }
        self.logger.debug(
            "  Negative Modifiers %r = %d",
            self._negative_modifiers,
            sum(self._negative_modifiers.values()),
        )

        # difficulty is (exacebation - alleviation) / 2.
        tot = sum(self._spell_total.values()) - sum(self._negative_modifiers.values())
        d = int(0.5 + (tot / 2))
        self.logger.debug(
            "  Difficulty ⎡(%d - %d) ÷ 2⎤ = ⎡%.1f⎤ = %d",
            sum(self._spell_total.values()),
            sum(self._negative_modifiers.values()),
            tot / 2,
            d,
        )
        self._difficulty = d
        return d

    def __repr__(self) -> str:
        try:
            attrs = [
                f"{name}={getattr(self, name)!r}"
                for name in ("effect", "duration", "range", "casting_time", "speed")
                if hasattr(self, name)
            ]
            return (
                f"{self.__class__.__name__}("
                f"name={self.name!r}, "
                f"skill={self.skill!r}, "
                f"notes={self.notes!r}, "
                f"{', '.join(attrs)}, "
                f"other_aspects={self.other_aspects!r}, "
                f"other_conditions={self.other_conditions!r}, "
                f")"
            )
        except AttributeError:
            return (
                f"{self.__class__.__name__}("
                f"name={self.name!r}, "
                f"skill={self.skill!r}, "
                f"aspects=*{self.aspects!r}"
                f")"
            )

    def __eq__(self, other: Any) -> bool:
        match other:
            case Spell() as other_spell:
                self_attrs = set(filter(lambda n: hasattr(self, n), self.field_names))
                other_attrs = set(filter(lambda n: hasattr(other, n), self.field_names))
                same = self_attrs == other_attrs and all(
                    getattr(other_spell, name) == getattr(self, name) for name in self_attrs
                )
                return same
            case _:
                return NotImplemented

    def _asdict(self) -> dict[str, Any]:
        """
        Emit details of this spell (and all of the aspects) for a TOML dump.

        ..  todo:: Finish TOML dump of a spell.
        """

        def items_iter() -> Iterator[tuple[str, Any]]:
            for name in self.field_names:
                if hasattr(self, name):
                    value = getattr(self, name)
                    match value:
                        case Aspect():
                            yield name, value._asdict()
                        case dict():
                            yield name, {key: oa._asdict() for key, oa in value.items()}
                        case list():
                            yield name, [oc._asdict() for oc in value]
                        case _:
                            yield name, value

        return dict(items_iter())


class Miracle(Spell):
    """A subclass of :py:class:`Spell` for Invocations."""

    pass


Cantrip = Spell

## Part V -- Reporting and Display


class TableSummary:
    """Summarize a Spell (or Miracle) for CSV output.

    This extracts name, skill, difficulty, and description.
    It's suitable for a player's guide summary of available spells.

    >>> import io
    >>> import csv
    >>> from opend6_tools.magic2 import example_spell
    >>> from opend6_tools.magic2 import *

    >>> buffer = io.StringIO()
    >>> book = [example_spell()]
    >>> writer = csv.writer(buffer, quoting=csv.QUOTE_STRINGS)
    >>> _ = writer.writerow(TableSummary.header)
    >>> _ = writer.writerows(TableSummary.csv(s) for s in book)
    >>> buffer.getvalue().splitlines()
    ['"Spell","Skill","Difficulty","Effect"', '"Example","*Acumen: testing*","4","Acumen: testing +4D"']

    """

    header: ClassVar[tuple[str, ...]] = (
        "Spell",
        "Skill",
        "Difficulty",
        "Effect",
    )

    @staticmethod
    def csv(spell: Spell) -> tuple[str, ...]:
        """CSV-extract from a Spell.

        :returns: tuple with (name, skill, difficulty, and description)
        """
        spell.finalize()
        return (
            spell.name,
            f"*{spell.skill}*",
            str(spell.difficulty),
            spell.effect.description(),
        )


class SpellWriter:
    """Output RST-format details for publication.
    This relies on :py:mod:`jinja2` templates.
    """

    spell_template = dedent(
        """\
        {{ spell.name | safe }}
        {{ spell_name_underline * spell.name|length() }}

        :Skill: {{spell.skill}}
        :Difficulty: {{spell.difficulty}} {% if spell._difficulty_note %}(Note: *{{ spell._difficulty_note }}*){% endif %}
        :Effect: {{spell.effect.difficulty()}} ({{spell.effect.description()}})
        :Range: {{spell.range.description()}} \\({{spell.range.difficulty()}})
        :Speed: {{spell.speed.description()}} \\({{spell.speed.difficulty()}})
        :Duration: {{spell.duration.description()}} \\({{spell.duration.difficulty()}})
        :Casting Time: {{spell.casting_time.description()}} \\({{spell.casting_time.difficulty()}})
        {%- if spell.other_aspects %}

        :Other Aspects:
        {% for label, aspect in spell.other_aspects.items() if label != "Difficulty" %}
            {{label}} ({{aspect.difficulty()}}): {{aspect.description()}}

        {% endfor %}
        {% endif %}
        {% if spell.other_conditions %}

        :Other Conditions:
        {%- for aspect in spell.other_conditions %}
            ({{aspect.difficulty()}}): {{aspect.description()}}

        {% endfor %}
        {% endif %}

        {{spell.notes}}

        """
    )
    book_template = dedent("""\
    {% for spell in book %}
    {% include "spell.rst" with context %}
    {% endfor %}
    """)
    multi_book_template = dedent("""\
    {% for name in books %}
    {{ name | safe }}
    {{ book_section_underline * name|length() }}
    {% set book = books[name] %}
    {% include "book.rst" with context%}
    {% endfor %}
    """)

    def __init__(self, section_underline: str = "=", spell_underline: str = "~") -> None:
        """Initialize the SpellWriter.

        :param section_underline: The RST section heading underline.
        :param spell_underline: The RST spell heading underline.
        """
        self.jinja_env: jinja2.Environment = Environment(
            # autoescape=select_autoescape()
        )
        self.jinja_env.loader = jinja2.DictLoader(
            {
                "spell.rst": self.spell_template,
                "book.rst": self.book_template,
                "skill_area.rst": self.multi_book_template,
            }
        )
        self.spell_name_underline = spell_underline
        self.book_section_underline = section_underline

    @singledispatchmethod
    def report(self, spell: Spell) -> str:
        """Prepare a report for a Spell, a list of Spells, or a mapping from name to Spell.

        :param spell: The Spell to format
        :returns: The string which can be printed.
        """
        template = self.jinja_env.get_template("spell.rst")
        spell.finalize()
        return template.render(
            spell=spell,
            spell_name_underline=self.spell_name_underline,
        )

    @report.register(list)
    def _(self, book: list[Spell]) -> str:
        """Report a list of Spells."""
        template = self.jinja_env.get_template("book.rst")
        for spell in book:
            spell.finalize()
        return template.render(
            book=book,
            spell_name_underline=self.spell_name_underline,
        )

    @report.register(dict)
    def _(self, collection: dict[str, list[Spell]]) -> str:
        """Report a dict[str, Spell] book of Spells."""
        template = self.jinja_env.get_template("skill_area.rst")
        for book in collection.values():
            for spell in book:
                spell.finalize()
        return template.render(
            books=collection,
            spell_name_underline=self.spell_name_underline,
            book_section_underline=self.book_section_underline,
        )


def summary(book: list[Spell] | dict[str, list[Spell]], destination: TextIO = sys.stdout) -> None:
    """
    Writes CSV-format summary to a given destination file.
    Uses :py:class:`TableSummary`.

    :param book: spell collection.
    :param destination: Open file, often directed to ``shared/{name}_spells.csv`` or.
    """
    wtr = csv.writer(destination)
    wtr.writerow(TableSummary.header)
    match book:
        case list() as single:
            wtr.writerows(TableSummary.csv(s) for s in single)
        case dict() as multi:
            for section in multi:
                wtr.writerow((f"**{section}**",))
                wtr.writerows(TableSummary.csv(s) for s in multi[section])


def detail(
    spell_or_book: Spell | list[Spell] | dict[str, list[Spell]],
    section_heading: str = "=",
    spell_heading: str = "~",
) -> None:
    """Prints RST-format details of spells to STDOUT.
    Uses :py:class:`SpellWriter` to format the detailes of a spell.

    :param spell_or_book: Spell or collection of Spells
    :param section_header: RST underline for section (when collection is a ``dict``)
    :param spell_header: RST underline for each spell.
    """
    writer = SpellWriter(section_underline=section_heading, spell_underline=spell_heading)
    print(writer.report(spell_or_book))


## Part VI -- Testing and Debugging


def display(spell: Spell | Miracle | Cantrip) -> str:
    """
    Returns the display for a spell in plain text to help designers.

    Does the :py:meth:`Spell.finalize` computation, which will recompute difficulty.
    To **force** this, set ``spell._finalize = False``.
    Note that template spells need to be finalized manually.

    When logging is level is DEBUG, this will reveal the details of the computation, also.

    Used by :py:func:`debug`.

    :param spell: The Spell to display.
    :returns: Character string to print.
    """
    if not spell._finalize:
        # Caution is required. Don't re-finalize.
        spell.finalize()

    attrs = list(k for k in spell.__dict__.keys() if not (k.startswith("_") or k == "aspects"))
    other_aspects = {}
    other_conditions = []
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        for a in attrs:
            val = getattr(spell, a)
            match val:
                case dict() as other_aspects:
                    pass
                case list() as other_conditions:
                    pass
                case Aspect() | Effect():
                    print(f"  {a:20s}: {val.incr_decr.value * val.difficulty():+3d} {val!r}")
                case _:
                    print(f"  {a:20s}: {val!r}")
        if other_aspects:
            print(f"  {'other_aspects':20s}:")
            for k, v in other_aspects.items():
                print(f"  - {k:18s}: {v.incr_decr.value * v.difficulty():+3d} {v!r}")
        if other_conditions:
            print(f"  {'other_conditions':20s}:")
            for v in other_conditions:
                print(f"  - {v.incr_decr.value * v.difficulty():+3d} {v!r}")
        _ = spell.difficulty  # Forces computation of difficulty and related values
        print(f"Effect Details        : {spell.effect.details!r}")
        print(
            f"Spell Total           : {spell._spell_total!r} = {sum(spell._spell_total.values()):d}"
        )
        print(
            f"Negative Modifiers    : {spell._negative_modifiers!r} = {sum(spell._negative_modifiers.values()):d}"
        )
        print(
            f"Difficulty            : ⎡({sum(spell._spell_total.values()):d} - {sum(spell._negative_modifiers.values()):d}) ÷ 2⎤ = {spell.difficulty:d}"
        )
    return buffer.getvalue()


def debug(
    spells: list[Spell | Miracle | Cantrip], ident: int | str | None | list[str] = None
) -> None:
    """
    Prints details of a Spell to STDOUT.
    Uses :py:func:`display`.

    >>> from opend6_tools.magic2 import example_spell
    >>> from opend6_tools.magic2 import *

    >>> book = [example_spell()]
    >>> debug(book, 0)
    ## Example
      name                : 'Example'
      notes               : 'Mage waves their hands and says the words'
      skill               : 'Acumen: testing'
      effect              : +12 SkillEffect('Acumen: testing', '+4D')
      duration            :  +0 DurationAspect('1 sec')
      range               :  +0 RangeAspect('1 m')
      casting_time        :  -4 CastingTimeAspect('5 sec')
      speed               :  +0 SpeedAspect.based_on(('range',), 'Instantaneous')
      other_conditions    :
      -  -1 GenericAspect(Decimal('1'), 'Everthing else is completed')
    Effect Details        : [(Decimal('12'), '+4D')]
    Spell Total           : {'effect': 12, 'duration': 0, 'range': 0, 'speed': 0} = 12
    Negative Modifiers    : {'casting_time': 4, 'condition: Everthing else is [...]': 1} = 5
    Difficulty            : ⎡(12 - 5) ÷ 2⎤ = 4
    <BLANKLINE>
    <BLANKLINE>

    :param spells: Spell Book
    :param ident: Identifier for a spell, a number, or a name, or a list of names.
        Shell-style wild-cards are used to match names.
    """
    logging.basicConfig(level=logging.INFO)
    # logging.getLogger("Spell").setLevel(logging.DEBUG)

    keys: list[str]
    spell_map = {s.name: s for s in spells}
    match ident:
        case None:
            keys = list(spell_map.keys())
        case str():
            try:
                keys = [list(spell_map.keys())[int(ident)]]
            except (ValueError, TypeError):
                keys = [ident]
        case int() as index:
            keys = [list(spell_map.keys())[index]]
        case list() as ident_list:
            keys = [
                n
                for key_pat in ident_list
                for n in spell_map.keys()
                if fnmatch.fnmatch(n.lower(), key_pat.lower())
            ]
        case _:
            raise ValueError("unknown identifier {ident!r}")

    for name in keys:
        spell = spell_map[name]
        print("##", spell.name)
        print(display(spell))
        print()


def dumps(spell: Spell | Miracle | Cantrip) -> str:
    """Returns a TOML-formatted dump of the spell.

    **Not complete**.

    ..  todo:: Finish this.
    """
    return tomli_w.dumps(spell._asdict())


def workbook_spells(context: dict[str, Any]) -> dict[str, Spell]:
    """
    Emit sequence of Spells from a Workbook.
    This examines **all** code cells looking for Spell definitions.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from ``Spell`` name to ``Spell`` instances
    """
    return {value.name: value for name, value in context.items() if isinstance(value, Spell)}


def workbook_rank(context: dict[str, Any]) -> dict[int, list[Spell]]:
    r"""Transform a dict[name: str, Spell] of spells into a dictionary: dict[rank: int, list[Spell]].
    This uses :py:func:`workbook_spells` to get all spells from a Notebook.

    The difficulty of a spell is :math:`d(S)`.
    The range is around a target, :math:`T`, is :math:`-2 \leq d(S) - T < +3`.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from rank number to lists of ``Spell`` instances
    """
    ranked: defaultdict[int, list[Spell]] = defaultdict(list)
    for name, spell in workbook_spells(context).items():
        rank = (spell.difficulty + 2) // 5
        ranked[rank].append(spell)
    return ranked


def workbook_validation(
    context: dict[str, Any], valid: Callable[[Spell], bool] | int, width: int | None = None
) -> list[str]:
    """
    Validate cells in a notebook that define a Spell (or subclass).
    Workbooks often have spells of a given rank, which means a target difficulty of rank × 5.
    This uses :py:func:`workbook_spells` to get all spells from a Notebook.

    :param context: Usually ``globals()`` for a Notebook
    :param valid: Either a callable lambda that validates a spell, or an integer expected difficulty.
    :param width: width of the interval around the expected difficulty.
    :return: list of lines of output.
    """
    match valid:
        case int() as target:
            span = width or 5
            low, high = -(span // 2), span - (span // 2)
            validator = lambda spell: low <= spell.difficulty - target < high  # noqa: E731
            good = (
                f"## All spells approximately {target} difficulty, {target + low}..{target + high}."
            )
            bad = "## Difficulty errors."
        case Callable() as validator:
            good = "## All spells pass difficulty test."
            bad = "## Difficulty errors."
        case _:
            raise TypeError(f"unknown {type(valid)}: {valid!r}")
    spells = workbook_spells(context)
    if not spells:
        raise ValueError("no Spell values in globals()")
    valid_difficulty = {name for name, spell in spells.items() if validator(spell)}
    report: list[str]
    if len(valid_difficulty) == len(spells):
        report = [good]
    else:
        report = [bad]
        for name, spell in spells.items():
            if name not in valid_difficulty:
                report.append(f"### {name!r}\n\n```\n{display(spell)}\n```\n")
    report.append(f"{len(spells)} Spells")
    return report


def build_app(
    book: list[Spell], *, rich_markup_mode: Literal["rich", "markdown"] | None = "rich"
) -> typer.Typer:
    spellbook_app = typer.Typer(
        help="Work with this collection of Spells.", rich_markup_mode=rich_markup_mode
    )

    @spellbook_app.command(name="display")
    def display_command():
        """Write RST-formatted details of all definitions to STDOUT."""
        # TODO: Spell underline and section underline characters.
        detail(book)

    @spellbook_app.command(name="debug")
    def debug_command(
        names: Annotated[list[str] | None, typer.Argument(help="Spell name (or number)")] = None,
    ):
        """Print debugging information for a specific definition to STDOUT"""
        debug(book, names)

    return spellbook_app


def example_spell() -> Spell:
    """An example spell to demonstrate some module features."""
    example = Spell(
        name="Example",
        notes="Mage waves their hands and says the words",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects={},
        other_conditions=[GenericAspect(1, "Everthing else is completed")],
    )
    return example
