# Software Installation & Registration Status

**Last Updated:** 2025-01-24  
**Status:** In Progress

## Overview

This document tracks the installation and registration status of required software for the Lumina project workstation setup.

## Installation Requirements

All software should be installed to `D:\Program Files` (NOT C: drive).

## Azure Key Vault

**Vault Name:** `lumina-n8n-keyvault`  
**Location:** Azure  
**Status:** ✓ All serial keys stored

## Software Status

### 1. Process Lasso
- **Status:** ⚠ Installed on C: drive (should be on D:)
- **Location:** `C:\Program Files\Process Lasso\ProcessLasso.exe`
- **Serial Key:** ✓ Available in Azure Key Vault (`ProcessLasso-LicenseKey`)
- **Registration:** ⏳ Pending (needs registration)
- **Action Required:** 
  - Reinstall to D: drive OR
  - Register existing installation manually
  - Serial Key: `65ca55d86c5844be57f625515413cc88`

### 2. Park Control
- **Status:** ⏳ Installation in progress
- **Expected Location:** `D:\Program Files\Park Control\ParkControl.exe`
- **Serial Key:** ✓ Available in Azure Key Vault (`ParkControl-LicenseKey`)
- **Registration:** ⏳ Pending (waiting for installation to complete)
- **Action Required:** 
  - Complete installation wizard (ensure D: drive location)
  - Register after installation
  - Serial Key: `261d95e05a51853af3caaffb795b86af`

### 3. Perfect Disk
- **Status:** ✗ Not installed
- **Expected Location:** `D:\Program Files\Perfect Disk\pd.exe`
- **Serial Key:** ✓ Available in Azure Key Vault (`PerfectDisk14-Pro-Key`)
- **Registration:** ⏳ Pending (waiting for installation)
- **Action Required:** 
  - Download from: https://www.raxco.com/downloads
  - Install to D: drive
  - Register after installation
  - Serial Key: `358-0959882-002682-5392`

### 4. Office 365
- **Status:** ✗ Not installed
- **Expected Location:** `D:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE`
- **Serial Key:** ✓ Available in Azure Key Vault (`Office365-ProductKey`)
- **Registration:** ⏳ Pending (waiting for installation)
- **Action Required:** 
  - Install from: `C:\Users\mlesn\Downloads\MS_Office_365.exe` (if file exists)
  - Or download from: https://aka.ms/office-installer
  - Install to D: drive
  - Activate with product key after installation
  - Product Key: `NVGD2-6XCXV-DVQBK-6B97R-BY29Q`
  - Order Number: `212485104`

## Serial Keys in Azure Key Vault

All serial keys have been successfully stored in Azure Key Vault:

| Software | Vault Secret Name | Status |
|----------|------------------|--------|
| Process Lasso | `ProcessLasso-LicenseKey` | ✓ Stored |
| Park Control | `ParkControl-LicenseKey` | ✓ Stored |
| Perfect Disk | `PerfectDisk14-Pro-Key` | ✓ Stored |
| Perfect Disk (Upgrade) | `PerfectDisk14-Pro-Upgrade-Key` | ✓ Stored |
| Perfect Disk (v13) | `PerfectDisk13-Pro-Key` | ✓ Stored |
| Office 365 | `Office365-ProductKey` | ✓ Stored |
| Office 365 | `Office365-OrderNumber` | ✓ Stored |

## Registration Methods

### Automatic Registration
Software that supports command-line registration can be registered using:
```powershell
.\scripts\verify_and_register_all_software.ps1
```

### Manual Registration
Some software requires manual registration:
- **Process Lasso:** Help > Enter License Key
- **Park Control:** Help > Enter License Key (or via setup executable)
- **Perfect Disk:** GUI registration required
- **Office 365:** Office activation wizard

## Verification Script

Run the verification script to check status and attempt automatic registration:
```powershell
.\scripts\verify_and_register_all_software.ps1
```

This script will:
1. Check all installations
2. Retrieve serial keys from Azure Key Vault
3. Attempt automatic registration where possible
4. Display manual registration steps for software that requires it
5. Provide a comprehensive status summary

## Next Steps

1. ✅ **COMPLETED:** Store all serial keys in Azure Key Vault
2. ⏳ **IN PROGRESS:** Complete Park Control installation
3. ⏳ **IN PROGRESS:** Complete Process Lasso installation (reinstall to D: drive)
4. ⏳ **PENDING:** Install Perfect Disk
5. ⏳ **PENDING:** Install Office 365
6. ⏳ **PENDING:** Register all installed software
7. ⏳ **PENDING:** Verify all registrations complete

## Notes

- Process Lasso is currently installed on C: drive but should be on D: drive
- Park Control and Process Lasso installers were started but may still be running
- Office 365 installer file may need to be verified/re-downloaded
- Perfect Disk download failed and needs manual download

## Related Scripts

- `scripts/install_required_apps_d_drive.ps1` - Main installation script
- `scripts/verify_and_register_all_software.ps1` - Verification and registration script
- `scripts/register_installed_software.ps1` - Registration-only script
- `scripts/store_serials_simple.ps1` - Serial key storage script

## Related Documentation

- `config/lumina_required_apps.json` - Single Source of Truth for required applications
- `docs/system/LUMINA_REQUIRED_APPS.md` - Application requirements documentation

