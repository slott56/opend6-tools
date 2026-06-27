"""
Tests for the ``character.output`` module.
"""
from pathlib import Path
import random
from textwrap import dedent

from typer.testing import CliRunner
import pytest

from opend6_tools.character import *

def test_Writer_static():
    assert CharacterWriter.pad("xyz", 5) == "xyz  "
    assert CharacterWriter.pad("xyzabc", 5) == "xyzab"

    assert CharacterWriter.lpad("xyz", 5) == "  xyz"
    assert CharacterWriter.lpad("xyzabc", 5) == "xyzab"

    assert CharacterWriter.line(["1", "2"], 0, width=1) == "1"
    assert CharacterWriter.line(["1", "2"], 1, width=2) == "2"
    assert CharacterWriter.line(["1", "2"], 2, width=3) == "   "

    assert CharacterWriter.if_none(None, "***") == "***"
    assert CharacterWriter.if_none("", "***") == "***"
    assert CharacterWriter.if_none("42", "***") == "42"


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


@pytest.fixture
def another_character():
    random.seed(42)  # Forces a wild die result
    healer = Character(
        name="Long***Name",
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

def test_CharacterWriter(sample_character):
    """Publication details, long form."""
    assert sample_character.strength_damage == 2*D
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
        ':Body Points: 28',
    ]


def test_CharacterWriter_Short(sample_character, another_character):
    """Publication details, short form."""
    characters = {c.occupation: c for c in (sample_character, another_character)}
    w = CharacterWriter_Short()
    text = w.report(characters)
    assert text.splitlines() == [
        '**Aspiring Hero**:',
        'Agility 3D+1, Coordination 2D+2, Physique 3D, Intellect 2D+2, Acumen 3D+1, Charisma 3D.',
        '*Move*: 10, ',
        '*Strength Damage*: 2D, ',
        '*Fate Points*: 1, ',
        '*Character Points*: 5, ',
        '*Body Points*: 28, *Equipment*: leather jerkin (Armor Value +2); Dagger '
        '(damage +1D); shoulder bag with cheese, bread, and silver coins in it, '
        '*Description*: Always fascinated by the traveling sword-showmen that came through',
        'your little village, you practiced mimicking their techniques (in between your chores',
        '- and sometimes as part of them). Perhaps inheriting wanderlust from your uncle, you',
        'have set on to find your fortune in the larger world and maybe gain fame by helping a few',
        'people along the way.',
        '',
        '',
        '**Healer**:',
        'Agility 2D, Coordination 2D, sleight of hand 2D+1, Physique 2D, stamina '
        '2D+1, Intellect 3D, healing 4D, reading/writing 2D+1, scholar 2D+2, Acumen '
        '3D+1, investigation 2D+1, Charisma 2D.',
        '*Move*: 10, ',
        '*Strength Damage*: 1D, ',
        '*Fate Points*: 0, ',
        '*Character Points*: 2, ',
        "*Body Points*: 10, *Equipment*: large healer's kit (+1 bonus to 6 to 12 healing attempts).",
        '',
        '',
    ]


def test_CharacterWriter_Table(sample_character):
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
        '| fighting                     | scholar                      | jerkin (Armor Value          |',
        '|                              |                              |                              |',
        '| flying                       | speaking                     | +2); shoulder bag with       |',
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
        '| alteration                   | Str Damage                2D | Body Points 28               |',
        '|                              |                              |                              |',
        '| apportation                  | Move                      10 | [ ] Stunned   17-21          |',
        '|                              |                              |                              |',
        '| conjuration                  | Fate Pts      1              | [ ] Wounded   11-16          |',
        '|                              |                              |                              |',
        '| divination                   | Character Pts 5              | [ ] Severe    6-10           |',
        '|                              |                              |                              |',
        "|                              | Funds 3D                     | [ ] Incapac'd 3-5            |",
        '|                              |                              |                              |',
        '|                              | Silver 180                   | [ ] Mortal    1-2            |',
        '|                              |                              |                              |',
        '|                              |                              | [ ] Dead                     |',
        '+------------------------------+------------------------------+------------------------------+',
    ]


def test_CharacterWriter_HTML1(sample_character, tmp_path):
    """Player's Character Sheet -- HTML Content, suitable for conversion to PDF."""
    name = "character1.html"
    w = CharacterWriter_HTML1()
    destination = tmp_path / name
    text = w.report(sample_character)
    destination.write_text(text)
    print(f"file://{destination}")
    expected = Path.cwd() / "tests" / name
    assert destination.read_text() == expected.read_text()

def test_CharacterWriter_HTML2(sample_character, tmp_path):
    """Player's Character Sheet -- HTML Content, suitable for conversion to PDF."""
    name = "character2.html"
    w = CharacterWriter_HTML2()
    destination = tmp_path / name
    text = w.report(sample_character)
    destination.write_text(text)
    print(f"file://{destination}")
    expected = Path.cwd() / "tests" / name
    assert destination.read_text() == expected.read_text()

def test_CharacterWriter_LaTeX(sample_character, tmp_path):
    """Player's Character Sheet -- LaTeX Content, suitable for conversion to PDF."""
    name = "character2.tex"
    w = CharacterWriter_LaTeX()
    destination = tmp_path / name
    text = w.report(sample_character)
    destination.write_text(text)
    print(f"pdflatex {destination}")
    expected = Path.cwd() / "tests" / name
    assert destination.read_text() == expected.read_text()

@pytest.fixture
def character_dict(sample_character, another_character):
    book = {'Sample': sample_character, 'Long***Name': another_character}
    return book

@pytest.fixture
def character_list(sample_character, another_character):
    book = [sample_character, another_character]
    return book

@pytest.fixture
def character_app(character_dict):
    app = build_app(character_dict)
    return app

def test_app_display(character_app):
    runner = CliRunner()
    result = runner.invoke(character_app, ["display"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[1] == '**OpenD6 Fantasy**'

def test_app_debug(character_app):
    runner = CliRunner()
    result = runner.invoke(character_app, ["debug", "Sample"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[:3] == [
        '## ',
        "{'name': '',",
        " 'occupation': 'Aspiring Hero',",
    ]


@pytest.mark.skip(reason="very hard to test from within pytest")
def test_app_test(character_app):
    """
    This doesn't quite work because the target function
    designed to be run from the CLI, not from within pytest.
    We can't easily patch ``sys``.

    This needs to be run as a subprocess.
    """
    runner = CliRunner()
    result = runner.invoke(character_app, ["test"], )
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[:3] == [
        '## ',
        "{'name': '',",
        " 'occupation': 'Aspiring Hero',",
    ]

def test_app_blank(character_app):
    runner = CliRunner()
    result = runner.invoke(character_app, ["blank"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[15] == '<h1>OpenD6 Fantasy</h1>'

def test_app_pdf(character_app, tmp_path, monkeypatch):
    runner = CliRunner()
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(character_app, ["pdf", "--format=LATEX", "Long***Name"])
    assert result.exit_code == 0
    assert result.output.splitlines() == [
        f"Creating {tmp_path}/Long_Name.tex",
        f"pdflatex {tmp_path}/Long_Name.tex",
    ]
    output = tmp_path / "Long_Name.pdf"
    assert output.exists()


def test_app_pdf_list(character_list, tmp_path, monkeypatch):
    runner = CliRunner()
    monkeypatch.chdir(tmp_path)
    character_app = build_app(character_list)
    result = runner.invoke(character_app, ["pdf", "--format=PLAYER", "Long***Name"])
    assert result.exit_code == 0
    assert result.output.splitlines() == [
        f"Creating {tmp_path}/Long_Name.html",
        f"xhtml2pdf {tmp_path}/Long_Name.html {tmp_path}/Long_Name.pdf",
    ]
    output = tmp_path / "Long_Name.pdf"
    assert output.exists()


def test_app_pdf_single(another_character, tmp_path, monkeypatch):
    runner = CliRunner()
    monkeypatch.chdir(tmp_path)
    character_app = build_app(another_character)
    result = runner.invoke(character_app, ["pdf", "--format=TABLE", "Long***Name"])
    assert result.exit_code == 0
    assert result.output.splitlines() == [
        f"Creating {tmp_path}/Long_Name.rst",
        f"rst2html {tmp_path}/Long_Name.rst {tmp_path}/Long_Name.html",
        f"xhtml2pdf {tmp_path}/Long_Name.html {tmp_path}/Long_Name.pdf",
    ]
    output = tmp_path / "Long_Name.pdf"
    assert output.exists()
