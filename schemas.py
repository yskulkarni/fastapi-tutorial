from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# --- 2. TYPE VALIDATION (Pydantic Models) ---
class TicketRequest(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str
    user_email: EmailStr
    priority: int = Field(default=3, ge=1, le=5) # Priority must be between 1 and 5

class TicketResponse(BaseModel):
    ticket_id: int
    title: str
    assigned_queue: str
    status: str
    created_at: datetime

class TicketDetails(BaseModel):
    ticket_id: int
    title: str
    description: str
    user_email: str
    priority: int
    assigned_queue: str
    status: str
    created_at: datetime