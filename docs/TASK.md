# Initial Project Tasks

## Setup & Infrastructure

1. **Project Repository Setup**
   - [ ] Initialize Git repository
   - [ ] Define branch strategy (main, dev, feature branches)
   - [ ] Create `.gitignore` for Python, SvelteKit, and model files
   - [ ] Write initial `README.md`

2. **Backend Environment**
   - [ ] Create Python 3.12 virtual environment
   - [ ] Install and pin core dependencies:
     - [ ] LangChain
     - [ ] langchain-mcp-adapters
     - [ ] fastmcp
     - [ ] whisper.cpp wrapper
     - [ ] TTS engine (Piper or Coqui TTS)
   - [ ] Set up basic backend scaffolding
   - [ ] Write `requirements.txt` with pinned versions

3. **LLM Runtime**
   - [ ] Install `llama.cpp` or `Ollama`
   - [ ] Download and configure quantized model (e.g. TinyLlama or Phi-2)
   - [ ] Validate model startup and local inference capability

## Backend Development

4. **Speech-to-Text Pipeline**
   - [ ] Integrate microphone input using `whisper.cpp`
   - [ ] Build STT interface script for live transcription
   - [ ] Normalize and prepare text for LLM

5. **LangChain + MCP Integration**
   - [ ] Define MCP tool spec for `AddCalendarEvent` and `ControlDevice`
   - [ ] Create MCP server (`calendar_mcp_server.py`) with fastmcp
   - [ ] Implement LangChain agent with MCP tool loading
   - [ ] Test tool invocation via prompt

6. **Text-to-Speech Pipeline**
   - [ ] Configure local TTS using Piper or Coqui
   - [ ] Route LLM response to TTS engine
   - [ ] Output voice to connected speaker

7. **Task Orchestration**
   - [ ] Combine STT → LLM → MCP → TTS pipeline
   - [ ] Use asyncio or threading for non-blocking voice loop
   - [ ] Handle failure recovery and restarts

## Frontend Development

8. **Dashboard Interface (SvelteKit)**
   - [ ] Initialize SvelteKit app
   - [ ] Build voice activity log viewer
   - [ ] Create UI for manually invoking tasks (e.g., add calendar entry)
   - [ ] Add kiosk-mode dashboard support

9. **Tool Configuration Panel**
   - [ ] Add settings page for calendar and smart home tools
   - [ ] Allow dynamic enabling/disabling of tools

## Testing & Deployment

10. **Testing**
    - [ ] Unit tests for MCP tools
    - [ ] Integration tests for full voice pipeline
    - [ ] Load testing of LLM response loop

11. **Deployment Setup**
    - [ ] Write Dockerfile for voice assistant services
    - [ ] Create systemd services for auto-start on Pi
    - [ ] Document setup in `INSTALL.md`

12. **Security & Privacy**
    - [ ] Limit all network access to LAN only
    - [ ] Use secure tokens or permissions for tool access
    - [ ] Avoid logging sensitive content unless explicitly enabled

13. **Logging & Troubleshooting**
    - [ ] Integrate Python’s built-in `logging` module for all backend services
    - [ ] Configure logging for both console and file outputs
    - [ ] Use structured log messages (preferably JSON format)
    - [ ] Apply appropriate log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
    - [ ] Ensure all exceptions/errors are logged with stack traces and context
    - [ ] Implement log rotation to manage log file size
    - [ ] Document logging best practices for developers
    - [ ] (Optional) Integrate with external log management solutions (e.g., ELK Stack, Sentry)
