# Cursor ULTRON & IRON LEGION Cluster Configuration

## Problem Fixed
Cursor was showing error: "The model Ultron does not work with your current plan or api key."

**Root Cause**: Cursor didn't recognize "ultron" or "iron-legion" as valid local model/cluster names.

## Solution Applied

Added "ULTRON" and "IRON LEGION" model configurations to `data/cursor_models/cursor_models_config.json` and synced them to `.vscode/settings.json`.

### Specialized @SYPHON Troubleshooting Decision:
Based on the error "The model Ultron does not work with your current plan or api key", the @SYPHON extraction identifies that Cursor is likely treating "Ultron" as a cloud model due to name collision or lack of explicit local-only enforcement.

**DECISION**: Implement absolute local-only enforcement using the `/v1` endpoint suffix and unique name variants.

### Robust Configuration:
- **ULTRON (Local)**: `ultron-local` -> `http://localhost:11434/v1`
- **IRON LEGION (Local)**: `iron-legion-local` -> `http://localhost:11434/v1`
- **Aliases**: `ultron`, `Ultron`, `iron-legion` all point to the `/v1` endpoint.
- **Local Only**: `true`
- **API Key**: `ollama` (placeholder)

## How to Apply in Cursor

I have already pushed these settings to `.vscode/settings.json`.

### FINAL Verification Steps (@DOIT)

1. **RESTART CURSOR**: This is critical. Workspace settings for custom models often require a fresh boot.
2. **Select "ULTRON (Local)"**: Try selecting the explicit local variant first.
3. **Check Global Settings**: If it still fails, press `Ctrl+Shift+P` -> `Open User Settings (JSON)` and check if there is an existing "Ultron" entry there that is overriding the workspace setting.
4. **Ollama Logs**: Run `ollama serve` in a terminal to see if Cursor is actually hitting the endpoint.


## Verification

After configuration:

1. **Restart Cursor** (important!)

2. Open the model selector (usually in chat or top right)

3. You should see both "ULTRON" and "IRON LEGION" in the list

4. Select either "ULTRON" or "IRON LEGION" and test with a simple message

5. Both should work without any API key errors

## Current Configuration

### ULTRON:
- **Model Name**: `ultron` (exact match)
- **Backend Model**: `qwen2.5:72b` (your local Ollama model)
- **Endpoint**: `http://localhost:11434` (local Ollama)
- **Status**: ✅ Configured in project config file

### IRON LEGION:
- **Model Name**: `iron-legion` (exact match)
- **Backend Model**: `codellama:13b` (KAIJU Code Expert)
- **Endpoint**: `http://10.17.17.11:3001` (KAIJU Iron Legion cluster)
- **Status**: ✅ Configured in project config file
- **Note**: Requires KAIJU machine to be powered on and accessible

## Troubleshooting

### Still seeing "Invalid Model" error?

1. **Restart Cursor completely** (close all windows)
2. For ULTRON: Verify Ollama is running: `curl http://localhost:11434/api/tags`
3. For IRON LEGION: Verify KAIJU is accessible: `curl http://10.17.17.11:3001/api/tags`
4. Check the model names are exactly `ultron` or `iron-legion` (lowercase with hyphen)
5. Verify models are available:
   - ULTRON: `ollama list` (should show `qwen2.5:72b`)
   - IRON LEGION: Requires KAIJU to be powered on

### Model not appearing in selector?

1. Check Cursor Settings → Models section
2. Verify the configuration was saved
3. Try adding it manually using Option 2 above
4. Check Cursor logs for errors

### Connection errors?

1. Ensure Ollama is running: `docker-compose up -d ollama` (if using Docker)
2. Test endpoint: `curl http://localhost:11434/api/tags`
3. Verify firewall isn't blocking port 11434

## Notes

- "ULTRON" and "IRON LEGION" are **cluster names**, not model names
- **ULTRON**: Uses `qwen2.5:72b` from your local Ollama instance (laptop)
- **IRON LEGION**: Uses `codellama:13b` from KAIJU Iron Legion cluster (requires KAIJU to be on)
- Both configurations are **LOCAL ONLY** - no API keys required
- ULTRON provides failover: if KAIJU is down, it uses local laptop models
- IRON LEGION provides direct access to KAIJU's 7-model expert cluster
- When KAIJU is available, IRON LEGION offers better performance for code tasks

## Related Files

- `config/cursor_ultron_model_config.json` - ULTRON cluster configuration
- `data/cursor_models/cursor_models_config.json` - Cursor model definitions
- `config/local_ai_config.json` - Local AI settings
