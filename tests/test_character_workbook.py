"""Test character.workbook module.
"""
import random
from unittest.mock import Mock, sentinel
import pytest

from opend6_tools.character import (
    Character, Agility, Coordination, Physique,
    Intellect, Acumen, Charisma, Magic, OptionList, NoteList, D
)
from opend6_tools.character.workbook import *

@pytest.fixture
def mock_characters():
    cells = {
        f"character_{d}": Mock(
            spec=Character,
            sequence=d,
            realm=f"Realm {d % 3}",
        )
        for d in range(1, 11)
    }
    cells |= {
        f"other": Mock(spec=int, sequence=d)
        for d in range(11, 16)
    }
    # Can't set ``name`` in a Mock directly...
    for c in cells.values():
        c.name = f"Character {c.sequence}"
    return cells

def test_workbook_characters(mock_characters):
    subset = workbook_characters(mock_characters)
    assert len(subset) == 10

def test_workbook_groupby(mock_characters):
    groups = workbook_groupBy(mock_characters, lambda c: c.realm)
    assert len(groups) == 3
    assert set(groups.keys()) == {"Realm 0", "Realm 1", "Realm 2"}
    assert len(groups["Realm 0"]) == 3
    assert len(groups["Realm 1"]) == 4
    assert len(groups["Realm 2"]) == 3

@pytest.fixture
def sample_character():
    random.seed(42)
    return Character(name='Sample')

def test_workbook_display(sample_character):
    something = display(sample_character)
    assert something.splitlines() == [
         "{'name': 'Sample',",
         " 'occupation': '',",
         " 'race': '',",
         " 'gender': '',",
         " 'age': '',",
         " 'height': '',",
         " 'weight': '',",
         " 'physical_description': '',",
         " 'agility': Agility(3*D, {'acrobatics': 0*D, 'climbing': 0*D, "
     "'contortion': 0*D, 'dodge': 0*D, 'fighting': 0*D, 'flying': 0*D, "
     "'jumping': 0*D, 'melee combat': 0*D, 'combat': 0*D, 'riding': 0*D, "
     "'stealth': 0*D}),",
         " 'intellect': Intellect(3*D, {'cultures': 0*D, 'devices': 0*D, 'healing': "
     "0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, "
     "'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),",
         " 'coordination': Coordination(3*D, {'charioteering': 0*D, 'lockpicking': "
     "0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, "
     "'throwing': 0*D}),",
         " 'acumen': Acumen(3*D, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, "
     "'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, "
     "'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),",
         " 'physique': Physique(3*D, {'lifting': 0*D, 'running': 0*D, 'stamina': "
     "0*D, 'swimming': 0*D}),",
         " 'charisma': Charisma(3*D, {'animal handling': 0*D, 'bluff': 0*D, "
     "'charm': 0*D, 'command': 0*D, 'intimidation': 0*D, 'mettle': 0*D, "
     "'persuasion': 0*D}),",
         " 'extranormal': Magic(0*D, {'alteration': 0*D, 'apportation': 0*D, "
     "'conjuration': 0*D, 'divination': 0*D}),",
         " 'advantages': OptionList(),",
         " 'disadvantages': OptionList(),",
         " 'special_abilities': OptionList(),",
         " 'description': '',",
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
         " 'equipment': NoteList(),",
         " 'armor': NoteList(),",
         " 'weapons': NoteList(),",
         " 'spells': NoteList(),",
         " 'personality': '',",
         " 'objectives': '',",
         " 'native_language': '',",
         " 'other_notes': '',",
         " 'Check': {'Attributes': '18D out of 18D',",
         "           'Skills': 'Nothing out of 7D',",
         "           'Options': 'Nothing'}}",
    ]

def test_workbook_debug(sample_character, capsys):
    debug([sample_character], 'Sample')
    out, err = capsys.readouterr()
    assert out.splitlines() == [
         '## Sample',
         "{'name': 'Sample',",
         " 'occupation': '',",
         " 'race': '',",
         " 'gender': '',",
         " 'age': '',",
         " 'height': '',",
         " 'weight': '',",
         " 'physical_description': '',",
         " 'agility': Agility(3*D, {'acrobatics': 0*D, 'climbing': 0*D, "
     "'contortion': 0*D, 'dodge': 0*D, 'fighting': 0*D, 'flying': 0*D, "
     "'jumping': 0*D, 'melee combat': 0*D, 'combat': 0*D, 'riding': 0*D, "
     "'stealth': 0*D}),",
         " 'intellect': Intellect(3*D, {'cultures': 0*D, 'devices': 0*D, 'healing': "
     "0*D, 'navigation': 0*D, 'reading/writing': 0*D, 'scholar': 0*D, "
     "'speaking': 0*D, 'trading': 0*D, 'traps': 0*D}),",
         " 'coordination': Coordination(3*D, {'charioteering': 0*D, 'lockpicking': "
     "0*D, 'marksmanship': 0*D, 'pilotry': 0*D, 'sleight of hand': 0*D, "
     "'throwing': 0*D}),",
         " 'acumen': Acumen(3*D, {'artist': 0*D, 'crafting': 0*D, 'disguise': 0*D, "
     "'gambling': 0*D, 'hide': 0*D, 'investigation': 0*D, 'know-how': 0*D, "
     "'search': 0*D, 'streetwise': 0*D, 'survival': 0*D, 'tracking': 0*D}),",
         " 'physique': Physique(3*D, {'lifting': 0*D, 'running': 0*D, 'stamina': "
     "0*D, 'swimming': 0*D}),",
         " 'charisma': Charisma(3*D, {'animal handling': 0*D, 'bluff': 0*D, "
     "'charm': 0*D, 'command': 0*D, 'intimidation': 0*D, 'mettle': 0*D, "
     "'persuasion': 0*D}),",
         " 'extranormal': Magic(0*D, {'alteration': 0*D, 'apportation': 0*D, "
     "'conjuration': 0*D, 'divination': 0*D}),",
         " 'advantages': OptionList(),",
         " 'disadvantages': OptionList(),",
         " 'special_abilities': OptionList(),",
         " 'description': '',",
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
         " 'equipment': NoteList(),",
         " 'armor': NoteList(),",
         " 'weapons': NoteList(),",
         " 'spells': NoteList(),",
         " 'personality': '',",
         " 'objectives': '',",
         " 'native_language': '',",
         " 'other_notes': '',",
         " 'Check': {'Attributes': '18D out of 18D',",
         "           'Skills': 'Nothing out of 7D',",
         "           'Options': 'Nothing'}}",
         '',
    ]

def test_workbook_debug_dict_all(sample_character, capsys):
    debug({'Sample': sample_character})
    out, err = capsys.readouterr()
    assert out.splitlines()[0] == '## Sample'

def test_workbook_debug_dict_list(sample_character, capsys):
    debug({'Sample': sample_character}, ['Sample'])
    out, err = capsys.readouterr()
    assert out.splitlines()[0] == '## Sample'

