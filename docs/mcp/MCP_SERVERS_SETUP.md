# MCP Servers Setup - MANUS and ElevenLabs

Complete setup guide for running both MANUS and ElevenLabs MCP servers in Docker.

## Quick Start

1. **Configure environment:**
   ```bash
   cd containerization/services/mcp-servers
   cp .env.example .env
   # Edit .env and add your ELEVENLABS_API_KEY
   ```

2. **Start services:**
   ```bash
   docker-compose up -d
   ```

3. **Verify:**
   ```bash
   docker-compose ps
   docker-compose logs -f
   ```

## Configuration Files

### Cursor IDE

Configuration file: `.cursor/mcp_config.json`

```json
{
  "mcpServers": {
    "MANUS": {
      "command": "docker",
      "args": ["exec", "-i", "manus-mcp-server", "python3", "-m", "manus_mcp_server"]
    },
    "ElevenLabs": {
      "command": "docker",
      "args": ["exec", "-i", "elevenlabs-mcp-server", "python3", "-m", "elevenlabs_mcp"],
      "env": {
        "ELEVENLABS_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Claude Desktop

Configuration file location:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "MANUS": {
      "command": "docker",
      "args": ["exec", "-i", "manus-mcp-server", "python3", "-m", "manus_mcp_server"]
    },
    "ElevenLabs": {
      "command": "docker",
      "args": ["exec", "-i", "elevenlabs-mcp-server", "python3", "-m", "elevenlabs_mcp"],
      "env": {
        "ELEVENLABS_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note for Windows**: You may need to enable Developer Mode in Claude Desktop (Help > Enable Developer Mode).

## Alternative: Using uvx for ElevenLabs

For ElevenLabs, you can also use `uvx` directly (as recommended in their documentation):

```json
{
  "mcpServers": {
    "ElevenLabs": {
      "command": "uvx",
      "args": ["elevenlabs-mcp"],
      "env": {
        "ELEVENLABS_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Available Tools

### MANUS MCP Server

- `manus_execute_operation` - Execute any MANUS control operation
- `manus_get_health` - Get health status
- `manus_get_history` - Get operation history
- `manus_ide_control` - Control IDE operations
- `manus_workstation_control` - Control workstation operations

### ElevenLabs MCP Server

See [ElevenLabs MCP documentation](https://github.com/elevenlabs/elevenlabs-mcp) for complete tool list. Includes:
- Text-to-Speech generation
- Voice cloning
- Audio processing
- Transcription
- And more

## Troubleshooting

See the main [README.md](../containerization/services/mcp-servers/README.md) for detailed troubleshooting.
