from collections import deque
from typing import List, Dict, Any

# --- 1. DATA STRUCTURES (In-Memory State) ---
# Keep a fixed-size history of the last 3 critical error messages
error_logs = deque(maxlen=3)

# In-memory storage for tickets
tickets_storage: List[Dict[str, Any]] = []