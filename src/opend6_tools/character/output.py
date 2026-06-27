"""
OpenD6 Character and Creature DSL.
Output functions and classes.

These are the conventional top-level application components.
The :py:func:`display` function produces the useful RST output.

A character extract application can produce character sheets in a variety of formats:

 -  RST for use with Sphinx to produce HTML websites, books, and player handouts.
    RST can be converted via **rst2html** into HTML. Custom CSS styles can make the HTML more useful.
    Alternative, RST can be converted via **rst2latex** into LaTex.

-   Stripped-down HTML (with carefully-designed CSS styles) that can be used by tools like **xhtml2pdf** to produce PDF player handouts.

-   LaTeX that can be used by tools like **pdflatex** to produce PDF player handouts.

The HTML can be converted to PDF to create Player handouts.

RST output
==========

..  autoclass:: CharacterWriter
    :members:

..  autoclass:: CharacterWriter_Short
    :members:

..  autoclass:: CharacterWriter_Long2
    :members:

..  autoclass:: CharacterWriter_Table
    :members:

..  autoclass:: CharacterWriter_Literal
    :members:


HTML Output
===========

..  autoclass:: CharacterWriter_HTML1
    :members:

..  autoclass:: CharacterWriter_HTML2
    :members:


LaTex Output
============

..  autoclass:: CharacterWriter_LaTeX
    :members:


High-Level Output API
=====================

..  autofunction::  detail

..  autofunction::  summary



PDF Conversion
==============

There are some alternative HTML to PDF conversion tool candidates:

-   https://pypi.org/project/xhtml2pdf/.
    This installs an easy-to-use application, ``xhtml2pdf x.html x.pdf``.
    It requires ``brew install pkg-config cairo`` on MacOS.

-   https://pypi.org/project/fpdf2/
    This does **not** read the CSS from the HTML source, but requires it separately,
    making the templates slightly more complicated.

-   WeasyPrint (too complicated to install.)

Supported CSS styles by xhtml2pdf:

    background-color
    border-bottom-color, border-bottom-style, border-bottom-width
    border-left-color, border-left-style, border-left-width
    border-right-color, border-right-style, border-right-width
    border-top-color, border-top-style, border-top-width
    colordisplay
    font-family, font-size, font-style, font-weight
    height
    line-height, list-style-type
    margin-bottom, margin-left, margin-right, margin-top
    padding-bottom, padding-left, padding-right, padding-top
    page-break-after, page-break-before
    size
    text-align, text-decoration, text-indent
    vertical-align
    white-space
    width
    zoom

The following properties can also be set true in a style

    -pdf-frame-border
    -pdf-frame-break
    -pdf-frame-content
    -pdf-keep-with-next
    -pdf-next-page
    -pdf-outline
    -pdf-outline-level
    -pdf-outline-open
    -pdf-page-break

"""

import difflib
from enum import Enum
from functools import singledispatchmethod
import textwrap
from typing import Any, Literal, TextIO
import sys

import jinja2
from jinja2 import Environment


from .features import (
    Character,
    CharacterDict,
)


def parse_param_name(all_characters: CharacterDict, arg_value: str) -> str | None:
    """
    Given a dictionary with names and characters, find the closest match to a given arg_value.

    :param all_characters: A dictionary with names and Characters.
    :param arg_value: A command-line argument value.
    :returns: closest matching key from the dictionary.
    """
    names_lc = {n.lower(): n for n in all_characters.keys()}
    matches = difflib.get_close_matches(arg_value, names_lc.keys(), 1)
    if matches:
        return names_lc[matches[0]]
    # Nothing even close??
    return None  # pragma: no cover


class CharacterWriter:
    """
    Report a character for publication.

    Default is long form with table-formatted identity block as a header.
    """

    suffix = ".rst"

    base_template = textwrap.dedent("""\
    {%- block preface %}
    **OpenD6 Fantasy**

    {% endblock %}
    {%- block identity %}
    +--------------------------------------------------+
    | Character Name: {{c.name|pad(50-18)}} |
    +--------------------------------------------------+
    | Occupation: {{c.occupation|pad(50-14)}} |
    +-------------------------+------------------------+
    | Race: {{c.race|pad(25-8)}} | Gender: {{c.gender|pad(24-10)}} |
    +----------------+--------+-------+----------------+
    | Age: {{c.age|pad(16-8)}}  | Height: {{c.height|pad(16-10)}} | Weight: {{c.weight|pad(16-10)}} |
    +----------------+----------------+----------------+
    | Physical Description {{c.physical_description|pad(50-23)}} |
    +--------------------------------------------------+
    {% endblock %}
    {% block attributes %}
    :Agility ({{c.agility.dice}}):
        {% for skill in c.agility.skills %}{% if c.agility[skill] %}{{ skill }} {{c.agility[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Coordination ({{c.coordination.dice}}):
        {% for skill in c.coordination.skills %}{% if c.coordination[skill] %}{{ skill }} {{c.coordination[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Physique ({{c.physique.dice}}):
        {% for skill in c.physique.skills %}{% if c.physique[skill] %}{{ skill }} {{ c.physique[skill] }}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Intellect ({{c.intellect.dice}}):
        {% for skill in c.intellect.skills %}{% if c.intellect[skill] %}{{ skill }} {{c.intellect[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Acumen ({{c.acumen.dice}}):
        {% for skill in c.acumen.skills %}{% if c.acumen[skill] %}{{ skill }} {{c.acumen[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Charisma ({{c.charisma.dice}}):
        {% for skill in c.charisma.skills %}{% if c.charisma[skill] %}{{ skill }} {{c.charisma[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Extranormal ({{c.extranormal.dice}}):
        {% for skill in c.extranormal.skills %}{% if c.extranormal[skill] %}{{ skill }} {{c.extranormal[skill]}}{% if not loop.last %}, {% endif %}{%endif%}{%endfor%}

    :Advantages:
        {{c.advantages}}

    :Disadvantages:
        {{c.disadvantages}}

    :Special Abilities:
        {{c.special_abilities}}

    :Strength Damage: {{c.strength_damage}}
    :Move: {{c.move}}
    :Fate Points: {{c.fate_points}}
    :Character Points: {{c.character_points}}
    :Body Points: {{c.body}}
    {% endblock %}
    """)

    character_template = '{% extends "base.rst" %}'

    character_list_template = textwrap.dedent("""\
    {% for c in book -%}
        {%- set n = c.name %}
        {%- include "character.rst" with context %}

    {% endfor %}
    """)

    character_dict_template = textwrap.dedent("""\
    {% for n, c in book.items() -%}
        {%- include "character.rst" with context %}

    {% endfor %}
    """)

    templates = {
        "base.rst": base_template,
        "character.rst": character_template,
        "character_list.rst": character_list_template,
        "character_dict.rst": character_dict_template,
    }

    @staticmethod
    def pad(text: str, size: int, empty: str = "_") -> str:
        """Pad a line of text on the right"""
        if text:
            if len(text) <= size:
                return text + (size - len(text)) * " "
            else:
                return text[:size]
        else:
            return empty * size

    @staticmethod
    def lpad(text: str, size: int, empty: str = "_") -> str:
        """Pad a line of text on the left"""
        if text:
            if len(text) <= size:
                return (size - len(text)) * " " + text
            else:
                return text[:size]
        else:
            return empty * size

    @staticmethod
    def line(lines: list[str], num: int, width: int = 22) -> str:
        """
        Emits a single line of a multi-line block of text.

        :param lines: Block of text
        :param num: Line number
        :param width: width of the column
        :return: Always returns a string.
        """
        if num < len(lines):
            return lines[num]
        return " " * width

    @staticmethod
    def if_none(value: Any, otherwise: str) -> str:
        """
        A function that can be installed in Jinja to
        replace None values with a string.

        :param value: value to include in a template
        :param otherwise: value to include if ``value`` is ``None`` or an empty string
        :return: value or otherwise
        """
        if value is None:
            return otherwise
        if text := str(value):
            return text
        return otherwise

    @staticmethod
    def col_3(
        character: Character,
        *,
        equipment: bool = True,
        description: bool = True,
        markup: str = "rst",
    ) -> list[str]:
        """For some displays, the third column is a mix of various things.
        It does not trivially align with other attributes and skills in the first two columns.

        This is extracted from the character details, and cached within
        the character to slightly optimize the way the content is generated.
        The output template can then laminate rows of these rows with rows from other collections of skills.

        :param character: The Character instance from which to gather details.
        :param equipment: True to include equipment
        :param markup: Either "rst" or "html" for markup to use.
        """
        bolding = {
            "html": ("<b>", "</b>"),
            "rst": ("**", "**"),
            "latex": (r"\textbf{", r"}"),
        }
        bold_on, bold_off = bolding[markup.lower()]
        if not hasattr(character, "_col3"):
            width = 20 + len(bold_on)
            text = []

            # OptionList types...
            text.extend(
                textwrap.fill(
                    f"{bold_on}Advantages{bold_off}: {'; '.join(str(adv) for adv in character.advantages) or ''}",
                    width,
                ).splitlines()
            )
            text.extend(
                textwrap.fill(
                    f"{bold_on}Disadvantages{bold_off}: {'; '.join(str(dis) for dis in character.disadvantages) or ''}",
                    width,
                ).splitlines()
            )
            text.extend(
                textwrap.fill(
                    f"{bold_on}Special Abilities{bold_off}: {'; '.join(str(spec) for spec in character.special_abilities) or ''}",
                    width,
                ).splitlines()
            )
            # NoteList types...
            if equipment:
                all_eq = "; ".join(
                    character.weapons + character.armor + character.equipment
                )
                text.extend(
                    textwrap.fill(
                        f"{bold_on}Equipment{bold_off}: {all_eq}",
                        width,
                    ).splitlines()
                )
            # Text
            if description:
                text.extend(
                    textwrap.fill(
                        f"{bold_on}Description{bold_off}: {character.description.replace('\n', ' ') or ''}",
                        width,
                    ).splitlines()
                )
            setattr(character, "_col3", text)
        return getattr(character, "_col3")

    def __init__(self) -> None:
        self.jinja_env: jinja2.Environment = Environment(
            # autoescape=select_autoescape()
            # undefined=jinja2.DebugUndefined  # Helps when debugging.
        )
        self.jinja_env.filters |= {
            "pad": self.pad,
            "lpad": self.lpad,
            "line": self.line,
            "if_none": self.if_none,
        }
        self.jinja_env.globals |= {
            "col_3": self.col_3,
        }
        # Scan class attributes for the "*_template" variables...
        templates = {}
        for parent in self.__class__.__mro__:
            if hasattr(parent, "templates"):
                templates |= parent.templates
        templates |= self.templates
        self.jinja_env.loader = jinja2.DictLoader(templates)

    @singledispatchmethod
    def report(self, character: Character, template_name: str = "character") -> str:
        """RST-format for publication."""
        template = self.jinja_env.get_template(f"{template_name}{self.suffix}")
        return template.render(c=character)

    @report.register(list)
    def _(self, book: list[Character], template_name: str = "character_list") -> str:
        template = self.jinja_env.get_template(f"{template_name}{self.suffix}")
        return template.render(book=book)

    @report.register(dict)
    def _(
        self, book: dict[str, Character], template_name: str = "character_dict"
    ) -> str:
        template = self.jinja_env.get_template(f"{template_name}{self.suffix}")
        return template.render(book=book)


class CharacterWriter_Short(CharacterWriter):
    """Short-form -- no identity block header."""

    character_template = textwrap.dedent("""\
    {%- extends "base.rst" -%}
    {%- block preface %}**{{ n }}**:{% endblock -%}
    {%- block identity %}{% endblock -%}
    {%- block attributes -%}
    {%- set comma = '' -%}
    {% if c.agility.dice %}{% set comma = ', ' %}Agility {{ c.agility.dice }}{% for skill in c.agility.skills %}{% if c.agility[skill] %}, {{ skill }} {{c.agility[skill]}}{% endif %}{% endfor %}{% endif -%}
    {% if c.coordination.dice %}{{ comma }}{% set comma = ', ' %}Coordination {{ c.coordination.dice }}{% for skill in c.coordination.skills %}{% if c.coordination[skill] %}, {{ skill }} {{c.coordination[skill]}}{%endif%}{%endfor%}{% endif -%}
    {% if c.physique.dice %}{{ comma }}{% set comma = ', ' %}Physique {{ c.physique.dice }}{% for skill in c.physique.skills %}{% if c.physique[skill] %}, {{ skill }} {{ c.physique[skill] }}{%endif%}{%endfor%}{% endif -%}
    {% if c.intellect.dice %}{{ comma }}{% set comma = ', ' %}Intellect {{ c.intellect.dice }}{% for skill in c.intellect.skills %}{% if c.intellect[skill] %}, {{ skill }} {{c.intellect[skill]}}{%endif%}{%endfor%}{% endif -%}
    {% if c.acumen.dice %}{{ comma }}{% set comma = ', ' %}Acumen {{ c.acumen.dice }}{% for skill in c.acumen.skills %}{% if c.acumen[skill] %}, {{ skill }} {{c.acumen[skill]}}{%endif%}{%endfor%}{% endif -%}
    {% if c.charisma.dice %}{{ comma }}{% set comma = ', ' %}Charisma {{ c.charisma.dice }}{% for skill in c.charisma.skills %}{% if c.charisma[skill] %}, {{ skill }} {{c.charisma[skill]}}{%endif%}{%endfor%}{% endif -%}
    {% if c.extranormal.dice %}{{ comma }}Extranormal {{ c.extranormal.dice }}{% for skill in c.extranormal.skills %}{% if c.extranormal[skill] %}, {{ skill }} {{c.extranormal[skill]}}{% endif %}{% endfor %}{% endif %}.
    {%- if c.advantages %}
    *Advantages*: {{ c.advantages }}, 
    {%- endif %}
    {%- if c.disadvantages %}
    *Disadvantages*: {{ c.disadvantages }}, 
    {%- endif %}
    {%- if c.special_abilities %}
    *Special Abilities*: {{ c.special_abilities }}, 
    {%- endif %}
    *Move*: {{ c.move }}, 
    *Strength Damage*: {{ c.strength_damage }}, 
    *Fate Points*: {{ c.fate_points }}, 
    *Character Points*: {{ c.character_points }}, 
    *Body Points*: {{ c.body }}
    {%- if c.equipment or c.armor or c.weapons %}, *Equipment*: {{ (c.armor + c.weapons + c.equipment)|join("; ") }}{% endif -%}
    {%- if c.description %}, *Description*: {{ c.description }}{% endif -%}
    {%- if c.natural_abilities %}, *Natural Abilities*: {{ c.natural_abilities|join("; ") }}{% endif -%}
    {%- if c.note %}, *Note*: {{ c.note }}{% endif -%}.
    {% endblock %}
    """)

    templates = {"character.rst": character_template}


class CharacterWriter_Long2(CharacterWriter):
    """Long-form -- Base with no identity block header."""

    character_template = textwrap.dedent("""\
    {%- extends "base.rst" -%}
    {%- block preface %}{% endblock -%}
    {%- block identity %}{% endblock -%}
    """)

    templates = {"character.rst": character_template}


class CharacterWriter_Table(CharacterWriter):
    """Long-form -- with three-column table for attributes and skills."""

    character_template = textwrap.dedent("""\
    {% extends "base.rst" %}

    {% block attributes %}
    {%- set c_col_3 = col_3(c) %}
    +------------------------------+------------------------------+------------------------------+
    | Agility {{c.agility.dice|if_none("_____")|lpad(30-10)}} | Intellect {{c.intellect.dice|if_none("_____")|lpad(30-12)}} | {{" "|lpad(30-2)}} |                 
    +------------------------------+------------------------------+------------------------------+
    {%- for r in range(0, 13) %}
    | {{c.agility.row(r, 28)|lpad(28, " ")}} | {{c.intellect.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+                              +
    | Coordination {{c.coordination.dice|if_none("_____")|lpad(30-15)}} | Acumen {{c.acumen.dice|if_none("_____")|lpad(30-9)}} | {{c_col_3|line(13)|pad(28)}} |                 
    +------------------------------+------------------------------+                              +
    {%- for r in range(0, 13) %}
    | {{c.coordination.row(r, 28)|lpad(28, " ")}} | {{c.acumen.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r+14)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+                              +
    | Physique {{c.physique.dice|if_none("_____")|lpad(30-11)}} | Charisma {{c.charisma.dice|if_none("_____")|lpad(30-11)}} | {{c_col_3|line(27)|pad(28)}} |                 
    +------------------------------+------------------------------+                              +
    {%- for r in range(0, 13) %}
    | {{c.physique.row(r, 28)|lpad(28, " ")}} | {{c.charisma.row(r, 28)|lpad(28, " ")}} | {{c_col_3|line(r+28)|pad(28)}} |
    |                              |                              |                              |
    {%- endfor %}
    +------------------------------+------------------------------+------------------------------+
    | Extranormal {{c.extranormal.dice|if_none("_____")|lpad(30-14)}} | {{" "|lpad(30-2)}} | {{" "|lpad(30-2)}} |                 
    +------------------------------+------------------------------+------------------------------+
    | {{c.extranormal.row(0, 28)|lpad(28, " ")}} | Str Damage {{c.strength_damage|if_none("_____")|lpad(30-13)}} | Body Points {{c.body|if_none("_____")|pad(30-13)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(1, 28)|lpad(28, " ")}} | Move {{c.move|string|lpad(30-7)}} | [ ] Stunned   {{c.wounds['Stunned']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(2, 28)|lpad(28, " ")}} | Fate Pts      {{c.fate_points|string|pad(30-16)}} | [ ] Wounded   {{c.wounds['Wounded']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(3, 28)|lpad(28, " ")}} | Character Pts {{c.character_points|string|pad(30-16)}} | [ ] Severe    {{c.wounds['Severe']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(4, 28)|lpad(28, " ")}} | Funds {{c.funds|string|pad(30-8)}} | [ ] Incapac'd {{c.wounds['Incapacitated']|string|pad(30-15)}}|
    |                              |                              |                              |
    | {{c.extranormal.row(5, 28)|lpad(28, " ")}} | Silver {{c.silver|string|pad(30-9)}} | [ ] Mortal    {{c.wounds['Mortal']|string|pad(30-15)}}|
    |                              |                              |                              |
    |                              |                              | [ ] Dead                     |
    +------------------------------+------------------------------+------------------------------+
    {% endblock %}
    """)

    templates = {"character.rst": character_template}


class CharacterWriter_Literal(CharacterWriter):
    """Long-form -- with three-column table for attributes and skills.

    The table is indented into a ``::`` code-block directive to create an RST display of the source for the table.
    """

    character_template = textwrap.dedent("""\
    {% extends "base.rst" %}
    {% block preface %}
    ..  rubric:: OpenD6 Fantasy

    {% endblock %}
    {% block attributes %}
    {%- set c_col_3 = col_3(c) %}
    ::

        +----------------------+----------------------+----------------------+
        | Agility {{c.agility.dice|string|lpad(22-10)}} | Intellect {{c.intellect.dice|string|lpad(22-12)}} | {{" "|lpad(22-2)}} |
        +----------------------+----------------------+----------------------+
        {%- for r in range(0, 13) %}
        | {{c.agility.row(r)|lpad(20)}} | {{c.intellect.row(r)|lpad(20)}} |{{c_col_3|line(r)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+{{c_col_3|line(13)|pad(22)}}|
        | Coordination {{c.coordination.dice|string|lpad(22-15)}} | Acumen {{c.acumen.dice|string|lpad(22-9)}} |{{c_col_3|line(14)|pad(22)}}|
        +----------------------+----------------------+{{c_col_3|line(15)|pad(22)}}|
        {%- for r in range(0, 13) %}
        | {{c.coordination.row(r)|lpad(20)}} | {{c.acumen.row(r)|lpad(20)}} |{{c_col_3|line(r+16)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+{{c_col_3|line(27)|pad(22)}}|
        | Physique {{c.physique.dice|string|lpad(22-11)}} | Charisma {{c.charisma.dice|string|lpad(22-11)}} |{{c_col_3|line(28)|pad(22)}}|
        +----------------------+----------------------+{{c_col_3|line(29)|pad(22)}}|
        {%- for r in range(0, 13) %}
        | {{c.physique.row(r)|lpad(20)}} | {{c.charisma.row(r)|lpad(20)}} |{{c_col_3|line(r+30)|pad(22)}}|
        {%- endfor %}
        +----------------------+----------------------+----------------------+
        | {{c.extranormal.name|pad(11)}} {{c.extranormal.dice|string|lpad(22-14)}} | {{" "|lpad(22-2)}} | {{" "|lpad(22-2)}} |
        +----------------------+----------------------+----------------------+
        | {{c.extranormal.row(0)|lpad(20)}} | Str Damage {{c.strength_damage|string|lpad(22-13)}} | Body Points {{c.body|string|pad(22-13)}}|
        | {{c.extranormal.row(1)|lpad(20)}} | Move {{c.move|string|lpad(22-7)}} | [ ] Stunned   {{c.wounds['Stunned']|string|pad(22-15)}}|
        | {{c.extranormal.row(2)|lpad(20)}} | Fate Pts      {{c.fate_points|string|pad(22-16)}} | [ ] Wounded   {{c.wounds['Wounded']|string|pad(22-15)}}|
        | {{c.extranormal.row(3)|lpad(20)}} | Character Pts {{c.character_points|string|pad(22-16)}} | [ ] Severe    {{c.wounds['Severe']|string|pad(22-15)}}|
        | {{c.extranormal.row(4)|lpad(20)}} | Funds {{c.funds|string|pad(22-8)}} | [ ] Incapac'd {{c.wounds['Incapacitated']|string|pad(22-15)}}|
        | {{c.extranormal.row(5)|lpad(20)}} | Silver {{c.silver|string|pad(22-9)}} | [ ] Mortal    {{c.wounds['Mortal']|string|pad(22-15)}}|
        |                      |                      | [ ] Dead             |
        +----------------------+----------------------+----------------------+
    {% endblock %}
    """)

    templates = {"character.rst": character_template}


class CharacterWriter_HTML1(CharacterWriter):
    """
    Report a character for publication.

    This creates HTML that can be converted to PDF.

    The structure is a 1-page, 3-column layout to create PDF's for player's sheets.
    """

    suffix = ".html"

    # Note px = 1/96 in; pt = 1/72 in.
    style1_css = textwrap.dedent("""\
    @page {size: letter portrait; margin: 36pt; }
    body {font-size: 10pt; font-family: serif; line-height: 1.0;}
    table.full {width: 100%;}
    table.box {border-bottom-color: black; border-bottom-style: solid; border-bottom-width: 1px; border-collapse: collapse;}
    table.box tr {border-bottom-color: black; border-bottom-style: solid; border-bottom-width: 1px; border-collapse: collapse;}
    table th {text-align: start;}
    table td {vertical-align: top; margin-top: 12pt; padding-top: 12pt;}
    table.box td {vertical-align: top; margin-top: 1pt; padding-top: 1pt;}
    """)

    style_template = textwrap.dedent("""\
    <style type="text/css">
        {% include "style1.css" %}
    </style>
    """)

    base_template = textwrap.dedent("""\
    {%- block preface %}
    <h1>OpenD6 Fantasy</h1>
    {% endblock %}
    
    <table class="full">
    {%- block identity %}
    <thead>
    <tr>
        <td style="width: 33%;"></td>
        <td style="width: 33%;"></td>
        <td style="width: 34%;"></td>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan=2>
            <table class="full box">
            <tr><td colspan="6"><b>Character Name</b> {{ c.name }}</td></tr>
            <tr><td colspan="6"><b>Occupation</b> {{ c.occupation }}</td></tr>
            <tr><td colspan="3"><b>Race</b> {{ c.race }}</td> <td colspan="3"><b>Gender</b> {{ c.gender }}</td></tr>
            <tr><td colspan="2"><b>Age</b> {{ c.age }}</td>   <td colspan="2"><b>Height</b> {{ c.height }}</td>  <td colspan="2"><b>Weight</b> {{ c.weight }}</td></tr>
            <tr><td colspan="6"><b>Physical Description</b> {{ c.physical_description }}</td></tr>
            <tr><td colspan="6">&nbsp;</td></tr>
            </table>
        </td>
        <td>
            &nbsp;
        </td>
    </tr>
    {% endblock %}

    {% block attributes %}
    {%- set c_col_3 = col_3(c, markup="html") %}
    <tr>
    <td>
            <b>Agility</b> {{ c.agility.dice }}
            {%- for r in range(13) %}
            {% if c.agility.row(r) %}<br/>{{ c.agility.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Intellect</b> {{ c.intellect.dice }}
            {%- for r in range(13) %}
            {% if c.intellect.row(r) %}<br/>{{ c.intellect.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            {%- for r in range(13) %}
            {% if c_col_3[r] %}<br/>{{ c_col_3[r] }}{% endif %}
            {%- endfor %}        
    </td>
    </tr>

    <tr>
    <td>
            <b>Coordination</b> {{ c.coordination.dice }}
            {%- for r in range(13) %}
            {% if c.coordination.row(r) %}<br/>{{ c.coordination.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Acumen</b> {{ c.acumen.dice }}
            {%- for r in range(13) %}
            {% if c.acumen.row(r) %}<br/>{{ c.acumen.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            {{ c_col_3[13] }}
            {%- for r in range(13) %}
            {% if c_col_3[r+14] %}<br/>{{ c_col_3[r+14] }}{% endif %}
            {%- endfor %}        
    </td>
    </tr>

    <tr>
    <td>
            <b>Physique</b> {{ c.physique.dice }}
            {%- for r in range(13) %}
            {% if c.physique.row(r) %}<br/>{{ c.physique.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Charisma</b> {{ c.charisma.dice }}
            {%- for r in range(13) %}
            {% if c.charisma.row(r) %}<br/>{{ c.charisma.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            {{ c_col_3[27] }}
            {%- for r in range(13) %}
            {% if c_col_3[r+28] %}<br/>{{ c_col_3[r+28] }}{% endif %}
            {%- endfor %}        
    </td>
    </tr>
    
    <tr>
    <td>
            <b>{{ c.extranormal.name }}</b> {{ c.extranormal.dice }}
            {%- for r in range(7) %}
            <br/>{{ c.extranormal.row(r)|if_none("&nbsp;") }}
            {%- endfor %}
    </td>
    <td>
                 <b>Str Damage</b>    {{ c.strength_damage }}
            <br/><b>Move</b>          {{ c.move }}
            <br/><b>Fate Pts</b>      {{ c.fate_points }}
            <br/><b>Character Pts</b> {{ c.character_points }}
            <br/><b>Funds</b>         {{ c.funds }}
            <br/><b>Silver</b>        {{ c.silver }}  
    </td>
    <td>
                 <b>Body Points</b>        {{ c.body }}
            <br/><b>[ ] Stunned</b>        {{ c.wounds['Stunned'] }}
            <br/><b>[ ] Wounded</b>        {{ c.wounds['Wounded'] }}
            <br/><b>[ ] Severe</b>         {{ c.wounds['Severe'] }}
            <br/><b>[ ] Incapacitated</b>  {{ c.wounds['Incapacitated'] }}
            <br/><b>[ ] Mortal</b>         {{ c.wounds['Mortal'] }}
            <br/><b>[ ] Dead</b>
    </td>
    </tr>
    {% endblock %}
    </tbody>
    </table>
    {% block page2 %}{% endblock %}
    """)

    sheet_template = '{% extends "base.html" %}'

    character_template = textwrap.dedent("""\
    <html>
    <head>
    {% include "style.html" %}
    </head>
    <body>
    {% include "sheet.html" with context %}
    </body>
    </html>
    """)

    character_list_template = textwrap.dedent("""\
    <html>
    <head>
    {% include "style.html" %}
    </head>
    <body>
    {% for c in book -%}
        {%- set n = c.name %}
        {%- include "sheet.html" with context %}
        <br/>
    {% endfor %}
    </body>
    </html>
    """)

    character_dict_template = textwrap.dedent("""\
    <html>
    <head>
    {% include "style.html" %}
    </head>
    <body>
    {% for n, c in book.items() -%}
        {%- include "sheet.html" with context %}
        <br/>
    {% endfor %}
    </body>
    </html>
    """)

    templates = {
        "style1.css": style1_css,
        "style.html": style_template,
        "base.html": base_template,
        "sheet.html": sheet_template,
        "character.html": character_template,
        "character_list.html": character_list_template,
        "character_dict.html": character_dict_template,
    }


class CharacterWriter_HTML2(CharacterWriter_HTML1):
    """
    Report a character for publication.

    This creates HTML that can be converted to PDF by the **xhtml2pdf** tool.

    The structure is a 2-page, 3-column layout to create PDF's for player handouts.
    """

    style2_css = textwrap.dedent("""\
        td.col2 {padding-left: 1em;}        
    """)

    style_template = textwrap.dedent("""\
    <style>
        {%- include "style1.css" %}
        {% include "style2.css" %}
    </style>
    """)

    sheet_template = textwrap.dedent("""\
    {%- extends "base.html" -%}
    
    {% block attributes %}
    <tr>
    <td>
            <b>Agility</b> {{ c.agility.dice }}
            {%- for r in range(13) %}
            {% if c.agility.row(r) %}<br/>{{ c.agility.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Intellect</b> {{ c.intellect.dice }}
            {%- for r in range(13) %}
            {% if c.intellect.row(r) %}<br/>{{ c.intellect.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
    </td>
    </tr>

    <tr>
    <td>
            <b>Coordination</b> {{ c.coordination.dice }}
            {%- for r in range(13) %}
            {% if c.coordination.row(r) %}<br/>{{ c.coordination.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Acumen</b> {{ c.acumen.dice }}
            {%- for r in range(13) %}
            {% if c.acumen.row(r) %}<br/>{{ c.acumen.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Advantages</b>
            {%- if c.advantages %}{% for adv in c.advantages %}
            <br/>{{ adv }}
            {% endfor -%}
            {% else %}
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            {% endif %}
            <br/><b>Disadvantages</b>
            {%- if c.disadvantages %}{% for disad in c.disadvantages %}
            <br/>{{ disad }}
            {% endfor -%}
            {% else %}
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            {% endif %}
    </td>
    </tr>

    <tr>
    <td>
            <b>Physique</b> {{ c.physique.dice }}
            {%- for r in range(13) %}
            {% if c.physique.row(r) %}<br/>{{ c.physique.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Charisma</b> {{ c.charisma.dice }}
            {%- for r in range(13) %}
            {% if c.charisma.row(r) %}<br/>{{ c.charisma.row(r) }}{% endif %}
            {%- endfor %}
    </td>
    <td>
            <b>Special Abilities</b>
            {%- if c.special_abilities %}{% for spec in c.special_abilities %}
            <br/>{{ spec }}
            {% endfor -%}
            {% else %}
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            {% endif %}
    </td>
    </tr>
    
    <tr>
    <td>
            <b>{{ c.extranormal.name }}</b> {{ c.extranormal.dice }}
            {%- for r in range(7) %}
            <br/>{{ c.extranormal.row(r)|if_none("&nbsp;") }}
            {%- endfor %}
    </td>
    <td>
                 <b>Str Damage</b>    {{ c.strength_damage }}
            <br/><b>Move</b>          {{ c.move }}
            <br/><b>Fate Pts</b>      {{ c.fate_points }}
            <br/><b>Character Pts</b> {{ c.character_points }}
            <br/><b>Funds</b>         {{ c.funds }}
            <br/><b>Silver</b>        {{ c.silver }}  
    </td>
    <td>
                 <b>Body Points</b>        {{ c.body }}
            <br/><b>[ ] Stunned</b>        {{ c.wounds['Stunned'] }}
            <br/><b>[ ] Wounded</b>        {{ c.wounds['Wounded'] }}
            <br/><b>[ ] Severe</b>         {{ c.wounds['Severe'] }}
            <br/><b>[ ] Incapacitated</b>  {{ c.wounds['Incapacitated'] }}
            <br/><b>[ ] Mortal</b>         {{ c.wounds['Mortal'] }}
            <br/><b>[ ] Dead</b>
    </td>
    </tr>
    {% endblock %}
    
    {% block page2 %}
    <!-- xhmtl2pdf page break -->
    <pdf:nextpage/>
    
    <table>
    <thead>
    <tr>
        <td style="width: 50%;"></td>
        <td style="width: 50%;"></td>
    </tr>
    </thead>
    <tbody>

    <tr>
        <td>
            <b>Character Name: </b>{{ c.name|if_none("____________________") }}
        </td>
        <td>&nbsp;</td>
    </tr>
    <tr>
        <td>
            <p><b>Armor</b><p>
            {% if c.armor %}
            <p>{{ c.armor }}
            <br/>______________________________
            <br/>______________________________
            </p>
            {% else %}
            <table class="full box">
                <tr><th style="width: 30%;">Type</th><th style="width: 15%;">AV</th><th style="width: 55%;">Notes</th></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            </table>
            {% endif %}
            <p><b>Weapons</b><p>
            {% if c.weapons %}
            <p>{{ c.weapons }}
            <br/>______________________________
            <br/> Ammo ( )( )( ) ( )( )( ) ( )( )( ) 
            <br/>______________________________
            <br/> Ammo ( )( )( ) ( )( )( ) ( )( )( ) 
            <br/>______________________________
            <br/> Ammo ( )( )( ) ( )( )( ) ( )( )( ) 
            </p>
            {% else %}
            <table class="full box">
                <tr><th style="width: 30%;">Type</th><th style="width: 15%;">Dmg</th><th style="width: 55%;">Range S/M/L</th></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td colspan="3"><b>Ammo</b>( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td colspan="3"><b>Ammo</b>( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td colspan="3"><b>Ammo</b>( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td colspan="3"><b>Ammo</b>( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )</td></tr>
            </table>
            {% endif %}
        </td>
        <td class="col2">
            <p><b>{% if c.extranormal %}{{ c.extranormal.name }}{% else %}Magic{% endif %}</b><p>
            {%- if c.spells|length > 0 %}
            <table class="full box">
            {% for s in c.spells %}
            <tr><td>{{ s }}</td></tr>
            {% endfor %}
            {% for x in range(c.spells|length, 15) %}
            <tr><td>&nbsp;</td></tr>
            {% endfor %}
            </table>
            {% else %}
            <table class="full box">
                <tr><th style="width: 30%;">Name</th><th style="width: 15%;">Diff</th><th style="width: 55%;">Notes</th></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            </table>
            {%- endif %}
        </td>
    </tr>
    <tr>
        <td>
            <p><b>Other Equipment</b><p>
            {% if c.equipment %}
            <p>{{ c.equipment }}
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            <br/>______________________________
            </p>
            {% else %}
            <table class="full box">
                <tr><th style="width: 30%;">Type</th><th style="width: 70%;">Notes</th></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
                <tr><td>&nbsp;</td><td>&nbsp;</td></tr>
            </table>
            {% endif %}
        </td>
        <td class="col2">
            <p><b>Personality</b><p>
            <table class="full box">
            <tr><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td></tr>
            </table>
            <p><b>Objectives</b><p>
            <table class="full box">
            <tr><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td></tr>
            </table>
            <p><b>Native Language</b><p>
            <table class="full box">
            <tr><td>&nbsp;</td></tr>
            </table>
            <p><b>Notes</b><p>
            <table class="full box">
            <tr><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td></tr>
            </table>
        </td>
    </tr>
    </table>
    {% endblock %}
    """)

    templates = {
        "style2.css": style2_css,
        "style.html": style_template,
        "sheet.html": sheet_template,
    }


class CharacterWriter_LaTeX(CharacterWriter):
    """
    Report a character for publication.

    This creates HTML that can be converted to PDF by the **xhtml2pdf** tool.

    The structure is a 2-page, 3-column layout to create PDF's for player handouts.

    ..  TODO:: Refactor the data into a form that can be readily tabularized by LaTeX.

        Specifically, page 2 items form a large grid with 5 sections:

        Armor | Magic
        Weapons |
        Other Equipment | etc.

        OR... Switch to \\usepackage{multicol}

        Page 1 is (potentially) {multicols}{3}, but... there's the top-right corner
        issue: a place for a figure that spans two columns.

        Page 2 is \\begin{multicols}{2}
        Armor
        Weapons
        Other Eq.
        \\columnbreak
        Magic
        Etc.
        \\end{multicols}




    """

    suffix = ".tex"

    character_template = textwrap.dedent(r"""
        % Preamble
        {% block preamble %}
        \documentclass[10pt]{article}
        
        % Packages
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{array}
        \usepackage{layout}
        \usepackage{fancyhdr}
        \usepackage{multicol}
        {% endblock %}
        
        % See https://www.overleaf.com/learn/latex/Articles%2FA_visual_guide_to_LaTeX’s_page_layout_parameters
        % Paper width = 612 pt height = 792 pt
        % 1in offset means \pagewidth = 72pt + \hoffset + \evensidemargin + Book_IM + DeltaX
        \setlength{\marginparwidth}{0pt}
        \setlength{\marginparsep}{0pt}
        \setlength{\textwidth}{504pt}   % 468 = 6.5 in, 504=7in
        \setlength{\textheight}{620pt}  % 8.6 in
        \setlength{\evensidemargin}{6pt}
        \setlength{\oddsidemargin}{6pt}
        \setlength{\topmargin}{6pt}
        \setlength{\headheight}{12pt}
        \setlength{\headsep}{12pt}
        
        {% block title %}
        \title{OpenD6 Fantasy Character Sheet}
        {% endblock %}
        
        % Document
        \begin{document}
        \pagestyle{fancy}
        \fancyhf{}
        \fancyhead[L]{\textit{OpenD6 Fantasy Character}}
        \fancyfoot[R]{\thepage}
        \renewcommand{\headrulewidth}{0pt}
        
        {% include "details_2.tex" %}
        
        \end{document}
    """)

    details_template = textwrap.dedent(r"""
        \cleardoublepage
        % \textwidth of 468 pt = 144pt * 3 + 36pt
        % \textwidth of 504 pt = 156pt * 3 + 36pt
        {%- block page1 %}
        \begin{table}
        \begin{tabular}{m{156pt} m{156pt} m{156pt}}
            \multicolumn{2}{l}{\textbf{Character Name}: {{ c.name }} \hrulefill} \\
            \multicolumn{2}{l}{\textbf{Occupation}: {{ c.occupation }} \hrulefill} \\
            \multicolumn{2}{l}{\textbf{Race}: {{ c.race }} \hrulefill \hspace{1em} \textbf{Gender}: {{ c.gender }} \hrulefill} \\
            \multicolumn{2}{l}{\textbf{Age}: {{ c.age }} \hrulefill \hspace{1em} \textbf{Height}: {{ c.height }} \hrulefill \hspace{1em}  \textbf{Weight}: {{ c.weight }} \hrulefill } \\
            \multicolumn{2}{l}{\textbf{Physical Description}: {{ c.physical_description }} \hrulefill } \\
            \multicolumn{2}{l}{ \hrulefill } \\
         & & \\
        {%- set c_col_3 = col_3(c, equipment=False, description=False, markup="latex") %}
        \textbf{Agility}: {{ c.agility.dice }} \hrulefill      & \textbf{Intellect}: {{ c.intellect.dice }} \hrulefill  &                             \\
        {% for r in range(13) %}
        {{ c.agility.row(r) }} \hrulefill & {{ c.intellect.row(r) }} \hrulefill & \\
        {% endfor %}
                                          
        \textbf{Coordination}: {{ c.coordination.dice }} \hrulefill & \textbf{Acumen}: {{ c.acumen.dice }} \hrulefill     & \hrulefill \\
        {% for r in range(13) %}
        {{ c.coordination.row(r) }} \hrulefill & {{ c.acumen.row(r) }} \hrulefill & {{ c_col_3[r] }} \hrulefill \\
        {% endfor %}
        
        \textbf{Physique}: {{ c.physique.dice }} \hrulefill & \textbf{Charisma}: {{ c.charisma.dice }} \hrulefill     & {{ c_col_3[13] }} \hrulefill \\
        {% for r in range(8) %}
        {{ c.physique.row(r) }} \hrulefill & {{ c.charisma.row(r) }} \hrulefill & {{ c_col_3[r+14] }} \hrulefill \\
        {% endfor %}
                                          &                                 &                             \\
        {{ '\\textbf{' }}{{ c.extranormal.name }} {{ '}' }}: {{ c.extranormal.dice }} \hrulefill  &                                 &                             \\
        {{ c.extranormal.row(0) }} \hrulefill & \textbf{Strength Damage}: {{ c.strength_damage }} \hrulefill                             & \textbf{Body Points}: {{ c.body }} \hrulefill \\
        {{ c.extranormal.row(1) }} \hrulefill                        & \textbf{Move}:             {{ c.move }}             \hrulefill    & $\Box$ Stunned \footnotesize{(80\%)} \hfill {{ c.wounds['Stunned'] }} \\
        {{ c.extranormal.row(2) }} \hrulefill                        & \textbf{Fate Points}:      {{ c.fate_points }}      \hrulefill    & $\Box$ Wounded \footnotesize{(60\%)} \hfill {{ c.wounds['Wounded'] }} \\
        {{ c.extranormal.row(3) }} \hrulefill                        & \textbf{Character Points}: {{ c.character_points }} \hrulefill    & $\Box$ Severely Wounded \footnotesize{(40\%)} \hfill {{ c.wounds['Severe'] }} \\
        {{ c.extranormal.row(4) }} \hrulefill                        & \textbf{Funds}:            {{ c.funds }}            \hrulefill    & $\Box$ Incapacitated \footnotesize{(20\%)} \hfill {{ c.wounds['Incapacitated'] }} \\
        {{ c.extranormal.row(5) }} \hrulefill                        & \textbf{Silver}:           {{ c.silver }}           \hrulefill    & $\Box$ Mortally Wounded \footnotesize{(10\%)} \hfill {{ c.wounds['Mortal'] }} \\
        {{ c.extranormal.row(5) }} \hrulefill                        &  \hrulefill                                                       & $\Box$ Dead   \\
        \end{tabular}
        \end{table}
        {%- endblock page1 %}
        {%- block page2 %}
        \newpage
        \begin{table}
        \begin{tabular}{m{216pt} m{216pt}}
            \textbf{Character Name}: \hrulefill & \\
            & \\
        \textbf{Armor}                & \textbf{Magic Spells/Miracles}   \\
            Type \hskip 4em AV \hskip 3em Notes             & Name \hskip 4em Difficulty \hskip 3em Notes            \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
                                      & \hrulefill                       \\
        \textbf{Weapons}              & \hrulefill                       \\
            Type \hskip 4em Dmg \hskip 3em Range: S/M/L     & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            Ammo: $\Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box$  & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            Ammo: $\Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box$ & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            Ammo: $\Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box$ & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            Ammo: $\Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box$  & \hrulefill                       \\
                                      & \hrulefill                       \\
        \textbf{Other Equipment}      & \textbf{Personality}: \hrulefill \\
            Type \hskip 4em Notes     & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \textbf{Objectives}: \hrulefill \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \textbf{Native Language}: \hrulefill \\
            \hrulefill                &  \\
            \hrulefill                & \textbf{Other Information}: \hrulefill  \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
            \hrulefill                & \hrulefill                       \\
        \end{tabular}
        \end{table}
        {%- endblock page2 %}
    """)

    details_2_template = textwrap.dedent(r"""
    {%- extends "details.tex" %}
    {%- block page2 %}
    % \newpage 
    \cleardoublepage

    \begin{multicols}{2}
    \textbf{Character Name:} \hrulefill
    
    \vspace{24pt}
    
    \textbf{Armor}
    {% for line in c.armor %}
    
    {{ line }}
    {% endfor %}
    {% if c.armor|length < 4 %}
    {% for n in range(c.armor|length, 4) %}

    \hrulefill
    {% endfor %}
    {% endif %}
    
    \vspace{24pt}
    
    \textbf{Weapons}
    {% for line in c.weapons %}
    
    {{ line }}
    {% endfor %}
    {% if c.weapons|length < 6 %}
    {% for n in range(c.weapons|length, 6) %}

    \hrulefill
    
    Ammo: $\Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box \Box$ 
    {% endfor %}
    {% endif %}

    \vspace{24pt}

    \textbf{Other Equipment}
    {% for line in c.equipment %}
    
    {{ line }}
    {% endfor %}
    {% if c.equipment|length < 18 %}
    {% for n in range(c.equipment|length, 18) %}

    \hrulefill
    {% endfor %}
    {% endif %}

    \columnbreak

    \vspace*{24pt}

    {{ '\\textbf{' }}{{ c.extranormal.name }} {{ '}' }}
    
    {% for s in c.spells %}
    {{ s.name }} {{ s.difficulty }}
    {% endfor %}
    {% for n in range(c.spells|length, 15) %}

    \hrulefill
    {% endfor %}
    
    \vspace{24pt}
    
    \textbf{Personality}: \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \textbf{Objectives}: \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    
    \textbf{Native Language}: \hrulefill
    
    \hrulefill
    
    \textbf{Other Information}: \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \hrulefill
    
    \end{multicols}
    {% endblock %}
    """)

    templates = {
        "character.tex": character_template,
        "details.tex": details_template,
        "details_2.tex": details_2_template,
    }


class Format(Enum):
    LONG = CharacterWriter
    LONG2 = CharacterWriter_Long2
    SHORT = CharacterWriter_Short
    TABLE = CharacterWriter_Table
    LITERAL = CharacterWriter_Literal
    HTML = CharacterWriter_HTML1
    PLAYER = CharacterWriter_HTML2
    LATEX = CharacterWriter_LaTeX


FORMAT_OPTIONS = Literal[
    "LONG",
    "LONG2",
    "SHORT",
    "TABLE",
    "LITERAL",  # RST
    "HTML",
    "PLAYER",  # HTML
    "LATEX",  # LaTeX
]


def detail(
    character: Character | list[Character] | CharacterDict,
    form: Format = Format.TABLE,
) -> None:
    """
    A character sheet, formatted for publication, using one of the defined formats.

    The HTML formats can be run through **xhtml2pdf** to create PDF files.

    :param character: The Character (or list or dictionary of characters) or Creature.
    :param form: The format to use.
    """
    writer_class: type[CharacterWriter] = form.value
    w = writer_class()
    print(w.report(character))


# A legacy function definition
sheet = detail


def summary(characters: list[Character], destination: TextIO = sys.stdout) -> None:
    """
    Write CSV summary.

    ..  todo:: CSV summary of characters. Not sure which attributes to show.
    """
    pass  # pragma: no cover
