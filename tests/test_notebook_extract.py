"""
Test the notebook_extract app
"""
import json
from pathlib import Path
from typing import Any

from  unittest.mock import Mock, call
import pytest

from opend6_tools import notebook_extract
from opend6_tools import magic2
from opend6_tools import character

@pytest.fixture
def mock_ipynb_1() -> dict[str, Any]:
    return {
        'cells': [
            {
                'cell_type': 'code',
                'source': 'spell_var = Spell(name="spell name")',
            }
        ]
    }

@pytest.fixture
def mock_notebook_1(tmp_path, mock_ipynb_1) -> Path:
    path = tmp_path / "sample1.ipynb"
    path.write_text(json.dumps(mock_ipynb_1))
    return path

def test_extractor(mock_notebook_1):
    extractor = notebook_extract.Extractor(mock_notebook_1)
    spell_source = list(extractor.definition_iter())
    assert len(spell_source) == 1
    target, code = spell_source[0]
    assert target == 'spell_var'
    assert code == 'spell_var = Spell(name="spell name")'

@pytest.fixture
def mock_spell_extract() -> dict[str, str]:
    return [
        ('r1_spell', 'r1_spell = Spell(name="rank 1", effect=Effect("small", 10))'),
        ('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=Effect("small", 20))'),
        ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=Effect("small", 21))'),
    ]


def test_unranked(mock_spell_extract, capsys):
    mock_writer = Mock(write_book=Mock(return_value="Some Book"))
    notebook_extract.write_spells_unranked('spells', None, "test.ipynb", mock_spell_extract, mock_writer)
    mock_writer.write_book.assert_called_once_with(
        book_type='Spells',
        title='test.ipynb',
        definitions=[
            ('r1_spell', 'r1_spell = Spell(name="rank 1", effect=Effect("small", 10))'),
            ('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=Effect("small", 20))'),
            ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=Effect("small", 21))')],
        book_variable_name='spells',
        tests={}
    )
    out, err = capsys.readouterr()
    assert out.splitlines() == ['Some Book']


def test_ranked(mock_spell_extract, capsys):
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_spells_ranked('spells', None, "test.ipynb", mock_spell_extract, mock_writer)
    assert mock_writer.write_book.mock_calls == [
        call(
            book_type='Spells',
            title='test.ipynb rank 1 spells',
            definitions=[('r1_spell', 'r1_spell = Spell(name="rank 1", effect=Effect("small", 10))')],
            book_variable_name='spells',
            tests={'r1_spell': '>>> -2 <= r1_spell.difficulty - 5 < +3\nTrue\n'}
        ),
        call(
            book_type='Spells',
            title='test.ipynb rank 2 spells',
            definitions=[('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=Effect("small", 20))'), ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=Effect("small", 21))')],
            book_variable_name='spells',
            tests={'r2_spell_a': '>>> -2 <= r2_spell_a.difficulty - 10 < +3\nTrue\n', 'r2_spell_b': '>>> -2 <= r2_spell_b.difficulty - 10 < +3\nTrue\n'}
        ),
    ]
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        '# RANK 1',
        '',
        'Book 1',
        '',
        '# RANK 2',
        '',
        'Book 2',
        '',
    ]

@pytest.fixture
def mock_ipynb_2() -> dict[str, Any]:
    return {
        'cells': [
            {
                'cell_type': 'code',
                'source': 'creature_var = Creature(name="creature name")',
            },
            {
                'cell_type': 'code',
                'source': 'character_var = Character(name="character name")',
            },
        ]
    }

@pytest.fixture
def mock_notebook_2(tmp_path, mock_ipynb_2) -> Path:
    path = tmp_path / "sample2.ipynb"
    path.write_text(json.dumps(mock_ipynb_2))
    return path

def test_character_extractor(mock_notebook_2):
    extractor = notebook_extract.Extractor(mock_notebook_2, target_type=character.Character)
    spell_source = list(extractor.definition_iter())
    assert len(spell_source) == 2
    assert spell_source[0] == ('creature_var', 'creature_var = Creature(name="creature name")')
    assert spell_source[1] == ('character_var', 'character_var = Character(name="character name")')

@pytest.fixture
def mock_creature_extract() -> dict[str, str]:
    return [
        ('r1_creature', 'r1_creature = Creature(name="creature", realm="one")'),
        ('r2_creature_a', 'r2_creature_a = Creature(name="creature_a", realm="Two")'),
        ('r2_creature_b', 'r2_creature_b = Creature(name="creature_b", realm="Two")'),
    ]

def test_grouped(mock_creature_extract, capsys):
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_characters_byRealm('characters', None, "test.ipynb", mock_creature_extract, mock_writer)
    assert mock_writer.write_book.mock_calls == [
        call(
            book_type='Characters',
            title='test.ipynb realm Two characters',
            definitions=[('r2_creature_a',
                           'r2_creature_a = Creature(name="creature_a", realm="Two")'),
                          ('r2_creature_b',
                           'r2_creature_b = Creature(name="creature_b", realm="Two")')],
            book_variable_name='characters'
            ),
        call(book_type='Characters',
             title='test.ipynb realm one characters',
             definitions=[('r1_creature',
                           'r1_creature = Creature(name="creature", realm="one")')],
             book_variable_name='characters'
             ),
    ]
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        '# REALM Two',
        '',
        'Book 1',
        '',
        '# REALM one',
        '',
        'Book 2',
        '',
    ]
