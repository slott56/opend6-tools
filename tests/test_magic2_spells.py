"""
Tests for the ``magic.spells`` module.
"""
from decimal import Decimal
from difflib import unified_diff
import logging
from pprint import pprint
from unittest.mock import Mock

import pytest

from opend6_tools.magic.spells import *
from opend6_tools.magic.workbook import display

# Overall tests of Spell, Miracle, etc.
# These are integration tests of a number of units.

@pytest.fixture
def charm_spell():
    return Spell(
        name="Charm",
        skill="Alteration",
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
            "unreal_effect": UnrealEffectAspect.based_on(("effect",), "difficulty 13"),
        },
        other_conditions=[
            GenericAspect(
                difficulty=-2,
                description="May only be used on humanoids who understand the caster’s language and can hear the caster",
            ),
        ],
    )

def test_legacy_measure_feature(charm_spell, caplog):
    caplog.set_level(logging.DEBUG)
    assert charm_spell.difficulty == 5

@pytest.fixture
def example_spell():
    example = Spell(
        name="Example",
        notes="GIVEN Example spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {},
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    return example

def test_spell(example_spell):
    assert example_spell.difficulty == 4
    # print(display(example_spell))
    ex_copy = eval(example_spell.source())
    # print(display(ex_copy))
    assert ex_copy == example_spell, "\n".join(unified_diff(display(ex_copy).splitlines(), display(example_spell).splitlines()))

    ex_copy2 = eval(repr(example_spell))
    assert ex_copy2 == example_spell

@pytest.fixture
def example_miracle():
    example = Miracle(
        name="Example",
        notes="GIVEN Example spell WHEN difficulty THEN 4",
        effect=SkillEffect("Acumen: testing", "+4D"),
        duration=DurationAspect("1 sec"),
        # range=RangeAspect("1m"),
        casting_time=CastingTimeAspect("5 sec"),
        # speed=SpeedAspect.based_on("range", description="Instantaneous"),
        other_aspects = {},
        other_conditions = [GenericAspect(1, "Everything else is completed")],
    )
    return example

def test_miracle(example_miracle):
    assert example_miracle.difficulty == 4
    # print(display(example_miracle))
    ex_copy = eval(example_miracle.source())
    # print(display(ex_copy))
    assert ex_copy == example_miracle, "\n".join(unified_diff(display(ex_copy).splitlines(), display(example_miracle).splitlines()))

# Tests of the "Based-on" variants.

def test_Spell_Simple():
    s = Spell(
        name="Simple",
        effect=GenericEffect(description="Power", difficulty=5),
        duration=GenericAspect(3, "Duration")
    )
    assert s.name == "Simple"
    assert s.difficulty == 1
    assert s.source() == "Spell(name='Simple', effect=GenericEffect('Power', 5), duration=GenericAspect(3, 'Duration'))"

def test_Spell_BasedOn_Simple():

    class MockRangeAspect(GenericDifficultyDescription, IncreasesDifficulty, Aspect):
        def __init__(self, measure: int) -> None:
            self.origin = ((measure,), {})
            m = Measure(measure, "Range")
            self.base = NormalizedAspect(self)
            self.base.details={"MEASURE": [m]}
            self.proxy = None
            self.reference = None
        def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
            return sum(d.difficulty for d in aspect.details["MEASURE"])
        def compute_description(self, aspect: NormalizedAspect) -> str:
            return repr(aspect.details["MEASURE"])

    class MockSpeedAspect(GenericDifficultyDescription, IncreasesDifficulty, Aspect):
        def derive_args(self):
            difficulty = sum(dep.difficulty() for dep in self.proxy.depends_on.values())
            proxy_args, kwargs = self.origin
            args = ((difficulty, "Instantaneous") + proxy_args[2:]), kwargs
            print(f"derived: {args}")
            return args
        def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
            print(aspect)
            return sum(d.difficulty for d in aspect.details["MEASURE"])
        def compute_description(self, aspect: NormalizedAspect) -> str:
            print(aspect)
            return repr(aspect.details["MEASURE"])

    s = Spell(
        name="BasedOn Simple",
        effect=GenericEffect(description="Power", difficulty=11),
        range=MockRangeAspect(4),
        speed=MockSpeedAspect.based_on("range", "Instantaneous"),
    )
    assert s.name == "BasedOn Simple"
    assert s.difficulty == 10
    assert s.effect.description() == "Power"
    assert s.range.description() == "[Measure(measure=Decimal('4'), description='Range', difficulty=Decimal('4'))]"
    assert s.speed.description() == "Instantaneous"
    assert s.speed.origin == ((0, "based_on('range', 'Instantaneous')",), {})
    assert s.speed.base.details == {}
    assert s.source() == "Spell(name='BasedOn Simple', effect=GenericEffect('Power', 11), range=test_Spell_BasedOn_Simple.<locals>.MockRangeAspect(4), speed=MockSpeedAspect.based_on('range', *('Instantaneous',), **{}))"

def test_Spell_BasedOn_Computation():
    class FocusedAspect(GenericDifficultyDescription, Aspect):
        def derive_args(self):
            basis = sum(dep.difficulty() for dep in self.proxy.depends_on.values())
            description = ", ".join(
                dep.description() for dep in self.proxy.depends_on.values())
            proxy_args, kwargs = self.origin
            return (basis // 5, f"based on {description}") + proxy_args[2:], kwargs

    s = Spell(
        name="BasedOn Computation",
        effect=GenericEffect(description="Power", difficulty=17),
        duration=GenericAspect(5, "Duration"),
        focused=FocusedAspect.based_on(("effect", "duration")),
    )
    assert s.name == "BasedOn Computation"
    assert s.difficulty == 4
    assert s.effect.difficulty() == 17
    assert s.effect.description() == "Power"
    assert s.duration.difficulty() == Decimal('5')
    assert s.duration.description() == "Duration"
    assert s.focused.description() == "based on Duration, Power"
    assert s.focused.difficulty() == Decimal('4')
    assert s.source() == "Spell(name='BasedOn Computation', effect=GenericEffect('Power', 17), duration=GenericAspect(5, 'Duration'), focused=FocusedAspect.based_on(('effect', 'duration'), *(), **{}))"

def test_Spell_BasedOn_Computation_Factor():
    class UnrealEffectAspect(GenericDifficultyDescription, Aspect):
        def derive_args(self):
            basis = sum(dep.difficulty() for dep in self.proxy.depends_on.values())
            # Factor from proxy.args lookup.
            factor = Decimal('0.5')
            proxy_args, kwargs = self.origin
            return (((basis * factor).quantize(1),) + proxy_args[1:]), kwargs

    s = Spell(
        name="BasedOn Computation Factor",
        effect=GenericEffect(description="Power", difficulty=17),
        duration=GenericAspect(5, "Duration"),
        unreal_effect=UnrealEffectAspect.based_on("effect", "difficulty 9"),
    )
    assert s.name == "BasedOn Computation Factor"
    assert s.difficulty == Decimal(2)
    assert s.effect.description() == "Power"
    assert s.duration.description() == "Duration"
    assert s.unreal_effect.description() == "based_on('effect', 'difficulty 9')"
    assert s.source() == "Spell(name='BasedOn Computation Factor', effect=GenericEffect('Power', 17), duration=GenericAspect(5, 'Duration'), unreal_effect=UnrealEffectAspect.based_on('effect', *('difficulty 9',), **{}))"

# Tests of some supporting classes

def test_parser():
    args = "a", "b; c"
    assert list(Parser.decompose(args)) == ['a', 'b', 'c']

def test_Aspect():
    a = GenericAspect(3, "Words")
    assert a.difficulty() == 3
    assert a.description() == "Words"
    assert a.source() == "GenericAspect(3, 'Words')"

def test_Aspect_subclass_Measure():
    class ExtendAspect(DecreasesDifficulty, Aspect):
        def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
            return sum(d.difficulty for d in aspect.details["CLASS"])
        def compute_description(self, aspect: NormalizedAspect) -> str:
            return repr(aspect.details["CLASS"])
        def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
            parsed_measure = Measure(25, "canonical")  # Mocked parsing.
            base = NormalizedAspect(self)
            base.details = {"CLASS": [parsed_measure]}
            return base
        def __init__(self, measure: str, *, proxy: NormalizedAspectProxy | None = None) -> None:
            super().__init__(measure, "")

    a = ExtendAspect("source")
    assert a.difficulty() == Decimal(7)
    assert a.description() == "[Measure(measure=Decimal('25'), description='canonical', difficulty=Decimal('7'))]"
    assert a.source() == "test_Aspect_subclass_Measure.<locals>.ExtendAspect('source', '')"

def test_Aspect_subclass_MeasureModifier():
    class ExtendAspect(DecreasesDifficulty, Aspect):
        def __init__(self, measure: str, modifier: str, *, proxy: NormalizedAspectProxy | None = None) -> None:
            self.origin = ((measure,modifier,), {})
            self.base = self.normalize_aspect(measure, modifier)
            self.proxy = proxy
            self.reference = None
        def compute_difficulty(self, aspect: NormalizedAspect) -> Decimal:
            return (
                sum(d.difficulty for d in aspect.details["MEASURE"])
            +   sum(d.difficulty for d in aspect.details["MODIFIER"])
            )
        def compute_description(self, aspect: NormalizedAspect) -> str:
            return repr(aspect.details["MEASURE"])
        def normalize_aspect(self, *args: Any, **kwargs: Any) -> NormalizedAspect:
            parsed_measure = Measure(25, "canonical")  # Mocked parsing.
            parsed_modifier = Modifier(2, "modifier")
            base = NormalizedAspect(self)
            base.details={"MEASURE": [parsed_measure], "MODIFIER": [parsed_modifier]}
            return base

    a = ExtendAspect("source", "modifier")
    assert a.difficulty() == Decimal(9)
    assert a.description() == "[Measure(measure=Decimal('25'), description='canonical', difficulty=Decimal('7'))]"
    assert a.source() == "test_Aspect_subclass_MeasureModifier.<locals>.ExtendAspect('source', 'modifier')"

def test_normalized_aspect_both():
    """A contrived test of NormalizedAspect building"""
    class TestAspectBoth(Aspect):
        def __init__(self, difficulty, description):
            self.origin = (difficulty, description), {}
            self.args = difficulty, description
            self.proxy = None
            self.reference = None
            self.base = self.normalize_aspect(difficulty, description)
        def normalize_order(self, *args: Any) -> tuple[Any, Any]:
            return args
    ta = TestAspectBoth(difficulty=10, description="Aspect")
    n = ta.base
    assert repr(n) == "NormalizedAspect(test_normalized_aspect_both.<locals>.TestAspectBoth(10, 'Aspect'))"
    assert str(n) == "NormalizedAspect parsers=[], details={}, notes=[''], kwargs={}, _difficulty=Decimal('10'), _description='Aspect'"
    assert n == n
    assert n != ta
    assert n._difficulty == Decimal('10')
    assert n._description == 'Aspect'

def test_normalized_aspect_measure():
    class TestAspectMeasure(Aspect):
        def __init__(self, difficulty):
            self.origin = (difficulty, "Measure"), {}
            self.args = difficulty,
            self.proxy = None
            self.reference = None
            self.base = self.normalize_aspect(difficulty, "Measure")
        def normalize_order(self, *args: Any) -> tuple[Any, Any]:
            return args[0],
    ta = TestAspectMeasure(difficulty=15)
    n = ta.base
    assert repr(n) == "NormalizedAspect(test_normalized_aspect_measure.<locals>.TestAspectMeasure(15, 'Measure'))"
    assert str(n) == "NormalizedAspect parsers=[], details={}, notes=[''], kwargs={}, _difficulty=Decimal('15'), _description=''"
    assert n == n
    assert n != ta
    assert n._difficulty == Decimal('15')

def test_normalized_aspect_empty():
    class TestAspectEmpty(Aspect):
        def __init__(self, **kwargs):
            self.origin = (), kwargs
            self.args = ()
            self.proxy = None
            self.reference = None
            self.base = self.normalize_aspect(0, "Measure")
        def normalize_order(self, *args: Any) -> tuple[Any, Any]:
            return ()
    ta = TestAspectEmpty(notes="Some Note")
    n = ta.base
    assert repr(n) == "NormalizedAspect(test_normalized_aspect_empty.<locals>.TestAspectEmpty())"
    assert str(n) == "NormalizedAspect parsers=[], details={}, notes=['Some Note'], kwargs={}, _difficulty=None, _description=None"
    assert n == n
    assert n != ta
    n.populate_details([])
    assert n._difficulty is None
    assert n._description is None

def test_aspect_parser():
    class SomeParser(Parser):
        def parse(self, text):
            return Decimal(42)
    class TestAspectBoth(ParsedAspect):
        result_cls = SomeParser
        def normalize_order(self, *args: Any) -> tuple[Any, Any]:
            return args

    ta = TestAspectBoth(1, "Test", notes="Some Notes")
    assert repr(ta.base) == "NormalizedAspect(test_aspect_parser.<locals>.TestAspectBoth(1, 'Test', notes='Some Notes'))"
    assert str(ta.base) == "NormalizedAspect parsers=['SomeParser'], details={'SomeParser': [Decimal('42'), Decimal('42')]}, notes=['Some Notes'], kwargs={}, _difficulty=None, _description=None"
    assert ta.base.notes == ["Some Notes"]

@pytest.fixture
def avu_debug():
    avu = AreaVolumeUnit()
    avu.DEBUG = True
    return avu

def test_avu_parsing_1(avu_debug):
    assert avu_debug.parse("2m radius circle") == Modifier(Decimal('4'), "2m radius circle")

def test_avu_parsing_ex1(avu_debug):
    with pytest.raises(InvalidVolumeError) as exc_info:
        avu_debug.parse("2m radius")
    assert exc_info.value.args == ("no shape provided in '2m radius'",)

def test_avu_parsing_ex2(avu_debug):
    with pytest.raises(ValueError) as exc_info:
        avu_debug.parse("some random fluff")
    assert exc_info.value.args == ("unknown token in 'some random fluff'",)

# Test some particularly challenging effects

def test_disadvantage_effect(caplog,):
    eff_1 = DisadvantageEffect("Hindrance: Initiative", 5, "-10 to all initiative totals")
    assert eff_1.difficulty() == 15
    assert eff_1.description() == 'hindrance: initiative (R5), -10 to all initiative totals'
    assert eff_1.incr_decr == Sign.Increase
    assert eff_1.source() == "DisadvantageEffect('Hindrance: Initiative', 5, '-10 to all initiative totals')"
    assert caplog.messages == []

def test_protection_effect(caplog,):
    protection = ProtectionEffect("Damage Resistance", 4*D+1, "physical damage", "ignore all armor")
    normalized = protection.base
    details = protection.base.details
    assert protection.difficulty() == 26
    assert protection.description() == 'Damage Resistance 4*D+1 (physical damage, ignore all armor)'
    assert protection.source() == "ProtectionEffect('Damage Resistance', 4*D+1, 'physical damage', 'ignore all armor')"

def test_components_aspect(caplog,):
    caplog.set_level(logging.DEBUG)
    components = ComponentsAspect(('Something from the type of creature being detected', 'uncommon; destroyed'), ('fire, such as a match or lit coal', 'very common; destroyed'))
    pprint([child.details for child in components.base.children])
    pprint(caplog.messages)
    assert components.difficulty() == 12
    assert components.description() == 'Something from the type of creature being detected (uncommon; destroyed); fire, such as a match or lit coal (very_common; destroyed)'

def test_spell_source(charm_spell):
    source = charm_spell.source()
    assert source.startswith("Spell(name='Charm', ")
    copy = eval(source)
    assert copy == charm_spell
    assert charm_spell.skill == "Alteration"
    # Force use of cache
    assert charm_spell.skill == "Alteration"

    assert charm_spell._asdict() == {
        'casting_time': {
            'args': (
                '1 round',
            ),
            'class_': 'CastingTimeAspect',
        },
        'duration': {
            'args': (
                '1 minute',
            ),
            'class_': 'DurationAspect',
        },
        'effect': {
            'args': (
                'charm skill',
                '+4D',
            ),
            'class_': 'SkillEffect',
        },
        'name': 'Charm',
        'notes': [
            'With a smile and a friendly gesture, the caster improves his charm '
            'skill by for one minute. (If he no charm skill, add the bonus to the '
            'character’s Charisma attribute.) As this is an illusory spell, if the '
            'intended target of the charm disbelieves it, any effect the charm '
            'attempt had wears off immediately.',
        ],
        'other_aspects': {
            'gesture': {
                'args': (
                    'Smile and make a gesture of welcome or admiration',
                    'simple',
                ),
                'class_': 'GesturesAspect',
            },
            'unreal_effect': {
                'args': (
                    0,
                    "based_on('effect', 'difficulty 13')",
                ),
                'class_': 'UnrealEffectAspect',
            },
        },
        'other_conditions': [
            {
                'args': (
                    -2,
                    'May only be used on humanoids who understand the caster’s '
                    'language and can hear the caster',
                ),
                'class_': 'GenericAspect',
            },
        ],
        'range': {
            'args': (
                'self',
            ),
            'class_': 'RangeAspect',
        },
        'speed': {
            'args': (
                0,
                "based_on('range', '')",
            ),
            'class_': 'SpeedAspect',
        },
    }
