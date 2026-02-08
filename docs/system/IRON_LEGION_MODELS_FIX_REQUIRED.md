# @DOIT @TRIAGE: Iron Legion Models - Fix Required

**Date**: 2026-01-09
**Status**: ⚠️ **ACTION REQUIRED**

---

## Summary

4 of 7 Iron Legion models are not working due to missing or inaccessible model files.

## Current Status

| Mark     | Model              | Status       | Issue                                        |
| -------- | ------------------ | ------------ | -------------------------------------------- |
| Mark I   | codellama:13b      | ✅ Working    | -                                            |
| Mark II  | llama3.2:11b       | ❌ Restarting | Model file missing                           |
| Mark III | qwen2.5-coder:1.5b | ❌ Restarting | Model file exists but container can't access |
| Mark IV  | llama3:8b          | ✅ Working    | -                                            |
| Mark V   | mistral:7b         | ✅ Working    | -                                            |
| Mark VI  | mixtral:8x7b       | ❌ Restarting | Model file exists but container can't access |
| Mark VII | gemma:2b           | ❌ Restarting | Model file missing                           |

## Model Files Status

### ✅ Available Models (in shared volume)
- `/models/codellama-13b.Q4_K_M.gguf` ✅
- `/models/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf` ✅
- `/models/mistral-7b-v0.1.Q4_K_M.gguf` ✅
- `/models/mixtral-8x7b-v0.1.Q4_K_M.gguf` ✅ (25GB)
- `/models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf` ✅ (1.1GB)

### ❌ Missing Models
- `/models/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf` (Mark II)
- `/models/gemma-2b-it.Q4_K_M.gguf` (Mark VII)

## Root Cause

1. **Mark II & Mark VII**: Model files don't exist - need to be downloaded
2. **Mark III & Mark VI**: Model files exist but containers are in restart loop, possibly due to:
   - Model loading errors
   - GPU memory issues
   - Container configuration issues

## Fix Required

### Immediate Actions

1. **Download Missing Models** (Mark II & Mark VII):
   ```bash
   ssh 10.17.17.11
   docker exec -it iron-legion-mark-i-codellama-llamacpp bash
   cd /models

   # Download Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf
   # Download gemma-2b-it.Q4_K_M.gguf
   ```

2. **Fix Mark III & Mark VI**:
   - Check container logs for specific errors
   - Verify GPU memory availability
   - Check if model files are accessible from containers

### Investigation Steps

1. Check container logs:
   ```bash
   ssh 10.17.17.11
   docker logs iron-legion-mark-iii-qwen-llamacpp --tail 50
   docker logs iron-legion-mark-vi-mixtral-llamacpp --tail 50
   ```

2. Verify model file accessibility:
   ```bash
   docker exec iron-legion-mark-i-codellama-llamacpp ls -lh /models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf
   docker exec iron-legion-mark-i-codellama-llamacpp ls -lh /models/mixtral-8x7b-v0.1.Q4_K_M.gguf
   ```

3. Check GPU memory:
   ```bash
   nvidia-smi
   ```

## Expected Outcome

After fixes:
- ✅ All 7 models operational
- ✅ Expert router can route to all experts
- ✅ 100% Iron Legion availability

## Files Created

- `scripts/python/fix_all_iron_legion_models.py` - Comprehensive fix script
- `scripts/python/download_iron_legion_models.py` - Model download helper
- `scripts/python/fix_iron_legion_containers.py` - Container fix script

---

**Status**: ⚠️ **PENDING MODEL DOWNLOADS**
**Priority**: HIGH
**Last Updated**: 2026-01-09
