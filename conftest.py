import pytest 
from httpx import AsyncClient, ASGITransport 
from main import app
from config import error_logs, tickets_storage

@pytest.fixture
def anyio_backend():
    """Defines the backend engine for running asynchronous tests globally."""
    return "asyncio"

@pytest.fixture(autouse=True)
def clear_state():
    error_logs.clear()
    tickets_storage.clear()

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac  # Hand over control to the test function, then clean up after
