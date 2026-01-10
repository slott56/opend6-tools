# Make opend6 tools
.PHONY : test type docs build coverage

test :
	uv tool run tox run
	uv tool run ruff check src --ignore E741,F405
	cd docs && ${MAKE} doctest

type : test
	uv tool run tox run -e type

docs :
	cd docs && ${MAKE} html

build :
	rm -f dist/*.gz dist/*.whl
	uv tool run ruff format src --line-length 100
	uv build

coverage :
	cd docs && ${MAKE} coverage
