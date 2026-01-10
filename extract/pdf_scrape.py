"""
Scrape text from PDF source documnts.


1.  PDF -> Text. This application.

2.  Text to more useful RST has to be done more-or-less manually.
    Some automated parsing is possible for structured data like spells.
"""

from contextlib import redirect_stdout
from pathlib import Path
from pypdf import PdfReader


def text_from_pdf(source: Path) -> None:
    reader = PdfReader(source)

    print("..  toctree::")
    for item in reader.outline:
        match item:
            case dict():
                print("    ", item["/Title"])
            case list() as sublist:
                for subitem in sublist:
                    print("    - ", subitem["/Title"])
    print()

    for page_number in range(1, reader.get_num_pages()):
        page = reader.pages[page_number]
        print(page.extract_text())


def main():
    # source = Path.cwd().parent / "source" / "D6_Magic_weg51024OGL.pdf"
    source = Path.cwd().parent / "source" / "D6_Fantasy_v1.3_weg51013OGL.pdf"
    target = source.with_suffix(".rst")
    with target.open("w") as target_file:
        with redirect_stdout(target_file):
            text_from_pdf(source)


if __name__ == "__main__":
    main()
