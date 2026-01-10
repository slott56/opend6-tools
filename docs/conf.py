# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd().parent.resolve()))
sys.path.insert(0, str((Path.cwd().parent / "src").resolve()))

project = "OpenD6 Tools"
copyright = "2025, S.Lott"
author = "S.Lott"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinxcontrib.plantuml",
]

plantuml = f"java -jar {Path.cwd().parent}/plantuml-gplv2-1.2025.7.jar"

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

html_theme_options = {"globaltoc_maxdepth": 5}

# -- Options for intersphinx ------

intersphinx_mapping = {
    "fantasy": (
        "../../../../world/fantasy_rulebook/_build/html/",
        ("../../world/fantasy_rulebook/_build/html/objects.inv", None),
    ),
    "magic_guide": (
        "../../../../world/magic_guide/_build/html/",
        ("../../world/magic_guide/_build/html/objects.inv", None),
    ),
}

# -- Options for coverage --

coverage_show_missing_items = True
coverage_statistics_to_stdout = True

# -- Options for Alabaster HTML --

html_sidebars = {
   'tutorial': ['about.html','relations.html','searchfield.html',
        'navigation.html'],
   '**': [
        'about.html',
        'relations.html',
        'searchfield.html',
        'navigation.html',
        # 'sourcelink.html'
    ],
}
