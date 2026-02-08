# Cloud AI Migration for Decisioning

## Overview

This guide helps you migrate from local AI models to cloud AI (OpenAI/Anthropic) for decision-making, as local models are struggling with complex decisions.

## Why Cloud AI?

- **Better Decision Quality**: Cloud AI models (GPT-4, Claude) excel at complex reasoning
- **No Local Resource Strain**: Frees up local compute for other tasks
- **Automatic Escalation**: System automatically uses cloud AI when decisions are too complex
- **Consistent Performance**: No dependency on local model availability

## Quick Setup

### Step 1: Add Cloud AI Credentials

```bash
# Check current status
python scripts/python/configure_cloud_ai_decisioning.py --check

# Setup OpenAI
python scripts/python/configure_cloud_ai_decisioning.py --setup openai --interactive

# Setup Anthropic
python scripts/python/configure_cloud_ai_decisioning.py --setup anthropic --interactive
```

### Step 2: Verify Configuration

The system will:
1. Store API keys in Azure Key Vault
2. Create `config/cloud_ai_decisioning_config.json`
3. Update decisioning to use cloud AI

### Step 3: Test

```bash
# Test decisioning
python scripts/python/aiq_fallback_decisioning.py --check-load
```

## Configuration Details

### Cloud AI Config Location
- **File**: `config/cloud_ai_decisioning_config.json`
- **Settings**:
  - `use_cloud_ai`: `true` (enabled)
  - `escalate_to_cloud`: `true` (auto-escalate complex decisions)
  - `local_ai_disabled`: `true` (disable local models for decisioning)
  - `fallback_to_local`: `false` (don't fall back to local)

### Decisioning Behavior

When a decision is needed:
1. **Check complexity**: System evaluates if decision is too complex
2. **Escalate to cloud**: If complex, automatically uses cloud AI
3. **Use cloud AI**: GPT-4 or Claude handles the decision
4. **Return result**: Decision is returned with reasoning

## API Keys Required

### OpenAI
- **Get key**: https://platform.openai.com/api-keys
- **Stored as**: `openai-api-key` in Azure Key Vault
- **Model**: `gpt-4` (default)

### Anthropic
- **Get key**: https://console.anthropic.com/
- **Stored as**: `anthropic-api-key` in Azure Key Vault
- **Model**: `claude-3-opus-20240229` (default)

## Escalation Rules

The system escalates to cloud AI when:
- Decision complexity exceeds local model capability
- Multiple options need deep analysis
- Troubleshooting requires advanced reasoning
- AIQ consensus needs high-quality evaluation

## Monitoring

Check cloud AI usage:
```bash
# View config
cat config/cloud_ai_decisioning_config.json

# Check credentials
python scripts/python/configure_cloud_ai_decisioning.py --check
```

## Troubleshooting

### Issue: "Credentials not found"
**Solution**: Run setup again with API key
```bash
python scripts/python/configure_cloud_ai_decisioning.py --setup openai --api-key <your-key>
```

### Issue: "Still using local AI"
**Solution**: Verify config has `local_ai_disabled: true`

### Issue: "API rate limits"
**Solution**: System automatically retries with backoff

## Next Steps

1. ✅ Add cloud AI credentials
2. ✅ Configure decisioning to use cloud
3. ✅ Test with sample decisions
4. ✅ Monitor usage and costs
5. ✅ Adjust escalation thresholds as needed
