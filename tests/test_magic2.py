"""
More tests for the ``magic2`` module.
"""
from decimal import Decimal
from difflib import unified_diff
from unittest.mock import Mock

import pytest

from opend6_tools.magic2 import *
from opend6_tools.magic2 import Sign

# Tests that recapitulate the doctests.

def test_disadvantage_effect():
    eff_1 = DisadvantageEffect("Hindrance: Initiative", 5, "-10 to all initiative totals")
    assert eff_1.difficulty() == 15
    assert eff_1.description() == 'Hindrance: Initiative (R5), -10 to all initiative totals'
    assert eff_1.incr_decr == Sign.Increase
    assert repr(eff_1) == "DisadvantageEffect('Hindrance: Initiative', 5, note='-10 to all initiative totals')"

@pytest.fixture
def mock_spells():
    cells = {
        f"spell_{d}": Mock(spec=Spell, sequence=d, difficulty=d)
        for d in range(3, 13)
    }
    for c in cells.values():
        c.name = f"Spell {c.sequence}"
    return cells

def test_notebook_rank(mock_spells):
    r"""The range is around the target, $T$, is $-2 \leq d - T < +3$"""
    ranks = workbook_rank(mock_spells)
    assert len(ranks) == 2
    assert all(s.difficulty - 2 <= 5 < s.difficulty + 3 for s in ranks[1])
    assert all(s.difficulty - 2 <= 10 < s.difficulty + 3 for s in ranks[2])

@pytest.fixture
def example_spell():
    example = Spell(
        name="Example",
        notes="GIVEN Example spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {},
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    example.finalize()
    return example

def test_spell(example_spell):
    assert example_spell.difficulty == 4
    ex_copy = eval(repr(example_spell)).finalize()
    assert ex_copy == example_spell, "\n".join(unified_diff(display(ex_copy).splitlines(), display(example_spell).splitlines()))

@pytest.mark.skip(reason="deferred feature: TOML-format dump")
def test_spell_dump(example_spell):
    assert dumps(example_spell).splitlines() == [
        'name = "Example"',
        'notes = "GIVEN Example spell WHEN difficulty THEN 4"',
        'skill = "Acumen: testing"',
    ]

@pytest.fixture
def example_miracle():
    example = Miracle(
        name="Example",
        notes="GIVEN Example spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        # range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        # speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {},
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    example.finalize()
    return example

def test_miracle(example_miracle):
    assert example_miracle.difficulty == 4
    print(display(example_miracle))
    ex_copy = eval(repr(example_miracle)).finalize()
    print(display(ex_copy))
    assert ex_copy == example_miracle, "\n".join(unified_diff(display(ex_copy).splitlines(), display(example_miracle).splitlines()))

def test_build_app(example_spell, capsys):
    book = [example_spell]
    app = build_app(book, rich_markup_mode=None)
    app(["--help"], standalone_mode=False)
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        'Usage: pytest [OPTIONS] COMMAND [ARGS]...',
        '',
        '  Work with this collection of Spells.',
        '',
        'Options:',
        '  --install-completion  Install completion for the current shell.',
        '  --show-completion     Show completion for the current shell, to copy it or',
        '                        customize the installation.',
        '  --help                Show this message and exit.',
        '',
        'Commands:',
        '  display  Write RST-formatted details of all definitions to STDOUT.',
        '  debug    Print debugging information for a specific definition to STDOUT',
    ]


    app(["debug", "Example"], standalone_mode=False)
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        '## Example',
        "  name                : 'Example'",
        "  notes               : 'GIVEN Example spell WHEN difficulty THEN 4'",
        "  skill               : 'Acumen: testing'",
        "  effect              : +12 SkillEffect('Acumen: testing', '+4D')",
        "  duration            :  +0 DurationAspect('1 sec')",
        "  range               :  +0 RangeAspect('1 m')",
        "  casting_time        :  -4 CastingTimeAspect('5 sec')",
        "  speed               :  +0 SpeedAspect.based_on(('range',), 'Instantaneous')",
        '  other_conditions    :',
        "  -  -1 GenericAspect(Decimal('1'), 'Everything else is completed')",
        "Effect Details        : [(Decimal('12'), '+4D')]",
        "Spell Total           : {'effect': 12, 'duration': 0, 'range': 0, 'speed': 0} = 12",
        "Negative Modifiers    : {'casting_time': 4, 'condition: Everything else is [...]': 1} = 5",
        'Difficulty            : ⎡(12 - 5) ÷ 2⎤ = 4',
        '',
        '',
    ]
