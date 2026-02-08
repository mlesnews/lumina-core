# Cursor Local AI Configuration Fix

## Problem
Error: "The model Ultron does not work with your current plan or api key."

**Root Cause**: Cursor is trying to use "Ultron" as a cloud-based model, but "Ultron" is a local cluster alias, not an actual model name.

## Solution

### Step 1: Configure Ollama Endpoint in Cursor

1. Open Cursor Settings:
   - Press `Ctrl+,` (or `Cmd+,` on Mac)
   - Or go to: File → Preferences → Settings

2. Search for "Ollama" in settings

3. Set the Ollama endpoint to one of these:
   - **Primary (KAIJU)**: `http://kaiju_no_8:11437` or `http://10.17.17.32:11437`
   - **Fallback (Local)**: `http://localhost:11434`

4. Enable "Use Ollama" or "Local Models"

### Step 2: Select an Actual Model Name

Instead of "Ultron", select one of these actual model names:

**Available Models:**

#### KAIJU Iron Legion Models (Primary - Port 11437):
- `codellama:13b` - Code generation, debugging, refactoring
- `llama3.2:11b` - General purpose, balanced tasks
- `qwen2.5-coder:1.5b-base` - Quick code tasks
- `llama3:8b` - General purpose
- `mistral:7b` - Logic, reasoning, analysis
- `mixtral-8x7b` - Complex tasks
- `gemma:2b` - Lightweight tasks

#### Local Laptop Models (Fallback - Port 11434):
- `qwen2.5:72b` - Large general purpose model
- `llama3` - General purpose
- `codellama:13b` - Code tasks

### Step 3: Verify Ollama is Running

#### Check KAIJU (Primary):
```powershell
# Test KAIJU connection
curl http://kaiju_no_8:11437/api/tags
# Or
curl http://10.17.17.32:11437/api/tags
```

#### Check Local (Fallback):
```powershell
# Test local Ollama
curl http://localhost:11434/api/tags
```

### Step 4: Quick Fix - Use Model Dropdown

1. In Cursor, look for the model selector (usually in the top right or chat interface)
2. Click the dropdown that currently shows "Ultron"
3. Select "Add Model" or "Configure Models"
4. Choose "Ollama" as provider
5. Enter endpoint: `http://localhost:11434` (or KAIJU endpoint)
6. Select an actual model like `qwen2.5:72b` or `codellama:13b`

## Configuration Reference

### Recommended Settings

**For Local Development (Laptop):**
- Endpoint: `http://localhost:11434`
- Model: `qwen2.5:72b` (if available) or `llama3`

**For KAIJU Cluster (Best Performance):**
- Endpoint: `http://kaiju_no_8:11437` or `http://10.17.17.32:11437`
- Model: `codellama:13b` (for code) or `llama3.2:11b` (general)

### Model Selection Guide

| Task Type | Recommended Model | Endpoint |
|-----------|------------------|----------|
| Code Generation | `codellama:13b` | KAIJU (11437) |
| General Chat | `llama3.2:11b` | KAIJU (11437) |
| Quick Tasks | `qwen2.5-coder:1.5b-base` | KAIJU (11437) |
| Complex Reasoning | `mistral:7b` | KAIJU (11437) |
| Large Context | `qwen2.5:72b` | Local (11434) |
| Fallback | `llama3` | Local (11434) |

## Troubleshooting

### Issue: "Connection refused" or "Cannot connect"
**Solution**: 
1. Ensure Ollama is running on the target machine
2. Check firewall settings
3. Verify the endpoint URL is correct
4. Try the fallback endpoint

### Issue: "Model not found"
**Solution**:
1. List available models: `ollama list` (if Ollama CLI is available)
2. Or check via API: `curl http://localhost:11434/api/tags`
3. Use one of the models listed in the response

### Issue: Still seeing "Ultron" error
**Solution**:
1. Close and restart Cursor
2. Clear Cursor cache if needed
3. Make sure you're selecting an actual model name, not "Ultron"

## Verification

After configuration, test by:
1. Opening Cursor chat
2. Sending a simple message
3. Verify it uses the local model (should be fast, no API costs)

## Related Files

- `config/cursor_ultron_model_config.json` - ULTRON cluster configuration
- `config/local_ai_config.json` - Local AI settings
- `config/iron_legion_cluster_config.json` - Iron Legion cluster details

## Notes

- "Ultron" is a **cluster alias**, not a model name
- Cursor needs actual Ollama model names (e.g., `qwen2.5:72b`)
- The ULTRON cluster automatically routes to the best model, but Cursor needs direct model names
- Always use the actual model name in Cursor's model selector
