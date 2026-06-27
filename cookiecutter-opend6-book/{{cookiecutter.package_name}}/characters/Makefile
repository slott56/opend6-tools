# Characters and Creatures Makefile
.phony: characters

vpath %.ipynb ../notebooks

# Create a Python Character or Creature module from a Jupyter Notebook with the same name.
%.py : %.ipynb
	python -m opend6_tools.notebook_extract characters $< > $@

# Create an RST text file from a Python Character or Creature module with the same name.
%.txt : %.py
	python $< test
	python $< display --format SHORT > $@

# The list of all *.txt files with characters or creatures.
ALL_CHARACTERS =

characters : $(ALL_CHARACTERS)

.PRECIOUS : %.py
