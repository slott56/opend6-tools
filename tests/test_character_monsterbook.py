"""
Test character.monsterbook
"""
import random
from textwrap import dedent
import pytest

from opend6_tools.character.monsterbook import *
from opend6_tools.character.features import *

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

@pytest.fixture
def mock_creature_list(sample_creature, complex_creature):
    return [sample_creature, complex_creature]

def test_build_app_help(mock_creature_list, capsys):
    app = build_app(mock_creature_list, rich_markup_mode=None)
    app(["--help"], standalone_mode=False)
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        'Usage: python -m pytest [OPTIONS] COMMAND [ARGS]...',
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
        '  display  Write details of all Character or Creature definitions.',
        '  debug    Print debugging information for a specific definition to STDOUT',
        '  test     Run the doctest examples, using the __test__ global.',
        '  blank    Print a blank character sheet in the desired format.',
        '  pdf      Create a PDF character sheet.',
    ]


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

def test_build_app_display(sample_character, capsys):
    app = build_app(sample_character, rich_markup_mode=None)
    app(["display", "--format", "PLAYER"], standalone_mode=False)
    out, err = capsys.readouterr()
    expected = Path.cwd() / "tests" / "character2.html"
    assert out == expected.read_text() + "\n"


def test_build_app_pdf(sample_character, capsys, tmp_path, monkeypatch):
    """
    Requires docutils and xhtml2pdf both installed.
    """
    working_dir = tmp_path / "working"
    working_dir.mkdir()
    monkeypatch.chdir(working_dir)
    app = build_app({'Unnamed': sample_character}, rich_markup_mode=None)
    app(["pdf", "--format", "TABLE", "Unnamed"], standalone_mode=False)
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        f"Creating {Path.cwd()!s}/Unnamed.rst",
        f"rst2html {Path.cwd()!s}/Unnamed.rst {Path.cwd()!s}/Unnamed.html",
        f"xhtml2pdf {Path.cwd()!s}/Unnamed.html {Path.cwd()!s}/Unnamed.pdf",
    ]
    assert err == ""


def test_make_doctest(sample_character, capsys):
    make_character_doctest({'Sample': sample_character})
    out, err = capsys.readouterr()
    assert out.splitlines() == [
        '__test__ = {',
        '    "": ">>> '
        "characters[0].budget_check(CharacterBudget.NO_BUDGET)\\n{'Attributes': "
        "'{budget.attributes} out of {budget.attributes}', 'Skills': "
        "'{budget.skills} out of {budget.skills}', 'Options': '{budget.options} "
        'out of {budget.options}\'}",',
        '}',
    ]
