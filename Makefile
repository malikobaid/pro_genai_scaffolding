# Use project-local virtual environment
VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

PKG := genai_scaffolding_pro
TESTS := tests

.PHONY: help
help:
	@echo "Targets:"
	@echo "  setup           Create .venv and install deps"
	@echo "  lint            Run ruff and black in check mode"
	@echo "  fmt             Auto-format with black and ruff"
	@echo "  typecheck       Run mypy type checks"
	@echo "  test            Run pytest"
	@echo "  dev             Run API locally with reload"
	@echo "  cli             Run CLI chat once (example)"
	@echo "  ingest-sample   Ingest sample docs into local vector DB"
	@echo "  docker-build    Build local Docker image"
	@echo "  docker-run      Run container locally"
	@echo "  lambda-package  Build Lambda zip for serverless deploy"
	@echo "  clean           Remove build artifacts and .venv"


.PHONY: ci
ci:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .
	$(VENV)/bin/mypy genai_scaffolding_pro || true
	$(VENV)/bin/pytest \
		--cov=genai_scaffolding_pro \
		--cov-report=term-missing \
		--cov-fail-under=70 \
		--maxfail=1 --disable-warnings

.PHONY: clean
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info __pycache__

.PHONY: rebuild
rebuild: clean
	rm -rf .venv
	make setup
	pre-commit install
	pre-commit run --all-files

# Create venv and install dependencies
.PHONY: setup
setup:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: lint
lint:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .

.PHONY: fmt
fmt:
	$(VENV)/bin/black .
	$(VENV)/bin/ruff check . --fix

.PHONY: typecheck
typecheck:
	$(VENV)/bin/mypy $(PKG) || true

.PHONY: test
test:
	$(VENV)/bin/pytest -q

.PHONY: dev
dev:
	$(PY) -m $(PKG).api.server

.PHONY: cli
cli:
	$(PY) -m $(PKG).cli.chat --agent researcher --input "Test run"

.PHONY: ingest-sample
ingest-sample:
	$(PY) -m $(PKG).rag.ingest --path ./docs --namespace demo

.PHONY: docker-build
docker-build:
	docker build -t genai-scaffolding:local .

.PHONY: docker-run
docker-run:
	docker run --rm -p 8000:8000 -e ENV=local genai-scaffolding:local

.PHONY: lambda-package
lambda-package:
	./scripts/package_lambda.sh

.PHONY: hooks
hooks:
	$(PIP) install pre-commit
	pre-commit install
	pre-commit run --all-files