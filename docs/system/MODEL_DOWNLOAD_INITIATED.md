# Missing Model Download - Initiated ✅

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT  
**Status**: ✅ **DOWNLOAD INITIATED - M DRIVE**

## Executive Summary

After due diligence search failed to locate missing model files, downloading directly to M drive (NAS models share) using Internet Download Manager or direct download method.

## Missing Models

### Mark II - Llama-3.2-11B-Vision-Instruct
- **File**: `Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- **Size**: ~6GB
- **Source**: HuggingFace - `Sci-fi-vy/Llama-3.2-11B-Vision-Instruct-GGUF`
- **URL**: `https://huggingface.co/Sci-fi-vy/Llama-3.2-11B-Vision-Instruct-GGUF/resolve/main/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`

### Mark VII - gemma-2b-it
- **File**: `gemma-2b-it.Q4_K_M.gguf`
- **Size**: ~1.7GB
- **Source**: HuggingFace - `BafS/gemma-2-2b-it-Q4_K_M-GGUF`
- **URL**: `https://huggingface.co/BafS/gemma-2-2b-it-Q4_K_M-GGUF/resolve/main/gemma-2-2b-it-q4_k_m.gguf`

## Download Strategy

### M Drive Setup
- **Network Path**: `\\10.17.17.32\models`
- **Mapped Drive**: `M:\`
- **Purpose**: Permanent network storage for model files

### Download Method
1. **Primary**: Internet Download Manager (IDM) - if available
2. **Fallback**: Direct download using `Invoke-WebRequest`

### Process
1. ✅ Map M drive to NAS models share
2. ✅ Locate IDM installation
3. ⏳ Download models to M drive
4. ⏳ Verify downloads complete
5. ⏳ Copy to `D:\Ollama\models` for container use
6. ⏳ Restart containers

## Script Created

- **Location**: `D:\Dropbox\my_projects\.lumina\scripts\startup\DOWNLOAD_MISSING_MODELS.ps1`
- **Function**: Automated download and copy process
- **Features**:
  - M drive mapping verification
  - IDM detection and usage
  - Direct download fallback
  - Automatic copy to D:\Ollama\models
  - Verification and status reporting

## Next Steps

1. ⏳ Monitor download progress
2. ⏳ Verify files on M drive
3. ⏳ Copy to D:\Ollama\models
4. ⏳ Restart Mark II and Mark VII containers
5. ⏳ Validate container startup

---

**Last Updated**: 2026-01-09  
**Status**: ✅ **DOWNLOAD INITIATED - MONITORING PROGRESS**
