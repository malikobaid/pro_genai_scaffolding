# GenAI Scaffolding Pro

![CI](https://github.com/malikobaid/pro_genai_scaffolding/actions/workflows/ci.yml/badge.svg?branch=main) &nbsp;
[![codecov](https://codecov.io/gh/malikobaid/pro_genai_scaffolding/branch/main/graph/badge.svg)](https://codecov.io/gh/malikobaid/pro_genai_scaffolding)

A production-ready scaffolding project for GenAI applications.
This repo provides a clean, tested, and CI-integrated base for building agentic AI apps using LangGraph, FastAPI, and modern Python tooling.

## Features
- Structured package layout (`genai_scaffolding_pro/`)
- FastAPI API with `/health` and `/v1/agents/{name}/invoke`
- Minimal graph runner (plan → act → verify)
- Tests + coverage, Codecov OIDC, Dockerfile, Makefile
- Pre-commit (Black, Ruff, Mypy), unified `pyproject.toml`
- Config via `.env` and `config.py`

## Getting Started
```bash
make setup
make dev
curl -s http://localhost:8000/health
make ci
```

## Configuration
Copy `.env.example` to `.env` and set secrets. Defaults live in `genai_scaffolding_pro/config.py`.
