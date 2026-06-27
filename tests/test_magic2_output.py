"""Test magic.output module.
"""
from unittest.mock import Mock
import pytest

from opend6_tools.magic.output import *

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
    return example

def test_spell_dump(example_spell):
    assert dumps(example_spell).splitlines() == [
        'name = "Example"',
        'notes = "GIVEN Example spell WHEN difficulty THEN 4"',
        '',
        '[effect]',
        'class_ = "SkillEffect"',
        'args = [', '    "Acumen: testing",', '    "+4D",', ']',
        '',
        '[duration]',
        'class_ = "DurationAspect"',
        'args = [', '    "1 sec",', ']',
        '',
        '[range]',
        'class_ = "RangeAspect"',
        'args = [', '    "1m",', ']',
        '',
        '[casting_time]',
        'class_ = "CastingTimeAspect"',
        'args = [', '    "5 sec",', ']',
        '',
        '[speed]',
        'class_ = "SpeedAspect"',
        'args = [',
        '    0,',
        '    "based_on(\'range\', description=\'Instantaneous\')",',
        ']',
        '',
        '[[other_conditions]]',
        'class_ = "GenericAspect"',
        'args = [', '    1,', '    "Everything else is completed",', ']'
    ]


@pytest.fixture
def partial_spell():
    partial = Spell(
        name="Template Spell",
        notes="GIVEN Partial spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect.based_on_spell("duration"),
        range=RangeAspect.based_on_spell("range"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {},
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    return partial

def test_spellwriter(partial_spell):
    sw = SpellWriter()
    output = sw.report(partial_spell)
    assert output.splitlines() == [
        'Template Spell',
        '~~~~~~~~~~~~~~',
        '',
        ':Skill: Acumen: testing',
        ':Difficulty: 4 ',
        ':Effect: 12 (Acumen: testing 4*D)',
        ":Range: based_on_spell('range') \\(0)",
        ":Speed: based_on('range', description='Instantaneous') \\(0)",
        ":Duration: based_on_spell('duration') \\(0)",
        ':Casting Time: 5 sec \\(4)',
        '',
        '',
        ':Other Conditions:',
        '    (1): Everything else is completed',
        '',
        '',
        '',
        '',
        'GIVEN Partial spell WHEN difficulty THEN 4',
    ]

def test_spellwriter_groups(example_spell):
    sw = SpellWriter()
    output = sw.report({'group': [example_spell]})
    assert output.splitlines()[1:3] == ['group', '=====']

@pytest.fixture
def example_item():
    amulet_protection = Item(
        name = "Amulet of Protection",
        notes = "An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura",
        effect = SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, "non-enchanted weapons",
            modifications=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
        ),
        type="Jewelry",
        price="H (200 G)"
    )
    return amulet_protection

def test_itemwriter(example_item):
    iw = ItemWriter()
    output = iw.report(example_item)
    assert output.splitlines() == [
        'Amulet of Protection',
        '~~~~~~~~~~~~~~~~~~~~',
        '',
        'An oddly-shaped pendant on a thick leather cord envelopes the wearer in a '
        'defensive aura',
        '',
        ':Effect: 3 (attack_resistance (R1) non-enchanted weapons; burn_out (R1) can be lost or stolen)',
        ':Type: Jewelry',
        ':Price: H (200 G)',
        '',

    ]

def test_summary(example_spell):
    from io import StringIO
    buffer = StringIO()
    summary([example_spell], buffer)
    out = buffer.getvalue()
    assert out.splitlines() == [
        "Spell,Skill,Difficulty,Effect",
        "Example,*Acumen: testing*,4,Acumen: testing 4*D",
    ]

def test_summary_multi(example_spell):
    from io import StringIO
    buffer = StringIO()
    summary({'group': [example_spell]}, buffer)
    out = buffer.getvalue()
    assert out.splitlines() == [
        "Spell,Skill,Difficulty,Effect",
        '**group**',
        "Example,*Acumen: testing*,4,Acumen: testing 4*D",
    ]

def test_item_summary(example_item):
    from io import StringIO
    buffer = StringIO()
    item_summary([example_item], buffer)
    out = buffer.getvalue()
    assert out.splitlines() == [
        "Name,Type,Price,Effect",
        "Amulet of Protection,*Jewelry*,H (200 G),attack_resistance (R1) non-enchanted weapons; burn_out (R1) can be lost or stolen"
    ]


def test_detail_item(example_item, capsys):
    detail(example_item)
    out, err = capsys.readouterr()
    assert out.splitlines()[0] == "Amulet of Protection"

def test_detail_mapping_item(example_item, capsys):
    detail({'Amulets': [example_item]})
    out, err = capsys.readouterr()
    assert out.splitlines()[1] == "Amulets"

def test_detail_mapping_spells(example_spell, capsys):
    detail({'Rank 1': [example_spell]})
    out, err = capsys.readouterr()
    assert out.splitlines()[1] == "Rank 1"
