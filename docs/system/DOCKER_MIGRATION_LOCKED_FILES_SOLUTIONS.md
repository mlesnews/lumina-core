# Docker Migration - Locked Files Solutions

## Problem
During Docker volume migration, many files are locked by Docker Desktop processes:
- Log files (*.log)
- Socket files (*.sock)
- Runtime files in `run/` directory
- WSL-related files

**Current Status:** Only 0.12 GB of 131 GB migrated due to file locks.

## Solution Options

### Option 1: Volume Shadow Copy Service (VSS) - RECOMMENDED ⭐
**Best for:** Complete migration while Docker is running

Use Windows VSS to create a snapshot of the Docker directory, then copy from the snapshot.

**Advantages:**
- Can copy locked files
- No need to stop Docker
- Native Windows feature
- Reliable for large migrations

**Implementation:**
```powershell
# Create VSS snapshot
$snapshot = (New-Object -ComObject VSSSnapshot.VssSnapshot).CreateSnapshot("Docker Migration")

# Copy from snapshot path (typically \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyX\...)
robocopy "\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyX\..." "\\10.17.17.32\docker\Docker" /E /MT:8
```

**Script:** `scripts/python/migrate_docker_vss.py` (to be created)

---

### Option 2: Docker Volume Export (Individual Volumes) - RECOMMENDED ⭐
**Best for:** Migrating actual Docker data (volumes, not entire directory)

Export each Docker volume individually using Docker commands, then restore on NAS.

**Advantages:**
- Only migrates actual data (volumes)
- No locked files (volumes are mounted, not locked)
- Cleaner migration
- Can be done while containers are running (with some containers stopped)

**Implementation:**
```bash
# Export volume
docker run --rm -v volume_name:/data -v /backup:/backup alpine tar czf /backup/volume.tar -C /data .

# Or use docker volume backup plugin
docker volume create --driver local --opt type=nfs --opt device=:/volume1/docker/volumes backup_volume
```

**Script:** `scripts/python/migrate_docker_volumes_export.py` (already created)

---

### Option 3: Robocopy Backup Mode (/B)
**Best for:** Quick solution using existing tools

Use robocopy's backup mode which can copy files even if you don't have write permissions.

**Advantages:**
- Simple, uses existing tool
- Can copy locked files if run as administrator
- No additional software needed

**Limitations:**
- Requires administrator privileges
- May still fail on actively written files
- Socket files may not copy correctly

**Implementation:**
```powershell
# Run as Administrator
robocopy "C:\Users\mlesn\AppData\Local\Docker" "\\10.17.17.32\docker\Docker" /E /B /MT:8 /R:5 /W:10
```

---

### Option 4: Windows Backup & Restore
**Best for:** System-level backup before migration

Use Windows built-in backup to create a system image, then restore specific directories.

**Advantages:**
- Complete system backup
- Handles all locked files
- Can restore to different location

**Limitations:**
- Very large backup size
- Slower than direct copy
- Requires significant disk space

---

### Option 5: Docker Volume Plugin (NAS Direct)
**Best for:** Long-term solution - run Docker volumes directly on NAS

Configure Docker to use NAS as storage backend using volume plugins.

**Advantages:**
- No migration needed (volumes already on NAS)
- Better performance for NAS-hosted containers
- Native Docker integration

**Implementation:**
```bash
# Install Docker volume plugin for NFS/SMB
docker plugin install vieux/sshfs
docker volume create --driver vieux/sshfs \
  -o sshcmd=user@nas:/volume1/docker/volumes \
  -o password=xxx \
  nas-docker-volumes
```

---

### Option 6: Scheduled Migration (System Boot)
**Best for:** One-time complete migration

Schedule migration to run at system boot before Docker starts.

**Advantages:**
- No locked files (Docker not running)
- Complete migration possible
- Simple to implement

**Limitations:**
- Requires system restart
- One-time operation
- Need to prevent Docker auto-start

**Implementation:**
1. Disable Docker Desktop auto-start
2. Create scheduled task to run at boot
3. Run migration script
4. Re-enable Docker Desktop

---

### Option 7: Docker Desktop Stop + Wait + Copy
**Best for:** Ensuring all processes are stopped

More aggressive process termination with longer wait times.

**Advantages:**
- Ensures all processes stopped
- Can copy most files
- Simple approach

**Limitations:**
- May still have some locked files
- Requires extended downtime
- Some processes may restart

**Implementation:**
```powershell
# Stop all Docker processes
Get-Process | Where-Object {$_.ProcessName -match "Docker|docker"} | Stop-Process -Force

# Wait for file handles to release
Start-Sleep -Seconds 30

# Copy
robocopy "C:\Users\mlesn\AppData\Local\Docker" "\\10.17.17.32\docker\Docker" /E /MT:8
```

---

## Recommended Approach

**For Immediate Migration:**
1. **Option 2 (Docker Volume Export)** - Migrate actual volumes, skip runtime files
2. **Option 1 (VSS)** - If complete directory copy is needed

**For Long-term Solution:**
- **Option 5 (Docker Volume Plugin)** - Run volumes directly on NAS

**For One-time Complete Migration:**
- **Option 6 (Scheduled Boot Migration)** - Run at system boot

---

## Implementation Priority

1. ✅ **Option 2: Docker Volume Export** (Script already created)
   - Migrate 24 volumes individually
   - Skip locked runtime files
   - Clean, focused migration

2. ⭐ **Option 1: VSS Snapshot** (Recommended for complete copy)
   - Create VSS snapshot script
   - Copy from snapshot
   - Complete migration possible

3. **Option 3: Robocopy /B** (Quick alternative)
   - Run as administrator
   - May handle most locked files

---

## Notes

- **Locked files are mostly runtime artifacts:**
  - Logs can be regenerated
  - Sockets are temporary
  - WSL files can be recreated
  - Core data (volumes, images) is what matters

- **Volume export is preferred** because:
  - Only migrates actual data
  - No locked file issues
  - Cleaner migration
  - Can verify each volume individually

- **VSS is best for complete copy** if you need everything including logs for audit purposes.
