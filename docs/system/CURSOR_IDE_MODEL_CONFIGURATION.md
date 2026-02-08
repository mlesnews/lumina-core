# Cursor IDE Model Configuration Guide

## Where to Configure Models

### Settings File Location
**`.cursor/settings.json`** (in your workspace root)

### Configuration Sections

Models are configured in these sections:

1. **`cursor.chat.customModels`** - Chat models
2. **`cursor.composer.customModels`** - Composer models  
3. **`cursor.agent.customModels`** - Agent models
4. **`cursor.inlineCompletion.customModels`** - Inline completion models

## How to Add Models

### Method 1: Via Settings UI

1. Open Cursor Settings: `Ctrl+Shift+,` (or `Cmd+,` on Mac)
2. Search for "Models" or "customModels"
3. Click "Edit in settings.json"
4. Add your model to the appropriate section

### Method 2: Direct JSON Edit

1. Open `.cursor/settings.json` directly
2. Find the section (e.g., `cursor.chat.customModels`)
3. Add your model JSON object
4. Run `configure_cursor_models_properly.py` to auto-add proper config

## Required Configuration for LOCAL Models

### Critical Fields (MUST HAVE)

```json
{
  "title": "Model Display Name",
  "name": "model-identifier",
  "provider": "ollama",
  "model": "model-id",
  "apiBase": "http://localhost:11434",
  "localOnly": true,                    ← REQUIRED
  "skipProviderSelection": true,        ← REQUIRED
  "requiresApiKey": false,              ← REQUIRED
  "description": "... - LOCAL ONLY, NO API KEY"
}
```

### Field Explanations

- **`localOnly: true`** - Tells Cursor this is a local model (no cloud)
- **`skipProviderSelection: true`** - Skips provider selection UI
- **`requiresApiKey: false`** - No API key needed (LOCAL ONLY)
- **`provider: "ollama"`** - Provider type for local Ollama models
- **`apiBase`** - Endpoint URL (localhost, 10.17.17.11, etc.)

## Example: Adding ULTRON Model

```json
{
  "title": "ULTRON",
  "name": "ULTRON",
  "provider": "ollama",
  "model": "qwen2.5:72b",
  "apiBase": "http://localhost:11434",
  "contextLength": 32768,
  "description": "ULTRON - Local Docker/WSL Ollama instance - LOCAL ONLY, NO API KEY",
  "localOnly": true,
  "skipProviderSelection": true,
  "requiresApiKey": false
}
```

## Example: Adding KAIJU (Iron Legion) Model

```json
{
  "title": "KAIJU (Iron Legion)",
  "name": "KAIJU",
  "provider": "ollama",
  "model": "codellama:13b",
  "apiBase": "http://10.17.17.11:3001",
  "contextLength": 8192,
  "description": "KAIJU Mark I - Code Expert - LOCAL ONLY, NO API KEY",
  "localOnly": true,
  "skipProviderSelection": true,
  "requiresApiKey": false
}
```

## Auto-Configuration Script

**Run this after adding models:**

```powershell
python scripts\python\configure_cursor_models_properly.py
```

This script will:
- ✅ Add `localOnly: true` to all local models
- ✅ Add `skipProviderSelection: true` to all local models
- ✅ Set `requiresApiKey: false` for all local models
- ✅ Remove any API key fields
- ✅ Update descriptions with "LOCAL ONLY, NO API KEY"

## Common Issues

### Issue: Model shows as "Cloud" or asks for API key

**Solution:** Ensure these fields are set:
- `localOnly: true`
- `skipProviderSelection: true`
- `requiresApiKey: false`

### Issue: Model not appearing in selector

**Solution:** 
1. Check model is in correct section (chat/composer/agent/inline)
2. Verify JSON syntax is correct
3. Restart Cursor IDE
4. Check model endpoint is reachable

### Issue: Model configuration not saving

**Solution:**
1. Ensure `.cursor/settings.json` is writable
2. Check for JSON syntax errors
3. Verify you're editing workspace settings, not user settings

## Verification

After adding models, verify:

1. **Model appears in selector** (top-right of Cursor UI)
2. **No API key prompt** when selecting local models
3. **Model shows as "Local"** not "Cloud"
4. **Model connects successfully** to endpoint

## Quick Reference

| Field | Local Model Value | Cloud Model Value |
|-------|------------------|-------------------|
| `localOnly` | `true` | `false` or omit |
| `skipProviderSelection` | `true` | `false` or omit |
| `requiresApiKey` | `false` | `true` |
| `provider` | `"ollama"` | `"openai"`, `"anthropic"`, etc. |
| `apiBase` | `http://localhost:11434` | `https://api.openai.com/v1` |

---

**Status**: ✅ Configuration guide complete  
**Last Updated**: 2026-01-10
