# Home AI Voice Assistant with Local LLM and MCP

## Project Overview
This project sets up a private, voice-activated AI assistant running on a Raspberry Pi. It leverages a locally hosted language model and integrates with real-world services like calendars or smart home devices via Anthropic's Model Context Protocol (MCP). Key goals include:

1. Offline-capable AI voice assistant
2. Natural language interface for performing home automation and task management
3. Secure and modular integration using MCP

## Technical Architecture

### Backend (Python, LangChain)

#### Tech Stack
- **Python Version**: Python 3.12+
- **LLM Framework**: LangChain + `langchain-mcp-adapters`
  - `langchain` for agent orchestration
  - `langchain-mcp-adapters` for MCP integration
- **LLM Runtime**:
  - `llama.cpp` or `Ollama` for local inference
  - Compatible models: TinyLlama, Mistral 7B GGUF, Phi-2
- **MCP Tools**:
  - Custom Python MCP servers for calendar and smart home tasks
  - `fastmcp` for rapid server scaffolding
- **Voice Processing**:
  - `whisper.cpp` for Speech-to-Text
  - `Piper` for Text-to-Speech

#### Components
- **Speech Layer**: Microphone input to Whisper → LLM → TTS output to speaker
- **Agent Layer**:
  - ReAct-based LangChain agent with tool selection
  - Invokes MCP tools for task execution
- **Task Tooling**:
  - Calendar tool (Google Calendar API or CalDAV via MCP)
  - Smart Home tool (calls Home Assistant or MQTT via MCP)

### Frontend
- SvelteKit UI to power kiosk-based dashboard
- Logs, manual overrides, and live transcript view

## Key Features
1. **Voice-Activated Agent**: Say commands like "Add meeting at 3pm"
2. **LLM-Powered Reasoning**: Uses ReAct agent to choose tools intelligently
3. **Modular Tooling via MCP**: Tools can be added/removed independently
4. **Fully Local Execution**: No cloud dependency for core assistant logic
5. **Home Automation Support**: Integrates with Home Assistant or MQTT to control lights, thermostats, and more (future implementation)

## Data Sources
- User voice commands (live microphone stream)
- Google Calendar API or local CalDAV server
- Home Assistant APIs or local device interfaces
- Custom JSON files for local reference data (optional)

## Technical Considerations
- Quantized models needed for efficient local inference on Raspberry Pi
- Use asyncio for efficient orchestration between STT, LLM, and TTS
- MCP tool interfaces must sanitize inputs and return structured responses
- Network access should be local-only for security
- Use systemd or Docker Compose to manage service restarts and logs

## Logging & Troubleshooting

- **Centralized Logging**: Integrate a robust logging system using Python’s built-in `logging` module, configured for both console and file outputs.
- **Log Levels**: Use appropriate log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) throughout the codebase to distinguish between normal operation, warnings, and errors.
- **Structured Logs**: Prefer structured log messages (e.g., JSON format) to facilitate automated log parsing and integration with monitoring tools.
- **Error Reporting**: Ensure all exceptions and errors are logged with full stack traces. Use context-rich messages to aid in troubleshooting.
- **Log Rotation**: Implement log rotation to prevent log files from consuming excessive disk space.
- **Third-Party Integration**: Consider integration with external log management solutions (e.g., ELK Stack, Sentry, or cloud logging services) for production deployments.
- **Developer Guidelines**: Document logging best practices for contributors, including when and how to log, and how to avoid leaking sensitive information.
