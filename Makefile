install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff
	poetry run flake8 formatters
	poetry run flake8 tests

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
