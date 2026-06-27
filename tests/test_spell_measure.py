"""
Test spell_measure app
"""

from typer.testing import CliRunner

from opend6_tools.spell_measure import app


runner = CliRunner()

def test_spell_measure():
    result = runner.invoke(app, )
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert len(out_lines) == 36
    assert out_lines[0] == 'Val.,Measure,Val.,Measure,Val.,Measure'
    assert out_lines[35] == '34,6.0 million,69,60.0 trillion,,'


def test_spell_measure_all_rows():
    result = runner.invoke(app, ["--rows", "200"] )
    assert result.exit_code == 0
    out_lines = result.output.splitlines()
    assert len(out_lines) == 102
    assert out_lines[0] == 'Value,Measure'
    assert out_lines[35] == '34,6.0 million'
