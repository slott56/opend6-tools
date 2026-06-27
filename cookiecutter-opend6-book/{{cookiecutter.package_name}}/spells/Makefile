# Spells Makefile
.PHONY: spells invocations test

vpath %.ipynb ../notebooks

# Create a Python Spell module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract spells $< > $@

# Create an RST text file from a Python Spell module with the same name.
%.txt : %.py
	# pytest --doctest-modules $<
	python $< test
	python $< display > $@

# The list of all *.txt files with spells or invocations.
ALL_SPELLS =
ALL_INVOCATIONS =

spells : $(ALL_SPELLS) $(ALL_INVOCATIONS)

.PRECIOUS : %.py
