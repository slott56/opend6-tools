"""
Test die_simplification app
"""

import pytest

from opend6_tools import die_simplification

def test_die_simplification(capsys):
    die_simplification.main()
    out, err = capsys.readouterr()
    out_lines = out.splitlines()
    assert len(out_lines) == 51
    assert out_lines[0] == 'Die Code,5D,Wild Die'
    assert out_lines[50] == '50D,+158,+172'
