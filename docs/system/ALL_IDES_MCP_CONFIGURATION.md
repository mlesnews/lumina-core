# All IDEs and Coding Assistants - MCP Configuration

## Overview

This document describes the complete MCP (Model Context Protocol) configuration for all IDEs and coding assistants, aligned with Docker MCP configuration.

## IDEs Configured

### 1. Cursor IDE

- **Adapter Port**: `8083`
- **Priority**: `high`
- **Status**: `active`
- **Config**: `.cursor/settings.json`, `.cursor/mcp_config.json`
- **Primary Model**: `codellama:13b`
- **Fallback Model**: `llama3.2:11b`

### 2. VS Code

- **Adapter Port**: `8082`
- **Priority**: `high`
- **Status**: `active`
- **Config**: `.vscode/settings.json`, `.vscode/mcp_config.json`
- **Primary Model**: `llama3.2:11b`
- **Fallback Model**: `codellama:13b`

### 3. AbacusAI IDE

- **Adapter Port**: `8084`
- **Priority**: `medium`
- **Status**: `active`
- **Config**: `.abacus/settings.json`, `.abacus/mcp_config.json`
- **Primary Model**: `deepseek-coder:6.7b`
- **Fallback Model**: `llama3.2:11b`

## Coding Assistants Configured

### 1. Kilo Code

- **Priority**: `high`
- **Status**: `active`
- **MCP Endpoint**: `http://localhost:8080/assistants/kilo_code`
- **Config**: `config/kilo_code_optimized_config.json`
- **Primary Model**: `codellama:13b`
- **Fallback Model**: `llama3.2:11b`
- **@Peak Enabled**: `true`
- **Iron Legion Primary**: `true`
- **Capabilities**:
  - Codebase indexing
  - Semantic search
  - Code generation
  - Code analysis
  - 128k context window

### 2. Continue

- **Priority**: `high`
- **Status**: `active`
- **MCP Endpoint**: `http://localhost:8080/assistants/continue`
- **Config**: `config/continue_mcp_config.json`
- **Primary Model**: `llama3.2:11b`
- **Fallback Model**: `codellama:13b`
- **Capabilities**:
  - Tab autocomplete
  - Inline completion
  - Local LLM support
  - Multi-model support

### 3. Cline

- **Priority**: `medium`
- **Status**: `active`
- **MCP Endpoint**: `http://localhost:8080/assistants/cline`
- **Config**: `config/cline_mcp_config.json`
- **Primary Model**: `claude-3-5-sonnet`
- **Fallback Model**: `llama3.2:11b`
- **Capabilities**:
  - Claude 3.5 Sonnet
  - Local LLM fallback
  - Advanced reasoning
  - Code generation

### 4. GitHub Copilot

- **Priority**: `high`
- **Status**: `active` (requires approval)
- **MCP Endpoint**: `http://localhost:8080/assistants/copilot`
- **Config**: `config/github_copilot_mcp_config.json`
- **Primary Model**: `gpt-4`
- **Fallback Model**: `gpt-3.5-turbo`
- **Requires Approval**: `true`
- **Air Gap Mode**: `blocked`

## MCP Hub Configuration

### Universal Hub

- **Name**: Universal IDE & Coding Assistants Hub
- **Endpoint**: `http://localhost:8080`
- **Health Check**: `http://localhost:8080/health`
- **Unified Management**: `true`

### Iron Legion Cluster

- **Cluster Name**: Iron Legion
- **Primary Endpoint (Main)**: `http://localhost:3000`
- **Load Balancer**: `http://localhost:11437`
- **Models (7-stack)**:
  - **Mark I**: `llama3.2:11b` (general)
  - **Mark II**: `codellama:13b` (coding)
  - `qwen2.5-coder:1.5b-base` (fast/light)
  - `llama3` (general/creative)
  - `mistral` (reasoning)
  - `mixtral-8x7b` (deep analysis)
  - `gemma-2b` (fallback)

## Configuration Files

### IDE Configurations

- **Cursor**: `.cursor/settings.json`, `.cursor/mcp_config.json`
- **VS Code**: `.vscode/settings.json`, `.vscode/mcp_config.json`
- **Abacus**: `.abacus/settings.json`, `.abacus/mcp_config.json`

### Assistant Configurations

- **Kilo Code**: `config/kilo_code_optimized_config.json`
- **Continue**: `config/continue_mcp_config.json`
- **Cline**: `config/cline_mcp_config.json`
- **GitHub Copilot**: `config/github_copilot_mcp_config.json`

### Universal MCP Config

- **Location**: `cedarbrook-financial-services_llc-env/universal-mcp-config/config.json`

## Port Assignments

| Component | Port | Purpose |
|-----------|------|---------|
| MCP Hub | 8080 | Universal hub endpoint |
| VS Code Adapter | 8082 | VS Code MCP adapter |
| Cursor Adapter | 8083 | Cursor MCP adapter |
| Abacus Adapter | 8084 | Abacus MCP adapter |
| Iron Legion Primary (Main) | 3000 | Ollama primary endpoint |
| Iron Legion Load Balancer | 11437 | Ollama load balancer |

## Features by IDE

### Cursor IDE

- AI chat
- Code generation
- Smart rewrites
- Context aware
- Maximum @Peak utilization
- Full R5 integration
- Watcher Utau integration

### VS Code

- IntelliSense
- Debugging
- Git integration
- Extensions
- @Peak patterns
- R5 integration

### AbacusAI IDE

- Advanced analysis
- Multi-model
- Cloud sync
- Enterprise features
- @Peak patterns
- R5 integration

## Assistant Priorities by IDE

### Cursor

1. **Kilo Code** (Primary)
2. **Continue** (Secondary)
3. **Cline** (Tertiary)
4. **GitHub Copilot** (Requires approval)

### VS Code

1. **Kilo Code** (Primary)
2. **Continue** (Secondary)
3. **Cline** (Tertiary)
4. **GitHub Copilot** (Requires approval)

### Abacus

1. **Kilo Code** (Primary)
2. **Continue** (Secondary)
3. **Cline** (Tertiary)

## @Peak Pattern Integration

All IDEs support @Peak patterns through Kilo Code:

- ✅ Pattern extraction
- ✅ Nutrient-dense solutions
- ✅ Small footprint
- ✅ Reusability
- ✅ Documentation
- ✅ Maximum utilization
- ✅ Force multiplier
- ✅ Watcher Utau research
- ✅ R5 Living Context Matrix

## Security

### Air Gap Mode

- **Kilo Code**: Enabled (prefer local)
- **Continue**: Enabled (prefer local)
- **Cline**: Enabled (local fallback)
- **GitHub Copilot**: Blocked (cloud-based)

### Killswitch

- All assistants support killswitch modes
- Default mode: `normal`
- Modes: death, dormant, degraded, limited, normal, enhanced

## Verification

### Check MCP Hub Status

```bash
curl http://localhost:8080/health
```

### Check Iron Legion

```bash
curl http://localhost:11434/api/tags
curl http://localhost:11437/api/tags
```

### Verify Assistant Endpoints

```bash
curl http://localhost:8080/assistants/kilo_code
curl http://localhost:8080/assistants/continue
curl http://localhost:8080/assistants/cline
```

## Status

✅ **All IDEs Configured**

- Cursor IDE: ✅ Configured
- VS Code: ✅ Configured
- AbacusAI IDE: ✅ Configured

✅ **All Assistants Configured**

- Kilo Code: ✅ Configured
- Continue: ✅ Configured
- Cline: ✅ Configured
- GitHub Copilot: ✅ Configured (requires approval)

✅ **MCP Integration**

- Hub: ✅ Configured
- Iron Legion: ✅ Configured
- All endpoints: ✅ Aligned

---

**Last Updated**: 2024-12-19
**Version**: 2.0
**Maintained By**: Cedarbrook Financial Services LLC
