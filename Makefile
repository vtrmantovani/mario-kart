VERSION := 1.0.0


clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml

test: clean
	nosetests -s --rednose

coverage: clean
	nosetests --with-coverage --cover-package=mkart

requirements-dev:
	pip install -r requirements-dev.txt

requirements-test:
	pip install -r requirements-test.txt

lint: flake8 check-python-import

flake8:
	@flake8 --show-source  --exclude docs .

check-python-import:
	@isort --check --skip docs/

isort:
	@isort

outdated:
	pip list --outdated

run-docs:
	mkdocs serve

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major