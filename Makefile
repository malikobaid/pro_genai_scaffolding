VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

PKG := genai_scaffolding_pro

.PHONY: help
help:
	@echo "Targets: setup, fmt, lint, typecheck, test, dev, ci, docker-build, docker-run, clean, rebuild"

.PHONY: setup
setup:
	python3 -m venv $(VENV)
	$(PY) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: fmt
fmt:
	$(VENV)/bin/black .
	$(VENV)/bin/ruff check . --fix

.PHONY: lint
lint:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .

.PHONY: typecheck
typecheck:
	$(VENV)/bin/mypy $(PKG) || true

.PHONY: test
test:
	PYTHONPATH=. $(VENV)/bin/pytest -q

.PHONY: dev
dev:
	$(PY) -m $(PKG).api.server

.PHONY: ci
ci:
	$(VENV)/bin/ruff check .
	$(VENV)/bin/black --check .
	$(VENV)/bin/mypy $(PKG) || true
	PYTHONPATH=. $(VENV)/bin/pytest \
		--cov=$(PKG) \
		--cov-report=term-missing \
		--cov-fail-under=70 \
		--maxfail=1 --disable-warnings

.PHONY: docker-build
docker-build:
	docker build -t genai-scaffolding:local .

.PHONY: docker-run
docker-run:
	docker run --rm -p 8000:8000 genai-scaffolding:local

.PHONY: clean
clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info __pycache__

.PHONY: rebuild
rebuild: clean
	rm -rf .venv
	make setup
	$(PIP) install pre-commit
	$(VENV)/bin/pre-commit install
	$(VENV)/bin/pre-commit run --all-files
