r"""
Creates the Spell Measures table from first principles.

Two cases:

-   Very first range has steps: 1, 1.5, 2.5, 3.5, 5.

-   Remaining ranges and bands have steps:  1, 1.5, 2, 2.5, 4, 6.

Both are *essentially* this.

..  math::

    v = \lceil 5 \times \log_{10}(m) \rceil

However, the very first range and all the remaining ranges have slightly
different decimal rounding rules.

-   The first five are ``ROUND_CEILING``.

-   All the rest are  ``ROUND_HALF_UP``.

The whole table has 3 ranges: :math:`\times 10^0`, :math:`\times 10^1`, and :math:`\times 10^2`,
in 6 bands: "", ",000", " million", " billion", " quadrillion", " quintillion".


Implementation
==============

..  autofunction:: value_measure

..  autofunction:: main
"""

from collections.abc import Iterator
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_HALF_UP
import csv
import sys

import typer


def value_measure() -> Iterator[tuple[Decimal, str]]:
    """Emits the sequence of game values and the source measures."""
    first = [1, 1.5, 2.5, 3.5, 5]

    rest = [1, 1.5, 2.5, 4, 6]
    bands = [
        (group, scale, format)
        for group, format in [
            (1, lambda measure, scale: f"{int(measure * scale)}"),
            (10**3, lambda measure, scale: f"{int(measure * scale * 1000):,}"),
            (10**6, lambda measure, scale: f"{measure * scale:.1f} million"),
            (10**9, lambda measure, scale: f"{measure * scale:.1f} billion"),
            (10**12, lambda measure, scale: f"{measure * scale:.1f} trillion"),
            (10**15, lambda measure, scale: f"{measure * scale:.1f} quadrillion"),
            (10**18, lambda measure, scale: f"{measure * scale:.1f} quintillion"),
        ]
        for scale in [10**0, 10**1, 10**2]
    ]

    # First 5 -- measure < 10.
    for measure in first:
        m_10 = Decimal(str(measure))
        with localcontext(rounding=ROUND_CEILING):
            v = (m_10.log10() * 5).quantize(Decimal("1"))
        yield v, str(measure)
        # yield round(5 * math.log(measure, 10) + 0.25), measure

    # Remainder -- measure >= 10 up to 100 quintillion which has a value of 100.
    for group, scale, format_expr in bands:
        for measure in rest:
            if 10 <= (m := measure * scale * group) <= 100 * 10**18:
                m_10 = Decimal(m)
                with localcontext(rounding=ROUND_HALF_UP):
                    v = (m_10.log10() * 5).quantize(Decimal("1"))
                yield v, format_expr(measure, scale)
                # yield round(5 * math.log(m, 10)), format_expr(measure, scale)


def main(rows: int = 35) -> None:
    """Produce CSV-formatted table of Spell Measures.

    The number of rows defines the format.

    -   For 100 rows, the table is in a single pair of columns.

    -   For less than 100 rows, the table is split into columns to meet the row constraint.
        The published table has 35 rows, therefore, this is the default.
    """
    table = list(value_measure())
    target = csv.writer(sys.stdout)
    if rows >= len(table):
        target.writerow(("Value", "Measure"))
        target.writerows(table)
    else:
        columns = (len(table) + rows) // rows
        target.writerow(("Val.", "Measure") * columns)
        for row in range(rows):
            source_row = (row + col * rows for col in range(columns))
            display_row = [
                table[src][a] if src < len(table) else None
                for src in source_row
                for a in (0, 1)
            ]
            target.writerow(display_row)


app = typer.Typer()
app.command()(main)

if __name__ == "__main__":  # pragma: no cover
    app()
