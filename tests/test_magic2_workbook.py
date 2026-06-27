"""Test magic.workbook module.
"""
from unittest.mock import Mock, MagicMock
import pytest

from opend6_tools.magic.workbook import *

def mock_aspect_details_base():
    aspect = Mock(
        spec=Aspect,
        base=MagicMock(
            spec=NormalizedAspect,
            sign=Mock(return_value=Sign.Increase),
            __str__=Mock(return_value="NormalizedAspect"),
        ),
        difficulty=Mock(return_value=Decimal(42)),
        source=Mock(return_value="Aspect()")
    )
    aspect.name = "Mock Aspect"
    return aspect, True, "  aspect              : +42 Aspect()\n                            NormalizedAspect"

def mock_aspect_base():
    aspect = Mock(
        spec=Aspect,
        base=MagicMock(
            spec=NormalizedAspect,
            sign=Mock(return_value=Sign.Increase),
            __str__=Mock(return_value="NormalizedAspect"),
        ),
        difficulty=Mock(return_value=Decimal(42)),
        source=Mock(return_value="Aspect()")
    )
    aspect.name = "Mock Aspect"
    return aspect, False, "  aspect              : +42 Aspect()"

def mock_aspect():
    aspect = Mock(
        spec=Aspect,
        base=None,
        difficulty=Mock(return_value=Decimal(42)),
        source=Mock(return_value="Aspect()"),
        origin="Origin_Def()",
    )
    aspect.name = "Mock Aspect"
    return aspect, False, "  aspect              : Origin_Def()"


@pytest.mark.parametrize(
    "aspect, details, expected",
    [
        mock_aspect_details_base(),
        mock_aspect_base(),
        mock_aspect(),
    ]
)
def test_aspect_format(aspect, details, expected):
    details = aspect_format("aspect", aspect, details=details)
    assert details == expected

@pytest.fixture
def mock_spells():
    cells = {
        f"spell_{d}": Mock(
            spec=Spell,
            sequence=d,
            difficulty=d,
            effect=Mock(base=Mock(sign=Mock(return_value=Sign.Increase)), difficulty=Mock(return_value=d)),
            notes=f"{d}",
            aspects={},
            other_aspects={},
            other_conditions=[],
            _spell_total={},
            _negative_modifiers={},)
        for d in range(3, 13)
    }
    # Can't set ``name`` in a Mock directly...
    for c in cells.values():
        c.name = f"Spell {c.sequence}"
    return cells

def test_notebook_rank(mock_spells):
    r"""The range is around the target, $T$, is $-2 \leq d - T < +3$"""
    ranks = workbook_rank(mock_spells)
    assert len(ranks) == 2
    assert all(s.difficulty - 2 <= 5 < s.difficulty + 3 for s in ranks[1])
    assert all(s.difficulty - 2 <= 10 < s.difficulty + 3 for s in ranks[2])


def test_workbook_validation(mock_spells):
    report = workbook_validation(mock_spells, 2, 1)
    assert len(report) == 12
    assert report[0] == '## Difficulty errors.'
    assert report[1].startswith("### 'Spell 3'\n\n")

def test_workbook_validation_function(mock_spells):
    report = workbook_validation(mock_spells, lambda s: s.difficulty < 3)
    assert len(report) == 12
    assert report[0] == '## Difficulty errors.'
    assert report[1].startswith("### 'Spell 3'\n\n")

def test_workbook_validation_all_good(mock_spells):
    report = workbook_validation(mock_spells, 8, 14)
    assert len(report) == 2
    assert report == ['## All spells approximately 8 difficulty, 1..15.', '10 Spells']

@pytest.fixture
def example_spell():
    base_aspect = MagicMock(
        spec=NormalizedAspect,
        sign=Mock(return_value=Sign.Increase),
        __str__=Mock(return_value="NormalizedAspect"),
    )
    aspect = Mock(
        spec=Aspect,
        base=base_aspect,
        proxy=Mock(attr_paths=()),
        difficulty=Mock(return_value=Decimal(0)),
        description="description",
        source=Mock(return_value="Aspect()"),
    )
    aspect.name = "mock aspect"
    example = Spell(
        name="Example",
        notes="GIVEN Example spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {
            "something": aspect
        },
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    return example

def test_spell_display(example_spell):
    buffer = display(example_spell)
    assert buffer.splitlines() == [
         "  name                : 'Example'",
         "  notes               : 'GIVEN Example spell WHEN difficulty THEN 4'",
         "  skill               : 'Acumen: testing'",
         "  effect              : +12 SkillEffect('Acumen: testing', '+4D')",
         "  duration            :  +0 DurationAspect('1 sec')",
         "  range               :  +0 RangeAspect('1m')",
         "  casting_time        :  -4 CastingTimeAspect('5 sec')",
         "  speed               :  +0 SpeedAspect.based_on('range', *(), **{'description': 'Instantaneous'})",
         '  other_aspects       :',
         "  - something         :  +0 Aspect()",
         '  other_conditions    :',
         "  - Everything [...]  :  -1 GenericAspect(1, 'Everything else is completed')",
         "Effect Details        : SkillEffect based on DiceUnit [Modifier(difficulty=Decimal('12'), description='4*D')]",
         "Spell Total           : {'effect': 12, 'duration': 0, 'range': 0, 'speed': 0, 'something': 0} = 12",
         "Negative Modifiers    : {'casting_time': 4, 'condition: Everything else is [...]': 1} = 5",
         'Difficulty            : ⎡(12 - 5) ÷ 2⎤ = 4',
    ]

@pytest.fixture
def example_item():
    amulet_protection = Item(
        name = "Amulet of Protection",
        notes = "An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura",
        effect = SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, "non-enchanted weapons",
            modifications=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
        ),
        area_effect = AreaEffectAspect("2m radius sphere"),
        other_aspects={
            'fragile': GenericAspect(0, "Fragile")
        },
        other_conditions=[
            GenericAspect(0, "+1 under a full moon")
        ],
        type="Jewelry",
        price="H (200 G)"
    )
    return amulet_protection

def test_item_display(example_item):
    buffer = display(example_item)
    assert buffer.splitlines() == [
        "  name                : 'Amulet of Protection'",
        "  notes               : 'An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura'",
        "  type                : 'Jewelry'",
        "  price               : 'H (200 G)'",
        "  effect              :  +3 SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, 'non-enchanted weapons', modifications=[Limitation(LimitationType.burn_out, 1, 'can be lost or stolen')])",
        "  area_effect         : +10 AreaEffectAspect('2m radius sphere')",
        '  other_aspects       :',
        "  - fragile           :  -0 GenericAspect(0, 'Fragile')",
        '  other_conditions    :',
        "  - +1 under a [...]  :  -0 GenericAspect(0, '+1 under a full moon')",
        "Effect Details        : SpecialAbilityEffect based on SpecialAbilityLookup [Modifier(difficulty=Decimal('2'), description='attack_resistance')]",
        "Spell Total           : {'effect': 3, 'area_effect': 10} = 13",
        "Negative Modifiers    : {'fragile': 0, 'condition: +1 under a full moon': 0} = 0",
        'Difficulty            : ⎡(13 - 0) ÷ 2⎤ = 7'
    ]

def test_debug_all(example_spell, capsys):
    debug([example_spell], None)
    out, err = capsys.readouterr()
    assert out.splitlines()[0] == "## Example"

def test_debug_byname(example_spell, capsys):
    debug([example_spell], "Example")
    out, err = capsys.readouterr()
    assert out.splitlines()[0] == "## Example"
