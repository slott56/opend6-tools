"""
Reporting and Display features.

These are the conventional top-level application components.
The :py:func:`display` function produces the useful RST output.

Summaries
=========

..  autofunction:: summary

..  autofunction:: item_summary

..  autoclass:: TableSummary
    :members:
    :member-order:  bysource

Formatted
=========

..  autofunction:: detail

..  autoclass:: SpellWriter
    :members:
    :member-order:  bysource

Debugging
==========

..  autofunction:: dumps

"""

import csv
from functools import singledispatchmethod
import sys
from typing import ClassVar, TextIO

from .spells import *

import jinja2
import tomli_w


class TableSummary:
    """Summarize Spells (or Miracles, or Items for CSV output.

    This extracts name, skill or item type, difficulty or price, and description.
    It's suitable for a player's guide summary of available spells.

    >>> import io
    >>> import csv

    >>> example = Spell(
    ...     name="Example",
    ...     notes="Mage waves their hands and says the words",
    ...     effect=SkillEffect("Acumen: testing", "+4D"),
    ...     duration=DurationAspect("1 sec"),
    ...     range=RangeAspect("1m"),
    ...     casting_time=CastingTimeAspect("5 sec"),
    ...     speed=SpeedAspect.based_on("range", description="Instantaneous"),
    ...     other_aspects={},
    ...     other_conditions=[GenericAspect(1, "Everything else is completed")],
    ... )

    >>> buffer = io.StringIO()
    >>> book = [example]
    >>> writer = csv.writer(buffer, quoting=csv.QUOTE_STRINGS)
    >>> _ = writer.writerow(TableSummary.spell_header)
    >>> _ = writer.writerows(TableSummary.spell_csv(s) for s in book)
    >>> buffer.getvalue().splitlines()
    ['"Spell","Skill","Difficulty","Effect"', '"Example","*Acumen: testing*","4","Acumen: testing 4*D"']

    """

    spell_header: ClassVar[tuple[str, ...]] = (
        "Spell",
        "Skill",
        "Difficulty",
        "Effect",
    )

    item_header: ClassVar[tuple[str, ...]] = (
        "Name",
        "Type",
        "Price",
        "Effect",
    )

    @staticmethod
    def spell_csv(spell: Spell) -> tuple[str, ...]:
        """CSV-oriented extract from a Spell.

        :returns: tuple with (name, skill, difficulty, and description)
        """
        return (
            spell.name,
            f"*{spell.skill}*",
            str(spell.difficulty),
            spell.effect.description(),
        )

    @staticmethod
    def item_csv(item: Item) -> tuple[str, ...]:
        """CSV-oriented extract from an Item.

        :return: tuple with (name, type, price, and description)
        """
        return (item.name, f"*{item.type}*", item.price, item.effect.description())


def summary(
    book: list[Spell] | dict[str, list[Spell]], destination: TextIO = sys.stdout
) -> None:
    """
    Writes CSV-format summary of spells (or invocation) to a given destination file.
    Uses :py:class:`TableSummary`.

    :param book: :py:class:`Spell` collection: a list or a mapping from names to lists of spells.
    :param destination: Open file, often directed to ``shared/{name}_spells.csv`` or.
    """
    wtr = csv.writer(destination)
    wtr.writerow(TableSummary.spell_header)
    match book:
        case list() as single:
            wtr.writerows(TableSummary.spell_csv(s) for s in single)
        case dict() as multi:
            for section in multi:
                wtr.writerow((f"**{section}**",))
                wtr.writerows(TableSummary.spell_csv(s) for s in multi[section])


def item_summary(book: list[Item], destination: TextIO = sys.stdout) -> None:
    """
    Writes CSV-format summary of items to a given destination file.
    Uses :py:class:`TableSummary`.

    :param book: :py:class:`Item` collection
    :param destination: Open file, often directed to ``shared/{name}_spells.csv`` or.
    """
    wtr = csv.writer(destination)
    wtr.writerow(TableSummary.item_header)
    wtr.writerows(TableSummary.item_csv(s) for s in book)


class SpellWriter:
    """Output RST-format details of Spells for publication.

    This relies on three closely-related :py:mod:`jinja2` templates.
    One template handles details of a Spell or Item.
    Another is a list wrapper on details.
    The third is a dict wrapper for lists of details.
    """

    base_template = dedent(
        """\
        {% if detail_underline|length() == 0 %}**{% endif %}{{ spell.name | safe }}{% if detail_underline|length() == 0 %}**{% endif %}
        {{ detail_underline * spell.name|length() }}

        :Skill: {{spell.skill}}
        :Difficulty: {{spell.difficulty}} {% if spell._difficulty_note %}(Note: *{{ spell._difficulty_note }}*){% endif %}
        :Effect: {{spell.effect.difficulty()}} ({{spell.effect.description()}})
        :Range: {{ spell.range.description() if spell.range is defined }} \\({{ spell.range.difficulty() if spell.range is defined }})
        :Speed: {{spell.speed.description() if spell.speed is defined }} \\({{spell.speed.difficulty() if spell.speed is defined }})
        :Duration: {{spell.duration.description() if spell.duration is defined }} \\({{spell.duration.difficulty() if spell.duration is defined }})
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
            {% if aspect.difficulty() %}({{ aspect.difficulty() }}): {% endif %}{{ aspect.description() }}

        {% endfor %}
        {% endif %}

        {% if spell.notes is string %}{{spell.notes}}{% else %}
        {% for paragraph in spell.notes %}
        {{ paragraph }}

        {% endfor %}
        {% endif %}

        """
    )
    list_template = dedent("""\
    {% for spell in book %}
    {% include "base.rst" with context %}
    {% endfor %}
    """)
    dict_template = dedent("""\
    {% for name in books %}
    {{ name | safe }}
    {{ section_underline * name|length() }}
    {% set book = books[name] %}
    {% include "list.rst" with context%}
    {% endfor %}
    """)

    def __init__(
        self, section_underline: str = "=", detail_underline: str = "~"
    ) -> None:
        """Initialize the SpellWriter.

        :param section_underline: The RST section heading underline.
        :param detail_underline: The RST spell heading underline.
        """
        self.jinja_env: jinja2.Environment = jinja2.Environment(
            # autoescape=select_autoescape()
        )
        self.jinja_env.loader = jinja2.DictLoader(
            {
                "base.rst": self.base_template,
                "list.rst": self.list_template,
                "dict_list.rst": self.dict_template,
            }
        )
        self.detail_underline = detail_underline
        self.section_underline = section_underline

    @singledispatchmethod
    def report(self, thing: Any) -> str:
        """Prepare an RST-formatted report for a Spell, a list of Spells, or a mapping from name to Spell.

        :param thing: The Spell or Item to display in RST
        :returns: The string which can be printed.
        """
        template = self.jinja_env.get_template("base.rst")
        return template.render(
            spell=thing,
            detail_underline=self.detail_underline,
        )

    @report.register(list)
    def _(self, book: list[Spell | Item]) -> str:
        """Report a list of Spells or Items."""
        template = self.jinja_env.get_template("list.rst")
        return template.render(
            book=book,
            detail_underline=self.detail_underline,
        )

    @report.register(dict)
    def _(self, mapping: dict[str, list[Spell | Item]]) -> str:
        """Report on a mapping of names to Spell (or Item) lists."""
        template = self.jinja_env.get_template("dict_list.rst")
        return template.render(
            books=mapping,
            detail_underline=self.detail_underline,
            section_underline=self.section_underline,
        )


class ItemWriter(SpellWriter):
    """Output RST-format details of Items for publication.
    This relies on :py:mod:`jinja2` templates.

    The parameter to the base template is "spell",
    which is a little confusing when rendering an item.
    """

    base_template = dedent(
        """\
        {% if detail_underline|length() == 0 %}**{% endif %}{{ spell.name | safe }}{% if detail_underline|length() == 0 %}**{% endif %}
        {{ detail_underline * spell.name|length() }}

        {% if spell.notes is string %}{{spell.notes}}{% else %}
        {% for paragraph in spell.notes %}
        {{ paragraph }}

        {% endfor %}
        {% endif %}
        
        :Effect: {{spell.effect.difficulty()}} ({{spell.effect.description()}})
        {% if spell|attr('range') is defined -%}
        :Range: {{ spell.range.description() if spell.range is defined }} \\({{ spell.range.difficulty() if spell.range is defined }})
        {% endif -%}
        {% if spell|attr('speed') is defined -%}
        :Speed: {{spell.speed.description() if spell.speed is defined }} \\({{spell.speed.difficulty() if spell.speed is defined }})
        {% endif -%}
        {% if spell|attr('duration') is defined -%}
        :Duration: {{spell.duration.description() if spell.duration is defined }} \\({{spell.duration.difficulty() if spell.duration is defined }})
        {% endif -%}
        {% if spell.other_aspects -%}
        :Other Aspects:
        {% for label, aspect in spell.other_aspects.items() if label != "Difficulty" %}
            {{label}} ({{aspect.difficulty()}}): {{aspect.description()}}

        {% endfor %}
        {% endif -%}
        {% if spell.other_conditions -%}
        :Other Conditions:
        {%- for aspect in spell.other_conditions %}
            {% if aspect.difficulty() %}({{ aspect.difficulty() }}): {% endif %}{{ aspect.description() }}

        {% endfor -%}
        {% endif -%}
        {% if spell.type %}:Type: {{ spell.type }}{% endif %}
        :Price: {{ spell.price }}


        """
    )


def detail(
    item_spell_book: Spell
    | list[Spell]
    | dict[str, list[Spell]]
    | Item
    | list[Item]
    | dict[str, list[Item]],
    section_heading: str = "=",
    spell_heading: str = "~",
) -> None:
    """Prints RST-format details of spells to STDOUT.
    Uses :py:class:`SpellWriter` to format the detailes of a spell.

    :param item_spell_book: Spell, Item, or some collection of Spells or Items
    :param section_heading: RST underline for section (when collection is a ``dict``)
    :param spell_heading: RST underline for each spell.
    """
    match item_spell_book:
        case Item() | [Item(), *_] as items:
            writer = ItemWriter(
                section_underline=section_heading, detail_underline=spell_heading
            )
            print(writer.report(items))
        case Spell() | [Spell(), *_] as spells:
            writer = SpellWriter(
                section_underline=section_heading, detail_underline=spell_heading
            )
            print(writer.report(spells))
        # Okay. This is weird.
        case dict(mapping):
            if any(
                isinstance(v, Item) for sublist in mapping.values() for v in sublist
            ):
                writer = ItemWriter(
                    section_underline=section_heading, detail_underline=spell_heading
                )
                print(writer.report(mapping))
            else:
                writer = SpellWriter(
                    section_underline=section_heading, detail_underline=spell_heading
                )
                print(writer.report(mapping))
        case _:  # pragma: no cover
            raise ValueError("unknown type: {type(item_spell_book)}")


def dumps(spell: Spell | Miracle | Cantrip | Item) -> str:
    """Returns a TOML-formatted dump of the spell or Item.

    >>> example = Spell(
    ...     name="Example",
    ...     notes="Mage waves their hands and says the words",
    ...     effect=SkillEffect("Acumen: testing", "+4D"),
    ...     duration=DurationAspect("1 sec"),
    ...     range=RangeAspect("1m"),
    ...     casting_time=CastingTimeAspect("5 sec"),
    ...     speed=SpeedAspect.based_on("range", description="Instantaneous"),
    ...     other_aspects={},
    ...     other_conditions=[GenericAspect(1, "Everything else is completed")],
    ... )

    >>> print(dumps(example))
    name = "Example"
    notes = "Mage waves their hands and says the words"
    <BLANKLINE>
    [effect]
    class_ = "SkillEffect"
    args = [
        "Acumen: testing",
        "+4D",
    ]
    <BLANKLINE>
    [duration]
    class_ = "DurationAspect"
    args = [
        "1 sec",
    ]
    <BLANKLINE>
    [range]
    class_ = "RangeAspect"
    args = [
        "1m",
    ]
    <BLANKLINE>
    [casting_time]
    class_ = "CastingTimeAspect"
    args = [
        "5 sec",
    ]
    <BLANKLINE>
    [speed]
    class_ = "SpeedAspect"
    args = [
        0,
        "based_on('range', description='Instantaneous')",
    ]
    <BLANKLINE>
    [[other_conditions]]
    class_ = "GenericAspect"
    args = [
        1,
        "Everything else is completed",
    ]
    <BLANKLINE>

    """
    return tomli_w.dumps(spell._asdict())
