# Make opend6 tools
.PHONY : test type docs build coverage

test :
	uv tool run tox run
	uv tool run ruff check src --ignore E741,F405,F403,E731
	uv tool run tox run -e docs

type : test
	uv tool run tox run -e type

docs :
	uv sync --dev
	cd docs && ${MAKE} html

build :
	rm -f dist/*.gz dist/*.whl
	uv tool run ruff format src --line-length 100
	uv build

doc-coverage :
	uv sync --dev
	cd docs && ${MAKE} coverage

coverage :
	uv sync --active --dev
	coverage erase
	coverage run --append --source=opend6_tools -m pytest -x tests
	coverage run --append --source=opend6_tools -m pytest --doctest-modules src/opend6_tools
	coverage report -m

