"""
Scrape equipment from  "source/Armor, Weapons, and Vehicles | The OpenD6 Project.html"

This is saved page https://opend6project.wordpress.com/equipment/armor-weapons-and-vehicles/

Note. Modern Vehicles and Fantasy Vehicles sections have sections that masquerade as sub-tables.
Sigh.
"""

from contextlib import redirect_stdout
from dataclasses import dataclass
from pathlib import Path
import re
from typing import TextIO, Iterable, Iterator, Self, ClassVar

from bs4 import BeautifulSoup


@dataclass
class EquipmentTable:
    """Extract equipment columns.
    Locate Footnote references in data and footnote definitions from the end of the table.
    """

    title_row: list[str]
    header: list[str]
    body: list[list[str]]
    text: list[str]
    notes: list[str]

    # Order matters: longest first.
    NOTE_CHARS: ClassVar[list[str]] = ["**", "*", "†", "‡"]

    @property
    def title(self) -> str:
        return " ".join(self.title_row).strip()

    @property
    def title_slug(self) -> str:
        return self.title.lower().replace(" ", "_")

    @classmethod
    def has_footnote_ref(cls, cell: str) -> str:
        """
        Reference to a note is any of the NOTE_CHARS or end with (\\d)
        """
        fn_pat = re.compile(r"(\(\d\))$")
        if clean := cell.rstrip():
            char_matches = [c for c in cls.NOTE_CHARS if clean.endswith(c)]
            if char_matches:
                return char_matches[0]
            if match := fn_pat.search(clean):
                return match.group(1)
        return ""

    @classmethod
    def has_footnote_def(cls, text: str) -> bool:
        """
        Notes start with NOTE_CHARS char or digit.
        Supplemental text starts with "Notes:"
        """
        return any(text.startswith(n) for n in cls.NOTE_CHARS) or text[0].isdigit()

    @classmethod
    def from_text(
        cls, source: list[list[str]], notes: list[list[str]], text: list[list[str]]
    ) -> Self:
        """Source breaks down into Title, Heading, Body.
        Body may have footnote references in column values.
        Plus Notes rows scattered throughout.
        """
        print("Table:", " ".join(source[0]))
        cleaned_notes = []
        for note in [n[0] for n in notes]:
            splits = re.split(r"(\*\*|\*|†|‡|\d\.(?=\s+\w+))", note)
            if not splits[0]:
                del splits[0]
            for head, tail in zip(splits[::2], splits[1::2]):
                cleaned_notes.append(f"{head}{tail}")

        return EquipmentTable(
            title_row=source[0],
            header=source[1],
            body=source[2:],
            text=[row[0] for row in text],
            notes=cleaned_notes,
        )

    def rst(self) -> None:
        """
        Note reference text has ["**", "*", "†", "‡"] or (\\d)
        Mark notes lines in a cell gets RST links. `[#name]`_.

        At the end, add `.. [#name]` preface to note text.
        """

        def quote(row: list[str]) -> list[str]:
            """CSV ``csv.QUOTE_ALL`` dialect."""
            return list(map(lambda t: f'"{t.replace('"', '""')}"', row))

        NOTE_REPLACEMENTS = {
            "*": "asterisk",
            "**": "double_asterisk",
            "†": "dagger",
            "‡": "double_dagger",
            "1.": "one",
            "2.": "two",
            "3.": "three",
            "4.": "four",
            "(1)": "one",
            "(2)": "two",
            "(3)": "three",
            "(4)": "four",
        }

        print(f"..  csv-table:: {self.title}")
        print(f"    :header: {','.join(quote(self.header))}")
        print()

        notes_needed: set[str] = set()
        for row in self.body:
            rst_row = []
            # TODO: Two special cases...
            # 1. row[0] and not any(row[1:]) -- Needs **bold**.
            # 2. row[1:] == self.header[1:] -- Drop cols 1: and **bold**,
            for cell in row:
                if chars := self.has_footnote_ref(cell):
                    repl = NOTE_REPLACEMENTS[chars]
                    notes_needed.add(repl)
                    extra = f"{cell[: -len(chars)]} [#{repl}]_"
                    rst_row.append(extra)
                else:
                    rst_row.append(cell)
            print(f"    {','.join(quote(rst_row))}")
        print()

        # Stray text.
        for text in self.text:
            print(text)
            print()

        # Footnotes.
        for note in self.notes:
            npat = re.compile(r"\*\*|\*|†|‡|\d\.")
            if match := npat.match(note):
                chars = match.group(0)
            else:
                raise ValueError(note)
            repl = NOTE_REPLACEMENTS[chars]
            if repl in notes_needed:
                print(f".. [#{repl}] {note[len(chars) :]}")
                print()


def sub_table_splitter(
    all_rows: list[list[str]], text: list[list[str]], notes: list[list[str]]
) -> Iterator[EquipmentTable]:
    """The Modern Melee Weapons seems to have a sub-table inside it."""
    empty_row = True
    sub_table: list[list[str]] = []
    for row in all_rows:
        if not any(row):
            # Blank row
            empty_row = True
            continue
        # Found an embedded title row
        if empty_row and row[0] and not any(row[1:]):
            if sub_table:
                yield EquipmentTable.from_text(sub_table, notes=notes, text=text)
                sub_table = []
        sub_table.append(row)
        empty_row = False
    if sub_table:
        yield EquipmentTable.from_text(sub_table, notes=notes, text=text)


def table_iter(html_path: Path) -> Iterator[EquipmentTable]:
    html_doc = html_path.read_text()
    soup = BeautifulSoup(html_doc, "html.parser")
    article = soup.article
    header = article.header
    print("Title:", header.text)
    content = article.div

    # Mostly, each <table> is an equipment table.
    # Except in a few cases, where two tables are merged into one. Sigh.
    for c in content.children:
        if c.name == "p" and c.text.strip():
            print(c.text)
            print()
        elif c.name == "table":
            # colgroup = c.colgroup  # Mostly column widths.
            # print(colgroup.prettify())
            tbody = c.tbody

            # In one case, multiple sub-tables wedged into a single <tbody>.
            # These can share notes at the bottom of the sub-tables.
            # Extract notes and note-like text.
            all_rows = [
                [col.text.strip() for col in row.find_all("td", recursive=False)]
                for row in tbody.find_all("tr", recursive=False)
            ]
            print("Starting:", all_rows[0][0])

            notes: set[tuple[str, ...]] = set()
            text: list[list[str]] = []
            for row in all_rows:
                # Find internal notes rows
                if row[0] and not any(row[1:]):
                    # Segregate notes with footnote prefix and "Note" prefix
                    if EquipmentTable.has_footnote_def(row[0]):
                        notes.add(tuple(row))
                    if row[0][:4] == "Note":
                        text.append(row)

            for n in notes:
                while (orig := list(n)) in all_rows:
                    all_rows.remove(orig)
            for t in text:
                all_rows.remove(t)

            if all_rows[0][0] == "Modern Melee Weapons":
                yield from sub_table_splitter(all_rows, text=text, notes=notes)
            else:
                yield EquipmentTable.from_text(all_rows, text=text, notes=notes)
        elif c.name == "div":
            pass  # id=atatags-370373-688f73da8dfc9, a WordPress thingy
        elif non_whitespace := c.text.strip():
            print(non_whitespace)
        else:
            # No name and no text.
            pass


def main():
    source_dir = Path.cwd().parent / "source"
    html_path = source_dir / "Armor, Weapons, and Vehicles | The OpenD6 Project.html"
    equipment_tables = list(table_iter(html_path))

    target_dir = Path.cwd().parent / "campaign"
    for eq_tbl in equipment_tables:
        target_rst_path = (target_dir / f"{eq_tbl.title_slug}_equipment").with_suffix(
            ".rst"
        )
        """Redirect to equipment.rst"""
        with target_rst_path.open("w") as target_file:
            with redirect_stdout(target_file):
                print(eq_tbl.title)
                print("=" * len(eq_tbl.title))
                print()
                eq_tbl.rst()
        print(f"Created {target_rst_path}")


if __name__ == "__main__":
    main()
