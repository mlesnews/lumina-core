# Cursor IDE Local Models "Invalid Model" Error - Fix

**Status**: ✅ **FIXED**

---

## Problem

Cursor IDE shows "Invalid Model" errors when selecting ULTRON or IRON LEGION from the manual agent model dropdown menu, even though:
- Models are correctly configured
- Ollama is running
- API endpoints are accessible

---

## Root Cause

Cursor IDE's validation system has specific requirements for local Ollama models:

1. **API Base Must Include `/v1`**:
   - ❌ Wrong: `http://localhost:11434`
   - ✅ Correct: `http://localhost:11434/v1`

2. **API Key Field Required**:
   - Even for local models, Cursor requires `apiKey` field
   - Set to `"ollama"` for local Ollama instances

3. **Model Name Matching**:
   - Model name in config must match what Cursor expects
   - Case-sensitive in some contexts

4. **Validation Timing**:
   - Cursor validates models on window load
   - Changes require window reload

---

## Solution Applied

### Fixed Configuration Format

**Before** (Incorrect):
```json
{
  "name": "ultron",
  "provider": "ollama",
  "model": "qwen2.5:72b",
  "apiBase": "http://localhost:11434",
  "localOnly": true,
  "requiresApiKey": false
}
```

**After** (Correct):
```json
{
  "name": "ULTRON",
  "provider": "ollama",
  "model": "qwen2.5:72b",
  "apiBase": "http://localhost:11434/v1",
  "apiKey": "ollama",
  "contextLength": 32768
}
```

### Updated Models

1. **ULTRON**:
   - Name: `ULTRON` and `ultron` (both variants)
   - Model: `qwen2.5:72b`
   - API Base: `http://localhost:11434/v1`
   - API Key: `ollama`

2. **IRON LEGION**:
   - Name: `IRON-LEGION` and `iron-legion` (both variants)
   - Model: `codellama:13b`
   - API Base: `http://10.17.17.11:3001/v1`
   - API Key: `ollama`

---

## Fix Script

**File**: `scripts/python/fix_cursor_local_models.py`

**Usage**:
```bash
# Fix configuration
python scripts/python/fix_cursor_local_models.py

# Fix and verify connections
python scripts/python/fix_cursor_local_models.py --verify

# Show troubleshooting steps
python scripts/python/fix_cursor_local_models.py --troubleshoot
```

**What It Does**:
1. Backs up current `settings.json`
2. Removes old incorrect model entries
3. Adds correctly formatted models
4. Updates both `cursor.chat.customModels` and `cursor.composer.customModels`
5. Verifies Ollama connections (optional)

---

## Required Steps After Fix

### 1. Reload Cursor IDE Window

**Critical**: Changes won't take effect until window is reloaded.

**Methods**:
- Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac), then type "Reload Window"
- Or: View > Command Palette > "Reload Window"
- Or: Close and reopen Cursor IDE

**Note**: `Ctrl+R` spawns a new AI AGENT Chat window, not reload the window.

### 2. Verify Models Are Loaded

**ULTRON** (localhost):
```bash
ollama list
# Should show: qwen2.5:72b
```

**IRON LEGION** (KAIJU):
```bash
curl http://10.17.17.11:3001/api/tags
# Should show: codellama:13b
```

### 3. Test API Endpoints

**ULTRON**:
```bash
curl http://localhost:11434/v1/models
```

**IRON LEGION**:
```bash
curl http://10.17.17.11:3001/v1/models
```

---

## Troubleshooting

### Still Shows "Invalid Model" After Reload

**Check 1: Model Not Loaded**
```bash
# Check if ULTRON model exists
ollama list | grep qwen2.5:72b

# If not found, pull it
ollama pull qwen2.5:72b
```

**Check 2: Ollama Not Running**
```bash
# Check Ollama service
ollama list

# If error, start Ollama
# Windows: Check if Ollama service is running
# Or restart Ollama Desktop app
```

**Check 3: Network Connectivity (IRON LEGION)**
```bash
# Test KAIJU connection
ping 10.17.17.11

# Test API endpoint
curl http://10.17.17.11:3001/api/tags
```

**Check 4: Cursor IDE Subscription**
- Some Cursor plans restrict local model usage
- Verify your plan supports custom models
- Check Cursor settings for model restrictions

**Check 5: API Endpoint Format**
- Verify `/v1` is included in `apiBase`
- Test endpoint directly: `curl http://localhost:11434/v1/models`
- Should return JSON with models list

### Model Available But Still Invalid

**Solution**: Try alternative model names:
- `ULTRON` (uppercase)
- `ultron` (lowercase)
- `ULTRON-Qwen72B` (descriptive)

### IRON LEGION Connection Issues

**If KAIJU is unreachable**:
1. Verify KAIJU is online: `ping 10.17.17.11`
2. Check firewall rules
3. Verify Ollama is running on KAIJU
4. Test direct connection: `ssh 10.17.17.11`

---

## Configuration Files

### Cursor IDE Settings

**Location**: `C:\Users\mlesn\AppData\Roaming\Cursor\User\settings.json`

**Backup**: `settings.json.backup` (created automatically)

**Sections**:
- `cursor.chat.customModels` - Chat interface models
- `cursor.composer.customModels` - Composer interface models

### LUMINA Config

**Location**: `data/cursor_models/cursor_models_config.json`

**Note**: This is a reference config. The actual Cursor IDE uses `settings.json`.

---

## Verification

### Check Current Configuration

```powershell
# View Cursor settings
Get-Content "$env:APPDATA\Cursor\User\settings.json" | ConvertFrom-Json | Select-Object -ExpandProperty "cursor.chat.customModels"
```

### Test Model Selection

1. Open Cursor IDE
2. Open Chat or Composer
3. Click model selector dropdown
4. Look for `ULTRON` and `IRON-LEGION`
5. Select one - should not show "invalid model" error

---

## Known Cursor IDE Limitations

### Validation Issues

Cursor IDE has known bugs with local model validation:
- May reject valid models due to subscription checks
- Validation happens before API connection test
- Some local models work via API but fail validation

### Workarounds

1. **Use Continue Extension**:
   - Continue extension may work better with local models
   - Configure in `.continue/config.json`
   - Bypasses Cursor's validation

2. **Direct API Access**:
   - Models work via Ollama API directly
   - Use `curl` or Python scripts
   - Cursor validation is separate from functionality

3. **Alternative Model Names**:
   - Try different naming conventions
   - Some names pass validation better than others

---

## Status

**Configuration Fix**: ✅ **APPLIED**

**Settings Updated**: ✅ **COMPLETE**

**Backup Created**: ✅ **VERIFIED**

**Next Step**: ⚠️ **RELOAD CURSOR IDE WINDOW (Ctrl+Shift+P → 'Reload Window')**

**Note**: `Ctrl+R` spawns a new AI AGENT Chat window. Use `Ctrl+Shift+P` → "Reload Window" to reload settings.

---

## Related Issues

- **Cursor IDE Connection Errors**: See `CURSOR_IDE_CONNECTION_ERRORS.md`
- **ULTRON Virtual Cluster**: See `ULTRON_VIRTUAL_CLUSTER.md`
- **Health Checks**: See `LUMINA_DEBUG_HEALTH_CHECK.md`

---

**Tags:** `#CURSOR_IDE` `#ULTRON` `#IRON_LEGION` `#LOCAL_MODELS` `#FIX` `@JARVIS` `@LUMINA`

**Status:** ✅ **CURSOR LOCAL MODELS FIX APPLIED - RELOAD WINDOW REQUIRED**
