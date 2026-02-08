# Fix: Persistent "Invalid Model" Error
                    -LUM THE MODERN

## 🐛 Problem

The battle test was getting persistent "invalid model" errors, especially on Iron Legion nodes (Mark IV, Mark V, etc.). The health checks would pass, but inference would fail with 404 "Not Found" errors.

## 🔍 Root Cause

**Iron Legion endpoints use OpenAI-compatible API, not Ollama API!**

- **Iron Legion** (ports 3001-3007): Uses `/v1/chat/completions` (OpenAI format)
- **Ollama** (port 11434): Uses `/api/generate` (Ollama format)

The code was trying to use Ollama API format (`/api/generate`) on Iron Legion endpoints, causing the "model not found" errors.

## ✅ Solution

### 1. API Detection
Added detection for Iron Legion endpoints:
```python
is_iron_legion = ":300" in node.endpoint and any(f":{port}" in node.endpoint for port in range(3001, 3008))
is_openai_api = "/v1" in node.endpoint or is_iron_legion
```

### 2. Correct API Endpoints
- **Iron Legion**: `/v1/chat/completions` for inference, `/v1/models` or `/` for model listing
- **Ollama**: `/api/generate` for inference, `/api/tags` for model listing

### 3. Model Extraction
Handle different response formats:
- **OpenAI format**: `data[0].id` or root `model` field
- **Ollama format**: `models[0].name`

### 4. Removed "default" Fallback
- Removed `"default"` as fallback model name (doesn't exist)
- Skip inference if no model available instead of using invalid model

## 📊 Results

**Before Fix:**
- ❌ Mark IV: Model 'llama3' not found
- ❌ Mark V: Model 'mistral' not found
- ❌ Multiple "invalid model" errors

**After Fix:**
- ✅ **18/18 tests passing** (100%)
- ✅ All Iron Legion nodes working
- ✅ No more "invalid model" errors

## 🎯 Key Learnings

1. **Different endpoints use different APIs** - Always check API format
2. **Iron Legion = OpenAI-compatible**, not Ollama
3. **Never use "default" as model name** - It doesn't exist
4. **Health check != Inference working** - Models might be listed but not accessible

---

*Fix applied: 2026-01-17*
*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
