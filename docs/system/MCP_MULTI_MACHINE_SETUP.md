# MCP Multi-Machine Setup Guide

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    KAIJU (Desktop PC)                        │
│                      10.17.17.11                             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────────────────────────┐     │
│  │ Cursor IDE  │◄──►│  MCP Servers (stdio)            │     │
│  │             │    │  via Docker Desktop MCP Toolkit │     │
│  └─────────────┘    │  - ElevenLabs (24 tools)        │     │
│                     │  - filesystem                    │     │
│                     │  - memory                        │     │
│                     └─────────────────────────────────┘     │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Local Docker Containers                             │    │
│  │  - manus-mcp-server (8085-8086) - Custom API        │    │
│  │  - jarvis-personaplex (8998) - Voice AI             │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Network (HTTP)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    ULTRON (Laptop)                           │
│                      (Mobile)                                │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────────────────────────┐     │
│  │ Cursor IDE  │◄──►│  MCP Servers (stdio)            │     │
│  │             │    │  via Docker Desktop MCP Toolkit │     │
│  └─────────────┘    │  - ElevenLabs (24 tools)        │     │
│                     │  - filesystem                    │     │
│                     │  - memory                        │     │
│                     └─────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Network (HTTP) - when on LAN
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    NAS (Synology)                            │
│                    10.17.17.32                               │
├─────────────────────────────────────────────────────────────┤
│  - n8n (port 5678) - Workflow automation                    │
│  - Ollama (port 11434) - LLM inference                      │
│  - MariaDB (port 3306) - Database                           │
│  - File storage (SMB shares)                                │
└─────────────────────────────────────────────────────────────┘
```

## Key Insights

### What MCP Is (and Isn't)

| Aspect | MCP Servers | Network Services |
|--------|-------------|------------------|
| **Protocol** | stdio (stdin/stdout) | HTTP/REST |
| **Location** | LOCAL only | Can be remote |
| **Communication** | Direct process pipes | Network requests |
| **Examples** | ElevenLabs, filesystem, memory | n8n, Ollama, databases |
| **Management** | Docker Desktop MCP Toolkit | Docker containers |

### Why MCP Must Be Local

MCP (Model Context Protocol) servers communicate with the IDE via **stdio** (standard input/output). This is a direct process-to-process communication that:
- Cannot traverse network boundaries
- Requires the MCP server process to run on the same machine as the IDE
- Is managed by Docker Desktop's MCP Toolkit

### Network Services Are Different

Services like n8n and Ollama are **HTTP APIs** that:
- Can run anywhere on the network
- Are accessed via HTTP requests
- Are NOT MCP servers (despite similar functionality)

## Setup Instructions

### Per-Machine Setup (Kaiju & Ultron)

Each machine needs its own local MCP setup:

```powershell
# 1. Connect Cursor to MCP Toolkit
docker mcp client connect cursor

# 2. Set ElevenLabs API key
$apiKey = az keyvault secret show --vault-name jarvis-lumina --name elevenlabs-api-key --query "value" -o tsv
$apiKey | docker mcp secret set ELEVENLABS_API_KEY

# 3. Verify
docker mcp server ls
docker mcp client ls
```

### Automated Setup Script

Run the setup script on any machine:

```powershell
# From Dropbox (synced between machines)
& "$env:USERPROFILE\Dropbox\my_projects\.lumina\scripts\setup_mcp_ultron.ps1"
```

### Monitoring IDE notifications (including MCP errors)

**Yes – we should be monitoring IDE notifications.** When Cursor shows MCP errors or “MCP servers restarting”:

1. **Run the IDE notification monitor** (includes MCP config + Docker gateway check):
   - **Task:** `JARVIS: Monitor IDE Notifications` (Tasks: Run Task), or
   - **CLI:** `python scripts/python/jarvis_ide_notification_monitor.py --monitor`
2. **MCP-only check:** `JARVIS: MCP Check (config + Docker gateway)` or `--mcp-check`
3. The monitor reports on `.cursor/mcp.json`, Docker MCP gateway, and suggests running `scripts/fix_mcp_notifications_laptop.ps1` when needed.

*Note: A live “@mdv feed” or in-IDE notification stream is not available to the agent; **@mdv** = **Manus Desktop Video** (desktop/screen capture feed). When you share the MDV feed (e.g. screenshots or video from Manus), the agent can use that to see browser/DSM. A live in-IDE notification stream is not available; run the monitor task captures current state and recommendations. See `.cursor/docs/GLOSSARY_MDV_MANUS.md`.*

### Install Additional MCP Servers

In Docker Desktop → MCP Toolkit → Catalog:
- `filesystem` - File operations
- `memory` - Persistent context memory
- `fetch` - HTTP requests
- `time` - Date/time operations
- `sequential-thinking` - Step-by-step reasoning

## Configuration Files

### ~/.cursor/mcp.json (user-level)

**Use empty `mcpServers` so the project’s MCP_DOCKER is used and validation errors stop.**

Cursor merges user-level `~/.cursor/mcp.json` with the project’s `.cursor/mcp.json`. If the user file contains entries like `cursor-ide-browser` or `cursor-browser-extension` with only `type: "built-in"`, Cursor can show: *"Server 'cursor-browser-extension' must have either a command (for stdio) or url (for SSE)"* and MCP notifications will persist.

**Correct user-level content:**

```json
{
  "mcpServers": {}
}
```

To apply this automatically, run: **`scripts/fix_mcp_notifications_laptop.ps1`** (creates a backup first). Then run `docker mcp client connect cursor` and restart Cursor.

**Do NOT add HTTP URLs to mcp.json** – MCP uses stdio, not HTTP.

### Network Service Endpoints

These are accessed via HTTP from your code/applications:

| Service | URL | Purpose |
|---------|-----|---------|
| n8n | http://10.17.17.32:5678 | Workflow automation |
| Ollama | http://10.17.17.32:11434 | LLM inference |

## Troubleshooting

### MCP notifications persist (one-shot fix)

If MCP-related notifications keep appearing (e.g. "MCP configuration errors", "Server must have command or url", "MCP servers restarting"):

1. **Fix user-level MCP config** (required):
   ```powershell
   & "$env:USERPROFILE\Dropbox\my_projects\.lumina\scripts\fix_mcp_notifications_laptop.ps1"
   ```
   This writes `{"mcpServers":{}}` to `%USERPROFILE%\.cursor\mcp.json` (with a backup). No other entries in the user file – the project’s `.cursor/mcp.json` provides `MCP_DOCKER` only.

2. **Reconnect Cursor to Docker MCP:**
   ```powershell
   docker mcp client connect cursor
   ```

3. **Restart Cursor** (full exit and reopen).

4. **In Cursor:** Settings → Tools & MCP → ensure **MCP_DOCKER** is enabled. If you disabled it due to errors, re-enable it after the fix.

5. If notifications still appear after a restart, confirm Docker Desktop is running and run `JARVIS: MCP Check (config + Docker gateway)` (or `python scripts/python/jarvis_ide_notification_monitor.py --mcp-check`) for current state and recommendations.

### "cursor-ide-browser: Server 'cursor-browser-extension' must have either a command (for stdio) or url (for SSE)"

- Cursor validates MCP entries and expects each server to have `command` (stdio) or `url` (SSE). Built-in entries with only `type: "built-in"` in the **user** `mcp.json` trigger this and cause persistent notifications.
- **Fix:** Clear user-level `mcpServers` so only the project's MCP_DOCKER is used: run `scripts/fix_mcp_notifications_laptop.ps1` (or set `%USERPROFILE%\.cursor\mcp.json` to `{"mcpServers":{}}`). Restart Cursor. In Settings → Tools & MCP, enable **MCP_DOCKER** if it is disabled.

### "MCP notifications" / "MCP servers keep restarting" (especially on laptop)

1. **User-level config** – Cursor merges `~/.cursor/mcp.json` with the project. If the user file has old or broken servers (e.g. HTTP URLs, wrong `command`/`args`), those will keep failing and trigger notifications.
2. **Fix:** On the laptop, set user-level MCP to only built-ins (or leave it minimal) so the **project** `.cursor/mcp.json` is the source for the Docker gateway:
   - Open `%USERPROFILE%\.cursor\mcp.json` on the laptop.
   - Replace its contents with only built-ins, or ensure it has **no** `mcpServers` entries that point to HTTP or to `npx`/other commands that might fail. The project already defines `MCP_DOCKER`; avoid duplicating or conflicting servers in the user file.
3. **Docker must be running** – The project uses `MCP_DOCKER` (docker mcp gateway run). If Docker Desktop is not running on the laptop, the gateway will fail and Cursor will show MCP warnings. Start Docker Desktop and run:
   ```powershell
   docker mcp client connect cursor
   ```
4. **One-time setup on laptop:** Run `scripts/setup_mcp_ultron.ps1`, then restart Cursor.

### "MCP servers keep restarting" (general)

- Check `~/.cursor/mcp.json` for invalid HTTP URLs
- MCP servers use stdio, not HTTP - remove any URL entries

### "Cannot connect to MCP"

```powershell
# Reconnect Cursor to MCP Toolkit
docker mcp client connect cursor
# Then restart Cursor
```

### "ElevenLabs secrets required"

```powershell
# Re-set the secret
docker mcp secret rm ELEVENLABS_API_KEY
$apiKey = az keyvault secret show --vault-name jarvis-lumina --name elevenlabs-api-key --query "value" -o tsv
$apiKey | docker mcp secret set ELEVENLABS_API_KEY
```

---
*Last updated: 2026-02-04*
*Applies to: Kaiju (desktop), Ultron (laptop)*
