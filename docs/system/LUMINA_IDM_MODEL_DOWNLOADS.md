# Lumina IDM Model Downloads

## Overview

**CRITICAL POLICY**: All GGUF files and LLM model downloads **MUST** use IDM (Internet Download Manager).

This ensures:
- ✅ **Resume Capability**: Large model files (4-20GB+) can be resumed if interrupted
- ✅ **Speed Acceleration**: IDM's acceleration helps with large model files
- ✅ **Queue Management**: Download multiple models simultaneously
- ✅ **Bandwidth Control**: Control download speed to avoid network congestion

## Model Mapping

**Source of Truth**: `config/ollama_model_mapping.json`

This file maps Ollama model names to HuggingFace repositories for IDM downloads.

### Current Models

| Ollama Model | HuggingFace Repo | GGUF File | Size |
|-------------|------------------|-----------|------|
| `codellama:13b` | `TheBloke/CodeLlama-13B-GGUF` | `codellama-13b.Q4_K_M.gguf` | ~7.5GB |
| `llama3.2:11b` | `bartowski/Llama-3.2-11B-Instruct-GGUF` | `llama-3.2-11b-instruct.Q4_K_M.gguf` | ~6.5GB |
| `qwen2.5-coder:1.5b-base` | `Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF` | `qwen2.5-coder-1.5b-instruct.Q4_K_M.gguf` | ~1.0GB |

## Download Methods

### Method 1: Automated Scripts (Recommended)

#### Docker Cluster Setup

```powershell
# Setup models for Docker cluster
.\cedarbrook-financial-services_llc-env\containerization\services\ollama\setup-iron-legion-models.ps1
```

This script:
1. Checks for IDM installation
2. Loads model mapping
3. Downloads all required models via IDM
4. Falls back to Ollama API if IDM fails

#### Standard Model Pull

```powershell
# Check and pull models with IDM
.\scripts\powershell\check_and_pull_models.ps1

# Or use the dedicated IDM script
.\scripts\powershell\pull_ollama_models_with_idm.ps1
```

### Method 2: Python Helper (Direct)

```powershell
# Download a specific model
python scripts/python/download_gguf_with_idm.py <repo_id> <filename> <model_name>

# Example
python scripts/python/download_gguf_with_idm.py TheBloke/CodeLlama-13B-GGUF codellama-13b.Q4_K_M.gguf codellama:13b
```

### Method 3: PowerShell Script (Direct)

```powershell
# Download GGUF file via IDM
.\scripts\powershell\Invoke-IDMGGUFDownload.ps1 `
    -Url "https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/resolve/main/codellama-13b.Q4_K_M.gguf" `
    -ModelName "codellama:13b" `
    -Destination "D:\Ollama\models\codellama-13b.Q4_K_M.gguf"
```

## IDM Configuration

**Source of Truth**: `config/lumina_idm_config.json`

### IDM Detection

IDM is automatically detected from:
- `C:\Program Files (x86)\Internet Download Manager\idman.exe`
- `C:\Program Files\Internet Download Manager\idman.exe`
- `D:\Program Files\Internet Download Manager\idman.exe`

### Default Download Locations

- **Ollama Models**: `D:\Ollama\models` (if `OLLAMA_MODELS` env var set)
- **Fallback**: `$env:USERPROFILE\Downloads`
- **NAS**: `Z:\downloads\models` (if available)

## Workflow

### Complete Model Setup Workflow

1. **Check IDM Installation**
   ```powershell
   # Verify IDM is installed
   Get-Command idman -ErrorAction SilentlyContinue
   ```

2. **Check Model Mapping**
   ```powershell
   # Verify model mapping exists
   Test-Path config\ollama_model_mapping.json
   ```

3. **Download Models via IDM**
   ```powershell
   # Use automated script
   .\scripts\powershell\pull_ollama_models_with_idm.ps1
   ```

4. **Monitor Downloads in IDM**
   - Open IDM application
   - Check download queue
   - Monitor progress for each model

5. **Verify Downloads**
   ```powershell
   # Check downloaded files
   Get-ChildItem D:\Ollama\models\*.gguf
   ```

6. **Import to Ollama** (if needed)
   ```powershell
   # Import GGUF file to Ollama
   ollama create codellama:13b -f Modelfile
   ```

## Troubleshooting

### IDM Not Found

**Error**: `ERROR: IDM not found!`

**Solution**:
1. Install Internet Download Manager
2. Verify installation path matches configured paths
3. Add IDM to system PATH
4. Restart PowerShell session

### Model Mapping Not Found

**Error**: `ERROR: Model mapping not found`

**Solution**:
1. Verify `config/ollama_model_mapping.json` exists
2. Check file permissions
3. Recreate mapping file if missing

### Python Helper Not Found

**Error**: `ERROR: Python helper not found`

**Solution**:
1. Verify `scripts/python/download_gguf_with_idm.py` exists
2. Check Python installation
3. Verify Python is in PATH

### Downloads Not Starting in IDM

**Possible Causes**:
1. IDM not running
2. IDM browser integration not enabled
3. Script permissions issue

**Solution**:
1. Open IDM application
2. Check IDM queue manually
3. Run script as administrator if needed

### Fallback to Ollama Pull

If IDM download fails, scripts will automatically fall back to standard Ollama pull. However, this:
- ❌ Loses resume capability
- ❌ No speed acceleration
- ❌ No queue management

**Recommendation**: Fix IDM issues before downloading large models.

## Adding New Models

To add a new model to the mapping:

1. **Edit `config/ollama_model_mapping.json`**:
   ```json
   {
     "models": {
       "new-model:tag": {
         "huggingface_repo": "User/Model-Name-GGUF",
         "gguf_filename": "model-name.Q4_K_M.gguf",
         "model_name": "new-model:tag",
         "size_gb": 5.0,
         "description": "Model description"
       }
     }
   }
   ```

2. **Test Download**:
   ```powershell
   python scripts/python/download_gguf_with_idm.py User/Model-Name-GGUF model-name.Q4_K_M.gguf new-model:tag
   ```

3. **Update Documentation**: Add model to this document

## Related Files

- `config/ollama_model_mapping.json` - Model mapping (SSoT)
- `config/lumina_idm_config.json` - IDM configuration (SSoT)
- `scripts/powershell/Invoke-IDMDownload.ps1` - General IDM download helper
- `scripts/powershell/Invoke-IDMGGUFDownload.ps1` - GGUF-specific IDM helper
- `scripts/python/download_gguf_with_idm.py` - Python wrapper for GGUF downloads
- `scripts/powershell/pull_ollama_models_with_idm.ps1` - Automated model pull with IDM
- `scripts/powershell/check_and_pull_models.ps1` - Model check and pull with IDM
- `cedarbrook-financial-services_llc-env/containerization/services/ollama/setup-iron-legion-models.ps1` - Docker cluster model setup

## Policy Enforcement

**All model download scripts MUST**:
1. Check for IDM installation first
2. Use IDM for all GGUF/LLM downloads
3. Fall back to Ollama API only if IDM is unavailable
4. Log IDM usage in all cases
5. Warn if IDM is not available

**Violations**:
- Direct `ollama pull` without IDM check = **NOT ALLOWED**
- Direct `Invoke-WebRequest` for model downloads = **NOT ALLOWED**
- Bypassing IDM for large files = **NOT ALLOWED**

---

**Last Updated**: 2025-01-24  
**Maintained By**: Lumina Project Team  
**Policy**: All GGUF/LLM downloads MUST use IDM

