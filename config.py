from collections import deque

# --- 1. DATA STRUCTURES (In-Memory State) ---
# Keep a fixed-size history of the last 3 critical error messages
error_logs = deque(maxlen=3)