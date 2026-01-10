"""
Migrate magic1 definitions to magic2.

This covers all aspects **EXCEPT** the effect.
Effects are all over the map and very difficult to parse.
There are some patterns, but each one is more-or-less unique.

For a few untranslatable aspects, a special
"AisleFive" (as in "cleanup on aisle five") subclass is used.

CLI
====

::

    % python tools/migrate_magic.py --help

     Usage: migrate_magic.py [OPTIONS] [SOURCE]...

    ╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │   source      [SOURCE]...  [default: <class 'list'>]                                                                                                            │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --target                  TEXT  [default: spells_2]                                                                                                             │
    │ --style     --no-style          run ruff format on the output [default: style]                                                                                  │
    │ --force     --no-force          force overwrite of previous .py file [default: no-force]                                                                        │
    │ --keep      --no-keep           keep temporary file to help debugging [default: no-keep]                                                                        │
    │ --help                          Show this message and exit.                                                                                                     │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Generally, it's best to convert one book of spells at a time.

The migration app will *not* willingly overwrite a file.
The ``--force`` option will force overwriting a file.

Generally, it's used like this

..  code-block:: bash

    % python tools/migrate_magic.py spells_1/Photomancy.py --target spells_2

Since this will not overwrite the output, the ``spells_2/Photomancy.py`` must be deleted to rerun.

When debugging, it's sometimes helpful to use this:

..  code-block:: bash

    % python tools/migrate_magic.py spells_1/Photomancy.py --target spells_2 --keep

This will leave a ``tmp...`` file in the target directory.

Or. Use this.

..  code-block:: bash

    % python tools/migrate_magic.py spells_1/Photomancy.py --target spells_2 --force

This needs to be used with care. Once you edit the output file to clean up the remaining problems,
it can be overwritten and nobody wants that.
"""

import abc
import ast
import re
from collections.abc import Iterable, Iterator
from collections import Counter
from contextlib import redirect_stdout
import datetime
import importlib
import logging
from pathlib import Path
from pprint import pprint
import subprocess
import sys
import tempfile
from textwrap import dedent
from typing import Annotated
from zoneinfo import ZoneInfo

from humre import *
import jinja2
import typer

import magic1
import magic2


class ModuleWriter:
    module_template = dedent(
        '''\
        """
        {{ title }}
    
        When run as an app, generates .RST-formatted details of each Spell.
        """
        from decimal import Decimal
        from typing import Annotated, Any
        import typer
        from magic2 import *
    
        {% block books %}
        spells = [
        {%- for spell in spell_source %}
            {{ "%r" | format(spell) }},
        {% endfor -%}
        ]
        {% endblock books %}

        @spellbook_app.command(name="display")
        def display_command():
        {% block report %}
            detail(spells)
        {% endblock report %}
        
        @spellbook_app.command(name="debug")
        def debug_command(
            book_name: Annotated[str, typer.Option(help="book name if not `spells`")] = "spells",
            name_or_number: Annotated[str, typer.Argument(help="Spell name (or number)")] = None,
        ):
            spell_book = globals()[book_name]
            debug(spell_book, name_or_number)
        
        if __name__ == "__main__":
            spellbook_app()
            
        __test__ = { 
            {% for name, body in tests.items() %}
            {{ "{!r}".format(name) }}: {{ "{!r}".format(body) }},
            {% endfor %}
        }
        '''
    )
    # This is used rarely, if at all.
    # Maybe only the opend6 set of spells?
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
            # debug({{ book | slug }}[0])
            {% endfor -%}
        {% endblock report %}
        """
    )

    @staticmethod
    def book_slug(title: str) -> str:
        return title.lower().replace(" ", "_")

    def __init__(self) -> None:
        self.jinja_env = jinja2.Environment()
        self.jinja_env.filters["slug"] = self.book_slug
        self.jinja_env.loader = jinja2.DictLoader(
            {
                "base.rst": self.module_template,
                "multi-book.rst": self.multi_book_template,
            }
        )

    def write_book(self, title: str, spells: Iterable[magic1.Spell], tests: dict[str, str] | None = None) -> None:
        template = self.jinja_env.get_template("base.rst")
        # Compute attributes
        for spell in spells:
            spell.finalize()
        return template.render(spell_source=spells, title=title, tests=tests)


class AisleFive(magic2.GenericAspect):
    """Requires replacement; the description was uninterpretable."""

    pass


class RewriteAspect(abc.ABC):
    """Rewrite a spell aspect into a ``magic2`` version.
    AND. Save the descriptive text and their conversion status.
    """
    target : type

    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.good_descriptions = Counter()
        self.failed_descriptions = Counter()
        self.error_descriptions = Counter()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.target})"

    def convert(self, source: magic1.Aspect) -> magic2.Aspect | magic2.Effect:
        try:
            new = self.m2(source)
            self.good_descriptions[source.description] += 1
            return new
        except ValueError as ex:
            self.logger.info("could not rewrite %r: %s", source, ex)
            self.failed_descriptions[source.description] += 1
            return AisleFive(source.difficulty, source.description)
        except (AttributeError, TypeError) as ex:
            self.logger.error("error trying to rewrite %r: %s", source, ex)
            self.error_descriptions[source.description] += 1
            raise

    @abc.abstractmethod
    def m2(self, source: magic1.Aspect) -> magic2.Aspect | magic2.Effect: ...


class MakeGeneric(RewriteAspect):
    """Rewrite an aspects not otherwise defined into :py:class:`magic2.GenericAspect`."""
    target = magic2.GenericAspect

    def m2(self, source: magic1.Aspect) -> magic2.GenericAspect:
        return magic2.GenericAspect(
            difficulty=source.difficulty,
            description=source.description,
        )


class MakeAspect(RewriteAspect):
    """Baseline rewrite where the description text serves to create a ``magic2`` version."""
    def __init__(self, target: type[magic2.Aspect] = AisleFive) -> None:
        super().__init__()
        self.target = target

    def m2(self, source: magic1.Aspect) -> magic2.GenericAspect:
        cls = self.target
        return cls(
            source.description,
        )


class MakeEffect(RewriteAspect):
    """For Effects, we need to discern the sub-type of effect:
    Skill, Attribute, Special Ability, Disadvantage, Damage, Protection, or Measure.
    There are numerous forms and formats for these effects.
    """
    target = magic2.Effect

    def __init__(self) -> None:
        super().__init__()
        self.special = Counter()
        self.damage = Counter()
        self.time = Counter()
        self.mass = Counter()
        self.unknown = Counter()

    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        # 1. Look for a DieCode expression (nD[+-a]) -- skill or attribute effect.
        dice_pat = DIGIT + "D" + optional(chars(DIGIT, PLUS, MINUS))
        self.logger.debug("dice_pat %r, source_description %r", dice_pat, source.description)
        if match := re.search(dice_pat, source.description):
            # words [ nD+-a ] words
            pre, die_string, post = source.description[:match.start()], source.description[match.start():match.end()], source.description[match.end():]
            try:
                return magic2.SkillEffect(f"{pre} {post}", die_string)
            except ValueError as ex:
                self.logger.debug(ex)
            self.logger.debug("die %s %r", dice_pat,
                              source.description)
            self.special[source.description] += 1

        # 2. Look for (R\d) -- special ability or disadvantage effect.
        special_pat = (
                OPEN_PAREN + "R"
                + group(one_or_more(DIGIT))
                + CLOSE_PAREN
            )
        self.logger.debug("special_pat %r, source_description %r", special_pat, source.description)
        if match := re.search(special_pat, source.description):
            # words [ (R number) ] words
            pre, rank_string, post = source.description[:match.start()], source.description[match.start():match.end()], source.description[match.end():]
            try:
                return magic2.SpecialAbilityEffect(pre, rank=int(match.group(1)), note=post)
            except ValueError as ex:
                self.logger.debug(ex)
            try:
                return magic2.DisadvantageEffect(pre, rank=int(match.group(1)), note=post)
            except ValueError as ex:
                self.logger.debug(ex)
            self.logger.debug("special %s %r", special_pat,
                              source.description)
            self.special[source.description] += 1

        # 3. Look for "damage resistance" -- protection effect
        if match := re.search(r"damage\s+resistance", source.description, re.IGNORECASE):
            try:
                diff, desc = magic2.DieUnit().parse(source.description)
                return magic2.ProtectionEffect(source.description, desc)  # Canonical
            except ValueError as ex:
                self.logger.debug(ex)
                self.logger.debug("resistance %r",source.description)
                self.damage[source.description] += 1

        # 4. Look for "damage" -- damage effect
        if match := re.search(r"damage", source.description, re.IGNORECASE):
            try:
                diff, desc = magic2.DieUnit().parse(source.description)
                return magic2.DamageEffect(source.description,desc)  # Canonical
            except ValueError as ex:
                self.logger.debug(ex)
                self.logger.debug("damage %r",source.description)
                self.damage[source.description] += 1

        unit_pat_start =  (
            group(one_or_more(chars(DIGIT, PERIOD, PLUS, MINUS, ",")))  # +|- Number
            + optional(WHITESPACE)
        )

        # 5. Look for a time unit -- some kind of TimeEffect
        time_pat = (
            unit_pat_start
            + noncap_group(either("second", "round", "minute", "hour", "week", "month", "year"))
            + optional("s")
        )
        self.logger.debug("time_pat %r, source_description %r", time_pat, source.description)
        if match := re.search(time_pat, source.description):
            # words [ number unit ] words
            pre, measure, post = source.description[:match.start()], source.description[match.start():match.end()], source.description[match.end():]
            try:
                diff, desc = magic2.TimeUnit().parse(measure)
                return magic2.TimeEffect(f"{pre} -- {post}", measure)
            except ValueError:
                self.logger.debug("time %r", source.description)
                self.time[source.description] += 1

        # 6. Look for a mass unit some kind of MassEffect
        mass_pat = (
            unit_pat_start
            + noncap_group(either("kilogram", "ton"))
            + optional("s")
        )
        self.logger.debug("mass_pat %r, source_description %r", mass_pat, source.description)
        if match := re.search(mass_pat, source.description):
            # words [ number unit ] words
            pre, measure, post = source.description[:match.start()], source.description[match.start():match.end()], source.description[match.end():]
            self.logger.debug("mass pre, measure, post = %r, %r, %r", pre, measure, post)
            try:
                diff, desc = magic2.MassUnit().parse(measure)
                return magic2.MassEffect(f"{pre} -- {post}", measure)
            except ValueError:
                self.logger.debug("mass %r", source.description)
                self.mass[source.description] += 1

        # Give up.
        self.unknown[source.description] += 1
        self.logger.error("unparseable %r", source.description)
        return magic2.Effect(source.description, source.difficulty)


class MakeDuration(magic2.TimeUnit, RewriteAspect):
    target = magic2.DurationAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if "12 rounds" in source.description.lower():
            return magic2.DurationAspect("12 rounds")
        if "4 minutes" in source.description.lower():
            return magic2.DurationAspect("50 rounds")
        if "1.s rounds" in source.description.lower():
            return magic2.DurationAspect("1.5 rounds")
        diff, desc = self.parse(source.description)
        return magic2.DurationAspect(
            desc,
        )


class MakeRange(magic2.DistUnit, RewriteAspect):
    target = magic2.RangeAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if "self" in source.description.lower():
            return magic2.RangeAspect("self")
        if "1 meter" in source.description.lower():
            return magic2.RangeAspect("self")
        if "within 10m" in source.description.lower():
            return magic2.RangeAspect("10m")
        diff, desc = self.parse(source.description)
        return magic2.RangeAspect(
            desc,
        )


class MakeCastingTime(magic2.TimeUnit, RewriteAspect):
    target = magic2.CastingTimeAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        diff, desc = self.parse(source.description)
        return magic2.CastingTimeAspect(
            desc,
        )


class MakeSpeed(magic2.TimeUnit, RewriteAspect):
    target = magic2.SpeedAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if source.description == "0D":
            return magic2.SpeedAspect.based_on("range", "Instantaneous")
        if source.description == "Immediate":
            return magic2.SpeedAspect.based_on("range", "Instantaneous")
        if "/" in source.description:
            speed_text, note = source.description.split("/")
            speed_text = speed_text.replace("per second", "")
            return magic2.SpeedAspect(measure=speed_text, note=note)
        diff, desc = self.parse(source.description)
        return magic2.SpeedAspect.based_on("range", desc)


class MakeAreaEffect(magic2.TimeUnit, RewriteAspect):
    target = magic2.AreaEffectAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if "2m sphere" in source.description:
            return magic2.AreaEffectAspect(
                "2m sphere",
            )
        if "5-meter-radius circle" in source.description:
            return magic2.AreaEffectAspect(
                "5m radius circle",
            )
        if "height of 3 meters and width of 1 meter" in source.description:
            return magic2.AreaEffectAspect(
                "3m height 1m width wall"
            )
        # [shape] "with" "radius" "of" [size] "meters"
        pattern = either(
            group(either("sphere", "hemisphere", "circle", "divination" + one_or_more(WHITESPACE) + "sphere")) + one_or_more(WHITESPACE)
            + "with" + one_or_more(WHITESPACE)
            + "radius" + one_or_more(WHITESPACE)
            + "of" + one_or_more(WHITESPACE)
            + group(one_or_more(chars(DIGIT, PERIOD))) + one_or_more(WHITESPACE)
            + "meter" + optional("s"),
            # OR...
            group(either("sphere", "hemisphere", "circle", "divination" + one_or_more(WHITESPACE) + "sphere")) + one_or_more(
                WHITESPACE)
            + "with" + one_or_more(WHITESPACE)
            + group(one_or_more(chars(DIGIT, PERIOD))) + one_or_more(WHITESPACE)
            + "meter" + optional("s") + one_or_more(WHITESPACE)
            + "radius"
        )
        if match := re.match(pattern, source.description, re.IGNORECASE):
            if match.group(1) and match.group(2):
                new = f"{match.group(2)} meter radius {match.group(1).lower()}"
            else:
                new = f"{match.group(4)} meter radius {match.group(3).lower()}"
            self.logger.info("found %r, created %r", source, new)
            return magic2.AreaEffectAspect(new)
        diff, desc = self.parse(source.description)
        return magic2.AreaEffectAspect(
            desc,
        )

class MakeConcentration(magic2.TimeUnit, RewriteAspect):
    target = magic2.ConcentrationAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if source.description == '2 rounds of concentration with willpower/mettle difficulty of of 8':
            return magic2.ConcentrationAspect("2 rounds", note="willpower/mettle difficulty 8")
        if source.description == '1 round with willpower/mettle at difficulty 9':
            return magic2.ConcentrationAspect("1 round", note="willpower/mettle difficulty 9")
        if source.description.startswith('Every 24 hours'):
            return magic2.ConcentrationAspect("1 round", note="willpower/mettle difficulty 8; every 24 hours")
        pattern_1 = (
            group(
                noncap_group(one_or_more(DIGIT), zero_or_more(WHITESPACE)),
                noncap_group(either("hour", "minute", "minutes", "round", "rounds", "seconds")))
            + optional(noncap_group(zero_or_more(WHITESPACE), "of concentration", zero_or_more(WHITESPACE)))
            + one_or_more(WHITESPACE) + "with" + one_or_more(WHITESPACE)
            + group(ANYTHING + zero_or_more(WHITESPACE) + optional(noncap_group("difficulty" + zero_or_more(WHITESPACE))) + "of" + one_or_more(WHITESPACE) + one_or_more(DIGIT))
        )
        if match_1 := re.search(pattern_1, source.description):
            return magic2.ConcentrationAspect(match_1.group(1), note=match_1.group(2))
        self.logger.info("Pattern: %r, Input: %r", pattern_1, source.description)
        diff, desc = self.parse(source.description)
        return magic2.ConcentrationAspect(
            desc,
        )

class MakeCountenanceAspect(RewriteAspect):
    target = magic2.CountenanceAspect
    def m2(self, source: magic1.Aspect) -> magic2.Aspect:
        # Default is "noticeable"
        # Look for "exteme"
        measure = "extreme" if "extreme" in source.description.lower() else "noticeable"
        return magic2.CountenanceAspect(source.description, measure)

class MakeFeedbackAspect(RewriteAspect):
    """Makes a magic2.FeedbackAspect."""
    target = magic2.FeedbackAspect
    def m2(self, source: magic1.Aspect) -> magic2.Aspect:
        if '-3 to damage resistance' in source.description:
            return magic2.FeedbackAspect(3)
        elif '-2 to damage resistance' in source.description:
            return magic2.FeedbackAspect(2)
        elif '-1 to damage resistance' in source.description:
            return magic2.FeedbackAspect(1)
        return magic2.FeedbackAspect(source.description)

class MakeFocusedAspect(RewriteAspect):
    """Makes a magic2.FocusedAspect."""
    target = magic2.FocusedAspect
    def m2(self, source: magic1.Aspect) -> magic2.Aspect:
        return magic2.FocusedAspect.based_on(("effect", "duration"), target=source.format)


class MakeGestures(RewriteAspect):
    target = magic2.GesturesAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        if "program instructions into robot" in source.description.lower():
            return magic2.GesturesAspect("program instructions into robot, using devices/tech/robot interface/repair", "challenging", "difficulty 23")
        pattern = (
            group(ANYTHING) + one_or_more(WHITESPACE)
            + OPEN_PAREN + group(ANYTHING) + CLOSE_PAREN
        )
        if match := re.match(pattern, source.description):
            note = match.group(1)
            measures = match.group(2)
            roll_pattern = (
                group(ANYTHING) + zero_or_more(WHITESPACE)
                + ";" + zero_or_more(WHITESPACE) + group(EVERYTHING)
            )
            if roll_match := re.match(roll_pattern, measures):
                measures = f"{roll_match.group(1)} ({roll_match.group(2)})"
            else:
                measures = measures.replace(",", ";")
            return magic2.GesturesAspect(note, measures.replace("fairly ", ""))
        # self.logger.info("Pattern: %r, text: %r", pattern, source.description)
        return magic2.GesturesAspect(source.description)


class MakeIncantation(RewriteAspect):
    target = magic2.IncantationsAspect
    def m2(self, source: magic1.Aspect) -> magic2.Effect:
        pattern = (
            group(ANYTHING) + one_or_more(WHITESPACE)
            + OPEN_PAREN + group(ANYTHING) + CLOSE_PAREN
        )
        if match := re.match(pattern, source.description):
            note = match.group(1)
            measures = match.group(2)
            roll_pattern = (
                group(ANYTHING) + zero_or_more(WHITESPACE)
                + ";" + zero_or_more(WHITESPACE) + group(EVERYTHING)
            )
            if roll_match := re.match(roll_pattern, measures):
                measures = f"{roll_match.group(1)} ({roll_match.group(2)})"
            else:
                measures = measures.replace(",", ";")
            return magic2.IncantationsAspect(note, measures)
        return magic2.IncantationsAspect(source.description)


class ConversionError(BaseException):
    pass


class RewriteSpell:
    converter_map = {
        # Core
        "effect": MakeEffect(),
        "duration": MakeDuration(),
        "range": MakeRange(),
        "casting_time": MakeCastingTime(),
        "speed": MakeSpeed(),
        # Other Aspects
        # The following increase difficulty:
        "area effect": MakeAreaEffect(),
        "area_of_effect": MakeAreaEffect(),
        "area_effect": MakeAreaEffect(),
        "change target": MakeAspect(magic2.ChangeTargetAspect),
        "change_target": MakeAspect(magic2.ChangeTargetAspect),
        "charges": MakeAspect(magic2.ChargesAspect),
        "focused": MakeFocusedAspect(),
        "focus": MakeFocusedAspect(),
        "multiple_targets": MakeAspect(magic2.MultipleTargetAspect),
        "multi-target": MakeAspect(magic2.MultipleTargetAspect),
        "variable_effect": MakeAspect(magic2.VariableEffect),
        "variable_movement": MakeAspect(magic2.VariableMovementAspect),
        "variable_duration": MakeAspect(magic2.VariableDurationAspect),
        "other_alterants": MakeGeneric(),
        "other_alterant": MakeGeneric(),
        # The remaining are negative modifiers
        "community": MakeAspect(magic2.CommunityAspect),
        "component": MakeAspect(magic2.ComponentsAspect),
        "components": MakeAspect(magic2.ComponentsAspect),
        "concentration": MakeConcentration(),
        "countenance": MakeCountenanceAspect(),
        "feedback": MakeFeedbackAspect(),
        "gesture": MakeGestures(),
        "gestures": MakeGestures(),
        "incantation": MakeIncantation(),
        "incantations": MakeIncantation(),
        "unreal_effect": MakeAspect(magic2.UnrealEffectAspect),
        "_other_": MakeGeneric(),  # The other_conditions, which sometimes have area_effect hidden in there.
        # No difficulty: this is similar to the "skill" attribute of a Spell.
        "arcane knowledge": MakeAspect(magic2.ArcaneKnowledgeAspect),
    }
    default = MakeGeneric()

    logger = logging.getLogger("RewriteSpell")

    def m2_aspect(
        self, name: str, source: magic1.Aspect, original_name: str = ""
    ) -> magic2.Aspect:
        if name.lower() not in self.converter_map:
            self.logger.error("  %r: NO CONVERSION", name.lower())
            converter = self.default
        else:
            converter = self.converter_map[name.lower()]
        try:
            new_aspect = converter.convert(source)
            if original_name:
                new_aspect._description = f"{original_name}: {new_aspect._description}"
            self.logger.info("  %r: %r using %r --> %r", name, source, converter, new_aspect)
            return name.lower().replace(" ", "_") , new_aspect
        except AttributeError:
            self.logger.error("  %r: %r using %r", name, source, converter)
            raise
        except ValueError as ex:
            text = f"{self.__class__.__name__} error [{ex}] in {name!r}: {source!r}"
            self.logger.error("  %r: %r using %r", name, source, converter)
            self.logger.error("  %s", text)
            self.errors.append(text)
            return name.lower().replace(" ", "_"), AisleFive(0, f"error: {text} in {source!r}")

    def m2_spell(self, source: magic1.Spell) -> magic2.Spell:
        self.logger.info("Convert %s", source.name)
        self.errors = []
        aspects = dict(
            [
                self.m2_aspect("effect", source.effect),
                self.m2_aspect("duration", source.duration),
                self.m2_aspect("range", source.range),
                self.m2_aspect("casting_time", source.casting_time),
                self.m2_aspect("speed", source.speed),
                (
                    "other_aspects",
                    dict(
                        self.m2_aspect(name, aspect)
                        for name, aspect in source.other_aspects.items()
                        if name.lower() in self.converter_map
                    ),
                ),
            ]
        )
        # TODO: Is "Area Effect" in other_conditions or other_aspects properly?
        aspects["other_conditions"] = [
            aspect
            for _, aspect in (
                self.m2_aspect("_other_", aspect) for aspect in source.other_conditions
            )
        ] + [
            aspect
            for _, aspect in (
                self.m2_aspect("_other_", aspect, name)
                for name, aspect in source.other_aspects.items()
                if name.lower() not in self.converter_map
            )
        ]
        # pprint(aspects)
        if self.errors:
            raise ConversionError(self.errors)
        return magic2.Spell(
            name=source.name, skill=source.skill, notes=source.notes, **aspects
        )


def migrate_source(
    rewriter: RewriteSpell, module_name: str, globals: list[str]
) -> None:
    logger = logging.getLogger("migrate_source")
    area = importlib.import_module(module_name)
    for book_name in globals:
        try:
            new_book = [rewriter.m2_spell(spell) for spell in getattr(area, book_name)]
            if hasattr(area, "__test__"):
                tests = getattr(area, "__test__")
            else:
                tests = {}
            logger.info("converted %r %r", module_name, book_name)
        except ConversionError as ex:
            logger.error("did not convert %r %r", module_name, book_name)
            for error in ex.args[0]:
                logger.error("  %s", error)
            raise
        writer = ModuleWriter()
        print(writer.write_book(module_name, new_book, tests))
        # TODO MOVED INTO THE TEMPLATE!
        # print()
        # print()
        # print(f"__test__ = {tests!r}")


def book_iter(base: Iterable[Path]) -> Iterator[tuple[str, list[str]]]:
    """Find all the spell book globals in the various modules."""
    logger = logging.getLogger("book_iter")

    class ImportVisitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.imports = set()

        def visit_Import(self, node: ast.Import) -> None:
            names = [alias.name for alias in node.names]
            self.imports.union(set(names))

        def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
            self.imports.add(node.module)

    def global_assignments(module: ast.Module) -> Iterator[str]:
        for stmt in module.body:
            match stmt:
                case ast.Assign() as assignment:
                    yield from (
                        name.id
                        for name in assignment.targets
                        if not name.id.startswith("_")
                    )

    for module in sorted(base):
        module_ast = ast.parse(module.read_text(), module.name)
        iv = ImportVisitor()
        iv.visit(module_ast)
        if "magic" in iv.imports:
            logger.error("!!! FIX OLD PATH %s", module.relative_to(base))
        elif "magic1" in iv.imports:
            assignments = list(global_assignments(module_ast))
            yield module.stem, assignments
        else:
            pass

def summarize_rewrites(rewriter: RewriteSpell, source: list[Path], target: Path, format: bool, force: bool, keep: bool) -> None:
    logger = logging.getLogger("summary")
    logger.info("source   %r", source)
    logger.info("--target %r", target)
    logger.info("--style  %r", format)
    logger.info("--force  %r", force)
    logger.info("--keep   %r", keep)
    for name in rewriter.converter_map:
        if rewriter.converter_map[name].failed_descriptions:
            text = "\n   ".join(map(repr, rewriter.converter_map[name].failed_descriptions.keys()))
            logger.info("%r %s\n   %s\n", name, "failed", text)
        if rewriter.converter_map[name].error_descriptions:
            text = "\n   ".join(map(repr, rewriter.converter_map[name].error_descriptions.keys()))
            logger.info("%r %s\n   %s\n", name, "error", text)
    # MakeEffect() has slightly different details than other Aspects.
    for effect_type in ("damage", "time", "mass", "unknown"):
        errors = getattr(rewriter.converter_map["effect"], effect_type)
        text = "\n   ".join(map(repr, errors.keys()))
        logger.info("effect (%s)\n   %s\n", effect_type, text)

def main(
        source: Annotated[list[str], typer.Argument(help="magic1 files to process", default_factory=list)],
        target: Annotated[str, typer.Option(help="output directory")] = "spells_2",
        style: Annotated[bool, typer.Option(help="run ruff format on the output")] = True,
        force: Annotated[bool, typer.Option(help="force overwrite of previous .py file")] = False,
        keep: Annotated[bool, typer.Option(help="keep temporary file to help debugging")] = False,
) -> None:
    logger = logging.getLogger("main")
    ruff_output = logging.getLogger("ruff")
    rewriter = RewriteSpell()

    base = [Path(s) for s in source]
    # Tweak the PYTHONPATH used for importing spell modules.
    base_dirs = set(b.parent for b in base)
    for base_dir in base_dirs:
        sys.path.insert(0, str(base_dir))

    target_dir = Path(target)
    target_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Migrate to %r", target_dir)

    source_iter = book_iter(base)
    for module, globals in source_iter:
        logger.info("%s defines %r", module, globals)
        target_module = (target_dir / module).with_suffix(".py")
        temp = tempfile.NamedTemporaryFile(suffix=".py", dir=target_dir, mode='w+',
                                           delete=False)
        try:
            # 1. Write to TEMP/whatever.py
            with temp:
                with redirect_stdout(temp):
                    migrate_source(rewriter, module, globals)

            # 2. Rename if (file exists and --force) or file does not exist...
            if (not target_module.exists()) or (target_module.exists() and force):
                Path(temp.name).rename(target_module)
                logger.info("wrote   %s", target_module.relative_to(target_dir))

                if style:
                    # Requires Internet Access so uv can install ruff
                    proc = subprocess.run(
                        ["uv", "tool", "run", "ruff", "format", str(target_module)],
                        check=True,
                        text=True,
                        capture_output=True,
                    )
                    if proc.stderr:
                        ruff_output.error(proc.stderr)
                    ruff_output.info(proc.stdout)

            else:
                logger.warning(
                    "%s already exists, use --force to overwrite", target_module.relative_to(target_dir)
                )
        except ConversionError as ex:
            logger.error("skipped %s", target_module.relative_to(target_dir))

        if (temp_path := Path(temp.name)).exists() and not keep:
            temp_path.unlink()

    # Final summary of *all* conversions.
    summarize_rewrites(rewriter, source, target, style, force, keep)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("ruff").setLevel(logging.WARNING)
    typer.run(main)
