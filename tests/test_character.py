"""
Tests for the ``character`` package.

Most of these belong in module-specific test suites: test_character_output, etc.
"""
from pathlib import Path
import random
from unittest.mock import sentinel
from textwrap import dedent

import pytest

from opend6_tools.character import *

def test_attribute():
    class TestAttribute(Attribute):
        SKILL_NAMES = ["skill1", "skill2"]
    a = TestAttribute(sentinel.BASE, {"skill1": 42, "skill2": 42*D})
    assert a.name == "TestAttribute"
    assert a.skill1 == 42
    assert a.skill2 == 42*D
    assert a.nothing is None
    assert repr(a) == "TestAttribute(sentinel.BASE, {'skill1': 14*D, 'skill2': 42*D})"
    assert a.row(0) == "skill1           14D"
    assert a.row(1) == "skill2           42D"
    assert a.row(2) == ""
    assert a.row(3) == ""
    assert a['skill1'] == 42

@pytest.fixture
def sample_character():
    random.seed(42)  # Forces a wild die result
    hero = Character(
        occupation="Aspiring Hero",
        race="Human",
        agility=Agility(3 * D + 1),
        intellect=Intellect(2 * D + 2),
        coordination=Coordination(2 * D + 2),
        acumen=Acumen(3 * D + 1),
        physique=Physique(3 * D),
        charisma=Charisma(3 * D),
        weapons=["Dagger (damage +1D)"],
        armor=["leather jerkin (Armor Value +2)"],
        equipment=["shoulder bag with cheese, bread, and silver coins in it"],
        description=dedent("""\
            Always fascinated by the traveling sword-showmen that came through
            your little village, you practiced mimicking their techniques (in between your chores
            - and sometimes as part of them). Perhaps inheriting wanderlust from your uncle, you
            have set on to find your fortune in the larger world and maybe gain fame by helping a few
            people along the way"""),
    )
    return hero

def test_sample_character(sample_character):
    assert sample_character.budget_check() == {
        'Attributes': '18D',
        'Options': 'Nothing',
        'Skills': 'Nothing',
    }

@pytest.fixture
def another_character():
    random.seed(42)
    healer = Character(
        occupation="Healer",
        race="Human",
        height=None,
        weight=None,
        agility=Agility(2 * D),
        coordination=Coordination(
            2 * D,
            {"sleight of hand": 2 * D + 1, "throwing": 0}),
        physique=Physique(
            2 * D, {"stamina": 2 * D + 1}),
        intellect=Intellect(
            3 * D,
            {
                "healing": 4 * D,
                "reading/writing": 2 * D + 1,
                "scholar": 2 * D + 2,
            },
        ),
        acumen=Acumen(
            3 * D + 1,
            {
                "investigation": 2 * D + 1,
            },
        ),
        charisma=Charisma(2 * D),
        move=10,
        fate_points=0,
        character_points=2,
        body=2*D+20,
        equipment="large healer's kit (+1 bonus to 6 to 12 healing attempts)",
    )
    return healer

def test_another_character(another_character):
    assert another_character.budget_check() == {
        'Attributes': '14D+1',
        'Options': 'Nothing',
        'Skills': '16D',
    }
    assert another_character.body == 25
    assert another_character.height == "186cm"
    assert another_character.weight == "92kg"

def test_special_cases():
    random.seed(42)
    c = Character(body=0, charisma=Charisma(4*D), gender='female', height=None, weight=None)
    assert c.wounds == {'Stunned': '80%', 'Wounded': '60%', 'Severe': '40%', 'Incapacitated': '20%', 'Mortal': '10%'}
    assert c.funds_roll() == 4*D
    assert c.height == "166cm"
    assert c.weight == "72kg"
    assert c.height_weight_roll(symmetric=True) == ('166cm', '81kg')

# This may be redundant -- see test_character_workbook
def test_display(sample_character):
    """Player's Character Sheet -- RST Literal that looks tabular.

    Example from Fantasy Hero Introduction.
    """
    text = display(sample_character)
    assert text.splitlines() == [
        "{'name': '',",
        " 'occupation': 'Aspiring Hero',",
        " 'race': 'Human',",
        " 'gender': '',",
        " 'age': '',",
        " 'height': '',",
        " 'weight': '',",
        " 'physical_description': '',",
        " 'agility': Agility(3*D+1, {'acrobatics': 0*D, 'climbing': 0*D, 'contortion': 0*D, 'dodge': 0*D, 'fighting': 0*D, 'flying': 0*D, 'jumping': 0*D, 'melee combat': 0*D, 'combat': 0*D, 'riding': 0*D, 'stealth': 0*D}),",
        " 'intellect': Intellect(2*D+2, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),",
        " 'coordination': Coordination(2*D+2, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),",
        " 'acumen': Acumen(3*D+1, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, 'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, 'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),",
        " 'physique': Physique(3*D, {'lifting': 0*D, 'running': 0*D, 'stamina': 0*D, 'swimming': 0*D}),",
        " 'charisma': Charisma(3*D, {'animal handling': 0*D, 'bluff': 0*D, 'charm': 0*D, 'command': 0*D, 'intimidation': 0*D, 'mettle': 0*D, 'persuasion': 0*D}),",
        " 'extranormal': Magic(0*D, {'alteration': 0*D, 'apportation': 0*D, 'conjuration': 0*D, 'divination': 0*D}),",
        " 'advantages': OptionList(),",
        " 'disadvantages': OptionList(),",
        " 'special_abilities': OptionList(),",
        " 'description': 'Always fascinated by the traveling sword-showmen that came '",
        "                'through\\n'",
        "                'your little village, you practiced mimicking their techniques '",
        "                '(in between your chores\\n'",
        "                '- and sometimes as part of them). Perhaps inheriting '",
        "                'wanderlust from your uncle, you\\n'",
        "                'have set on to find your fortune in the larger world and '",
        "                'maybe gain fame by helping a few\\n'",
        "                'people along the way',",
        " 'realm': 'Human realm',",
        " 'move': 10,",
        " 'strength_damage': 2*D,",
        " 'body': 28,",
        " 'wounds': {'Mortal': '1-2',",
        "            'Incapacitated': '3-5',",
        "            'Severe': '6-10',",
        "            'Wounded': '11-16',",
        "            'Stunned': '17-21'},",
        " 'funds': 3*D,",
        " 'silver': 180,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
        " 'equipment': NoteList('shoulder bag with cheese, bread, and silver coins in it'),",
        " 'armor': NoteList('leather jerkin (Armor Value +2)'),",
        " 'weapons': NoteList('Dagger (damage +1D)'),",
        " 'spells': NoteList(),",
        " 'personality': '',",
        " 'objectives': '',",
        " 'native_language': '',",
        " 'other_notes': '',",
        " 'Check': {'Attributes': '18D out of 18D',",
        "           'Skills': 'Nothing out of 7D',",
        "           'Options': 'Nothing'}}",
    ]

@pytest.fixture
def sample_creature():
    raptor = Creature(
        name='Bird of Prey (Falcon, Hawk)',
        agility=Agility(4 * D, {'fighting': 5 * D, 'flying': 5 * D}),
        coordination=Coordination(1 * D),
        physique=Physique(2 * D),
        intellect=Intellect(1 * D),
        acumen=Acumen(2 * D, {'search': 3 * D, 'tracking': 3 * D}),
        charisma=Charisma(2 * D, {'mettle': 3 * D}),
        move='32 (flying)/15 (gliding)',
        # strength_damage='1D',
        body=7,   # '7 /Wound levels: 1',
        natural_abilities=[
            NaturalAbility('wings allow the bird to fly or glide for several hundred miles or as long as there are thermals to keep them aloft'),
            NaturalAbility('beak (damage +2)'),
            NaturalAbility('talons (damage +1D)'),
            NaturalAbility('small size (scale modifier 9)'),
        ]
    )
    return raptor

def test_creature(sample_creature):
    text = display(sample_creature)
    assert text.splitlines() == [
        "{'name': 'Bird of Prey (Falcon, Hawk)',",
        " 'occupation': '',",
        " 'race': '',",
        " 'gender': '',",
        " 'age': '',",
        " 'height': '',",
        " 'weight': '',",
        " 'physical_description': '',",
        " 'agility': Agility(4*D, {'fighting': 5*D, 'flying': 5*D}),",
        " 'intellect': Intellect(1*D, {'cultures': 0*D, 'devices': 0*D, 'healing': 0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),",
        " 'coordination': Coordination(1*D, {'charioteering': 0*D, 'lockpicking': 0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, 'throwing': 0*D}),",
        " 'acumen': Acumen(2*D, {'search': 3*D, 'tracking': 3*D}),",
        " 'physique': Physique(2*D, {'lifting': 0*D, 'running': 0*D, 'stamina': 0*D, 'swimming': 0*D}),",
        " 'charisma': Charisma(2*D, {'mettle': 3*D}),",
        " 'extranormal': Magic(0*D, {'alteration': 0*D, 'apportation': 0*D, 'conjuration': 0*D, 'divination': 0*D}),",
        " 'advantages': OptionList(),",
        " 'disadvantages': OptionList(),",
        " 'special_abilities': OptionList(),",
        " 'description': '',",
        " 'realm': 'Human realm',",
        " 'move': '32 (flying)/15 (gliding)',",
        " 'strength_damage': 1*D,",
        " 'body': 7,",
        " 'wounds': {'Mortal': '1',",
        "            'Incapacitated': '2',",
        "            'Severe': '3',",
        "            'Wounded': '4',",
        "            'Stunned': '5'},",
        " 'funds': 2*D,",
        " 'silver': 120,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
        " 'equipment': NoteList(),",
        " 'armor': NoteList(),",
        " 'weapons': NoteList(),",
        " 'spells': NoteList(),",
        " 'personality': '',",
        " 'objectives': '',",
        " 'native_language': '',",
        " 'other_notes': '',",
        " 'natural_abilities': OptionList(NaturalAbility(notes='wings allow the "
          'bird to fly or glide for several hundred miles or as long as there are '
          "thermals to keep them aloft'), NaturalAbility(notes='beak (damage +2)'), "
          "NaturalAbility(notes='talons (damage +1D)'), NaturalAbility(notes='small "
          "size (scale modifier 9)')),",
        " 'note': '',",
        " 'Check': {'Attributes': '12D out of 18D',",
        "           'Skills': '19D out of 7D',",
        "           'Options': 'Nothing'}}",
    ]

@pytest.fixture
def complex_creature():
    dragon_young = Creature(
        name='Dragon, Young',
        agility=Agility(3 * D, {'fighting': 4 * D, 'flying': 3 * D + 1}),
        coordination=Coordination(2 * D, {'marksmanship': 3 * D}),
        physique=Physique(5 * D, {'lifting': 5 * D + 1}),
        intellect=Intellect(3 * D),
        acumen=Acumen(2 * D),
        charisma=Charisma(3 * D, {'intimidation': 6 * D, 'mettle': 3 * D + 2}),
        move='10',
        strength_damage='3D',
        body=32,
        advantages=OptionList(Size(4, "scale value 12")),
        disadvantages=[
            AchillesHeel(3, "Metabolic Difference, requires large quantities of fresh meat"),
            Infamy(3, "species feared and hunted because of destructive tendencies"),
            Quirk(3, "easily angered"),
            Quirk( 3, "greedy"),
        ],
        special_abilities=[
            NaturalArmor(2, "Scales, +1D to damage resistance total"),
            NaturalHandWeapon(3, "Claws, damage +3D"),
            NaturalRangedWeapon(2, "Fiery Breath, damage 6D"),
        ],
    )
    return dragon_young

def test_complex_creature(complex_creature):
    text = display(complex_creature, check=CharacterBudget.EXPERIENCED)
    assert text.splitlines() == [
        "{'name': 'Dragon, Young',",
        " 'occupation': '',",
        " 'race': '',",
        " 'gender': '',",
        " 'age': '',",
        " 'height': '',",
        " 'weight': '',",
        " 'physical_description': '',",
        " 'agility': Agility(3*D, {'fighting': 4*D, 'flying': "
    '3*D+1}),',
        " 'intellect': Intellect(3*D, {'cultures': 0*D, "
    "'devices': 0*D, 'healing': 0*D, 'navigation': "
    "0*D, 'reading/writing': 0*D, 'scholar': 0*D, 'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),",
        " 'coordination': Coordination(2*D, {'marksmanship': 3*D}),",
        " 'acumen': Acumen(2*D, {'artist': 0*D, 'crafting': "
    "0*D, 'disguise': 0*D, 'gambling': 0*D, "
    "'hide': 0*D, 'investigation': 0*D, 'know-how': "
    "0*D, 'search': 0*D, 'streetwise': 0*D, "
    "'survival': 0*D, 'tracking': 0*D}),",
        " 'physique': Physique(5*D, {'lifting': 5*D+1}),",
        " 'charisma': Charisma(3*D, {'intimidation': 6*D, "
    "'mettle': 3*D+2}),",
        " 'extranormal': Magic(0*D, {'alteration': 0*D, "
    "'apportation': 0*D, 'conjuration': 0*D, 'divination': "
    '0*D}),',
        " 'advantages': OptionList(Size(rank=4, notes='scale value 12')),",
        " 'disadvantages': OptionList(AchillesHeel(rank=3, notes='Metabolic "
          "Difference, requires large quantities of fresh meat'), Infamy(rank=3, "
          "notes='species feared and hunted because of destructive tendencies'), "
          "Quirk(rank=3, notes='easily angered'), Quirk(rank=3, notes='greedy')),",
        " 'special_abilities': OptionList(NaturalArmor(rank=2, notes='Scales, +1D "
          "to damage resistance total'), NaturalHandWeapon(rank=3, notes='Claws, "
          "damage +3D'), NaturalRangedWeapon(rank=2, notes='Fiery Breath, damage "
          "6D')),",
        " 'description': '',",
        " 'realm': 'Human realm',",
        " 'move': '10',",
        " 'strength_damage': '3D',",
        " 'body': 32,",
        " 'wounds': {'Mortal': '1-2',",
        "            'Incapacitated': '3-5',",
        "            'Severe': '6-12',",
        "            'Wounded': '13-18',",
        "            'Stunned': '19-25'},",
        " 'funds': 3*D,",
        " 'silver': 180,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
        " 'equipment': NoteList(),",
        " 'armor': NoteList(),",
        " 'weapons': NoteList(),",
        " 'spells': NoteList(),",
        " 'personality': '',",
        " 'objectives': '',",
        " 'native_language': '',",
        " 'other_notes': '',",
        " 'natural_abilities': OptionList(),",
        " 'note': '',",
        " 'Check': {'Attributes': '18D out of 18D',",
        "           'Skills': '25D+1 out of 22D',",
        "           'Options': '3D+1'}}",
    ]

def test_CharacterWriter_HTML2_complex(complex_creature, tmp_path):
    """Complex Creature Character Sheet -- HTML Content, suitable for conversion to PDF."""
    name = "character3.html"
    w = CharacterWriter_HTML2()
    destination = tmp_path / name
    text = w.report(complex_creature)
    destination.write_text(text)
    print(f"file://{destination}")
    expected = Path.cwd() / "tests" / name
    assert destination.read_text() == expected.read_text()

@pytest.fixture
def mock_creature_list(sample_creature, complex_creature):
    return [sample_creature, complex_creature]

def test_display_many(mock_creature_list, capsys):
    expected = [
        '**Bird of Prey (Falcon, Hawk)**:',
        'Agility 4D, fighting 5D, flying 5D, Coordination 1D, Physique 2D, '
        'Intellect 1D, Acumen 2D, search 3D, tracking 3D, Charisma 2D, mettle 3D.',
        '*Move*: 32 (flying)/15 (gliding), ',
        '*Strength Damage*: 1D, ',
        '*Fate Points*: 1, ',
        '*Character Points*: 5, ',
        '*Body Points*: 7, *Natural Abilities*: wings allow the bird to fly or '
        'glide for several hundred miles or as long as there are thermals to keep '
        'them aloft; beak (damage +2); talons (damage +1D); small size (scale '
        'modifier 9).',
        '',
        '',
        '**Dragon, Young**:',
        'Agility 3D, fighting 4D, flying 3D+1, Coordination 2D, marksmanship 3D, '
        'Physique 5D, lifting 5D+1, Intellect 3D, Acumen 2D, Charisma 3D, '
        'intimidation 6D, mettle 3D+2.',
        '*Advantages*: Size (R4), scale value 12,',
        "*Disadvantages*: Achilles' Heel (R3), Metabolic Difference, requires "
        'large quantities of fresh meat; Infamy (R3), species feared and hunted '
        'because of destructive tendencies; Quirk (R3), easily angered; Quirk '
        '(R3), greedy,',
        '*Special Abilities*: Natural Armor (R2), Scales, +1D to damage resistance '
        'total; Natural Hand-to-Hand Weapon (R3), Claws, damage +3D; Natural '
        'Ranged Weapon (R2), Fiery Breath, damage 6D,',
        '*Move*: 10, ',
        '*Strength Damage*: 3D, ',
        '*Fate Points*: 1, ',
        '*Character Points*: 5, ',
        '*Body Points*: 32.',
        '',
        '',
    ]
    w = CharacterWriter_Short()
    text_writer = w.report(mock_creature_list)
    assert text_writer.splitlines() == expected

    detail(mock_creature_list, Format.SHORT)
    text_detail, err = capsys.readouterr()
    assert text_detail.splitlines() == expected + [""]


@pytest.fixture
def sample_wizard():
    wizard = Character(
        occupation="Wizard",
        race="Human",
        agility=Agility(
            2 * D + 1,
            {
                "acrobatics": 0,
                "fighting": 0,
                "riding": 0,
                "stealth": 0,
            },
        ),
        intellect=Intellect(
            3 * D + 1,
            {
                "cultures": 0,
                "devices": 0,
                "healing": 0,
                "navigation": 0,
                "reading/writing": 0,
                "scholar": 0,
                "speaking": 0,
                "trading": 0,
                "traps": 0,
            },
        ),
        coordination=Coordination(
            2 * D,
            {
                "charioteering": 0,
                "marksmanship": 0,
                "sleight of hand": 0,
                "throwing": 0,
            },
        ),
        acumen=Acumen(
            3 * D + 1,
            {
                "artist": 0,
                "crafting": 0,
                "disguise": 0,
                "gambling": 0,
                "hide": 0,
                "investigation": 0,
                "know-how": 0,
                "search": 0,
                "streetwise": 0,
                "survival": 0,
            },
        ),
        physique=Physique(
            2 * D,
            {
                "lifting": 0,
                "running": 0,
            },
        ),
        charisma=Charisma(
            2 * D + 2,
            {
                "animal handling": 0,
                "bluff": 0,
                "charm": 0,
                "command": 0,
                "intimidation": 0,
                "mettle": 0,
                "persuasion": 0,
            },
        ),
        extranormal=Magic(
            2 * D + 1,
            {
                "alteration": 0,
                "apportation": 0,
                "conjuration": 0,
                "divination": 0,
            },
        ),
        advantages=[],
        disadvantages=[
            Prejudice(2,
                      "the wizard cult you belonged to has a bad reputation, and you find many people shun you"),
        ],
        special_abilities=[
            LuckGood(1),
        ],
        armor=["soft leather jerkin and pants (Armor Value +2)"],
        weapons=["Small knife (damage +2)"],
        equipment=["paper, quill, and kin", "a few small spell components",
                   "a few spells on scrolls"],
        spells=["Charm, 5, charm skill bonus of +4D", "Deadly Dart, 11, +4D in damage"],
        description=dedent("""\
        Though the art of spell design fascinates you, the idea of staying locked in a
        stuffy library doesn't. You've taken  to adventuring to find inspiration for new
        spells, lost sources of mystical energy, and forgotten ancient artifacts."""),
    )
    return wizard

# Goes in test_character_workbook...
def test_workbook_display(sample_wizard, tmp_path):
    """Complex Character Sheet with spells -- HTML Content, suitable for conversion to PDF."""
    name = "character4.html"
    w = CharacterWriter_HTML2()
    destination = tmp_path / name
    text = w.report(sample_wizard)
    destination.write_text(text)
    print(f"file://{destination}")
    expected = Path.cwd() / "tests" / name
    assert destination.read_text() == expected.read_text()

@pytest.fixture
def some_sword():
    s = Sword(
        name="Halfwit",
        intellect=Intellect(2*D),
        charisma=Charisma(3*D, {'charm': 1*D}),
        description="Full of bad ideas.",
        natural_abilities=[
            BadLuck(2, "Really unhelpful")
        ]
    )
    return s

def test_sword(some_sword):
    assert some_sword.natural_abilities == OptionList(BadLuck(rank=2, notes='Really unhelpful'))
