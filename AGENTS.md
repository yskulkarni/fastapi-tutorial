# AI Agent Instructions

This repository is a small FastAPI service with an in-memory ticket system.

## Key files

- `main.py` — FastAPI application entrypoint. Includes routers for tickets and system diagnostics.
- `routers/tickets.py` — Ticket creation and retrieval endpoints.
- `routers/system.py` — System diagnostics endpoint for recent error logs.
- `schemas.py` — Pydantic models for request and response validation.
- `config.py` — In-memory application state: `tickets_storage` and `error_logs`.
- `conftest.py` — Pytest fixtures and test state reset logic.
- `Dockerfile` / `.dockerignore` — Docker build configuration.

## Technology stack

- Python `>=3.14`
- FastAPI
- Pydantic
- Uvicorn
- `uv` package manager
- pytest / httpx for tests

## Recommended workflow

1. Install dependencies
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r pyproject.toml
   ```
2. Run locally
   ```bash
   uvicorn main:app --reload
   ```
3. Run tests
   ```bash
   pytest -v
   ```

## Important conventions

- The service uses in-memory data structures, not a database.
- Ticket state is stored in `config.tickets_storage`.
- Error history is stored in `config.error_logs` as a fixed-size deque.
- Tests use HTTPX `AsyncClient` with `ASGITransport` against `main.app`.
- Avoid assuming a globally available `python` command; use `.venv/bin/python` or `uv`.

## Useful links

- README: [README.md](README.md)

## When working in this repo

- Keep API changes consistent with existing router structure.
- Preserve the current in-memory state model unless a user explicitly asks to replace it.
- Prefer small, testable changes.
