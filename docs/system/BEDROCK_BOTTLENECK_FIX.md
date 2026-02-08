# Bedrock Model Selection Bottleneck Fix

**Date**: 2025-01-02  
**Status**: ✅ **FIXED**  
**Request ID**: a2448884-9307-4c86-b132-7a6881cb5102  
**Tag**: @JARVIS @MARVIN @BEDROCK @FIX

---

## Problem Summary

Agent chat session resumption was failing with timeout errors and the following error:

```
ERROR_OPENAI: Selected model is not supported by bedrock, please use a different model
```

### Root Cause

1. **Bedrock Enabled in Cursor**: AWS Bedrock was enabled in Cursor IDE settings
2. **ULTRON Model Without Provider**: Agent chat sessions used `model="ULTRON"` (an Ollama model) but didn't specify `provider="ollama"`
3. **Cursor Default Routing**: When provider is not specified, Cursor defaults to Bedrock for cloud models
4. **Bedrock Rejection**: Bedrock doesn't support "ULTRON" as a model name (it's an Ollama model: `qwen2.5:72b`)

### Impact

- All agent chat session resumptions failed
- Sessions with ULTRON/KAIJU models couldn't be resumed
- Timeout errors occurred when Cursor tried to route Ollama models through Bedrock

---

## Solution

### Fix 1: Provider Specification in Session Resumption

**File**: `scripts/python/jarvis_resume_all_sessions.py`

**Changes**:
1. Added `MODEL_PROVIDER_MAP` to map Ollama models to `provider="ollama"`
2. Updated `ensure_model_config()` to automatically set provider based on model
3. Updated `discover_all_sessions()` to set provider during discovery

**Code**:
```python
MODEL_PROVIDER_MAP = {
    "ULTRON": "ollama",
    "KAIJU": "ollama",
    "qwen2.5:72b": "ollama",
    "llama3": "ollama"
}

# In ensure_model_config():
if model in MODEL_PROVIDER_MAP:
    expected_provider = MODEL_PROVIDER_MAP[model]
    if "provider" not in session or session.get("provider") != expected_provider:
        session["provider"] = expected_provider
```

### Fix 2: Error Handling and Auto-Recovery

**File**: `scripts/python/jarvis_resume_all_sessions.py`

**Changes**:
1. Added Bedrock error detection in `consolidate_sessions_to_master()`
2. Auto-fix provider when Bedrock errors are detected
3. Track fixed sessions and report in consolidation results

**Code**:
```python
# Detect Bedrock-specific errors
if "bedrock" in error_lower or "model is not supported" in error_lower:
    # Try to auto-fix by ensuring provider
    session = self.ensure_model_config(session)
```

### Fix 3: Diagnostic Script

**File**: `scripts/python/diagnose_bedrock_bottleneck.py`

**Purpose**: Comprehensive diagnostic tool to identify Bedrock routing issues

**Features**:
- Checks all agent chat sessions for provider specification
- Verifies Bedrock configuration status
- Identifies model/provider mismatches
- Generates recommendations for fixes

**Usage**:
```powershell
python scripts\python\diagnose_bedrock_bottleneck.py
```

---

## Verification

### Before Fix

```json
{
  "session_id": "session_123",
  "model": "ULTRON",
  "provider": null  // ❌ Missing - Cursor defaults to Bedrock
}
```

**Result**: Error - "Selected model is not supported by bedrock"

### After Fix

```json
{
  "session_id": "session_123",
  "model": "ULTRON",
  "provider": "ollama"  // ✅ Explicitly set - Cursor uses Ollama
}
```

**Result**: Success - Session resumes correctly with Ollama

---

## Testing

### Test 1: Run Diagnostic

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts\python\diagnose_bedrock_bottleneck.py
```

**Expected**: No critical findings after fix

### Test 2: Resume Sessions

```powershell
python scripts\python\jarvis_resume_all_sessions.py
```

**Expected**: All sessions resume successfully with provider set to "ollama"

### Test 3: Verify Provider in Sessions

Check that all sessions have provider set:

```powershell
# Check a session file
Get-Content data\agent_chat_sessions\session_*.json | Select-String "provider"
```

**Expected**: All sessions show `"provider": "ollama"` for ULTRON/KAIJU models

---

## Prevention

### Best Practices

1. **Always Specify Provider**: When setting model, always specify provider
   ```python
   session = {
       "model": "ULTRON",
       "provider": "ollama"  # ✅ Always specify
   }
   ```

2. **Use Model-Provider Mapping**: Use the `MODEL_PROVIDER_MAP` when creating sessions
   ```python
   MODEL_PROVIDER_MAP = {
       "ULTRON": "ollama",
       "KAIJU": "ollama"
   }
   ```

3. **Run Diagnostic Regularly**: Run diagnostic script after major changes
   ```powershell
   python scripts\python\diagnose_bedrock_bottleneck.py
   ```

### Configuration Options

#### Option 1: Keep Bedrock Enabled (Current)

- **Pros**: Can use Bedrock models when needed
- **Cons**: Must always specify provider for Ollama models
- **Action**: Ensure all sessions specify provider

#### Option 2: Disable Bedrock (If Not Using)

- **Pros**: No routing confusion, simpler configuration
- **Cons**: Can't use Bedrock models
- **Action**: Disable Bedrock in Cursor Settings → Personal Configuration → AWS Bedrock

---

## Related Files

- **Diagnostic Script**: `scripts/python/diagnose_bedrock_bottleneck.py`
- **Resumption Code**: `scripts/python/jarvis_resume_all_sessions.py`
- **Bedrock Config**: `config/aws_bedrock_config.json`
- **Bedrock Setup Guide**: `docs/system/CURSOR_BEDROCK_QUICK_SETUP.md`

---

## Troubleshooting

### Issue: Still Getting Bedrock Errors

**Solution**:
1. Run diagnostic: `python scripts\python\diagnose_bedrock_bottleneck.py`
2. Check session files for missing provider
3. Re-run resumption: `python scripts\python\jarvis_resume_all_sessions.py`

### Issue: Provider Not Being Set

**Solution**:
1. Verify `MODEL_PROVIDER_MAP` includes your model
2. Check `ensure_model_config()` is being called
3. Check logs for provider setting messages

### Issue: Cursor Still Routing to Bedrock

**Solution**:
1. Restart Cursor after changes
2. Verify Cursor settings don't force Bedrock
3. Check if provider is being saved in session files

---

## Summary

✅ **Fixed**: Provider specification for Ollama models (ULTRON, KAIJU)  
✅ **Fixed**: Error handling and auto-recovery for Bedrock errors  
✅ **Added**: Diagnostic script for identifying issues  
✅ **Documented**: Root cause, solution, and prevention  

**Status**: All agent chat sessions should now resume correctly without Bedrock routing errors.

---

**Last Updated**: 2025-01-02  
**Maintained By**: @JARVIS @MARVIN
