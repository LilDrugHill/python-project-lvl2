publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff
	poetry run flake8 stylish
	poetry run flake8 plain

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
