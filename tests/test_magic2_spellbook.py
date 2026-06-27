"""Test magic.spellbook module.
"""
from unittest.mock import Mock, MagicMock, patch
import pytest
from typer.testing import CliRunner


import opend6_tools.magic.spellbook
from opend6_tools.magic.spellbook import *


@pytest.fixture
def example_spell_no_difficulty():
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

@pytest.fixture
def example_book(example_spell_no_difficulty):
    return [example_spell_no_difficulty,]

def test_make_spell_doctest(example_book, capsys):
    make_spell_doctest(example_book)
    out, err = capsys.readouterr()
    out_lines = out.splitlines()
    assert out_lines[0] == "__test__ = {"
    assert out_lines[-1] == "}"

def test_build_app(example_book):
    runner = CliRunner()
    app = build_app(example_book, rich_markup_mode=None)

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines == [
        'Usage: root [OPTIONS] COMMAND [ARGS]...',
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
        '  test     Run the doctest examples, using the __test__ global.'
    ]

def test_cli_debug(example_book):
    runner = CliRunner()
    app = build_app(example_book, rich_markup_mode=None)

    result = runner.invoke(app,["debug", "Example"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines == [
        '## Example',
        "  name                : 'Example'",
        "  notes               : 'GIVEN Example spell WHEN difficulty THEN 4'",
        "  skill               : 'Acumen: testing'",
        "  effect              : +12 SkillEffect('Acumen: testing', '+4D')",
        "  duration            :  +0 DurationAspect('1 sec')",
        "  range               :  +0 RangeAspect('1m')",
        "  casting_time        :  -4 CastingTimeAspect('5 sec')",
        "  speed               :  +0 SpeedAspect.based_on('range', *(), **{'description': 'Instantaneous'})",
        '  other_conditions    :',
        "  - Everything [...]  :  -1 GenericAspect(1, 'Everything else is completed')",
        "Effect Details        : SkillEffect based on DiceUnit [Modifier(difficulty=Decimal('12'), description='4*D')]",
        "Spell Total           : {'effect': 12, 'duration': 0, 'range': 0, 'speed': 0} = 12",
        "Negative Modifiers    : {'casting_time': 4, 'condition: Everything else is [...]': 1} = 5",
        'Difficulty            : ⎡(12 - 5) ÷ 2⎤ = 4',
        '',
        '',
    ]

def test_cli_display(example_book):
    runner = CliRunner()
    app = build_app(example_book, rich_markup_mode=None)

    result = runner.invoke(app,["display", "Example"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines == [
        'Example',
        '~~~~~~~',
        '',
        ':Skill: Acumen: testing',
        ':Difficulty: 4 ',
        ':Effect: 12 (Acumen: testing 4*D)',
        ':Range: 1 m \\(0)',
        ':Speed:  \\(0)',
        ':Duration: 1 sec \\(0)',
        ':Casting Time: 5 sec \\(4)',
        '',
        '',
        ':Other Conditions:',
        '    (1): Everything else is completed',
        '',
        '',
        '',
        '',
        'GIVEN Example spell WHEN difficulty THEN 4',
        '',
    ]

def test_cli_display_all(example_book):
    runner = CliRunner()
    app = build_app(example_book, rich_markup_mode=None)

    result = runner.invoke(app,["display"])
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[1] == 'Example'


@pytest.mark.skip(reason="very hard to test from within pytest")
def test_cli_test(example_book):
    """
    This doesn't quite work because the target function
    designed to be run from the CLI, not from within pytest.
    We can't easily patch ``sys``.

    This needs to be run as a subprocess.
    """
    runner = CliRunner()
    with patch.object(opend6_tools.magic.spellbook.sys, 'modules', {'__main__': MagicMock(__test__=True)}):
        with patch('opend6_tools.magic.spellbook.doctest', Mock(testmod=Mock(return_value=(0, 0)))):
            app = build_app(example_book, rich_markup_mode=None)

    result = runner.invoke(app,["test"])
    print(result.output)
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert out_lines[1] == 'Example'
