..  _notebook_extract_app:

######################################
``notebook_extract`` app
######################################

Spells and Characters (as well as Creatures) are defined in Python modules.
This makes testing and publication relatively straightforward.

However, making changes to a module and considering the consequences of those changes is easier in Jupyter Lab.
This extends the build process slightly by introducing the :py:mod:`opend6_tools.notebook_extract` application.

This application pulls Spell (or Invocation) definitions from a notebook.
Or, with a separate command-line argument, pulls Character and Creature definitions from a notebook.
The definitions from a notebook are organized into a module, with a CLI application included.

..  uml::

    @startuml
    'https://plantuml.com/class-diagram

    title Campaign Documents When Using Jupyter Lab

    package python {
        package opend6_tools {
            component magic2.py <<lib>>
            component character.py <<lib>>
            component notebook_extract.py <<app>>
        }
    }

    package document_source {
        artifact magic.rst <<RST>>
        artifact character_templates.rst <<RST>>
        package spells {
            component spells_subsection.py <<app>> {
                component Spell
            }
            artifact spells_subsection.txt <<RST>>
            spells_subsection.py ..> magic2.py : import
        }
        spells_subsection.txt <- spells_subsection.py : Creates
        magic.rst --> spells_subsection.txt : """include::"" directive"

        package characters {
            component template_character.py <<app>> {
                component Character
            }
            artifact template_character.txt <<RST>>
            template_character.py ..> character.py : import
        }
        template_character.txt <- template_character.py : Creates
        character_templates.rst --> template_character.txt : """include::"" directive"
    }

    package notebooks {
        artifact spells_subsection.ipynb <<Notebook>> {
            component Spell
        }
        spells_subsection.ipynb ..> magic2.py : import
        artifact template_character.ipynb <<Notebook>> {
            component Character
        }
        template_character.ipynb ..> character.py : import
    }

    notebook_extract.py --> spells_subsection.ipynb : "Reads"
    notebook_extract.py --> spells_subsection.py : "Writes"

    notebook_extract.py --> template_character.ipynb : "Reads"
    notebook_extract.py --> template_character.py : "Writes"


    @enduml

Implementation
==============

..  automodule:: opend6_tools.notebook_extract

