#!/usr/bin/env python
"""
This module creates an MCP server that exposes a resource which returns the current date and time.
"""

from datetime import datetime

from mcp.server.fastmcp import FastMCP

# Initialize an MCP server instance with a custom name.
mcp = FastMCP("DateTimeServer")


@mcp.tool()
def get_current_datetime() -> str:
    """
    Return the current date and time in ISO 8601 format.

    Returns:
        str: The current date and time as a string.
    """
    current_time = datetime.now().isoformat()
    return current_time


if __name__ == "__main__":
    mcp.run(transport="stdio")
