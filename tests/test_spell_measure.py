"""
Test spell_measure app
"""

import pytest

from opend6_tools import spell_measure

def test_spell_measure(capsys):
    spell_measure.main()
    out, err = capsys.readouterr()
    out_lines = out.splitlines()
    assert len(out_lines) == 36
    assert out_lines[0] == 'Val.,Measure,Val.,Measure,Val.,Measure'
    assert out_lines[35] == '34,6.0 million,69,60.0 trillion,,'
