# M Drive Mapping - REQUIRED (Not Optional) ✅

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT  
**Status**: ✅ **SCRIPT UPDATED - M DRIVE REQUIRED**

## Update

**M Drive mapping is REQUIRED, not optional.** Script has been updated to:
1. **Require** M drive mapping before proceeding
2. Download models **directly to M drive** (primary storage)
3. Copy from M drive to `D:\Ollama\models` for container use

## Updated Process

### Step 1: M Drive Mapping (REQUIRED)
- Script checks if M drive is mapped
- If not mapped, attempts automatic mapping
- If mapping fails, script exits with instructions
- **M drive is the permanent storage location for models**

### Step 2: Download to M Drive
- Models download **directly to M drive** (`M:\`)
- Primary storage location for all .gguf files
- Network share: `\\10.17.17.32\models`

### Step 3: Copy to D Drive
- After download, files are copied to `D:\Ollama\models`
- This is for Docker container access
- Containers mount `D:\Ollama\models` as `/models`

## Model Locations

### M Drive (Primary Storage)
- `M:\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- `M:\gemma-2b-it.Q4_K_M.gguf`

### D Drive (Container Access)
- `D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- `D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf`

## Manual M Drive Mapping

If automatic mapping fails, map manually:

```powershell
net use M: \\10.17.17.32\models /persistent:yes
```

Then re-run the download script.

---

**Last Updated**: 2026-01-09  
**Status**: ✅ **M DRIVE REQUIRED - SCRIPT UPDATED**
