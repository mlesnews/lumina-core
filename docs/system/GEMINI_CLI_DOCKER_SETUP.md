# Gemini CLI Docker Setup

**Status:** Active  
**Last Updated:** 2026-02-04  
**Registry:** `config/coding_assistants_registry.json` (gemini_cli)  
**Docker:** `docker/gemini-cli/`

## Overview

[Gemini CLI](https://github.com/google-gemini/gemini-cli) is an open-source AI agent that brings Gemini directly into the terminal. This document covers the Lumina homelab Docker integration.

## Quick Reference

| Item | Value |
|------|-------|
| **Docker Image** | `lumina/gemini-cli:latest` |
| **Vault Secret** | `gemini-api-key` |
| **Free Tier** | 60 req/min, 1000 req/day |
| **Context Window** | 1M tokens |
| **Model** | Gemini 3 |

## Features

- **Terminal-first AI agent** - designed for developers who live in the command line
- **1M token context window** - analyze entire codebases
- **Built-in tools** - Google Search grounding, file operations, shell commands, web fetching
- **MCP support** - extensible with Model Context Protocol servers
- **Checkpointing** - save and resume conversations
- **Free tier** - 60 requests/min and 1,000 requests/day with personal Google account

## Installation

### 1. Add API Key to Azure Key Vault

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/add_secret_to_vault.py --name gemini-api-key
# Get your key from: https://aistudio.google.com/apikey
```

### 2. Build the Container

```powershell
cd docker\gemini-cli
docker compose build
```

### 3. Run Gemini CLI

```powershell
# Using the convenience script (auto-fetches from Azure Vault)
.\run-gemini.ps1

# Or directly with docker compose
docker compose run --rm gemini-cli
```

## Usage Examples

### Interactive Mode

```powershell
.\run-gemini.ps1
# Inside gemini:
> Explain the architecture of this codebase
> Give me a summary of all changes from yesterday
```

### With Specific Project

```powershell
.\run-gemini.ps1 -Workspace "c:\Users\mlesn\Dropbox\my_projects\.lumina"
```

### Non-Interactive (Scripting)

```powershell
# Simple text response
docker compose run --rm gemini-cli -p "What is the purpose of this Dockerfile?"

# JSON output for parsing
docker compose run --rm gemini-cli -p "List all TODO comments" --output-format json
```

## Authentication

### Azure Key Vault (Recommended)

The API key is stored in Azure Key Vault for security:

- **Vault:** `https://jarvis-lumina.vault.azure.net/`
- **Secret Name:** `gemini-api-key`
- **Fetch Script:** `docker/gemini-cli/fetch_api_key_from_vault.py`

The `run-gemini.ps1` script automatically fetches the key from Azure Vault.

### Alternative Methods

1. **Environment Variable:** `$env:GEMINI_API_KEY = "your-key"`
2. **Vertex AI:** Set `GOOGLE_API_KEY` and `GOOGLE_GENAI_USE_VERTEXAI=true`

## Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Container definition (Node 20-slim) |
| `docker-compose.yml` | Deployment configuration |
| `settings.json` | Gemini CLI configuration |
| `GEMINI.md` | Lumina context file |
| `run-gemini.ps1` | PowerShell convenience script |
| `fetch_api_key_from_vault.py` | Azure Vault integration |

## MCP Server Integration

Add MCP servers to `settings.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

## Coding Assistants Registry

Gemini CLI is registered in `config/coding_assistants_registry.json`:

```json
{
  "gemini_cli": {
    "name": "Gemini CLI",
    "status": "active",
    "priority": 6,
    "type": "cloud_terminal",
    "authentication": {
      "method": "azure_key_vault",
      "secret_name": "gemini-api-key"
    }
  }
}
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `/help` | Show all commands |
| `/chat` | Start new conversation |
| `/clear` | Clear screen |
| `/save` | Save checkpoint |
| `/load` | Load checkpoint |
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit |

## Troubleshooting

### Authentication Issues
- Verify Azure Vault access: `az keyvault secret show --vault-name jarvis-lumina --name gemini-api-key`
- Check API key at [AI Studio](https://aistudio.google.com/apikey)

### Container Issues
- Rebuild: `docker compose build --no-cache`
- Check logs: `docker compose logs`

## Related Documentation

- [Coding Assistants Registry](../../config/coding_assistants_registry.json)
- [Azure Key Vault Config](../../config/azure/key_vault_config.json)
- [Docker README](../../docker/gemini-cli/README.md)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Docs](https://geminicli.com)

## Tags

#GEMINI_CLI #DOCKER #AZURE_KEY_VAULT #CODING_ASSISTANT #TERMINAL @JARVIS
