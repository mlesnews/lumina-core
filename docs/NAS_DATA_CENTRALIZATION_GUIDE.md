# NAS Data Centralization Guide

## Overview

This guide explains how to move data from local storage to NAS for centralization and testing cloud storage integration.

## Quick Start

### 1. Identify Candidates

Run the analysis script:
```bash
python scripts/python/move_data_to_nas.py --dry-run --priority all
```

This will show you:
- What data can be moved
- Size of each candidate
- Priority (high/medium/low)
- Estimated space savings

### 2. Map Network Drive (Optional but Recommended)

Map the NAS as a network drive for easier access:
```powershell
# Map NAS backup share
net use Z: \\10.17.17.32\backups /user:admin

# Or map directly to MATT_Backups
net use Z: \\10.17.17.32\backups\MATT_Backups /user:admin
```

### 3. Move Data

**Option A: Using the Script**
```bash
# Move high priority items only
python scripts/python/move_data_to_nas.py --priority high --nas-path "Z:\lumina"

# Move everything (with confirmation)
python scripts/python/move_data_to_nas.py --priority all --nas-path "Z:\lumina"
```

**Option B: Manual Move**
1. Access NAS via File Station or mapped drive
2. Create destination: `Z:\lumina\data\<directory>`
3. Copy/move files manually
4. Verify transfer

## What Should Be Moved

### High Priority (Move First)
- **Backups** (`data/backups`) - Should always be on NAS
- **Archives** (`data/archives`, `data/session_archives`) - Perfect for NAS storage
- **Video Production** (`data/holocron/video_production`, `data/videos`) - Large files, ideal for NAS

### Medium Priority
- **Logs** (`data/logs`) - Can be archived on NAS
- **Exports** (`data/exports`) - Archive after use
- **Transcriptions** (`data/transcriptions`) - Can be archived
- **Data Mining Results** (`data/lumina_data_mining`) - Archive old results

### Low Priority
- **Cache** (`data/cache`) - Can be cleaned or moved
- **Temp** (`data/temp`) - Usually should be cleaned, but can move to NAS if needed

## NAS Paths

### Available NAS Paths
- `\\10.17.17.32\backups\MATT_Backups\lumina` (Recommended)
- `\\10.17.17.32\backups\MATT_Backups`
- `\\10.17.17.32\backups`

### Structure on NAS
```
\\10.17.17.32\backups\MATT_Backups\lumina\
├── data\
│   ├── backups\          (from local data/backups)
│   ├── archives\         (from local data/archives)
│   ├── holocron\         (from local data/holocron)
│   └── ...
├── config\
└── logs\
```

## Integration with Cloud Storage

After moving data to NAS, set up DSM Cloud Sync:

1. **Run DSM Cloud Storage Setup:**
   ```bash
   python scripts/python/nas_dsm_cloud_storage_setup.py
   ```

2. **Configure Cloud Sync in DSM:**
   - Open DSM Package Manager
   - Install/Open Cloud Sync
   - Add cloud provider (Dropbox, OneDrive, Google Drive, etc.)
   - Configure sync for `\\10.17.17.32\backups\MATT_Backups\lumina`

3. **Set Up Selective Sync:**
   - Sync only important data (not everything)
   - Keep large archives local-only on NAS
   - Sync configs and critical data to cloud

## Benefits

1. **Centralized Storage**: All data in one place
2. **Backup Redundancy**: NAS + Cloud Sync = multiple backups
3. **Space Savings**: Free up local C: drive
4. **Accessibility**: Access from any device on network
5. **Cloud Backup**: Automatic cloud sync via DSM

## Testing

### Test 1: Small Directory
Start with a small directory to test:
```bash
# Test with transcriptions (small)
python scripts/python/move_data_to_nas.py --priority medium --nas-path "Z:\lumina"
```

### Test 2: Verify Access
After moving, verify:
1. Files are accessible on NAS
2. Scripts still work (if they reference moved paths)
3. Cloud sync is working (if configured)

### Test 3: Large Directory
Once verified, move larger directories:
```bash
# Move video production data
python scripts/python/move_data_to_nas.py --priority high --nas-path "Z:\lumina"
```

## Troubleshooting

### NAS Not Accessible
1. Check network connection: `ping 10.17.17.32`
2. Map network drive with credentials:
   ```powershell
   net use Z: \\10.17.17.32\backups /user:admin * /persistent:yes
   ```
3. Use File Station on NAS to verify paths

### Permission Denied
- Ensure you have write access to NAS share
- Check NAS user permissions in DSM

### Script Errors
- Run with `--dry-run` first to see what would happen
- Check that source paths exist
- Verify destination has enough space

## Next Steps

1. ✅ Run analysis to identify candidates
2. ✅ Map network drive
3. ✅ Move high-priority data
4. ✅ Set up DSM Cloud Sync
5. ✅ Configure selective sync
6. ✅ Verify data integrity
7. ✅ Update any hardcoded paths in scripts

---

**Created**: 2025-12-31  
**Status**: Ready for testing
