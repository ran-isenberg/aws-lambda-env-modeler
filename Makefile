.PHONY: dev format format-fix lint complex pre-commit mypy-lint deps unit pipeline-tests docs lint-docs update-deps pr
VENV ?= .venv
PYTHON=$(VENV)/bin/python


dev:
	poetry config --local virtualenvs.in-project true
	poetry install
	poetry run pre-commit install


format:
	poetry run ruff check . --fix

format-fix:
	poetry run ruff format .


lint:
	poetry run mypy --pretty aws_lambda_env_modeler docs/snippets tests

complex:
	poetry run radon cc -e 'tests/*,cdk.out/*' .
	poetry run xenon --max-absolute A --max-modules A --max-average A -e 'tests/*,.venv/*,cdk.out/*' .

pre-commit:
	poetry run pre-commit run -a --show-diff-on-failure

deps:
	poetry export --with=dev --without-hashes --format=requirements.txt > lib_requirements.txt

unit:
	poetry run pytest tests/unit --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml

pr: deps pre-commit complex lint lint-docs unit


pipeline-tests:
	poetry run pytest tests/unit --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml

docs:
	poetry run mkdocs serve

lint-docs:
	docker run -v ${PWD}:/markdown 06kellyjac/markdownlint-cli --fix "docs"

update-deps:
	poetry update
	poetry run pre-commit autoupdate
