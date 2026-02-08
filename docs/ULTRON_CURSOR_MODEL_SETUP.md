# 🤖 ULTRON Cluster in Cursor IDE

## Overview

Configure Cursor IDE to use the ULTRON cluster (local Qwen2.5 72B + KAIJU Iron Legion) as a model option.

## Important Note
**ULTRON Cluster does NOT require an API key** - it's a local Docker LLM cluster (Ollama-based). No authentication needed.

## Quick Setup

### Option 1: Using Ollama Extension/Settings

1. **Open Cursor Settings** (`Ctrl+,`)
2. **Search for "ollama"**
3. **Set Ollama endpoint**: `http://localhost:11434`
4. **Set default model**: `qwen2.5:72b`

### Option 2: Using Custom Model Configuration

The `.cursor/settings.json` has been updated with ULTRON configuration.

**Models Added:**
- `ULTRON Cluster` - Local Qwen2.5 72B
- `ULTRON Router` - Smart routing between local and KAIJU
- `KAIJU Iron Legion` - NAS with 7 models

## Verifying ULTRON is Available

### Check Local Ollama

```bash
curl http://localhost:11434/api/tags
```

### Check KAIJU

```bash
curl http://10.17.17.32:11434/api/tags
```

### Check ULTRON Router

```bash
curl http://10.17.17.32:3008/health
```

## How to See ULTRON in Cursor

### Method 1: Model Selector Dropdown

1. Open the Chat panel (`Ctrl+L`)
2. Click on the model dropdown (usually shows current model name)
3. Look for "ULTRON" or the configured Ollama models

### Method 2: Settings Search

1. Open Settings (`Ctrl+,`)
2. Search for "AI" or "Model"
3. Look for model configuration options

### Method 3: Using Continue Extension

If you have the Continue extension:
1. Open Continue settings
2. Add Ollama as a provider:
   ```json
   {
     "models": [{
       "title": "ULTRON Cluster",
       "provider": "ollama",
       "model": "qwen2.5:72b",
       "apiBase": "http://localhost:11434"
     }]
   }
   ```

### Method 4: Using Cline Extension

If you have Cline:
1. Open Cline settings
2. Configure Ollama endpoint: `http://localhost:11434`
3. Select model: `qwen2.5:72b`

## Cursor Settings Configuration

The following has been added to `.cursor/settings.json`:

```json
{
  "cursor.model": {
    "customModels": [
      {
        "name": "ULTRON Cluster",
        "endpoint": "http://localhost:11434/api/generate",
        "model": "qwen2.5:72b",
        "provider": "ollama"
      }
    ]
  },
  "ollama.endpoint": "http://localhost:11434",
  "ollama.defaultModel": "qwen2.5:72b"
}
```

## Endpoints

| Cluster | Endpoint | Model |
|---------|----------|-------|
| Local ULTRON | http://localhost:11434 | qwen2.5:72b |
| ULTRON Router | http://10.17.17.32:3008 | auto |
| KAIJU Iron Legion | http://10.17.17.32:11434 | llama3, codellama, etc. |

## Troubleshooting

### ULTRON Not Showing in Dropdown

1. **Restart Cursor** - Settings may need a restart to take effect
2. **Check Ollama is running**: `ollama serve` or `ollama list`
3. **Verify endpoint**: `curl http://localhost:11434/api/tags`

### Model Not Responding

1. Check Ollama is running: `ollama list`
2. Check model is loaded: `ollama ps`
3. Try pulling model: `ollama pull qwen2.5:72b`

### Connection Refused

1. Ensure Ollama is running on correct port
2. Check firewall settings
3. Verify Docker network if using containers

## Starting ULTRON Cluster

```bash
# Start local Ollama
ollama serve

# Or start Docker cluster
docker-compose -f containerization/services/laptop-optimized-llm/docker-compose.hybrid-cluster.yml up -d
```

## Files

- `.cursor/settings.json` - Cursor workspace settings with ULTRON config
- `config/cursor_ultron_model_config.json` - Full ULTRON model configuration

---

**Created**: 2025-12-31  
**Status**: Configuration Complete
