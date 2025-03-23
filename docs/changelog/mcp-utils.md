# Changelog for mcp-utils.py

## 2025-03-23

- Initial creation of the mcp-utils.py file
- Implemented three tools:
  - `get_current_datetime`: Cloned from mcp-datetime.py to provide current date and time in ISO format
  - `play_done_sound`: New tool to play cursor_done.mp3 when the AI assistant completes its task
  - `play_confirmation_sound`: New tool to play cursor_confirmation.mp3 when the AI assistant requires confirmation
- Updated sound playing tools to use playsound library for cross-platform compatibility
- Replaced playsound with pygame for better PEP 517 compatibility
- Fixed sound file paths to correctly point to files in the assets directory
