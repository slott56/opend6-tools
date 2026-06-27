r"""
Core definitions for spells.

A :py:class:`Spell` is a collection of an :py:class:Effect`,
and a number of individual :py:class:`Aspect` details.

Example
-------

    >>> from opend6_tools.magic import *
    >>> example = Spell(
    ...     name="Example",
    ...     notes="Mage waves their hands and says the words",
    ...     effect=SkillEffect("Acumen: testing", "+4D"),
    ...     duration=DurationAspect("1 sec"),
    ...     range=RangeAspect("1m"),
    ...     casting_time=CastingTimeAspect("5 sec"),
    ...     speed=SpeedAspect.based_on("range", "Instantaneous"),
    ...     other_aspects = {},
    ...     other_conditions = [GenericAspect(1, "Everything else is completed")],
    ... )
    >>> example.difficulty
    4
    >>> detail(example)  # doctest: +NORMALIZE_WHITESPACE
    Example
    ~~~~~~~
    <BLANKLINE>
    :Skill: Acumen: testing
    :Difficulty: 4
    :Effect: 12 (Acumen: testing 4*D)
    :Range: 1 m \(0)
    :Speed: Instantaneous \(0)
    :Duration: 1 sec \(0)
    :Casting Time: 5 sec \(4)
    <BLANKLINE>
    <BLANKLINE>
    :Other Conditions:
        (1): Everything else is completed
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    Mage waves their hands and says the words
    <BLANKLINE>

Spell, Cantrip, Miracle
------------------------

..  autoclass:: Spell
    :members:
    :member-order:  bysource

..  autoclass:: Miracle
    :members:

..  autoclass:: Cantrip
    :members:

Aspects and Effects
-------------------

The base class for all aspects and effects.

..  autoclass:: Aspect
    :members:

..  autoclass:: OtherAspects
    :members:
    :undoc-members:


Effects
~~~~~~~~~~~~

There are a number of effects, all derived from :py:class:`Effect`.

..  autoclass:: Effect
    :members:

..  autoclass:: CharacteristicType
    :members:
    :undoc-members:

..  autoclass:: CharacteristicFactor
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


..  autoclass:: TimeAspect
    :show-inheritance:

..  autoclass:: DistanceAspect
    :show-inheritance:

GenericAspect
~~~~~~~~~~~~~

..  autoclass:: GenericAspect
    :show-inheritance:


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

..  autoclass:: AreaVolumeUnit
    :show-inheritance:
    :members:
    :undoc-members:
    :member-order:  bysource

ChangeTargetAspect
~~~~~~~~~~~~~~~~~~

..  autoclass:: ChangeTargetAspect

..  autoclass:: ChangeTargetUnit
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

..  autoclass:: CommunitySizeUnit
    :members:
    :undoc-members:

..  autoclass:: CommunityParticipationFactor
    :members:
    :undoc-members:

ComponentsAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: ComponentsAspect

..  autoclass:: ComponentRarityUnit
    :members:
    :undoc-members:

..  autoclass:: ComponentQuantityFactor
    :members:
    :undoc-members:

ConcentrationAspect
~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: ConcentrationAspect

CountenanceAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: CountenanceAspect

..  autoclass:: CountenanceVisibilityModifier
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

..  autoclass:: GestureComplexityModifier
    :members:
    :undoc-members:

IncantationsAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: IncantationsAspect

..  autoclass:: IncantationComplexityModifier
    :members:
    :undoc-members:

MultipleTargetAspect
~~~~~~~~~~~~~~~~~~~~

..  autoclass:: MultipleTargetAspect

..  autoclass:: MultiTargetUnit
    :members:
    :undoc-members:

UnrealEffectAspect
~~~~~~~~~~~~~~~~~~~

..  autoclass:: UnrealEffectAspect

..  autoclass:: UnrealDisbeliefFactor
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

..  autofunction:: logged

..  autoclass:: Sign
    :members:
    :undoc-members:

..  autoclass:: DifficultyAdjustment

..  autoclass:: IncreasesDifficulty
    :show-inheritance:

..  autoclass:: DecreasesDifficulty
    :show-inheritance:

DetailValue definitions
~~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: Difficulty
    :members:

..  autoclass:: Measure
    :members:

..  autoclass:: Modifier
    :members:

..  autoclass:: Factor
    :members:

Normalized Aspect Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  autoclass:: NormalizedAspect
    :members:
    :member-order:  bysource

..  autoclass:: CompositeNormalizedAspect
    :members:
    :member-order:  bysource

..  autoclass:: NormalizedAspectProxy
    :members:
    :member-order:  bysource

..  autoclass:: NormalizedAspectReference
    :members:
    :member-order:  bysource

..  autofunction:: m2v

Parsers
~~~~~~~

..  autoclass:: Parser
    :members:
    :member-order:  bysource

..  autoclass:: MatchingEnum
    :members:
    :member-order:  bysource

..  autoclass:: UniqueMatchingEnum
    :members:
    :member-order:  bysource


..  autoclass:: Lookup
    :members:
    :undoc-members:

..  autoclass:: QualifiedLookup
    :members:

..  autoclass:: Unit
    :show-inheritance:
    :members:

Specific Units
~~~~~~~~~~~~~~~~

These are implementations of specific sections of the rules.

..  autoclass:: DieCode
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: DiceUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: Time

..  autoclass:: TimeUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: Mass

..  autoclass:: MassUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: Distance

..  autoclass:: DistUnit
    :show-inheritance:
    :members:
    :undoc-members:

..  autoclass:: Volume

..  autoclass:: VolumeUnit
    :show-inheritance:
    :members:
    :undoc-members:

"""

import abc
from collections import defaultdict
from collections.abc import Sequence, Iterator
from dataclasses import dataclass, field
import decimal
from decimal import Decimal
from difflib import get_close_matches
from enum import Enum
import graphlib
import inspect
from itertools import chain
import logging
from math import prod
from textwrap import dedent, shorten
from typing import Self, TypedDict, ClassVar, cast, NamedTuple
from weakref import ref

from ..dice import *

from humre import (
    group,
    named_group,
    optional_group,
    either,
    optional,
    chars,
    nonchars,
    zero_or_more,
    one_or_more,
    one_or_more_lazy,
    PLUS,
    MINUS,
    WHITESPACE,
    DIGIT,
    ANYTHING,
    OPEN_PAREN,
    CLOSE_PAREN,
    PERIOD,
    ANYCHAR,
)

## Part I: Foundations


def logged[T: "type[Aspect]"](cls: T) -> T:
    """Inject a properly-named logger into a class definition to permit logging prior to super().__init__()."""
    cls.logger = logging.getLogger(cls.__name__)
    return cls


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


# There are four varieties of parsed DetailValue subclasses:
#
# - Difficulty, a difficulty. Used rarely.
#
# - Measure, a value (usually in KMS units).
#   The difficulty is based on the given value.
#   The :py:func:`m2v` function does measure-to-value conversion.
#
# - Modifier, also difficulty value, usually applied by a Measure.
#
# - Factor, a dimensionless factor used to scale a difficulty.


@dataclass(init=False)
class Difficulty:
    """A difficulty and a description.

    >>> d = Difficulty(10, "Moderately Difficult")
    >>> d.description
    'Moderately Difficult'
    >>> d.difficulty
    Decimal('10')
    """

    difficulty: Decimal
    description: str

    def __init__(self, difficulty: int | Decimal, description: str) -> None:
        self.difficulty = Decimal(difficulty)
        self.description = description


@dataclass(init=False)
class Measure:
    """A parsed measure and a canonical string description.

    The difficulty is computed from the given value.
    The :py:func:`m2v` function does measure-to-value conversion.

    >>> m = Measure(10, "Units")
    >>> m.measure
    Decimal('10')
    >>> m.difficulty
    Decimal('5')
    >>> m.description
    'Units'
    """

    measure: Decimal
    description: str
    difficulty: Decimal

    def __init__(self, measure: int | Decimal, description: str) -> None:
        self.measure = Decimal(measure)
        self.difficulty = m2v(self.measure)
        self.description = description


@dataclass(init=False)
class Modifier:
    """A modifier and a description.

    Total difficulty is sum(measures) + sum(modifiers).

    >>> m=Modifier(3, "Modifier")
    >>> m.difficulty
    Decimal('3')
    >>> m.description
    'Modifier'
    """

    difficulty: Decimal
    description: str

    def __init__(self, difficulty: int | Decimal, description: str) -> None:
        self.difficulty = Decimal(difficulty)
        self.description = description


@dataclass(init=False)
class Factor:
    """A factor and a description.
    Factors are dimensionless and generally applied to Difficulties.

    Total difficulty is (sum(measures) + sum(modifiers)) * max(factor)

    >>> f = Factor(1.5, "Factor")
    >>> f.factor
    Decimal('1.5')
    >>> f.description
    'Factor'
    """

    factor: Decimal
    description: str

    def __init__(self, factor: int | Decimal, description: str) -> None:
        self.factor = Decimal(factor)
        self.description = description


type DifficultyValue = Difficulty | Measure | Modifier
type DetailValue = DifficultyValue | Factor


class NormalizedAspect:
    """Normalized details supporting an Aspect or Effect.

    The parameters an ``Aspect`` (or ``Effect``) class
    use values generally designed for human readability.
    This means a number of alternative formats and types are tolerated.
    A number of distinct, specialized :py:class:`Parser`
    subclasses are used to parse the source material and create the
    normalized details for these objects.

    There are three paths to creating a ``NormalizedAspect`` from an ``Aspect``.

    -   In many cases, the ``NormalizedAspect`` can be created directly from the argument values.
        There's a nuanced issue where some aspects have a difficulty first, and other aspects provide a metric from which the difficulty is derived.

    -   In cases where the aspect is "based-on" another aspect,
        a ``NormalizedAspectProxy`` is created from the argument values.
        Then, a ``NormalizedAspect`` is created during ``Spell`` finalization.

    -   In a few cases, a ``NormalizedAspect`` can be copied from a different spell.
        This is a "based-on-spell" aspect used as part of a spell template.
        A ``NormalizedAspectReference`` is created from the argument values.
        Then,  ``NormalizedAspect`` is cloned during ``Spell`` finalization.
    """

    rank: Decimal | None = None  #: Used by SpecialAbilityEffect
    effect_difficulty: Modifier | None = None  #: Used by UnrealEffectAspect
    mettle_target: Decimal | None = None  #: Used by ConcentrationAspect

    # Cached values
    _difficulty: Decimal | None = None
    _description: str | None = None

    def __init__(self, aspect: "Aspect") -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.aspect = ref(aspect)
        self.parsers = [
            value()
            for name, value in inspect.getmembers_static(aspect)
            if name.endswith("_cls") and inspect.isclass(value)
        ]
        self.logger.debug(
            "Context: %s\n  Parsers=%r", aspect.__class__.__name__, self.parsers
        )
        self.details: dict[type["Parser"], list[DetailValue]] = defaultdict(list)
        self.notes: list[str] = []
        self.kwargs: dict[str, Any] = {}

    def __repr__(self) -> str:
        if aspect := self.aspect():
            aspect_repr = aspect.source()
        else:  # pragma: no cover
            aspect_repr = "**REF ERROR**"
        return f"{self.__class__.__name__}({aspect_repr})"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f" parsers={[p.__class__.__name__ for p in self.parsers]}"
            f", details={ {prsr.__name__: dets for prsr, dets in self.details.items()}!r}"
            f", notes={self.notes!r}"
            f", kwargs={self.kwargs!r}"
            f", _difficulty={self._difficulty!r}"
            f", _description={self._description!r}"
        )

    def __eq__(self, other: Any) -> bool:
        match other:
            case NormalizedAspect() as other_aspect:
                return (
                    self.details == other_aspect.details
                    and self.notes == other_aspect.notes
                    and self.kwargs == other_aspect.kwargs
                )
            case _:
                return NotImplemented

    def difficulty(self) -> Decimal:
        """Compute and cache difficulty using the Aspect's method."""
        if self._difficulty is None:
            if aspect := self.aspect():
                self._difficulty = aspect.compute_difficulty(self)
            else:  # pragma: no cover
                raise RuntimeError("broken weak reference")
        return cast(Decimal, self._difficulty)

    def description(self) -> str:
        """Compute and cache description using the Aspect's method."""
        if self._description is None:
            if aspect := self.aspect():
                self._description = aspect.compute_description(self)
            else:  # pragma: no cover
                raise RuntimeError("broken weak reference")
        return cast(str, self._description)

    def origin(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """The original args and kwargs used to create an Aspect."""
        if aspect := self.aspect():
            return aspect.origin
        else:  # pragma: no cover
            raise RuntimeError("broken weak reference")

    def sign(self) -> Sign:
        """The Sign that applies to this Aspect."""
        if aspect := self.aspect():
            return aspect.incr_decr
        else:  # pragma: no cover
            raise RuntimeError("broken weak reference")

    def populate_details(
        self, args: Sequence[Any], **kwargs: list[DetailValue]
    ) -> Self:
        """
        Parse the argument values given to the Aspect, and **update** this NormalizedAspect.

        This can be used incrementally where the arguments are very complicated.

        Try each parser, in the order given,
        to resolve the argument's meaning.
        First match wins.

        ..  todo:: Composition vs. Inheritance issue.

            As a special case, this supports the generic Aspect and Effect classes have no parsers.
            These parser-less cases expect either number, string) or (string, number)
            as the two argument values.
        """
        if not self.parsers:
            # Aspect, Effect, GenericAspect have no parsers.
            # TODO: extract this from the general case.
            if not args:
                args, kwargs = self.origin()
            match args:
                case (int() | Decimal() as diff, str() as desc):
                    self._difficulty = Decimal(diff)
                    self._description = desc
                case (str() as desc, int() | Decimal() as diff):
                    self._difficulty = Decimal(diff)
                    self._description = desc
                case (int() | Decimal() as diff,):
                    self._difficulty = Decimal(diff)
                    self._description = ""
                case (None, str() as desc):
                    # ArcaneKnowedgeAspect has only a description.
                    self._difficulty = Decimal(0)
                    self._description = desc
                case tuple() if len(args) == 0:
                    # CompositeEffect has no useful arguments, nor any parsers
                    pass
                case _:  # pragma: no cover
                    raise ValueError(f"can't parse {args!r}")
            notes = kwargs.pop("notes", "")
            self.notes = cast(
                list[str], list(notes) if isinstance(notes, (list, tuple)) else [notes]
            )
            self.kwargs = kwargs
            self.logger.debug(
                "  No-Parsers: args=%r, kwargs=%r, difficulty=%r, description=%r",
                args,
                kwargs,
                self._difficulty,
                self._description,
            )
            return self

        # Parsers are present in the class definition.
        if "notes" in kwargs:
            notes = kwargs.pop("notes")
            self.notes = cast(
                list[str], list(notes) if isinstance(notes, (list, tuple)) else [notes]
            )
        errors = defaultdict(list)
        for a in args:
            self.logger.debug("  parse %r", a)
            parser = value = None
            for dtl_parser in filter(None, self.parsers):
                try:
                    parser = dtl_parser.__class__
                    value = dtl_parser.parse(a)
                    break
                except InvalidVolumeError:  # pragma: no cover
                    # Special case: more involved than a value error
                    raise
                except (ValueError, KeyError) as ex:
                    self.logger.debug(
                        "  parser %r error %r", dtl_parser.__class__.__name__, ex
                    )
                    errors[repr(a)].append(f"{dtl_parser.__class__.__name__}: {ex}")
            if parser and value:
                self.logger.debug("  parser %r: %r is %r", parser.__name__, a, value)
                self.details[parser].append(value)
            else:
                self.logger.debug("  %r is a note", a)
                self.notes.append(a)
        self.kwargs = kwargs
        self.logger.debug(
            "  args=%r, kwargs=%r, details=%r, notes=%r",
            args,
            kwargs,
            self.details,
            self.notes,
        )

        if not self.details:  # pragma: no cover
            raise ValueError(
                f"incomplete measure in {args=!r} {kwargs=!r}, errors={errors.items()!r}, notes={self.notes!r}"
            )

        return self

    def difficulty_details(
        self, parser_cls: type["Parser"] | None
    ) -> Iterator[Decimal]:
        """Extract Difficulty, Measure, or Modifier details.

        This assumes the given ``parser_cls`` returned a value in the ``DifficultyValue`` union.
        """
        subset = (
            cast(list[DifficultyValue], self.details[parser_cls]) if parser_cls else []
        )
        return (d.difficulty for d in subset)

    def factor_details(self, parser_cls: type["Parser"] | None) -> Iterator[Decimal]:
        """Extract Factor details.

        This assumes the given ``parser_cls`` returned a value of the ``Factor`` type.
        """
        subset = cast(list[Factor], self.details[parser_cls]) if parser_cls else []
        return (d.factor for d in subset)

    def description_details(self, parser_cls: type["Parser"] | None) -> Iterator[str]:
        """Extract the description from a subset of details."""
        subset = self.details[parser_cls] if parser_cls else []
        return (d.description for d in subset)


class CompositeNormalizedAspect(NormalizedAspect):
    """A NormalizedAspect which contains other NormalizedAspect instances."""

    def __init__(self, aspect: "Aspect"):
        super().__init__(aspect)
        self.children: list[NormalizedAspect] = []

    def append(self, normalized: NormalizedAspect) -> None:
        self.children.append(normalized)

    def populate_details(
        self, args: Sequence[Any], **kwargs: list[DetailValue]
    ) -> Self:
        """Should be invoked incrementally for each distinct sub-aspect of the composite.

        The canonical example is Components, where each component is
        populated separately.
        """
        if aspect := self.aspect():
            child = NormalizedAspect(aspect).populate_details(args, **kwargs)
            self.append(child)
            self.notes.append(" ".join(child.notes))
            return self
        else:  # pragma: no cover
            raise RuntimeError("broken weak reference")

    def __str__(self) -> str:
        children = [
            f"{ {prsr.__name__: dets for prsr, dets in child.details.items()}!r}"
            for child in self.children
        ]
        return (
            f"{self.__class__.__name__}"
            f" parsers={[p.__class__.__name__ for p in self.parsers]}"
            f", details={', '.join(children)}"
            f", notes={self.notes!r}"
            f", kwargs={self.kwargs!r}"
            f", _difficulty={self._difficulty!r}"
            f", _description={self._description!r}"
        )

    def __eq__(self, other: Any) -> bool:
        match other:
            case CompositeNormalizedAspect() as other_aspect:
                return (
                    self.details == other_aspect.details
                    and self.notes == other_aspect.notes
                    and self.kwargs == other_aspect.kwargs
                    and self.children == other_aspect.children
                )
            case _:  # pragma: no cover
                return NotImplemented

    def difficulty(self) -> Decimal:
        """Compute and cache difficulty using the Aspect's method."""
        if self._difficulty is None:
            if aspect := self.aspect():
                self._difficulty = sum(
                    (aspect.compute_difficulty(child) for child in self.children),
                    Decimal(0),
                )
            else:  # pragma: no cover
                raise RuntimeError("broken weak reference")
        return cast(Decimal, self._difficulty)

    def description(self) -> str:
        """Compute and cache description using the Aspect's method."""
        if self._description is None:
            if aspect := self.aspect():
                self._description = "; ".join(
                    aspect.compute_description(child) for child in self.children
                )
            else:  # pragma: no cover
                raise RuntimeError("broken weak reference")
        return cast(str, self._description)

    def difficulty_details(
        self, parser_cls: type["Parser"] | None
    ) -> Iterator[Decimal]:
        return (
            sum(child.difficulty_details(parser_cls), Decimal(0))
            for child in self.children
        )

    def factor_details(self, parser_cls: type["Parser"] | None) -> Iterator[Decimal]:
        return (
            Decimal(prod(child.factor_details(parser_cls))) for child in self.children
        )

    def description_details(self, parser_cls: type["Parser"] | None) -> Iterator[str]:
        return (
            "; ".join(child.description_details(parser_cls)) for child in self.children
        )


@dataclass
class NormalizedAspectProxy:
    """A proxy for a ``NormalizedAspect``, waiting for other spell details to compute a derived value.

    :attr_paths:
        The aspects names on which this depends.

    :args: Original args to the :py:meth:`Aspect.based_on` method.

    :kwargs: Original kwargs to the :py:meth:`Aspect.based_on` method.

    :depends_on:
        A mapping from aspect name to NormalizedAspect instances.
        This is normally empty.
        It is set during :py:meth:`Spell.finalize` processing.
    """

    attr_paths: tuple[str, ...]
    args: tuple[Any, ...]
    kwargs: dict[str, Any]

    # Set during finalize processing by get_dependencies
    depends_on: dict[str, NormalizedAspect] = field(default_factory=dict)

    def set_dependencies(self, spell: "Spell") -> None:
        """Extracts requested NormalizedAspect values from a given Spell."""
        all_attrs = tuple(
            (attr, spell.aspects[attr].base)
            for attr in self.attr_paths
            if attr in spell.aspects  # avoid "effect"
        )
        if "effect" in self.attr_paths:
            all_attrs += (("effect", spell.effect.base),)
        self.depends_on = {attr: base for attr, base in all_attrs if base is not None}


@dataclass
class NormalizedAspectReference:
    """A reference for a ``NormalizedAspect`` to be copied from another spell.
    Created by a based_on_spell aspect.

    :attr_path:
        The aspect name to copy from another spell.
    """

    attr_path: str

    def difficulty(self) -> Decimal:
        return Decimal(0)

    def description(self) -> str:
        return f"based on spell's {self.attr_path}"


def m2v(measure: Decimal) -> Decimal:
    r"""
    The core conversion of a Measure, :math:`m`, to a Difficulty Value, :math:`v`.

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

    Where :math:`\rceil_{u}` uses ``decimal.ROUND_UP``,
    and :math:`\rceil` uses ``decimal.ROUND_HALF_UP``.

    Two alternate interpretations for the cutoff. :math:`m \leq 5` or :math:`m < 10`.
    Both fit the available data.

    The rules are ambiguous. Consider this:

        If the desired amount is greater than one number but less than
        another, either lower your amount or select the bigger number.

    This appears to mean make a design change ("lower your amount") or round up ("select the bigger number").

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
    except (ValueError, decimal.InvalidOperation):  # pragma: no cover
        raise ValueError(f"invalid measure, {measure} <= 0")


class Parser(abc.ABC):
    """ABC for all Measure, Modifier, and Factor Parsers."""

    @staticmethod
    def decompose(args: Sequence[Any]) -> Iterator[Any]:
        """
        Decompose strings into separate arg values by splitting at the ``;``.

        Often used as part of creating a NormalizedAspect.

        ::

            self.base = self.normalize_aspect(*Parser.decompose(args))
        """
        for arg in args:
            match arg:
                case str():
                    if ";" in arg:
                        yield from map(lambda s: s.strip(), arg.split(";"))
                    else:
                        yield arg
                case _:
                    yield arg

    @abc.abstractmethod
    def parse(self, *args: Any) -> DetailValue: ...


# Two version of Enum
# - With Aliases -- used for units with multiple aliases for a unit name.
# - Unique -- used for modifiers and factors where values are reused.


class MatchingEnum(Enum):
    """Each name can be an alias of another name.
    The ``.value`` attribute will be the given metric.
    Also, a ``.metric`` attribute will also have the metric value.

    The first nam with a value is the canonical name.
    All subsequent names for the same value are aliases.

    >>> from opend6_tools.magic.spells import MatchingEnum

    >>> class Rig(MatchingEnum):
    ...     sloop = 1
    ...     ketch = 2
    ...     yawl  = 2

    >>> Rig.sloop.metric
    1

    >>> k = Rig.match("catch")
    >>> k.metric
    2
    >>> k.name
    'ketch'

    >>> Rig.yawl
    <Rig.ketch: 2>
    """

    metric: Decimal
    _ignore_ = ["lookup_list"]

    def __new__(cls, metric: Decimal):
        obj = object.__new__(cls)
        obj._value_ = metric
        obj.metric = metric
        return obj

    @classmethod
    def match(cls, name: str, cutoff: float = 0.6) -> "MatchingEnum":
        """Search the enum names for the closest match."""
        if not hasattr(cls, "lookup_list"):
            cls.lookup_list = list(c.lower() for c in cls.__members__)
        matches = get_close_matches(enumify(name), cls.lookup_list, 1, cutoff=cutoff)
        if not matches:
            raise KeyError(
                f"enum {cls.__name__} has no name {name!r} in {cls.lookup_list!r}"
            )
        return cls[matches[0]]


class UniqueMatchingEnum(MatchingEnum):
    """Each name is forced to be unique.
     This is needed when there are multiple names that are not simply aliases.
     ("m" and "meter", for example, are aliases, and "m" is the canonical form.)

    The ``.value`` attribute will be an integer of no importance.
    The ``.metric`` attribute will have the metric value.

    >>> from opend6_tools.magic.spells import UniqueMatchingEnum

    >>> class Rig(UniqueMatchingEnum):
    ...     sloop = 1
    ...     ketch = 2
    ...     yawl  = 2
    >>> Rig.sloop.metric
    1
    >>> k = Rig.match("catch")
    >>> k.metric
    2
    >>> k.name
    'ketch'

    >>> Rig.yawl
    <Rig.yawl: 3>
    >>> Rig.yawl.metric
    2
    >>> Rig.match("yawl")
    <Rig.yawl: 3>

    """

    metric: Decimal

    def __new__(cls, metric: Decimal):
        unique_id = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = unique_id
        obj.metric = metric
        return obj


class Lookup[T_enum: MatchingEnum](Parser):
    """Generic Lookup class to use an enumerated list of unit names.
    Must be instantiated with a result class.

    >>> class FactorChoices(MatchingEnum):
    ...     single = Decimal(1)
    ...     double = Decimal(2)
    ...     triple = Decimal(3)

    >>> class MetricFactor(Lookup[FactorChoices]):
    ...     choices = FactorChoices
    ...     result_cls = Factor

    >>> mf = MetricFactor()
    >>> mf.parse("single")
    Factor(factor=Decimal('1'), description='single')
    >>> mf.parse(FactorChoices.double)
    Factor(factor=Decimal('2'), description='double')

    """

    choices: type[T_enum]
    result_cls: type[DetailValue] = Modifier
    cutoff: float = 0.6

    _choice_names: list[str]  # Cache for enum names.

    def parse(self, *args: Any) -> DetailValue:
        """Parse the arguments for a Lookup: either strings or Enum values.

        To make things *slightly* simpler
        """
        result_cls = self.result_cls
        match args:
            case (str(),) as single_text:
                (text,) = single_text
                return result_cls(*self.parse_str(text))
            case (MatchingEnum(),) as single_obj:
                (lookup_enum,) = single_obj
                value = lookup_enum.metric
                name = lookup_enum.name
                return result_cls(value, name)
            case _:
                raise ValueError(f"invalid {', '.join(map(repr, args))}")

    def parse_str(self, text: str) -> tuple[Decimal, str]:
        """Find the closest-matching item in the choices Enum type."""
        try:
            unit = self.choices.match(text, self.cutoff)
            return unit.metric, unit.name
        except KeyError as ex:
            raise ValueError(f"invalid {text}, {ex.args[0]}")


class QualifiedLookup[T_enum](Lookup):
    """A Lookup that supports a modifier name and a supporting detail.

    - "modifier:detail"

    - "modifier(detail)"
    """

    cutoff: float = 0.8

    pattern_1 = group(ANYTHING) + OPEN_PAREN + group(ANYTHING) + CLOSE_PAREN

    def parse_str(self, text: str) -> tuple[Decimal, str]:
        """Search the enum names for the closest match.

        Sometimes ":" is part of the name, like "Luck: Good".
        Sometimes, it separates a note from the essential ability name,
        as in "Enhanced Sense: bugs".

        This leads to multiple matching attempts.

        Case 1: "()"'s.

            Extract the prefix and the note.
            If the prefix matches, slap the suffix onto the matching name as part of the result.

        Case 2: ":".

            Try to match the full name.

            1.  Partition the text on the ":", into ``prefix:suffix``.
                If a full-name match is found AND the suffix is in the full name, the ":" was
                part of the special ability name (Luck: Good, or Possession: Full).
                Done.

            2.  At this point either (1) the suffix is not in the full name,
                or (2) the full name didn't match in the first place.
                If the prefix matches, slap the suffix onto the matching name as part of the result.
                Done.

        Case _:

            Match. No note.

        raise ValueError.
        """
        clean_unit = text.strip().lower()

        if match := re.match(self.pattern_1, clean_unit):
            prefix, suffix = match.group(1).strip(), match.group(2).strip()
            try:
                unit = self.choices.match(prefix)
                return unit.metric, f"{unit.name} ({suffix})"
            except KeyError as ex:  # pragma: no cover
                raise ValueError(f"invalid ()-qualifier {text!r}, {ex.args[0]}")

        elif ":" in clean_unit:
            # Complex cases: ":" might be part of the name or might be a note.
            try:
                unit = self.choices.match(clean_unit, self.cutoff)
                return unit.metric, unit.name
            except KeyError:
                pass
            prefix, suffix = map(lambda s: s.strip(), clean_unit.split(":"))
            try:
                unit = self.choices.match(prefix, self.cutoff)
                # Option 1: suffix actually **was** part of the name
                if suffix in unit.name:
                    return unit.metric, unit.name
                # Option 2: suffix is a note, not part of the name
                unit = self.choices.match(prefix, self.cutoff)
                return unit.metric, f"{unit.name}: {suffix}"
            except KeyError as ex:  # pragma: no cover
                raise ValueError(f"invalid :-qualifier {text!r}, {ex.args[0]}")

        else:
            try:
                unit = self.choices.match(clean_unit, self.cutoff)
                return unit.metric, unit.name
            except KeyError as ex:
                raise ValueError(f"invalid {text!r}, {ex.args[0]}")


class Unit[T_enum: MatchingEnum](Parser):
    """Generic Unit-of-Measure class to use an enumerated list of unit names.
    This looks for value and a unit, and applies the :py:func:`m2v` conversion
    to create a :py:class:`Measure`.

    This is a mixin for an Aspect or Effect.

    >>> class Metric(MatchingEnum):
    ...     single = Decimal(1)
    ...     double = Decimal(2)
    ...     triple = Decimal(3)

    >>> class MetricUnit(Unit[Metric]):
    ...     choices = Metric
    ...     result_cls = Measure
    >>> Metric.match("double")
    <Metric.double: Decimal('2')>
    >>> MetricUnit().base_unit()
    'single'
    >>> MetricUnit().parse(5, Metric.triple)
    Measure(measure=Decimal('15'), description='5 triple', difficulty=Decimal('6'))
    >>> MetricUnit().parse("7 double")
    Measure(measure=Decimal('14'), description='7 double', difficulty=Decimal('6'))
    >>> MetricUnit().parse(11)
    Measure(measure=Decimal('11'), description='11 single', difficulty=Decimal('5'))
    >>> MetricUnit().parse("13")
    Measure(measure=Decimal('13'), description='13 single', difficulty=Decimal('6'))

    ..  todo:: Should the Unit class be part of Measure???

        class TimeUnit(Measure[Time]):
            choices = Time

        What we have are three aspects:

        -   Enumerated values -- clearly a Mixin with many subclasses.

        -   Parsing text or enumerated objects. A good candidate for a mixin.
            Variants:

            -   Measures: where the lookup is a scale factor.
                Essentially KMS units for Distance, Mass, and Time.
                The :func:`m2v` function is used to create a value from
                the raw measure.
                This adds more complex parsing and transformations
                built in the enum lookup.

            -   Modifiers and Factors: the table lookup
                is the modifier or factor.
                These add enum lookups to the base class.

            -   DieCode: There's no table, *per se*, only parsing.
                In a way, this is the base class.

        -   Emitting a Measure, Modifier, Factor, or raw Difficulty.
            This is the target use for a given parser subclass.
    """

    choices: type[T_enum]
    result_cls: type[DetailValue] = Measure
    cutoff: float = 0.6

    _base_unit: str  # Cache for default unit

    def base_unit(self) -> str:
        cls = self.__class__
        if not hasattr(cls, "_base_unit"):
            bases = list(c.name for c in cls.choices if c.metric == 1)
            cls._base_unit = bases[0]
        return cls._base_unit

    unit_pat = (
        optional(WHITESPACE)
        + optional_group(
            one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS, ","))
        )  # +|- Number
        + optional(WHITESPACE)
        + group(zero_or_more(nonchars("(")))  # The text from choice.
        + optional_group(zero_or_more(nonchars(")")))  # Notes in ()'s.
    )

    def parse_str(self, text: str) -> tuple[Decimal, str]:
        """Parse the string into a number and a unit.
        Find the unit in the choices Enum type.
        """
        if not (unit_match := re.match(self.unit_pat, text)):
            raise ValueError(f"invalid {text=!r}")  # pragma: no cover
        if unit_match.group(1) and unit_match.group(2):
            # Number and Unit
            clean_unit = unit_match.group(2).strip().lower()
            unit = self.choices.match(clean_unit, self.cutoff)
            scale = unit.metric
            name = unit.name
            value = Decimal(unit_match.group(1).replace(",", ""))
        elif unit_match.group(1):
            # Number with no unit, find first "Decimal(1)" name.
            name = self.base_unit()
            scale = self.choices[name].metric
            value = Decimal(unit_match.group(1).replace(",", ""))
        elif unit_match.group(2):
            # No number, only unit word, assume value is 1.
            clean_unit = unit_match.group(2).strip().lower()
            unit = self.choices.match(clean_unit, self.cutoff)
            scale = unit.metric
            name = unit.name
            value = Decimal(1)
        else:
            raise ValueError(f"invalid {text=!r}")
        return value * scale, f"{value} {name}"

    def parse(self, *args: Any) -> DetailValue:
        """Parse the arguments for a Unit with several forms.

        -   Number, String with unit text
        -   Number, Enum value with unit
        -   String with numeric text and unit text
        -   Number
        """
        result_cls = self.result_cls
        match args:
            case (str() as single_text,):
                return result_cls(*self.parse_str(single_text))
            case (int() | float() | Decimal() as single_number,):
                name = self.base_unit()
                scale = self.choices[name].metric
                return result_cls(
                    Decimal(single_number) * scale, f"{single_number} {name}"
                )
            case (int() | float() | Decimal() as value, str() as unit_name):
                unit = self.choices.match(unit_name, self.cutoff)
                scale = unit.metric
                name = unit.name
                return result_cls(Decimal(value) * scale, f"{value} {name}")
            case (int() | float() | Decimal() as value, MatchingEnum() as unit_enum):
                scale = unit_enum.metric
                name = unit_enum.name
                return result_cls(Decimal(value) * scale, f"{value} {name}")
            case _:  # pragma: no cover
                raise ValueError(f"invalid {', '.join(map(repr, args))}")


## Part II: Units: Mass, Distance, Time, Area, and Volume


class Time(MatchingEnum):
    """
    All the time scale factors.

    >>> scale = Time.instantaneous.metric
    >>> scale
    Decimal('1')
    >>> Time.instantaneous.name
    'sec'
    >>> scale = Time['rounds'].metric
    >>> scale
    Decimal('5')
    """

    sec = Decimal(1)  # Canonical name
    second = Decimal(1)
    seconds = Decimal(1)
    s = Decimal(1)
    instant = Decimal(1)  # Alias for seconds
    instantaneous = Decimal(1)
    round = Decimal(5)
    rounds = Decimal(5)
    r = Decimal(5)
    min = Decimal(60)
    minute = Decimal(60)
    minutes = Decimal(60)
    m = Decimal(60)
    hr = Decimal(60) * 60
    hrs = Decimal(60) * 60
    hour = Decimal(60) * 60
    hours = Decimal(60) * 60
    h = Decimal(60) * 60
    day = Decimal(60) * 60 * 24
    days = Decimal(60) * 60 * 24
    d = Decimal(60) * 60 * 24
    wk = Decimal(60) * 60 * 24 * 7
    week = Decimal(60) * 60 * 24 * 7
    weeks = Decimal(60) * 60 * 24 * 7
    w = Decimal(60) * 60 * 24 * 7
    mon = Decimal(60) * 60 * 24 * Decimal("30.4375")  # Julian year; it's simpler
    month = Decimal(60) * 60 * 24 * Decimal("30.4375")
    months = Decimal(60) * 60 * 24 * Decimal("30.4375")
    yr = Decimal(60) * 60 * 24 * Decimal("365.25")
    year = Decimal(60) * 60 * 24 * Decimal("365.25")
    years = Decimal(60) * 60 * 24 * Decimal("365.25")
    y = Decimal(60) * 60 * 24 * Decimal("365.25")
    century = Decimal(60) * 60 * 24 * 36525
    centuries = Decimal(60) * 60 * 24 * 36525
    c = Decimal(60) * 60 * 24 * 36525


class TimeUnit(Unit[Time]):
    """
    Time Unit mixin for Aspects.

    >>> tu = TimeUnit()
    >>> tu.parse("1 round")
    Measure(measure=Decimal('5'), description='1 round', difficulty=Decimal('4'))
    >>> tu.parse(2, "round")
    Measure(measure=Decimal('10'), description='2 round', difficulty=Decimal('5'))
    >>> tu.parse("round")
    Measure(measure=Decimal('5'), description='1 round', difficulty=Decimal('4'))
    >>> tu.parse(3)
    Measure(measure=Decimal('3'), description='3 sec', difficulty=Decimal('3'))
    >>> tu.parse(4, Time.round)
    Measure(measure=Decimal('20'), description='4 round', difficulty=Decimal('7'))
    >>> tu.parse("1 year")
    Measure(measure=Decimal('31557600.00'), description='1 yr', difficulty=Decimal('37'))

    """

    choices = Time
    result_cls = Measure


class Mass(MatchingEnum):
    """
    All the mass scale factors.

    >>> scale = Mass.kg.metric
    >>> scale
    Decimal('1')
    >>> Mass.ton.name
    'ton'
    >>> scale = Mass['megaton'].metric
    >>> scale
    Decimal('1000000000')
    """

    kg = Decimal(1)
    kilogram = Decimal(1)
    kilograms = Decimal(1)
    ton = Decimal(1000)
    mg = Decimal(1000)  # mega-gram, should be Mg
    t = Decimal(1000)
    metric_ton = Decimal(1000)
    kiloton = Decimal(1_000_000)
    kt = Decimal(1_000_000)
    gg = Decimal(1_000_000)  # giga-gram, should be Gg
    megaton = Decimal(1_000_000_000)
    pg = Decimal(1_000_000_000)  # peta-gram, should be Pg
    mt = Decimal(1_000_000_000)


class MassUnit(Unit[Mass]):
    """
    Mass Unit mixin for Aspects.

    >>> mu = MassUnit()
    >>> mu.parse("1 kg")
    Measure(measure=Decimal('1'), description='1 kg', difficulty=Decimal('0'))
    >>> mu.parse(2, "kg")
    Measure(measure=Decimal('2'), description='2 kg', difficulty=Decimal('2'))
    >>> mu.parse("kg")
    Measure(measure=Decimal('1'), description='1 kg', difficulty=Decimal('0'))
    >>> mu.parse(3)
    Measure(measure=Decimal('3'), description='3 kg', difficulty=Decimal('3'))
    >>> mu.parse(4, Mass.kg)
    Measure(measure=Decimal('4'), description='4 kg', difficulty=Decimal('4'))
    """

    choices = Mass
    result_cls = Measure


class Distance(MatchingEnum):
    """
    All the distance scale factors.

    >>> scale = Distance.km.metric
    >>> scale
    Decimal('1000')
    >>> Distance.m.name
    'm'
    >>> scale = Distance['touch'].metric
    >>> scale
    Decimal('1')
    >>> Distance.meter
    <Distance.m: Decimal('1')>
    """

    m = Decimal(1)
    self = Decimal(1)  # Special case for <1m.
    touch = Decimal(1)  # Special case for <1m.
    m_per_second = Decimal(1)  # For rate, really.
    meter = Decimal(1)
    meters = Decimal(1)
    km = Decimal(1_000)
    kilometer = Decimal(1_000)
    kilometers = Decimal(1_000)


class DistUnit(Unit[Distance]):
    """
    Distance Unit mixin for Aspects.

    >>> du = DistUnit()
    >>> du.parse("1 m")
    Measure(measure=Decimal('1'), description='1 m', difficulty=Decimal('0'))
    >>> du.parse(2, "km")
    Measure(measure=Decimal('2000'), description='2 km', difficulty=Decimal('17'))
    >>> du.parse("m")
    Measure(measure=Decimal('1'), description='1 m', difficulty=Decimal('0'))
    >>> du.parse(3)
    Measure(measure=Decimal('3'), description='3 m', difficulty=Decimal('3'))
    >>> du.parse(4, Distance.km)
    Measure(measure=Decimal('4000'), description='4 km', difficulty=Decimal('18'))
    """

    choices = Distance
    result_cls = Measure


class Volume(MatchingEnum):
    """
    All the volume scale factors.

    >>> scale = Volume.l.metric
    >>> scale
    Decimal('1')
    >>> Volume.l.name
    'liter'
    >>> scale = Volume['liter'].metric
    >>> scale
    Decimal('1')
    """

    liter = Decimal(1)
    liters = Decimal(1)
    l = Decimal(1)


class VolumeUnit(Unit[Volume]):
    """
    Volume Unit mixin for Aspects.

    >>> vu = VolumeUnit()
    >>> vu.parse("1 l")
    Measure(measure=Decimal('1'), description='1 liter', difficulty=Decimal('0'))
    >>> vu.parse(2, "l")
    Measure(measure=Decimal('2'), description='2 liter', difficulty=Decimal('2'))
    >>> vu.parse("l")
    Measure(measure=Decimal('1'), description='1 liter', difficulty=Decimal('0'))
    >>> vu.parse(3)
    Measure(measure=Decimal('3'), description='3 liter', difficulty=Decimal('3'))
    >>> vu.parse(4, Volume.l)
    Measure(measure=Decimal('4'), description='4 liter', difficulty=Decimal('4'))
    """

    choices = Volume
    result_cls = Measure


class InvalidVolumeError(RuntimeError):
    pass


def cuberoot(n: Decimal) -> Decimal:
    cube = Decimal(1) / Decimal(3)
    return (n**cube).quantize(Decimal(1), rounding=decimal.ROUND_UP)


# Terminal types for parsing Area-Volume specifications

Number = NamedTuple("Number", [("text", str)])
Shape = NamedTuple("Shape", [("text", str)])
UnitName = NamedTuple("Unit", [("text", str)])
Axis = NamedTuple("Axis", [("text", str)])

type Token = Number | Shape | UnitName | Axis

# AST types used to parse Area-Volume specifications

Dimension = NamedTuple(
    "Dimension", [("distance", Decimal | None), ("unit", str | None), ("axis", str)]
)
ShapeSpec = NamedTuple("ShapeSpec", [("shape_name", str), ("axes", list[Dimension])])


class AreaVolumeUnit(Unit):
    r"""
    The Area (and Volume) ussd for AreaEffectAspect.
    Note that this is generally a Modifier, not a Measure.
    The computed value is already a difficulty.

    The values are generally very complex phrases:
    - {d} m|meter r|radius circle
    - {d} m|meter r|radius sphere
    - {d} m|meter r|radius hemisphere
    - {d} m|meter r|radius divination sphere
    - [{d} m|meter l|length|h|height|r|radius|base]+ cone
    - [{d} m|meter h|height|w|width]+ wall
    - [{d} m|meter h|height|w|width|d|depth]+ cuboid
    - [{d} m|meter l|length|h|height|r|radius|base]+ blast

    The rules include a "fluid shape", which is a modifier, not a measure.

    While we could define a sub-language of Python classes for this,
    we've left it as strings, since the examples all conform to a simple
    with no exceptions.

    The grammar for these shapes is the following.

    ..  code-block:: peg

        shape_spec: dimension+ SHAPE
        dimension: NUMBER UNIT AXIS | AXIS

    ..  code-block:: peg

        WHITESPACE: ' ' | 'and'
        NUMBER: DIGIT+
        UNIT: 'm' | 'meter' | 'meters'
        AXIS: 'radius' | 'height' | 'width' | 'base' | etc.
        SHAPE: 'circle' | 'sphere' | 'cuboid' | etc.

    The short form of the ``dimension`` -- only an axis name --
    means the number ond unit are cloned from the previous axis. Ugh.

    The **OpenD6 Magic Guide** rules are vague on how these shapes work.
    Here are reasonably accurate formulae for the various shapes.

    ..  csv-table::
        :header-rows: 1

        Shape,Measures,Equivalent Sphere R
        Hemisphere,radius :math:`r`,:math:`0.79 r`
        Cone,"height :math:`h`, base radius :math:`r`",:math:`0.63 \sqrt[3]{h r^{2}}`
        Cuboid,"height :math:`h`, width :math:`w`, depth :math:`d`",:math:`0.62 \sqrt[3]{d h w}`
        Cylinder,"height :math:`h`, radius :math:`r`",:math:`0.91 \sqrt[3]{h r^{2}}`
        Pyramid,"height :math:`h`, base width :math:`w`, base length :math:`l`",:math:`0.43 \sqrt[3]{h l w}`


    >>> avu = AreaVolumeUnit()
    >>> avu.parse("2 m radius circle")
    Modifier(difficulty=Decimal('4'), description='2m radius circle')
    >>> avu.parse("2 m radius sphere")
    Modifier(difficulty=Decimal('10'), description='2m radius sphere')
    >>> avu.parse("2 m radius hemisphere")
    Modifier(difficulty=Decimal('7'), description='2m radius hemisphere')
    >>> avu.parse("10 m radius divination sphere")
    Modifier(difficulty=Decimal('15'), description='10m radius divination sphere')
    >>> avu.parse("10 m length 5m radius cone")
    Modifier(difficulty=Decimal('22'), description='10m length 5m base cone')
    >>> avu.parse("10 m length 5m base cone")
    Modifier(difficulty=Decimal('22'), description='10m length 5m base cone')
    >>> avu.parse("1 meter height 2 meter width and depth cuboid")
    Modifier(difficulty=Decimal('6'), description='1m height 2m width 2m depth cuboid')
    """

    DEBUG = False

    def parse_str(self, text: str) -> tuple[Decimal, str]:
        """
        Parse the words of the area-of-effect string.
        Locate the axes distances and the shape, and compute the difficulty.

        This function contains a great deal of hidden complexity
        in the form of a string parser.

        :terminals:
            The token definitions for the grammar.

        :Token:
            A type alias for a union of various token types.

        :raw_tokens:
            A function to parse the string into tokens.

        :Tokenizer:
            A stateful iterator that can unget a token.
        """

        terminals = either(
            named_group("whitespace", either(WHITESPACE, "and")),
            named_group("number", one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS))),
            named_group(
                "shape",
                either(
                    "circle",
                    "sphere",
                    "hemisphere",
                    "divination" + one_or_more(WHITESPACE) + "sphere",
                    "cone",
                    "wall",
                    "cuboid",
                    "blast",
                ),
            ),
            named_group("unit", either("meter", "m")),
            # Others are possible, not not used in practice.
            named_group(
                "axis",
                either(
                    "radius",
                    "length",
                    "base",
                    "height",
                    "width",
                    "depth",
                    "r",
                    "l",
                    "h",
                    "w",
                    "d",
                ),
            ),
        )

        def raw_tokens(raw_text: str) -> Iterator[Token]:
            """Decompose the text into tokens: numbers, units, axes, and shapes."""
            start = 0
            while start < len(raw_text):
                if (match := re.match(terminals, raw_text[start:])) is None:
                    raise ValueError(f"unknown token in {raw_text[start:]!r}")
                if match["number"]:
                    yield Number(match["number"])
                elif match["shape"]:
                    yield Shape(match["shape"])
                elif match["unit"]:
                    yield UnitName(match["unit"])
                elif match["axis"]:
                    yield Axis(match["axis"])
                elif match["whitespace"]:
                    pass
                else:  # pragma: no cover
                    # None of the above. Whitespace or stop words
                    raise InvalidVolumeError(f"unknown {match!r} in {raw_text!r}")
                prev_start, start = start, start + match.end()
                if start == prev_start:  # pragma: no cover
                    raise InvalidVolumeError(
                        f"parsing problem in {raw_text[start:]!r} after {match!r}"
                    )

        class Tokenizer(Iterator[Token]):
            """..  todo:: Replace with a deque."""

            def __init__(self, text: str) -> None:
                self.tokens = list(raw_tokens(text))
                self.pos = 0

            def __next__(self) -> Token:
                if self.pos == len(self.tokens):
                    raise StopIteration
                else:
                    self.pos += 1
                    return self.tokens[self.pos - 1]

            def unget(self) -> None:
                self.pos -= 1

        # Shape parsers for the various grammar clauses.

        def parse_shape_spec(tokenizer: Tokenizer) -> ShapeSpec | None:
            """
            ..  code-block:: peg

                    shape_spec: dimension+ SHAPE
            """
            dimension_list: list[Dimension] = []
            dimension = parse_dimension(tokenizer)
            while dimension:
                dimension_list.append(dimension)
                dimension = parse_dimension(tokenizer)
            try:
                shape = next(tokenizer)
                if not isinstance(shape, Shape):
                    raise InvalidVolumeError  # pragma: no cover
            except StopIteration:
                raise InvalidVolumeError(f"no shape provided in {text!r}")
            if dimension_list:
                return ShapeSpec(shape.text, dimension_list)
            return None  # pragma: no cover

        def parse_dimension(tokenizer: Tokenizer) -> Dimension | None:
            """
            ..  code-block:: peg

                dimension: NUMBER UNIT AXIS | AXIS
            """
            # Normalize the axis names
            norm_name = {
                "r": "radius",
                "l": "length",
                "h": "height",
                "w": "width",
                "d": "depth",
            }

            try:
                first = next(tokenizer)
            except StopIteration:
                return None
            match first:
                case Number() as number:
                    # Get Unit and Axis
                    try:
                        unit = next(tokenizer)
                        if not isinstance(unit, UnitName):
                            raise InvalidVolumeError(
                                f"no unit in {text!r}"
                            )  # pragma: no cover
                        axis = next(tokenizer)
                        if not isinstance(axis, Axis):
                            tokenizer.unget()
                            axis = Axis("radius")
                    except StopIteration:  # pragma: no cover
                        raise InvalidVolumeError
                    # If there were more units (i.e., km, cm, etc.) apply unit scaling.
                    return Dimension(
                        Decimal(number.text),
                        unit.text,
                        norm_name.get(axis.text, axis.text),
                    )
                case Axis() as axis_only:
                    return Dimension(
                        None, None, norm_name.get(axis_only.text, axis_only.text)
                    )
                case _:
                    tokenizer.unget()
                    return None

        def axis_expansion(shape: ShapeSpec) -> dict[str, Decimal]:
            """
            Rewrite AltShape list of dimensions into a dictionary.
            Fill in omitted values from the previous value.

            Essentially ``{d.axis: d.distance for d in shape.axes}`` but with None's replaced.
            """

            def filler(axes: list[Dimension]) -> Iterator[tuple[str, Decimal]]:
                prev = Decimal(0)
                for ax in axes:
                    if ax.distance is not None:
                        prev = ax.distance
                        yield ax.axis, ax.distance
                    else:
                        yield ax.axis, prev

            return dict(filler(shape.axes))

        def shape_difficulty(shape: ShapeSpec) -> tuple[Decimal, str]:
            try:
                method_name = f"comp_{shape.shape_name.replace(' ', '_')}"
                if self.DEBUG:
                    print(method_name)
                method = getattr(self, method_name)
                axes = axis_expansion(shape)
                if self.DEBUG:
                    print(axes)
                diff_desc = method(**axes)
                if self.DEBUG:
                    print(diff_desc)
                return diff_desc
            except AttributeError:  # pragma: no cover
                raise ValueError(f"no shape provided in {text!r}")
            except KeyError:  # pragma: no cover
                raise ValueError(f"no area rule for {shape!r}")
            except Exception as ex:  # pragma: no cover
                raise ValueError(f"can't compute {shape!r}: {ex!r}")

        # The final computation: parse and compute difficulty.
        if shape_spec := parse_shape_spec(Tokenizer(text)):
            return shape_difficulty(shape_spec)
        raise ValueError(f"invalid shape {text!r}")  # pragma: no cover

    def comp_blast(self, length: Decimal, radius: Decimal) -> tuple[Decimal, str]:
        """
        +1 for the first meter of length and final width and
        +1 per each additional two meters (total) of length and/or
        width.

        Area equals 1 plus the ending width, with the result multiplied by half of the length.

        ..  todo:: Implement blast area of effect.
        """
        raise NotImplementedError  # pragma: no cover

    def comp_circle(self, radius: Decimal) -> tuple[Decimal, str]:
        """+1 per half-meter radius."""
        return 2 * radius, f"{radius}m radius circle"

    def comp_cone(
        self,
        length: Decimal | None = None,
        height: Decimal | None = None,
        base: Decimal | None = None,
        radius: Decimal | None = None,
    ) -> tuple[Decimal, str]:
        r"""
        The approximation in the rules is this:

            +5 for a basic cone two meters long and a base with
            a one-meter radius

            and +1 for each additional half meter of
            length or meter of base radius.

            Example: A cone
            that’s three meters long with a base two meters wide (radius
            of one meter) has a cost of +7.

        Which is close for a few small cones, but fails for large radius.

        The correct formula is to convert to an equivalent sphere.
        :math:`R = 0.63 \sqrt[3]{h r^{2}}`

        From this, the difficulty is :math:`5R`.
        """
        if length is not None:
            h = length
        elif height is not None:
            h = height
        else:
            raise ValueError("no length for cone")  # pragma: no cover
        if base is not None:
            r = base
        elif radius is not None:
            r = radius
        else:
            raise ValueError("no base for cone")  # pragma: no cover
        # volume = math.pi * h * r**2 / 3
        # return 2 * h + r, f"{h}m length {r}m base cone"
        R_sphere = Decimal("0.63") * cuberoot(h * r**2)
        return (5 * R_sphere).quantize(
            Decimal(1), rounding=decimal.ROUND_DOWN
        ), f"{h}m length {r}m base cone"

    def comp_cuboid(
        self, height: Decimal, width: Decimal, depth: Decimal
    ) -> tuple[Decimal, str]:
        r"""
        Rules say nothing more than (Volume equals length times width times height.)

        The correct formula is to convert to an equivalent sphere.
        :math:`R = 0.62 \sqrt[3]{d h w}`

        From this, the difficulty is :math:`5R`.
        """
        R_sphere = Decimal("0.62") * cuberoot(height * width * depth)
        return (5 * R_sphere).quantize(
            Decimal(1), rounding=decimal.ROUND_DOWN
        ), f"{height}m height {width}m width {depth}m depth cuboid"

    def comp_divination_sphere(self, radius: Decimal) -> tuple[Decimal, str]:
        """
        Look up the radius of the
        area of effect as a measure on the “Spell Measures” chart;
        double its corresponding value to get the value of the area
        of effect: divination circle aspect. Triple the “Spell Measures”
        value for three-dimensional areas.

        Examples: A divination circle with
        a one-meter radius costs one, while a divination sphere of
        the same size is two.
        """
        return 3 * m2v(radius), f"{radius}m radius divination sphere"

    def comp_hemisphere(self, radius: Decimal) -> tuple[Decimal, str]:
        r"""
        The approximation in the rules is this:

            +5 per meter radius, with a +1 bonus to hit the central target.
            This is a three-dimensional shape.
            (Volume equals 2 times pi times radius cubed divided by 3.)

        The correct formula is to convert to an equivalent sphere.
        :math:`R = 0.79 r`

        From this, the difficulty is :math:`5R`.
        """
        R_sphere = Decimal("0.79") * radius
        return (5 * R_sphere).quantize(
            Decimal(1), rounding=decimal.ROUND_DOWN
        ), f"{radius}m radius hemisphere"

    def comp_sphere(self, radius: Decimal) -> tuple[Decimal, str]:
        """+5 per meter radius and +1 bonus to hit one target"""
        return 5 * radius, f"{radius}m radius sphere"

    def comp_wall(self, height: Decimal, width: Decimal) -> tuple[Decimal, str]:
        """
        +1 for the first meter of length and width and +1 per
        each additional two meters (total) of length and/or width.

        (Area equals length times width.)
        """
        return (
            Decimal(1)
            + (height * width * Decimal("0.5")).quantize(
                Decimal(1), decimal.ROUND_DOWN
            ),
            f"{height}m height {width}m width wall",
        )

    def parse(self, *args: Any) -> Modifier:
        """Parse an Area of Effect string, creating a Modifier.

        There are no expedient definitions for this rather
        complicated aspect. There are a large number of alternatives,
        handled by the string parser.
        """
        match args:
            case (str(),) as single_text:
                (text,) = single_text
                return Modifier(*self.parse_str(text))
            case _:  # pragma: no cover
                raise ValueError(f"invalid {', '.join(map(repr, args))}")


class DiceUnit(Unit):
    """
    A Unit based on the DieCode used for numerous Effects and Aspects.
    Note that this is generally a Modifier, not a Measure.
    The computed value is already a difficulty.

    >>> du = DiceUnit()
    >>> du.parse("3D+2")
    Modifier(difficulty=Decimal('11'), description='3*D+2')
    >>> du.parse(3 * D + 2)
    Modifier(difficulty=Decimal('11'), description='3*D+2')
    """

    def parse(self, *args: Any) -> Modifier:
        """Parse an DiceUnit string, creating a Modifier."""
        match args:
            case (str(),) as single_text:
                dice = DieCode.parse_str(*single_text)
                return Modifier(dice.measure, repr(dice))
            case (DieCode(),) as die_code:
                (dice,) = die_code
                return Modifier(dice.measure, repr(dice))
            case _:  # pragma: no cover
                raise ValueError(f"invalid {', '.join(map(repr, args))}")


## Part III: Aspects and Effects


class GenericDifficultyDescription:
    """A mix-in for generic Aspects, where difficulty is often provided first.

    No swapping is done; this is the "normal" mode.

    This applies to ``NormalizedAspect.populate_details()`` processing for a few classes
    outside the simple class hierarchy.
    """

    def normalize_order(self, *args: Any) -> tuple[Any, ...]:
        return args


class GenericDescriptionMeasure:
    """A mix-in for GenericEffect, where the description is provided first, followed by a metric that provides difficulty.

    This applies to ``NormalizedAspect.populate_details()`` processing for a few classes
    outside the simple class hierarchy.
    """

    def normalize_order(self, *args: Any) -> tuple[Any, ...]:
        description, measure, *others = args
        return (measure, description) + tuple(others)


@logged
class Aspect:
    r"""Abstract Base Class for all Aspects and Effects.

    An ``Aspect`` defines Aspect-specific methods and detail parsers.
    It contains a :py:class:`NormalizedAspect`
    with the elaborated details of the Aspect.

    Each subclass of Aspect (and Effect) has a unique mix of parameter definitions.

    The base class can be initialized with a pre-computed difficulty.

    Additionally, a few aspect classes can have difficulties based on other aspects
    of a Spell.
    In this case, the parsing and finalization must be deferred until the Spell is
    finalized.
    A :py:class:`NormalizedAspectProxy` is used to hold details of the dependency relationship.

    Some Spells are "templates" and require details copied from another spell.
    In this case, an aspect will have a ``NormalizedAspectReference`` to hold this dependency relationship.
    """

    # A default to permit using Aspect directly, not a subclass with a mixin.
    incr_decr: ClassVar[Sign] = Sign.Decrease

    logger: logging.Logger  # Set by a decorator

    # State of being -- independent or depending on another aspect.
    base: NormalizedAspect | None  #: Finalized details of this aspect.
    proxy: (
        NormalizedAspectProxy | None
    )  #: Aspect depends on another aspect of this spell.
    reference: (
        NormalizedAspectReference | None
    )  #: Aspect depends on an aspect of another spell.

    def __init__(
        self,
        difficulty: Any,
        description: Any,
        *,
        proxy: NormalizedAspectProxy | NormalizedAspectReference | None = None,
        **kwargs: Any,
    ) -> None:
        """
        Unique argument values for an Aspect or Effect.
        This class also includes unique difficulty and description computations.
        Each subclass provides distinct lookup types for measures,
        modifiers, as well as factors.

        This method has two invocations.

        -   Independent, using ``Aspect(args...)``.
            This method creates a base ``NormalizedAspect``.
            The :py:meth:`NormalizedAspect.populate_details` parses the given arguments.

        -   Dependent, using ``Aspect.based_on('name', args...)``.
            This classmethod uses ``Aspect(args..., proxy=proxy)`` to
            provide a proxy setting.

            This is later finalized by the :py:class:`init_dependencies` method.
            This creates the base ``NormalizedAspect``.
            The :py:meth:`NormalizedAspect.populate_details` parses the deived arguments.
        """
        self.origin = ((difficulty, description), {})
        if proxy:
            match proxy:
                case NormalizedAspectProxy():
                    self.proxy = proxy
                    self.reference = None
                case NormalizedAspectReference():
                    self.proxy = None
                    self.reference = proxy
            self.base = None  # Will be replaced.
        else:
            self.proxy = None
            self.reference = None
            self.base = self.normalize_aspect(difficulty, description, **kwargs)

    def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
        """Default normalization process: populate the details from the Aspect's parsers."""
        return NormalizedAspect(self).populate_details(
            self.normalize_order(*args), **kwargs
        )

    def normalize_order(self, *args: Any) -> tuple[Any, Any]:
        raise NotImplementedError  # pragma: no cover

    @classmethod
    def based_on(
        cls, attr_paths: str | tuple[str, ...], *measures: Any, **kwargs: Any
    ) -> "Aspect":
        """Defines an Aspect with a difficulty based on another Aspect.
        The independent Aspect may **not** have been computed yet.
        Computation is delayed until :meth:`Spell.finalize`.

        Cases:

        -   ``SpeedAspect.based_on("range", description="Instantaneous")``
            The speed is given as a distance measure, implicitly per-second.
            The speed distance measure needs to be copied from the range distance measure.

        -   ``ConcentrationAspect.based_on("casting_time")``.
            The concentration time measure needs to be copied from the casting_time time measure.

        -   ``FocusedAspect.based_on(("effect", "duration"))``
            The focus difficulty is based on (effect.difficulty + duration.difficulty)/5.
            There's no measure, modifier, or factor for this.

        -   ``UnrealEffectAspect.based_on("effect", "difficulty 9")``
            The unreal effect difficulty is based on effect.difficulty * factor.
            This involves a mixture of the effect difficulty and a parsed factor value.
            This is perhaps the most complicated.
        """
        match attr_paths:
            case str():
                attr_path_text = (repr(attr_paths),)
            case Sequence():
                attr_path_text = tuple(map(repr, attr_paths))
            case _:  # pragma: no cover
                raise RuntimeError
        arg_text = (
            attr_path_text
            + tuple(map(repr, measures))
            + tuple(f"{name}={value!r}" for name, value in kwargs.items())
        )
        placeholder_aspect = cls(
            0,
            f"based_on({', '.join(arg_text)})",
            proxy=NormalizedAspectProxy(
                attr_paths=(
                    attr_paths if isinstance(attr_paths, tuple) else (attr_paths,)
                ),
                args=measures,
                kwargs=kwargs,
            ),
        )
        return placeholder_aspect

    @classmethod
    def based_on_spell(cls, attr_path: str) -> "Aspect":
        """
        Defines an Aspect that must be copied from another Spell.

        The ``shaped_by(spell)`` method will copy NormalizedAspects
        from the spell on which this depends.
        After the aspects are copied, the spell can be finalized.
        """
        placeholder_aspect = cls(
            0,
            f"based_on_spell({attr_path!r})",
            proxy=NormalizedAspectReference(attr_path),
        )
        return placeholder_aspect

    def derive_args(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """Compute arguments for a "based_on" definitions.

        This requires the :py:class:`NormalizedAspectProxy.get_dependencies` has
        interrogated the containing :py:class:`Spell` to get the definitions.

        This generic implementation copies the independent aspect's measure argument
        to create the based-on measure arguments.
        """
        if self.proxy is None:
            raise ValueError("not a based-on aspect")  # pragma: no cover

        # Args from a (single) depends-on aspect.
        assert len(self.proxy.attr_paths) == 1, (
            f"too many dependencies {self.proxy.attr_paths}"
        )
        (depends_on_aspect,) = self.proxy.depends_on.values()
        dep_args, dep_kwargs = depends_on_aspect.origin()

        # Combine the dependent args with any overrides from based_on.
        return (dep_args + self.proxy.args[2:], dep_kwargs | self.proxy.kwargs)

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        (difficulty, description, *_), _ = self.origin
        return Decimal(difficulty)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        (difficulty, description, *_), _ = self.origin
        return description

    def init_dependencies(self, proxy: NormalizedAspectProxy) -> Self:
        """Build an ``NormalizedAspect`` from a ``NormalizedAspectProxy``.
        The proxy was created by the :meth:`based_on` method.
        It was then updated by the :py:meth:`NormalizedAspectProxy.set_dependencies` method.

        The Aspect-specific ``derive_args`` method compute the
        argument values used to build the final ``NormalizedAspect``.
        """
        self.logger.debug("init_dependencies proxy=%r", proxy)
        args, kwargs = self.derive_args()
        self.base = self.normalize_aspect(*args, **kwargs)
        return self

    def _asdict(self) -> dict[str, Any]:
        args, kwargs = self.origin
        return {
            "class_": self.__class__.__name__,
            "args": args,
        } | (kwargs if kwargs else {})

    # @property
    # def is_ready(self) -> bool:
    #     """Ready for finalization: independent, self-contained, no dependencies."""
    #     return bool(self.base)

    @property
    def is_dependent(self) -> bool:
        """Depends on something else, derived, and base has not been computed yet."""
        return bool(self.proxy) and not bool(self.base)

    @property
    def is_reference(self) -> bool:
        """Depends on an aspect of a different spell and base has not been copied yet."""
        return bool(self.reference) and not bool(self.base)

    def difficulty(self) -> Decimal:
        """Delegate to NormalizedAspect or NormalizedAspectReference."""
        if self.base:
            return self.base.difficulty()
        (difficulty, _), _ = self.origin
        return Decimal(difficulty)

    def description(self) -> str:
        """Delegate to NormalizedAspect or NormalizedAspectReference."""
        if self.base:
            return self.base.description()
        (_, description), _ = self.origin
        return description

    def source(self) -> str:
        """Generic source for an Aspect.

        This reflects proxies (with based_on).
        It also reflects references (with based_on_spell).
        """

        def to_source(arg: Any) -> str:
            """Most things use repr(). There are exceptions, however.

            - Enum needs to become type.name
            - Limitations and Enhancements need to use source()
            """
            match arg:
                case Enum():
                    return f"{arg.__class__.__name__}.{arg.name}"
                case Limitation() | Enhancement() as lim_enh:
                    return lim_enh.source()
                case str():
                    return repr(arg)
                case Sequence() as seq:
                    return f"[{', '.join(to_source(item) for item in seq)}]"
                case _:
                    return repr(arg)

        if self.proxy:
            if len(self.proxy.attr_paths) == 1:
                (attr_paths,) = self.proxy.attr_paths
            else:
                attr_paths = self.proxy.attr_paths
            return f"{self.__class__.__name__}.based_on({attr_paths!r}, *{self.proxy.args!r}, **{self.proxy.kwargs!r})"
        elif self.reference and not self.base:
            return f"{self.__class__.__name__}.based_on_spell({self.reference.attr_path!r})"
        else:
            args, kwargs = self.origin
            arg_list = [to_source(arg) for arg in args] + [
                f"{name}={to_source(value)}" for name, value in kwargs.items() if value
            ]
            return f"{self.__class__.__qualname__}({', '.join(arg_list)})"

    def __eq__(self, other: Any) -> bool:
        match other:
            case Aspect() as other_aspect:
                return (
                    self.__class__ == other_aspect.__class__
                    and self.base == other_aspect.base
                    and self.proxy == other_aspect.proxy
                    and self.reference == other_aspect.reference
                    and self.incr_decr == other_aspect.incr_decr
                )
            case _:
                return NotImplemented


class Effect(IncreasesDifficulty, Aspect):
    """
    An extension to the Aspect class to define the spell's Effect.

    .. important:: Description and Difficulty argument order

        The description and difficulty for some ``Effect`` classes
        are generally reversed from the order defined for ``Aspect``.
        This follows the style of the published rules, which reversed
        Effect and Aspect displays.

    This class is abstract, and lacks a :py:meth:`normalize_order` method.
    The ``GenericEffect`` subclass is concrete, with order-swapping for
    the argument values.
    """

    def __init__(self, description: Any, difficulty: Any = 1, **kwargs: Any) -> None:
        # Normalization will swap these to match generic Aspect definition.
        self._skill = description
        super().__init__(description, difficulty, **kwargs)

    def skill(self) -> str:
        """Skill string, based (without other arrangements) on the measure."""
        return self._skill


class GenericEffect(GenericDescriptionMeasure, Effect):
    pass


class CharacteristicType(UniqueMatchingEnum):
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

    ..  note:: Spelling aliases are preserved, not collapsed into a canonical form.
    """

    stun_only = Decimal("0.75")
    protection_modifier = Decimal("1.5")
    physical_damage = Decimal(1)
    mental_damage = Decimal(1)
    damage_modifier = Decimal("1.5")
    only_effects_attack_spells = Decimal("1.5")
    ignore_nonmagical_armor = Decimal("1.5")
    ignores_nonmagical_armor = Decimal("1.5")
    ignore_all_armor = Decimal("2")
    ignores_all_armor = Decimal("2")
    skill = Decimal(1)
    skill_modifier = Decimal("1.5")
    attribute = Decimal("1.5")
    attribute_modifier = Decimal("2")
    extranormal_skill = Decimal("2")
    extranormal_skill_modifier = Decimal("2.5")
    extranormal_attribute_modifier = Decimal(3)


class CharacteristicFactor(Lookup[CharacteristicType]):
    """
    Maps a ``CharacteristicType`` and to a ``Factor``.

    >>> from opend6_tools.magic.spells import CharacteristicFactor
    >>> cf = CharacteristicFactor()
    >>> cf.parse("ignore all armor")
    Factor(factor=Decimal('2'), description='ignore_all_armor')
    >>> cf.parse("extranormal_skill_modifier")
    Factor(factor=Decimal('2.5'), description='extranormal_skill_modifier')
    >>> cf.parse(CharacteristicType.extranormal_skill_modifier)
    Factor(factor=Decimal('2.5'), description='extranormal_skill_modifier')
    """

    choices = CharacteristicType
    result_cls = Factor
    cutoff = 0.8


class CharactersticAdjustmentType(UniqueMatchingEnum):
    """
    Note: To have damage ignore non-magical armor, add 0.5
    to the value multiplier listed. To have protection against either
    magical or non-magical attacks (but not both), subtract 0.5 from
    the value multiplier listed.

    ..  important:: This is an adjustment to a factor!
    """

    ignore_non_magical_armor = Decimal("0.5")
    magical_only = Decimal("-0.5")
    non_magical_only = Decimal("-0.5")


class CharacteristicFactorAdjustment(Lookup[CharactersticAdjustmentType]):
    """
    >>> cfa = CharacteristicFactorAdjustment()
    >>> cfa.parse("ignore_non_magical_armor")
    Factor(factor=Decimal('0.5'), description='ignore_non_magical_armor')
    >>> cfa.parse(CharactersticAdjustmentType.non_magical_only)
    Factor(factor=Decimal('-0.5'), description='non_magical_only')
    """

    choices = CharactersticAdjustmentType
    result_cls = Factor
    cutoff = 0.8


@logged
class MeasureEffect[T_unit: Unit](GenericDifficultyDescription, Effect):
    """Generic Class for all measure-based effects.

    Requires a specific subclass of ``Unit`` to provide a parser for measures.
    ``DiceUnit`` provides a ``Modifier`` with the difficulty provided directly.
    Most others provide a ``Measure`` with a measure-to-value conversion to get a difficulty.
    """

    measure_cls: type[Parser] | None = None
    modifier_cls: type[Parser] | None = None
    factor_cls: type[Parser] | None = CharacteristicFactor
    factor_adj_cls: type[Parser] | None = CharacteristicFactorAdjustment

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        base_difficulty = sum(aspect.difficulty_details(self.measure_cls), Decimal(0))
        modifiers = sum(aspect.difficulty_details(self.modifier_cls), Decimal(0))
        factors = list(aspect.factor_details(self.factor_cls))
        factor_adj = sum(aspect.factor_details(self.factor_adj_cls))
        max_factor = max(factors) if factors else Decimal(1)
        factors = max_factor + factor_adj
        difficulty = ((base_difficulty + modifiers) * factors).quantize(
            Decimal(1), rounding=decimal.ROUND_UP
        )
        return difficulty

    def compute_description(self, aspect: NormalizedAspect) -> str:
        skills_text = " ".join(aspect.notes)
        measures_text = "; ".join(aspect.description_details(self.measure_cls))
        modifiers_text = "; ".join(
            map(de_enumify, aspect.description_details(self.modifier_cls))
        )
        factors_text = ", ".join(
            chain(
                map(de_enumify, aspect.description_details(self.factor_cls)),
                map(de_enumify, aspect.description_details(self.factor_adj_cls)),
            )
        )

        description = (
            (
                f"{skills_text} {measures_text} {modifiers_text}"
                + (f" ({factors_text})" if factors_text else "")
            )
            .replace("  ", " ")
            .strip()
        )
        return description

    def __init__(self, *args: Any) -> None:
        self.origin = (args, {})
        self.base = self.normalize_aspect(*Parser.decompose(args))
        self.proxy = None
        self.reference = None
        # print(self.base)
        if skills_text := " ".join(self.base.notes):
            self._skill = skills_text
        else:
            measures_text = (
                "; ".join(d.description for d in self.base.details[self.measure_cls])
                if self.measure_cls
                else ""
            )
            self._skill = measures_text


@logged
class DamageEffect(MeasureEffect[DiceUnit]):
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

    >>> damage = DamageEffect("Body damage", "+4D+1")
    >>> damage.difficulty()
    Decimal('13')
    >>> damage.description()
    'Body damage 4*D+1'
    >>> damage.incr_decr
    <Sign.Increase: 1>
    >>> damage.source()
    "DamageEffect('Body damage', '+4D+1')"

    >>> d2 = DamageEffect('Dart', '+4D', 'physical damage; damage modifier')
    >>> d2.difficulty()
    Decimal('18')
    >>> d2.description()
    'Dart...'

    """

    modifier_cls = DiceUnit


@logged
class ProtectionEffect(MeasureEffect[DiceUnit]):
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


    >>> protection = ProtectionEffect("Damage Resistance", "+4D+1", "physical damage", "ignore all armor")
    >>> protection.difficulty()
    Decimal('26')
    >>> protection.description()
    'Damage Resistance 4*D+1 (physical damage, ignore all armor)'
    >>> protection.incr_decr
    <Sign.Increase: 1>
    >>> protection.source()
    "ProtectionEffect('Damage Resistance', '+4D+1', 'physical damage', 'ignore all armor')"
    """

    modifier_cls = DiceUnit


@logged
class SkillEffect(GenericDescriptionMeasure, MeasureEffect[DiceUnit]):
    """An Effect of a Spell or Miracle that boosts a Skill.
    It uses DieCodes for units.
    (see :external:ref:`fantasy.magic.applying_the_effect`.)

    Rules:

        Damage spells affect character health (that is, their Body
        Points or Wounds). To hurt someone, 6D (which you can
        determine, by using the "Die Code" table, has a value of 18)
        is a safe bet. To kill someone outright, lOD (which has a value
        of 30) is usually necessary.

        ...

        Spells that increase, decrease, create, or otherwise affect attributes
        or skills are determined the same way [using the "Die Code" table].
        For example, a spell to take
        over someone's mind would give the caster a persuasion of +3D or
        more with a value of at least 14.

        [*This doesn't follow. 3D is 9. 4D+2 is 14.*]

    Example from the :external:ref:`fantasy.magic.die_codes`:

    ..  csv-table:

        Stand-alone die code or non-Extranormal skill, 1
        Non-Extranormal skill modifier, 1.5

    >>> skill = SkillEffect("Physique: lifting", "+5D")
    >>> skill.difficulty()
    Decimal('15')
    >>> skill.description()
    'Physique: lifting 5*D'
    >>> skill.incr_decr
    <Sign.Increase: 1>
    >>> skill.source()
    "SkillEffect('Physique: lifting', '+5D')"

    Note the order is reversed from generic Aspect.
    This follows the pattern of generic Effect, with description first and measure information second.
    """

    modifier_cls = DiceUnit


@logged
class AttributeEffect(MeasureEffect[DiceUnit]):
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

    >>> attr = AttributeEffect("Physique", "+5D", "attribute modifier")
    >>> attr.difficulty()
    Decimal('30')
    >>> attr.description()
    'Physique 5*D (attribute modifier)'
    >>> attr.incr_decr
    <Sign.Increase: 1>
    >>> attr.source()
    "AttributeEffect('Physique', '+5D', 'attribute modifier')"
    """

    modifier_cls = DiceUnit


def enumify(text: str) -> str:
    """Make a Python symbol from a word or phrase.
    This is lossy and not fully reversible.

    >>> enumify("Possession: Limited")
    'possession_limited'
    >>> enumify("Infravision/Ultravision")
    'infravision_ultravision'
    >>> enumify("difficulty 13")
    'difficulty_13'
    """
    text = text.strip().lower()
    fix = [c for c in text if not (c.isalnum() or c == "_")]
    for c in fix:
        text = text.replace(c, "_")
    while "__" in text:
        text = text.replace("__", "_")
    return text


def de_enumify(text: str) -> str:
    """Recover (partially) a word or phrase turned into a Python symbol.

    >>> de_enumify('possession_limited')
    'possession limited'
    >>> de_enumify('infravision_ultravision')
    'infravision ultravision'
    """
    return text.replace("_", " ")


def parse_rule_table(table: str) -> Iterator[tuple[str, str]]:
    """Parse a rule table with ``name (number)`` or ``name (Rnumber)``"""
    ability_pattern = (
        group(one_or_more_lazy(ANYCHAR))
        + zero_or_more(WHITESPACE)
        + OPEN_PAREN
        + zero_or_more(WHITESPACE)
        + group(one_or_more_lazy(ANYCHAR))
        + zero_or_more(WHITESPACE)
        + CLOSE_PAREN
    )
    clean = filter(None, (row.strip() for row in table.splitlines()))
    for line in clean:
        if match := re.match(ability_pattern, line):
            yield match.group(1), match.group(2)
        else:
            raise SyntaxError(
                f"invalid {line!r}, doesn't match {ability_pattern!r}"
            )  # pragma: no cover


SPECIALABILITY_RULES = dedent(  # type: ignore
    """
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
    """
)


class SpecialAbilityType(UniqueMatchingEnum):
    """
    The defined Special Abilities, and their costs.
    (See :external:ref:`options.special_abilities`.)

    >>> ability = SpecialAbilityType.match("Possession: Limited")
    >>> (ability.metric, ability.name)
    (Decimal('8'), 'possession_limited')
    """

    _ignore_ = ["source", "label", "val", "number", "words"]
    SpecialAbilityType = vars()  # type: ignore
    for label, val in parse_rule_table(SPECIALABILITY_RULES):
        number, *words = val.split()  # type: ignore
        SpecialAbilityType[enumify(label)] = Decimal(number)


class SpecialAbilityLookup(QualifiedLookup[SpecialAbilityType]):
    choices = SpecialAbilityType
    result_cls = Modifier
    cutoff = 0.9


class LimitationType(UniqueMatchingEnum):
    """
    The defined Special Ability Limitations, and their costs.
    (See :external:ref:`options.special_abilities.limitations`.)

    >>> ability = LimitationType.match("Burn-out")
    >>> (ability.metric, ability.name)
    (Decimal('1'), 'burn_out')

    ..  todo:: Handle the more complex price-per-rank rules implied by the table.
    """

    _ignore_ = ["source", "label", "val", "number", "words"]
    source = dedent(  # type: ignore
        """\
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
    """
    )
    LimitationType = vars()  # type: ignore
    for label, val in parse_rule_table(source):
        number, *words = val.split()  # type: ignore
        LimitationType[enumify(label)] = Decimal(number)


class LimitationLookup(Lookup[LimitationType]):
    choices = LimitationType
    result_cls = Modifier


class Limitation(DecreasesDifficulty, Effect):
    """
    A Limitation that can be applied to a SpecialAbilityEffect.

    >>> lim = Limitation("Restricted", 2, "ability uncontrolled by target")
    >>> lim.difficulty()
    Decimal('2')
    >>> lim.description()
    'restricted (R2) ability uncontrolled by target'

    ..  todo:: Unify Limitation, Enhancement, DisadvantageEffect
    """

    modifier_cls: type[Parser] | None = LimitationLookup

    def __init__(
        self,
        description: str | LimitationType,
        rank: str | int,
        note: str = "",
    ) -> None:
        self.origin = ((description, rank, note), {})
        self.base = NormalizedAspect(self)
        self.base.rank = Decimal(rank)
        self.base.notes = [note]
        self.base.populate_details([description])
        self.proxy = None
        self.reference = None

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        rank = aspect.rank or Decimal(1)
        return rank * sum(aspect.difficulty_details(self.modifier_cls), Decimal(0))

    def compute_description(self, aspect: NormalizedAspect) -> str:
        limitations = aspect.description_details(self.modifier_cls)
        description = ", ".join(limitations)
        notes = " ".join(aspect.notes)
        return f"{description} (R{aspect.rank}) {notes}".strip()


class EnhancementType(UniqueMatchingEnum):
    """
    The defined Special Ability Enhancements, and their costs.
    (See :external:ref:`options.special_abilities.enhancements`.)

    >>> ability = EnhancementType.match("Extended Range")
    >>> (ability.metric, ability.name)
    (Decimal('3'), 'extended_range')

    ..  todo:: Handle the more complex price-per-rank rules implied by the table.
    """

    _ignore_ = ["source", "label", "val", "number", "words"]
    source = dedent(  # type: ignore
        """\
    Additional Effect (1)
    Bestow (1 or more)
    Extended Range (3)
    Magically Empowered (4 for 1 rank; 5 for 2 ranks)
    Multiple Targets (2)
    """
    )
    EnhancementType = vars()  # type: ignore
    for label, val in parse_rule_table(source):
        number, *words = val.split()  # type: ignore
        EnhancementType[enumify(label)] = Decimal(number)


class EnhancementLookup(Lookup[EnhancementType]):
    choices = EnhancementType
    result_cls = Modifier


class Enhancement(Effect):
    """
    A Limitation that can be applied to a SpecialAbilityEffect.

    >>> lim = Enhancement("Extended Range", 2)
    >>> lim.difficulty()
    Decimal('6')
    >>> lim.description()
    'extended_range (R2)'

    Interestingly, the only example is better described as an Effect

    Effect(description="related special ability", note="up to 19 points — not ranks — of related Special Abilities, with additional ranks in a Special Ability equalling the point cost of the first rank", difficulty=19)

    ..  todo:: Unify Limitation, Enhancement, DisadvantageEffect

    """

    modifier_cls = EnhancementLookup

    def __init__(
        self,
        description: str | EnhancementType,
        rank: str | int,
        note: str = "",
    ) -> None:
        self.origin = ((description, rank, note), {})
        self.base = NormalizedAspect(self)
        self.base.rank = Decimal(rank)
        self.base.notes = [note]
        self.base.populate_details([description])
        self.proxy = None
        self.reference = None

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        rank = aspect.rank or Decimal(1)
        return rank * sum(aspect.difficulty_details(self.modifier_cls), Decimal(0))

    def compute_description(self, aspect: NormalizedAspect) -> str:
        limitations = aspect.description_details(self.modifier_cls)
        description = ", ".join(limitations)
        notes = " ".join(aspect.notes)
        return f"{description} (R{aspect.rank}) {notes}".strip()


@logged
class SpecialAbilityEffect(Effect):
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

    >>> eff_1 = SpecialAbilityEffect("Extra Sense: Bugs", 3)
    >>> eff_1.difficulty()
    Decimal('9')
    >>> eff_1.description()
    'extra_sense: bugs (R3)'
    >>> eff_1.source()
    "SpecialAbilityEffect('Extra Sense: Bugs', 3, '')"

    Ability cost = 1, ranks = 3, (x3) = 9

    >>> eff_2 = SpecialAbilityEffect("Accelerated Healing", 7)
    >>> eff_2.difficulty()
    Decimal('63')
    >>> eff_2.description()
    'accelerated_healing (R7)'
    >>> eff_2.source()
    "SpecialAbilityEffect('Accelerated Healing', 7, '')"

    Ability cost = 3, ranks = 7, (x3) = 63

    >>> eff_3 = SpecialAbilityEffect("Possession: Full", 2)
    >>> eff_3.difficulty()
    Decimal('60')
    >>> eff_3.description()
    'possession_full (R2)'
    >>> eff_3.source()
    "SpecialAbilityEffect('Possession: Full', 2, '')"

    >>> eff_4 = SpecialAbilityEffect("Accelerated Healing", 2, modifications=Enhancement("Bestow", 2))
    >>> eff_4.difficulty()
    Decimal('30')
    >>> eff_4.description()
    'accelerated_healing (R2) ; bestow (R2)'

    Syntax is unique. Often stated as ``Ability[: Details] (R\\d)``.
    We break it into two parameters: the ``Ability[: Details]`` and the rank as a simple integer.
    The ``: Details`` suffix has one of two roles:

    -   It may be part of the ability name, or
    -   It may be an additional detail.

    BOTH options need to be checked.
    """

    effect_cls: type[Parser] | None = SpecialAbilityLookup

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        if aspect.rank is None:
            raise ValueError(
                f"missing rank for {self.__class__.__name__}"
            )  # pragma: no cover
        effects = aspect.difficulty_details(self.effect_cls)
        sa_cost = sum(effects, Decimal(0))
        enh_cost = sum((enh.difficulty() for enh in self.enhancements), Decimal(0))
        lim_cost = sum((lim.difficulty() for lim in self.limitations), Decimal(0))
        return Decimal((sa_cost + enh_cost - lim_cost) * aspect.rank * 3)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        effects = aspect.description_details(self.effect_cls)
        description = "; ".join(effects)
        notes = (
            [" ".join(aspect.notes)]
            + [lim.description() for lim in self.limitations]
            + [enh.description() for enh in self.enhancements]
        )
        return f"{description} (R{aspect.rank}) {'; '.join(notes)}".strip()

    def __init__(
        self,
        ability: str | SpecialAbilityType,
        rank: str | int,
        note: str = "",
        *,
        modifications: Limitation
        | Enhancement
        | list[Limitation | Enhancement]
        | None = None,
    ) -> None:
        self.origin = ((ability, rank, note), dict(modifications=modifications))
        self.base = NormalizedAspect(self)
        # self.base = super().normalize_aspect(ability)
        self.base.populate_details([ability])
        self.base.rank = Decimal(rank)
        self.base.notes = [note]
        self.proxy = None
        self.reference = None

        self.limitations: list[Effect] = []  # Usually Limitation
        self.enhancements: list[Effect] = []  # Usually Enhancement
        match modifications:
            case None:
                modifications = []
            case list():
                pass
            case Limitation() | Enhancement() | Effect():
                modifications = [modifications]
            case _:  # pragma: no cover
                raise ValueError(
                    f"must be list, Enhancement, or Limitation {modifications!r}"
                )
        for m in modifications:
            match m:
                case Limitation() as lim:
                    self.limitations.append(lim)
                case Enhancement() | Effect() as enh:
                    self.enhancements.append(enh)
                case _:  # pragma: no cover
                    raise ValueError(
                        f"must be Enhancement, Limitation, or Effect {m!r}"
                    )


# Also used by character module
DISADVANTAGE_RULES = dedent("""\
    Achilles' Heel (R3, R4); examples (R3): Allergy, Cultural Allergy, Environmental Incompatibility, Metabolic Difference, Nutritional Requirements, Rot, Vulnerability; examples(R4): Allergy, Cultural Allergy, Environmental Incompatibility, Rot, Symbiosis
    Advantage Flaw(R1, R2, R3); examples(R3): Infection, Minor Stigma, Stench
    Age(R1, R2)
    Bad Luck(R2, R3, R4)
    Burn-out (R1 or more)
    Cultural Unfamiliarity(R1, R2, R3)
    Debt(R1, R2, R3)
    Devotion(R1, R2, R3)
    Employed(R1, R2, R3)
    Enemy(R1, R2, R3)
    Hindrance(R1 or more); examples: Bad Knee, Gruffness / Arrogance, Trick Shoulder, Uncoordinated, Unobservant
    Infamy(R1, R2, R3)
    Language Problems(R2)
    Learning Problems(R1 per rank)
    Poverty(R1)
    Prejudice(R1, R2)
    Price(R1, R2)
    Quirk(R1, R2, R3); examples(R1): Dependency, Kleptomania, Indecision, Stutter; examples(R2): Dependency, Secret; examples(R3): Dependency, Paranoid, Phobic, Vengeful
    Reduced Attribute(R2 or more)
    """)


class DisadvantageType(UniqueMatchingEnum):
    """
    The defined Disadvantages, and their costs.
    (See :external:ref:`options.special_abilities.Disadvantages`.)

    >>> disadvantage = DisadvantageType.match("Infamy")
    >>> (disadvantage.metric, disadvantage.name)
    (Decimal('1'), 'infamy')

    ..  todo:: Handle minimum rank feature; not all Disadvatages permit R1.
    """

    _ignore_ = ["label", "val"]
    DisadvantageType = vars()  # type: ignore
    for label, val in parse_rule_table(DISADVANTAGE_RULES):
        DisadvantageType[enumify(label)] = Decimal(1)


class DisadvantageLookup(QualifiedLookup[DisadvantageType]):
    choices = DisadvantageType
    result_cls = Modifier


@logged
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

    ..  todo:: Unify Limitation, Enhancement, DisadvantageEffect

    Examples:

    >>> eff_1 = DisadvantageEffect("Hindrance: Initiative", 5, "-10 to all initiative totals")
    >>> eff_1.difficulty()
    Decimal('15')
    >>> eff_1.description()
    'hindrance: initiative (R5), -10 to all initiative totals'
    >>> eff_1.incr_decr
    <Sign.Increase: 1>
    >>> eff_1.incr_decr.value * eff_1.difficulty()
    Decimal('15')
    >>> eff_1.source()
    "DisadvantageEffect('Hindrance: Initiative', 5, '-10 to all initiative totals')"
    """

    modifier_cls: type[Lookup] = DisadvantageLookup

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        if aspect.rank is None:
            raise ValueError(
                f"missing rank for {self.__class__.__name__}"
            )  # pragma: no cover
        return aspect.rank * 3

    def compute_description(self, aspect: NormalizedAspect) -> str:
        modifiers = aspect.details[self.modifier_cls]
        description = "; ".join(m.description for m in modifiers)
        notes = " ".join(aspect.notes)
        return (
            f"{description} (R{aspect.rank}), {notes}"
            if notes
            else f"{description} (R{aspect.rank})"
        )

    def __init__(
        self, ability: str | DisadvantageType, rank: str | int, note: str = ""
    ) -> None:
        self.origin = ((ability, rank, note), {})
        self.base = NormalizedAspect(self)
        try:
            self.base.populate_details([ability])
        except ValueError:
            # We tolerate misspelled and unconventional disadvantages.
            self.base.details[self.modifier_cls] = [Modifier(Decimal(1), str(ability))]
        self.base.rank = Decimal(rank)
        self.base.notes = [note]
        self.proxy = None
        self.reference = None


@logged
class TimeEffect(MeasureEffect[TimeUnit]):
    """An Effect of a Spell or Miracle based on time.
     For example, one that adjusts duration of another spell.
     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> time = TimeEffect("Reduces duration", "10 min")
    >>> time.difficulty()
    Decimal('14')
    >>> time.description()
    'Reduces duration 10 min'
    >>> time.incr_decr
    <Sign.Increase: 1>
    >>> time.source()
    "TimeEffect('Reduces duration', '10 min')"
    """

    measure_cls = TimeUnit


@logged
class DistanceEffect(MeasureEffect[DistUnit]):
    """An Effect of a Spell or Miracle based on distance, usually Apportation.

     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> dist = DistanceEffect("Moves something", "1 km")
    >>> dist.difficulty()
    Decimal('15')
    >>> dist.description()
    'Moves something 1 km'
    >>> dist.incr_decr
    <Sign.Increase: 1>
    >>> dist.source()
    "DistanceEffect('Moves something', '1 km')"
    """

    measure_cls = DistUnit


@logged
class MassEffect(MeasureEffect[MassUnit]):
    """An Effect of a Spell or Miracle based on mass.
     (See :external:ref:`Spell Measures Table <fantasy.magic.spell_measures>`.)

    >>> mass = MassEffect("Moves", "100 kilograms")
    >>> mass.difficulty()
    Decimal('10')
    >>> mass.description()
    'Moves 100 kg'
    >>> mass.incr_decr
    <Sign.Increase: 1>
    >>> mass.source()
    "MassEffect('Moves', '100 kilograms')"
    """

    measure_cls = MassUnit


class VolumeEffect(MeasureEffect[VolumeUnit]):
    """An Effect of a Spell or Miracle based on volume.

    This may be a superfluous addition.
    All examples of this are -- perhaps -- better described
    with :external:ref:`Area Effect: Odd Shapes <magic_guide.aspects.area_odd_shapes>`.

    ..  todo:: Rethink VolumeEffect; this might really be AreaEffectAspect

    >>> vol = VolumeEffect("Creates", "100 liters")
    >>> vol.difficulty()
    Decimal('10')
    >>> vol.description()
    'Creates 100 liter'
    >>> vol.incr_decr
    <Sign.Increase: 1>
    >>> vol.source()
    "VolumeEffect('Creates', '100 liters')"
    """

    measure_cls = VolumeUnit


@logged
class CompositeEffect(Effect):
    """Combines two or more :py:class:`Effect` instances.
    All the Effects must be a subclass of :py:class:`IncreasesDifficulty`.

    Rules:

        A spell may contain more than one effect. Each effect is determined
        separately and added to the total. All of the effects must fall under
        the domain of the same skill. You should also list the skill used to
        cast the spell at this time. See the "Skills and Sample Effects" sidebar
        for suggestions.


    >>> e_1 = SkillEffect("Coordination: marksmanship", "+2D")
    >>> e_1.description()
    'Coordination: marksmanship 2*D'
    >>> e_2 = DamageEffect("Damage", "2*D")
    >>> e_2.description()
    'Damage 2*D'
    >>> composite = CompositeEffect("Magic Bullet", e_1, e_2)
    >>> composite.difficulty()
    Decimal('12')
    >>> composite.description()
    'Magic Bullet: Coordination: marksmanship 2*D; Damage 2*D'
    >>> composite.incr_decr
    <Sign.Increase: 1>
    >>> composite.source()
    "CompositeEffect('Magic Bullet', SkillEffect('Coordination: marksmanship', '+2D'), DamageEffect('Damage', '2*D'))"

    >>> composite_mod = CompositeEffect("Magic Bullet", e_1, e_2, modifications=Limitation("Side Effect", 2))
    >>> composite_mod.difficulty()
    Decimal('12')
    >>> composite_mod.description()
    'Magic Bullet: Coordination: marksmanship 2*D; Damage 2*D; all with side_effect (R2)'
    """

    def __init__(
        self,
        summary: str,
        *effects: Effect,
        modifications: Limitation
        | Enhancement
        | list[Limitation | Enhancement]
        | None = None,
    ) -> None:
        """Builds the CompositeEffect from a description and individual Effects.

        As with the :py:class:`SpecialAbilityEffect`, this can have modifications
        that apply to all of the individual effects.

        :param summary: A pithy summary
        :param effects: Individual :py:class:`Effect` instances.
        :param modifications: Limitations or Enhancements that apply to each Effect.
        """
        self.origin = (
            (summary, *effects),
            {"modifications": modifications} if modifications else {},
        )
        self.summary = summary
        self.effects = list(effects)
        self.modifications = (
            []
            if modifications is None
            else (
                list(modifications)
                if isinstance(modifications, (list, tuple))
                else [modifications]
            )
        )
        self._skill = summary
        self.base = NormalizedAspect(self)
        self.proxy = None
        self.reference = None

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        """Sum of component difficulties.

        ..  todo:: Apply modification to difficulty
        """
        return sum((e.difficulty() for e in self.effects), Decimal(0))

    def compute_description(self, aspect: NormalizedAspect) -> str:
        """Join of component descriptions and any modifications."""
        effects = "; ".join(e.description() for e in self.effects)
        if mods := "; ".join(m.description() for m in self.modifications):
            return f"{self.summary}: {effects}; all with {mods}"
        return f"{self.summary}: {effects}"

    def source(self) -> str:
        """Override Effect source to include all individual Effects."""
        text = [e.source() for e in self.effects]
        return f"{self.__class__.__name__}({self.summary!r}, {', '.join(text)})"


class ParsedAspect(abc.ABC, Aspect):
    """
    Generic base class for all aspects with a common parser structure.

    This decomposes string values by splitting on ";".

    ..  todo:: This could be Generic with respect to measure, modifier, and factor.
    """

    measure_cls: type[Parser] | None = None
    modifier_cls: type[Parser] | None = None
    factor_cls: type[Parser] | None = None

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        r"""Default difficulty computation.

        ..  math::

            (v(M) + \sum m) \times \prod f

        Where :math:`M` is any measure,
        :math:`m` is the list of modifiers,
        :math:`f` is the list of factors,
        and :math:`v(M)` is the conversion of measure to value.
        """
        measures = modifiers = Decimal(0)
        factors = Decimal(1)

        measures = sum(aspect.difficulty_details(self.measure_cls), Decimal(0))
        modifiers = sum(aspect.difficulty_details(self.modifier_cls), Decimal(0))
        factors = prod(aspect.factor_details(self.factor_cls))
        return ((measures + modifiers) * factors).quantize(
            Decimal(1), decimal.ROUND_DOWN
        )

    def compute_description(self, aspect: NormalizedAspect) -> str:
        details_text = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        return details_text

    def __init__(
        self,
        *args: Any,
        proxy: NormalizedAspectProxy | NormalizedAspectReference | None = None,
        **kwargs: Any,
    ) -> None:
        # For legacy v2 aspects, sometimes measure is provided via a keyword.
        if not args:
            for legacy in ("measure",):  # May be others...
                args += (kwargs.pop(legacy),) if legacy in kwargs else ()
        self.origin = (args, kwargs)
        if proxy:
            match proxy:
                case NormalizedAspectProxy():
                    self.proxy = proxy
                    self.reference = None
                case NormalizedAspectReference():
                    self.proxy = None
                    self.reference = proxy
            self.base = None
        else:
            self.proxy = None
            self.reference = None
            self.base = self.normalize_aspect(*args, **kwargs)

    def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
        return super().normalize_aspect(*Parser.decompose(args), **kwargs)


@logged
class GenericAspect(GenericDifficultyDescription, DecreasesDifficulty, Aspect):
    """Used by legacy definitions."""

    pass


@logged
class OtherAlterant(GenericDifficultyDescription, IncreasesDifficulty, Aspect):
    """
    Generic Aspect with simple description and difficulty.
    This is designed for the things like items listed as an "other alterant" of a Spell.

    If there are more than one aspect to an alterant,
    they can be combined with ``Other_Alterant([difficulty, description], [difficulty, description], etc.)``.

    (See :external:ref:`fantasy.magic.other_alterant`.)


    >>> alterant = OtherAlterant(2, "An Additional Nuance")
    >>> alterant.difficulty()
    Decimal('2')
    >>> alterant.description()
    'An Additional Nuance'
    >>> alterant.source()
    "OtherAlterant(2, 'An Additional Nuance')"
    """


@logged
class MeasureAspect[T_unit](GenericDifficultyDescription, ParsedAspect):
    """Generic Class for all measure-based Aspects."""


@logged
class TimeAspect(MeasureAspect[TimeUnit]):
    """A base class for any Aspects using :py:class:`TimeUnit`.

    # 2 rounds = 10 seconds
    >>> a = TimeAspect("2 rounds")
    >>> a.difficulty()
    Decimal('5')
    >>> a.description()
    '2 round'
    >>> a.source()
    "TimeAspect('2 rounds')"

    # 1.5 rounds = 7.5 seconds
    >>> b = TimeAspect("1.5 rounds")
    >>> b.difficulty()
    Decimal('5')
    >>> b.description()
    '1.5 round'
    >>> b.source()
    "TimeAspect('1.5 rounds')"

    """

    measure_cls = TimeUnit


@logged
class DistanceAspect(MeasureAspect[DistUnit]):
    """A base class for any Aspects using :py:class:`DistUnit`.

    >>> d = DistanceAspect("10 m")
    >>> d.difficulty()
    Decimal('5')
    >>> d.description()
    '10 m'
    >>> d.source()
    "DistanceAspect('10 m')"
    """

    measure_cls = DistUnit


@logged
class RangeAspect(IncreasesDifficulty, DistanceAspect):
    """The Range Aspect, implemented using the :py:class:`DistanceAspect`.

    (See :external:ref:`fantasy.magic.range`.)

    >>> r_15 = RangeAspect("15 m")
    >>> r_15.difficulty()
    Decimal('6')
    >>> r_15.description()
    '15 m'
    >>> r_15.incr_decr
    <Sign.Increase: 1>
    >>> r_15.source()
    "RangeAspect('15 m')"

    >>> r_0 = RangeAspect("1m")
    >>> r_0.difficulty()
    Decimal('0')
    >>> r_0.description()
    '1 m'
    >>> r_0.source()
    "RangeAspect('1m')"

    >>> r_self = RangeAspect(measure="self")
    >>> r_self.difficulty()
    Decimal('0')
    >>> r_self.description()
    '1 m'
    """


@logged
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

    >>> from types import SimpleNamespace
    >>> from opend6_tools.magic.spells import m2v
    >>> from decimal import Decimal

    >>> m2v(Decimal(15))
    Decimal('6')

    >>> ra = RangeAspect("15 m")
    >>> ra.difficulty()
    Decimal('6')
    >>> spell = SimpleNamespace(
    ...     aspects={'range': ra},
    ... )
    >>> speed_based = SpeedAspect.based_on("range", "Instantaneous")

    Mock ``finalize()`` process for spell.

    >>> speed_based.proxy.set_dependencies(spell)
    >>> _ = speed_based.init_dependencies(speed_based.proxy)
    >>> speed_based.base
    NormalizedAspect(SpeedAspect.based_on('range', *('Instantaneous',), **{}))
    >>> speed_based.difficulty()
    Decimal('6')
    >>> speed_based.description()
    'Instantaneous'
    >>> speed_based.source()
    "SpeedAspect.based_on('range', *('Instantaneous',), **{})"

    >>> sa = SpeedAspect("5 m_per_second")
    >>> sa.difficulty()
    Decimal('4')
    >>> sa.description()
    '5 m'
    """

    def derive_args(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """Arguments Speed "based_on(X)" definition -- get the measure from X.

        This uses the measure difficulty to compute the based-on difficulty.
        """
        if self.proxy is None:
            raise ValueError("not a based-on aspect")  # pragma: no cover
        assert len(self.proxy.depends_on.values()) == 1
        (depends_on_aspect,) = self.proxy.depends_on.values()
        proxy_args, kwargs = depends_on_aspect.origin()
        if not proxy_args:
            if "measure" in kwargs:
                proxy_args = (kwargs.pop("measure"),)
            else:
                proxy_args = ("Instantaneous",)
        # Combine the dependent args with any overrides from based_on.
        return (proxy_args + self.proxy.args, kwargs | self.proxy.kwargs)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        """Since this is generally "based_on", the description ignores the measures."""
        if self.proxy:
            return " ".join(aspect.notes)
        else:
            measures_text = "; ".join(aspect.description_details(self.measure_cls))
            return measures_text


@logged
class DurationAspect(IncreasesDifficulty, TimeAspect):
    """The Duration Aspect implemented using :py:class:`TimeAspect`.

    (See :external:ref:`fantasy.magic.duration`.)

    >>> duration = DurationAspect("1 min")
    >>> duration.difficulty()
    Decimal('9')
    >>> duration.description()
    '1 min'
    >>> duration.incr_decr
    <Sign.Increase: 1>
    >>> duration.source()
    "DurationAspect('1 min')"
    """


@logged
class CastingTimeAspect(DecreasesDifficulty, TimeAspect):
    """The Casting Time Aspect implemented using :py:class:`TimeAspect`.

    (See :external:ref:`fantasy.magic.casting_time`.)

    >>> casting_time = CastingTimeAspect("1 r")
    >>> casting_time.difficulty()
    Decimal('4')
    >>> casting_time.description()
    '1 round'
    >>> casting_time.incr_decr
    <Sign.Decrease: -1>
    >>> casting_time.source()
    "CastingTimeAspect('1 r')"
    """


class FluidAreaType(UniqueMatchingEnum):
    fluid = Decimal(6)
    fluid_shape = Decimal(6)


class FluidShapeModifier(Lookup[FluidAreaType]):
    choices = FluidAreaType
    result_cls = Modifier


@logged
class AreaEffectAspect(IncreasesDifficulty, MeasureAspect[AreaVolumeUnit]):
    """
    The Area of Effect Aspect.

    This can have multiple values; the spell difficulty is computed using the
    most difficult area, plus a modifier for the number of areas.

    Note "alternate shape" rules:
    One alternate shape adds 1,
    several alternate shapes adds 3.
    Alternates are separated by ``;`` or ``"or"``.

    (See :external:ref:`fantasy.magic.area_effect`.)

    The Magic Guidebook has numerous Area of Effect rules.
    See :external:ref:`magic_guide.aspects.area_divination`,
    and :external:ref:`magic_guide.aspects.area_odd_shapes`.

    Example:

    -   2.5m r circle is difficulty 5

    -   3m l 1m r cone is difficulty 7

    -   One Alternate shape adds 1

    We *assume* the base difficulty is the most difficult shape.

    >>> area_effect = AreaEffectAspect("2.5 m r circle; 3m l 1m r cone")
    >>> area_effect.description()
    '2.5m radius circle; 3m length 1m base cone; alternate shape'
    >>> area_effect.difficulty()
    Decimal('7')
    >>> area_effect.base.details[AreaVolumeUnit]
    [Modifier(difficulty=Decimal('5.0'), description='2.5m radius circle'), Modifier(difficulty=Decimal('6'), description='3m length 1m base cone')]
    >>> area_effect.source()
    "AreaEffectAspect('2.5 m r circle; 3m l 1m r cone')"

    # The rules have this stated as 5, using the not-quite correct simplified formula
    >>> sandman_cone = AreaEffectAspect("3m height 3m radius cone")
    >>> sandman_cone.difficulty()
    Decimal('9')
    >>> sandman_cone.description()
    '3m length 3m base cone'
    >>> sandman_cone.source()
    "AreaEffectAspect('3m height 3m radius cone')"

    # The rules have this stated as 15, using the not-quite correct simplified formula
    >>> wind_cone = AreaEffectAspect("8m h 4m r cone")
    >>> wind_cone.difficulty()
    Decimal('18')
    >>> wind_cone.description()
    '8m length 4m base cone'
    >>> wind_cone.source()
    "AreaEffectAspect('8m h 4m r cone')"

    >>> portcullis_wall = AreaEffectAspect("3m h 1m w wall")
    >>> portcullis_wall.difficulty()
    Decimal('2')
    >>> portcullis_wall.description()
    '3m height 1m width wall'
    >>> portcullis_wall.source()
    "AreaEffectAspect('3m h 1m w wall')"

    >>> fluid = AreaEffectAspect("1m sphere", "fluid shape")
    >>> fluid.difficulty()
    Decimal('11')
    >>> fluid.description()
    '1m radius sphere; fluid_shape'

    >>> many = AreaEffectAspect("1m sphere; 3m h 1m w wall; 8m h 4m r cone")
    >>> many.difficulty()
    Decimal('21')
    >>> many.description()
    '1m radius sphere; 3m height 1m width wall; 8m length 4m base cone; multiple alternate shapes'
    """

    measure_cls = AreaVolumeUnit
    modifier_cls = FluidShapeModifier

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        details = list(aspect.difficulty_details(self.measure_cls))
        modifiers = sum(
            (d for d in aspect.difficulty_details(self.modifier_cls)), Decimal(0)
        )
        if len(details) == 2:
            return max(details) + 1 + modifiers
        elif len(details) > 2:
            return max(details) + 3 + modifiers
        return details[0] + modifiers  # .quantize(Decimal(1))

    def compute_description(self, aspect: NormalizedAspect) -> str:
        details = list(aspect.description_details(self.measure_cls))
        if len(details) == 2:
            details.append("alternate shape")
        elif len(details) > 2:
            details.append("multiple alternate shapes")
        modifiers = list(aspect.description_details(self.modifier_cls))
        return "; ".join(details + modifiers)


class TargetType(UniqueMatchingEnum):
    targets = Decimal(5)
    target = Decimal(5)
    times = Decimal(5)


class ChangeTargetUnit(Unit[TargetType]):
    choices = TargetType
    result_cls = Modifier


@logged
class ChangeTargetAspect(
    GenericDifficultyDescription, IncreasesDifficulty, ParsedAspect
):
    """
    The Change Target Aspect.

    (See :external:ref:`fantasy.magic.change_target`.)

    >>> from opend6_tools.magic.spells import ChangeTargetUnit

    >>> change_target = ChangeTargetAspect("2 targets")
    >>> change_target.difficulty()
    Decimal('10')
    >>> change_target.description()
    '2 targets'
    >>> change_target.base.details[ChangeTargetUnit]
    [Modifier(difficulty=Decimal('10'), description='2 targets')]
    >>> change_target.source()
    "ChangeTargetAspect('2 targets')"

    ..`todo:: This can *also* be based_on("other_aspects.multi_target").

    """

    modifier_cls = ChangeTargetUnit


class ChargesType(UniqueMatchingEnum):
    charges = Decimal(1)
    improved_charges = Decimal(5)
    improved_charge = Decimal(5)


class ChargesUnit(Unit[ChargesType]):
    choices = ChargesType
    result_cls = Measure


@logged
class ChargesAspect(GenericDifficultyDescription, IncreasesDifficulty, ParsedAspect):
    """
    The Charges Aspect.

    (See :external:ref:`fantasy.magic.charges`.)

    (Also see :external:ref:`magic_guide.aspects.charges`.)

    ..  important::

        The Measures table is used to locate a value
        for the number of charges.

    >>> charges = ChargesAspect(10)
    >>> charges.difficulty()
    Decimal('5')
    >>> charges.description()
    '10 charges'
    >>> charges.source()
    'ChargesAspect(10)'

    >>> ci = ChargesAspect("3 improved charges")
    >>> ci.description()
    '3 improved_charges'
    >>> ci.difficulty()
    Decimal('6')
    >>> ci.source()
    "ChargesAspect('3 improved charges')"

    ..  todo:: Implement Charges with WARDS.

        1. Each condition: +10%.

        2. Optional skill to circumvent: -1 for difficulty 20
            Bigger reduction for lower difficilty.

        3. If circumvention allowed, requires speed < range.
    """

    modifier_cls = ChargesUnit


class CommunitySizeType(UniqueMatchingEnum):
    helpers = Decimal(1)


class CommunitySizeUnit(Unit[CommunitySizeType]):
    choices = CommunitySizeType
    result_cls = Measure


class CommunityParticipationType(UniqueMatchingEnum):
    simple_actions = Decimal("0.5")
    difficulty_11_action = Decimal("1")
    difficulty_13_action = Decimal("1.5")
    difficulty_15_action = Decimal("2")
    difficulty_17_action = Decimal("2.5")
    difficulty_21_action = Decimal("3")


class CommunityParticipationFactor(Lookup[CommunityParticipationType]):
    choices = CommunityParticipationType
    result_cls = Factor


@logged
class CommunityAspect(GenericDifficultyDescription, DecreasesDifficulty, ParsedAspect):
    """
    This has two distinct effects:

    1. The Community Modifier for the spell as a whole.
        Size Modifier * Participation Factor

    2. A separate difficulty applied to a mass skill roll for a large community given their skills and the inherent difficulty of the task.
       (Used for groups of NPC's.)

       This is 2 * m2v(number of helpers).

       Example: 31 helpers has a skill roll difficulty of 14.

    (See :external:ref:`fantasy.magic.community`.)

    >>> community = CommunityAspect("31 helpers", "Simple actions")
    >>> community.base.details
    defaultdict(<class 'list'>, {<class 'opend6_tools.magic.spells.CommunitySizeUnit'>: [Measure(measure=Decimal('31'), description='31 helpers', difficulty=Decimal('7'))], <class 'opend6_tools.magic.spells.CommunityParticipationFactor'>: [Factor(factor=Decimal('0.5'), description='simple_actions')]})
    >>> community.difficulty()
    Decimal('4')
    >>> community.description()
    '31 helpers; simple_actions (difficulty roll 14)'
    >>> community.source()
    "CommunityAspect('31 helpers', 'Simple actions')"
    """

    modifier_cls = CommunitySizeUnit
    factor_cls = CommunityParticipationFactor

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        """Special difficulty computation for community: modifiers + 1."""
        modifiers = sum(
            (d + 1 for d in aspect.difficulty_details(self.modifier_cls)), Decimal(0)
        )
        factors = prod(aspect.factor_details(self.factor_cls))
        return (modifiers * factors).quantize(Decimal(1), decimal.ROUND_DOWN)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        measures_text = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        difficulty_note = (
            f"difficulty roll {2 * sum(aspect.difficulty_details(self.modifier_cls))}"
        )
        notes_text = ", ".join(aspect.notes + [difficulty_note])
        return f"{measures_text} ({notes_text})"


class ComponentRarityType(UniqueMatchingEnum):
    ordinary = Decimal(1)
    very_common = Decimal(2)
    common = Decimal(3)
    uncommon = Decimal(4)
    rare = Decimal(4)
    very_rare = Decimal(5)
    extremely_rare = Decimal(6)
    unique = Decimal(7)


class ComponentRarityUnit(Lookup[ComponentRarityType]):
    choices = ComponentRarityType
    result_cls = Modifier


class ComponentQuantityType(UniqueMatchingEnum):
    from_1_3_components = Decimal(1)
    from_4_6_components = Decimal("0.75")
    over_6_components = Decimal("0.5")
    destroyed = Decimal(2)


class ComponentQuantityFactor(Lookup[ComponentQuantityType]):
    choices = ComponentQuantityType
    result_cls = Factor
    cutoff = 0.8


@logged
class ComponentsAspect(DecreasesDifficulty, ParsedAspect):
    """
    The Components Aspect, based on Rarity, Quantity, and Consumability of the components.

    (See :external:ref:`fantasy.magic.components`.)

    >>> components = ComponentsAspect("something", "uncommon; destroyed")
    >>> components.base.notes
    ['something']
    >>> components.difficulty()
    Decimal('8')
    >>> components.description()
    'something (uncommon; destroyed)'
    >>> components.source()
    "ComponentsAspect('something', 'uncommon; destroyed')"

    A more complicated description with multiple components.
    In the source text, "Black obsidian (uncommon, destroyed), dart (common)".
    >>> c2 = ComponentsAspect(
    ...     ["Black obsidian", "uncommon; destroyed"],
    ...     ["dart", "common"],
    ... )
    >>> c2.base.notes
    ['Black obsidian', 'dart']
    >>> c2.difficulty()
    Decimal('11')
    >>> c2.description()
    'Black obsidian (uncommon; destroyed); dart (common)'
    >>> str(c2.base)
    "CompositeNormalizedAspect parsers=['ComponentQuantityFactor', 'ComponentRarityUnit'], details={'ComponentRarityUnit': [Modifier(difficulty=Decimal('4'), description='uncommon')], 'ComponentQuantityFactor': [Factor(factor=Decimal('2'), description='destroyed')]}, {'ComponentRarityUnit': [Modifier(difficulty=Decimal('3'), description='common')], 'ComponentQuantityFactor': []}, notes=['Black obsidian', 'dart'], kwargs={}, _difficulty=Decimal('11'), _description='Black obsidian (uncommon; destroyed); dart (common)'"
    >>> c2.base == c2.base
    True
    >>> list(c2.base.difficulty_details(c2.measure_cls))
    [Decimal('0'), Decimal('0')]
    >>> list(c2.base.factor_details(c2.factor_cls))
    [Decimal('2'), Decimal('1')]
    >>> list(c2.base.description_details(c2.modifier_cls))
    ['uncommon', 'common']
    """

    modifier_cls = ComponentRarityUnit
    factor_cls = ComponentQuantityFactor

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        # TODO: Include a top-level ComponentQuantityType factor, if present.
        return super().compute_difficulty(aspect)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        # TODO: Include a top-level ComponentQuantityType factor, if present.
        notes = " ".join(aspect.notes)
        description = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        return f"{notes} ({description})"

    def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
        """The arguments have two forms:

        -   A single [note, modifier, factor] set. (Order doesn't matter.)
            The ``ComponentQuantityType.from_1_3_components`` is assumed.

        -   [note, modifier, factor], [note, modifier, factor], ...
            A value of ``ComponentQuantityType`` will be selected based on the number of components.

        As a simplification, a value of ``ComponentQuantityType`` can be provided in the first case.
        This is used where there are a lot of components, but they're not explicitly enumerated.

        Ths Normalized Aspect becomes rather complex.
        """
        match args:
            case (str() | MatchingEnum(), *_):
                # Strings and Enum values -- a single (note, modifier, factor) triple.
                base = NormalizedAspect(self)
                base.populate_details(tuple(Parser.decompose(args)), **kwargs)
                # TODO: Inject overall ComponentQuantityType.from_1_3_components
            case (Sequence(), *_) as multi_component:
                # Lists or Tuples of strings and enum values.
                base = CompositeNormalizedAspect(self)
                for component in multi_component:
                    base.populate_details(tuple(Parser.decompose(component)), **kwargs)
                    kwargs = {}
                # TODO: Inject overall ComponentQuantityType value based on number of components
            case _:  # pragma: no cover
                # Not sure what this might be, treat it like a string or enum.
                base = NormalizedAspect(self)
                base.populate_details(tuple(Parser.decompose(args)), **kwargs)
                # TODO: Inject overall ComponentQuantityType.from_1_3_components
        return base


@logged
class ConcentrationAspect(DecreasesDifficulty, TimeAspect):
    """
    Concentration time.
    Frequently ``ConcentrationAspect.based_on("casting_time")``
    Alternative ``ConcentrationAspect("3 sec", note="willpower difficulty 9")``, requires casting_time be >= 3sec

    The rules describe the aspect has having two distinct effects:

    1.  The Concentration Modifier for the spell as a whole.
        Measure-to-Value(time) / 3.

        'Use the "Spell Measures" table to determine
        the corresponding value for the concentration time measure; divide
        this value by 3 (round up) to determine the amount to add to the
        Negative Spell Total Modifiers.'

    2.  A separate difficulty for any distraction roll as part of the description.
        "mettle roll difficulty = {6+modifier}"

    (See :external:ref:`fantasy.magic.concentration`.)

    Note that the magic rules have examples of Concentration
    that do not align with the duration, but instead align with
    a the desired willpower/mettle roll.
    A roll of 16 means the base concentration difficulty must be adjusted to
    10, irrespective of the actual duration.

    This can be seen as a hidden modifier, or two alternative ways
    to set the difficulty for this aspect.

    -   Duration.

    -   Skill Roll.

    Note there are concentration distraction modifiers that
    also apply when the mettle roll is actually made during play.
    These have no bearing on the design of the spell.

    >>> from types import SimpleNamespace
    >>> cta = CastingTimeAspect("5 sec")
    >>> spell = SimpleNamespace(aspects={'casting_time': cta})
    >>> concentration_based = ConcentrationAspect.based_on("casting_time")

    Mock finalize() process for spell.

    >>> concentration_based.proxy.set_dependencies(spell)
    >>> _ = concentration_based.init_dependencies(concentration_based.proxy)
    >>> concentration_based.base.details
    defaultdict(<class 'list'>, {<class 'opend6_tools.magic.spells.TimeUnit'>: [Measure(measure=Decimal('5'), description='5 sec', difficulty=Decimal('4'))]})
    >>> concentration_based.difficulty()
    Decimal('2')
    >>> concentration_based.description()
    'Concentration: 5 sec (willpower/mettle roll 8)'
    >>> concentration_based.source()
    "ConcentrationAspect.based_on('casting_time', *(), **{})"

    >>> c_2 = ConcentrationAspect("1 round", mettle=13)
    >>> c_2.difficulty()
    Decimal('7')
    >>> c_2.description()
    'Concentration: 1 round (willpower/mettle roll 13)'
    >>> c_2.source()
    "ConcentrationAspect('1 round', mettle=13)"
    """

    def __init__(
        self,
        *args: Any,
        proxy: NormalizedAspectProxy | NormalizedAspectReference | None = None,
        **kwargs: Any,
    ) -> None:
        if "mettle" in kwargs:
            mettle_target = Decimal(kwargs["mettle"])
        else:
            mettle_target = None
        super().__init__(*args, proxy=proxy, **kwargs)
        if self.base:
            self.base.mettle_target = mettle_target
        elif self.proxy:
            # proxy... Must wait for init_dependencies...
            # Tweak the mettle kwarg into the proxy.
            self.proxy.kwargs["mettle"] = mettle_target

    def init_dependencies(self, proxy: NormalizedAspectProxy) -> Self:
        super().init_dependencies(proxy)
        # Extract the mettle_target from the proxy for later use.
        if self.base:
            self.base.mettle_target = proxy.kwargs.pop("mettle")
        return self

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        """Difficulty depends on duration or, it must match the desired mettle roll."""
        if aspect.mettle_target:
            diff = aspect.mettle_target - Decimal(6)
        else:
            base = sum(aspect.difficulty_details(self.measure_cls), Decimal(0))
            diff = (base / Decimal(3)).quantize(Decimal(1), decimal.ROUND_UP)
        return diff

    def compute_description(self, aspect: NormalizedAspect) -> str:
        description = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        mettle = self.difficulty() + Decimal(6)
        difficulty_note = f"willpower/mettle roll {mettle}"
        notes = " ".join(aspect.notes + [difficulty_note])
        return f"Concentration: {description} ({notes})"


class CountenanceVisibilityType(UniqueMatchingEnum):
    noticeable = Decimal(1)
    extreme = Decimal(2)


class CountenanceVisibilityModifier(Lookup[CountenanceVisibilityType]):
    choices = CountenanceVisibilityType
    result_cls = Modifier


@logged
class CountenanceAspect(
    GenericDifficultyDescription, DecreasesDifficulty, ParsedAspect
):
    """
    Countenance Aspect

    (See :external:ref:`fantasy.magic.countenance`.)

    >>> countenance = CountenanceAspect("red eyes", "noticeable")
    >>> countenance.difficulty()
    Decimal('1')
    >>> countenance.base.details
    defaultdict(<class 'list'>, {<class 'opend6_tools.magic.spells.CountenanceVisibilityModifier'>: [Modifier(difficulty=Decimal('1'), description='noticeable')]})
    >>> countenance.description()
    'red eyes (noticeable)'
    >>> countenance.source()
    "CountenanceAspect('red eyes', 'noticeable')"
    """

    modifier_cls = CountenanceVisibilityModifier

    def compute_description(self, aspect: NormalizedAspect) -> str:
        notes = " ".join(aspect.notes)
        description = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        return f"{notes} ({description})"


@logged
class FeedbackAspect(GenericDifficultyDescription, DecreasesDifficulty, Aspect):
    """
    Lowered resistance against feedback.
    This uses the modifier value directly, it's not a ``DieUnit``.

    The description includes the damage resistance change.

    (See :external:ref:`fantasy.magic.feedback`.)

    >>> feedback = FeedbackAspect(3)
    >>> feedback.difficulty()
    Decimal('3')
    >>> feedback.description()
    'lowered resistance'
    >>> feedback.source()
    "FeedbackAspect(3, 'lowered resistance')"
    """

    def __init__(self, measure: int) -> None:
        super().__init__(measure, "lowered resistance")


@logged
class FocusedAspect(GenericDifficultyDescription, IncreasesDifficulty, Aspect):
    """
    Focused aspect. Merely has to be present.
    Always use ``FocusedAspect.based_on(("effect", "duration"))``

    Difficulty is computed from (effect + duration)/5.

    (See :external:ref:`fantasy.magic.focused`.)

    >>> from types import SimpleNamespace
    >>> spell = SimpleNamespace(effect=DamageEffect("Damage", "5D"), aspects={"duration": DurationAspect("10 sec")})
    >>> focus_based = FocusedAspect.based_on(("effect", "duration"))
    >>> focus_based.origin
    ((0, "based_on('effect', 'duration')"), {})

    Mock finalize() for the spell

    >>> focus_based.proxy.set_dependencies(spell)
    >>> _ = focus_based.init_dependencies(focus_based.proxy)
    >>> focus_based.difficulty()
    Decimal('4')
    >>> focus_based.description()
    'Focus based on effect, duration'
    >>> focus_based.source()
    "FocusedAspect.based_on(('effect', 'duration'), *(), **{})"

    ..  todo:: Implement Multi_target weighting factor for FocusedAspect

    """

    def derive_args(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """Arguments for Focus "based_on" definition.

        Focus difficulty = (effect.difficulty + aspects['duration'].difficulty) / 5.

        Because there's no parsing required, the computation can be done here.
        Unlike UnrealEffectAspect, where the effect is stuffed into the base details for later use.
        """
        if self.proxy is None:
            raise ValueError("not a based-on aspect")  # pragma: no cover
        difficulty = (
            sum(dep.difficulty() for dep in self.proxy.depends_on.values()) / Decimal(5)
        ).quantize(Decimal(1))
        description = f"Focus based on {', '.join(self.proxy.attr_paths)}"
        # description = "; ".join(dep.description() for dep in self.proxy.depends_on.values())
        _, kwargs = self.origin
        return ((difficulty, description), kwargs)


class GestureComplexityType(UniqueMatchingEnum):
    very_simple = Decimal(1)
    simple = Decimal(2)  # was "fairly simple"
    complex = Decimal(3)
    very_complex = Decimal(4)
    extremely_complex = Decimal(5)
    challenging = Decimal(6)
    offensive = Decimal(1)
    difficulty_23 = Decimal(17)


class GestureComplexityModifier(QualifiedLookup[GestureComplexityType]):
    choices = GestureComplexityType
    result_cls = Modifier


@logged
class GesturesAspect(GenericDescriptionMeasure, DecreasesDifficulty, ParsedAspect):
    """Gestures Aspect

    (See :external:ref:`fantasy.magic.gesture`.)

    >>> gestures = GesturesAspect("waves hands", "simple; offensive")
    >>> gestures.difficulty()
    Decimal('3')
    >>> gestures.description()
    'waves hands (simple; offensive)'
    >>> gestures.source()
    "GesturesAspect('waves hands', 'simple; offensive')"

    >>> gestures2 = GesturesAspect("hand-dance", "complex (difficulty 11)")
    >>> gestures2.difficulty()
    Decimal('3')
    >>> gestures2.description()
    'hand-dance (complex (difficulty 11))'
    >>> gestures2.source()
    "GesturesAspect('hand-dance', 'complex (difficulty 11)')"

    ..  todo:: Refactor Gestures and Incantations; they're identical.
    """

    modifier_cls = GestureComplexityModifier

    # def __init__(self, *args: Any, proxy: NormalizedAspectProxy | None = None) -> None:
    #     super().__init__(*args, proxy=proxy)
    #     if not self.base:
    #         raise RuntimeError
    #     # self.base.notes.append(self.base._description)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        notes = " ".join(aspect.notes)
        description = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        return f"{notes} ({description})"


class IncantationComplexityType(UniqueMatchingEnum):
    word = Decimal(1)
    short = Decimal(1)
    phrase = Decimal(1)
    lengthy = Decimal(2)
    sentence = Decimal(2)
    complex = Decimal(3)
    litany = Decimal(4)
    complex_formula = Decimal(5)
    extensive_and_complex = Decimal(6)
    foreign_tongue = Decimal(1)
    loud = Decimal(1)
    offensive = Decimal(1)


class IncantationComplexityModifier(QualifiedLookup[IncantationComplexityType]):
    choices = IncantationComplexityType
    result_cls = Modifier


@logged
class IncantationsAspect(
    GenericDifficultyDescription, DecreasesDifficulty, ParsedAspect
):
    """Incantations aspect.
    For complex, and foreign, there's a difficulty roll involved.
    This is currently not computed.

    (See :external:ref:`fantasy.magic.incantation`.)

    ..  todo:: Compute additional difficulty roll as extra effect

    >>> incantations = IncantationsAspect("Die, scum", 'phrase; loud; offensive')
    >>> incantations.difficulty()
    Decimal('3')
    >>> incantations.description()
    'Die, scum (phrase; loud; offensive)'
    >>> incantations.source()
    "IncantationsAspect('Die, scum', 'phrase; loud; offensive')"
    """

    modifier_cls = IncantationComplexityModifier

    # def __init__(self, note: str, *args: Any, base: NormalizedAspectProxy | None = None) -> None:
    #     super().__init__(*args, base=base)
    #     if not self.base:
    #         raise RuntimeError
    #     self.base.notes.append(note)

    def compute_description(self, aspect: NormalizedAspect) -> str:
        notes = " ".join(aspect.notes)
        description = "; ".join(
            d.description for d_list in aspect.details.values() for d in d_list
        )
        return f"{notes} ({description})"


class MultiTargetType(UniqueMatchingEnum):
    targets = Decimal(3)


class MultiTargetUnit(Unit[MultiTargetType]):
    choices = MultiTargetType
    result_cls = Modifier


@logged
class MultipleTargetAspect(
    GenericDifficultyDescription, IncreasesDifficulty, ParsedAspect
):
    """Multi-target aspect.

    (See :external:ref:`fantasy.magic.multi_target`.)

    >>> multi_target = MultipleTargetAspect("3 targets")
    >>> multi_target.difficulty()
    Decimal('9')
    >>> multi_target.description()
    '3 targets'
    >>> multi_target.source()
    "MultipleTargetAspect('3 targets')"
    """

    modifier_cls = MultiTargetUnit


class UnrealDisbeliefType(UniqueMatchingEnum):
    difficulty_0 = Decimal("0.75")
    difficulty_9 = Decimal("0.5")
    difficulty_13 = Decimal("0.25")


class UnrealDisbeliefFactor(Lookup[UnrealDisbeliefType]):
    choices = UnrealDisbeliefType
    result_cls = Factor
    cutoff = 0.9


@logged
class UnrealEffectAspect(GenericDifficultyDescription, DecreasesDifficulty, Aspect):
    """
    For Illusions (i.e., Unreal Effect).
    Always use ``UnrealEffectAspect.based_on("effect", "difficulty n")``

    This depends on spell ``effect`` and a difficulty factor.
    This value is the difficulty adjustment, the spell effect weighted by the factor.

        Start with the spell effect's value, determined way back in "Effect
        & Skill Used." Then, when you decide how hard it is for a character
        to disbelieve the illusion, multiply the effect's value by the modifier
        multiplier. Round up. The resulting number is added to the Negative
        Spell Total Modifiers.

    (See :external:ref:`fantasy.magic.unreal_effect`.)

    >>> from types import SimpleNamespace
    >>> spell = SimpleNamespace(effect=GenericEffect("Whatever", 12), aspects={})
    >>> spell.effect.difficulty()
    Decimal('12')
    >>> unreal_effect_based = UnrealEffectAspect.based_on("effect", "difficulty 13")

    Mock finalize() process for spell.

    >>> unreal_effect_based.proxy.set_dependencies(spell)
    >>> _ = unreal_effect_based.init_dependencies(unreal_effect_based.proxy)
    >>> unreal_effect_based.difficulty()
    Decimal('3')
    >>> unreal_effect_based.description()
    'Unreal Effect: difficulty_13'
    >>> unreal_effect_based.source()
    "UnrealEffectAspect.based_on('effect', *('difficulty 13',), **{})"
    """

    factor_cls = UnrealDisbeliefFactor

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        if aspect.effect_difficulty is None:
            raise RuntimeError  # pragma: no cover
        effect_difficulty = aspect.effect_difficulty.difficulty
        factors = prod(aspect.factor_details(self.factor_cls))
        return (effect_difficulty * factors).quantize(Decimal(1))

    def compute_description(self, aspect: NormalizedAspect) -> str:
        measures_text = "; ".join(
            d.description for d in aspect.details[self.factor_cls]
        )
        return f"Unreal Effect: {measures_text}"

    def derive_args(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """Arguments for UnrealEffectAspect "based_on" definition.

        UnrealEffectAspect difficulty = effect.difficulty * factor.

        The factor is applied to the base difficulty
        during the finalize process.
        This is a kind of hybrid between two classes.
        Partly, it's an Aspect, defined by difficulty and description.
        Partly, it's a ParsedAspect defined by parsed factors.
        """
        if self.proxy is None:
            raise ValueError("not a based-on aspect")  # pragma: no cover
        difficulty = sum(
            (dep.difficulty() for dep in self.proxy.depends_on.values()), Decimal(0)
        )
        description = "; ".join(
            dep.description() for dep in self.proxy.depends_on.values()
        )
        args, kwargs = self.origin
        return ((difficulty, description), kwargs | {"factor": self.proxy.args[0]})

    def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
        """
        Special parsing rules for this aspect.

        The default normalization relies on ``*_cls`` class variables to
        define the list of parsers for processing args.

        In this case, however, we have a mixture
        of (difficulty, description) plus a factor.
        The factor could be parsed normally.
        The base difficulty, however, isn't parsed.

        The :meth:`NormalizedAspect.populate_details` handles either
        case, but doesn't handle this unique combination.

        The effect needs to be wedged into the details without any parsing.
        """
        difficulty = Modifier(*args)
        factor_cls = self.factor_cls
        base = NormalizedAspect(self)
        base.effect_difficulty = difficulty
        base.details[factor_cls] = [factor_cls().parse(kwargs["factor"])]
        return base


class VariableDurationType(UniqueMatchingEnum):
    off_only = Decimal(4)
    on_off_switch = (Decimal(8),)


class VariableDurationModifier(Lookup[VariableDurationType]):
    choices = VariableDurationType
    result_cls = Modifier


@logged
class VariableDurationAspect(
    GenericDifficultyDescription, IncreasesDifficulty, ParsedAspect
):
    """
    Several modifier options to end a spell early, turn a spell on and off.

    (See :external:ref:`fantasy.magic.variable_duration`.)

    >>> vd = VariableDurationAspect("on/off switch")
    >>> vd.difficulty()
    Decimal('8')
    >>> vd.description()
    'on_off_switch'
    >>> vd.source()
    "VariableDurationAspect('on/off switch')"
    """

    modifier_cls = VariableDurationModifier


@logged
class VariableEffectAspect(GenericDifficultyDescription, IncreasesDifficulty, Aspect):
    """
    Allows spell effects to be increased (or decreased.)

    +1 for every pip or point per direction per effect.

    See :external:ref:`fantasy.magic.variable_effect`.

    >>> ve = VariableEffectAspect("Can increase", 10)
    >>> ve.difficulty()
    Decimal('10')
    >>> ve.description()
    'Can increase'
    >>> ve.source()
    "VariableEffectAspect('Can increase', 10)"
    """


class VariableMovementType(UniqueMatchingEnum):
    accuracy_bonus = Decimal(2)
    bend_around_smaller = Decimal(1)
    bend_around_same_size = Decimal(3)
    find_invisible = Decimal(4)
    target_invisible = Decimal(4)


class VariableMovementModifier(Lookup[VariableMovementType]):
    choices = VariableMovementType
    result_cls = Modifier


@logged
class VariableMovementAspect(
    GenericDifficultyDescription, IncreasesDifficulty, ParsedAspect
):
    """
    A number of modifiers to move the target of a spell.

    Accuracy and Bending modifiers from Variable Movement.
    A Speed option via ``DistanceUnit``

    (See :external:ref:`fantasy.magic.variable_movement`.)

    >>> variable_movement = VariableMovementAspect("bend around same size")
    >>> variable_movement.difficulty()
    Decimal('3')
    >>> variable_movement.description()
    'bend_around_same_size'
    >>> variable_movement.source()
    "VariableMovementAspect('bend around same size')"

    >>> variable_movement_spd = VariableMovementAspect("5m")
    >>> variable_movement_spd.difficulty()
    Decimal('5')
    >>> variable_movement_spd.description()
    '5 m'
    >>> variable_movement_spd.source()
    "VariableMovementAspect('5m')"
    """

    measure_cls = DistUnit
    modifier_cls = VariableMovementModifier

    def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
        measure = sum(aspect.difficulty_details(self.measure_cls), Decimal(0))
        if measure:
            measure += 1
        modifiers = sum(aspect.difficulty_details(self.modifier_cls), Decimal(0))
        return measure + modifiers


@logged
class ArcaneKnowledgeAspect(GenericDescriptionMeasure, Aspect):
    """
    This is generally zero-cost. It's more like the skill characteristic of a Spell,
    not a proper Aspect.

    (See :external:ref:`magic_guide.skills.arcane_knowledge`, in the "Magic Guide.")

    >>> arcane = ArcaneKnowledgeAspect("dimension, time")
    >>> arcane.difficulty()
    Decimal('0')
    >>> arcane.description()
    'Arcane Knowledge: dimension, time'
    >>> arcane.source()
    "ArcaneKnowledgeAspect('dimension, time')"
    """

    def __init__(
        self,
        description: Any,
        difficulty: Any = None,
        proxy: NormalizedAspectProxy | None = None,
    ):
        if difficulty:
            raise ValueError("arcane knowledge has no difficulty")  # pragma: no cover
        super().__init__(description, None, proxy=proxy)

    def description(self) -> str:
        if not self.base:
            raise RuntimeError  # pragma: no cover
        return f"Arcane Knowledge: {self.base.description()}"

    def source(self) -> str:
        """Unlike most other Aspects, the source never has a difficulty.
        Only args[0] is converted.
        """
        if self.proxy:
            # It seems really unlikely to use a proxy for this.
            return super().source()  # pragma: no cover
        args, kwargs = self.origin
        arg_list = [repr(args[0])] + [
            f"{name}={value!r}" for name, value in kwargs.items() if value
        ]
        return f"{self.__class__.__qualname__}({', '.join(arg_list)})"


## Part IV: Spell, Miracle, Cantrip


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

    >>> from opend6_tools.magic import *

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
        This based_on_spell() feature is a bit more complicated.

    It helps to treat dependency as the base case,
    and a self-contained Aspect as well as an entirely self-contained Spell
    as a kind of degenerate case.

    Example of an attribute, speed, based_on range:

    >>> sleep = Spell(
    ...    name="Sleep",
    ...    skill="Temperamental Alteration",
    ...    notes="Physique, Coordination, Acumen, and Intellect are (temporarily) reduced, leading to fatique",
    ...    effect=DisadvantageEffect("Narcolepsy", 4, "-4D to mental and physical attributes"),
    ...    duration=DurationAspect(measure="1 hr"),
    ...    range=RangeAspect(measure="20 m"),
    ...    casting_time=CastingTimeAspect(measure="5 sec"),
    ...    speed=SpeedAspect.based_on(("range",), ""),
    ...    other_aspects={
    ...        "incantation": IncantationsAspect("Control Chant", "litany"),
    ...    },
    ...    other_conditions=[
    ...        GenericAspect(difficulty=0, description="Controller: Folme Agility")
    ...    ],
    ... )
    >>> sleep.range.difficulty()
    Decimal('7')
    >>> sleep.speed.difficulty()
    Decimal('7')

    A more complex example of a template spell.
    This is based on another spell's duration.
    A special ``finalize()`` is used to extract missing
    details from another spell to fine-tune the ``cast_chaos`` spell.

    >>> cast_chaos = Spell(
    ...     name="Cast Chaos",
    ...     skill="Conjuration",
    ...     notes="Simulate another spell, may work...",
    ...     effect=GenericEffect(description="Spell being copied plus backlash", difficulty=30),
    ...     duration=DurationAspect.based_on_spell("duration"),
    ... )

    >>> s1 = Spell(
    ...     name="Some Actual Spell",
    ...     effect=DamageEffect("3D", "physical"),
    ...     duration=DurationAspect("1hr"),
    ... )

    >>> cast_chaos.finalize(spell=s1)
    >>> cast_chaos.duration.difficulty()
    Decimal('18')
    >>> cast_chaos.duration.description()
    '1 hr'
    >>> cast_chaos.duration.base
    NormalizedAspect(DurationAspect('1hr'))

    There are two distinct ways to define these dependencies:

    -   Use an Aspect's :py:meth:`Aspect.based_on` class method to get the difficulty from aspects or effect of **this** spell.

    -   Use an Aspect's :py:meth:`Aspect.based_on_spell` to get one or more attribute difficulties (or effect difficulty or overall difficulty) from another spell.

    ..  note:: Finalization Details

        Generally, the :py:meth:`Spell.finalize` method works out the internal dependency total order.
        It must also be given any external values (i.e. Spells or whatever)
        required to create the effect and aspects.
    """

    def __init__(
        self,
        *,
        name: str,
        effect: Effect,
        **aspects: "Aspect | OtherAspects | list[Aspect]",
    ) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.name = name
        self.effect = effect
        self.other_aspects: OtherAspects = cast(
            OtherAspects, aspects.pop("other_aspects", {})
        )
        self.other_conditions: list[Aspect] = cast(
            list[Aspect], aspects.pop("other_conditions", [])
        )
        self.notes: str = cast(str, aspects.pop("notes", ""))
        self._skill: str = cast(str, aspects.pop("skill", ""))
        self.aspects: dict[str, Aspect] = cast(dict[str, Aspect], aspects)
        self._difficulty: Decimal | None = None

        self.finalize()

    def _asdict(self) -> dict[str, Any]:
        base = {
            "name": self.name,
            "effect": self.effect._asdict(),
            "notes": self.notes,
        } | {name: aspect._asdict() for name, aspect in self.aspects.items()}
        if self.other_aspects:
            base["other_aspects"] = {
                name: aspect._asdict()
                for name, aspect in cast(dict[str, Aspect], self.other_aspects).items()
            }
        if self.other_conditions:
            base["other_conditions"] = [
                cond._asdict() for cond in self.other_conditions
            ]
        return base

    def finalize(self, spell: "Spell | None" = None) -> None:
        """
        Assign all aspects to visible attribute names.
        Also, compute any required ``based_on`` Aspect values.

        The "based on" Aspects depend on various independent Aspects
        of a spell, including the Effect, and possibly
        modifiers and factors.

        The order of operations is a topological sort of defined aspects.

        All dependent aspects are then computed from the independent aspects.

        ..  important:: No based-on-spell references

            If there are any references, finalization is delayed
            until after the :py:meth:`shape` method.
        """
        # Validate aspects are indeed Aspects.
        bad = []
        for name, aspect in self.aspects.items():
            match aspect:
                case Aspect() | dict() | [Aspect()]:
                    pass
                case _:  # pragma: no cover
                    error = f"Problem: {name}={aspect!r} isn't recognized did you use 'note' for 'notes'?"
                    print(error)
                    bad.append(error)
        if bad:
            raise ValueError(*bad)  # pragma: no cover
        # First, make sure any external references are resolved.
        # If needed, "shape" this spell with values from another.
        references = {
            name: aspect for name, aspect in self.aspects.items() if aspect.is_reference
        }
        if references:
            if spell is None:
                self.logger.debug(
                    "Cannot finalize %r, depends on %s", self.name, references
                )
                # Build visible attributes.
                self._set_attributes()
                return

            # The shape() method will call finalize again,
            # with no argument values the second time.
            # This will retry finalization.
            spell.shape(spell, references)

        # Second, work out order of operations: Independent union Dependent
        self.logger.debug("Finalize %r", self.name)
        all_aspects = self._aspect_union()
        dependencies = {
            name: () for name in all_aspects if not all_aspects[name].is_dependent
        } | {
            name: all_aspects[name].proxy.attr_paths  # type: ignore
            for name in all_aspects
            if all_aspects[name].is_dependent
        }
        try:
            ordering = list(graphlib.TopologicalSorter(dependencies).static_order())
        except graphlib.CycleError:  # pragma: no cover
            print(self.source())
            raise
        self.logger.debug("Aspects %r", dependencies)

        # Third, finalize the dependent aspects, those waiting for details from independent aspects.
        for name in ordering:
            if name == "effect":
                # based_on named "effect": this is ignored because effect can't be based on.
                continue
            if name in self.aspects:
                target = self.aspects
            elif name in self.other_aspects:
                target = self.other_aspects
            else:
                # An "other condition".
                continue
            if (aspect := target[name]).is_dependent:
                self.logger.debug("Dependent Aspect %r", name)
                proxy: NormalizedAspectProxy = cast(NormalizedAspectProxy, aspect.proxy)
                proxy.set_dependencies(self)
                self.logger.debug("  proxy %r", proxy)
                aspect.init_dependencies(proxy)
                self.logger.debug("  new base %r", aspect.base)

        # Build visible attributes.
        self._set_attributes()

    def _set_attributes(self) -> None:
        """Expose the aspects as attributes."""
        self.logger.debug("Aspects %r", self.name)
        for name in self.aspects:
            # if hasattr(self, name):
            #     raise TypeError(f"invalid aspect name {name!r}")
            self.logger.debug(
                "  %s = %r, aspect.base=%r",
                name,
                self.aspects[name].source(),
                self.aspects[name].base,
            )
            setattr(self, name, self.aspects[name])

    def shape(self, other_spell: "Spell", references: dict[str, Aspect]) -> None:
        """Copy Aspects from another spell into this spell."""
        for name, aspect in references.items():
            aspect.base = other_spell.aspects[name].base
        self.finalize()

    def _aspect_union(self) -> dict[str, Aspect]:
        """A temporary copy of all aspects, flattened out."""
        return (
            {"effect": self.effect}
            | self.aspects
            | cast(dict[str, Aspect], self.other_aspects)
            | {
                f"condition: {shorten(oc.description(), 24)}": oc
                for oc in self.other_conditions
            }
        )

    @property
    def skill(self) -> str:
        if self._skill:
            return self._skill
        return self.effect.skill()

    @property
    def difficulty(self) -> int:
        """Compute Difficulty."""
        if self._difficulty is None:
            all_aspects = self._aspect_union()

            self._spell_total = {
                name: abs(aspect.difficulty())
                for name, aspect in all_aspects.items()
                if aspect.base is not None and aspect.base.sign() == Sign.Increase
            }
            self.logger.debug(
                "Spell Total        %r = %d",
                self._spell_total,
                sum(self._spell_total.values()),
            )

            self._negative_modifiers = {
                name: abs(aspect.difficulty())
                for name, aspect in all_aspects.items()
                if aspect.base is not None and aspect.base.sign() == Sign.Decrease
            }
            self.logger.debug(
                "Negative Modifiers %r = %d",
                self._negative_modifiers,
                sum(self._negative_modifiers.values()),
            )

            self._difficulty = (
                (
                    sum(self._spell_total.values())
                    - sum(self._negative_modifiers.values())
                )
                / Decimal("2.0")
            ).quantize(Decimal(1), decimal.ROUND_HALF_UP)
            self.logger.debug(
                "Difficulty ⎡(%d - %d) ÷ 2⎤ = %d",
                sum(self._spell_total.values()),
                sum(self._negative_modifiers.values()),
                self._difficulty,
            )

        return int(self._difficulty)

    def effect_details(self) -> str:
        """A debugging aid for the Effect computation."""
        if not self.effect.base:
            raise RuntimeError("effect should not use BasedOn")  # pragma: no cover
        details = [
            f"{n.__name__} {val_list}"
            for n, val_list in self.effect.base.details.items()
            if val_list
        ]
        return f"{self.effect.__class__.__name__} based on {', '.join(details)}"

    def source(self) -> str:
        kwargs = (
            dict(
                name=repr(self.name),
                effect=self.effect.source(),
            )
            | {name: value.source() for name, value in self.aspects.items()}
            | ({"notes": repr(self.notes)} if self.notes else {})
        )
        if self.other_aspects:
            aspects = ", ".join(
                f"{name!r}: {value.source()}"
                for name, value in cast(dict[str, Aspect], self.other_aspects).items()
            )
            kwargs |= dict(other_aspects=f"{{ {aspects} }}")
        arg_list = [f"{name}={value}" for name, value in kwargs.items()]
        if self.other_conditions:
            conditions = [value.source() for value in self.other_conditions]
            arg_list.append(f"other_conditions=[{', '.join(conditions)}]")
        return f"{self.__class__.__name__}({', '.join(arg_list)})"

    __repr__ = source

    def __eq__(self, other: Any) -> bool:
        match other:
            case Spell() as other_spell:
                # Force computation of difficulty.
                diff_computation = self.difficulty == other_spell.difficulty
                same = all(
                    [
                        diff_computation,
                        self.name == other_spell.name,
                        self.effect == other_spell.effect,
                        self.other_aspects == other_spell.other_aspects,
                        self.other_conditions == other_spell.other_conditions,
                        self.aspects == other_spell.aspects,
                    ]
                )
                return same
            case _:  # pragma: no cover
                return NotImplemented


class Miracle(Spell):
    """A subclass of :py:class:`Spell` for Invocations."""

    pass


Cantrip = Spell


class PriceDifficultyType(Enum):
    """
    From the PRICE DIFFICULTIES table.

        Cheap (a few copper coins),                                Very Easy (VE)
        Inexpensive (a few silver coins),                          Easy(E)
        Nominally expensive (several gold coins),                  Moderate (M)
        Somewhat expensive (a few handfuls of gold coins),         Difficult (D)
        Expensive (several handfuls of gold coins),                Very Difficult (VD)
        Very Expensive (hundreds of gold coins),                   Heroic (H)
        Costly [#fstar_eq]_ (thousands of gold coins),             Legendary (L)
    """

    VE = "very_easy"
    E = "easy"
    M = "moderate"
    D = "difficult"
    VD = "very_difficult"
    H = "heroic"
    L = "legendary"


class Item(Spell):
    """A subclass of :py:class`Spell` for magical items.

    Instead of a skill, provide type="" for the type of item.
    "potion", "ring", "wand", etc.

    Items can have three standard aspects:

    :duration:
        An instance of the :py:class:`DurationAspect` class.

    :range:
        An instance of the :py:class:`RangeAspect` class.

    :speed:
        An instance of the :py:class:`SpeedAspect` class.

    There are a number of interesting other_aspect values.
    ``AreaEffectAspect``, ``ChargesAspect``, ``FocusedAspect``,
    ``MultipleTargetAspect``.
    ``ConcentrationAspect``, ``FeedbackAspect``, ``UnrealEffectAspect``.
    """

    def __init__(
        self,
        *,
        name: str,
        effect: Effect,
        **aspects: "Aspect | OtherAspects | list[Aspect]",
    ) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.name = name
        self.effect = effect
        self.other_aspects: OtherAspects = cast(
            OtherAspects, aspects.pop("other_aspects", {})
        )
        self.other_conditions: list[Aspect] = cast(
            list[Aspect], aspects.pop("other_conditions", [])
        )
        self.notes: str = cast(str, aspects.pop("notes", ""))
        self.type: str = cast(str, aspects.pop("type", ""))
        self.price: str = cast(str, aspects.pop("price", ""))
        self.aspects: dict[str, Aspect] = cast(dict[str, Aspect], aspects)
        self._difficulty: Decimal | None = None

        self.finalize()
