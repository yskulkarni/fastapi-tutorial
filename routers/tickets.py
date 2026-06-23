import asyncio
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, status
from schemas import TicketRequest, TicketResponse, TicketDetails
from config import error_logs, tickets_storage

router = APIRouter(prefix="/tickets", tags=["Tickets"])

# --- 3. ASYNCHRONOUS SIMULATIONS ---
async def simulate_db_write(ticket: TicketRequest) -> int:
    """Simulates saving a ticket to a database asynchronously."""
    await asyncio.sleep(1.5)  # Yields control back to the event loop
    return len(tickets_storage) + 1  # Use list length + 1 as ticket ID

async def simulate_audit_service(ticket: TicketRequest):
    """Simulates an external audit notification that might fail."""
    await asyncio.sleep(0.5)
    if ticket.priority == 1:
        # Intentionally log an issue to demonstrate our deque data structure
        error_logs.append(f"High priority alert failed for {ticket.user_email}")

# --- 4. ENDPOINTS ---
@router.post(
    "", 
    response_model=TicketResponse, 
    status_code=status.HTTP_201_CREATED
)
async def create_ticket(payload: TicketRequest):
    """
    Creates a support ticket.
    FastAPI automatically validates 'payload' against the TicketRequest model.
    """
    # Run independent async tasks concurrently using asyncio.gather
    try:
        db_task = simulate_db_write(payload)
        audit_task = simulate_audit_service(payload)
        
        # Concurrently await both non-blocking operations
        ticket_id, _ = await asyncio.gather(db_task, audit_task)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Internal processing failed"
        )

    # Route ticket to specialized queues based on priority rules
    queue_name = "CRITICAL_EXEC" if payload.priority == 1 else "STANDARD_SUPPORT"

    # Store ticket in memory
    ticket_data = {
        "ticket_id": ticket_id,
        "title": payload.title,
        "description": payload.description,
        "user_email": payload.user_email,
        "priority": payload.priority,
        "assigned_queue": queue_name,
        "status": "Open",
        "created_at": datetime.now()
    }
    tickets_storage.append(ticket_data)

    return TicketResponse(
        ticket_id=ticket_id,
        title=payload.title,
        assigned_queue=queue_name,
        status="Open",
        created_at=ticket_data["created_at"]
    )

@router.get("", response_model=List[TicketDetails])
async def get_all_tickets():
    """
    Retrieves all stored tickets.
    Returns a list of all tickets created during the application lifetime.
    """
    return tickets_storage

@router.get("/{ticket_id}", response_model=TicketDetails)
async def get_ticket(ticket_id: int):
    """
    Retrieves a specific ticket by ID.
    """
    for ticket in tickets_storage:
        if ticket["ticket_id"] == ticket_id:
            return ticket
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Ticket with ID {ticket_id} not found"
    )
