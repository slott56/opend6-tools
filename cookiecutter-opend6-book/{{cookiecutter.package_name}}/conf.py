# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter.year }}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"
release = "{{ cookiecutter.calver_version }}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store",
    "LICENSE*",
    "make.bat",
    "Makefile",
    "conf.py",
    "un.lock",
    "pyproject.toml",
    "*.tex",
    "*.ods",
    ".venv",
    "notebooks/*"
]

rst_prolog = """
.. |use_opend6| replace:: The **OpenD6 Fantasy** rules can be used without modification.

.. |mod_opend6| replace:: Generally, the **OpenD6 Fantasy** rules can be used with some modifications.

.. |no_opend6| replace:: The **OpenD6 Fantasy** rules are incompatible with this world, and should not be used.

"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

html_sidebars = {
    "**": [
        "about.html",
        "searchfield.html",
        "navigation.html",
        "relations.html",
    ]
}

html_theme_options = {
    "show_related": True,
    "extra_nav_links": {"Home": "../../../home_page/index.html"},
}

# -- Options for intersphinx ------

intersphinx_mapping = {
    # "book": ("/path/to/_build/html", ("/path/to/_build/html/objects.inv", None)),
    # ...
}

