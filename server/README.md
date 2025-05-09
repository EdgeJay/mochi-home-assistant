# Mochi Home Assistant Python Server

This is the backend FastAPI server for the Mochi Home Assistant project.

## Features
- Modular FastAPI structure
- Health check endpoint (`/health`)
- Ready for extension with MCP tools, LangChain, and LLM runtime

## Setup

1. **Install dependencies** (Python 3.12+ recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```
3. **Run tests:**
   ```bash
   pytest
   ```

## Project Structure
```
server/
  main.py           # FastAPI entry point
  models.py         # Pydantic models
  routers/
    __init__.py
    health.py       # Health check route
  tests/
    test_health.py  # Pytest for health endpoint
  requirements.txt
```

## Next Steps
- Add MCP tool routers
- Integrate LangChain agent
- Implement STT and TTS interfaces
