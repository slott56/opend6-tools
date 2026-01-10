"""
More tests for the ``character`` module.
"""
from difflib import unified_diff
import random
from unittest.mock import Mock

import pytest

from opend6_tools.character import *

@pytest.fixture
def sample_character():
    random.seed(42)
    hero = Character(
        occupation="Aspiring Hero",
        race="Human",
        agility=Agility(3 * D + 1),
        intellect=Intellect(2 * D + 2),
        coordination=Coordination(2 * D + 2),
        acumen=Acumen(3 * D + 1),
        physique=Physique(3 * D),
        charisma=Charisma(3 * D),
        equipment="Dagger (damage +1D); leather jerkin (Armor Value + 2); shoulder bag with cheese, bread, and silver coins in it",
        description=dedent("""\
            Always fascinated by the traveling sword-showmen that came through
            your little village, you practiced mimicking their techniques (in between your chores
            - and sometimes as part of them). Perhaps inheriting wanderlust from your uncle, you
            have set on to find your fortune in the larger world and maybe gain fame by helping a few
            people along the way"""),
    )
    return hero

@pytest.fixture
def another_character():
    healer = Character(
        occupation="Healer",
        race="Human",
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
        body=10,
        equipment="large healer's kit (+1 bonus to 6 to 12 healing attempts)",
    )
    return healer

def test_report_doc(sample_character):
    """Publication details, long form."""
    w = CharacterWriter()
    text = w.report(sample_character)
    assert text.splitlines() == [
        '',
        '**OpenD6 Fantasy**',
        '',
        '',
        '+--------------------------------------------------+',
        '| Character Name: ________________________________ |',
        '+--------------------------------------------------+',
        '| Occupation: Aspiring Hero                        |',
        '+-------------------------+------------------------+',
        '| Race: Human             | Gender: ______________ |',
        '+----------------+--------+-------+----------------+',
        '| Age: ________  | Height: ______ | Weight: ______ |',
        '+----------------+----------------+----------------+',
        '| Physical Description ___________________________ |',
        '+--------------------------------------------------+',
        '',
        '',
        ':Agility (3D+1):',
        '    ',
        '',
        ':Coordination (2D+2):',
        '    ',
        '',
        ':Physique (3D):',
        '    ',
        '',
        ':Intellect (2D+2):',
        '    ',
        '',
        ':Acumen (3D+1):',
        '    ',
        '',
        ':Charisma (3D):',
        '    ',
        '',
        ':Extranormal ():',
        '    ',
        '',
        ':Advantages:',
        '    ',
        '',
        ':Disadvantages:',
        '    ',
        '',
        ':Special Abilities:',
        '    ',
        '',
        ':Strength Damage: 2D',
        ':Move: 10',
        ':Fate Points: 1',
        ':Character Points: 5',
        ':Body Points: 37',
    ]


def test_report_doc_short(sample_character, another_character):
    """Publication details, short form."""
    characters = {c.occupation: c for c in (sample_character, another_character)}
    w = CharacterWriter_Short()
    text = w.report(characters)
    assert text.splitlines() == [
        '**Aspiring Hero**:',
        'Agility 3D+1, ',
        'Coordination 2D+2, ',
        'Physique 3D, ',
        'Intellect 2D+2, ',
        'Acumen 3D+1, ',
        'Charisma 3D, ',
        '*Move*: 10, ',
        '*Strength Damage*: 2D, ',
        '*Fate Points*: 1, ',
        '*Character Points*: 5, ',
        '*Body Points*: 37, *Equipment*: Dagger (damage +1D); leather jerkin (Armor Value + 2); '
        'shoulder bag with cheese, bread, and silver coins in it.',
        '',
        '',
        '**Healer**:',
        'Agility 2D, ',
        'Coordination 2D, sleight of hand 2D+1, ',
        'Physique 2D, stamina 2D+1, ',
        'Intellect 3D, healing 4D, reading/writing 2D+1, scholar 2D+2, ',
        'Acumen 3D+1, investigation 2D+1, ',
        'Charisma 2D, ',
        '*Move*: 10, ',
        '*Strength Damage*: 1D, ',
        '*Fate Points*: 0, ',
        '*Character Points*: 2, ',
        "*Body Points*: 10, *Equipment*: large healer's kit (+1 bonus to 6 to 12 healing attempts).",
        '',
        '',
    ]


def test_report_sheet(sample_character):
    """Player's Character Sheet -- RST Table"""
    w = CharacterWriter_Table()
    text = w.report(sample_character)
    assert text.splitlines() == [
        '',
        '**OpenD6 Fantasy**',
        '',
        '',
        '+--------------------------------------------------+',
        '| Character Name: ________________________________ |',
        '+--------------------------------------------------+',
        '| Occupation: Aspiring Hero                        |',
        '+-------------------------+------------------------+',
        '| Race: Human             | Gender: ______________ |',
        '+----------------+--------+-------+----------------+',
        '| Age: ________  | Height: ______ | Weight: ______ |',
        '+----------------+----------------+----------------+',
        '| Physical Description ___________________________ |',
        '+--------------------------------------------------+',
        '',
        '',
        '+------------------------------+------------------------------+------------------------------+',
        '| Agility                 3D+1 | Intellect               2D+2 |                              |                 ',
        '+------------------------------+------------------------------+------------------------------+',
        '| acrobatics                   | cultures                     | **Advantages**:              |',
        '|                              |                              |                              |',
        '| climbing                     | devices                      | **Disadvantages**:           |',
        '|                              |                              |                              |',
        '| combat                       | healing                      | **Special Abilities**:       |',
        '|                              |                              |                              |',
        '| contortion                   | navigation                   | **Equipment**: Dagger        |',
        '|                              |                              |                              |',
        '| dodge                        | reading/writing              | (damage +1D); leather        |',
        '|                              |                              |                              |',
        '| fighting                     | scholar                      | jerkin (Armor Value +        |',
        '|                              |                              |                              |',
        '| flying                       | speaking                     | 2); shoulder bag with        |',
        '|                              |                              |                              |',
        '| jumping                      | trading                      | cheese, bread, and           |',
        '|                              |                              |                              |',
        '| melee combat                 | traps                        | silver coins in it           |',
        '|                              |                              |                              |',
        '| riding                       |                              | **Description**:             |',
        '|                              |                              |                              |',
        '| stealth                      |                              | Always fascinated by         |',
        '|                              |                              |                              |',
        '|                              |                              | the traveling sword-         |',
        '|                              |                              |                              |',
        '|                              |                              | showmen that came            |',
        '|                              |                              |                              |',
        '+------------------------------+------------------------------+                              +',
        '| Coordination            2D+2 | Acumen                  3D+1 | through your little          |                 ',
        '+------------------------------+------------------------------+                              +',
        '| charioteering                | artist                       | village, you practiced       |',
        '|                              |                              |                              |',
        '| lockpicking                  | crafting                     | mimicking their              |',
        '|                              |                              |                              |',
        '| marksmanship                 | disguise                     | techniques (in between       |',
        '|                              |                              |                              |',
        '| pilotry                      | gambling                     | your chores - and            |',
        '|                              |                              |                              |',
        '| sleight of hand              | hide                         | sometimes as part of         |',
        '|                              |                              |                              |',
        '| throwing                     | investigation                | them). Perhaps               |',
        '|                              |                              |                              |',
        '|                              | know-how                     | inheriting wanderlust        |',
        '|                              |                              |                              |',
        '|                              | search                       | from your uncle, you         |',
        '|                              |                              |                              |',
        '|                              | streetwise                   | have set on to find          |',
        '|                              |                              |                              |',
        '|                              | survival                     | your fortune in the          |',
        '|                              |                              |                              |',
        '|                              | tracking                     | larger world and maybe       |',
        '|                              |                              |                              |',
        '|                              |                              | gain fame by helping a       |',
        '|                              |                              |                              |',
        '|                              |                              | few people along the         |',
        '|                              |                              |                              |',
        '+------------------------------+------------------------------+                              +',
        '| Physique                  3D | Charisma                  3D | way                          |                 ',
        '+------------------------------+------------------------------+                              +',
        '| lifting                      | animal handling              |                              |',
        '|                              |                              |                              |',
        '| running                      | bluff                        |                              |',
        '|                              |                              |                              |',
        '| stamina                      | charm                        |                              |',
        '|                              |                              |                              |',
        '| swimming                     | command                      |                              |',
        '|                              |                              |                              |',
        '|                              | intimidation                 |                              |',
        '|                              |                              |                              |',
        '|                              | mettle                       |                              |',
        '|                              |                              |                              |',
        '|                              | persuasion                   |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '|                              |                              |                              |',
        '+------------------------------+------------------------------+------------------------------+',
        '| Extranormal            _____ |                              |                              |                 ',
        '+------------------------------+------------------------------+------------------------------+',
        '| alteration                   | Str Damage                2D | Body Points 37               |',
        '|                              |                              |                              |',
        '| apportation                  | Move                      10 | [ ] Stunned   22-29          |',
        '|                              |                              |                              |',
        '| conjuration                  | Fate Pts      1              | [ ] Wounded   15-21          |',
        '|                              |                              |                              |',
        '| divination                   | Character Pts 5              | [ ] Severe    7-14           |',
        '|                              |                              |                              |',
        "|                              | Funds 3D                     | [ ] Incapac'd 4-6            |",
        '|                              |                              |                              |',
        '|                              | Silver 180                   | [ ] Mortal    1-3            |',
        '|                              |                              |                              |',
        '|                              |                              | [ ] Dead                     |',
        '+------------------------------+------------------------------+------------------------------+',
    ]


def test_display(sample_character):
    """Player's Character Sheet -- RST Literal that looks tabular."""
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
        " 'agility': Agility(DieCode(3, 1), {'acrobatics': DieCode(0, 0), 'climbing': DieCode(0, 0), 'contortion': DieCode(0, 0), 'dodge': DieCode(0, 0), 'fighting': DieCode(0, 0), 'flying': DieCode(0, 0), 'jumping': DieCode(0, 0), 'melee combat': DieCode(0, 0), 'combat': DieCode(0, 0), 'riding': DieCode(0, 0), 'stealth': DieCode(0, 0)}),",
        " 'intellect': Intellect(DieCode(2, 2), {'cultures': DieCode(0, 0), 'devices': DieCode(0, 0), 'healing': DieCode(0, 0), 'navigation': DieCode(0, 0), 'reading/writing': DieCode(0, 0), 'scholar': DieCode(0, 0), 'speaking': DieCode(0, 0), 'trading': DieCode(0, 0), 'traps': DieCode(0, 0)}),",
        " 'coordination': Coordination(DieCode(2, 2), {'charioteering': DieCode(0, 0), 'lockpicking': DieCode(0, 0), 'marksmanship': DieCode(0, 0), 'pilotry': DieCode(0, 0), 'sleight of hand': DieCode(0, 0), 'throwing': DieCode(0, 0)}),",
        " 'acumen': Acumen(DieCode(3, 1), {'artist': DieCode(0, 0), 'crafting': DieCode(0, 0), 'disguise': DieCode(0, 0), 'gambling': DieCode(0, 0), 'hide': DieCode(0, 0), 'investigation': DieCode(0, 0), 'know-how': DieCode(0, 0), 'search': DieCode(0, 0), 'streetwise': DieCode(0, 0), 'survival': DieCode(0, 0), 'tracking': DieCode(0, 0)}),",
        " 'physique': Physique(DieCode(3, 0), {'lifting': DieCode(0, 0), 'running': DieCode(0, 0), 'stamina': DieCode(0, 0), 'swimming': DieCode(0, 0)}),",
        " 'charisma': Charisma(DieCode(3, 0), {'animal handling': DieCode(0, 0), 'bluff': DieCode(0, 0), 'charm': DieCode(0, 0), 'command': DieCode(0, 0), 'intimidation': DieCode(0, 0), 'mettle': DieCode(0, 0), 'persuasion': DieCode(0, 0)}),",
        " 'extranormal': Magic(DieCode(0, 0), {'alteration': DieCode(0, 0), 'apportation': DieCode(0, 0), 'conjuration': DieCode(0, 0), 'divination': DieCode(0, 0)}),",
        " 'advantages': OptionList(),",
        " 'disadvantages': OptionList(),",
        " 'special_abilities': OptionList(),",
        " 'equipment': 'Dagger (damage +1D); leather jerkin (Armor Value + 2); shoulder '",
        "              'bag with cheese, bread, and silver coins in it',",
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
        " 'strength_damage': DieCode(2, 0),",
        " 'body': 37,",
        " 'wounds': {'Mortal': '1-3',",
        "            'Incapacitated': '4-6',",
        "            'Severe': '7-14',",
        "            'Wounded': '15-21',",
        "            'Stunned': '22-29'},",
        " 'funds': DieCode(3, 0),",
        " 'silver': 180,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
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
        natural_abilities=OptionList(
            NaturalAbility('wings allow the bird to fly or glide for several hundred miles or as long as there are thermals to keep them aloft'),
            NaturalAbility('beak (damage +2)'),
            NaturalAbility('talons (damage +1D)'),
            NaturalAbility('small size (scale modifier 9)'),
        )
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
        " 'agility': Agility(DieCode(4, 0), {'fighting': DieCode(5, 0), 'flying': DieCode(5, 0)}),",
        " 'intellect': Intellect(DieCode(1, 0), {'cultures': DieCode(0, 0), 'devices': DieCode(0, 0), 'healing': DieCode(0, 0), 'navigation': DieCode(0, 0), 'reading/writing': DieCode(0, 0), 'scholar': DieCode(0, 0), 'speaking': DieCode(0, 0), 'trading': DieCode(0, 0), 'traps': DieCode(0, 0)}),",
        " 'coordination': Coordination(DieCode(1, 0), {'charioteering': DieCode(0, 0), 'lockpicking': DieCode(0, 0), 'marksmanship': DieCode(0, 0), 'pilotry': DieCode(0, 0), 'sleight of hand': DieCode(0, 0), 'throwing': DieCode(0, 0)}),",
        " 'acumen': Acumen(DieCode(2, 0), {'search': DieCode(3, 0), 'tracking': DieCode(3, 0)}),",
        " 'physique': Physique(DieCode(2, 0), {'lifting': DieCode(0, 0), 'running': DieCode(0, 0), 'stamina': DieCode(0, 0), 'swimming': DieCode(0, 0)}),",
        " 'charisma': Charisma(DieCode(2, 0), {'mettle': DieCode(3, 0)}),",
        " 'extranormal': Magic(DieCode(0, 0), {'alteration': DieCode(0, 0), 'apportation': DieCode(0, 0), 'conjuration': DieCode(0, 0), 'divination': DieCode(0, 0)}),",
        " 'advantages': OptionList(),",
        " 'disadvantages': OptionList(),",
        " 'special_abilities': OptionList(),",
        " 'equipment': '',",
        " 'description': '',",
        " 'realm': 'Human realm',",
        " 'move': '32 (flying)/15 (gliding)',",
        " 'strength_damage': DieCode(1, 0),",
        " 'body': 7,",
        " 'wounds': {'Mortal': '1',",
        "            'Incapacitated': '2',",
        "            'Severe': '3',",
        "            'Wounded': '4',",
        "            'Stunned': '5'},",
        " 'funds': DieCode(2, 0),",
        " 'silver': 120,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
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
        " 'agility': Agility(DieCode(3, 0), {'fighting': DieCode(4, 0), 'flying': "
    'DieCode(3, 1)}),',
        " 'intellect': Intellect(DieCode(3, 0), {'cultures': DieCode(0, 0), "
    "'devices': DieCode(0, 0), 'healing': DieCode(0, 0), 'navigation': "
    "DieCode(0, 0), 'reading/writing': DieCode(0, 0), 'scholar': DieCode(0, "
    "0), 'speaking': DieCode(0, 0), 'trading': DieCode(0, 0), 'traps': "
    'DieCode(0, 0)}),',
        " 'coordination': Coordination(DieCode(2, 0), {'marksmanship': DieCode(3, "
    '0)}),',
        " 'acumen': Acumen(DieCode(2, 0), {'artist': DieCode(0, 0), 'crafting': "
    "DieCode(0, 0), 'disguise': DieCode(0, 0), 'gambling': DieCode(0, 0), "
    "'hide': DieCode(0, 0), 'investigation': DieCode(0, 0), 'know-how': "
    "DieCode(0, 0), 'search': DieCode(0, 0), 'streetwise': DieCode(0, 0), "
    "'survival': DieCode(0, 0), 'tracking': DieCode(0, 0)}),",
        " 'physique': Physique(DieCode(5, 0), {'lifting': DieCode(5, 1)}),",
        " 'charisma': Charisma(DieCode(3, 0), {'intimidation': DieCode(6, 0), "
    "'mettle': DieCode(3, 2)}),",
        " 'extranormal': Magic(DieCode(0, 0), {'alteration': DieCode(0, 0), "
    "'apportation': DieCode(0, 0), 'conjuration': DieCode(0, 0), 'divination': "
    'DieCode(0, 0)}),',
        " 'advantages': OptionList(Size(rank=4, notes='scale value 12')),",
        " 'disadvantages': OptionList(AchillesHeel(rank=3, notes='Metabolic "
          "Difference, requires large quantities of fresh meat'), Infamy(rank=3, "
          "notes='species feared and hunted because of destructive tendencies'), "
          "Quirk(rank=3, notes='easily angered'), Quirk(rank=3, notes='greedy')),",
        " 'special_abilities': OptionList(NaturalArmor(rank=2, notes='Scales, +1D "
          "to damage resistance total'), NaturalHandWeapon(rank=3, notes='Claws, "
          "damage +3D'), NaturalRangedWeapon(rank=2, notes='Fiery Breath, damage "
          "6D')),",
        " 'equipment': '',",
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
        " 'funds': DieCode(3, 0),",
        " 'silver': 180,",
        " 'fate_points': 1,",
        " 'character_points': 5,",
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

@pytest.fixture
def mock_creature_list(sample_creature, complex_creature):
    return [sample_creature, complex_creature]

def test_display_many(mock_creature_list):
    w = CharacterWriter_Short()
    text = w.report(mock_creature_list)
    assert text.splitlines() == [
         '**Bird of Prey (Falcon, Hawk)**:',
         'Agility 4D, fighting 5D, flying 5D, ',
         'Coordination 1D, ',
         'Physique 2D, ',
         'Intellect 1D, ',
         'Acumen 2D, search 3D, tracking 3D, ',
         'Charisma 2D, mettle 3D, ',
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
         'Agility 3D, fighting 4D, flying 3D+1, ',
         'Coordination 2D, marksmanship 3D, ',
         'Physique 5D, lifting 5D+1, ',
         'Intellect 3D, ',
         'Acumen 2D, ',
         'Charisma 3D, intimidation 6D, mettle 3D+2, ',
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

def test_build_app(mock_creature_list, capsys):
    app = build_app(mock_creature_list, rich_markup_mode=None)
    app(["--help"], standalone_mode=False)
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        'Usage: pytest [OPTIONS] COMMAND [ARGS]...',
        '',
        '  Work with this collection of Characters (or Creatures).',
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
        '  blank    Print a blank character sheet.',
    ]

