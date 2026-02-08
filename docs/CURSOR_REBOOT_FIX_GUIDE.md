# 🔄 Cursor IDE - Complete Fix & Reboot Guide

## Problem

**Error**: `Invalid Model Error: Model "Iron Legion" is not in your subscription plan and api key is not working.`

**Root Cause**: 
- "Iron Legion" is being used as a **model name** in Cursor settings
- "Iron Legion" is a **cluster/system name**, NOT a model name
- ULTRON is a **virtual cluster**, NOT a model name
- Cursor is trying to use these as cloud API models, which fails

## Important Clarifications

### ❌ WRONG - These are NOT model names:
- "Iron Legion" = Cluster/System Name
- "ULTRON" = Virtual Cluster Name
- "ULTRON Cluster" = Cluster Name

### ✅ CORRECT - These ARE model names:
- `qwen2.5:72b` = Actual Ollama model
- `llama3` = Actual Ollama model
- `codellama:13b` = Actual Ollama model

## Step-by-Step Fix

### Step 1: Run Automated Fix Script

```bash
# Navigate to project root
cd C:\Users\mlesn\Dropbox\my_projects\.lumina

# Run the fix script
python scripts/python/fix_cursor_iron_legion_model.py
```

This script will:
- ✅ Find all Cursor settings files
- ✅ Check for "Iron Legion" or "ULTRON" used as model names
- ✅ Fix incorrect configurations automatically
- ✅ Create backups before making changes

### Step 2: Manual Check (If Script Doesn't Find Files)

1. **Open Cursor Settings**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
   - Or: **File → Preferences → Settings**

2. **Search for "Iron Legion"**
   - Type "Iron Legion" in the settings search box
   - Look for any entries where "Iron Legion" is used as a **model name**

3. **Search for "ULTRON"**
   - Type "ULTRON" in the settings search box
   - Look for any entries where "ULTRON" is used as a **model name** (not just as a title)

4. **Fix Incorrect Entries**
   - If you find `"model": "Iron Legion"` → Change to `"model": "qwen2.5:72b"`
   - If you find `"model": "ULTRON"` → Change to `"model": "qwen2.5:72b"`
   - Ensure `"provider": "ollama"` is set (not "openai" or "anthropic")

5. **Edit Settings JSON Directly** (Alternative)
   - In Settings UI, click the "Open Settings (JSON)" icon (top right)
   - Search for "Iron Legion" or "ULTRON"
   - Fix any incorrect model configurations

### Step 3: Verify Correct Configuration

Your settings should look like this:

```json
{
  "cursor.model": {
    "customModels": [
      {
        "title": "ULTRON Cluster (Qwen2.5 72B)",  // ✅ OK - Display name
        "provider": "ollama",                      // ✅ Must be ollama
        "model": "qwen2.5:72b",                   // ✅ Actual model name
        "apiBase": "http://localhost:11434",
        "contextLength": 32768
      },
      {
        "title": "KAIJU Iron Legion",            // ✅ OK - Display name
        "provider": "ollama",                      // ✅ Must be ollama
        "model": "llama3",                         // ✅ Actual model name
        "apiBase": "http://10.17.17.32:11434",
        "contextLength": 8192
      }
    ]
  },
  "ollama.endpoint": "http://localhost:11434",
  "ollama.defaultModel": "qwen2.5:72b"
}
```

### Step 4: Close Cursor IDE Completely

**IMPORTANT**: You must close Cursor completely, not just the window.

1. **Close All Cursor Windows**
   - Close all open Cursor windows
   - Check system tray for Cursor icon
   - Right-click and "Exit" if present

2. **Verify Cursor is Closed**
   - Open Task Manager (`Ctrl+Shift+Esc`)
   - Look for "Cursor" processes
   - End any remaining Cursor processes

3. **Wait 10 seconds**
   - Give the system time to fully close Cursor

### Step 5: Restart Your PC

**Why restart?**
- Clears Cursor's internal cache
- Resets model configuration state
- Ensures all settings are reloaded fresh
- Prevents cached incorrect configurations

**How to restart:**
1. **Save all work** in other applications
2. **Click Start Menu**
3. **Click Power → Restart**
4. **Wait for PC to fully restart**

### Step 6: Verify After Reboot

1. **Open Cursor IDE**
   - Launch Cursor normally
   - Wait for it to fully load

2. **Check Settings**
   - Press `Ctrl+,` to open Settings
   - Verify Ollama endpoint is set: `http://localhost:11434`
   - Verify default model is set: `qwen2.5:72b`

3. **Test in Chat**
   - Press `Ctrl+L` to open Chat
   - Check model dropdown - should show Ollama models
   - Select `qwen2.5:72b` or another Ollama model
   - Send a test message
   - Should work without API key errors

## Troubleshooting

### Still Getting API Key Errors After Reboot

1. **Check Cursor Settings Again**
   - Search for "Iron Legion" or "ULTRON" again
   - Ensure no cloud provider is set for these

2. **Clear Cursor Cache**
   - Close Cursor
   - Delete cache directory:
     - Windows: `%APPDATA%\Cursor\Cache`
     - macOS: `~/Library/Caches/Cursor`
     - Linux: `~/.cache/Cursor`
   - Restart Cursor

3. **Check for Multiple Settings Files**
   - User settings: `%APPDATA%\Cursor\User\settings.json`
   - Workspace settings: `.cursor/settings.json` (in workspace)
   - Check both locations

### Models Not Showing in Chat

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

### Quick Verification Checklist

After reboot, verify:
- [ ] Cursor opens without errors
- [ ] Settings show Ollama endpoint: `http://localhost:11434`
- [ ] Chat (Ctrl+L) shows Ollama models in dropdown
- [ ] Can select `qwen2.5:72b` or other Ollama model
- [ ] Can send messages without API key errors
- [ ] No "Iron Legion" or "ULTRON" errors in console

## Summary

1. ✅ Run fix script: `python scripts/python/fix_cursor_iron_legion_model.py`
2. ✅ Close Cursor IDE completely
3. ✅ Restart PC
4. ✅ Open Cursor and test in Chat (Ctrl+L)
5. ✅ Verify no API key errors

**Key Points:**
- "Iron Legion" = Cluster name (OK for titles, NOT for model names)
- "ULTRON" = Virtual cluster (OK for titles, NOT for model names)
- Always use actual Ollama model names: `qwen2.5:72b`, `llama3`, etc.
- Always use `"provider": "ollama"` for local models
- No API keys needed for local Ollama models

---

**Created**: 2025-12-31  
**Status**: Active  
**Last Updated**: 2025-12-31
