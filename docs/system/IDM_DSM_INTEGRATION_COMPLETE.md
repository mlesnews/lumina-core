# IDM and DSM Download Manager Integration ✅

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT  
**Status**: ✅ **IDM & DSM INTEGRATION COMPLETE**

## Executive Summary

Integrated Internet Download Manager (IDM) and NAS DSM Download Manager for downloading missing LLM models. Downloads are now properly queued and managed.

## Integration Components

### 1. IDM Integration Script
- **File**: `scripts/startup/DOWNLOAD_MODELS_WITH_IDM.ps1`
- **Purpose**: Add downloads to IDM queue
- **Features**:
  - Auto-detects IDM installation
  - Adds downloads to IDM queue
  - Downloads to M drive (NAS storage)
  - Starts IDM automatically

### 2. NAS DSM Download Manager Integration
- **File**: `scripts/python/nas_dsm_download_manager.py`
- **Purpose**: Programmatic integration with Synology Download Station
- **Features**:
  - Login to DSM
  - Add downloads via API
  - List download tasks
  - Get Download Station info

## Download Process

### Using IDM (Primary Method)

1. **Run the script:**
   ```powershell
   cd 'D:\Dropbox\my_projects\.lumina'
   .\scripts\startup\DOWNLOAD_MODELS_WITH_IDM.ps1
   ```

2. **Script actions:**
   - Verifies M drive mapping
   - Locates IDM installation
   - Checks for existing files
   - Adds missing downloads to IDM queue
   - Starts IDM downloads

3. **Downloads go to:**
   - Primary: `M:\` (NAS storage)
   - Then copy to: `D:\Ollama\models\` for containers

### Using DSM Download Manager (Alternative)

```bash
# Add download via DSM API
python scripts\python\nas_dsm_download_manager.py \
    --username YOUR_USERNAME \
    --password YOUR_PASSWORD \
    --add "https://huggingface.co/.../model.gguf"

# List downloads
python scripts\python\nas_dsm_download_manager.py \
    --username YOUR_USERNAME \
    --password YOUR_PASSWORD \
    --list
```

## Models Being Downloaded

### Mark II - Llama-3.2-11B-Vision-Instruct
- **File**: `Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
- **Size**: ~6GB
- **URL**: `https://huggingface.co/Sci-fi-vy/Llama-3.2-11B-Vision-Instruct-GGUF/resolve/main/Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`

### Mark VII - gemma-2b-it
- **File**: `gemma-2b-it.Q4_K_M.gguf`
- **Size**: ~1.7GB
- **URL**: `https://huggingface.co/BafS/gemma-2-2b-it-Q4_K_M-GGUF/resolve/main/gemma-2-2b-it-q4_k_m.gguf`

## IDM Command Line Syntax

The script uses IDM command line interface:

```powershell
idman.exe /d URL /p PATH /f FILENAME /n /a
```

- `/d` = Download URL
- `/p` = Save path (M:\)
- `/f` = Filename
- `/n` = Don't start immediately (queue it)
- `/a` = Add to queue
- `/s` = Start all queued downloads

## After Downloads Complete

1. **Copy files to D drive:**
   ```powershell
   Copy-Item 'M:\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' -Destination 'D:\Ollama\models\'
   Copy-Item 'M:\gemma-2b-it.Q4_K_M.gguf' -Destination 'D:\Ollama\models\'
   ```

2. **Restart containers:**
   ```powershell
   docker restart iron-legion-mark-ii-llama32-llamacpp
   docker restart iron-legion-mark-vii-gemma-llamacpp
   ```

## Monitoring Downloads

### IDM
- Open IDM interface to monitor progress
- Downloads show in IDM queue
- Progress bar and speed displayed

### DSM Download Station
- Access via web: `http://10.17.17.32:5000`
- Or use Python script to list tasks

---

**Last Updated**: 2026-01-09  
**Status**: ✅ **IDM & DSM INTEGRATION COMPLETE - DOWNLOADS INITIATED**
