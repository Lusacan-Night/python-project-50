install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build:
	poetry build

run:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

pipx-install:
	pipx install . --force