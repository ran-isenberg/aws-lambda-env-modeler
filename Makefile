.PHONY: dev lint complex coverage pre-commit yapf sort deps unit pipeline-tests docs lint-docs



dev:
	pip install --upgrade pip pre-commit poetry
	pre-commit install
	poetry config --local virtualenvs.in-project true
	poetry install

lint:
	@echo "Running flake8"
	flake8 aws_lambda_env_vars_parser/* tests/* docs/examples/* --exclude patterns='build,cdk.json,cdk.context.json,.yaml'
	@echo "Running mypy"
	make mypy-lint

complex:
	@echo "Running Radon"
	radon cc -e 'tests/*,cdk.out/*' .
	@echo "Running xenon"
	xenon --max-absolute A --max-modules A --max-average A -e 'tests/*,.venv/*,cdk.out/*' .

sort:
	isort ${PWD}

pre-commit:
	pre-commit run -a --show-diff-on-failure

mypy-lint:
	mypy --pretty aws_lambda_env_vars_parser docs/examples tests

deps:
	poetry export --with=dev --without-hashes --format=requirements.txt > lib_requirements.txt

unit:
	pytest tests/unit  --cov-config=.coveragerc --cov=aws_lambda_env_vars_parser --cov-report xml


pr: deps yapf sort pre-commit complex lint lint-docs unit

yapf:
	yapf -i -vv --style=./.style --exclude=.venv --exclude=.build --exclude=cdk.out --exclude=.git  -r .

pipeline-tests:
	pytest tests/unit  --cov-config=.coveragerc --cov=aws_lambda_env_vars_parser --cov-report xml


docs:
	mkdocs serve

lint-docs:
	docker run -v ${PWD}:/markdown 06kellyjac/markdownlint-cli --fix "docs"
