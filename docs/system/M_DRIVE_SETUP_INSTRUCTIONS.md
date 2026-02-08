# M Drive Setup Instructions - Iron Legion Models

**Date**: 2026-01-09
**Protocol**: @DOIT @BAU @TRIAGE @END2END
**Status**: ⚠️ **REQUIRES MANUAL MAPPING**

## Overview

The M drive needs to be mapped to the NAS (`\\10.17.17.32\models`) to access the missing Iron Legion model files. Once mapped, models will be copied to `D:\Ollama\models` and containers will be restarted.

## Quick Setup

### Option 1: Run Automated Script (Recommended)

1. **SSH to KAIJU_NO_8**:
   ```powershell
   ssh 10.17.17.11
   ```

2. **Run the setup script**:
   ```powershell
   cd C:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\startup
   .\map_m_drive_and_fix_models.ps1
   ```

3. **Enter NAS credentials when prompted** (if required)

### Option 2: Manual Mapping

1. **Map M drive manually**:
   ```powershell
   net use M: \\10.17.17.32\models /persistent:yes
   ```
   (Enter NAS credentials when prompted)

2. **Verify M drive is accessible**:
   ```powershell
   Test-Path M:\
   Get-ChildItem M:\
   ```

3. **Search for models**:
   ```powershell
   Get-ChildItem M:\ -Recurse -Filter "*.gguf" | Where-Object { $_.Name -like "*llama*3.2*" -or $_.Name -like "*gemma*" }
   ```

4. **Copy models to D:/Ollama/models**:
   ```powershell
   $modelsPath = "D:\Ollama\models"
   # Find and copy Mark II model
   $markII = Get-ChildItem M:\ -Recurse -Filter "*llama*3.2*.gguf" | Select-Object -First 1
   if ($markII) { Copy-Item $markII.FullName -Destination "$modelsPath\$($markII.Name)" -Force }

   # Find and copy Mark VII model
   $markVII = Get-ChildItem M:\ -Recurse -Filter "*gemma*2b*.gguf" | Select-Object -First 1
   if ($markVII) { Copy-Item $markVII.FullName -Destination "$modelsPath\$($markVII.Name)" -Force }
   ```

5. **Restart containers**:
   ```powershell
   docker restart iron-legion-mark-ii-llama32-llamacpp
   docker restart iron-legion-mark-vii-gemma-llamacpp
   ```

6. **Verify status**:
   ```powershell
   docker ps --filter "name=iron-legion" --format "{{.Names}}\t{{.Status}}"
   ```

## Expected Models

### Mark II (llama3.2:11b)
- **Expected filename**: `Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- **Alternative names to search for**:
  - `*llama*3.2*`
  - `*llama-3.2-11b*`
  - `*Llama-3.2*`

### Mark VII (gemma:2b)
- **Expected filename**: `gemma-2b-it.Q4_K_M.gguf`
- **Alternative names to search for**:
  - `*gemma*2b*`
  - `*gemma-2b-it*`
  - `*Gemma-2b*`

## Current Status

### Working Models (3/7)
- ✅ Mark I: codellama-13b.Q4_K_M.gguf
- ✅ Mark IV: Meta-Llama-3-8B-Instruct.Q4_K_M.gguf
- ✅ Mark V: mistral-7b-v0.1.Q4_K_M.gguf

### Models with Files but Container Issues (2/7)
- ⚠️ Mark III: qwen2.5-coder-1.5b-instruct-q4_k_m.gguf (file exists, container can't load)
- ⚠️ Mark VI: mixtral-8x7b-v0.1.Q4_K_M.gguf (file exists, container can't load)

### Missing Models (2/7)
- ❌ Mark II: Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf (needs to be found/copied from M drive)
- ❌ Mark VII: gemma-2b-it.Q4_K_M.gguf (needs to be found/copied from M drive)

## Troubleshooting

### M Drive Won't Map

1. **Check network connectivity**:
   ```powershell
   Test-Connection 10.17.17.32
   ```

2. **Check if share exists**:
   ```powershell
   Get-ChildItem \\10.17.17.32\ -ErrorAction SilentlyContinue
   ```

3. **Try different share names**:
   - `\\10.17.17.32\models`
   - `\\10.17.17.32\Models`
   - `\\10.17.17.32\ollama`
   - `\\10.17.17.32\Ollama`

### Models Not Found on M Drive

1. **Search all drives**:
   ```powershell
   Get-PSDrive -PSProvider FileSystem | ForEach-Object {
       Write-Host "Searching $($_.Name): drive..."
       Get-ChildItem "$($_.Root)" -Recurse -Filter "*llama*3.2*.gguf" -ErrorAction SilentlyContinue
       Get-ChildItem "$($_.Root)" -Recurse -Filter "*gemma*2b*.gguf" -ErrorAction SilentlyContinue
   }
   ```

2. **Check Docker volume mount**:
   ```powershell
   docker inspect iron-legion-mark-i-codellama-llamacpp --format '{{range .Mounts}}{{println .Source}}{{end}}'
   ```

### Containers Still Restarting After Copying Models

1. **Check container logs**:
   ```powershell
   docker logs iron-legion-mark-ii-llama32-llamacpp --tail 50
   docker logs iron-legion-mark-vii-gemma-llamacpp --tail 50
   ```

2. **Verify model file integrity**:
   ```powershell
   docker exec iron-legion-mark-i-codellama-llamacpp bash -c "head -c 100 /models/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf | od -A x -t x1z | head -1"
   # Should show "GGUF" magic bytes
   ```

3. **Check GPU memory**:
   ```powershell
   nvidia-smi
   ```

## Next Steps

After M drive is mapped and models are copied:

1. ✅ Verify all 7 models are accessible
2. ✅ Fix container loading issues for Mark III and Mark VI
3. ✅ Test all models via expert router
4. ✅ Integrate into health checks
5. ✅ Update documentation

---

**Last Updated**: 2026-01-09
**Status**: ⚠️ **AWAITING M DRIVE MAPPING**
