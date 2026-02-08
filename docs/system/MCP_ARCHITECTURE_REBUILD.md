# MCP Architecture - Rebuild Guide

## Key Principle

**MCP servers are LOCAL processes that communicate via stdio (stdin/stdout), NOT network services.**

## Architecture Layers

### 1. MCP Servers (Local - stdio)
- **Location**: Host machine (Kaiju)
- **Protocol**: stdio (stdin/stdout)
- **Management**: Docker Desktop MCP Toolkit
- **Communication**: Direct process-to-process via pipes

**Examples:**
- `filesystem` - File operations
- `memory` - Persistent context
- `git` - Git operations
- `fetch` - HTTP requests
- `ElevenLabs` - Voice synthesis
- `time` - Date/time operations

**How to add:** Docker Desktop → MCP Toolkit → Catalog → Install

### 2. Network Services (Remote - HTTP)
- **Location**: NAS (10.17.17.32) or Cloud
- **Protocol**: HTTP/HTTPS REST API
- **Management**: Docker containers on NAS

**Examples:**
| Service | Location | Port | Purpose |
|---------|----------|------|---------|
| n8n | NAS | 5678 | Workflow automation |
| Ollama | NAS | 11434 | LLM inference |
| MariaDB | NAS | 3306 | Database |

### 3. Local Applications (Docker Desktop)
- **Location**: Kaiju (Docker Desktop)
- **Protocol**: Various (HTTP, WebSocket, etc.)

**Examples:**
| Container | Port | Purpose |
|-----------|------|---------|
| manus-mcp-server* | 8085-8086 | Custom Lumina API (NOT an MCP server) |
| jarvis-personaplex | 8998 | Voice AI |

*Note: Despite the name, this is a custom HTTP API, not an MCP server.

## Configuration Files

| File | Purpose |
|------|---------|
| `~/.cursor/mcp.json` | Cursor's MCP settings (built-in servers only) |
| Docker Desktop MCP Toolkit | Real MCP server management |
| `.lumina/config/homelab_mcp_hybrid_config.json` | Network service endpoints |

## What NOT to do

❌ Don't configure MCP servers with HTTP URLs in mcp.json
❌ Don't try to run MCP servers on NAS (they need local stdio)
❌ Don't confuse HTTP APIs with MCP servers

## What TO do

✅ Use Docker Desktop MCP Toolkit for MCP servers
✅ Keep network services (n8n, Ollama) on NAS
✅ Keep custom apps (manus, personaplex) in Docker Desktop
✅ MCP servers = local stdio, Network services = remote HTTP

## Rebuild Checklist

- [ ] Install MCP servers via Docker Desktop MCP Toolkit
- [ ] Configure ElevenLabs with API key in MCP Toolkit
- [ ] Keep n8n and Ollama running on NAS
- [ ] Rename/refactor manus-mcp-server to manus-api (clarity)
- [ ] Update documentation to reflect correct architecture

## Quick Reference

```
┌─────────────────────────────────────────────────────────┐
│                    KAIJU (Host)                         │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────────────┐    │
│  │   Cursor IDE    │◄──►│  MCP Servers (stdio)    │    │
│  │                 │    │  - filesystem           │    │
│  │                 │    │  - memory               │    │
│  │                 │    │  - ElevenLabs           │    │
│  └─────────────────┘    └─────────────────────────┘    │
│                              ▲                          │
│                              │ Docker Desktop           │
│                              │ MCP Toolkit              │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Docker Desktop Containers                       │   │
│  │  - manus-api (localhost:8085) ◄─── HTTP         │   │
│  │  - personaplex (localhost:8998)                 │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                          │
                          │ Network (HTTP)
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  NAS (10.17.17.32)                      │
├─────────────────────────────────────────────────────────┤
│  - n8n (port 5678) - Workflow automation               │
│  - Ollama (port 11434) - LLM inference                 │
│  - MariaDB (port 3306) - Database                      │
│  - File storage (SMB shares)                           │
└─────────────────────────────────────────────────────────┘
```

---
*Last updated: 2026-02-04*
*Context: Rebuild after MCP architecture clarification*
