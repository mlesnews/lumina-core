# Emergency Local AI Only Mode

## Critical Situation

**Cloud AI tokens will be exhausted by the 15th at current usage rate.**

This document describes the emergency local-only AI configuration to preserve cloud tokens.

## Local AI Resources

### 1. ULTRON (Laptop Local AI)
- **Endpoint**: `http://localhost:11434`
- **Model**: `qwen2.5:72b`
- **Context**: 32768 tokens
- **Status**: Local Ollama instance on laptop

### 2. KAIJU Iron Legion (NAS Cluster)
- **Endpoint**: `http://10.17.17.32:11434`
- **Models**: 7 models available
  - `codellama:13b` (Primary code generation)
  - `llama3.2:11b` (Secondary general)
  - `qwen2.5-coder:1.5b-base` (Lightweight quick)
  - `llama3:8b` (General purpose)
  - `mistral:7b` (General reasoning)
  - `mixtral-8x7b` (High complexity)
  - `gemma:2b` (Lightweight fallback)
- **Context**: 8192 tokens
- **Status**: Docker/WSL cluster on NAS

### 3. ULTRON Virtual Hybrid Cluster
- **Type**: Virtual hybrid cluster
- **Nodes**:
  - ULTRON Local (localhost:11434) - Priority 1
  - KAIJU (10.17.17.32:11434) - Priority 2
- **Routing**: Load-balanced
- **Description**: Combines laptop ULTRON + KAIJU Iron Legion into single virtual cluster

## Enforcement

### Automatic Enforcement Script

Run the emergency enforcement script:

```bash
python scripts/python/enforce_local_ai_only_emergency.py
```

This script:
1. ✅ Verifies local AI resources are available
2. ✅ Updates Cursor IDE settings to force local-only
3. ✅ Removes all cloud model configurations
4. ✅ Sets ULTRON as default for Chat, Composer, and Agent

### Manual Verification

1. **Restart Cursor IDE**
2. **Check Model Selector** (top-right of Cursor UI)
   - Should show "ULTRON" selected
   - Should NOT show cloud models (Claude, GPT-4, etc.)
3. **Verify Settings** (Cmd/Ctrl+,)
   - Chat default: ULTRON
   - Composer default: ULTRON
   - Agent default: ULTRON
   - Inline Completion default: ULTRON

### Configuration Files

- **Cursor Settings**: `.cursor/settings.json`
  - All models have `"localOnly": true`
  - All models have `"skipProviderSelection": true`
  - Default models set to "ULTRON"

## Usage Guidelines

### When to Use Each Resource

1. **ULTRON (localhost)** - Primary for:
   - Code generation
   - Complex reasoning
   - Large context windows (32k tokens)

2. **KAIJU Iron Legion (NAS)** - Use for:
   - Quick responses (lightweight models)
   - Code-specific tasks (codellama)
   - When ULTRON is busy

3. **ULTRON Virtual Cluster** - Use for:
   - Automatic load balancing
   - Failover between laptop and NAS
   - Maximum availability

### Model Selection Strategy

- **High complexity**: ULTRON (qwen2.5:72b) or KAIJU mixtral-8x7b
- **Medium complexity**: KAIJU llama3.2:11b or llama3:8b
- **Low complexity**: KAIJU qwen2.5-coder:1.5b-base or gemma:2b
- **Code generation**: ULTRON or KAIJU codellama:13b

## Troubleshooting

### ULTRON Not Available

1. Check Ollama is running:
   ```bash
   curl http://localhost:11434/api/tags
   ```

2. Start Ollama if needed:
   ```bash
   ollama serve
   ```

3. Verify model is installed:
   ```bash
   ollama list
   ```

### KAIJU Iron Legion Not Available

1. Check NAS is accessible:
   ```bash
   ping 10.17.17.32
   ```

2. Verify Ollama on NAS:
   ```bash
   curl http://10.17.17.32:11434/api/tags
   ```

3. Check Docker/WSL on NAS is running

### Cursor Still Using Cloud Models

1. **Force restart Cursor** (close completely, reopen)
2. **Check User Settings** (not just workspace settings)
3. **Manually select ULTRON** in model selector
4. **Run enforcement script again**:
   ```bash
   python scripts/python/enforce_local_ai_only_emergency.py
   ```

## Status

✅ **Local AI Only Mode**: ACTIVE
- ULTRON: Available
- KAIJU Iron Legion: Available
- Cursor: Configured for local-only

## Notes

- **Cloud tokens preserved**: All AI requests route to local resources
- **No API costs**: Local AI has no per-request costs
- **Privacy**: All data stays local
- **Performance**: May be slower than cloud, but no token limits

---

**Last Updated**: 2025-01-05
**Emergency Status**: ACTIVE
**Cloud Token Preservation**: CRITICAL
