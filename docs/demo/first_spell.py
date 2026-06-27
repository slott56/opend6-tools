"""Example from documentation."""

from opend6_tools.magic import *

charm = Spell(
    name="Charm",
    skill="Temperamental Alteration",
    notes=[
        "With a smile and a friendly gesture, the caster improves his charm skill by for one minute. (If he no charm skill, add the bonus to the character’s Charisma attribute.) As this is an illusory spell, if the intended target of the charm disbelieves it, any effect the charm attempt had wears off immediately."
    ],
    effect=SkillEffect("charm skill", "+4D"),
    duration=DurationAspect(measure="1 minute"),
    range=RangeAspect(measure="self"),
    casting_time=CastingTimeAspect(measure="1 round"),
    speed=SpeedAspect.based_on(("range",), ""),
    other_aspects={
        "gesture": GesturesAspect(
            "Smile and make a gesture of welcome or admiration", "simple"
        ),
        "unreal_effect": UnrealEffectAspect.based_on(("effect",),
                                                     "difficulty 13"),
    },
    other_conditions=[
        GenericAspect(
            difficulty=-2,
            description="May only be used on humanoids who understand the caster’s language and can hear the caster",
        ),
    ],
)

spells = [
    charm,
]

__test__ = {
    "Charm": ">>> spells[0].difficulty\n5",
}

if __name__ == "__main__":
    app = build_app(spells)
    app()
