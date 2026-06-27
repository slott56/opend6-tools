"""
More tests for magic.dice
"""
from unittest.mock import patch, Mock

import pytest
from typer.testing import CliRunner

from opend6_tools.dice import *

def test_dice_DSL():
    d_3_2 = 3 * D + 2
    assert d_3_2.measure == 11
    assert str(d_3_2) == '3D+2'

def test_dice_str():
    d_3_2 = DieCode.parse_str("3D+2")
    assert d_3_2.measure == 11
    assert str(d_3_2) == '3D+2'

def test_dice_str_bad():
    with pytest.raises(ValueError):
        d_3_2 = DieCode.parse_str("What?")

def test_dice_str_pips_only():
    d_0_2 = DieCode.parse_str("+2")
    assert d_0_2.measure == 2
    assert str(d_0_2) == '+2'

def test_dice_math():
    d_2 = 2 * D
    assert d_2 + 2 == 2 * D + 2
    assert d_2 - 2 == 1 * D + 1
    assert d_2 == 6
