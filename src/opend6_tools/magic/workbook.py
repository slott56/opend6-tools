"""
Functions to aid creating JupyterLab Workbooks of Spell definitions.

..  autofunction:: workbook_spells

..  autofunction:: workbook_rank

..  autofunction:: workbook_validation

..  autofunction:: display

..  autofunction:: debug

"""

from collections.abc import Callable
from contextlib import redirect_stdout
import fnmatch
import functools
import io

from .spells import *


def workbook_spells(context: dict[str, Any]) -> dict[str, Spell]:
    """
    Emit sequence of Spells from a Workbook.
    This examines **all** code cells looking for Spell definitions.

    :param context: Usually ``globals()`` for a Notebook
    :return: dict mapping from ``Spell`` name to ``Spell`` instances
    """
    return {
        value.name: value for name, value in context.items() if isinstance(value, Spell)
    }


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
    context: dict[str, Any],
    valid: Callable[[Spell], bool] | int,
    width: int | None = None,
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
            good = f"## All spells approximately {target} difficulty, {target + low}..{target + high}."
            bad = "## Difficulty errors."
        case Callable() as validator:
            good = "## All spells pass difficulty test."
            bad = "## Difficulty errors."
        case _:  # pragma: no cover
            raise TypeError(f"unknown {type(valid)}: {valid!r}")
    spells = workbook_spells(context)
    if not spells:  # pragma: no cover
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


def aspect_format(name: str, aspect: Aspect, *, details: bool = False) -> str:
    """Apply consistent formatting for an individual Aspect."""
    if details:
        extra = f"\n  {' ':26s}{aspect.base!s}"
    else:
        extra = ""
    if aspect.base:
        return f"  {name:20s}: {aspect.base.sign().value * aspect.difficulty():+3f} {aspect.source()}{extra}"
    else:
        return f"  {name:20s}: {aspect.origin}"


@functools.singledispatch
def display(thing: Any, details: bool = False) -> str:  # pragma: no cover
    raise NotImplementedError(f"unknown {type(thing)}")


@display.register(Spell)
@display.register(Miracle)
@display.register(Cantrip)
def _(spell: Spell | Miracle | Cantrip, details: bool = False) -> str:
    """
    Returns a detailed display of a spell to help designers.
    This includes the final computation of difficulty.

    With ``details`` set to True, it includes the detailed results
    of parsing the Aspect or Effect. Normally, this isn't shown.

    When logging is level is DEBUG, this will reveal the details of the computation, also.

    Used by :py:func:`debug`.

    :param spell: The Spell to display.
    :param details: Include the NormalizedAspect details.
    :returns: Character string to print.
    """
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        if spell.effect.base is None:  # pragma: no cover
            raise ValueError(f"incomplete spell definition: {spell}")
        print(f"  {'name':20s}: {spell.name!r}")
        print(f"  {'notes':20s}: {spell.notes!r}")
        print(f"  {'skill':20s}: {spell.skill!r}")
        print(aspect_format("effect", spell.effect, details=details))
        for a, val in spell.aspects.items():
            if val.base is None:  # pragma: no cover
                print(f"  {a:20s}: not finalized {val.source()}")
            else:
                print(aspect_format(a, val))
        if spell.other_aspects:
            print(f"  {'other_aspects':20s}:")
            for k, v in cast(dict[str, Aspect], spell.other_aspects).items():
                name = f"- {k}"
                if v.base is None:  # pragma: no cover
                    print(f"  {name:20s}: not finalized {v.source()}")
                else:
                    print(aspect_format(name, v))
        if spell.other_conditions:
            print(f"  {'other_conditions':20s}:")
            for v in spell.other_conditions:
                name = f"- {shorten(v.description(), 18)}"
                if v.base is None:  # pragma: no cover
                    print(f"  {name:20s}: not finalized {v.source()}")
                print(aspect_format(name, v))
        spell._difficulty = None  # Clear cache to force computation of difficulty.
        _ = spell.difficulty  # Recomputation will expose implementation details
        print(f"Effect Details        : {spell.effect_details()}")
        st = {name: int(val) for name, val in spell._spell_total.items()}
        print(f"Spell Total           : {st!r} = {sum(spell._spell_total.values())}")
        nm = {name: int(val) for name, val in spell._negative_modifiers.items()}
        print(
            f"Negative Modifiers    : {nm!r} = {sum(spell._negative_modifiers.values())}"
        )
        print(
            f"Difficulty            : ⎡({sum(spell._spell_total.values())} - {sum(spell._negative_modifiers.values())}) ÷ 2⎤ = {spell.difficulty}"
        )
    return buffer.getvalue()


@display.register(Item)
def _(item: Item, details: bool = False) -> str:
    """
    Returns a detailed display of an item to help designers.
    This includes the final computation of difficulty.

    With ``details`` set to True, it includes the detailed results
    of parsing the Effect and any aspects provided. Normally, this isn't shown.

    When logging is level is DEBUG, this will reveal the details of the computation, also.

    Used by :py:func:`debug`.

    :param item: The Item to display.
    :param details: Include the NormalizedAspect details.
    :returns: Character string to print.
    """
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        if item.effect.base is None:  # pragma: no cover
            raise ValueError(f"item not finalized {item!r}")
        print(f"  {'name':20s}: {item.name!r}")
        print(f"  {'notes':20s}: {item.notes!r}")
        print(f"  {'type':20s}: {item.type!r}")
        print(f"  {'price':20s}: {item.price!r}")
        print(aspect_format("effect", item.effect, details=details))
        for a, val in item.aspects.items():
            if val.base is None:  # pragma: no cover
                print(f"  {a:20s}: not finalized {val.source()}")
            else:
                print(aspect_format(a, val))
        if item.other_aspects:
            print(f"  {'other_aspects':20s}:")
            for k, v in cast(dict[str, Aspect], item.other_aspects).items():
                name = f"- {k}"
                if v.base is None:  # pragma: no cover
                    print(f"  {name:20s}: not finalized {v.source()}")
                else:
                    print(aspect_format(name, v))
        if item.other_conditions:
            print(f"  {'other_conditions':20s}:")
            for v in item.other_conditions:
                name = f"- {shorten(v.description(), 18)}"
                if v.base is None:  # pragma: no cover
                    print(f"  {name:20s}: not finalized {v.source()}")
                print(aspect_format(name, v))
        item._difficulty = None  # Clear cache to force computation of difficulty.
        _ = item.difficulty  # Recomputation will expose implementation details
        print(f"Effect Details        : {item.effect_details()}")
        st = {name: int(val) for name, val in item._spell_total.items()}
        print(f"Spell Total           : {st!r} = {sum(item._spell_total.values())}")
        nm = {name: int(val) for name, val in item._negative_modifiers.items()}
        print(
            f"Negative Modifiers    : {nm!r} = {sum(item._negative_modifiers.values())}"
        )
        print(
            f"Difficulty            : ⎡({sum(item._spell_total.values())} - {sum(item._negative_modifiers.values())}) ÷ 2⎤ = {item.difficulty}"
        )
    return buffer.getvalue()


def debug(
    book: list[Spell | Miracle | Cantrip | Item],
    ident: int | str | None | list[str] = None,
    details: bool = False,
) -> None:
    """
    Prints details of a Spell or spells to STDOUT.
    Uses :py:func:`display`.

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

    >>> book = [example]
    >>> debug(book, 0)
    ## Example
      name                : 'Example'
      notes               : 'Mage waves their hands and says the words'
      skill               : 'Acumen: testing'
      effect              : +12 SkillEffect('Acumen: testing', '+4D')
      duration            :  +0 DurationAspect('1 sec')
      range               :  +0 RangeAspect('1m')
      casting_time        :  -4 CastingTimeAspect('5 sec')
      speed               :  +0 SpeedAspect.based_on('range', *(), **{'description': 'Instantaneous'})
      other_conditions    :
      - Everything [...]  :  -1 GenericAspect(1, 'Everything else is completed')
    Effect Details        : SkillEffect based on DiceUnit [Modifier(difficulty=Decimal('12'), description='4*D')]
    Spell Total           : {'effect': 12, 'duration': 0, 'range': 0, 'speed': 0} = 12
    Negative Modifiers    : {'casting_time': 4, 'condition: Everything else is [...]': 1} = 5
    Difficulty            : ⎡(12 - 5) ÷ 2⎤ = 4
    <BLANKLINE>
    <BLANKLINE>

    :param spells: Spell Book
    :param ident: Identifier for a spell, a number, or a name, or a list of names.
        Shell-style wild-cards are used to match names.
    :param details: True to show the internal NormalizedAspect details.
    """
    logging.basicConfig(level=logging.INFO)
    # logging.getLogger("Spell").setLevel(logging.DEBUG)

    keys: list[str]
    spell_map = {s.name: s for s in book}
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
        case _:  # pragma: no cover
            raise ValueError("unknown identifier {ident!r}")

    for name in keys:
        spell_or_item = spell_map[name]
        print("##", spell_or_item.name)
        print(display(spell_or_item, details))
        print()
