"""
Test the notebook_extract app
"""
import importlib
import json
from pathlib import Path
from typing import Any

from  unittest.mock import Mock, call
import pytest
from typer.testing import CliRunner


from opend6_tools import notebook_extract
from opend6_tools import character

@pytest.fixture
def mock_ipynb_1() -> dict[str, Any]:
    return {
        'cells': [
            {
                'cell_type': 'code',
                'source': 'spell_var = Spell(name="spell name")',
            },
            {
                'cell_type': 'code',
                'source': 'assert some_spell.difficulty == 42',
            },
            {
                'cell_type': 'code',
                'source': 'pi = 355 / 113',
            },
            {
                'cell_type': 'code',
                'source': 'assert some_spell.difficulty > 0',
            },
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

    test_source = list(extractor.test_case_iter())
    assert len(test_source) == 1
    left, right = test_source[0]
    assert left == 'some_spell.difficulty'
    assert right == '42'

@pytest.fixture
def mock_spell_extract() -> dict[str, str]:
    return [
        ('r1_spell', 'r1_spell = Spell(name="rank 1", effect=GenericEffect("small", 10))'),
        ('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=GenericEffect("small", 20))'),
        ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=GenericEffect("small", 21))'),
    ]

@pytest.fixture
def mock_test_extract() -> dict[str, str]:
    return [
        ('r1_spell.difficulty', '10'),
        ('r2_spell_a.difficulty', '20'),
        ('r2_spell_b.difficulty', '21'),
    ]

def test_writer(mock_spell_extract):
    mw = notebook_extract.ModuleWriter()
    content = mw.write_book(
        book_type="spells",
        title="Test",
        definitions=mock_spell_extract,
        book_variable_name="spells"
    )
    assert mw.book_slug("Two Words") == "two_words"

    expected_version = importlib.metadata.version("opend6-tools")
    assert content.splitlines()[:3] == [
        '"""',
        'Extract Spells from ``Test``.',
        f'Created by V{expected_version} opend6-tools, ``opend6_tools.notebook_extract`` ',
    ]

def test_unranked(mock_spell_extract, mock_test_extract, capsys):
    mock_writer = Mock(write_book=Mock(return_value="Some Book"))
    notebook_extract.write_spells_unranked('spells', None, "test.ipynb", mock_spell_extract, mock_test_extract, mock_writer)
    mock_writer.write_book.assert_called_once_with(
        book_type='Spells',
        title='test.ipynb',
        definitions=[
            ('r1_spell', 'r1_spell = Spell(name="rank 1", effect=GenericEffect("small", 10))'),
            ('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=GenericEffect("small", 20))'),
            ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=GenericEffect("small", 21))')],
        book_variable_name='spells',
        tests={
            'r1_spell': '>>> r1_spell.difficulty\n10\n',
            'r2_spell_a': '>>> r2_spell_a.difficulty\n20\n',
            'r2_spell_b': '>>> r2_spell_b.difficulty\n21\n'
        }
    )
    out, err = capsys.readouterr()
    assert out.splitlines() == ['Some Book']

def test_unranked_files(mock_spell_extract, mock_test_extract, capsys, tmp_path):
    directory = tmp_path / "here"
    directory.mkdir()
    base = directory / "name"
    mock_writer = Mock(write_book=Mock(return_value="Some Book"))
    notebook_extract.write_spells_unranked('spells', base, "test.ipynb", mock_spell_extract, mock_test_extract, mock_writer)

    out, err = capsys.readouterr()
    assert out.splitlines() == []
    assert base.read_text() == "Some Book\n"


def test_ranked(mock_spell_extract, mock_test_extract, capsys):
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_spells_ranked('spells', None, "test.ipynb", mock_spell_extract, mock_test_extract, mock_writer)
    assert mock_writer.write_book.mock_calls == [
        call(
            book_type='Spells',
            title='test.ipynb rank 1 spells',
            definitions=[('r1_spell', 'r1_spell = Spell(name="rank 1", effect=GenericEffect("small", 10))')],
            book_variable_name='spells',
            tests={'r1_spell': '>>> -2 <= r1_spell.difficulty - 5 < +3\nTrue\n'}
        ),
        call(
            book_type='Spells',
            title='test.ipynb rank 2 spells',
            definitions=[('r2_spell_a', 'r2_spell_a = Spell(name="rank 2a", effect=GenericEffect("small", 20))'), ('r2_spell_b', 'r2_spell_b = Spell(name="rank 2b", effect=GenericEffect("small", 21))')],
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

def test_ranked_files(mock_spell_extract, mock_test_extract, capsys, tmp_path):
    directory = tmp_path / "here"
    directory.mkdir()
    base = directory / "name"
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_spells_ranked('spells', base, "test.ipynb", mock_spell_extract, mock_test_extract, mock_writer)

    out, err = capsys.readouterr()
    assert out.splitlines() == []
    assert (directory / "name_Rank1").read_text() == "Book 1\n"
    assert (directory / "name_Rank2").read_text() == "Book 2\n"


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

def test_write_characters_byrealm(mock_creature_extract, capsys):
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

def test_write_characters_byrealm_file(mock_creature_extract, capsys, tmp_path):
    directory = tmp_path / "here"
    directory.mkdir()
    path = directory / "base"
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_characters_byRealm('characters', path, "test.ipynb", mock_creature_extract, mock_writer)

    out, err = capsys.readouterr()
    assert out.splitlines() == [    ]
    assert (directory / "base_one").read_text() == 'Book 2\n'
    assert (directory / "base_two").read_text() == 'Book 1\n'

def test_write_characters(mock_creature_extract, capsys):
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_characters('characters', None,
                                              "test.ipynb",
                                              mock_creature_extract,
                                              mock_writer)
    assert mock_writer.write_book.mock_calls == [
        call(book_type='Characters', title='test.ipynb', definitions=[
            ('r1_creature',
             'r1_creature = Creature(name="creature", realm="one")'),
            ('r2_creature_a',
             'r2_creature_a = Creature(name="creature_a", realm="Two")'),
            ('r2_creature_b',
             'r2_creature_b = Creature(name="creature_b", realm="Two")')],
             book_variable_name='characters', tests={})    ]
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        'Book 1',
    ]

def test_write_characters_files(mock_creature_extract, capsys, tmp_path):
    directory = tmp_path / "here"
    directory.mkdir()
    path = directory / "document"
    mock_writer = Mock(write_book=Mock(side_effect=["Book 1", "Book 2"]))
    notebook_extract.write_characters('characters', path,
                                              "test.ipynb",
                                              mock_creature_extract,
                                              mock_writer)
    assert mock_writer.write_book.mock_calls == [
        call(book_type='Characters', title='test.ipynb', definitions=[
            ('r1_creature',
             'r1_creature = Creature(name="creature", realm="one")'),
            ('r2_creature_a',
             'r2_creature_a = Creature(name="creature_a", realm="Two")'),
            ('r2_creature_b',
             'r2_creature_b = Creature(name="creature_b", realm="Two")')],
             book_variable_name='characters', tests={})    ]
    out, err = capsys.readouterr()
    assert out.splitlines() == []
    assert path.read_text() == 'Book 1\n'


def test_slug():
    assert notebook_extract.slug("Big Name") == "bigname"


def test_cli_spells(tmp_path):
    file = tmp_path / "test.ipynb"
    file.write_text('{"cells": {}}')
    runner = CliRunner()
    result = runner.invoke(notebook_extract.app, ["spells", str(file)])
    assert result.exit_code == 0
    output = result.output.splitlines()
    assert output[1] == "Extract Spells from ``test.ipynb``."

def test_cli_spells_ranked_verbose(tmp_path, caplog):
    file = tmp_path / "test.ipynb"
    file.write_text('{"cells": {}}')
    runner = CliRunner()
    result = runner.invoke(notebook_extract.app, ["spells", str(file), "--ranked", "--verbose"])
    assert result.exit_code == 0
    assert result.output == ""
    assert caplog.messages == [
        f"source {file!r}, output None, book_variable 'spells', ranked True",
        f"Extractor {file!s}: 0 code cell analyzers",
        "Wrote 0 spells",
    ]

def test_cli_characters(tmp_path):
    file = tmp_path / "test.ipynb"
    file.write_text('{"cells": {}}')
    runner = CliRunner()
    result = runner.invoke(notebook_extract.app, ["characters", str(file)])
    assert result.exit_code == 0
    output = result.output.splitlines()
    assert output[1] == "Extract Characters from ``test.ipynb``."

def test_cli_characters_grouped_verbose(tmp_path, caplog):
    file = tmp_path / "test.ipynb"
    file.write_text('{"cells": {}}')
    runner = CliRunner()
    result = runner.invoke(notebook_extract.app, ["characters", str(file), "--groupby", "realm", "--verbose"])
    assert result.exit_code == 0
    assert result.output == ""
    assert caplog.messages == [
        f"source {file!r}, output None, book_variable 'characters', groupby 'realm'",
        f"Extractor {file!s}: 0 code cell analyzers",
        "Wrote 0 characters",
    ]
