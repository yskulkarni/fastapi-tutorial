# GitHub Copilot Instructions

This repository is a small FastAPI service focused on tickets and system diagnostics.

## What to know

- Entry point: `main.py`
- Ticket logic: `routers/tickets.py`
- System diagnostics: `routers/system.py`
- Shared in-memory state: `config.py`
- Validation models: `schemas.py`
- Tests use `pytest`, `httpx.AsyncClient`, and `ASGITransport`
- The project relies on `uv` for dependency management and recommends using the local virtual environment from `.venv`

## Common patterns

- Keep state in memory rather than adding a database unless explicitly requested.
- Add new API behavior as router endpoints.
- Preserve the existing FastAPI router structure and Pydantic models.
- Clear `error_logs` and `tickets_storage` between tests via `conftest.py`.

## How to run

- Install dependencies:
  ```bash
  uv venv
  source .venv/bin/activate
  uv pip install -r pyproject.toml
  uv run pre-commit install
  ```
- Run locally:
  ```bash
  uvicorn main:app --reload
  ```
- Run tests:
  ```bash
  pytest -v
  ```
