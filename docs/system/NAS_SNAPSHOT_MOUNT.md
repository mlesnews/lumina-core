# NAS Snapshot Permanent Mount Configuration

**Status**: ✅ **IMPLEMENTED**

---

## Overview

Permanent Windows network drive mount configuration for NAS snapshot directories. Maps Synology NAS snapshot locations as persistent network drives that survive reboots.

---

## Configuration

### NAS Details

- **Host**: `10.17.17.32`
- **User**: `mlesn`
- **Type**: Synology NAS
- **Snapshot Enabled**: Yes

### Mount Points

| Drive | Network Path | Type | Auto-Mount |
|-------|--------------|------|------------|
| **S:** | `\\10.17.17.32\snapshot` | Snapshot Share | ✅ Yes |
| **T:** | `\\10.17.17.32\volume1\@snapshot` | BTRFS Snapshot | ❌ No |
| **U:** | `\\10.17.17.32\backups\@snapshot` | Backup Snapshot | ❌ No |

---

## Usage

### PowerShell Script

```powershell
# Check current mounts
.\scripts\nas_snapshot_mount.ps1 -Check

# Mount snapshot drive (auto-detects available path)
.\scripts\nas_snapshot_mount.ps1

# Remove mount
.\scripts\nas_snapshot_mount.ps1 -Remove
```

### Python Manager

```bash
# Check current mounts
python scripts/python/nas_snapshot_mount_manager.py --check

# Setup all auto-mount configurations
python scripts/python/nas_snapshot_mount_manager.py --setup

# Mount specific drive
python scripts/python/nas_snapshot_mount_manager.py --mount S
```

---

## Setup Instructions

### Step 1: Enable Snapshot Replication on Synology NAS

1. Open **Synology DSM**
2. Go to **Snapshot Replication** app
3. Enable snapshots for desired volumes
4. Create snapshot schedule

### Step 2: Enable Snapshot Share (Optional)

1. Go to **Control Panel** > **Shared Folder**
2. Create or enable snapshot share
3. Set permissions for user `mlesn`

### Step 3: Run Mount Script

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\nas_snapshot_mount.ps1
```

### Step 4: Verify Mount

```powershell
# Check if drive is mounted
Get-PSDrive -Name S

# Test access
Test-Path S:\

# List snapshots
Get-ChildItem S:\ -Directory
```

---

## Snapshot Paths

### Synology Default Paths

- **BTRFS Snapshot Directory**: `/volume1/@snapshot`
- **Backup Snapshot**: `/volume1/backups/@snapshot`
- **Share-Based**: `/volume1/snapshot` (if share created)

### Windows UNC Paths

- **Snapshot Share**: `\\10.17.17.32\snapshot`
- **Volume1 Snapshot**: `\\10.17.17.32\volume1\@snapshot`
- **Backup Snapshot**: `\\10.17.17.32\backups\@snapshot`

---

## Configuration File

**Location**: `config/nas_snapshot_mount.json`

**Structure**:
```json
{
  "nas": {
    "host": "10.17.17.32",
    "user": "mlesn",
    "type": "Synology"
  },
  "mounts": [
    {
      "name": "NAS Snapshot",
      "drive_letter": "S",
      "network_path": "\\\\10.17.17.32\\snapshot",
      "persistent": true,
      "auto_mount": true
    }
  ]
}
```

---

## Troubleshooting

### Mount Fails with "Network Path Not Found"

**Causes**:
- Snapshot share not enabled on NAS
- NAS offline or unreachable
- User lacks permissions

**Solutions**:
1. Verify NAS is online: `ping 10.17.17.32`
2. Check Snapshot Replication app is enabled
3. Verify user permissions in Control Panel
4. Try accessing path directly: `\\10.17.17.32\snapshot`

### Drive Already Mapped to Different Path

**Solution**:
```powershell
# Remove existing mapping
net use S: /delete /yes

# Remount with correct path
.\scripts\nas_snapshot_mount.ps1
```

### BTRFS @snapshot Directory Not Accessible via SMB

**Note**: BTRFS `@snapshot` directories may require SSH access instead of SMB.

**Alternative**: Use SSH/SFTP to access snapshots:
```bash
ssh mlesn@10.17.17.32
ls /volume1/@snapshot
```

---

## Verification Commands

### Check Mounts

```powershell
# List all NAS mounts
Get-PSDrive -PSProvider FileSystem | Where-Object { $_.DisplayRoot -like "\\10.17.17.32\*" }

# Test specific drive
Test-Path S:\

# List snapshot directories
Get-ChildItem S:\ -Directory | Select-Object Name, LastWriteTime
```

### Check Configuration

```powershell
# View mount configuration
Get-Content config\nas_snapshot_mount.json | ConvertFrom-Json

# Check network drives
net use
```

---

## Persistence

Mounts created with `/persistent:yes` will:
- ✅ Survive Windows reboots
- ✅ Auto-reconnect on login
- ✅ Remain mapped until manually removed

To remove persistent mount:
```powershell
net use S: /delete /yes
```

---

## Integration

### With Backup Systems

The snapshot mount integrates with:
- **Backup scripts**: Access snapshots for backup verification
- **Holocron**: Store snapshot metadata
- **R5 Matrix**: Track snapshot history
- **SYPHON**: Extract patterns from snapshots

### With Health Checks

The mount status can be checked via:
- `lumina_debug_health_check.py` (can be extended)
- `nas_snapshot_mount_manager.py --check`

---

## Status

**Mount Script**: ✅ **IMPLEMENTED**

**Configuration**: ✅ **COMPLETE**

**Documentation**: ✅ **COMPLETE**

---

**Tags:** `#NAS` `#SNAPSHOT` `#MOUNT` `#PERMANENT` `#WINDOWS` `@JARVIS` `@LUMINA`

**Status:** ✅ **NAS SNAPSHOT PERMANENT MOUNT CONFIGURATION COMPLETE**
