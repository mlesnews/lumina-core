# C Drive Cleanup Guide

## Current Status
- **Free Space**: ~364 GB
- **Used Space**: ~3.3 TB  
- **Status**: Monitor and optimize

## Root Causes & Solutions

### 1. Temporary Files
**Location**: `C:\Users\<username>\AppData\Local\Temp`
**Action**:
```powershell
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
```

### 2. Windows Temp
**Location**: `C:\Windows\Temp` (requires admin)
**Action**: Run Disk Cleanup or:
```powershell
Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue
```

### 3. Recycle Bin
**Action**: Empty Recycle Bin manually or:
```powershell
Clear-RecycleBin -Force -ErrorAction SilentlyContinue
```

### 4. Browser Caches
- **Chrome**: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache`
- **Edge**: `%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache`
- **Firefox**: `%LOCALAPPDATA%\Mozilla\Firefox\Profiles\*\cache2`

### 5. Windows Update Files
**Location**: `C:\Windows\SoftwareDistribution\Download` (requires admin)
**Action**:
```powershell
Stop-Service wuauserv
Remove-Item -Path "C:\Windows\SoftwareDistribution\Download\*" -Recurse -Force
Start-Service wuauserv
```

### 6. Docker Data
**Location**: `C:\ProgramData\Docker`
**Action**: Prune Docker (careful!):
```powershell
docker system prune -a --volumes -f
```

### 7. Large Projects/Files
**Check these locations**:
- `C:\Users\<username>\Downloads`
- `C:\Users\<username>\Documents`
- `C:\Users\<username>\Desktop`
- Projects in Dropbox (consider moving to D: drive)

**Action**: Move large projects to D: drive:
```powershell
# Example: Move project to D drive
Move-Item -Path "C:\Users\...\project" -Destination "D:\projects\" -Force
```

### 8. Log Files
**Search for**:
- `.log` files older than 7 days
- Large log files in project directories

### 9. Git Repositories
If you have many repositories, they can take significant space. Consider:
- Running `git gc --aggressive` in repositories
- Moving rarely-used repos to D: drive
- Removing old/unused repositories

### 10. Node Modules
**Location**: Various project directories
**Action**: Only keep node_modules in active projects, delete from archived projects

## Quick Cleanup Script

Run this for safe cleanup:

```powershell
# User temp
Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue

# Empty Recycle Bin
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

# Run Windows Disk Cleanup
cleanmgr /d C:
```

## Prevention

1. **Regular Cleanup**: Run cleanup monthly
2. **Move Projects**: Keep large projects on D: drive
3. **Monitor Downloads**: Regularly clean Downloads folder
4. **Docker**: Regularly prune unused images/containers
5. **Git**: Clean up old repositories and run `git gc`

## Tools Created

1. **analyze_c_drive_usage.ps1** - Analyze disk usage
2. **cleanup_c_drive_safe.ps1** - Safe cleanup script

## Next Steps

1. Run `cleanmgr /d C:` for Windows Disk Cleanup
2. Clean user temp files
3. Empty Recycle Bin
4. Check Downloads/Documents for large files
5. Move large projects to D: drive if possible
6. Monitor disk space weekly

---

**Created**: 2025-12-31
