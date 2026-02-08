# Lumina MCP Integration

Complete integration guide for MANUS and ElevenLabs MCP servers with the Lumina ecosystem.

## Overview

The Lumina MCP integration provides seamless integration of Model Context Protocol (MCP) servers with the Lumina ecosystem, including:

- **MANUS MCP Server**: Exposes MANUS Unified Control functionality via MCP
- **ElevenLabs MCP Server**: Provides Text-to-Speech and audio processing capabilities
- **Azure Key Vault Integration**: All secrets securely stored and retrieved from Azure Key Vault
- **IDE Integration**: Works with Cursor IDE, Claude Desktop, and other MCP-compatible clients

## Quick Start

### 1. Generate Environment File from Azure Key Vault

```bash
python scripts/python/manus_mcp_lumina_integration.py --generate-env
```

This will:
- Retrieve ElevenLabs API key from Azure Key Vault
- Generate `.env` file in `containerization/services/mcp-servers/`
- Configure all required environment variables

### 2. Start MCP Servers

```bash
python scripts/python/manus_mcp_lumina_integration.py --start
```

Or manually:

```bash
cd containerization/services/mcp-servers
docker-compose up -d
```

### 3. Check Status

```bash
python scripts/python/manus_mcp_lumina_integration.py --status
```

Or manually:

```bash
cd containerization/services/mcp-servers
docker-compose ps
docker-compose logs -f
```

## Azure Key Vault Integration

### Required Secrets

All secrets MUST be stored in Azure Key Vault:

| Secret Name | Service | Required | Description |
|------------|---------|----------|-------------|
| `elevenlabs-api-key` | ElevenLabs | ✅ Yes | ElevenLabs API key for TTS and audio processing |
| `elevenlabs-api-residency` | ElevenLabs | ❌ No | Data residency region (default: `us`) |

### Setting Up Secrets

If secrets are not yet in Key Vault, add them:

```python
from scripts.python.azure_service_bus_integration import AzureKeyVaultClient

vault_url = "https://jarvis-lumina.vault.azure.net/"
key_vault = AzureKeyVaultClient(vault_url)

# Add ElevenLabs API key
key_vault.set_secret("elevenlabs-api-key", "your-api-key-here")

# Optional: Set data residency
key_vault.set_secret("elevenlabs-api-residency", "us")
```

### Automatic Secret Retrieval

The integration script automatically:
1. Connects to Azure Key Vault
2. Retrieves all required secrets
3. Generates `.env` file with secrets
4. Configures Docker Compose to use the secrets

## Configuration Files

### Lumina Integration Config

**File**: `config/lumina_mcp_integration.json`

Contains complete configuration for MCP servers integration with Lumina ecosystem.

### IDE Configuration

#### Cursor IDE

**File**: `.cursor/mcp_config.json`

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
        "ELEVENLABS_API_KEY": "retrieved-from-key-vault"
      }
    }
  }
}
```

#### Claude Desktop

**File**: `config/claude_desktop_mcp_config.json`

Generate using:

```bash
python scripts/python/manus_mcp_config_helper.py
```

Then copy to Claude Desktop config location:
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

## Docker Compose Integration

### Service Configuration

The MCP servers are configured in:

**File**: `containerization/services/mcp-servers/docker-compose.yml`

### Network

Both services run on the `mcp-network` network, allowing communication between services and with the Lumina ecosystem.

### Volumes

- `manus-data`: Persistent data for MANUS MCP server
- `manus-logs`: Logs for MANUS MCP server
- `elevenlabs-output`: Output directory for ElevenLabs generated files
- `elevenlabs-data`: Persistent data for ElevenLabs MCP server

### Environment Variables

All environment variables are loaded from `.env` file, which is generated from Azure Key Vault secrets.

## Integration with Lumina Ecosystem

### MANUS MCP Server Tools

The MANUS MCP server exposes the following tools for Lumina workflows:

1. **`manus_execute_operation`** - Execute any MANUS control operation
2. **`manus_get_health`** - Get health status of all control areas
3. **`manus_get_history`** - Get operation history
4. **`manus_ide_control`** - Control IDE operations (Cursor, VS Code)
5. **`manus_workstation_control`** - Control workstation operations
6. **`manus_lumina_control`** - Control Project Lumina operations

### ElevenLabs MCP Server Tools

The ElevenLabs MCP server provides:

- Text-to-Speech generation
- Voice cloning
- Audio processing
- Transcription
- Soundscape generation

See [ElevenLabs MCP documentation](https://github.com/elevenlabs/elevenlabs-mcp) for complete tool list.

### Lumina Workflow Integration

MCP servers can be integrated into Lumina workflows:

```python
# Example: Using MANUS MCP in a Lumina workflow
from manus_unified_control import MANUSUnifiedControl, ControlArea, ControlOperation

# MANUS operations can be executed via MCP or directly
control = MANUSUnifiedControl(project_root)
operation = ControlOperation(
    operation_id="workflow_001",
    area=ControlArea.PROJECT_LUMINA_MANAGEMENT,
    action="deploy",
    parameters={"target": "production"}
)
result = control.execute_operation(operation)
```

## Troubleshooting

### Secrets Not Found in Key Vault

```bash
# Check if secrets exist
python scripts/python/manus_mcp_lumina_integration.py --generate-env
# If fails, add secrets to Key Vault (see above)
```

### Docker Services Not Starting

```bash
# Check logs
cd containerization/services/mcp-servers
docker-compose logs -f

# Check status
docker-compose ps

# Rebuild if needed
docker-compose up -d --build
```

### MCP Client Connection Issues

1. **Verify services are running:**
   ```bash
   docker-compose ps
   ```

2. **Check service logs:**
   ```bash
   docker-compose logs manus-mcp-server
   docker-compose logs elevenlabs-mcp-server
   ```

3. **Verify configuration:**
   - Check `.cursor/mcp_config.json` for Cursor
   - Check Claude Desktop config file location
   - Ensure Docker commands are correct

4. **Test manually:**
   ```bash
   docker exec -it manus-mcp-server python3 -m manus_mcp_server
   docker exec -it elevenlabs-mcp-server python3 -m elevenlabs_mcp
   ```

## Security Best Practices

1. **All secrets in Azure Key Vault** ✅
   - Never hardcode API keys
   - Use Key Vault for all sensitive data
   - Rotate keys regularly

2. **Environment File Security**
   - `.env` file is gitignored
   - Never commit `.env` files
   - Regenerate from Key Vault on each deployment

3. **Container Security**
   - Run containers as non-root users
   - Use minimal base images
   - Keep images updated

4. **Network Security**
   - Use isolated Docker networks
   - Only expose necessary ports
   - Use health checks for monitoring

## Monitoring and Health Checks

### Health Check Endpoints

```bash
# MANUS MCP Server (port 8085)
# Note: MCP servers use stdio, so health checks verify container is running
docker exec manus-mcp-server python3 -c "import sys; sys.exit(0)"

# ElevenLabs MCP Server (port 8086)
docker exec elevenlabs-mcp-server python3 -c "import sys; sys.exit(0)"
```

### Service Status

```bash
# Using integration script
python scripts/python/manus_mcp_lumina_integration.py --status

# Using Docker Compose
cd containerization/services/mcp-servers
docker-compose ps
docker-compose logs -f
```

## References

- [MCP Configuration Guide](MCP_CONFIGURATION.md)
- [MCP Setup Quickstart](MCP_SETUP_QUICKSTART.md)
- [MCP Servers Setup](../mcp/MCP_SERVERS_SETUP.md)
- [Lumina IDE Integration](config/lumina_ide_integration.json)
- [ElevenLabs MCP Repository](https://github.com/elevenlabs/elevenlabs-mcp)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
