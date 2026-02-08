# @DOIT @TRIAGE: Iron Legion M Drive Setup

**Date**: 2026-01-09
**Status**: ⚠️ **M DRIVE MAPPING REQUIRED**

---

## Summary

Iron Legion models need to be accessed from M drive. Current setup uses `D:/Ollama/models`, but models may be on M drive.

## Current Status

- **Current Mount**: `D:/Ollama/models` (bound to Docker volume)
- **Available Models**: 5/7 (codellama, llama3, mistral, mixtral, qwen)
- **Missing Models**: llama3.2 (Mark II), gemma (Mark VII)

## M Drive Setup

### Option 1: Map M Drive as Network Share

If M drive is a network share:

```powershell
# Map M drive
net use M: \\server\share /persistent:yes

# Verify
dir M:\models
```

### Option 2: Update Docker Volume to M Drive

Update the Docker volume to mount M drive:

1. **Stop containers**:
   ```bash
   docker stop iron-legion-mark-ii-llama32-llamacpp
   docker stop iron-legion-mark-iii-qwen-llamacpp
   docker stop iron-legion-mark-vi-mixtral-llamacpp
   docker stop iron-legion-mark-vii-gemma-llamacpp
   ```

2. **Update docker-compose.iron-legion.yml**:
   ```yaml
   volumes:
     iron-legion-models:
       driver: local
       driver_opts:
         type: none
         o: bind
         device: M:/models  # or M:/Ollama/models
   ```

3. **Recreate volume** (if needed):
   ```bash
   docker volume rm iron-legion-llamacpp_iron-legion-models
   docker-compose up -d
   ```

### Option 3: Copy Models from M Drive to D Drive

If models are on M drive but you want to keep D drive mount:

```powershell
# Copy missing models
Copy-Item "M:\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf" "D:\Ollama\models\"
Copy-Item "M:\models\gemma-2b-it.Q4_K_M.gguf" "D:\Ollama\models\"
```

## Verification

After mapping M drive or updating mounts:

```bash
# Check models are accessible
docker exec iron-legion-mark-i-codellama-llamacpp ls -lh /models/

# Should see:
# - Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf (Mark II)
# - gemma-2b-it.Q4_K_M.gguf (Mark VII)
```

## Next Steps

1. ✅ Map M drive (if network share)
2. ✅ Verify models are on M drive
3. ✅ Update Docker volume mount
4. ✅ Restart containers
5. ✅ Verify all 7 models working

---

**Status**: ⚠️ **PENDING M DRIVE MAPPING**
**Priority**: HIGH
**Last Updated**: 2026-01-09
