# NAS Migration - File Analysis Summary

**Date**: 2025-01-14
**Status**: 📊 **ANALYSIS COMPLETE**

---

## Findings Summary

### ✅ Already on NAS
- **Ollama Models**: ✅ Configured for NAS (`\\10.17.17.32\data\models\ollama`)
- **Folder Redirections**: ✅ All folders redirect to NAS

### 📦 Small Items Moved
- **Downloads**: 0.99 GB moved
- **pip cache**: Moved
- **npm cache**: Moved
- **Large files in user folders**: 0.79 GB found (installers, archives)

### ⚠️ Items Requiring Manual Action

#### Docker (1.19 GB)
- **Location**: `C:\Users\mlesn\.docker`
- **Size**: 1.19 GB
- **Action Required**:
  1. Stop Docker Desktop completely
  2. Move to: `\\10.17.17.32\homes\mlesn\docker`
  3. Create symlink or configure Docker Desktop settings
  4. Restart Docker Desktop

#### Temp Files (4.09 GB)
- **Location**: `C:\Users\mlesn\AppData\Local\Temp`
- **Size**: 4.09 GB
- **Action**: Clean old temp files (>30 days)

---

## Disk Usage Status

- **Current**: 98.5% (3639.8 GB / 3694.9 GB)
- **Target**: 80% (2955.9 GB)
- **Still Need to Free**: ~684 GB

---

## Problem Analysis

The small files we've moved (Downloads, caches) total only ~2-3 GB. We still need to free **~684 GB**, which suggests:

1. **Large files are in non-standard locations**:
   - Root of C: drive
   - Hidden/system folders
   - Program Files (unlikely to move)
   - Windows folder (cannot move)

2. **Possible large items**:
   - Docker images/volumes (if not in `.docker` folder)
   - Virtual machines (VHD/VHDX files)
   - Large databases
   - Backup files
   - Old Windows installations
   - WSL distributions

3. **Next steps to find the space**:
   - Use `WinDirStat` or `TreeSize` to visualize disk usage
   - Check for VHD/VHDX files
   - Check for WSL distributions
   - Check for large log files
   - Check for old Windows.old folder

---

## Recommendations

### Immediate Actions
1. **Use disk space analyzer**:
   - Install WinDirStat or TreeSize
   - Run full C: drive scan
   - Identify largest directories

2. **Check common large items**:
   ```powershell
   # Check for VHD files
   Get-ChildItem -Path C:\ -Recurse -Include *.vhd,*.vhdx -ErrorAction SilentlyContinue |
     Select-Object FullName, @{Name="SizeGB";Expression={[math]::Round($_.Length/1GB,2)}}

   # Check for WSL
   wsl --list --verbose

   # Check Windows.old
   Test-Path "C:\Windows.old"
   ```

3. **Move Docker** (when ready):
   - Stop Docker Desktop
   - Move `.docker` folder to NAS
   - Create symlink

4. **Clean temp files**:
   - Delete files in `AppData\Local\Temp` older than 30 days

---

## Scripts Created

1. **`scan_large_files.ps1`** - Scans for large files in user folders
2. **`move_docker_to_nas.ps1`** - Instructions for moving Docker
3. **`move_large_media.ps1`** - Moves large media files (interactive)
4. **`move_files_simple.ps1`** - Simple file mover

---

## Next Steps

1. ✅ **Folder redirections**: Complete
2. ✅ **Small caches**: Moved
3. ⏳ **Find large space hogs**: Use disk analyzer
4. ⏳ **Move Docker**: When Docker Desktop can be stopped
5. ⏳ **Clean temp files**: Delete old temp files

---

**Last Updated**: 2025-01-14
**Status**: Analysis complete, need disk space analyzer to find remaining ~684 GB
