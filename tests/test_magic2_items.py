"""
Tests for the ``magic.spells`` module, focused on Items.
"""
import pytest

from opend6_tools.magic.spells import *

@pytest.fixture
def example_item():
    amulet_protection = Item(
        name = "Amulet of Protection",
        notes = "An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura",
        effect = SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, "non-enchanted weapons",
            modifications=[Limitation(LimitationType.burn_out, 1, "can be lost or stolen")]
        ),
        type="Jewelry",
        price="H (200 G)"
    )
    return amulet_protection

# @pytest.mark.skip("not implemented, yet.")
def test_item(example_item):
    assert example_item.difficulty == 2
    assert example_item.notes.startswith('An oddly-shaped')
    assert example_item.source() == (
        "Item(name='Amulet of Protection', effect=SpecialAbilityEffect(SpecialAbilityType.attack_resistance, 1, 'non-enchanted weapons', modifications=[Limitation(LimitationType.burn_out, 1, 'can be lost or stolen')]), notes='An oddly-shaped pendant on a thick leather cord envelopes the wearer in a defensive aura')"
    )
