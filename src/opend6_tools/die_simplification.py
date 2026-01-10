r"""
Creates the Die Code Simplification table from first principles.

This script emits the **published** wild-die table:

..  csv-table::
    :header: Die Code, 5D, Wild Die

    :math:`n`, :math:`\lfloor 0.5 + 3.5(n-5) \rfloor`, :math:`\lfloor 0.5 + 3.5(n-1) \rfloor`

Alternate
=========

There might be **slightly** more accurate approach, but it doesn't seem any more playable.

Any given die roll of :math:`n` die has two components: Ordinary Die and Wild Die.

-   **Ordinary Die**. Average is :math:`(n-1) \times 3.5`.

-   **Wild Die**. There are three possible outcomes.

    -  :math:`\frac{1}{6}` Critical Failure. This can reduce the total.
        The simplification however, doesn't change the total. Die value is 1.
        Contribution to the total is about 0.17.

    -   :math:`\frac{1}{6}` Critical Success. Roll this Wild Die again, accumulating the values.
        There can be multiple re-rolls of the wild die.

        -   :math:`\frac{5}{6}` the re-roll is not 6.
            Expected value is :math:`\frac{1}{6} + (6 + 3\times\frac{5}{6}) = \frac{17}{12} \approx 1.42`.

        -   :math:`\frac{1}{6} \times \frac{5}{6}` the first re-roll is 6, the second is not 6.
            Expected value is :math:`\frac{1}{6}^2 \times (12 + 3\times\frac{5}{6}) = \frac{29}{72} \approx 0.4`.

        -   :math:`(\frac{1}{6})^3 \frac{5}{6}` three re-rolls.
            Expected value is :math:`\frac{1}{6}^3 \times (18 + 3\times\frac{5}{6}) = \frac{41}{432} \approx 0.095`.

        -   etc. :math:`\sum 6\times\frac{1}{6}^n = \frac{6}{5}` for :math:`n` re-rolls.
            Total is :math:`\frac{1}{6} (\frac{6}{5} + 3\times\frac{5}{6}) = \frac{27}{10} = 2.7`.

    -   :math:`\frac{4}{6}` Nothing Special. Die average is 3.5.
        Contribution to the total is about 2.3.

    Total: :math:`\frac{31}{6} \approx 5.16`.

    Rolling :math:`n` die seems to be :math:`(n-1) \times 3.5 + \frac{31}{6}`.

Implementation
==============

..  autofunction:: die_code

..  autofunction:: main

"""

from collections.abc import Iterator
import csv
import sys

import typer


def die_code(start: int = 1, stop: int = 51, step: int = 1) -> Iterator[tuple[str, str, str]]:
    """Emits the sequence of die code simplifications as triples.
    (Die code, 5D, Wild Die).

    :param start: starting Die code (default 1)
    :param stop: ending Die code (default 51)
    :param step: step vvalue (default 1)
    """
    for n in range(start, stop, step):
        if n >= 5:
            d5 = int(0.5 + (n - 5) * 3.5)
        else:
            d5 = 0
        if n >= 2:
            wd = int(0.5 + (n - 1) * 3.5)
        else:
            wd = 0
        yield f"{n}D", f"+{d5}", f"+{wd}"


def main(start: int = 1, stop: int = 51) -> None:
    """Produce CSV-formatted table of Die Code simplifications."""
    target = csv.writer(sys.stdout)
    target.writerow(("Die Code", "5D", "Wild Die"))
    target.writerows(die_code(start, stop))


if __name__ == "__main__":
    typer.run(main)
