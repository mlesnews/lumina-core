# 🔧 Fix: "Iron Legion" Invalid Model Error

## Problem

**Error Message**: `Invalid Model Error: Model "Iron Legion" is not in your subscription plan and api key is not working.`

**Root Cause**: Cursor IDE is trying to use "Iron Legion" as a model name with a cloud provider (OpenAI, Anthropic, etc.), but "Iron Legion" is a **local cluster name**, not a cloud model name.

## Solution

"Iron Legion" should **NOT** be used as a model name in Cursor. Instead, configure Cursor to use **Ollama** with actual model names like `qwen2.5:72b`, `llama3`, `codellama:13b`, etc.

### Step 1: Remove "Iron Legion" from Cursor Model Settings

1. **Open Cursor Settings**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Or: **File → Preferences → Settings**

2. **Search for "Model" or "AI"**
   - Look for any settings that reference "Iron Legion" as a model name
   - Remove or change any entries that use "Iron Legion" as a model identifier

3. **Check Custom Models**
   - Look for settings like:
     - `cursor.model.customModels`
     - `cursor.agent.customModels`
     - `cursor.chat.models`
   - Remove any entries where `"model": "Iron Legion"` or `"name": "Iron Legion"`

### Step 2: Configure Ollama Properly

1. **Set Ollama Endpoint**
   - Find **"Ollama: Endpoint"** setting
   - Set to: `http://localhost:11434`
   - Or: `http://10.17.17.32:11434` (for KAIJU)

2. **Set Default Model**
   - Find **"Ollama: Default Model"** setting
   - Set to: `qwen2.5:72b` (or another valid Ollama model)

3. **Add Custom Models (if needed)**
   - In Settings JSON, add:

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
        "title": "KAIJU Iron Legion (llama3)",
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

### Step 3: Verify Available Models

Check what models are actually available in Ollama:

```bash
# List available models
ollama list

# Test Ollama connection
curl http://localhost:11434/api/tags
```

### Step 4: Use Correct Model Names

**DO NOT USE:**
- ❌ `"model": "Iron Legion"`
- ❌ `"name": "Iron Legion"`
- ❌ `"title": "Iron Legion"` (as a model name)

**USE INSTEAD:**
- ✅ `"model": "qwen2.5:72b"`
- ✅ `"model": "llama3"`
- ✅ `"model": "codellama:13b"`
- ✅ `"title": "KAIJU Iron Legion"` (OK as display name, but model must be actual Ollama model)

### Step 5: Restart Cursor

After making changes:
1. **Save settings**
2. **Close Cursor completely**
3. **Restart Cursor**
4. **Test in Chat** (Ctrl+L)

## Common Mistakes

### ❌ Wrong Configuration
```json
{
  "model": "Iron Legion",  // ❌ WRONG - This is a cluster name, not a model
  "provider": "openai"     // ❌ WRONG - Iron Legion is local, not cloud
}
```

### ✅ Correct Configuration
```json
{
  "title": "KAIJU Iron Legion",  // ✅ OK - Display name
  "model": "llama3",              // ✅ CORRECT - Actual Ollama model
  "provider": "ollama",           // ✅ CORRECT - Local Ollama
  "apiBase": "http://10.17.17.32:11434"
}
```

## Verification

1. **Open Chat** (Ctrl+L)
2. **Check Model Dropdown** - Should show Ollama models, not "Iron Legion"
3. **Select a Model** - Choose `qwen2.5:72b` or another Ollama model
4. **Send a Test Message** - Should work without API key errors

## Troubleshooting

### Still Getting API Key Errors

1. **Check if "Iron Legion" is in any other settings**
   - Search Cursor settings for "Iron Legion"
   - Remove all references where it's used as a model name

2. **Check Cursor Settings JSON**
   - Open Settings JSON (icon in top right of Settings UI)
   - Search for "Iron Legion"
   - Remove or fix any incorrect model configurations

3. **Clear Cursor Cache**
   - Close Cursor
   - Delete cache directory (varies by OS)
   - Restart Cursor

### Models Not Showing

1. **Verify Ollama is Running**
   ```bash
   ollama list
   ```

2. **Test Ollama Endpoint**
   ```bash
   curl http://localhost:11434/api/tags
   ```

3. **Check Cursor Logs**
   - Help → Toggle Developer Tools
   - Check Console for errors

## Important Clarifications

### ❌ These are NOT model names (they are cluster/system names):
- **"Iron Legion"** = Cluster/System Name (OK for display/titles, NOT for model names)
- **"ULTRON"** = Virtual Cluster Name (OK for display/titles, NOT for model names)
- **"ULTRON Cluster"** = Cluster Name (NOT a model name)

### ✅ These ARE actual model names (use these):
- **"qwen2.5:72b"** = Actual Ollama Model Name
- **"llama3"** = Actual Ollama Model Name
- **"codellama:13b"** = Actual Ollama Model Name

## Summary

- **"Iron Legion"** = Cluster/System Name (OK for display/titles, NOT for model names)
- **"ULTRON"** = Virtual Cluster Name (OK for display/titles, NOT for model names)
- **"qwen2.5:72b"** = Actual Model Name (use this in model config)
- **Never use "Iron Legion" or "ULTRON" as model names** - they're not valid cloud or Ollama models
- **Always use Ollama provider** for local models
- **No API keys needed** for local Ollama models

## Complete Fix Process

1. **Run the fix script**: `python scripts/python/fix_cursor_iron_legion_model.py`
2. **Close Cursor IDE completely**
3. **Restart your PC** (recommended to clear cache)
4. **Reopen Cursor and test**

See `docs/CURSOR_REBOOT_FIX_GUIDE.md` for complete step-by-step instructions with reboot procedures.

---

**Created**: 2025-12-31  
**Status**: Active  
**Last Updated**: 2025-12-31
