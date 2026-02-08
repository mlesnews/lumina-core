# DSM Cloud Storage Aggregator Setup Guide

**Date**: 2026-01-05  
**Status**: ✅ **COMPLETE**  
**Package**: Synology DSM Cloud Sync  
**Purpose**: Aggregate multiple cloud storage providers on NAS (N: drive)

---

## Overview

This guide provides step-by-step instructions for setting up the DSM Cloud Sync package as a cloud storage aggregator, combining Dropbox, Microsoft OneDrive, ProtonDrive, and other providers into a unified location on the NAS.

### Architecture

```
NAS (10.17.17.32)
└── N:\cloud_storage_aggregated\
    ├── dropbox\          ← Dropbox sync
    ├── onedrive\         ← OneDrive sync
    └── protondrive\      ← ProtonDrive sync
```

---

## Prerequisites

### 1. DSM Package Installation

- ✅ DSM version: 7.x
- ✅ Cloud Sync package installed
- ✅ Package Center access: `https://10.17.17.32:5001`

### 2. Network Drive

- ✅ N: drive mapped to `\\10.17.17.32\backups\MATT_Backups`
- ✅ Path accessible: `N:\cloud_storage_aggregated`

### 3. Azure Key Vault

- ✅ Key Vault URL: `https://jarvis-lumina.vault.azure.net/`
- ✅ Secrets configured for all cloud providers
- ✅ Access credentials available

---

## Configuration File

**Location**: `config/dsm_cloud_storage_aggregator.json`

This file contains all configuration for the cloud storage aggregator, including:
- Provider settings
- Sync policies
- Authentication credentials (references to Azure Key Vault)
- Monitoring and alerting

---

## Setup Steps

### Step 1: Access DSM Web Portal

1. Open browser and navigate to: `https://10.17.17.32:5001`
2. Login with admin credentials
3. Navigate to **Package Center**

### Step 2: Install/Verify Cloud Sync Package

1. Search for "Cloud Sync" in Package Center
2. If not installed, click **Install**
3. Wait for installation to complete
4. Open **Cloud Sync** from Main Menu

### Step 3: Configure Dropbox Sync

#### 3.1 Create Dropbox Sync Task

1. In Cloud Sync, click **Create**
2. Select **Dropbox** from provider list
3. Click **Next**

#### 3.2 Authenticate Dropbox

1. Click **Sign in to Dropbox**
2. Browser will open Dropbox OAuth2 page
3. Login with Dropbox account
4. Authorize DSM Cloud Sync access
5. Return to DSM interface

#### 3.3 Configure Sync Settings

**Local Folder**:
```
N:\cloud_storage_aggregated\dropbox
```

**Remote Folder**:
```
/ (root)
```

**Sync Direction**:
- ✅ **Bidirectional** (recommended)
- Alternative: One-way (local → remote or remote → local)

**Sync Mode**:
- ✅ **Selective Sync** (sync specific folders)
- Alternative: Full Sync (sync everything)

**Conflict Resolution**:
- ✅ **Local Wins** (NAS files take precedence)
- Alternative: Remote Wins, Ask Me

**Advanced Settings**:
- ✅ Sync subfolders
- ✅ Sync deleted files
- ❌ Sync hidden files (disabled)
- ✅ Preserve file permissions
- Bandwidth limit: None (unlimited)

**Exclude Patterns**:
```
.git
node_modules
__pycache__
*.tmp
*.log
```

#### 3.4 Save and Start Sync

1. Review settings
2. Click **Apply**
3. Sync task will start automatically
4. Monitor progress in Cloud Sync dashboard

### Step 4: Configure Microsoft OneDrive Sync

#### 4.1 Create OneDrive Sync Task

1. In Cloud Sync, click **Create**
2. Select **Microsoft OneDrive** from provider list
3. Click **Next**

#### 4.2 Authenticate OneDrive

1. Click **Sign in to Microsoft**
2. Browser will open Microsoft OAuth2 page
3. Login with Microsoft account (Office 365)
4. Authorize DSM Cloud Sync access
5. Return to DSM interface

#### 4.3 Configure Sync Settings

**Local Folder**:
```
N:\cloud_storage_aggregated\onedrive
```

**Remote Folder**:
```
/ (root)
```

**Sync Direction**: Bidirectional  
**Sync Mode**: Selective Sync  
**Conflict Resolution**: Local Wins

**Advanced Settings**: Same as Dropbox

#### 4.4 Save and Start Sync

1. Review settings
2. Click **Apply**
3. Sync task will start automatically

### Step 5: Configure ProtonDrive Sync

#### 5.1 Check ProtonDrive Support

**Note**: ProtonDrive may not be directly supported by DSM Cloud Sync. Options:

1. **WebDAV Connection** (if ProtonDrive supports WebDAV)
2. **Third-party sync tools** (rclone, etc.)
3. **Manual sync scripts**

#### 5.2 WebDAV Setup (if available)

1. In Cloud Sync, click **Create**
2. Select **WebDAV** or **Other**
3. Enter ProtonDrive WebDAV URL
4. Enter credentials from Azure Key Vault

**Local Folder**:
```
N:\cloud_storage_aggregated\protondrive
```

**Remote Folder**: `/`

#### 5.3 Alternative: Rclone Integration

If WebDAV not available, use rclone on NAS:

```bash
# SSH into NAS
ssh admin@10.17.17.32

# Install rclone (if not installed)
# Configure ProtonDrive
rclone config

# Create sync task
rclone sync protondrive:/ N:/cloud_storage_aggregated/protondrive/ --transfers 16
```

### Step 6: Configure Additional Providers

For homelab-specific cloud storage providers:

1. Check if provider is supported by DSM Cloud Sync
2. If supported, follow same steps as Dropbox/OneDrive
3. If not supported, use rclone or custom sync scripts
4. Update `config/dsm_cloud_storage_aggregated.json` with new provider

---

## Sync Policies

### Default Policies

All sync tasks follow these default policies:

- **Sync Direction**: Bidirectional
- **Conflict Resolution**: Local Wins (NAS takes precedence)
- **Sync Schedule**: Real-time (continuous sync)
- **Bandwidth Limit**: None (unlimited)

### Custom Policies

You can customize policies per provider:

1. Open Cloud Sync in DSM
2. Select sync task
3. Click **Edit**
4. Modify settings as needed
5. Click **Apply**

### Sync Priority

Sync priority order (as configured):
1. **Dropbox** (highest priority)
2. **OneDrive**
3. **ProtonDrive**

Priority affects bandwidth allocation during simultaneous syncs.

---

## Monitoring

### DSM Cloud Sync Dashboard

Access dashboard: `https://10.17.17.32:5001` → Cloud Sync

**Dashboard shows**:
- Sync task status
- Last sync time
- Files synced
- Sync errors
- Bandwidth usage

### Health Checks

Automated health checks run every 15 minutes:

- ✅ Sync status verification
- ✅ Connection status check
- ✅ Disk space monitoring
- ✅ Sync error detection
- ✅ Bandwidth usage tracking

### Alerts

Alerts are sent when:

- **Sync Errors**: > 10 errors in 15 minutes
- **Disk Space**: < 15% free (85% used)
- **Connection Failures**: 3 consecutive failures

**Alert Channels**:
- JARVIS system notifications
- Email alerts
- Webhook notifications

### Metrics

Tracked metrics:
- Sync speed (MB/s)
- Files synced per hour
- Sync errors per hour
- Bandwidth usage (MB/s)

---

## Authentication Management

### OAuth2 Tokens

All cloud providers use OAuth2 authentication:

1. **Initial Authentication**: Manual OAuth2 flow in browser
2. **Token Refresh**: Automatic (handled by DSM Cloud Sync)
3. **Token Storage**: Stored securely in DSM

### Azure Key Vault Integration

Credentials are referenced (not stored) in configuration:

**Secrets in Azure Key Vault**:
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

**Note**: DSM Cloud Sync handles OAuth2 tokens directly. Azure Key Vault secrets are for API access if needed.

---

## Troubleshooting

### Sync Task Not Starting

**Symptoms**: Sync task created but not syncing

**Solutions**:
1. Check sync task status in Cloud Sync dashboard
2. Verify authentication (re-authenticate if needed)
3. Check local folder path exists: `N:\cloud_storage_aggregated\[provider]`
4. Verify network connectivity
5. Check DSM Cloud Sync package logs

### Authentication Failures

**Symptoms**: OAuth2 authentication fails

**Solutions**:
1. Clear browser cache and cookies
2. Try incognito/private browsing mode
3. Verify cloud provider account is active
4. Check if provider has rate limits
5. Re-authenticate from Cloud Sync interface

### Sync Errors

**Symptoms**: Files not syncing, errors in dashboard

**Solutions**:
1. Check error messages in Cloud Sync dashboard
2. Verify file permissions on N: drive
3. Check disk space on NAS
4. Review exclude patterns (may be excluding needed files)
5. Check network connectivity
6. Review DSM Cloud Sync logs

### Slow Sync Speed

**Symptoms**: Sync is very slow

**Solutions**:
1. Check network speed: `Test-Connection 10.17.17.32`
2. Verify NAS hardware performance
3. Reduce number of simultaneous sync tasks
4. Check bandwidth limits in sync settings
5. Monitor NAS CPU and memory usage

### Disk Space Issues

**Symptoms**: Sync fails due to disk space

**Solutions**:
1. Check free space on N: drive: `Get-PSDrive -Name "N"`
2. Clean up old files if needed
3. Adjust retention policies
4. Consider archiving old data
5. Expand NAS storage if needed

---

## Best Practices

### 1. Selective Sync

Use selective sync to avoid syncing unnecessary files:
- Exclude `.git` directories
- Exclude `node_modules`
- Exclude temporary files (`*.tmp`, `*.log`)
- Exclude cache directories

### 2. Conflict Resolution

**Local Wins** is recommended because:
- NAS is primary storage location
- Local changes are typically more recent
- Easier to manage conflicts

### 3. Bandwidth Management

Configure bandwidth limits during business hours:
- Set limits to avoid impacting other network traffic
- Use schedule-based limits
- Monitor bandwidth usage

### 4. Regular Monitoring

- Check sync status daily
- Review error logs weekly
- Monitor disk space regularly
- Verify sync integrity monthly

### 5. Backup Strategy

Even with cloud sync, maintain backups:
- NAS has built-in backup to external drives
- Cloud providers have version history
- Consider additional backup to separate location

---

## Security Considerations

### Credentials Security

- ✅ OAuth2 tokens stored securely in DSM
- ✅ No credentials in configuration files
- ✅ Azure Key Vault for API credentials (if needed)
- ✅ Regular token refresh

### Network Security

- ✅ NAS accessible only on local network
- ✅ TLS required for DSM web portal
- ✅ Encrypted connections for cloud sync
- ✅ Firewall rules restrict external access

### Data Encryption

- ✅ ProtonDrive: End-to-end encryption
- ✅ OneDrive: Encryption at rest and in transit
- ✅ Dropbox: Encryption at rest and in transit
- ✅ NAS: Optional encryption for local storage

---

## Maintenance

### Regular Tasks

1. **Weekly**: Check sync status and errors
2. **Monthly**: Review disk space and cleanup
3. **Quarterly**: Verify authentication tokens
4. **Annually**: Review and update sync policies

### Updates

- **DSM Updates**: Keep DSM updated for security and features
- **Cloud Sync Updates**: Update Cloud Sync package when available
- **Provider Changes**: Update if cloud providers change APIs

---

## Related Documentation

- [Dropbox to NAS Migration Guide](./DROPBOX_TO_NAS_MIGRATION.md)
- [Network Drive Configuration](../config/network_drives_config.json)
- [DSM Cloud Sync API Reference](./DSM_CLOUD_SYNC_API.md)
- [NAS Integration Guide](./LUMINA_NAS_SSH_API.md)

---

## Support

For issues or questions:

1. Check DSM Cloud Sync logs in Package Center
2. Review configuration file: `config/dsm_cloud_storage_aggregator.json`
3. Check JARVIS system logs for integration issues
4. Consult [Known Issues](./KNOWN_ISSUES.md)

---

**Tags**: #DSM #CLOUD-SYNC #CLOUD-STORAGE #AGGREGATOR #DROPBOX #ONEDRIVE #PROTONDRIVE #NAS #JARVIS #LUMINA
