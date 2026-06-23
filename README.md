# FastAPI Tutorial

A comprehensive FastAPI application demonstrating core concepts including asynchronous operations, request validation with Pydantic, error handling, and system diagnostics.

## Project Overview

This project showcases:
- **Advanced FastAPI Concepts**: Routing, middleware, dependency injection
- **Asynchronous Programming**: Async/await patterns for non-blocking I/O operations
- **Data Validation**: Pydantic models for request/response validation with email support
- **API Organization**: Modular routing with separate routers for different domains
- **Error Handling**: Comprehensive error logging and status tracking
- **System Diagnostics**: Health checks and error monitoring endpoints

## API Endpoints

### Tickets (`/tickets`)
- Create, retrieve, and manage support tickets
- Async database and audit service simulations
- Email validation for ticket submissions

### System (`/system`)
- Monitor recent critical errors
- System diagnostics and health status

## Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)
- Docker (optional, for containerized deployment)

## Local Setup

### Using uv (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yskulkarni/fastapi-tutorial.git
   cd fastapi-tutorial
   ```

2. **Install dependencies with uv**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r pyproject.toml
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Interactive API Documentation

Once the server is running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Running with Docker

### Build the Docker Image

```bash
docker build -t fastapi-tutorial .
```

### Run the Container

```bash
docker run -p 8000:8000 fastapi-tutorial
```

The application will be accessible at `http://localhost:8000`

## Development

### Install Development Dependencies

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov
```

## Project Structure

```
.
├── main.py              # FastAPI application entry point
├── config.py            # Configuration and shared state
├── schemas.py           # Pydantic data models
├── conftest.py          # Pytest configuration
├── test_main.py         # Test suite
├── routers/
│   ├── __init__.py
│   ├── tickets.py       # Tickets API endpoints
│   └── system.py        # System diagnostics endpoints
├── Dockerfile           # Docker configuration
├── .dockerignore         # Docker build exclusions
├── pyproject.toml       # Project metadata and dependencies
└── README.md            # This file
```

## Dependencies

### Main Dependencies
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation using Python type annotations

### Development Dependencies
- **pytest**: Testing framework
- **httpx**: Async HTTP client for testing
- **anyio**: Async compatibility layer

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
