"""
Test die_simplification app
"""

from typer.testing import CliRunner

from opend6_tools.die_simplification import app

runner = CliRunner()

def test_die_simplification():
    result = runner.invoke(app, )
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert len(out_lines) == 51
    assert out_lines[0] == 'Die Code,5D,Wild Die'
    assert out_lines[50] == '50D,+158,+172'
