from fastapi import APIRouter
from config import error_logs
from typing import List

router = APIRouter(prefix="/system", tags=["System Diagnostics"])

@router.get("/errors", response_model=List[str])
async def get_recent_errors():
    """
    Retrieves the fixed-size queue of recent critical errors.
    Returns a maximum of 3 items due to deque constraints.
    """
    return list(error_logs)

