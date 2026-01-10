"""
Extract OpenD6 WordPress Content to local cache and parse to create RST
"""

from collections.abc import Iterator
from pathlib import Path
import random
import time
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel


class Topic(BaseModel):
    text: str
    url: str
    children: list["Topic"]
    list_item_id: str | None = None


def toc_walk(base: Tag) -> Iterator[Topic]:
    if not base:  # Not even a tag. What?
        return []
    if base.name != "ul":
        print(base.name, base.attrs)
        return []
    for item in base.find_all("li", recursive=False):
        yield Topic(
            text=item.a.text,
            url=item.a.attrs["href"],
            children=list(toc_walk(item.ul)),
            list_item_id=item.attrs["id"],
        )


def toc_dump(base: list[Topic], depth: int = 0) -> None:
    for item in base:
        indent = "#" * (depth + 1)
        print(indent, item.text, item.url)
        toc_dump(item.children, depth + 1)


INDEX = Path.cwd().parent / "source" / Path("index.json")
BASE_URL = "https://opend6project.wordpress.com"


def get_index(base_url: str = BASE_URL) -> None:
    """Main App to get index prior to getting articles."""
    with urllib.request.urlopen(base_url) as source:
        if source.status == 200:
            doc = BeautifulSoup(source.read(), "html.parser")
        else:
            print(source)
    nav = doc.body.find("nav", class_="secondary-navigation")

    # Do a recursive traversal of the <ul> tag structure to create proper (<a>, [...]) navigation
    # print(nav.prettify())
    menu = Topic(text="OpenD6", url="", children=list(toc_walk(nav.ul)))
    INDEX.write_text(menu.model_dump_json(indent=2))


def dump_index() -> None:
    """Main App to dump the index structure."""
    menu = Topic.model_validate_json(INDEX.read_text())
    toc_dump(menu.children)


def flatten_index(topic: Topic) -> Iterator[Topic]:
    """Flatten the index hierarchy"""
    yield topic
    for child in topic.children:
        yield from flatten_index(child)


def tocreee_index(topic: Topic, parents: tuple[str, ...] = ()) -> None:
    if topic.children:
        if topic.url:
            print("    ", parents, "index")
        for child in topic.children:
            tocreee_index(child, parents=parents + (child.text,))
    else:
        print("    ", parents, topic.text)


CACHE = Path.cwd().parent / "source" / "cache"


def local_name(url: str) -> Path:
    url_parsed = urllib.parse.urlparse(url)
    cache_path = CACHE / Path(url_parsed.path).relative_to("/")
    if url_parsed.path.endswith("/"):
        cache_path = cache_path / "index.html"
    return cache_path


def get_article(title: str, url: str) -> None:
    """App to get an article either from cache or from the site.
    Populates local cache.
    """
    cache_path = local_name(url)
    print(f"Fetching {url} -> {cache_path}")

    if not cache_path.exists():
        with urllib.request.urlopen(url) as source:
            if source.status == 200:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_bytes(source.read())
            else:
                print(source)
                raise IOError(f"Could not read {url}")


def get_all() -> None:
    index = Topic.model_validate_json(INDEX.read_text())
    for topic in flatten_index(index):
        if topic.url:
            print(topic.text)
            get_article(topic.text, topic.url)
            # Rate limit...
            pause = random.random() * 2
            time.sleep(pause)


def inline_rewrite(tag: Tag) -> str:
    """Convert inline HTML into RST"""
    if not tag.name:
        # Navigable String. Boom. Done.
        return tag.string
    elif tag.name in {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"}:
        content = "".join(inline_rewrite(c) for c in tag.children)
        return content
    elif tag.name in {"strong", "b"}:
        content = "".join(inline_rewrite(c) for c in tag.children)
        return f"**{content}**"
    elif tag.name in {"emphasis", "i", "em"}:
        content = "".join(inline_rewrite(c) for c in tag.children)
        return f"*{content}*"
    elif tag.name == "a":
        content = "".join(inline_rewrite(c) for c in tag.children)
        href = tag.attrs["href"]
        return f"`{content} <{href}>`_"
    elif tag.name == "img":
        src = tag.attrs["src"]
        alt = tag.attrs.get("alt", "")
        return f"\n..  image:: {src}\n    :alt: {alt}\n"
    elif tag.name == "br":
        return "\n"
    elif tag.name == "span":
        return "".join(inline_rewrite(c) for c in tag.children)
    else:
        raise ValueError(tag)


def structure_rewrite(content: Tag, prefix: str = "") -> None:
    """
    Walk the HTML structure.

    -   Skip some <div id=...> and <span> that seem to be Wordpress-ism.

    -   Find <h?> headings and transform to RST headings.

    -   Find <p> and unwind the text.

    -   Expand <table>

    -   Walk the <ul> and <ol> hierarchies.

    -   There are some <figure> items, perhaps.
    """
    HEADING = {
        "h1": "#",
        "h2": "=",
        "h3": "-",
        "h4": "~",
        "h5": "^",
        "h6": "+",
        "h7": "*",
        "h8": ".",
    }
    for item in content.children:
        if item.name is None and (text := item.text.strip()):
            print(text)
        elif item.name is not None:
            if item.name == "div" and set(item.attrs.keys()) == {"id"}:
                # Some WordPress thing
                continue
            elif item.name == "span" and "display: none" in item.attrs.get("style", ""):
                # Some WordPress thing
                continue
            elif item.name in {"p", "li"}:
                print(prefix, inline_rewrite(item))
            elif item.name in {"h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"}:
                title = inline_rewrite(item)
                print(title)
                print(HEADING[item.name] * len(title))
                print()
            elif item.name == "table":
                tbody = item.tbody
                all_rows = [
                    [col.text.strip() for col in row.find_all("td", recursive=False)]
                    for row in tbody.find_all("tr", recursive=False)
                ]
                print(prefix, all_rows)
            elif item.name == "ul":
                # Recursive descent into structure_rewrite(item)
                # Each item gets an RST prefix.
                structure_rewrite(item, prefix=prefix + "-   ")
            elif item.name == "ol":
                # Recursive descent into structure_rewrite(item)
                # Each item gets an RST prefix.
                structure_rewrite(item, prefix=prefix + "#.  ")
            elif item.name == "figure":
                # A floating thing, often a <table>.
                print(prefix, f".. figure: {item.attrs}")
                for c in item.children:
                    structure_rewrite(item, prefix=prefix)
            elif item.name == "span":
                print(inline_rewrite(item))
            else:
                raise ValueError(item)
                print(f"<{item.name} {item.attrs}>", item.text, f"</{item.name}>")
            print()


def parse_article(title: str, url: str, depth: int = 0) -> None:
    cache_path = local_name(url)
    doc = BeautifulSoup(cache_path.read_bytes(), "html.parser")

    article = doc.body.article
    title = article.header.h1.text
    print("#" * len(title))
    print(title)
    print("#" * len(title))
    print()
    content = article.div

    # print(content.prettify())
    structure_rewrite(content)


if __name__ == "__main__":
    # get_index()
    # dump_index()
    # get_all()

    index = Topic.model_validate_json(INDEX.read_text())

    # Create an RST doc hierarchy. The index tree defines a ``..  toctree::`` hierarchy.
    print("..  toctree::")
    print("")
    tocreee_index(index)

    # for topic in flatten_index(index):
    #     if topic.url:
    #         parse_article(topic.text, topic.url)
