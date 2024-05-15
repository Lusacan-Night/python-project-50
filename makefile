install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

build:
	poetry build

run:
	poetry run gendiff file1.json file2.json

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

pipx-install:
	pipx install . --force