# Selective Remote Sync Setup Guide

**Date**: 2026-01-06  
**Status**: ✅ **ACTIVE**  
**Strategy**: Full storage on LAN, selective sync for remote work

---

## Overview

This guide documents the selective remote sync strategy:
- **Full Storage**: All Dropbox and cloud storage maintained on NAS (N: drive) for LAN access
- **Selective Sync**: Only chosen directories/files synced for remote work (with/without VPN)
- **Proton Family**: Primary provider for secure remote access

---

## Architecture

### Storage Strategy

```
LAN (Homelab)
├── N:\Dropbox\                    # Full Dropbox (4.5TB) - LAN only
├── N:\cloud_storage_aggregated\
│   ├── dropbox\                   # Selective sync for remote
│   ├── onedrive\                  # Selective sync for remote
│   └── protondrive\               # Primary encrypted sync (VPN preferred)
└── N:\my_projects\                # Active projects (selective sync)

Remote Access
├── With VPN (ProtonVPN)
│   └── ProtonDrive (encrypted)    # Primary access method
├── Without VPN
│   ├── Dropbox (selective)        # Less sensitive files
│   └── OneDrive (selective)       # Office documents
```

---

## Selective Sync Directories

### Active Projects
- **Local**: `N:\my_projects`
- **Remote Sync**: All providers
- **Priority**: 1 (highest)
- **VPN**: Optional but recommended

### Documents
- **Local**: `N:\Documents`
- **Remote Sync**: All providers
- **Priority**: 2
- **VPN**: Optional

### Configuration Files
- **Local**: `N:\my_projects\.lumina\config`
- **Remote Sync**: ProtonDrive only (encrypted)
- **Priority**: 1
- **VPN**: Required
- **Encryption**: Required

### Scripts
- **Local**: `N:\my_projects\.lumina\scripts`
- **Remote Sync**: Dropbox, ProtonDrive
- **Priority**: 2
- **VPN**: Optional

---

## Excluded from Remote Sync

### Large Data
- `node_modules/`
- `.git/objects/`
- `venv/`, `.venv/`
- `__pycache__/`
- `*.pyc`
- `data/large/`
- `data/cache/`
- `backups/`

### Sensitive Local Only
- `secrets/`
- `credentials/`
- `.env.local`
- `local_backup/`

---

## Remote Work Scenarios

### With VPN (ProtonVPN)

**Access Methods**:
- ProtonDrive (primary)
- NAS direct access
- Homelab services

**Encryption**: Required  
**Preferred Provider**: ProtonDrive

**Setup**:
1. Connect to ProtonVPN
2. Access ProtonDrive for encrypted files
3. Direct NAS access available

### Without VPN

**Access Methods**:
- Dropbox (selective)
- OneDrive (selective)

**Excluded**:
- ProtonDrive
- NAS direct access
- Sensitive files

**Encryption**: Recommended  
**Sensitive Files**: Excluded

---

## Migration Strategy

### Phase 1: Full Local Storage
- Migrate all Dropbox to `N:\Dropbox` (LAN only)
- Maintain full 4.5TB on NAS
- No remote sync for full storage

### Phase 2: Selective Remote Sync
- Configure selective sync for chosen directories
- Set up DSM Cloud Sync with include/exclude patterns
- Configure ProtonDrive as primary provider

### Phase 3: Proton Family Integration
- Set up ProtonVPN for secure access
- Configure ProtonDrive for encrypted sync
- Integrate ProtonMail, ProtonCalendar, ProtonPass

---

## DSM Cloud Sync Configuration

### Selective Sync Settings

**Include Patterns**:
```
my_projects/**
Documents/**
config/**
scripts/**
```

**Exclude Patterns**:
```
**/node_modules/**
**/.git/objects/**
**/venv/**
**/__pycache__/**
**/data/large/**
**/secrets/**
```

### Provider Priority

1. **ProtonDrive** (Priority 1)
   - Encrypted sync
   - VPN preferred
   - Sensitive files

2. **Dropbox** (Priority 2)
   - General files
   - VPN optional

3. **OneDrive** (Priority 3)
   - Office documents
   - VPN optional

---

## Usage

### LAN Access (Full Storage)

```powershell
# Access full Dropbox on NAS
cd N:\Dropbox

# Access all cloud storage
cd N:\cloud_storage_aggregated
```

### Remote Access with VPN

```powershell
# Connect to ProtonVPN
protonvpn-cli connect

# Access ProtonDrive
cd N:\cloud_storage_aggregated\protondrive

# Direct NAS access available
cd N:\my_projects
```

### Remote Access without VPN

```powershell
# Access Dropbox (selective)
cd N:\cloud_storage_aggregated\dropbox

# Access OneDrive (selective)
cd N:\cloud_storage_aggregated\onedrive

# ProtonDrive not available without VPN
```

---

## Migration Script

### Selective Migration

```powershell
# Dry run
.\migrate_selective_to_nas.ps1 -DryRun

# Execute selective migration
.\migrate_selective_to_nas.ps1
```

### Full Migration (LAN Only)

```powershell
# Migrate full Dropbox to NAS (LAN only, no remote sync)
.\migrate_dropbox_to_nas.ps1 -SourcePath "C:\Users\mlesn\Dropbox" -DestPath "N:\Dropbox"
```

---

## Configuration Files

- **Selective Sync Config**: `config/selective_remote_sync_config.json`
- **Proton Family Config**: `config/proton_family_integration.json`
- **DSM Cloud Sync Config**: `config/dsm_cloud_storage_aggregator.json`

---

## Security Considerations

### With VPN
- ✅ End-to-end encryption (ProtonDrive)
- ✅ Secure NAS access
- ✅ All sensitive files accessible

### Without VPN
- ⚠️ Standard encryption (Dropbox/OneDrive)
- ❌ No NAS direct access
- ❌ Sensitive files excluded

---

## Related Documentation

- [Proton Family Integration](./PROTON_FAMILY_INTEGRATION.md)
- [Dropbox to NAS Migration](./DROPBOX_TO_NAS_MIGRATION.md)
- [DSM Cloud Storage Aggregator Setup](./DSM_CLOUD_STORAGE_AGGREGATOR_SETUP.md)

---

**Tags**: #SELECTIVE-SYNC #REMOTE-WORK #VPN #PROTON #DROPBOX #NAS #LUMINA
