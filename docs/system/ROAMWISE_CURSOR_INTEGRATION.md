# RoamWise.AI ↔ Cursor Integration

**Purpose:** Connect Cursor IDE to RoamWise.AI internal portal for comprehensive documentation and knowledge access.

---

## The Vision

RoamWise.AI is the internal portal. Cursor is the IDE. They should be connected so:
- AI can access RoamWise knowledge base
- AI can query RoamWise APIs
- Documentation is browsable via `@Docs`
- Session hooks inject RoamWise context

---

## Integration Methods

### Method 1: Cursor @Docs (Web URL)

If RoamWise.AI is running as a web server, add it to Cursor's documentation sources:

1. **Start RoamWise server:**
   ```powershell
   python scripts/python/roamwise_server.py --host 0.0.0.0 --port 5000
   ```

2. **In Cursor:** Type `@Docs` → "Add new doc" → Enter URL:
   ```
   http://RoamWise.AI.lesnewski.local:5000
   ```

3. **Use in chat:** `@Docs RoamWise` to query

**Limitation:** Cursor's @Docs works best with static documentation sites. RoamWise's dynamic API endpoints may not be fully indexed.

---

### Method 2: MCP Server (Recommended)

Create an MCP server that exposes RoamWise APIs to Cursor:

**File:** `containerization/services/mcp-roamwise/server.py`

```python
#!/usr/bin/env python3
"""MCP server for RoamWise.AI integration."""

import json
import requests
from mcp.server import Server
from mcp.types import Tool, TextContent

ROAMWISE_BASE = "http://RoamWise.AI.lesnewski.local:5000"

server = Server("roamwise-mcp")

@server.tool("roamwise_search")
async def search(query: str) -> str:
    """Search RoamWise knowledge base."""
    resp = requests.get(f"{ROAMWISE_BASE}/api/holocron", params={"query": query})
    return json.dumps(resp.json())

@server.tool("roamwise_wordcloud")
async def wordcloud() -> str:
    """Get RoamWise word cloud data."""
    resp = requests.get(f"{ROAMWISE_BASE}/api/wordcloud")
    return json.dumps(resp.json())

@server.tool("roamwise_path")
async def find_path(from_node: str, to_node: str) -> str:
    """Find path between knowledge nodes."""
    resp = requests.get(f"{ROAMWISE_BASE}/api/path", params={"from": from_node, "to": to_node})
    return json.dumps(resp.json())

if __name__ == "__main__":
    server.run()
```

**Add to `.cursor/mcp.json`:**
```json
{
  "mcpServers": {
    "roamwise": {
      "command": "python",
      "args": ["containerization/services/mcp-roamwise/server.py"],
      "description": "RoamWise.AI knowledge base integration"
    }
  }
}
```

---

### Method 3: Session Hook Context Injection

Inject RoamWise context at session start:

**Update `.cursor/hooks/session_init.py`:**

```python
def get_roamwise_context() -> str:
    """Fetch current RoamWise status and inject into session."""
    try:
        import requests
        resp = requests.get("http://RoamWise.AI.lesnewski.local:5000/api/status", timeout=2)
        if resp.ok:
            status = resp.json()
            return f"""
**RoamWise.AI Portal:** Active at http://RoamWise.AI.lesnewski.local:5000
- Use `roamwise_search` MCP tool to query knowledge base
- Use `roamwise_wordcloud` for trending topics
- Use `roamwise_path` for knowledge graph navigation
"""
    except:
        pass
    return ""
```

---

### Method 4: Direct API Access

AI can call RoamWise APIs directly via shell/scripts:

```bash
# Search holocron
curl "http://RoamWise.AI.lesnewski.local:5000/api/holocron?query=JARVIS"

# Get word cloud
curl "http://RoamWise.AI.lesnewski.local:5000/api/wordcloud"

# Get all data
curl "http://RoamWise.AI.lesnewski.local:5000/api/data"
```

---

## RoamWise API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/status` | GET | System status |
| `/api/data` | GET | All nodes/paths/zones |
| `/api/path?from=X&to=Y` | GET | Find path between nodes |
| `/api/zone/<name>` | GET | Get zone map |
| `/api/wordcloud` | GET | Word cloud data |
| `/api/holocron?query=X` | GET | Search holocron |
| `/api/videos?search=X` | GET | Search video archive |

---

## Deployment Options

### Option A: Local (Ultron Laptop)

```powershell
python scripts/python/roamwise_server.py --host 127.0.0.1 --port 5000
```
- Access: `http://localhost:5000`
- Use case: Personal development

### Option B: NAS (10.17.17.32)

Deploy as Docker container on Synology NAS:
- Access: `http://10.17.17.32:5000` or `http://nas.lesnewski.local:5000`
- Use case: Always-on, accessible from any device

### Option C: Kaiju Desktop (10.17.17.11)

```powershell
python scripts/python/roamwise_server.py --host 0.0.0.0 --port 5000
```
- Access: `http://10.17.17.11:5000`
- Use case: High-performance, GPU-accelerated features

---

## Summary

| Integration | Best For | Setup Effort |
|-------------|----------|--------------|
| **@Docs** | Static documentation | Low |
| **MCP Server** | Live API queries | Medium |
| **Session Hook** | Context injection | Low |
| **Direct API** | Ad-hoc queries | None |

**Recommended:** MCP Server + Session Hook for comprehensive integration.

---

**Tags:** #roamwise #cursor #mcp #integration @JARVIS @LUMINA
