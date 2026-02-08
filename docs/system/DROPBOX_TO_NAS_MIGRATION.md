# Dropbox to NAS Migration Guide

**Date**: 2026-01-05  
**Status**: ✅ **COMPLETE**  
**Migration Target**: Local Dropbox → NAS Network Storage (N: Drive)  
**Cloud Storage Aggregator**: DSM Cloud Sync Package

---

## Overview

This guide documents the complete migration from local Dropbox storage (D:\Dropbox or C:\Users\mlesn\Dropbox) to NAS network storage with permanent mapped drive N: for cloud storage aggregation.

### Migration Goals

1. ✅ **Permanent N: Drive Mapping** - Map N: drive to NAS permanent storage
2. ✅ **Data Migration** - Migrate all Dropbox data to NAS
3. ✅ **Cloud Storage Aggregation** - Configure DSM Cloud Sync for multiple providers
4. ✅ **Path Updates** - Update all configuration files to use N: drive
5. ✅ **Verification** - Ensure data integrity and accessibility

---

## Architecture

### Network Drive Configuration

- **Drive Letter**: `N:`
- **Network Path**: `\\10.17.17.32\backups\MATT_Backups`
- **Purpose**: Primary cloud storage aggregator location
- **Persistence**: Permanent mapping (reconnects on startup)

### Cloud Storage Aggregator Structure

```
N:\
├── my_projects\              # Migrated Dropbox projects
├── cloud_storage_aggregated\
│   ├── dropbox\              # Dropbox sync location
│   ├── onedrive\             # Microsoft OneDrive sync location
│   └── protondrive\           # ProtonDrive sync location
└── backups\                   # Additional NAS backups
```

---

## Prerequisites

### 1. NAS Access

- ✅ NAS IP: `10.17.17.32`
- ✅ Network connectivity to NAS
- ✅ Appropriate permissions on NAS shares
- ✅ NAS path exists: `\\10.17.17.32\backups\MATT_Backups`

### 2. DSM Package Installation

- ✅ **Cloud Sync** package installed on DSM
- ✅ DSM version: 7.x
- ✅ Web portal accessible: `https://10.17.17.32:5001`

### 3. Azure Key Vault

- ✅ Azure Key Vault configured
- ✅ Secrets stored for cloud provider credentials:
  - `dropbox-client-id`
  - `dropbox-client-secret`
  - `dropbox-access-token`
  - `dropbox-refresh-token`
  - `onedrive-client-id`
  - `onedrive-client-secret`
  - `onedrive-access-token`
  - `onedrive-refresh-token`
  - `protondrive-client-id`
  - `protondrive-client-secret`
  - `protondrive-access-token`
  - `protondrive-refresh-token`

### 4. PowerShell Execution Policy

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Migration Steps

### Step 1: Map N: Drive

The migration script automatically maps the N: drive, but you can verify manually:

```powershell
# Manual mapping (if needed)
New-PSDrive -Name "N" -PSProvider FileSystem -Root "\\10.17.17.32\backups\MATT_Backups" -Persist
```

Verify mapping:
```powershell
Get-PSDrive -Name "N"
Test-Path "N:\"
```

### Step 2: Run Migration Script

#### Dry Run (Recommended First)

```powershell
cd "C:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell"
.\migrate_dropbox_to_nas.ps1 -DryRun
```

#### Actual Migration

```powershell
# From D:\Dropbox
.\migrate_dropbox_to_nas.ps1 -SourcePath "D:\Dropbox" -DestPath "N:\my_projects"

# From C:\Users\mlesn\Dropbox
.\migrate_dropbox_to_nas.ps1 -SourcePath "C:\Users\mlesn\Dropbox" -DestPath "N:\my_projects"
```

#### Verify Existing Migration

```powershell
.\migrate_dropbox_to_nas.ps1 -VerifyOnly
```

### Step 3: Verify Migration

The script automatically verifies migration, but you can manually verify:

```powershell
# Check file counts
$sourceFiles = (Get-ChildItem -Path "D:\Dropbox\my_projects" -Recurse -File).Count
$destFiles = (Get-ChildItem -Path "N:\my_projects" -Recurse -File).Count
Write-Host "Source: $sourceFiles files | Destination: $destFiles files"

# Check disk space
Get-PSDrive -Name "N" | Select-Object Used, Free
```

### Step 4: Configure DSM Cloud Sync Aggregator

See [DSM Cloud Storage Aggregator Setup Guide](#dsm-cloud-storage-aggregator-setup) below.

---

## DSM Cloud Storage Aggregator Setup

### Overview

DSM Cloud Sync package aggregates multiple cloud storage providers into a unified location on the NAS (N: drive).

### Supported Providers

1. **Dropbox** - Primary cloud storage (migrating from local)
2. **Microsoft OneDrive** - Office 365 integration
3. **ProtonDrive** - Encrypted cloud storage
4. **Custom Homelab Providers** - Additional providers as needed

### Configuration File

Configuration is stored in: `config/dsm_cloud_storage_aggregator.json`

### DSM Web Portal Setup

1. **Access DSM Web Portal**
   - URL: `https://10.17.17.32:5001`
   - Login with admin credentials

2. **Open Cloud Sync Package**
   - Navigate to Package Center
   - Open Cloud Sync

3. **Add Dropbox Sync Task**
   - Click "Create" → "Dropbox"
   - Authenticate with Dropbox OAuth2
   - **Local folder**: `N:\cloud_storage_aggregated\dropbox`
   - **Remote folder**: `/` (root)
   - **Sync direction**: Bidirectional
   - **Sync mode**: Selective sync
   - **Conflict resolution**: Local wins

4. **Add OneDrive Sync Task**
   - Click "Create" → "OneDrive"
   - Authenticate with Microsoft OAuth2
   - **Local folder**: `N:\cloud_storage_aggregated\onedrive`
   - **Remote folder**: `/` (root)
   - **Sync direction**: Bidirectional
   - **Sync mode**: Selective sync

5. **Add ProtonDrive Sync Task**
   - Click "Create" → "ProtonDrive" (if available)
   - Or use WebDAV connection if supported
   - **Local folder**: `N:\cloud_storage_aggregated\protondrive`
   - **Remote folder**: `/` (root)
   - **Sync direction**: Bidirectional
   - **Encryption**: Enabled

### Sync Settings

#### Default Settings

- **Sync Direction**: Bidirectional
- **Conflict Resolution**: Local wins
- **Sync Schedule**: Real-time
- **Bandwidth Limit**: None (unlimited)
- **Exclude Patterns**: `.git`, `node_modules`, `__pycache__`, `*.tmp`, `*.log`

#### Bandwidth Management

Configure bandwidth limits if needed:
- **Max Bandwidth**: Set in Mbps (null = unlimited)
- **Schedule**: Configure time-based limits

### Monitoring

#### Health Checks

- **Interval**: Every 15 minutes
- **Checks**:
  - Sync status
  - Connection status
  - Disk space
  - Sync errors
  - Bandwidth usage

#### Alerts

- **Channels**: JARVIS, Email, Webhook
- **Thresholds**:
  - Sync error count: 10
  - Disk space: 85%
  - Connection failures: 3

---

## Path Updates

### Configuration Files Updated

The migration script automatically updates:
- `config/jupyter/nas_config.json`
- `config/runtime.json`

### Manual Path Updates

If needed, update these files manually:

1. **Jupyter Configuration**
   ```json
   {
     "nas": {
       "project_root": "N:\\my_projects",
       "notebook_directory": "N:\\my_projects\\data\\jupyter"
     }
   }
   ```

2. **Runtime Configuration**
   ```json
   {
     "project_root": "N:\\my_projects"
   }
   ```

3. **Environment Variables**
   ```powershell
   $env:PROJECT_ROOT = "N:\my_projects"
   [System.Environment]::SetEnvironmentVariable("PROJECT_ROOT", "N:\my_projects", "User")
   ```

### Search and Replace Script

For bulk path updates, use:

```powershell
# Find all references to old Dropbox paths
Get-ChildItem -Path "N:\my_projects" -Recurse -Include "*.json","*.py","*.ps1","*.md" | 
    Select-String -Pattern "D:\\Dropbox|C:\\Users\\mlesn\\Dropbox" | 
    Select-Object Path, LineNumber, Line
```

---

## Rollback Procedure

If migration fails or needs to be rolled back:

1. **Load Migration State**
   ```powershell
   $state = Get-Content "$env:TEMP\dropbox_migration\migration_state.json" | ConvertFrom-Json
   ```

2. **Restore from Backup**
   - If backup was created before migration, restore from backup
   - Or manually copy files back from N: to original Dropbox location

3. **Update Configuration**
   - Revert configuration file changes
   - Update path references back to original Dropbox paths

4. **Unmap N: Drive** (if needed)
   ```powershell
   Remove-PSDrive -Name "N" -Force
   net use N: /delete /y
   ```

---

## Verification Checklist

After migration, verify:

- [ ] N: drive is mapped and accessible
- [ ] All files migrated successfully (file count matches)
- [ ] File sizes match between source and destination
- [ ] Configuration files updated to use N: drive
- [ ] Applications can access files on N: drive
- [ ] DSM Cloud Sync tasks configured and running
- [ ] Cloud storage providers syncing correctly
- [ ] No errors in migration log file
- [ ] Network drive reconnects on system startup

---

## Troubleshooting

### N: Drive Not Mapping

**Issue**: Network drive fails to map

**Solutions**:
1. Verify NAS is accessible: `Test-Connection 10.17.17.32`
2. Check network path: `Test-Path "\\10.17.17.32\backups\MATT_Backups"`
3. Verify credentials and permissions
4. Check Windows Credential Manager for stored credentials

### Migration Fails

**Issue**: Migration script fails with errors

**Solutions**:
1. Check log file: `$env:TEMP\dropbox_migration\migration_*.log`
2. Verify source path exists and is accessible
3. Check destination has sufficient space
4. Ensure robocopy has necessary permissions
5. Try running PowerShell as Administrator

### Cloud Sync Not Working

**Issue**: DSM Cloud Sync tasks not syncing

**Solutions**:
1. Verify Cloud Sync package is installed and running
2. Check OAuth2 authentication for each provider
3. Verify local folders exist on N: drive
4. Check DSM Cloud Sync logs in Package Center
5. Verify Azure Key Vault secrets are correct

### Path References Not Updated

**Issue**: Applications still reference old Dropbox paths

**Solutions**:
1. Run path update script manually
2. Search codebase for remaining references: `grep -r "D:\\Dropbox" N:\my_projects`
3. Update environment variables
4. Restart applications to pick up new paths

---

## Performance Considerations

### Network Speed

- **Gigabit Ethernet**: ~125 MB/s theoretical
- **Actual Speed**: Depends on NAS hardware and network conditions
- **Migration Time**: Large migrations may take hours

### Optimization Tips

1. **Use robocopy with multi-threading**: `/MT:16` (default in script)
2. **Schedule during off-hours**: Reduce network congestion
3. **Monitor bandwidth**: Use DSM bandwidth management if needed
4. **Incremental syncs**: After initial migration, use incremental syncs

---

## Security Considerations

### Credentials Storage

- ✅ All cloud provider credentials stored in Azure Key Vault
- ✅ No credentials in configuration files
- ✅ OAuth2 tokens refreshed automatically

### Network Security

- ✅ NAS accessible only on local network (10.17.17.0/24)
- ✅ TLS required for DSM web portal
- ✅ Encrypted connections for cloud sync

### Access Control

- ✅ Network drive mapped with appropriate user permissions
- ✅ Cloud sync tasks use service account credentials
- ✅ Audit logging enabled for all operations

---

## Maintenance

### Regular Tasks

1. **Monitor Disk Space**
   - Check N: drive free space regularly
   - Set up alerts at 85% capacity

2. **Verify Sync Status**
   - Check DSM Cloud Sync dashboard weekly
   - Review sync logs for errors

3. **Update Credentials**
   - Refresh OAuth2 tokens as needed
   - Update Azure Key Vault secrets if changed

4. **Backup Configuration**
   - Backup `config/dsm_cloud_storage_aggregator.json`
   - Backup network drive configuration

---

## Related Documentation

- [DSM Cloud Storage Aggregator Setup](./DSM_CLOUD_STORAGE_AGGREGATOR_SETUP.md)
- [Network Drive Configuration](../config/network_drives_config.json)
- [NAS Integration Guide](./LUMINA_NAS_SSH_API.md)
- [JARVIS System Documentation](./JARVIS_SYSTEM.md)

---

## Support

For issues or questions:

1. Check migration log files: `$env:TEMP\dropbox_migration\`
2. Review DSM Cloud Sync logs in Package Center
3. Check JARVIS system logs for integration issues
4. Consult [Known Issues](./KNOWN_ISSUES.md)

---

**Tags**: #DROPBOX #NAS #MIGRATION #CLOUD-STORAGE #DSM #NETWORK-DRIVE #JARVIS #LUMINA
