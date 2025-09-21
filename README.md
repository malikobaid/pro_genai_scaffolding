# GenAI Scaffolding Pro

![CI](https://github.com/malikobaid/pro_genai_scaffolding/actions/workflows/ci.yml/badge.svg?branch=main)&nbsp;[![codecov](https://codecov.io/gh/malikobaid/pro_genai_scaffolding/branch/main/graph/badge.svg)](https://codecov.io/gh/malikobaid/pro_genai_scaffolding)

A production-ready scaffolding project for GenAI applications.  
This repo provides a clean, tested, and CI-integrated base for building agentic AI apps using LangGraph, FastAPI, and modern Python tooling.

## Features
- ✅ Structured project layout with `genai_scaffolding_pro/` package
- ✅ FastAPI API with `/health` and `/v1/agents/{name}/invoke`
- ✅ Pre-commit hooks (Black, Ruff, Mypy, Pytest)
- ✅ GitHub Actions CI with lint, type-check, tests, coverage, and Docker
- ✅ Codecov integration with 70% coverage threshold

## Getting Started
```bash
make setup     # create venv + install dependencies
make dev       # run FastAPI server locally
make test      # run test suite
make ci        # run all CI checks locally