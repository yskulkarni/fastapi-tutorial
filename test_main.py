import pytest 
from httpx import AsyncClient

@pytest.mark.anyio
async def test_create_ticket_success(client: AsyncClient):
    """Validates that a correctly formatted request yields a 201 status."""
    payload = {
        "title": "System connection failure",
        "description": "Database connection timing out after 30 seconds.",
        "user_email": "dev_ops@company.com",
        "priority": 3
        }
    
    response = await client.post("/tickets", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data["ticket_id"], int) and data["ticket_id"] > 0
    assert data["assigned_queue"] == "STANDARD_SUPPORT"
    assert data["status"] == "Open"
    assert "created_at" in data
        
@pytest.mark.anyio
async def test_create_ticket_validation_trigger(client: AsyncClient):
    """Validates that Pydantic properly blocks structurally invalid payloads."""
    invalid_payload = {
        "title": "Shor",  # Fails min_length=5
        "description": "Missing a valid email format",
        "user_email": "bad_email_string",  # Fails EmailStr
        "priority": 99  # Fails le=5
        }
    
    response = await client.post("/tickets", json=invalid_payload)
    assert response.status_code == 422  # Unprocessable Entity
    errors = response.json()["detail"]
    assert len(errors) == 3  # Triggers 3 validation errors
            
@pytest.mark.anyio
async def test_priority_queue_and_deque_logging(client: AsyncClient):
    """Validates priority routing and in-memory queue max length limits."""
    high_priority_payload = {
        "title": "Critical pipeline down",
        "description": "Production deploy failing.",
        "user_email": "lead_engineer@company.com",
        "priority": 1
        }
    
    # Trigger the condition that populates the deque error log
    response = await client.post("/tickets", json=high_priority_payload)
    assert response.status_code == 201
    assert response.json()["assigned_queue"] == "CRITICAL_EXEC"

    # Verify the log endpoint registers the event
    log_response = await client.get("/system/errors")
    assert log_response.status_code == 200
    assert len(log_response.json()) == 1
    assert "lead_engineer@company.com" in log_response.json()[0]