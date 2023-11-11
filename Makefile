.PHONY: dev lint complex coverage pre-commit yapf sort deps unit pipeline-tests docs lint-docs



dev:
	pip install --upgrade pip pre-commit poetry
	pre-commit install
	poetry config --local virtualenvs.in-project true
	poetry install

format:
	poetry run ruff check . --fix

format-fix:
	poetry run ruff format .


lint:
	@echo "Running mypy"
	make mypy-lint

complex:
	@echo "Running Radon"
	radon cc -e 'tests/*,cdk.out/*' .
	@echo "Running xenon"
	xenon --max-absolute A --max-modules A --max-average A -e 'tests/*,.venv/*,cdk.out/*' .

pre-commit:
	pre-commit run -a --show-diff-on-failure

mypy-lint:
	mypy --pretty aws_lambda_env_modeler docs/snippets tests

deps:
	poetry export --with=dev --without-hashes --format=requirements.txt > lib_requirements.txt

unit:
	pytest tests/unit  --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml


pr: deps pre-commit complex lint lint-docs unit


pipeline-tests:
	pytest tests/unit  --cov-config=.coveragerc --cov=aws_lambda_env_modeler --cov-report xml


docs:
	mkdocs serve

lint-docs:
	docker run -v ${PWD}:/markdown 06kellyjac/markdownlint-cli --fix "docs"

update-deps:
	poetry update
	pre-commit autoupdate
