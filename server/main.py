# Entry point for FastAPI server
from fastapi import FastAPI
from routers import health

app = FastAPI(title="Mochi Home Assistant Server")

# Include routers
app.include_router(health.router)
