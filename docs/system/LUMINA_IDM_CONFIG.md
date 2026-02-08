# Lumina IDM Configuration

## Overview

Internet Download Manager (IDM) is configured as the default downloader for Cursor IDE and all Lumina project downloads.

**Source of Truth:** `config/lumina_idm_config.json`

## Configuration

### IDM Detection

IDM is automatically detected from common installation paths:
- `C:\Program Files (x86)\Internet Download Manager\idman.exe`
- `C:\Program Files\Internet Download Manager\idman.exe`
- `D:\Program Files\Internet Download Manager\idman.exe`

### Download Helper Script

**Script:** `scripts/powershell/Invoke-IDMDownload.ps1`

This script routes downloads through IDM, providing:
- Resume capability
- Speed acceleration
- Download management
- Queue management

**Usage:**
```powershell
# Basic download
.\scripts\powershell\Invoke-IDMDownload.ps1 -Url "https://example.com/file.zip"

# With destination
.\scripts\powershell\Invoke-IDMDownload.ps1 `
    -Url "https://example.com/file.zip" `
    -Destination "C:\Downloads\file.zip" `
    -Description "File Download"
```

## Cursor IDE Integration

### Settings Configuration

Cursor IDE is configured to use IDM via:
- `.cursor/settings.json` - Cursor-specific settings
- `.vscode/settings.json` - Workspace settings (also used by Cursor)

**Key Settings:**
```json
{
  "workbench.downloadService.useIDM": true,
  "workbench.downloadService.idmScript": "${workspaceFolder}/scripts/powershell/Invoke-IDMDownload.ps1"
}
```

### How It Works

1. **Extension Downloads:** Cursor extensions that download files will use IDM
2. **Manual Downloads:** Scripts and commands can call `Invoke-IDMDownload.ps1`
3. **Browser Integration:** IDM browser integration module handles browser downloads

## Browser Integration

IDM browser integration module should be installed for:
- Browser-based downloads
- Extension marketplace downloads
- Web-based file downloads

**Supported Browsers:**
- Neo (preferred)
- Chrome
- Edge
- Firefox

## PowerShell Integration

### Direct Usage

```powershell
# Download a file
& '.\scripts\powershell\Invoke-IDMDownload.ps1' `
    -Url 'https://example.com/file.zip' `
    -Destination 'C:\Downloads\file.zip' `
    -Description 'File Download'
```

### In Scripts

```powershell
# Use in other scripts
$downloadScript = Join-Path $PSScriptRoot "Invoke-IDMDownload.ps1"
& $downloadScript -Url $url -Destination $dest -Description "Download"
```

## Default Download Locations

- **Local:** `$env:USERPROFILE\Downloads`
- **NAS:** `Z:\downloads` (if available)

## Verification

**Check if IDM is available:**
```powershell
.\scripts\powershell\Invoke-IDMDownload.ps1 -Url "https://example.com/test" -Description "Test"
```

**Expected output:**
```
Adding to IDM queue: Test
  URL: https://example.com/test
  Destination: C:\Users\...\Downloads\test
✓ Added to IDM queue successfully
  Check IDM to monitor download progress
```

## Troubleshooting

### IDM Not Found

If IDM is not detected:
1. Verify IDM is installed
2. Check installation path matches configured paths
3. Add IDM to system PATH
4. Manually specify IDM path in script

### Downloads Not Using IDM

1. **Check Cursor Settings:**
   - Verify `.cursor/settings.json` has IDM configuration
   - Reload Cursor window (`Ctrl+Shift+P` → "Developer: Reload Window")

2. **Check Script Path:**
   - Verify `Invoke-IDMDownload.ps1` exists
   - Check script permissions

3. **Manual Override:**
   - Use script directly: `.\scripts\powershell\Invoke-IDMDownload.ps1`

### Browser Integration Issues

1. **Install IDM Browser Integration:**
   - Open IDM
   - Go to Downloads → Options → General
   - Click "Browser Integration" button
   - Enable integration for your browsers

2. **Restart Browsers:**
   - Close and reopen browsers after enabling integration

## LLM GGUF Downloads

### Specialized GGUF Download Helper

**Script:** `scripts/powershell/Invoke-IDMGGUFDownload.ps1`

This specialized script handles GGUF model file downloads:
- Automatically detects Ollama models directory (`D:\Ollama\models`)
- Integrates with HuggingFace Hub URLs
- Routes through IDM for resume capability
- Handles large model files efficiently

**PowerShell Usage:**
```powershell
# Download GGUF from HuggingFace
.\scripts\powershell\Invoke-IDMGGUFDownload.ps1 `
    -Url "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf" `
    -ModelName "llama2" `
    -Destination "D:\Ollama\models\llama2.gguf"
```

**Python Usage:**
```python
# Using the Python helper
python scripts/python/download_gguf_with_idm.py \
    TheBloke/Llama-2-7B-GGUF \
    llama-2-7b.Q4_K_M.gguf \
    llama2
```

### Integration with Existing Scripts

The existing `download_models.py` scripts can be updated to use IDM:
1. Get URL from HuggingFace Hub
2. Route through `Invoke-IDMGGUFDownload.ps1`
3. Monitor download in IDM
4. Verify file after completion

### Default GGUF Locations

- **Ollama Models:** `D:\Ollama\models` (if `OLLAMA_MODELS` env var set)
- **Fallback:** `$env:USERPROFILE\Downloads`
- **NAS:** `Z:\downloads\models` (if available)

### Benefits for GGUF Downloads

✅ **Resume Large Downloads:** GGUF files are often 4-20GB+ - IDM can resume if interrupted  
✅ **Speed Acceleration:** IDM's acceleration helps with large model files  
✅ **Queue Management:** Download multiple models simultaneously  
✅ **Bandwidth Control:** Control download speed to avoid network congestion  

## Related Files

- `config/lumina_idm_config.json` - SSoT configuration
- `scripts/powershell/Invoke-IDMDownload.ps1` - General download helper script
- `scripts/powershell/Invoke-IDMGGUFDownload.ps1` - GGUF-specific download helper
- `scripts/python/download_gguf_with_idm.py` - Python wrapper for GGUF downloads
- `.cursor/settings.json` - Cursor IDE settings
- `.vscode/settings.json` - Workspace settings

## Benefits

✅ **Resume Capability:** Resume interrupted downloads  
✅ **Speed Acceleration:** Faster downloads with IDM's acceleration  
✅ **Queue Management:** Manage multiple downloads  
✅ **Scheduled Downloads:** Schedule downloads for off-peak hours  
✅ **Bandwidth Control:** Control download bandwidth usage  

---

**Last Updated:** 2025-01-24  
**Maintained By:** Lumina Project Team

