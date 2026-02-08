# MCP Setup Quickstart

Quick setup guide for configuring MANUS and ElevenLabs MCP servers.

## Prerequisites

1. **Install MCP SDK:**
   ```bash
   pip install mcp
   ```

2. **Install ElevenLabs MCP (choose one):**
   ```bash
   # Option 1: Using pip
   pip install elevenlabs-mcp
   
   # Option 2: Using uvx (recommended)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Get ElevenLabs API Key:**
   - Sign up at https://elevenlabs.io
   - Get your API key from the dashboard
   - Store it in Azure Key Vault as `elevenlabs-api-key`:
     ```python
     from scripts.python.azure_service_bus_integration import AzureKeyVaultClient
     
     vault_url = "https://jarvis-lumina.vault.azure.net/"
     key_vault = AzureKeyVaultClient(vault_url)
     key_vault.set_secret("elevenlabs-api-key", "your-api-key-here")
     ```

## Setup Steps

### 1. Generate Configuration

Run the configuration helper script:

```bash
python scripts/python/manus_mcp_config_helper.py
```

This will:
- Retrieve the ElevenLabs API key from Azure Key Vault (if available)
- Generate the complete MCP configuration
- Save it to `config/claude_desktop_mcp_config.json`
- Print the configuration to stdout

### 2. Install Configuration

Copy the generated configuration to your Claude Desktop config file:

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

### 3. Enable Developer Mode (Windows only)

1. Open Claude Desktop
2. Click "Help" in the top-left menu
3. Select "Enable Developer Mode"

### 4. Restart Claude Desktop

Close and reopen Claude Desktop to load the new MCP servers.

## Verify Installation

Once configured, you should see both MCP servers available in Claude Desktop. You can test them by asking Claude to:

- **MANUS:** "Check MANUS health status" or "Execute a MANUS operation"
- **ElevenLabs:** "Create an AI agent that speaks like a film noir detective"

## Troubleshooting

### MANUS MCP Server Not Working

1. **Check Python path:** Ensure `scripts/python/manus_mcp_server.py` is accessible
2. **Check logs:** Look for errors in Claude Desktop logs
3. **Verify dependencies:** Run `pip install mcp`

### ElevenLabs MCP Server Not Working

1. **Check API key:** Ensure it's in Azure Key Vault or manually configured
2. **Check uvx installation:** Run `which uvx` (or `where uvx` on Windows) to verify
3. **Check logs:** Look for errors in Claude Desktop logs

### Log Locations

**Windows:**
```
%APPDATA%\Claude\logs\mcp-server-manus.log
%APPDATA%\Claude\logs\mcp-server-elevenlabs.log
```

**macOS:**
```
~/Library/Logs/Claude/mcp-server-manus.log
~/Library/Logs/Claude/mcp-server-elevenlabs.log
```

## Manual Configuration

If you prefer to configure manually, see `config/claude_desktop_mcp_config.json` for the template, or refer to `docs/system/MCP_CONFIGURATION.md` for detailed documentation.
