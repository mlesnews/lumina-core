# MCP (Model Context Protocol) Configuration

This document describes how to configure MANUS and ElevenLabs as MCP servers for use with Claude Desktop, Cursor, and other MCP clients.

## Overview

We have two MCP servers configured:

1. **MANUS MCP Server**: Exposes the MANUS unified control interface for managing IDE, workstation, infrastructure, Lumina, automation, data, and security operations.

2. **ElevenLabs MCP Server**: Official ElevenLabs MCP server for text-to-speech and audio processing capabilities.

## Prerequisites

### 1. Install Required Packages

```bash
# Install MCP SDK for MANUS server
pip install mcp

# Install ElevenLabs MCP server
pip install elevenlabs-mcp

# Or use uvx (recommended for ElevenLabs)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Get ElevenLabs API Key

The ElevenLabs API key should be stored in Azure Key Vault. To retrieve it:

1. Ensure you have Azure Key Vault access configured
2. The key should be stored as one of these secret names:
   - `elevenlabs-api-key`
   - `elevenlabs-key`
   - `ELEVENLABS_API_KEY`

If you need to store the key in Key Vault:

```python
from scripts.python.azure_service_bus_integration import AzureKeyVaultClient

vault_url = "https://jarvis-lumina-vault.vault.azure.net/"
key_vault = AzureKeyVaultClient(vault_url)
key_vault.set_secret("elevenlabs-api-key", "your-api-key-here")
```

## Configuration

### Claude Desktop Configuration

#### Option 1: Use Configuration Helper (Recommended)

Run the configuration helper script to generate the config with API keys from Key Vault:

```bash
python scripts/python/manus_mcp_config_helper.py
```

This will:
- Retrieve the ElevenLabs API key from Azure Key Vault
- Generate the complete MCP configuration
- Save it to `config/claude_desktop_mcp_config.json`
- Print the configuration to stdout

Then copy the generated configuration to your Claude Desktop config file:

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

#### Option 2: Manual Configuration

Edit your Claude Desktop config file directly:

```json
{
  "mcpServers": {
    "MANUS": {
      "command": "python",
      "args": [
        "-m",
        "scripts.python.manus_mcp_server"
      ],
      "cwd": "C:\\Users\\mlesn\\Dropbox\\my_projects\\.lumina",
      "env": {}
    },
    "ElevenLabs": {
      "command": "uvx",
      "args": [
        "elevenlabs-mcp"
      ],
      "env": {
        "ELEVENLABS_API_KEY": "<YOUR_API_KEY_HERE>",
        "ELEVENLABS_MCP_BASE_PATH": "~/Desktop",
        "ELEVENLABS_MCP_OUTPUT_MODE": "files"
      }
    }
  }
}
```

**Important Notes:**
- Replace `cwd` with your actual project root path
- Replace `<YOUR_API_KEY_HERE>` with your ElevenLabs API key (preferably from Key Vault)
- On Windows, enable Developer Mode in Claude Desktop (Help → Enable Developer Mode)

### Cursor/Windsurf Configuration

For Cursor and Windsurf, use the `--print` flag to get the configuration:

```bash
# Install ElevenLabs MCP
pip install elevenlabs-mcp

# Generate configuration
python -m elevenlabs_mcp --api-key=<your-api-key> --print
```

Then configure MANUS separately by ensuring the MANUS MCP server module is accessible.

## MANUS MCP Server Tools

The MANUS MCP server exposes the following tools:

### 1. `manus_execute_operation`

Execute any MANUS control operation across all control areas.

**Parameters:**
- `area` (required): Control area (`ide_control`, `workstation_control`, `home_lab_infrastructure`, `project_lumina_management`, `automation_control`, `data_management`, `security_control`)
- `action` (required): Action to perform
- `parameters` (optional): Action-specific parameters
- `priority` (optional): Operation priority (1-10, default: 1)
- `timeout` (optional): Timeout in seconds (default: 300)

### 2. `manus_get_health_status`

Get health status of all MANUS control areas.

### 3. `manus_get_operation_history`

Get recent MANUS operation history.

**Parameters:**
- `limit` (optional): Number of operations to return (default: 50, max: 1000)

### 4. `manus_ide_control`

Control IDE operations (Cursor, VS Code).

**Parameters:**
- `action` (required): IDE action (`connect`, `execute_command`, `open_file`, `get_status`)
- `ide` (optional): Target IDE (`cursor`, `vscode`, default: `cursor`)
- `parameters` (optional): Action-specific parameters

### 5. `manus_workstation_control`

Control workstation operations (Windows, services, resources).

**Parameters:**
- `action` (required): Workstation action (`execute_command`, `get_status`, `manage_service`, `check_resources`)
- `parameters` (optional): Action-specific parameters

### 6. `manus_lumina_control`

Control Project Lumina operations (Git, codebase, deployments).

**Parameters:**
- `action` (required): Lumina action (`git_operation`, `deploy`, `get_status`, `run_script`)
- `parameters` (optional): Action-specific parameters

## ElevenLabs MCP Server

The ElevenLabs MCP server provides text-to-speech and audio processing capabilities. See the [official documentation](https://github.com/elevenlabs/elevenlabs-mcp) for available tools.

**Example usage:**
- "Create an AI agent that speaks like a film noir detective"
- "Generate three voice variations for a wise, ancient dragon character"
- "Convert this recording of my voice to sound like a medieval knight"
- "Create a soundscape of a thunderstorm in a dense jungle"

## Environment Variables

### ElevenLabs MCP Server

- `ELEVENLABS_API_KEY`: Your ElevenLabs API key (required)
- `ELEVENLABS_MCP_BASE_PATH`: Base path for file operations (default: `~/Desktop`)
- `ELEVENLABS_MCP_OUTPUT_MODE`: Output mode (`files`, `resources`, or `both`, default: `files`)
- `ELEVENLABS_API_RESIDENCY`: Data residency region (default: `"us"`, enterprise only)

## Troubleshooting

### MANUS MCP Server Issues

**Error: "MCP SDK not installed"**
```bash
pip install mcp
```

**Error: "Module not found: scripts.python.manus_mcp_server"**
- Ensure you're in the project root directory
- Check that `scripts/python/manus_mcp_server.py` exists
- Verify Python path includes the project root

**Error: "MANUS controller initialization failed"**
- Check that all MANUS dependencies are installed
- Review logs for specific initialization errors
- Ensure required controllers are properly configured

### ElevenLabs MCP Server Issues

**Error: "spawn uvx ENOENT"**
- Find uvx path: `which uvx` (Linux/macOS) or `where uvx` (Windows)
- Update configuration to use absolute path: `"command": "/usr/local/bin/uvx"`

**Error: "API key invalid"**
- Verify API key is correct in Azure Key Vault
- Check that the key is active and has credits available
- Ensure the key is properly passed in the environment variables

**Timeouts on long operations**
- Voice design and audio isolation can take a long time
- Timeouts in MCP Inspector are normal
- Should not occur when using Claude Desktop or other clients

### Logs

**Claude Desktop Logs:**

Windows:
```
%APPDATA%\Claude\logs\mcp-server-manus.log
%APPDATA%\Claude\logs\mcp-server-elevenlabs.log
```

macOS:
```
~/Library/Logs/Claude/mcp-server-manus.log
~/Library/Logs/Claude/mcp-server-elevenlabs.log
```

## Security Notes

⚠️ **ALL SECRETS MUST BE STORED IN AZURE KEY VAULT**

**Mandatory Security Policy:**
- ❌ NEVER hardcode API keys in configuration files
- ❌ NEVER commit API keys to version control
- ❌ NEVER pass API keys via environment variables in config files
- ✅ ALWAYS store all keys in Azure Key Vault
- ✅ ALWAYS retrieve keys at runtime via Key Vault client
- ✅ Use wrapper scripts that fetch keys from Key Vault before launching services

**Setting Up Keys in Key Vault:**

Run the setup script to interactively store all required keys:

```bash
python scripts/python/store_all_mcp_keys_to_vault.py
```

This script will:
- Connect to Azure Key Vault
- Prompt for each required API key
- Store them securely in Key Vault
- Verify they can be retrieved

**Required Secrets in Key Vault:**
- `elevenlabs-api-key` - ElevenLabs API key for TTS services

**Verifying Keys Are Stored:**

```bash
python scripts/python/manus_mcp_config_helper.py
```

This will verify all keys can be retrieved from Key Vault and generate the configuration.

## References

- [ElevenLabs MCP GitHub Repository](https://github.com/elevenlabs/elevenlabs-mcp)
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Claude Desktop MCP Setup](https://claude.ai/docs/mcp)
