# Items Makefile
.PHONY: items

vpath %.ipynb ../notebooks

# Create a Python Items module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells --book-variable items $< > $@

# Special case for swords, each notebook must be listed separately.
swords.py : swords.ipynb
	python -m opend6_tools.notebook_extract characters --book-variable swords $< > $@

# Create an RST text file from a Python Spell module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

# Special cases for swords
swords.txt : swords.py
	python $< display --format SHORT > $@

# The list of all *.txt files with items or swords.
ALL_ITEMS =

items : $(ALL_ITEMS)

.PRECIOUS : %.py
