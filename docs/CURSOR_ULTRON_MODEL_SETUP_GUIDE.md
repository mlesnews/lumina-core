# 🚀 ULTRON Models in Cursor IDE - Complete Setup Guide

## Problem
ULTRON virtual cluster models (hybrid KAIJU + laptop) are not showing in the Cursor chat model dropdown.

## Important Note
**ULTRON Cluster does NOT require an API key** - it's a local Docker LLM cluster (Ollama-based). No authentication needed.

## Solution

### Method 1: Through Cursor Settings UI (Recommended)

1. **Open Cursor Settings**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Or: **File → Preferences → Settings**

2. **Search for "Ollama" or "Model"**
   - Type in the settings search box

3. **Configure Ollama Settings**
   - Find **"Ollama: Endpoint"** setting
   - Set to: `http://localhost:11434`
   - Find **"Ollama: Default Model"** setting  
   - Set to: `qwen2.5:72b`

4. **Add Custom Models (if available)**
   - Look for settings like:
     - "Cursor: Custom Models"
     - "AI: Custom Models"
     - "Models: Additional"
   
   If these settings exist, click "Add Item" or "Edit in settings.json"

5. **Alternative: Edit settings.json directly**
   - In Settings UI, click the "Open Settings (JSON)" icon (top right)
   - Add this configuration:

```json
{
  "cursor.model": {
    "customModels": [
      {
        "title": "ULTRON Cluster (Qwen2.5 72B)",
        "provider": "ollama",
        "model": "qwen2.5:72b",
        "apiBase": "http://localhost:11434",
        "contextLength": 32768
      },
      {
        "title": "ULTRON Router (Smart Routing)",
        "provider": "ollama",
        "model": "qwen2.5:72b",
        "apiBase": "http://10.17.17.32:3008",
        "contextLength": 32768
      },
      {
        "title": "KAIJU Iron Legion",
        "provider": "ollama",
        "model": "llama3",
        "apiBase": "http://10.17.17.32:11434",
        "contextLength": 8192
      }
    ]
  },
  "ollama.endpoint": "http://localhost:11434",
  "ollama.defaultModel": "qwen2.5:72b"
}
```

### Method 2: Verify Models in Chat Panel

1. **Open Chat Panel**
   - Press `Ctrl+L` (or `Cmd+L` on Mac)
   - Or click the chat icon in the sidebar

2. **Check Model Dropdown**
   - Look for the model selector at the top of the chat panel
   - Click on it to see available models
   - ULTRON models should appear if configured correctly

3. **Test Connection**
   - Select a ULTRON model
   - Try sending a message
   - If it works, you're all set!

### Method 3: Verify Ollama is Running

Before models can appear, ensure Ollama is running:

```bash
# Check if Ollama is running
ollama list

# If not running, start it
ollama serve

# Pull the model if needed
ollama pull qwen2.5:72b
```

### Authentication

**No API keys required!** ULTRON cluster is a local Docker LLM running Ollama. All endpoints are local/network accessible without authentication:
- `http://localhost:11434` - No auth needed
- `http://10.17.17.32:3008` - No auth needed (local network)
- `http://10.17.17.32:11434` - No auth needed (local network)

### Troubleshooting

#### Models Still Not Showing

1. **Restart Cursor IDE**
   - Close completely and reopen
   - Settings changes often require a restart

2. **Check Ollama Endpoint**
   ```bash
   curl http://localhost:11434/api/tags
   ```
   - Should return list of available models

3. **Verify Network Access**
   - For KAIJU models, ensure network access:
   ```bash
   curl http://10.17.17.32:11434/api/tags
   curl http://10.17.17.32:3008/health
   ```

4. **Check Cursor Logs**
   - Open: **Help → Toggle Developer Tools**
   - Check Console for errors related to model loading

5. **Clear Cursor Cache**
   - Close Cursor
   - Delete cache directory (varies by OS)
   - Restart Cursor

#### Model Appears But Doesn't Work

1. **Check Model is Loaded**
   ```bash
   ollama ps
   ```
   - Should show running models

2. **Test Direct API Call**
   ```bash
   curl http://localhost:11434/api/generate -d '{
     "model": "qwen2.5:72b",
     "prompt": "Hello"
   }'
   ```

3. **Check Cursor Network Settings**
   - Ensure no firewall blocking localhost:11434
   - For KAIJU, ensure network access is allowed

### ULTRON Cluster Endpoints

| Model | Endpoint | Model Name | Description |
|-------|----------|------------|-------------|
| ULTRON Cluster | http://localhost:11434 | qwen2.5:72b | Local laptop Qwen2.5 72B |
| ULTRON Router | http://10.17.17.32:3008 | qwen2.5:72b | Smart router (hybrid) |
| KAIJU Iron Legion | http://10.17.17.32:11434 | llama3 | KAIJU NAS with 7 models |

### Quick Setup Script

Run the automated setup script:

```bash
python scripts/python/setup_ultron_cursor_models.py
```

This will:
- Update `.cursor/settings.json` with ULTRON models
- Provide manual setup instructions
- Verify configuration

### Next Steps

1. ✅ Run setup script
2. ✅ Restart Cursor IDE
3. ✅ Open Chat (Ctrl+L)
4. ✅ Select ULTRON model from dropdown
5. ✅ Test with a message

---

**Created**: 2025-12-31  
**Status**: Active  
**Last Updated**: 2025-12-31
