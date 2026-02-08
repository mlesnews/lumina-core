# Switch Cursor IDE to Local AI - Emergency Cost Control

**Date**: 2025-01-24  
**Status**: ⚠️ **URGENT - CLOUD API USAGE DETECTED**  
**Tag**: @ULTRON #local-ai #cost-control #cursor-config

---

## 🚨 PROBLEM: Proof of Cloud API Usage

**Evidence**:
```
You are projected to reach your usage limits by 1/16/2026 based on your current usage.
Consider switching to a different model or enabling pay-as-you-go to avoid interruptions
until your cycle resets on 1/20/2026.
```

**Current State**: Cursor IDE is using **CLOUD AI (Claude/Anthropic)** instead of local AI resources.

**Expected State**: Cursor should use **LOCAL AI (Ollama/ULTRON)** - already configured but not active.

---

## ✅ Available Local AI Resources

### ULTRON Cluster (Configured)
- **Primary Node**: KAIJU NAS (`http://10.17.17.32:11437` or `http://kaiju_no_8:11437`)
- **Fallback Node**: Laptop Local (`http://localhost:11434`)
- **Router**: ULTRON Router (`http://10.17.17.32:3008`)

### Local Models Available (via Ollama)
- `qwen2.5:72b` - High-quality general purpose (72B parameters)
- `codellama:13b` - Code generation (13B parameters)
- `llama3.2:11b` - General purpose (11B parameters)
- `qwen2.5-coder:1.5b-base` - Quick completions (1.5B parameters)
- `llama3` - General purpose (8B parameters)
- `mistral` - Reasoning (7B parameters)
- `mixtral-8x7b` - High complexity (8x7B parameters)

### Configuration Files (Already Created)
- ✅ `config/cursor_ultron_model_config.json` - ULTRON cluster config
- ✅ `config/local_ai_config.json` - Local AI endpoints
- ✅ `config/cloud_api_blocker.json` - Cloud API blocker config
- ✅ `.cursor/settings.json` - Cursor settings (needs activation)

---

## 🔧 How to Switch Cursor to Local AI

### Method 1: Cursor Settings UI (Recommended)

1. **Open Cursor Settings**:
   - Press `Ctrl+,` (or `Cmd+,` on Mac)
   - Or: File → Preferences → Settings

2. **Navigate to Models**:
   - Search for: `model` or `ollama` or `claude`
   - Look for: "Cursor → Models" section

3. **Change Default Model**:
   - Find: `cursor.chat.defaultModel`
   - Change from: `claude-sonnet` or `claude-opus` (cloud)
   - Change to: `ULTRON` or `ollama/qwen2.5:72b` (local)

4. **Add/Optimize Ollama Endpoint**:
   - Find: `cursor.ollama.endpoint`
   - Set to: `http://localhost:11434`
   - Or: `http://10.17.17.32:11437` (KAIJU NAS)

5. **Update Composer Model**:
   - Find: `cursor.composer.defaultModel`
   - Change to: `ollama/qwen2.5:72b` or `ULTRON`

6. **Update Agent Model**:
   - Find: `cursor.agent.defaultModel`
   - Change to: `ollama/qwen2.5:72b` or `ULTRON`

---

### Method 2: Edit Settings JSON Directly

1. **Open Settings JSON**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type: `Preferences: Open User Settings (JSON)`
   - Or manually edit: `%APPDATA%\Cursor\User\settings.json`

2. **Add/Update These Settings**:

```json
{
  // Disable cloud models
  "cursor.chat.defaultModel": "ULTRON",
  "cursor.composer.defaultModel": "ULTRON",
  "cursor.agent.defaultModel": "ULTRON",
  
  // Configure Ollama endpoint
  "cursor.ollama.endpoint": "http://localhost:11434",
  
  // Optional: Add custom models
  "cursor.chat.customModels": [
    {
      "name": "ULTRON",
      "provider": "ollama",
      "model": "qwen2.5:72b",
      "apiBase": "http://localhost:11434",
      "contextLength": 32768
    },
    {
      "name": "KAIJU",
      "provider": "ollama",
      "model": "llama3",
      "apiBase": "http://10.17.17.32:11437",
      "contextLength": 8192
    }
  ],
  
  // Block cloud APIs (optional but recommended)
  "cursor.chat.disabledModels": [
    "claude-sonnet",
    "claude-opus",
    "gpt-4",
    "gpt-4-turbo"
  ]
}
```

---

### Method 3: Workspace Settings (Project-Specific)

1. **Edit `.cursor/settings.json` in project root**:
   - File already exists: `.cursor/settings.json`
   - Update default models to use ULTRON/local endpoints

2. **Verify Configuration**:
   - Check that `cursor.chat.defaultModel` points to local model
   - Check that `cursor.ollama.endpoint` is set correctly

---

## ✅ Verification Steps

### 1. Check Ollama is Running

```powershell
# Check local Ollama
curl http://localhost:11434/api/tags

# Check KAIJU NAS Ollama (if available)
curl http://10.17.17.32:11437/api/tags
```

**Expected Output**: List of available models in JSON format.

### 2. Test Local Model in Cursor

1. Open Cursor Chat (`Ctrl+L`)
2. Type: "Test local model"
3. Check the model indicator (should show `ULTRON` or `ollama/qwen2.5:72b`)
4. **Should NOT show**: `claude-sonnet`, `claude-opus`, or any cloud model

### 3. Verify No Cloud API Calls

- Check Cursor usage dashboard (if available)
- Monitor network traffic (should not see calls to `api.anthropic.com`)
- Check billing/usage in Anthropic dashboard (should stop increasing)

---

## 🔍 Troubleshooting

### Problem: "Ollama endpoint not found"

**Solution**:
1. Verify Ollama is running: `curl http://localhost:11434/api/tags`
2. If not running, start Ollama:
   ```powershell
   # Docker (if using Docker)
   docker start cfs-ollama
   
   # Or native Ollama
   ollama serve
   ```

### Problem: "Model not found"

**Solution**:
1. Pull the model:
   ```bash
   ollama pull qwen2.5:72b
   ollama pull codellama:13b
   ollama pull llama3.2:11b
   ```
2. Verify model exists: `ollama list`

### Problem: "Still using cloud model"

**Solution**:
1. Restart Cursor completely
2. Clear Cursor cache (if applicable)
3. Check workspace settings override user settings
4. Verify `.cursor/settings.json` has correct configuration

### Problem: "Slow responses with local model"

**Solution**:
1. Use lighter model for quick tasks: `qwen2.5-coder:1.5b-base`
2. Use KAIJU NAS if available (better hardware)
3. Use ULTRON Router for intelligent routing

---

## 📊 Expected Results

### Before (Cloud API)
- ❌ Usage limits warning
- ❌ API costs accumulating
- ❌ Calls to `api.anthropic.com`
- ❌ Model shows: `claude-sonnet` or `claude-opus`

### After (Local AI)
- ✅ No usage limits
- ✅ Zero API costs
- ✅ Calls to `localhost:11434` or `10.17.17.32:11437`
- ✅ Model shows: `ULTRON` or `ollama/qwen2.5:72b`
- ✅ Usage dashboard shows no cloud API calls

---

## 🎯 Quick Switch Checklist

- [ ] Open Cursor Settings (`Ctrl+,`)
- [ ] Change `cursor.chat.defaultModel` to `ULTRON`
- [ ] Change `cursor.composer.defaultModel` to `ULTRON`
- [ ] Change `cursor.agent.defaultModel` to `ULTRON`
- [ ] Set `cursor.ollama.endpoint` to `http://localhost:11434`
- [ ] Verify Ollama is running: `curl http://localhost:11434/api/tags`
- [ ] Pull required models: `ollama pull qwen2.5:72b`
- [ ] Restart Cursor
- [ ] Test chat with local model
- [ ] Verify no cloud API calls in usage dashboard

---

## 📚 Related Documentation

- **ULTRON Cluster Config**: `config/cursor_ultron_model_config.json`
- **Local AI Config**: `config/local_ai_config.json`
- **Cloud API Blocker**: `config/cloud_api_blocker.json`
- **Ollama Model Mapping**: `config/ollama_model_mapping.json`
- **Cursor Settings**: `.cursor/settings.json`

---

## 🚨 Emergency Actions

If you need to **immediately stop cloud API usage**:

1. **Disable Cloud Models in Cursor**:
   - Settings → Models → Disable all Claude/GPT models
   - Or add to disabled list in settings JSON

2. **Force Local Only**:
   - Set `cursor.ollama.endpoint` to local endpoint
   - Remove/comment out cloud model configurations

3. **Block Network Access** (Last Resort):
   - Firewall rule to block `api.anthropic.com`
   - Only enable when absolutely necessary

---

**Last Updated**: 2025-01-24  
**Status**: ⚠️ **URGENT - SWITCH TO LOCAL AI IMMEDIATELY**  
**Maintained By**: @ULTRON #local-ai