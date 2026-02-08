# ULTRON Local-Only Setup Guide

## Problem

ULTRON is a **LOCAL** Ollama model, but Cursor may try to route it to AWS Bedrock (cloud), causing errors like:
- "ULTRON Virtual Cluster model is not available for your subscription plan and api key"
- "Selected model is not supported by bedrock"

## Solution

ULTRON must be configured as **LOCAL ONLY** with explicit settings to prevent cloud routing.

## Configuration Requirements

ULTRON must have these settings in `.cursor/settings.json`:

```json
{
  "name": "ULTRON",
  "title": "ULTRON",
  "provider": "ollama",
  "localOnly": true,
  "skipProviderSelection": true,
  "apiBase": "http://localhost:11434",
  "model": "qwen2.5:72b"
}
```

### Key Settings Explained

1. **`"localOnly": true`**
   - Tells Cursor this is a LOCAL model
   - Prevents routing to cloud providers (Bedrock, OpenAI, etc.)

2. **`"skipProviderSelection": true`**
   - Skips the provider selection dialog
   - Prevents user from accidentally selecting a cloud provider

3. **`"provider": "ollama"`**
   - Explicitly sets provider to Ollama
   - Ensures Cursor knows to use local Ollama instance

4. **`"apiBase": "http://localhost:11434"`**
   - Points to local Ollama instance
   - Must be localhost (not a cloud endpoint)

## Fix Scripts

Run these scripts to ensure ULTRON is configured correctly:

```bash
# Fix ULTRON to be local-only
python scripts/python/fix_ultron_local_only.py

# Disable Bedrock routing for local models
python scripts/python/disable_bedrock_for_local_models.py

# Fix session provider fields
python scripts/python/fix_session_provider_fields.py
```

## After Making Changes

**⚠️ IMPORTANT: Restart Cursor after making configuration changes!**

The settings are only read when Cursor starts, so changes won't take effect until you restart.

## Verification

To verify ULTRON is configured correctly:

```bash
python scripts/python/verify_ultron_cluster.py
```

Expected output:
- ✅ ULTRON is set as default agent model
- ✅ Provider: ollama
- ✅ Local Only: True
- ✅ API Base: http://localhost:11434

## AWS Bedrock

**Question: Should AWS Bedrock be set up?**

**Answer:** Only if you want to use cloud models. If you're using ULTRON (local), you don't need Bedrock.

If you DO want to use Bedrock for other models:
1. Set up AWS credentials
2. Configure Bedrock models in Cursor settings
3. Ensure ULTRON has `localOnly: true` to prevent routing

If you DON'T want to use Bedrock:
- You can ignore Bedrock setup
- ULTRON will work fine as a local model
- The error about subscription/API key should go away after fixing ULTRON config and restarting Cursor

## Troubleshooting

### Error: "subscription plan and api key"

**Cause:** Cursor is trying to route ULTRON to a cloud provider (Bedrock, OpenAI, etc.)

**Fix:**
1. Run `python scripts/python/fix_ultron_local_only.py`
2. Verify settings have `localOnly: true`, `provider: "ollama"`
3. **Restart Cursor**

### Error persists after restart

1. Check `.cursor/settings.json` - verify ULTRON has all required fields
2. Check all model sections (agent, chat, composer, inlineCompletion)
3. Verify Ollama is running: `curl http://localhost:11434/api/tags`
4. Check Cursor logs for routing decisions

## Tags

#ULTRON #LOCAL #OLLAMA #BEDROCK #FIX #TROUBLESHOOTING
