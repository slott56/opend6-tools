"""
OpenD6 Spell Definitions and Computation.

DSL
====

An ``Aspect`` and ``Spell`` class.
Not very expressive of the real complications of Spell design.

Example
========

From *OpenD6 Magic Guidebook*, "Alternate Magic Systems".

>>> spell_1 = Spell(
...     name="Blink-Away",
...     effect = Apportation.move_1km,
...     duration = Duration.instant,
...     range = Range.self_or_touch,
...     casting_time = CastingTime.cast_1r,
... )
>>> spell_1.difficulty
13
>>> writer = SpellWriter()
>>> print(writer.report(spell_1))  # doctest: +NORMALIZE_WHITESPACE
Blink-Away
~~~~~~~~~~
<BLANKLINE>
:Skill: Apportation
:Difficulty: 13
:Effect: 30 (Move you or something 1 kilometer)
:Range: Self, touch, or 1 meter \\(0)
:Speed: 1 sec \\(0)
:Duration: Instantaneous \\(0)
:Casting Time: 1 round \\(-4)
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>

Conversion to Magic2
====================

Because we have an existing ``Aspect`` class,
this is a separate module.
A Conversion App loads ``magic1`` definitions and emits ``magic`` definitions.

Things that change (profoundly) from ``magic1``.

1. The time_aspect(), weight_aspect(), and distance_aspect() need to be simplified into Aspect subclassess.

    ::

        duration = Aspect(TIME, '5 sec')  # good
        duration = TimeAspect('5 sec')  # better
        duration = DurationAspect('5 sec')  # best

2.  A "DIE_CODE" unit for effects (mostly). Difficulty = 3 x Die + adjustment.

    ::

        effect = Aspect(DIE_CODE, "+3D", format="Damage: %{measure}")  # good
        effect = DieCodeAspect("+3D", format="Damage: %{measure}")  # better
        effect = DamageEffect("+3D")  # best

3.  Some other aspects are based on proper measures and standard units.
    Example: ConcentrationAspect is a TimeUnit.

4.  Introduce Modifiers and Factors.
    Modifiers are direct modifications to difficulty, without a measure -> value conversion.
    Factors are multiplicative adjustments to modifiers.

5.  Some aspects are based on others: speed == range, concentration == casting_time

    ::

        speed = SpeedAspect.based_on("range", description="Instantaneous"))

"""

from collections.abc import Iterator
import csv
from dataclasses import dataclass, asdict, field
from functools import singledispatchmethod
import logging
import math
import sys
from textwrap import dedent
from types import SimpleNamespace
from typing import Self, Any, ClassVar, TextIO

import jinja2
from jinja2 import Environment, DictLoader, Template, select_autoescape
from humre import *


@dataclass
class Aspect:
    """Generic aspect of a Spell."""

    format: str
    base_difficulty: float = 0.0
    count: int = 1
    skill: Any = field(
        init=False, default=None, repr=False
    )  # Set by Skill for selected Aspects.

    @property
    def description(self) -> str:
        return self.format.format(**asdict(self))

    @property
    def difficulty(self) -> int:
        return int(round(self.base_difficulty * self.count))

    def __mul__(self, other: Any) -> Self:
        match other:
            case int() as num:
                new = Aspect(
                    format=self.format,
                    base_difficulty=self.base_difficulty,
                    count=num,
                )
                new.skill = self.skill
                return new
            case _:
                raise ValueError(f"unsupported {type(other)}: {other!r}")

    __rmul__ = __mul__


# A Skill is an Aspect used to define the effect of a Spell.
Skill = Aspect


class SkillArea:
    """
    A Namespace for a collection of related Skills.
    """

    def __init__(self, name: str, **kwargs: Skill) -> None:
        self._name = name
        for name, value in kwargs.items():
            setattr(self, name, value)
            value.skill = self

    @property
    def name(self) -> str:
        return self._name


Alteration = SkillArea(
    "Alteration",
    add_to_skill=Skill(
        format="Add +{count}D to a skill, damage, or protection", base_difficulty=4.5
    ),
    add_to_attribute=Skill(format="Add +{count}D to an attribute", base_difficulty=18),
)

Apportation = SkillArea(
    "Apportation",
    move_1m=Skill(format="Move mage or something 1 meter", base_difficulty=2),
    move_10m=Skill(format="Move you or something 10 meters", base_difficulty=10),
    move_1km=Skill(format="Move you or something 1 kilometer", base_difficulty=30),
)

Conjuration = SkillArea(
    "Conjuration",
    get_skill=Skill(format="Get a skill at +{count}D", base_difficulty=3),
    do_damage=Skill(format="{count}D damage", base_difficulty=3),
    prevent_damage=Skill(format="Protect for {count}D", base_difficulty=3),
    # TODO: These are Aspects that combine to subsidiary aspects_text...
    simple_1kg=Skill("Conjure something simple, 1 kg or less", base_difficulty=1),
    complex_1kg=Skill("Conjure something complex, 1 kg or less", base_difficulty=5),
    simple_5kg=Skill("Conjure something simple, 5 kg or less", base_difficulty=4),
    complex_5kg=Skill("Conjure something complex, 5 kg or less", base_difficulty=8),
    simple_100kg=Skill("Conjure something simple, 100 kg or less", base_difficulty=10),
    complex_100kg=Skill(
        "Conjure something complex, 100 kg or less", base_difficulty=14
    ),
    simple_1000kg=Skill(
        "Conjure something simple, 1,000 kg or less", base_difficulty=15
    ),
    complex_1000kg=Skill(
        "Conjure something complex, 1,000 kg or less", base_difficulty=19
    ),
)

Divination = SkillArea(
    "Divination",
    see_1m=Skill(format="See one minute in the past or future", base_difficulty=9),
    see_1h=Skill(format="See one hour in the past or future", base_difficulty=18),
    see_1d=Skill(format="See one day in the past or future", base_difficulty=25),
    search_1m_circle=Skill(
        "Search a 1 m-radius circle with a search of 4D", base_difficulty=18
    ),
    search_1m_sphere=Skill(
        "Search a 1 m-radius sphere with a search of 4D", base_difficulty=19
    ),
    search_10m_circle=Skill(
        "Search a 10 m-radius circle with a search of 4D", base_difficulty=27
    ),
    search_10m_sphere=Skill(
        "Search a 10 m-radius sphere with a search of 4D", base_difficulty=32
    ),
    search_100m_circle=Skill(
        "Search a 100 m-radius circle with a search of 4D", base_difficulty=37
    ),
    search_100m_sphere=Skill(
        "Search a 100 m-radius sphere with a search of 4D", base_difficulty=47
    ),
    search_1km_circle=Skill(
        "Search a 1 km-radius circle with a search of 4D", base_difficulty=47
    ),
    search_1km_sphere=Skill(
        "Search a 1 km-radius sphere with a search of 4D", base_difficulty=62
    ),
)


def value(measure: float) -> int:
    r"""
    The core Measure, :math: `m`, to Difficulty Value, :math:`v`, conversion.

    See the *OpenD6 Fantasy Rulebook*, "Magic" chapter.

    For measures from 1 to 5, the mapping is slightly different than all others.
    [1, 1.5, 2.5, 3.5, 5] map to [0, 1, 2, 3, 4].
    Everything else follows [1, 1.5, 2, 2.5, 4, 6] pattern.

    ..  math::

        v = \begin{cases}
         &\lceil 5 \log_{10}(m) + 0.51 \rceil \textbf{ if $m < 10$}\\
         &\lceil 5 \log_{10}(m) \rceil \textbf{ if $m \geq 10$}
        \end{cases}

    :param measure: in one of the base units: seconds, kilograms, meters.
    :return: value an integer
    """
    if measure <= 5:
        value = int(5 * math.log(measure, 10) + 0.51)
    else:  #  measure > 5:
        value = int(round(5 * math.log(measure, 10)))
    return value


def make_aspect(units: dict[str, float], measure: str | float) -> Aspect:
    """
    Difficulty value is a function of a measure, :math:`m`.
    Measure can be a string with a unit, "1s", "1m", "1kg", or a float,
    where the base unit is assumed.

    :param units: Unit name strings and scale values.
    :param measure: The measure string or float to convert
    :return: An Aspect with the measure and the value.
    """
    unit_pat = re.compile(
        optional(WHITESPACE)
        + group(one_or_more(DIGIT))
        + optional(WHITESPACE)
        + optional_group(one_or_more(LETTER))
    )
    base_unit = list(units.keys())[0]  # First unit name is used when unit is omitted.
    match measure:
        case str():
            if match := unit_pat.match(measure):
                if match.group(2):
                    # Units Conversion and format normalization.
                    base_measure = (scale := units[unit := match.group(2)]) * float(
                        match.group(1)
                    )
                    format = f"{base_measure / scale:,.0f} {unit}"
                else:
                    # No unit, assume the default unit.
                    base_measure = float(match.group(1))
                    format = f"{base_measure:,.0f} {base_unit}"
        case float() | int():
            base_measure = measure
            format = f"{base_measure} {base_unit}"
        case _:
            raise ValueError(f"Invalid {measure=!r}")
    return Aspect(format=format, base_difficulty=value(base_measure))


DURATION_UNITS = {
    "sec": 1,
    "s": 1,
    "second": 1,
    "seconds": 1,
    "r": 5,
    "round": 5,
    "rounds": 5,
    "m": 60,
    "min": 60,
    "minute": 60,
    "minutes": 60,
    "h": 60 * 60,
    "hr": 60 * 60,
    "hour": 60 * 60,
    "hours": 60 * 60,
    "d": 60 * 60 * 24,
    "day": 60 * 60 * 24,
    "days": 60 * 60 * 24,
    "w": 60 * 60 * 24 * 7,
    "wk": 60 * 60 * 24 * 7,
    "week": 60 * 60 * 24 * 7,
    "weeks": 60 * 60 * 24 * 7,
    "mon": 60 * 60 * 24 * 30.4375,  # Julian year, it's simpler.
    "month": 60 * 60 * 24 * 30.4375,
    "months": 60 * 60 * 24 * 30.4375,
    "y": 60 * 60 * 24 * 365.25,
    "yr": 60 * 60 * 24 * 365.25,
    "year": 60 * 60 * 24 * 365.25,
    "years": 60 * 60 * 24 * 365.25,
    "c": 60 * 60 * 24 * 36525,
    "century": 60 * 60 * 24 * 36525,
    "centuries": 60 * 60 * 24 * 36525,
}


def time_aspect(duration: str | float, note: str = "") -> Aspect:
    """
    Difficulty is a function of the duration in seconds, :math:`t`.
    Units: s/sec, r, m/min, h/hr, d/day, w/wk, mon, y/yr, c/century

    >>> time_aspect("1s")
    Aspect(format='1 s', base_difficulty=0, count=1)
    >>> time_aspect("1r")
    Aspect(format='1 r', base_difficulty=4, count=1)
    >>> time_aspect("1m")
    Aspect(format='1 m', base_difficulty=9, count=1)
    >>> time_aspect("1hr")
    Aspect(format='1 hr', base_difficulty=18, count=1)
    >>> time_aspect("2 rounds")
    Aspect(format='2 rounds', base_difficulty=5, count=1)
    """
    return make_aspect(DURATION_UNITS, f"{duration} ({note})" if note else duration)


WEIGHT_UNITS = {
    "kg": 1,
    "mg": 1000,
    "t": 1000,
    "ton": 1000,
    "gg": 1_000_000,
    "kt": 1_000_000,
    "kiloton": 1_000_000,
    "pg": 1_000_000_000,
    "mt": 1_000_000_000,
    "megaton": 1_000_000_000,
}


def weight_aspect(weight: str | float, note: str = "") -> Aspect:
    """
    Difficulty is a function of the weight in kilograms, :math:`w`.
    Units: kg, mg/t/ton, gg/kt/kiloton, pg/mt/megaton

    >>> weight_aspect("1kg")
    Aspect(format='1 kg', base_difficulty=0, count=1)
    >>> weight_aspect("1t")
    Aspect(format='1 t', base_difficulty=15, count=1)
    >>> weight_aspect("1kt")
    Aspect(format='1 kt', base_difficulty=30, count=1)
    >>> weight_aspect("1mt")
    Aspect(format='1 mt', base_difficulty=45, count=1)
    """
    return make_aspect(WEIGHT_UNITS, f"{weight} ({note})" if note else weight)


DISTANCE_UNITS = {
    "m": 1,
    "km": 1000,
    "mm": 1_000_000,
}


def distance_aspect(distance: str) -> Aspect:
    """
    Difficulty is a function of the distance in meters, :math:`r`.
    Units: m, km, mm

    >>> distance_aspect("1m")
    Aspect(format='1 m', base_difficulty=0, count=1)
    >>> distance_aspect(" 1 km")
    Aspect(format='1 km', base_difficulty=15, count=1)
    >>> distance_aspect("20km")
    Aspect(format='20 km', base_difficulty=22, count=1)
    >>> distance_aspect("1000km")
    Aspect(format='1,000 km', base_difficulty=30, count=1)
    """
    return make_aspect(DISTANCE_UNITS, distance)


Duration = SimpleNamespace(
    instant=Aspect(format="Instantaneous", base_difficulty=0),  # time_aspect(1)
    duration_1r=Aspect(format="1 round", base_difficulty=4),  # time_aspect("1 round")
    duration_2r=Aspect(format="2 rounds", base_difficulty=5),  # time_aspect("2 rounds")
    duration_1m=Aspect(format="1 minute", base_difficulty=9),  # time_aspect("1 minute")
    duration_1h=Aspect(format="1 hour", base_difficulty=18),  # time_aspect("1 hour")
)

# Note the sign flip -- this is used as a difficulty decrement.
CastingTime = SimpleNamespace(
    cast_1s=Aspect(format="1 second", base_difficulty=-0),  # time_aspect("1 second")
    cast_1r=Aspect(format="1 round", base_difficulty=-4),  # time_aspect("1 round")
    cast_1m=Aspect(format="1 minute", base_difficulty=-9),  # time_aspect("1 minute")
    cast_1h=Aspect(format="1 hour", base_difficulty=-18),  # time_aspect("1 hour")
)

Range = SimpleNamespace(
    self_or_touch=Aspect(format="Self, touch, or 1 meter", base_difficulty=0),
    within_5m=Aspect(format="Within 5m", base_difficulty=8),
    within_10m=Aspect(format="Within 10m", base_difficulty=10),
    within_100m=Aspect(format="Within 100m", base_difficulty=20),
    within_1km=Aspect(format="Within 1km", base_difficulty=30),
)


@dataclass
class Spell:
    """
    A collection of Aspects with a net difficulty and an effect.

    The rules say eight characteristics matter the most:

    -   Skill Used
    -   Difficulty (this is computed from the Aspects)
    -   Effect
    -   Duration
    -   Range
    -   Speed (Which has a default of 0: 1m/s to arrive at target; a better default is same as range to be instantaneous)
    -   Casting Time
    -   Other Aspects -- a dictionary of aspect names and Aspect values.

        The following increase difficulty:
            "area_of_effect", "area_effect", "change_target", "charges", "focused", "focus",
            "multiple_targets", "multi-target",
            "variable_effect", "variable_movement", "variable_duration",
            "other_alterants", "other_alterant",

        The remaining are negative modifiers
            "community",
            "component", "components",
            "concentration", "countenance", "feedback",
            "gesture", "gestures",
            "incantation", "incantations",
            "unreal_effect",
            "arcane_knowledge",
    """

    effect: Skill  # See the Alteration, Apportation, Conjuration or Divination Skill namespaces.
    duration: Aspect  # See Duration namespace
    range: Aspect  # See Range namespace
    casting_time: Aspect  # See CastingTime namespace
    name: str
    # TODO: This should be a ``TypedDict`` with a short list of permitted keys.
    other_aspects: dict[str, Aspect] = field(default_factory=dict)
    other_conditions: list[Aspect] = field(default_factory=list)
    # Speed and Skill have defaults;
    speed: Aspect = field(default_factory=lambda: time_aspect(1))
    skill: str = field(
        default=""
    )  # May be deduced from the Namespace used to provide the Effect.
    notes: str = field(default="")

    difficulty: int = field(init=False)  # Will be computed.

    # A logger for debugging difficulty computations.
    logger: ClassVar[logging.Logger] = logging.getLogger("Spell")

    def __post_init__(self) -> None:
        if not self.skill:
            # If the Effect comes from a SkillArea namespace... (Alteration, Apportation, Conjuration, etc.)
            match self.effect.skill:
                case SkillArea():
                    self.skill = self.effect.skill.name
                case _:
                    raise ValueError(f"No skill provided for {self.name}")

        SPECIAL_ASPECTS = {
            "Effect",
            "Duration",
            "Range",
            "Speed",
            "Casting Time",
            "Cast Time",
        }
        if bad := set(self.other_aspects.keys()) & SPECIAL_ASPECTS:
            raise ValueError(f"invalid attibute name {bad} used in other_aspects")

        # Compute the difficulty.
        # Note. This is done as part of ``__init__()``, making debuggin
        # potentially complicated.
        self.difficulty = self._difficulty()

    def _difficulty(self) -> int:
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

        Confusingly, the signs in the rules appear to be all over the map.
        All difficulty modifier values *should* be unsigned;
        it's the Exacerbation/Alleviation nature of the Aspect that matters.

        :return: Computed Difficulty
        """
        exacerbators = {
            # Attributes "effect", "range", "speed", "duration",
            # Keys in other_aspects:
            "area_of_effect",
            "area_effect",
            "change_target",
            "charges",
            "focused",
            "focus",
            "multiple_targets",
            "multi-target",
            "variable_effect",
            "variable_movement",
            "variable_duration",
            "other_alterants",
            "other_alterant",
        }

        alleviators = {
            # Attribute "casting_time"
            # Keys in other_aspects:
            "community",
            "component",
            "components",
            "concentration",
            "countenance",
            "feedback",
            "gesture",
            "gestures",
            "incantation",
            "incantations",
            "unreal_effect",
            "arcane_knowledge",
        }
        # Plus everything in self.other_conditions.

        # Normalize keys in ``self.other_aspects``
        other = {
            key.lower().strip().replace(" ", "_"): value
            for key, value in self.other_aspects.items()
        }
        if bad := set(other.keys()) - (exacerbators | alleviators | {"difficulty"}):
            raise ValueError(f"unknown keys {bad} in other_aspects")

        self.logger.debug(self.name)
        exacerbation = {
            core: abs(getattr(self, core).difficulty)
            for core in ["effect", "range", "speed", "duration"]
        } | {
            exacer: abs(other[exacer].difficulty)
            for exacer in exacerbators
            if exacer in other
        }
        self.logger.debug(
            "  Spell Total %r = %d", exacerbation, sum(exacerbation.values())
        )
        alleviation = (
            {core: abs(getattr(self, core).difficulty) for core in ["casting_time"]}
            | {
                allev: abs(other[allev].difficulty)
                for allev in alleviators
                if allev in other
            }
            | {
                condition.format: abs(condition.difficulty)
                for condition in self.other_conditions
            }
        )
        self.logger.debug(
            "  Negative Modifiers %r = %d", alleviation, sum(alleviation.values())
        )
        tot = sum(exacerbation.values()) - sum(alleviation.values())
        d = int(0.5 + (tot / 2))
        self.logger.debug("  Difficulty ⎡%d ÷ 2⎤ = ⎡%.1f⎤ = %d", tot, tot / 2, d)
        return d


# Some aliases that can make the books look a little cleaner.
Miracle = Spell
Cantrip = Spell


class SpellWriter:
    """Output RST-format details for publication."""

    spell_template = dedent(
        """\
        {{ spell.name | safe }}
        {{ spell_name_underline * spell.name|length() }}

        :Skill: {{spell.skill}}
        :Difficulty: {{spell.difficulty}}
        :Effect: {{spell.effect.difficulty}} ({{spell.effect.description}})
        :Range: {{spell.range.description}} \\({{spell.range.difficulty}}) 
        :Speed: {{spell.speed.description}} \\({{spell.speed.difficulty}}) 
        :Duration: {{spell.duration.description}} \\({{spell.duration.difficulty}}) 
        :Casting Time: {{spell.casting_time.description}} \\({{spell.casting_time.difficulty}}) 
        {%- if spell.other_aspects %}

        :Other Aspects:
        {% for label, aspect in spell.other_aspects.items() if label != "Difficulty" %}
            {{label}} ({{aspect.difficulty}}): {{aspect.description}}

        {% endfor %}
        {% endif %} 
        {% if spell.other_conditions %}

        :Other Conditions:
        {%- for aspect in spell.other_conditions %}
            ({{aspect.difficulty}}): {{aspect.description}}

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

    def __init__(
        self, section_underline: str = "=", spell_underline: str = "~"
    ) -> None:
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
        template = self.jinja_env.get_template("spell.rst")
        return template.render(
            spell=spell,
            spell_name_underline=self.spell_name_underline,
        )

    @report.register(list)
    def _(self, book: list[Spell]) -> str:
        template = self.jinja_env.get_template("book.rst")
        return template.render(
            book=book,
            spell_name_underline=self.spell_name_underline,
        )

    @report.register(dict)
    def _(self, collection: dict[str, list[Spell]]) -> str:
        template = self.jinja_env.get_template("skill_area.rst")
        return template.render(
            books=collection,
            spell_name_underline=self.spell_name_underline,
            book_section_underline=self.book_section_underline,
        )


def summary(
    book: list[Spell] | dict[str, list[Spell]], destination: TextIO = sys.stdout
) -> None:
    """Provide destination of shared/{name}_spells.csv"""
    wtr = csv.writer(destination)
    wtr.writerow(Spell.header)
    match book:
        case list() as single:
            wtr.writerows(s.csv() for s in single)
        case dict() as multi:
            for section in book:
                wtr.writerow((f"**{section}**",))
                wtr.writerows(s.csv for s in book[section])


def detail(
    spell_or_book: Spell | list[Spell] | dict[str, list[Spell]],
    section_heading: str = "=",
    spell_heading: str = "~",
) -> None:
    """Redirect to shared/{name}_spells.txt"""
    writer = SpellWriter(
        section_underline=section_heading, spell_underline=spell_heading
    )
    print(writer.report(spell_or_book))


def module(title: str, spell_source: Iterator[Spell] | dict[str, list[Spell]]):
    """
    Emit a Python module with a spell book.

    Generally, this is used by applications to parse source
    HTML or PDF files.

    ..  todo:: Merge into other SpellWriter.
            This isn't **really** distinct; it's another format.
    """

    def book_slug(title: str) -> str:
        return title.lower().replace(" ", "_")

    module_template = dedent(
        '''\
        """
        {{ title }}
            
        When run as an app, generates .RST details of each Spell.
        """
        from magic1 import Aspect, Spell, detail
        
        {% block books %}
        spells = [
        {%- for spell in spell_source %}
            {{ "%r" | format(spell) }},
        {% endfor -%}
        ]
        {% endblock books %}
        
        if __name__ == "__main__":
        {% block report %}
            detail(spells)
        {% endblock report %}
        '''
    )
    multi_book_template = dedent(
        """\
        {% extends "base.rst" %}
        {% block books %}
        {% for book in spell_source %}
        {{book | slug}} = [
            {%- for spell in spell_source[book] %}
            {{ "%r" | format(spell) }},
            {% endfor -%}
        ]
        {% endfor %}
        {% endblock books %}
        {% block report %}
            {%- for book in spell_source %}
            print("{{ book }}")
            print("{{ '=' * book | length() }}")
            print()

            detail({{ book | slug }})
            {% endfor -%}
        {% endblock report %}
        """
    )
    jinja_env = jinja2.Environment()
    jinja_env.filters["slug"] = book_slug
    jinja_env.loader = jinja2.DictLoader(
        {"base.rst": module_template, "multi-book.rst": multi_book_template}
    )

    match spell_source:
        case dict():
            template = jinja_env.get_template("multi-book.rst")
        case _:
            template = jinja_env.get_template("base.rst")

    return template.render(spell_source=spell_source, title=title)
