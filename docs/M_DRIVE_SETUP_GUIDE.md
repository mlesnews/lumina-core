# M: Drive Setup Guide - Centralize my_projects on NAS

## Overview

Map M: drive to NAS and move `my_projects` directory there to:
- Free up C: drive space (currently 4.5 TB in Dropbox)
- Centralize all projects on NAS
- Enable cloud sync via DSM
- Improve backup and redundancy

## Quick Start

### Step 1: Map M: Drive to NAS

```powershell
# Run the mapping script
.\scripts\powershell\map_my_projects_to_m_drive.ps1

# Or manually:
net use M: \\10.17.17.32\backups\MATT_Backups /persistent:yes /user:admin
```

### Step 2: Verify M: Drive

```powershell
# Check M: drive is mapped
Get-PSDrive M

# Test write access
"Test" | Out-File "M:\test.txt"
Remove-Item "M:\test.txt"
```

### Step 3: Move my_projects (Dry Run First)

```powershell
# See what would happen (dry run)
.\scripts\powershell\move_my_projects_to_m_drive.ps1 -DryRun

# Actually move (after verification)
.\scripts\powershell\move_my_projects_to_m_drive.ps1
```

## Detailed Steps

### 1. Map M: Drive

**Option A: Using Script**
```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\powershell\map_my_projects_to_m_drive.ps1 -Persistent
```

**Option B: Manual Mapping**
```powershell
# Basic mapping
net use M: \\10.17.17.32\backups\MATT_Backups

# With credentials
net use M: \\10.17.17.32\backups\MATT_Backups /user:admin * /persistent:yes

# Verify
Get-PSDrive M
```

### 2. Analyze Current my_projects

```powershell
# Check current size
$size = [math]::Round((Get-ChildItem "C:\Users\mlesn\Dropbox\my_projects" -Recurse -File -ErrorAction SilentlyContinue | 
    Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB, 2)
Write-Host "my_projects size: $size GB"
```

### 3. Move my_projects to M: Drive

**Dry Run First:**
```powershell
.\scripts\powershell\move_my_projects_to_m_drive.ps1 -DryRun
```

**Actual Move:**
```powershell
.\scripts\powershell\move_my_projects_to_m_drive.ps1
```

This will:
- Copy all files from `C:\Users\mlesn\Dropbox\my_projects` to `M:\my_projects`
- Verify the copy
- Remove source after verification
- Use robocopy for reliable transfer with resume capability

### 4. Update Dropbox Location

After moving, update Dropbox to sync from M: drive:

1. Open Dropbox Settings
2. Go to "Sync" tab
3. Click "Move" next to Dropbox folder location
4. Change to: `M:\my_projects`
5. Let Dropbox move/re-sync files

### 5. Update Path References

Update any hardcoded paths in scripts/configs:

**Common paths to update:**
- `C:\Users\mlesn\Dropbox\my_projects` → `M:\my_projects`
- `D:\Dropbox\my_projects` → `M:\my_projects`

**Search for references:**
```powershell
# Find hardcoded paths
Select-String -Path "*.py","*.ps1","*.json" -Pattern "C:\\Users\\mlesn\\Dropbox\\my_projects" -Recurse
Select-String -Path "*.py","*.ps1","*.json" -Pattern "D:\\Dropbox\\my_projects" -Recurse
```

### 6. Set Up DSM Cloud Sync

After moving to M: drive, configure cloud sync:

```bash
# Run DSM cloud storage setup
python scripts/python/nas_dsm_cloud_storage_setup.py
```

Then in DSM:
1. Open Package Manager
2. Install/Open Cloud Sync
3. Add cloud provider
4. Configure sync for `M:\my_projects` (or NAS path equivalent)

## Benefits

1. **C: Drive Space**: Frees up ~4.5 TB from C: drive
2. **Centralized Storage**: All projects in one location
3. **NAS Performance**: Better for large files
4. **Cloud Backup**: Easy to sync via DSM Cloud Sync
5. **Network Access**: Access from any device on network
6. **Backup Redundancy**: NAS + Cloud = multiple backups

## Troubleshooting

### M: Drive Not Mapping

1. **Check Network:**
   ```powershell
   ping 10.17.17.32
   ```

2. **Check Credentials:**
   - Verify NAS username/password
   - Try mapping with explicit credentials

3. **Check Permissions:**
   - Ensure account has write access to NAS share
   - Check NAS share permissions in DSM

### Move Fails

1. **Check Space:**
   ```powershell
   Get-PSDrive M | Select-Object Free,Used
   ```

2. **Check Permissions:**
   - Ensure write access to M: drive
   - Check source directory permissions

3. **Use Robocopy Manually:**
   ```powershell
   robocopy "C:\Users\mlesn\Dropbox\my_projects" "M:\my_projects" /E /COPYALL /MT:8
   ```

### After Move - Projects Don't Work

1. **Update Environment Variables:**
   ```powershell
   [Environment]::SetEnvironmentVariable("PROJECT_ROOT", "M:\my_projects", "User")
   ```

2. **Update IDE Workspaces:**
   - Close and reopen workspace from new location
   - Update workspace settings

3. **Update Git Configs:**
   - Update any absolute paths in git configs
   - Verify git still works

## Verification Checklist

- [ ] M: drive is mapped and accessible
- [ ] Write test successful on M: drive
- [ ] my_projects moved to M:\my_projects
- [ ] Files verified (size matches)
- [ ] Dropbox location updated
- [ ] Scripts/configs updated with new paths
- [ ] Projects still work from M: drive
- [ ] DSM Cloud Sync configured
- [ ] Cloud sync test successful

## Rollback Plan

If you need to rollback:

1. **Stop Dropbox sync** (if changed)
2. **Copy back from M: to original location:**
   ```powershell
   robocopy "M:\my_projects" "C:\Users\mlesn\Dropbox\my_projects" /E /COPYALL
   ```
3. **Update Dropbox location back**
4. **Update path references back**

---

**Created**: 2025-12-31  
**Status**: Ready for execution
