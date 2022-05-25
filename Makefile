publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
