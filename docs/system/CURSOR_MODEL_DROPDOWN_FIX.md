# Cursor Model Dropdown Fix

## Issue

**Problem**: 
- ULTRON not showing in Cursor model dropdown
- Too many models configured that aren't available
- Unavailable models clutter the dropdown

**Root Cause**: 
- Cursor only shows models that are actually available
- If you configure more models than are available, they won't appear
- Model names must match exactly what's in Ollama

## Solution

### Fixed Configuration

1. **Removed Unavailable Models**:
   - ❌ Removed `codellama:13b` (not available)
   - ❌ Removed `llama3.2:11b` (not available)
   - ❌ Removed `qwen2.5-coder:1.5b-base` (not available)

2. **Kept Available Models**:
   - ✅ **ULTRON** (`qwen2.5:72b`) - Available on localhost
   - ✅ **KAIJU** (`llama3.2:3b`) - Available on KAIJU NAS

3. **Simplified ULTRON Configuration**:
   - Changed title from "ULTRON (qwen2.5:72b)" to just "ULTRON"
   - Removed complex auto-selection criteria (not needed for dropdown)
   - Kept cluster configuration for load balancing

## Current Available Models

### ULTRON (Primary)
- **Model**: `qwen2.5:72b`
- **Location**: `localhost:11434`
- **Context**: 32K tokens
- **Status**: ✅ Available

### KAIJU (Secondary)
- **Model**: `llama3.2:3b`
- **Location**: `10.17.17.32:11434`
- **Context**: 8K tokens
- **Status**: ✅ Available

## How to Verify

1. **Reload Cursor IDE** (close and reopen)
2. **Check Model Dropdown**:
   - Click model selector (top-right of Cursor)
   - You should see:
     - ✅ **ULTRON**
     - ✅ **KAIJU (llama3.2:3b)**
3. **Select ULTRON** as your agent model

## Auto Mode Behavior

When using **ULTRON with Auto Mode**:
- ULTRON cluster automatically routes between:
  - ULTRON Local (`localhost:11434`) - Primary
  - KAIJU (`10.17.17.32:11434`) - Fallback
- System picks the best endpoint based on availability
- No manual selection needed

## Adding More Models

If you want to add more models to the dropdown:

1. **Pull the model first**:
   ```bash
   # On localhost
   ollama pull codellama:13b
   
   # Or on KAIJU
   ssh kaiju_no_8
   ollama pull codellama:13b
   ```

2. **Verify it's available**:
   ```bash
   curl http://localhost:11434/api/tags
   # or
   curl http://10.17.17.32:11434/api/tags
   ```

3. **Run the fix script** to automatically add it:
   ```bash
   python scripts/python/fix_cursor_model_dropdown.py
   ```

## Key Points

1. ✅ **Only available models show** - Cursor filters out unavailable models
2. ✅ **ULTRON is visible** - Properly configured and available
3. ✅ **Auto mode works** - ULTRON cluster handles routing automatically
4. ✅ **Clean dropdown** - Only shows what you can actually use

## Troubleshooting

### If ULTRON still doesn't show:

1. **Check Ollama is running**:
   ```bash
   curl http://localhost:11434/api/tags
   ```

2. **Verify model name matches**:
   - Model name in settings: `qwen2.5:72b`
   - Must match exactly what Ollama reports

3. **Check Cursor settings**:
   - Ensure `.cursor/settings.json` has ULTRON configured
   - Verify `cursor.agent.defaultModel` is set to "ULTRON"

4. **Clear Cursor cache**:
   - Close Cursor
   - Delete cache: `%APPDATA%\Cursor\Cache` (Windows)
   - Restart Cursor

### If models disappear:

- Models will disappear if Ollama stops or model is removed
- Run the fix script to update configuration:
  ```bash
  python scripts/python/fix_cursor_model_dropdown.py
  ```

## Tags

@ULTRON @KAIJU #CURSOR_CONFIG #MODEL_SELECTION #DROPDOWN_FIX
