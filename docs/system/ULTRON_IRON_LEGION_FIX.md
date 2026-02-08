# ULTRON / Iron Legion Configuration Fix

## Issue

**Problem**: Cursor IDE shows error "Your subscription plan does not support the Iron Legion model" or "API key" error when trying to use Iron Legion, even though it's a local Ollama LLM that doesn't require an API key or subscription.

**Root Cause**: Cursor is trying to validate "Iron Legion" as if it's a cloud model, when it should recognize it as a local Ollama model.

## Solution

### 1. Fixed Configuration

The `.cursor/settings.json` has been updated to:
- ✅ Ensure ULTRON is the default agent model (not "Iron Legion")
- ✅ Remove any standalone "Iron Legion" model entries that cause validation issues
- ✅ Ensure all Ollama models have `localOnly: true`
- ✅ Ensure all Ollama models have `skipProviderSelection: true`
- ✅ Remove any API key requirements from local models
- ✅ Ensure ULTRON cluster configuration is present

### 2. Model Naming

**Important**: "Iron Legion" is now only referenced as part of "KAIJU (Iron Legion)" - it's not a standalone model name. This prevents Cursor from trying to validate it as a cloud model.

**Available Models**:
1. **ULTRON** - Default agent model (Virtual Hybrid Cluster)
   - Local: `http://localhost:11434`
   - KAIJU: `http://10.17.17.32:11434`
   - Model: `qwen2.5:72b`

2. **ULTRON Router** - Smart routing
   - Endpoint: `http://10.17.17.32:3008`
   - Model: `qwen2.5:72b`

3. **KAIJU (Iron Legion)** - NAS-based cluster
   - Endpoint: `http://10.17.17.32:11434`
   - Model: `llama3.2:3b`
   - Note: This is the "Iron Legion" - it's properly configured as local-only

### 3. ULTRON Virtual Hybrid Cluster

The ULTRON cluster is configured as a virtual hybrid cluster with:
- **Type**: `virtual_hybrid`
- **Nodes**:
  1. ULTRON Local (`http://localhost:11434`) - Priority 1
  2. KAIJU (`http://10.17.17.32:11434`) - Priority 2
- **Routing**: `load_balanced`

This cluster should appear in Cursor's model selector as "ULTRON" with cluster capabilities.

## Verification

Run the verification script:

```bash
python scripts/python/verify_ultron_cluster.py
```

This will check:
- ✅ Agent model configuration
- ✅ Endpoint accessibility
- ✅ Model availability
- ✅ Cluster configuration

## Troubleshooting

### If ULTRON cluster doesn't appear:

1. **Reload Cursor**: Close and reopen Cursor IDE
2. **Check Settings**: Verify `.cursor/settings.json` has ULTRON cluster config
3. **Check Model Selector**: In Cursor, click the model selector (top-right) and look for "ULTRON"
4. **Check Agent Settings**: Go to Cursor Settings > Features > Agent and verify default model is "ULTRON"

### If still getting "Iron Legion" error:

1. **Don't select "Iron Legion" directly** - Use "ULTRON" or "KAIJU (Iron Legion)" instead
2. **Check User Settings**: Cursor user settings might override workspace settings
   - Go to `File > Preferences > Settings` (or `Ctrl+,`)
   - Search for "agent" or "model"
   - Ensure no cloud models are selected
3. **Clear Cursor Cache**: 
   - Close Cursor
   - Delete `%APPDATA%\Cursor\Cache` (Windows) or `~/Library/Application Support/Cursor/Cache` (Mac)
   - Restart Cursor

### If endpoints are not accessible:

1. **ULTRON Local** (`localhost:11434`):
   ```bash
   # Check if Ollama is running
   curl http://localhost:11434/api/tags
   ```

2. **KAIJU** (`10.17.17.32:11434`):
   ```bash
   # Check if KAIJU is accessible
   ping 10.17.17.32
   curl http://10.17.17.32:11434/api/tags
   ```

3. **ULTRON Router** (`10.17.17.32:3008`):
   ```bash
   # Check if router is running
   curl http://10.17.17.32:3008/health
   ```

## Configuration Files

- **Workspace Settings**: `.cursor/settings.json`
- **KAIJU Config**: `config/kaiju_iron_legion_config.json`
- **ULTRON Cluster Config**: `config/ultron_hybrid_cluster.json`

## Key Points

1. ✅ **ULTRON is the default** - Use ULTRON, not "Iron Legion"
2. ✅ **All models are local** - No API keys or subscriptions needed
3. ✅ **Cluster is configured** - ULTRON uses both local and KAIJU nodes
4. ✅ **Iron Legion = KAIJU** - It's the same system, just different names

## Tags

@ULTRON @KAIJU @IRON_LEGION #LOCAL_AI #OLLAMA #CURSOR_CONFIG
