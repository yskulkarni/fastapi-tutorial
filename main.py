from fastapi import FastAPI
from routers import tickets, system


app = FastAPI(title="Advanced Core Concepts API")
app.include_router(tickets.router)
app.include_router(system.router)

@app.get("/")
def read_root():
    return {"status": "Application is healthy and routing traffic"}





