# IDM (Internet Download Manager) Integration with Ollama

## SYPHON Analysis ID: SYPHON-CURSOR-LOCAL-MODEL-20260113

## Problem Statement

Ollama's built-in HTTP downloader fails when:
1. Downloading to network storage (NAS)
2. Large models (>10GB) over unreliable connections
3. Connection interrupts during multi-hour downloads

## Current State

```
OLLAMA_MODELS = \\10.17.17.32\backups\OllamaModels  (NAS - PROBLEMATIC)
```

**Issue**: Network storage introduces latency and connection timeouts during large downloads.

## Solution: Local Storage + IDM for Large Models

### Quick Fix: Switch to Local Storage

```powershell
# Run the fix script
.\scripts\fix_ollama_local_storage.ps1 -Fix
.\scripts\fix_ollama_local_storage.ps1 -PullModel -Model "llama3.2:3b"
.\scripts\fix_ollama_local_storage.ps1 -SyncToNas
```

### For Large Models (>10GB): Use IDM

#### Step 1: Get Model Blob URLs

Models are stored in the Ollama registry at:
```
https://registry.ollama.ai/v2/library/{model}/manifests/{tag}
```

Example for `qwen2.5:72b`:
```bash
curl https://registry.ollama.ai/v2/library/qwen2.5/manifests/72b
```

This returns a manifest with blob digests.

#### Step 2: Download Blobs with IDM

Blob download URL pattern:
```
https://registry.ollama.ai/v2/library/{model}/blobs/sha256:{digest}
```

1. Open IDM
2. Add New Download
3. Enter blob URL
4. Save to: `C:\OllamaModels\blobs\sha256-{digest}`
5. Start download (IDM handles resume, segments, etc.)

#### Step 3: Import into Ollama

After downloading all blobs:

```powershell
# Create manifest (copy from registry)
curl https://registry.ollama.ai/v2/library/qwen2.5/manifests/72b > C:\OllamaModels\manifests\registry.ollama.ai\library\qwen2.5\72b

# Restart Ollama to detect new model
ollama serve

# Verify
ollama list
```

## Model Size Reference

| Model | Size | Download Time (100Mbps) |
|-------|------|------------------------|
| llama3.2:3b | ~2GB | ~3 min |
| qwen2.5:7b | ~4.5GB | ~6 min |
| codellama:13b | ~7GB | ~10 min |
| qwen2.5:72b | ~45GB | ~60 min |
| llama3.3:70b | ~40GB | ~55 min |

## Recommended Workflow

### Small Models (<10GB)
```powershell
ollama pull llama3.2:3b
```

### Large Models (>10GB)
1. Use IDM for blob download
2. Import manually
3. Sync to NAS for backup

## Storage Paths

| Type | Path | Purpose |
|------|------|---------|
| **Local (Active)** | `C:\OllamaModels` | Fast inference, reliable downloads |
| **NAS (Backup)** | `\\10.17.17.32\backups\OllamaModels` | Archival, multi-machine sharing |
| **KAIJU (Remote)** | `10.17.17.11:/ollama/models` | Server-side models |

## Environment Variables

```powershell
# For local storage (RECOMMENDED)
setx OLLAMA_MODELS "C:\OllamaModels"

# For NAS storage (NOT RECOMMENDED for downloads)
# setx OLLAMA_MODELS "\\10.17.17.32\backups\OllamaModels"
```

## Troubleshooting

### Model download fails/stalls
1. Check `OLLAMA_MODELS` env var
2. Switch to local storage
3. Use IDM for large models

### Cursor IDE "Invalid Model" error
1. Verify model exists: `ollama list`
2. Test API: `curl http://localhost:11434/v1/models`
3. Reload Cursor: `Ctrl+R`

### Models on NAS not detected
- NAS is for backup only
- Set `OLLAMA_MODELS` to local path
- Ollama needs low-latency access to model files

## See Also

- `scripts/fix_ollama_local_storage.ps1` - Automated fix script
- `scripts/python/fix_cursor_local_models.py` - Cursor config fixer
- `data/syphon_analysis/cursor_local_model_issue_20260113.json` - Full analysis
