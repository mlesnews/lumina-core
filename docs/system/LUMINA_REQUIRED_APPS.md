# Lumina Required Applications

## Overview

This document describes the required applications for the Lumina project that should be installed to `D:\Program Files`.

**Source of Truth:** `config/lumina_required_apps.json`

## Installation Script

**Script:** `scripts/install_required_apps_d_drive.ps1`

**Usage:**
```powershell
# Basic installation
.\scripts\install_required_apps_d_drive.ps1

# With Azure Key Vault for serial keys
.\scripts\install_required_apps_d_drive.ps1 -UseAzureVault -KeyVaultName "jarvis-lumina"

# Custom install path
.\scripts\install_required_apps_d_drive.ps1 -InstallPath "D:\Program Files"
```

## Required Applications

### 1. MS Office 365
- **Purpose:** Office productivity suite
- **Download:** https://aka.ms/office-installer
- **Install Path:** `D:\Program Files\Microsoft Office`
- **Serial Key:** Available from Azure Key Vault (`Office365-ProductKey`)
- **Notes:** Product key may need manual activation after installation

### 2. Copilot (GitHub)
- **Purpose:** AI coding assistant
- **Download:** https://github.com/github/copilot/releases/latest
- **Install Path:** `D:\Program Files\GitHub Copilot`

### 3. Copilot 365 (Microsoft)
- **Purpose:** Microsoft Copilot integration
- **Download:** https://aka.ms/copilot-installer
- **Install Path:** `D:\Program Files\Microsoft Copilot`

### 4. Process Lasso
- **Purpose:** CPU optimization and process management
- **Download:** https://bitsum.com/files/processlassosetup64.exe
- **Install Path:** `D:\Program Files\Process Lasso`
- **Serial Key:** Available from Azure Key Vault (`ProcessLasso-LicenseKey`)
- **Install Parameter:** `/KEY=<key>`

### 5. Park Control
- **Purpose:** CPU core parking management
- **Download:** https://bitsum.com/files/parkcontrolsetup.exe
- **Install Path:** `D:\Program Files\Park Control`
- **Serial Key:** Available from Azure Key Vault (`ParkControl-LicenseKey`)
- **Install Parameter:** `/KEY=<key>`

### 6. Perfect Disk
- **Purpose:** Disk optimization and defragmentation
- **Download:** https://www.raxco.com/downloads
- **Install Path:** `D:\Program Files\Perfect Disk`
- **Serial Key:** Available from Azure Key Vault (`PerfectDisk14-Pro-Key`)
- **Install Parameter:** `/KEY=<key>`

### 7. CfosSpeed
- **Purpose:** Network traffic shaping and optimization
- **Download:** https://www.cfos.de/en/download/download.htm
- **Install Path:** `D:\Program Files\CfosSpeed`

## Features

### IDM Integration
- Script automatically detects Internet Download Manager (IDM)
- Uses IDM for downloads if available (resume capability)
- Falls back to `Invoke-WebRequest` if IDM not found

### Download Location Detection
- Checks NAS downloads folder: `Z:\downloads`
- Checks local downloads: `$env:USERPROFILE\Downloads`
- Uses existing downloads if found

### Azure Key Vault Integration
- Load serial keys from Azure Key Vault (`jarvis-lumina`)
- Enable with `-UseAzureVault` switch
- Serial keys automatically included in installation

### Terminal Truncation Prevention
- Script automatically configures terminal buffer (200 characters)
- Prevents loss of valuable output data

## Installation Process

1. **Check D Drive:** Verifies `D:\` exists
2. **Check IDM:** Detects Internet Download Manager
3. **Load Serial Keys:** (If `-UseAzureVault` specified) Loads keys from Azure Key Vault
4. **Check Downloads:** Searches NAS and local Downloads folders
5. **Download Missing:** Downloads any missing installers
6. **Install Applications:** Runs installers with elevation

## Manual Installation

If automatic installation fails, the script provides:
- Download URLs for manual download
- Install paths for manual installation
- Serial keys (if available from Key Vault)

## Azure Key Vault Secrets

The following secrets should be stored in Azure Key Vault (`jarvis-lumina`):

- `Office365-ProductKey` - Office 365 product key
- `ProcessLasso-LicenseKey` - Process Lasso license key
- `ParkControl-LicenseKey` - Park Control license key
- `PerfectDisk14-Pro-Key` - Perfect Disk Pro license key

**To store a secret:**
```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name <SecretName> `
    --value "<secret-value>"
```

## Troubleshooting

### D Drive Not Found
- Ensure D drive exists and is accessible
- Check drive letter assignment

### IDM Not Found
- Script will use standard download method
- Consider installing IDM for resume capability

### Download Failures
- Check internet connection
- Verify download URLs are accessible
- Try manual download from provided URLs

### Installation Failures
- Some installers require manual interaction
- Ensure installers are set to install to `D:\Program Files`
- Check for elevation requirements

### Serial Key Issues
- Verify Azure Key Vault access
- Check secret names match expected values
- Ensure `az` CLI is installed and logged in

## Related Documentation

- [Lumina Setup Complete](./LUMINA_SETUP_COMPLETE.md)
- [Lumina SSoT Registry](./LUMINA_SSOT_REGISTRY.md)
- [Azure Setup Guide](./AZURE_SETUP_GUIDE.md)

---

**Last Updated:** 2025-01-24  
**Maintained By:** Lumina Project Team

