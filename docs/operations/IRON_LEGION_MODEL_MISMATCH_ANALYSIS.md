# Iron Legion Model Mismatch Analysis
                    -LUM THE MODERN

**Date**: 2026-01-17  
**Issue**: Multiple Iron Legion nodes using the same model (`qwen2.5-coder:1.5b`)

---

## 🎯 Intended Configuration

According to `config/iron_legion_experts_config.json`:

| Node | Intended Model | Purpose | Status |
|------|----------------|---------|--------|
| **Mark I** | `codellama:13b` | Code Expert | ✅ Working |
| **Mark II** | `llama3.2:11b` | General Purpose | ⚠️ **MISMATCH** |
| **Mark III** | `qwen2.5-coder:1.5b-base` | Quick Response | ✅ Correct |
| **Mark IV** | `llama3:8b` | Balanced Expert | ✅ Working |
| **Mark V** | `mistral:7b` | Reasoning Expert | ✅ Working |
| **Mark VI** | `mixtral:8x7b` | Complex Expert | ⚠️ **MISMATCH** |
| **Mark VII** | `gemma:2b` | Fallback Expert | ⚠️ **MISMATCH** |

---

## 🔍 Current Reality

### What's Actually Loaded:

| Node | Current Model(s) | Issue |
|------|------------------|-------|
| **Mark I** | `codellama:13b` | ✅ Correct |
| **Mark II** | `qwen2.5-coder:1.5b`, `gemma:2b` | ❌ Should be `llama3.2:11b` |
| **Mark III** | `qwen2.5-coder:1.5b` | ✅ Correct (close enough) |
| **Mark IV** | `llama3` | ✅ Correct |
| **Mark V** | `mistral` | ✅ Correct |
| **Mark VI** | `qwen2.5-coder:1.5b` | ❌ Should be `mixtral:8x7b` |
| **Mark VII** | `qwen2.5-coder:1.5b` | ❌ Should be `gemma:2b` |

---

## 🐛 Problem

**Three nodes (Mark II, Mark VI, Mark VII) are using `qwen2.5-coder:1.5b` instead of their intended specialized models.**

This defeats the purpose of having specialized experts:
- **Mark II** should be general purpose (`llama3.2:11b`)
- **Mark VI** should handle complex tasks (`mixtral:8x7b`)
- **Mark VII** should be lightweight fallback (`gemma:2b`)

---

## 🔧 Root Cause

1. **Shared Docker Volume**: All Iron Legion containers share the same volume (`iron-legion-data:/root/.ollama`), so they all have access to the same model pool
2. **OLLAMA_MODEL Not Enforced**: The `OLLAMA_MODEL` environment variable in Docker Compose may not be forcing each container to use its specific model
3. **Models Not Pulled**: The intended models (`llama3.2:11b`, `mixtral:8x7b`) may not be available in the shared volume
4. **Fallback Behavior**: Containers are using whatever models are available (`qwen2.5-coder:1.5b`, `gemma:2b`) instead of their intended specialized models

---

## ✅ Solution

### Immediate Actions:

1. **SSH to KAIJU (10.17.17.11) and Pull Missing Models**:
   ```bash
   # Pull models into the shared volume
   ollama pull llama3.2:11b
   ollama pull mixtral:8x7b
   ```

2. **Restart Containers to Enforce Model Assignment**:
   ```bash
   # On KAIJU, restart the containers
   docker-compose -f containerization/docker-compose.iron-legion.yml restart iron-man-mark-ii
   docker-compose -f containerization/docker-compose.iron-legion.yml restart iron-man-mark-vi
   ```

3. **Alternative: Use Separate Volumes** (if OLLAMA_MODEL doesn't work):
   - Modify `docker-compose.iron-legion.yml` to use separate volumes per container
   - This ensures each container only has access to its intended model

4. **Verify Model Assignment**:
   - Run the analysis script again: `python scripts/python/fix_iron_legion_model_assignments.py`
   - Confirm each node is using its intended model

---

## 📊 Impact

### Current State:
- ✅ **4/7 nodes** have correct models
- ⚠️ **3/7 nodes** using wrong model (`qwen2.5-coder:1.5b`)
- ❌ **Specialization lost** for Mark II, VI, VII

### After Fix:
- ✅ **7/7 nodes** with correct specialized models
- ✅ **Full expert specialization** restored
- ✅ **Optimal routing** based on task type

---

## 🎯 Next Steps

1. **Check Model Availability**:
   - Verify if `llama3.2:11b`, `mixtral:8x7b`, `gemma:2b` are available
   - Check if they need to be downloaded

2. **Deploy Models**:
   - Pull missing models to correct nodes
   - Verify model loading

3. **Update Battle Test**:
   - Re-run Phase 1 to verify correct models
   - Confirm specialization is working

---

*Analysis: 2026-01-17*  
*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
