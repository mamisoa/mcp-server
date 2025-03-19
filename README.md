# MCP DateTime Server 🕒

## Overview

MCP DateTime Server is a specialized tool designed to provide datetime functionality within the Cursor IDE environment. It enables accurate timestamp generation and datetime operations, which is particularly useful for maintaining changelogs, documentation versioning, and other time-sensitive operations.

## Features ✨

- ⏰ Current datetime retrieval in ISO 8601 format
- 🔌 Integration with Cursor IDE
- 📝 Useful for automated changelog generation
- 🏷️ Timestamp generation for documentation
- 🔄 Version control support

## Installation 🚀

### Prerequisites

- 🐍 Python 3.x
- 📦 Poetry (Python dependency management)
- 💻 Cursor IDE

### Setup

1. Clone the repository:

```bash
git clone https://github.com/mamisoa/mcp-server.git
cd mcp-server
```

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Add the following configuration to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "datetime": {
      "command": "poetry",
      "args": [
        "run",
        "python",
        "/path/to/your/mcp-server/mcp_server/mcp-datetime.py"
      ]
    }
  }
}
```

2. Replace `/path/to/your` with your actual installation path.

## Usage

### In Changelogs

When creating or updating changelogs, you can use the datetime server to automatically insert timestamps:

```markdown
## [Version 1.0.0] - <timestamp>
```

### Other Use Cases

1. **Documentation Updates** 📚
   - Automatically timestamp when documentation was last updated
   - Track review cycles for technical documentation

2. **Version Control** 🔄
   - Add timestamps to commit messages
   - Track when files were last modified

3. **Logging** 📊
   - Generate precise timestamps for application logs
   - Track execution time of operations

4. **Audit Trails** 🔍
   - Maintain accurate records of system modifications
   - Track user actions with precise timestamps

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

