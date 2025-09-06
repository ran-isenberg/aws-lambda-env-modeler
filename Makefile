.PHONY: dev format format-fix lint complex pre-commit mypy-lint deps unit pipeline-tests docs lint-docs update-deps pr push-docs
VENV ?= .venv
PYTHON=$(VENV)/bin/python


dev:
	uv sync --frozen

format:
	uv run ruff check . --fix

format-fix:
	uv run ruff format .

lint:
	uv run mypy --pretty aws_lambda_env_modeler docs/snippets tests

complex:
	uv run radon cc -e 'tests/*,cdk.out/*' .
	uv run xenon --max-absolute A --max-modules A --max-average A -e 'tests/*,.venv/*,cdk.out/*' .

pre-commit:
	uv run pre-commit run -a --show-diff-on-failure

deps:
	uv pip compile pyproject.toml --group dev > lib_requirements.txt

unit:
	uv run pytest tests/unit --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml

pr: deps pre-commit complex lint lint-docs unit


pipeline-tests:
	uv run pytest tests/unit --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml

docs:
	uv run mkdocs serve

lint-docs:
	docker run -v ${PWD}:/markdown 06kellyjac/markdownlint-cli --fix "docs"

update-deps:
	uv lock --upgrade
	uv run pre-commit autoupdate
	uv pip freeze > requirements.txt

push-docs:
	uv run mkdocs gh-deploy --force
