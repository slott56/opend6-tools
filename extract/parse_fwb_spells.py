"""Spells from Fantasy Wargaming Book"""

from collections import Counter
import csv
from dataclasses import dataclass, field
from io import StringIO
from typing import ClassVar, Self

from humre import *
import magic1 as magic

# WW = Wise Woman, CM = Cunning Man classes of mage
# BMC = Basic Magic Calculation
# DD = Degree of Difficulty
FW_BOOK_SOURCE = r"""\
Name of spell, Effects, Maximum duration, Astrological Controllers, Diminishers, DD Witch, WW/CM, Wizard, High Sorcerer, Cabalist, Notes
# Page 206
Flight, "Air movement of self, other creature or object: twice normal ground speed", "1 turn (20 mins)", 'Pisces Sagittarius", "Virgo Capricorn", 3, 6, 5, 4, 3, "DD + 1 for object" 
Levitation, "Vertical ascent and floating: up to S0 ft, controllable at will. Soft descent guaranteed.", "10 mins", Aquarius Virgo, Libra Capricorn, 4, 6, 5, 4, 3, ""
Lethargic/rapid mvoement, "Halves/doubles speed of movement on ground or in water", "1-6 turns (dice)", "Virgo/Pisces", "Pisces/Virgo", 2, 4, 3, 3, 2, ""
Teleportation, "istantaneous transporatation through Ethereal plane: destination must be known.", "Instantaneous", "Aquarius Pisces", "Cancer Leo", 7, 9, 7, 6, 5, "Can also be used to teleport objects and persons from a known, distant location to the Mage; +4 DD" 
Giant leap, "Increases bounding power to 1 yard per physique point.", "1 leap", "Leo", "Scorpio", 2, 3, 3, 2, 2, "Targets: human only"
Climbing, "Subject of spell obtains physique and agility of 20 during his climb.", "1 turn",  "Leo Capricon", "Scorpio Libra", 4, 6, 4, 4, 3, "Range: 30 ft."
Invisibility, "(a) Personal invisibility (can still be heard or touched); (b) Invisibility for all persons, objects in a 10 ft cube area.", "1 turn", "Gemini Pisces", "Taurus Capricorn", 3, 5, 4, 4, 3, "Area = +4 on DD (and ignore multiple target section of BMC(3))."
Absolute darkness, "Unnatural darkness, oppressive (-1 on morale throws). Will snuff out natural sources of light.",  "1 turn", "Gemini Aquarius", "Leo Cancer", 3\*, 4\*, 3\*, 3\*, 2\*,  "\* Darkness covers 10 ft cube. Increase DD by 1 for each doubling in size. Penetrated by fire spells or by \"Light.\""
# Page 207
Night vision, "Subject can see through any natural darkness as if fully lit. Range: natural horizon.", "1-6 turns (dice)", "Cancer Leo", "Pisces Aquarius", 2, 2, 2, 2, 1, "Does not penetrate Absolute Darkness-see \"Light\""
Telescopic Vision, "Subject can zero in on distant events, as if happening 10 ft away. Range: natural horizon.", "1-6 turns (dice)", "Sagittarius Aquarius", "Gemini Pisces", 3, 4, 3, 2, 1
Through vision, "Subject can see through up to 3 layers of solid matter, in perfect clarity.", "10 mins", "Taurus Sagittarius", "Aries Capricorn", 4, 5, 4, 4, 3
Ethereal vision, "Subject can observe spirits, etc, on Ethereal plane or spy on events anywhere in the Earthly plane.", "5 mins", "Pisces Libra", "Cancer Aries", 5, 7, 6, 5\*, 4, "\* DD6 for Runic Sorcerers." 
Telepathic communication, "Subject can 'talk' to another's mind (living creatures only) or listen in unobserved.", "1 turn", "Gemini Aries", "Scorpio Capricorn", 4, 6, 5, 4, 3, "+2 DD with animals, monsters, spirits. There is a 'natural' telepathy between witch and familiar, needing no spell."
Animal speech, "Subject understands speech of any living creature, and can converse in it. Language forgotten afterwards.", "1 turn", "Gemini Virgo", "Leo Aries", 3, 3, 4, 3, 2
Gift of tongues, "Subject can read/write any unknown language or script. Forgotten afterwards.", "1-6 turns (dice)", "Gemini Virgo", "Aquarius Pisces", 4, 6, 5, 3, 2 
Silence, "Artificial silence in a 10 ft cube, smothering all natural noises. Cube moves with subject of spell.", "1 turn", "Capricorn Scorpio", "Virgo Libra", 2, 3, 3, 2, 2
# Page 208
Bolt of lightning, "Visible lightning streak from above Mage's head directed at target by arms. 3-18 (3 6-dice), damage points inflicted.", "Immediate", "Leo Aries", "Libra Sagittarius", 4, 6, 5, , 3
Gentle nudge, "Invisible push (up to physique 6) on an object, person etc. No gesture by Mage.", "Immediate", "Sagittarius Pisces", "Libra Capricorn", 2, 3, 2, 2, 1
Bolt of force, "Invisible bolt of force by Mage (no gesture). 4-24 (4 6-dice) damage.", "Immediate", "Aquarius Virgo", "Leo Sagittarius", 5, 8, 7, 5, 4
Weapon-wield, "Increases *or* decreases agility needed to wield a particular weapon. Targeted at weapon only.", "1-6 turns (dice)", "Aries Scorpio/Libra Sagittarius", "Sagittarius Libra/Aries Scorpio", 1\*, 3\*, 2\*, 1\*, 1\*, "\* + number of points difference to be made in agility needed. Runic Sorcerers start from base DD0"
Weapon-power, "Likewise, strength needed.", "1-6 turns (dice)", "Aries Scorpio/Libra Sagittarius", "Sagittarius Libra/Aries Scorpio", 1\*, 3\*, 2\*, 1\*, 1\*, "\*+ number of points difference to be made in strength needed. Runic Sorcerers start from base DDO."
Armor strength, "Increases or decreases protection of a shield, helm, suit of armor", "1-6 turns (dice)",  "Sagittarius Aries/Scorpio Capricorn", "Capricorn Scorpio/Sagittarius Aries", 1\*, 3\*, 2\*, 1\*, 1\*, "\*+ number of extra (or lower!) protection points. Altering shield, armor and helm is an extra +2. Runic Sorcerers start from base DDO."
# Page 209
Open/lock door, "Will open any locked door, lock any open one.", 1-6 turns  (dice), Aquarius Libra/Scorpio Leo, Pisces Leo/Aquarius Libra, 2, 2, 2, 2, 1, "Mage stores mana in the door, to 'lock' it. Mana fades at 1 point per turn. Door can be opened magically by another Mage, spending extra mana on an open spell to surpass that in door."
Create poison, "Poisons liquid, food, vegetable or animal matter:poison removes 2 EP at once, then 1 EP per hour." "Immediate (poison is indefinite)", "Scorpio Capricorn", "Taurus Cancer", 4, 3, 5, 4, 3, "+3 DD for an 'instant-death' poison."
Purify food and water, "Removes all poison, germs, etc, from food and water.", "Immediate", "Taurus Virgo", "Scorpio Capricorn", 4, 2, 4, 3, 2, "+2 DD to remove 'instant-death' poison."
Earthquake, "Will collapse stone/timber buildings, forests, shake caverns, ctc. Shaking itself causes 1-2 EP loss.", "Immediate", "Earth signs", "Water signs", 7, 9, 8, 7, 6, "GM must check effects of falling masonry, cic, on party."
Psychic disruption, "Reduces intelligence and other personality factors (not class) of target to 3.", "Immediate", "Aquarius Capricorn",  "Cancer", 4, 6, 6, 5\*, 4, "Target recovers at 1 point on all factors per hour. \* DD6 for a Runic Sorcerer."
Water breathing, "Target can breathe and operate happily under water.", "1-6 turns (dice)", "Pisces Салсеr", "Virgo Capricorn", 5, 4, 5, 4\*, 3, "\* DD3 for a Runic (Dark Age) Sorcerer."
Soft landing, "Ensures damage-free landing from any height/at any speed.", "Immediate", "Leo Gemini", "Aries Capricorn", 4, 6, 5, 4, 3, "Likewise"
Suspended animation, "Target is dead to all appearances but conscious, alert and in command of his senses.", "Up to 1 day", "Sagittarius Capricorn", "Taurus Cancer", 5, 3, 5, 4, 3
# Page 210
'Stoppage of Time', "Stops time (and all movement, action etc) within a 20 it cubic arca about Mage. Affects others entering area.", "1 turn", "Aquarius Virgo", "Leo Capricorn", 7, 8, 7, 6\*, 6, "\* DD7 for a Runic (Dark Age) Sorcerer."
Destruction of magic, "Dispels any spell currently in operation within a 30 ft cubic arca about Mage.", Immediate, "Cancer Aries", "Aquarius Pisces", \*, +1\*, \*, \*, -1\*, "\*DD equal to that of spell they are trying to dispel -- except as marked in columns."
Shape changing, "Target can assume any animate or inanimate form. Mental attributes remain the same, personality and physical attributes alter.", "Up to 1 day", "Aquarius Pisces", "Taurus Cancer", 7, 9, 7, 7\*, 6, "+ SDD il object/creature turned into has + 25% mass of target. \* But DD4 for Dark Age Runic Sorcerers."
Light, "A cold light, moveable at will of Mage, the size of a tennis ball: lights a 10 ft cube magically.",  "1-6 turns (dice)", "Cancer Taurus", "Leo Capricorn", 2, 2, 2, 2, 1, "+2 for an area or wall of light will break a spell of Absolute Darkness."
Pain, "No EP loss, just pain: take  bravery from 20 and equal/throw over with a six-dice t0 avoid surrender\*",  "1-3 turns (6-dice ÷ 2)", "Scorpio Pisces", "Taurus Libra", 3, 3, 5, 4, 3, "\* Surrendering means curling up (no action possible), begging for relief. Relief at Mage's will. Resistors: -3 in calculations." 
Evil eye, "1 EP loss. -1 on all luck throws.", "1 month", "Scorpio Cancer", "Sagittarius Leo", 2, 3, 4, 4, 4, "Can be removed by removal spell (same DDs) or by scratching the Mage to draw blood."
"""


@dataclass
class FWBSpell:
    """
    A Fantasy Wargaming Book spell summary.
    """

    spell_name: str  # keep this.
    description: str
    duration: str
    astro_control: str
    astro_diminish: str
    dd_witch: str
    dd_ww_CM: str
    dd_wizard: str
    dd_high_sorcerer: str
    dd_cabalist: str
    notes: str = ""

    @classmethod
    def from_csv(cls, row: list[str]) -> Self:
        try:
            return cls(*row)
        except TypeError:
            print(row)
            raise

    def diety(self) -> str:
        """Controller is usually one of the correspondencies."""
        CONTROLLER_MAP = {
            "aister": "Hildeþrymm Physique",
            "inat": "Cyþan Intelligence",
            "wissa": "Witan Acumen",
            "conna": "Hælan Coordination",
            "iudax": "Folme Agility",
            "ercha": "Baelu Charisma",
            "ercha/iudax": "Agility",
        }
        if self.controller in CONTROLLER_MAP:
            return CONTROLLER_MAP[self.controller]
        else:
            return self.controller

    def skill_used(self) -> str:
        TYPE_MAP = {
            "elemental": "Alteration",
            "abs. command": "Psychic Communication",
            "complex matter": "Alteration",
            "transmutation": "Alteration",
            "illusion": "Psychic Communication",
            "cure/disease": "Alteration: Physique",
            "divination": "Divination",
            "protection": "Conjuration",
            "abs.command": "Alteration?",
        }
        if self.type in TYPE_MAP:
            return TYPE_MAP[self.type]
        else:
            return self.type


def source_table():
    """Parse the source table big-block-of-bytes data into FWBSpell instances."""
    source_file = StringIO(FW_BOOK_SOURCE)
    non_comment = (line for line in source_file if not line.startswith("#"))
    reader = csv.reader(non_comment, skipinitialspace=True)
    header = next(reader)
    for row in reader:
        yield FWBSpell.from_csv(row)


def main():
    raw_spells = list(source_table())
    for spell in raw_spells:
        print(spell)


if __name__ == "__main__":
    main()
