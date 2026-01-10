"""Spells from my Fantasy Wargaming Notes.

No real idea where these spell descriptions originated.
These appear to be a mapping from some Hero System 4th ed. Fantasy Hero Supplement.)
"""

from collections import Counter
from collections.abc import Iterator
import csv
from dataclasses import dataclass, field
from enum import Enum, auto
from io import StringIO
from typing import ClassVar, Self

from humre import *
import magic1 as magic


NOTE_SOURCE_CSV = """\
roll_low, roll_high, number, spell_name, type, DD, controller, details
3, 5, 2, Immediate Hurt, Cure/Disease, 5, Aister, -1 End <= 1/2, +1 1 Part, +3 Cause & Immed. Loss, +1 2 pts.
13, 14, 6, Prot. from Magic, Protection, 1, Aister, +1 ea. -1 in opp. link
22, 24, 10, Move Wall of Rock, Elemental, 6, Aister, +2 Earth, +2 10 cu. ft., +2 construct
25, 26, 11, Conjure Wall of Rock, Elemental, 7, Aister, +2 Earth, +2 10 cu. ft., +3 create from nothing
32, 33, 14, Passwall 20 ft., Elemental , 6, Aister, +2 earth, +2 medium, +2 breach
41, 43, 18, Earth Quake, Elemental, 10, Aister, +2 Earth, +4 immense, +1 move slowly, +3 animate
58, 60, 25, Flesh-Stone, Transmutation, 8, Aister, +3 Aminal flesh, +3 Transmute, +2 Earth
61, 62, 26, Charm, Abs.Command, 5, Inat, 
1, 2, 1, Gradual Heal, Cure/Disease, 4, Conna, 0 End <= 3/4, +3 3 Parts, +1 Cure Only
18, 19, 8, Freeze (10 min.), Abs. Command, 4, Conna, 
20, 21, 9, Sleep, Abs. Command, 2, Conna, 
44, 45, 19, Dirt to Mud, Elemental, 6, Conna, +1 Water, +3 large, +2 amplify
27, 29, 12, Light Fire, Elemental, 3, Ercha, 0 Fire, +3 create from nothing
30, 31, 13, Move Fire, Elemental, 1, Ercha, 0 Fire, 0 Move Slowly, 0 no change
34, 36, 15, Passfire 20 ft., Elemental, 4, Ercha, 0 fire, +2 medium, +2 breach
37, 38, 16, Fire Ball, Elemental, 5, Ercha, 0 fire, +2 move quickly, +3 create
65, 67, 28, Light, Elemental, 3, Ercha, 0 Fire, 0 V. Small, +3 Create
91, 93, 39, Human Combustion, Elemental, 6, Ercha, +3 Animal, 0 fire, +1 small, 0 no motion, +2 amplify
39, 40, 17, Lightning, Elemental, 6, Ercha/Iudax, 0 fire, +1 air, +1 small, +1 slowly, +3 create
84, 86, 36, Shocking Grasp, Elemental, 3, Ercha/Iudax, 0 fire, +1 air, 0 v. small, 0 no motion, +2 amplify
6, 7, 3, Illusion of Sm. Monster, Illusion, 5, Inat, +1 Small, +1 2-3 colors, +1 monster, +2 moving
8, 10, 4, Illusion of Rat, Illusion, 2, Inat, -1 Tiny, 0 1 color, +1 animal, +2 moving
11, 12, 5, Perm. Illusion of sm. monster, Illusion, 8, Inat, +1 Small, +1 2-3 colors, +1 monster, +2 moving, +3 permanent
56, 57, 24, ESP, Divination, 3, Inat, 
80, 81, 34, Infravision, Abs. Command, 4, Inat, 
89, 90, 38, Find Path, Divination, 3, Inat, 
99, 100, 42, Communicate w/ Plant/Animal, Abs. Command, 3, Inat, 
15, 17, 7, Halt, Abs. Command, 1, Iudax, 
46, 48, 20, Wind Gust, Elemental, 3, Iudax, +1 air, +1 small, +1 slow
49, 50, 21, Wind Storm, Elemental, 5, Iudax, +1 air, +3 large, +1 slow
68, 69, 29, Shield, Abs. Command, 2, Iudax, Shields from linked people
70, 71, 30, Shield, Abs. Command, 2, Iudax, Shields from linked people
77, 79, 33, Levitate/Fly, Complex Matter, 6, Iudax, +3 Animal, +1 small, +1 move slowly, +1 defy gravity
94, 95, 40, Telekinesis, Complex Matter, 3-6, Iudax, +x Object Type, +1 small, +1 Slowly, +1 Defy Gravity/Friction
96, 98, 41, Silence, Elemental, 4, Iudax, +1 Air, +2 medium, 0 no motion, +1 defy Conserv. Energy
75, 76, 32, Impervious leather armor, Transmutation, 5, [object made impervious], +2 Hides, +1 small, +2 amplify
72, 74, 31, Totally Invisible, Transmutation, 7, [object made invisible], +3 Animal, +1 small, +1 Defy Physics, +2 attenuate
82, 83, 35, Mend Iron, Complex Matter, 6, [Type of metal], +3 Lead/Iron, +1 small, +2 repair
87, 88, 37, Pass Plant, Complex Matter, 6, [type of plant], +2 plant matter, +2 medium, +2 breach
63, 64, 27, Hold Portal, Transmutation, 5, [Type of Wood], +2 Vegetable Matter, +2 Construct, +1 small
51, 52, 22, Knock, Complex matter, 4, [type of wood], +2 vegetable matter, +1 small, +1 slowly
53, 55, 23, Warp Wood, Complex matter, 4, [type of wood], +2 vegetable matter, +1 small, +1 slowly
"""


class AspectPurpose(Enum):
    EFFECT = "effect"
    OTHER_ASPECTS = "other_aspects"
    OTHER_CONDITIONS = "other_conditions"
    SKILL_USED = "skill"


@dataclass
class FWFeature:
    """
    Some features that don't make much sense.
    object type
    earth
    fire
    air
    water
    no motion
    defy physics
    defy gravity
    defy gravity/friction
    defy conserv. energy
    """

    difficulty: int | str  # Usually a signed number, one example of "+x"
    description: str

    @classmethod
    def from_csv(cls, text: str) -> Self | None:
        if not text:
            return None
        pattern = (
            group(optional(chars("+-")) + one_or_more(chars(DIGIT, "x")))
            + zero_or_more(WHITESPACE)
            + group(EVERYTHING)
        )
        if match := re.match(pattern, text):
            dd: int | str
            try:
                dd = int(match.group(1))
            except:
                dd = match.group(1)
            feature = cls(difficulty=dd, description=match.group(2))
        else:
            # print(f"&&& Could not match {text!r}: edit to move to effect")
            feature = cls(difficulty=0, description=text)
        return feature

    def aspect(self) -> tuple[AspectPurpose, magic.Aspect, str | None]:
        """
        Needs to help build a dictionary.

            {
            effect=Aspect,
            other_aspects={name: Aspect},
            other_conditions=[Aspect],
            skill_used=name,
            }

        The result is s Enum, Aspect, and optional name for the other Aspects.
        Mostly, these are "area_of_effect", and "other_alterants".
        """
        mass_dist_time = {
            "tiny": magic.weight_aspect("1kg", "tiny"),
            "v. small": magic.weight_aspect("5kg", "v. small"),
            "small": magic.weight_aspect("25kg", "small"),
            "medium": magic.weight_aspect("100kg", "medium"),
            "large": magic.weight_aspect("250kg", "large"),
            "immense": magic.weight_aspect("600kg", "immense"),
            "permanent": magic.time_aspect("1mon", "permanent"),
            "move slowly": magic.Aspect(format="move 1m/s", base_difficulty=0),
            "slowly": magic.Aspect(format="move 1m/s", base_difficulty=0),
            "slow": magic.Aspect(format="move 1m/s", base_difficulty=0),
            "move quickly": magic.Aspect(format="move 2m/s", base_difficulty=5),
            "2 pts.": magic.Aspect(format="does 2D Stun damage", base_difficulty=10),
            "shields from linked people": magic.Aspect(
                "adds +2D to link difficulty", base_difficulty=10
            ),
        }
        other_aspect = {
            # "cause & immed. loss": magic.Aspect(format="Damage", base_difficulty=10),
            "10 cu. ft.": (
                magic.Aspect(format="27 cu m, 3m×3m×3m, 2m sphere", base_difficulty=10),
                "area_of_effect",
            ),
            "monster": (
                magic.Aspect(format="illusion includes a monster", base_difficulty=10),
                "other_alterant",
            ),
            "animal": (
                magic.Aspect(
                    format="illusion includes a common animal", base_difficulty=5
                ),
                "other_alterant",
            ),
            "moving": (
                magic.Aspect(format="illusion is moving", base_difficulty=5),
                "other_alterant",
            ),
        }
        skill_used = {
            "construct": "Conjuration",
            "create from nothing": "Conjuration",
            "create": "Conjuration",
            "breach": "Alteration",
            "no change": "Alteration",
            "animate": "Alteration",
            "amplify": "Alteration",
            "transmute": "Alteration",
            "attenuate": "Alteration",
            "repair": "Alteration",
        }
        other_condition = {
            "end <= 3/4": magic.Aspect(
                format="Heal only with Body <= 3/4", base_difficulty=0
            ),
            "end <= 1/2": magic.Aspect(
                format="Damage only with Body <= 1/2", base_difficulty=-5
            ),
            "3 parts": magic.Aspect(
                format="limited to 3 body parts", base_difficulty=9
            ),
            "1 part": magic.Aspect(format="limited to 1 body part", base_difficulty=3),
            "cure only": magic.Aspect(
                format="limited to disease cure", base_difficulty=3
            ),
            "1 color": magic.Aspect(
                format="illusion limited to 1 color", base_difficulty=0
            ),
            "2-3 colors": magic.Aspect(
                format="illusion limited to 3 colors", base_difficulty=5
            ),
            "ea. -1 in opp. link": magic.Aspect(format="opposed"),
            "earth": magic.Aspect(format="elemental alteration: earth"),
            "air": magic.Aspect(format="elemental alteration: air"),
            "fire": magic.Aspect(format="elemental alteration: fire"),
            "water": magic.Aspect(format="elemental alteration: water"),
            "lead/iron": magic.Aspect(format="elemental alteration: earth/fire"),
            "vegetable matter": magic.Aspect(format="limited to wood"),
            "plant matter": magic.Aspect(format="limited to plants"),
            "aminal flesh": magic.Aspect(format="limited to living animal"),
            "hides": magic.Aspect(format="limited to leather"),
        }

        d = self.description.lower()
        if d in mass_dist_time:
            return AspectPurpose.EFFECT, mass_dist_time[d], None
        elif d in other_aspect:
            return (AspectPurpose.OTHER_ASPECTS,) + other_aspect[d]
        elif d in other_condition:
            return AspectPurpose.OTHER_CONDITIONS, other_condition[d], None
        elif d in skill_used:
            return AspectPurpose.SKILL_USED, skill_used[d]
        else:
            # print("No plausible feature for {d!r}")
            return None


@dataclass
class FWSpell:
    """
    A Fantasy Wargaming Spell summary.

    This is used to build a proper ``Spell`` instance with the OpenD6 aspects.

    Skill Used is the type
    Difficulty likely has a mapping above about FW * 4 or 5 is OpenD6.
    Effect is generally in the details
    Duration is unclear from these summaries
    Range isn't stated.
    Speed isn't used.
    Casting Time is unclear.
    """

    # Ignore these.
    roll_low: int
    roll_high: int
    number: int

    # Map these to OpenD6 attributes
    spell_name: str  # Name.
    type: str  # Skill Used.
    DD: str  # Difficulty (keep this as an Aspect to benchmark OpenD6 mapping)
    deity: str  # Maps to "controller" and "diminisher"
    details: list[FWFeature] = field(default=list)  # Effect, Other Aspects

    @classmethod
    def from_csv(cls, row: list[str]) -> Self:
        details_text = ", ".join(row[7:])
        details = list(
            filter(
                None,
                (FWFeature.from_csv(item.strip()) for item in details_text.split(",")),
            )
        )
        return cls(
            roll_low=int(row[0]),
            roll_high=int(row[1]),
            number=int(row[2]),
            spell_name=row[3],
            type=row[4].strip().lower(),
            DD=row[5],
            deity=row[6].lower(),
            details=details,
        )

    def controller(self) -> str:
        """Controller is one of the correspondencies.
        There's also a diminisher; the opposite side of the hexagon.
        """
        CONTROLLER_MAP = {
            "aister": "Physique",
            "inat": "Intelligence",
            "wissa": "Acumen",
            "iudax": "Agility",
            "conna": "Coordination",
            "ercha": "Charisma",
            "ercha/iudax": "Agility",
        }
        if self.deity in CONTROLLER_MAP:
            return CONTROLLER_MAP[self.deity]
        else:
            return self.deity

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

    def aspects(self) -> Iterator[tuple[AspectPurpose, magic.Aspect, str | None]]:
        return filter(None, (d.aspect() for d in self.details))

    def opend6(self) -> magic.Spell:
        d6_aspects = {
            "skill": self.skill_used(),
        }
        for p_a_n in self.aspects():
            match p_a_n:
                case (AspectPurpose.SKILL_USED, _, skill):
                    d6_aspects["skill"] = skill
                case (AspectPurpose.EFFECT, effect, _):
                    if "effect" in d6_aspects:
                        # multi-part effect
                        d6_aspects["effect"] = magic.Aspect(
                            format=d6_aspects["effect"].format + " " + effect.format,
                            base_difficulty=d6_aspects["effect"].base_difficulty
                            + effect.base_difficulty,
                        )
                    else:
                        d6_aspects["effect"] = effect
                case (AspectPurpose.OTHER_ASPECTS, other, name):
                    d6_aspects["other_aspects"] = d6_aspects.get(
                        "other_aspects", {}
                    ) | {name: other}
                case (AspectPurpose.OTHER_CONDITIONS, other, _):
                    d6_aspects.setdefault("other_conditions", []).append(other)
        if "effect" not in d6_aspects:
            d6_aspects["effect"] = magic.Aspect("?")
        return magic.Spell(
            name=self.spell_name,
            duration=magic.time_aspect("1s"),
            casting_time=magic.time_aspect("1s"),
            notes=self.controller(),
            range=magic.distance_aspect("20m"),
            **d6_aspects,
        )


def source_table():
    """Parse the source table big-block-of-bytes data into FWSpell instances."""
    source_file = StringIO(NOTE_SOURCE_CSV)
    reader = csv.reader(source_file, skipinitialspace=True)
    header = next(reader)
    for row in reader:
        yield FWSpell.from_csv(row)


def main():
    """Makes a module out of the converted spells."""
    raw_spells = sorted(source_table(), key=lambda rs: rs.number)
    d6_spells = [spell.opend6() for spell in raw_spells]
    print(magic.module("More Spells", d6_spells))
    # for spell in raw_spells:
    #    # print(spell.spell_name, spell.type, spell.skill_used(), spell.DD, spell.controller(), spell.aspects())
    #    print(spell.opend6())


if __name__ == "__main__":
    main()
