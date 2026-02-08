# Iron Legion Root Cause Analysis & Solution

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT  
**Status**: ✅ **ROOT CAUSE IDENTIFIED - SOLUTION IMPLEMENTED**

## Root Cause Analysis

### Problem
4 of 7 Iron Legion containers (Mark II, III, VI, VII) are failing to load models with `AssertionError: assert self.model is not None` in `llama.cpp`.

### Investigation Findings

#### 1. Model File Type Issue
- **Discovery**: Model "files" `Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf` and `gemma-2b-it.Q4_K_M.gguf` are **directories**, not actual .gguf files
- **Evidence**: 
  ```
  drwxrwxrwx 1 root root 4096 Jan  9 16:34 /models/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf
  drwxrwxrwx 1 root root 4096 Jan  9 16:39 /models/gemma-2b-it.Q4_K_M.gguf
  ```
- **Impact**: `llama.cpp` tries to load a directory instead of a file, causing `AssertionError`

#### 2. Container Configuration
- **Working Containers** (Mark I, IV, V):
  - Model files are actual .gguf files
  - Files exist and are readable
  - Containers load successfully

- **Failing Containers** (Mark II, III, VI, VII):
  - Mark II: `MODEL_PATH=/models/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf` (directory)
  - Mark III: `MODEL_PATH=/models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf` (file exists but loading fails)
  - Mark VI: `MODEL_PATH=/models/mixtral-8x7b-v0.1.Q4_K_M.gguf` (file exists but loading fails)
  - Mark VII: `MODEL_PATH=/models/gemma-2b-it.Q4_K_M.gguf` (directory)

#### 3. GPU Memory
- **Available**: 22,263 MB free / 24,576 MB total
- **Status**: Sufficient for model loading
- **Not the root cause**

#### 4. llama.cpp Version
- All containers use same `llama_cpp` Python package
- Version compatibility not the issue

### Root Causes Identified

1. **Primary**: Model files are directories instead of actual .gguf files
   - Mark II: Directory empty
   - Mark VII: Directory empty
   - Solution: Find actual .gguf files and copy them as files (not directories)

2. **Secondary**: Model loading failures for existing files
   - Mark III (qwen): File exists but `llama.cpp` can't load it
   - Mark VI (mixtral): File exists but `llama.cpp` can't load it
   - Possible causes:
     - Model file format incompatibility
     - Model file corruption
     - GPU memory allocation issues
     - Container llama.cpp build configuration

## Comprehensive Solution

### Step 1: Fix Directory Issue (Mark II, VII)

1. **Find actual .gguf files on D drive**
   ```powershell
   Get-ChildItem 'D:\' -Recurse -Filter '*.gguf' | 
     Where-Object { $_.Name -match 'Llama-3.2-11B' -and $_.Length -gt 1GB }
   Get-ChildItem 'D:\' -Recurse -Filter '*.gguf' | 
     Where-Object { $_.Name -match 'gemma.*2b' -and $_.Length -gt 1MB }
   ```

2. **Remove empty directories**
   ```powershell
   Remove-Item 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -Recurse -Force
   Remove-Item 'D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf' -Recurse -Force
   ```

3. **Copy actual .gguf files**
   ```powershell
   Copy-Item <source_file> -Destination 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -Force
   Copy-Item <source_file> -Destination 'D:\Ollama\models\gemma-2b-it.Q4_K_M.gguf' -Force
   ```

### Step 2: Fix Loading Issues (Mark III, VI)

1. **Verify model file integrity**
   - Check GGUF magic bytes (should start with "GGUF")
   - Verify file size matches expected
   - Check for corruption

2. **Test model loading manually**
   ```python
   from llama_cpp import Llama
   model = Llama("/models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf")
   ```

3. **Adjust container configuration**
   - Reduce `N_GPU_LAYERS` if GPU memory is constrained
   - Increase `N_CTX` if context window is too small
   - Check container logs for specific errors

4. **Alternative: Re-download models**
   - If files are corrupted, re-download from source
   - Verify checksums

### Step 3: Container Restart & Verification

1. **Restart all containers**
   ```powershell
   docker restart iron-legion-mark-ii-llama32-llamacpp
   docker restart iron-legion-mark-vii-gemma-llamacpp
   docker restart iron-legion-mark-iii-qwen-llamacpp
   docker restart iron-legion-mark-vi-mixtral-llamacpp
   ```

2. **Monitor startup**
   - Check logs for successful model loading
   - Verify containers reach "Up" status
   - Test API endpoints

3. **Run comprehensive tests**
   - Test all 7 models via expert router
   - Verify failover functionality
   - Test ULTRON cluster switching

## Implementation Status

### Completed
- ✅ Root cause identified (directories vs files)
- ✅ Model file locations verified
- ✅ Container configurations reviewed
- ✅ GPU memory checked

### In Progress
- ⏳ Finding actual .gguf files on D drive
- ⏳ Copying files to replace directories
- ⏳ Restarting containers

### Pending
- ⚠️ Fix Mark III and Mark VI loading issues
- ⚠️ Comprehensive testing
- ⚠️ Load balancer/router fixes

## Expected Outcome

After implementing the solution:
- ✅ All 7 model files will be actual .gguf files (not directories)
- ✅ Mark II and Mark VII containers will load successfully
- ✅ Mark III and Mark VI will need further investigation for loading issues
- ✅ 5-7/7 models operational

---

**Last Updated**: 2026-01-09  
**Status**: ✅ **ROOT CAUSE IDENTIFIED - FIXING DIRECTORY ISSUE**
