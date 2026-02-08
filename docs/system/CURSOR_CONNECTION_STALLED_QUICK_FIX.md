# Cursor Connection Stalled - Quick Fix Guide

## Immediate Actions

### 1. Check Ollama Service Status
```powershell
# Test if Ollama is running
Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing

# If it fails, start Ollama:
ollama serve
```

### 2. Verify Models Are Available
```powershell
ollama list

# If models missing, pull them:
ollama pull qwen2.5-coder:7b
ollama pull qwen2-72b:latest
```

### 3. Run Diagnostic Script
```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/diagnose_cursor_connection.py
```

### 4. Restart Cursor IDE
- Close Cursor completely
- Reopen Cursor
- Try your workflow again

## What Was Fixed

✅ **Added timeout configuration** to ULTRON model (60 seconds)
✅ **Added maxTokens limit** to ULTRON model (2000 tokens)
✅ **Added retry configuration** (3 attempts, 1 second delay)
✅ **Added connection timeout** (30 seconds)
✅ **Added stream timeout** (120 seconds)
✅ **Created diagnostic script** for troubleshooting

## Configuration Changes

The following settings were added to `.vscode/settings.json`:

```json
{
  "cursor.agent.retryAttempts": 3,
  "cursor.agent.retryDelay": 1000,
  "cursor.agent.connectionTimeout": 30000,
  "cursor.agent.streamTimeout": 120000
}
```

And timeout/maxTokens were added to all ULTRON model configurations.

## Retry scope (what we coded this for)

- **Our retry config** (`cursor.agent.retryAttempts` / `retryDelay`) was added for **connection-stalled** and **timeout** scenarios. Cursor may only use it for those error types.
- **Internal errors** (e.g. `[internal] serialize binary: invalid int 32: 4294967295`) are not connection/timeout; Cursor’s retry manager *should* retry those too but often does not. **Workaround:** copy the Request ID from the error → paste it in chat → we run the [Request ID rerun workflow](CURSOR_INTERNAL_ERROR_WORKAROUND.md) and you rerun the @ask.

## If Problem Persists

1. Check Ollama logs: `ollama logs`
2. Check Windows Event Viewer for Ollama service errors
3. Verify firewall isn't blocking localhost:11434
4. Try switching to a different model temporarily
5. Check Cursor IDE logs: `%APPDATA%\Cursor\logs`

## Related Files

- `docs/system/CURSOR_CONNECTION_STALLED_WORKFLOW_FIX.md` - Full diagnostic guide
- `scripts/python/diagnose_cursor_connection.py` - Diagnostic tool
- `.vscode/settings.json` - Updated configuration

---

**Request ID**: a2155803-eda4-4daf-88ef-927515c31d0c
**Fixed**: 2026-01-28
