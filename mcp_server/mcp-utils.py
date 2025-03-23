#!/usr/bin/env python
"""
This module creates an MCP server that exposes various utility tools including:
- Getting the current date and time
- Playing sound files for assistant completion and confirmation prompts

Note: This script requires the 'pygame' library for cross-platform audio playback.
Install with: pip install pygame
"""

import os
import time
from datetime import datetime

# Third-party imports
import pygame
from mcp.server.fastmcp import FastMCP

# Initialize an MCP server instance with a custom name.
mcp = FastMCP("UtilsServer")


@mcp.tool()
def get_current_datetime() -> str:
    """
    Return the current date and time in ISO 8601 format.

    Returns:
        str: The current date and time as a string.
    """
    current_time = datetime.now().isoformat()
    return current_time


@mcp.tool()
def play_done_sound() -> str:
    """
    Play a sound to indicate the AI assistant has completed its task.

    This function plays the sound file 'cursor_done.mp3' to provide
    auditory feedback when the assistant has finished its answer.

    Returns:
        str: Success message or error information if the sound couldn't be played.

    Raises:
        FileNotFoundError: If the sound file cannot be found.
        Exception: If there's an error playing the sound file.
    """
    # Use the correct path to the sound file in the assets directory
    sound_file = os.path.join(os.path.dirname(__file__), "assets", "cursor_done.mp3")
    try:
        # Check if file exists before attempting to play it
        if not os.path.exists(sound_file):
            return f"Error: Sound file {sound_file} not found"

        # Initialize pygame mixer
        pygame.mixer.init()
        # Load and play the sound
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        # Wait for the sound to finish playing
        time.sleep(sound.get_length())
        return f"Successfully played {sound_file}"
    except Exception as e:
        return f"Error playing sound: {str(e)}"


@mcp.tool()
def play_confirmation_sound() -> str:
    """
    Play a sound to indicate the AI assistant needs confirmation.

    This function plays the sound file 'cursor_confirmation.mp3' to provide
    auditory feedback when the assistant needs confirmation for executing
    a command or tool.

    Returns:
        str: Success message or error information if the sound couldn't be played.

    Raises:
        FileNotFoundError: If the sound file cannot be found.
        Exception: If there's an error playing the sound file.
    """
    # Use the correct path to the sound file in the assets directory
    sound_file = os.path.join(
        os.path.dirname(__file__), "assets", "cursor_confirmation.mp3"
    )
    try:
        # Check if file exists before attempting to play it
        if not os.path.exists(sound_file):
            return f"Error: Sound file {sound_file} not found"

        # Initialize pygame mixer
        pygame.mixer.init()
        # Load and play the sound
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        # Wait for the sound to finish playing
        time.sleep(sound.get_length())
        return f"Successfully played {sound_file}"
    except Exception as e:
        return f"Error playing sound: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
