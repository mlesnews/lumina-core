# Iron Legion Model Deployment Status

**Date:** 2026-01-17  
**Status:** 🔄 In Progress

## Current Status

### Llama 3.2 11B Model
- ✅ **File Found**: `\\10.17.17.32\backups\MATT_Backups\models\ollama\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- ✅ **Size**: 5.55 GB (valid)
- ✅ **Location**: Correct (NAS models/ollama directory)
- ⚠️  **Deployment**: Failed - Model name format issue

### Mixtral 8x7B Model
- ❌ **File Status**: Not found (still downloading or needs to be queued)
- ⚠️  **Deployment**: Cannot proceed until file is available

## Issues Identified

### 1. Model Name Format
- **Error**: `Error: pull model manifest: file does not exist`
- **Cause**: The model name `llama3.2:11b` may not exist in Ollama's registry
- **Solution**: Need to verify correct model name or import GGUF file directly

### 2. Container Names
- ✅ **Fixed**: Updated deployment script to use correct container names:
  - `iron-legion-mark-ii-ollama` (was `iron-man-mark-ii-llama3-2-11b`)
  - `iron-legion-mark-vi-ollama` (was `iron-man-mark-vi-mixtral-8x7b`)

### 3. GGUF Import Process
- **Status**: Need to determine if we should:
  1. Import GGUF file directly into Ollama
  2. Use correct Ollama model name format
  3. Copy file to KAIJU and import locally

## Next Steps

1. **Verify Model Name Format**
   - Check Ollama registry for correct `llama3.2:11b` format
   - Or determine if we need to use `llama3.2-11b` or similar

2. **Import GGUF File**
   - Copy GGUF file from NAS to KAIJU
   - Import into Ollama using `ollama create` or `ollama import`

3. **Complete Mixtral Download**
   - Monitor IDM for Mixtral download completion
   - Move to correct NAS location when ready

4. **Deploy and Restart**
   - Deploy models to containers
   - Restart Iron Legion containers
   - Verify model assignments

## Commands Reference

```bash
# Check available models in container
ssh mlesn@10.17.17.11 "docker exec iron-legion-mark-ii-ollama ollama list"

# Import GGUF file (if needed)
ssh mlesn@10.17.17.11 "docker exec iron-legion-mark-ii-ollama ollama create llama3.2:11b -f /path/to/modelfile"

# Restart container
ssh mlesn@10.17.17.11 "docker restart iron-legion-mark-ii-ollama"
```

## Related Files

- `scripts/python/deploy_iron_legion_models_to_kaiju.py` - Deployment script
- `scripts/python/verify_and_move_found_models.py` - Model verification
- `scripts/python/monitor_iron_legion_downloads.py` - Download monitoring
