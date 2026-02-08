# Iron Legion - Manual Fix Instructions

**Date**: 2026-01-09  
**Status**: ⚠️ **REQUIRES MANUAL EXECUTION ON KAIJU**

## Quick Fix - Run on KAIJU

SSH to KAIJU and run these commands in PowerShell (as Administrator):

```powershell
# Step 1: Remove directories
Remove-Item 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item 'D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf' -Recurse -Force -ErrorAction SilentlyContinue

# Step 2: Find actual files
$markII = Get-ChildItem 'D:\Ollama' -Recurse -Filter 'Llama-3.2-11B*.gguf' -ErrorAction SilentlyContinue -Depth 2 | 
    Where-Object { -not $_.PSIsContainer -and $_.Length -gt 1GB } | 
    Select-Object -First 1

$markVII = Get-ChildItem 'D:\Ollama' -Recurse -Filter 'gemma-2b*.gguf' -ErrorAction SilentlyContinue -Depth 2 | 
    Where-Object { -not $_.PSIsContainer -and $_.Length -gt 1MB } | 
    Select-Object -First 1

# Step 3: Copy files
if ($markII) { 
    Copy-Item $markII.FullName -Destination 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -Force
    Write-Host "Copied Mark II: $($markII.Name)"
}

if ($markVII) { 
    Copy-Item $markVII.FullName -Destination 'D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf' -Force
    Write-Host "Copied Mark VII: $($markVII.Name)"
}

# Step 4: Verify
Test-Path 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -PathType Leaf
Test-Path 'D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf' -PathType Leaf

# Step 5: Restart containers
docker restart iron-legion-mark-ii-llama32-llamacpp iron-legion-mark-vii-gemma-llamacpp
```

## Or Run the Script File

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\startup\FIX_MODEL_FILES.ps1
```

---

**Note**: Run in administrative PowerShell session on KAIJU for best results.
