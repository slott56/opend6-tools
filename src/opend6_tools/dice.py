"""
A DSL for dice definitions.

The most important global object is ``D``, which is the basis for the DieCode DSL.

Example:

>>> from opend6_tools.dice import D
>>> 3*D + 2
3*D+2

..  autoclass:: DieCode
    :members:
    :special-members:
    :member-order:  bysource

..  autoclass:: Roll
    :members:
    :undoc-members:

..  autoclass:: CriticalSuccess
    :show-inheritance:
    :members:

..  autoclass:: CriticalFailure
    :show-inheritance:
    :members:

This includes the ``dice_app`` CLI.

..  autofunction:: main
"""

from dataclasses import dataclass
from decimal import Decimal
import os
import random
from random import randint
import re
from typing import Any, ClassVar, Annotated

import typer

from humre import (
    optional_group,
    starts_and_ends_with,
)


@dataclass
class Roll:
    """A single roll of the dice."""

    die: list[int]  #: The die values
    pips: int  #: Additional pips to add
    rolls: int  #: Number of rolls (>1 for Critical Success)
    success: ClassVar[bool] = False
    fail: ClassVar[bool] = False

    @property
    def total(self) -> int:
        """Total of Die plus bonus pips"""
        return sum(self.die) + self.pips

    def __str__(self) -> str:
        return f"{self.total}"


@dataclass
class CriticalSuccess(Roll):
    """A single roll that was a Critical Success -- Wild Die was 6."""

    success = True

    def __str__(self) -> str:
        return f"{self.total}{'!' * (self.rolls - 1)}"


@dataclass
class CriticalFailure(Roll):
    """A single roll that was a Critical Failure -- Wild Die was 1."""

    fail = True

    @property
    def low_total(self) -> int:
        return sum(self.die) - max(self.die) + self.pips

    def __str__(self) -> str:
        return f"{self.low_total}? ({self.total})"


class DieCode:
    r"""
    Specifications for collections of dice.
    Computes the overall measure, :math:`3 \times d + p`.

    >>> from opend6_tools.dice import *

    >>> r = 3*D+2
    >>> r.measure
    Decimal('11')
    >>> repr(r)
    '3*D+2'

    Can also parse a text specification.

    >>> t = DieCode.parse_str("3D+2")
    >>> t.measure
    Decimal('11')
    >>> repr(t)
    '3*D+2'

    A degenerate case of only pips, not clear why someone might need this.

    >>> DieCode.parse_str("2")
    0*D+2
    >>> 0*D + 2
    0*D+2

    >>> from random import seed
    >>> seed(42)
    >>> physique = 4*D
    >>> [str(physique.roll()) for _ in range(12)]
    ['17!', '13!', '12? (18)', '6? (11)', '10', '13', '23', '15', '16!', '10', '9', '12']
    """

    # It is OpenD6, but, we might want to reuse this for other systems.
    faces: ClassVar[int] = 6

    def __init__(self, n: int | Decimal = 1, adj: int | Decimal = 0) -> None:
        """Create a working DieCode instance, usually the global ``D``."""
        self.n = int(n)  #: Number of dice
        self.adj = int(adj)  #: Additional pips

    def __repr__(self) -> str:
        return f"{int(self.n):d}*D{self.adj:+d}" if self.adj else f"{int(self.n):d}*D"

    def __str__(self) -> str:
        if self.n and self.adj:
            return f"{self.n}D+{self.adj}"
        elif self.n:
            return f"{self.n}D"
        elif self.adj:
            return f"+{self.adj}"
        else:
            return ""

    def __mul__(self, other: Any) -> "DieCode":
        """Implement the ``*`` operator for ``D`` and a number."""
        match other:
            case int() | Decimal():
                return DieCode(int(self.n * other), self.adj * other)
            case _:  # pragma: no cover
                return NotImplemented  # pragma: no cover

    __rmul__ = __mul__

    def __add__(self, other: Any) -> "DieCode":
        """Implement the ``+`` operator for ``D`` and a number."""
        match other:
            case int() | Decimal():
                dice, pips = divmod(self.adj + other, 3)
                return DieCode(int(self.n + dice), int(pips))
            case DieCode() as d:
                return DieCode.from_pips(self.measure + d.measure)
            case _:  # pragma: no cover
                return NotImplemented  # pragma: no cover

    __radd__ = __add__

    def __sub__(self, other: Any) -> "DieCode":
        match other:
            case int() as p:
                return DieCode.from_pips(self.measure - p)
            case DieCode() as d:
                return DieCode.from_pips(self.measure - d.measure)
            case _:  # pragma: no cover
                return NotImplemented

    def __bool__(self) -> bool:
        return bool(self.n) or bool(self.adj)

    def __eq__(self, other: Any) -> bool:
        match other:
            case DieCode() as die_code:
                return self.measure == die_code.measure
            case int() as n:
                return self.measure == n
            case _:  # pragma: no cover
                return NotImplemented

    @property
    def d(self) -> int:
        """Legacy attribute reference, now a property."""
        return self.n

    @classmethod
    def from_pips(cls, pips: int | Decimal) -> "DieCode":
        """
        Converts number of pips to Die + Pips.

        :param pips: pips value
        :return: DieCode
        """
        return cls(*divmod(pips, 3))

    @property
    def measure(self) -> Decimal:
        """The overall measure associated with this DieCode."""
        return Decimal(self.n * 3 + self.adj)

    @classmethod
    def parse_str(cls, text: str) -> "DieCode":
        """
        Parse a string representation of a DieCode object, example: ``"3D+2"``.

        The syntax has three closely-related forms:  ``[+]n[*]D+n`` | ``[+]n[*]D`` | ``+n``

        Pragmatically, ``+`` and ``*`` are essentially whitespace.
        The meaningful tokens are strings of digits and ``D``.
        The three interesting forms are nDn, nD, and n.
        """
        text_clean = re.sub(r"[\s\+\*]", "", text.strip())
        pattern = starts_and_ends_with(
            optional_group(r"\d+") + optional_group(r"D") + optional_group(r"\d+")
        )
        if (match := re.match(pattern, text_clean)) is None:
            raise ValueError(f"invalid dice expression {text!r}")
        if match.group(1) and match.group(2) and match.group(3):
            dice = int(match.group(1))
            pips = int(match.group(3))
        elif match.group(1) and match.group(2):
            dice = int(match.group(1))
            pips = 0
        elif match.group(1) and not match.group(2):
            dice = 0
            pips = int(match.group(1))
        else:  # pragma: no cover
            raise ValueError(f"invalid dice expression {text!r}")
        return dice * D + pips

    def roll(self) -> Roll:
        """The "Wild Die" roll algorithm.

        This returns several things:

        1. Ordinary result: a :py:class:`Roll` instance.

        2. Critical Success, wild die was 6.
            A :py:class:`CriticalSuccess` instance.

        3. Critical Failure, wild die was 1.
            Two totals (with and without the highest die value.)
            A :py:class:`CriticalFailure` instance.
        """
        # Last Die is the "wild die".
        count = 1
        roll = [randint(1, self.faces) for d in range(self.n)]
        if roll[-1] == 1:
            # Critical Failure -- two totals: with and without highest die value.
            return CriticalFailure(roll, self.adj, rolls=count)
        elif roll[-1] == self.faces:
            # Critical Success -- Reroll wild die.
            while roll[-1] == self.faces:
                count += 1
                roll.append(randint(1, self.faces))
            return CriticalSuccess(roll, self.adj, rolls=count)
        else:
            # Ordinary roll.
            return Roll(roll, self.adj, rolls=count)


D = DieCode()


dice_app = typer.Typer()


@dice_app.command()
def main(
    expr: Annotated[
        DieCode,
        typer.Argument(
            parser=DieCode.parse_str,
            help="Dice expression, example: '2*D6+3' (quotes are *required*)",
        ),
    ],
    count: Annotated[
        int, typer.Option("--count", "-c", help="number of times to roll")
    ] = 1,
):
    """Roll the handful of dice described by a dice expression.
    Use the --count option to roll multiple times.

    ? is a critical failure showing a total with the largest
    die value excluded, and, in ()'s, the total of all dice.

    ! is a critical success followed by the number of re-rolls.
    """
    if seed := os.environ.get("OPEND6_SEED"):
        random.seed(seed.encode("UTF-8"))

    for _ in range(count):
        output = expr.roll()
        print(output)


if __name__ == "__main__":  # pragma: no cover
    dice_app()
