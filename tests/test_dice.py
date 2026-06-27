"""
Test the Dice module.
"""
from typer.testing import CliRunner

from opend6_tools.dice import dice_app


def test_dice_cli():
    runner = CliRunner()
    result = runner.invoke(dice_app, ["3*D+2", "--count=3"], env={"OPEND6_SEED": "42"})
    assert result.exit_code == 0
    assert result.output == "19!\n4? (5)\n13\n"
