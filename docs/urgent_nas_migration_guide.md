# URGENT NAS Migration Guide

## 🚨 CRITICAL: Hard Drive Space Issue

**Current Status**: Only **52.86 GB free** out of 3642.06 GB (1.4% free!)

## Immediate Actions

### Quick Win: Docker Volumes (82.22 GB)
**BIGGEST WIN** - This alone will free up 82 GB!

```powershell
# 1. Stop Docker Desktop first
Stop-Process -Name "Docker Desktop" -Force -ErrorAction SilentlyContinue

# 2. Migrate Docker volumes
robocopy "C:\Users\mlesn\AppData\Local\Docker" "\\10.17.17.32\backups\docker" /MIR /MT:32 /R:1 /W:1 /FFT /XJ
```

### Other Quick Wins

1. **Pip Cache** (3.42 GB):
   ```powershell
   robocopy "C:\Users\mlesn\AppData\Local\pip\Cache" "\\10.17.17.32\backups\cache\pip" /MIR /MT:32 /R:1 /W:1 /FFT /XJ
   [Environment]::SetEnvironmentVariable("PIP_CACHE_DIR", "\\10.17.17.32\backups\cache\pip", "User")
   ```

2. **Temp Files** (4.57 GB):
   ```powershell
   robocopy "C:\Users\mlesn\AppData\Local\Temp" "\\10.17.17.32\backups\temp" /MOVE /MT:32 /R:1 /W:1 /FFT /XJ
   ```

3. **Downloads** (0.76 GB):
   ```powershell
   robocopy "C:\Users\mlesn\Downloads" "\\10.17.17.32\homes\mlesn\Downloads" /MIR /MT:32 /R:1 /W:1 /FFT /XJ
   ```

## Total Space to Free: ~91 GB

## Automated Scripts

### Option 1: Python Script (Recommended)
```powershell
# Dry run first
python scripts/python/urgent_nas_migration_accelerator.py

# Execute
python scripts/python/urgent_nas_migration_accelerator.py --execute

# Docker only (biggest win)
python scripts/python/urgent_nas_migration_accelerator.py --docker-only --execute
```

### Option 2: PowerShell Script
```powershell
. scripts/python/execute_urgent_migration_now.ps1
```

## Robocopy Speed Settings

- `/MT:32` - 32 threads (maximum speed)
- `/R:1` - 1 retry (fast)
- `/W:1` - 1 second wait (fast)
- `/MIR` - Mirror (delete files on target that don't exist in source)
- `/FFT` - Fast file times (faster on network)
- `/XJ` - Exclude junction points
- `/NP` - No progress (faster)

## Priority Order

1. **Docker Volumes** (82.22 GB) - CRITICAL
2. **Temp Files** (4.57 GB) - HIGH
3. **Pip Cache** (3.42 GB) - HIGH
4. **Downloads** (0.76 GB) - MEDIUM
5. **npm Cache** (0.50 GB) - MEDIUM

## Notes

- **Docker**: Must stop Docker Desktop before migration
- **Temp Files**: Use `/MOVE` to delete after copy (saves space immediately)
- **Pip Cache**: Set environment variable to redirect future cache
- **Downloads**: Can be redirected via folder redirection

## Verification

After migration, check free space:
```powershell
$drive = Get-PSDrive C
$freeGB = [math]::Round($drive.Free / 1GB, 2)
Write-Host "Free space: $freeGB GB"
```

Expected: ~144 GB free (52.86 + 91.47 GB freed)
