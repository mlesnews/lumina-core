# @SCOTTY's Shortcut Investigation & Restoration Guide

**Tags:** `#SCOTTY` `#SHORTCUTS` `#DIAGNOSTICS` `#RESTORATION` `#DESKTOP` `#TOOLBAR` `@SCOTTY` `@LUMINA`

## Overview

This guide explains how @SCOTTY can investigate and restore missing desktop and toolbar shortcuts after a reboot.

## Problem

Desktop and toolbar shortcuts disappeared after a system reboot. This can happen due to:
- Temporary user profile loading
- Windows profile corruption
- OneDrive sync issues
- System restore or profile reset
- Registry corruption

## Investigation Tools

### 1. Run Shortcut Investigation

```powershell
# Basic investigation
.\scripts\powershell\scotty-investigate-shortcuts.ps1

# Detailed investigation with event log checks
.\scripts\powershell\scotty-investigate-shortcuts.ps1 -Detailed
```

**What it checks:**
- Desktop shortcuts (user and public)
- Taskbar pins (registry)
- Quick Launch shortcuts
- Start Menu shortcuts
- System restore points
- Windows profile status
- Event log entries

**Output:**
- JSON report saved to `data/scotty_shortcut_investigation.json`
- Console summary with recommendations

### 2. Restore Shortcuts

```powershell
# Check Recycle Bin
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRecycleBin

# Check OneDrive sync
.\scripts\powershell\scotty-restore-shortcuts.ps1 -CheckOneDrive

# Dry run (see what would be restored)
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRecycleBin -DryRun

# System Restore (requires admin)
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRestorePoint
```

## Common Scenarios & Solutions

### Scenario 1: Temporary Profile

**Symptoms:**
- Investigation shows "Temporary profile detected"
- Desktop is empty
- User folder path contains "Temp"

**Solution:**
1. Log out completely
2. Log back in
3. Windows should restore normal profile
4. If issue persists, check Event Viewer for profile errors

### Scenario 2: OneDrive Sync Issue

**Symptoms:**
- Desktop was synced to OneDrive
- Shortcuts exist in OneDrive but not on local Desktop

**Solution:**
```powershell
# Restore from OneDrive
.\scripts\powershell\scotty-restore-shortcuts.ps1 -CheckOneDrive
```

### Scenario 3: Shortcuts in Recycle Bin

**Symptoms:**
- Shortcuts were accidentally deleted
- Investigation shows shortcuts in Recycle Bin

**Solution:**
```powershell
# Restore from Recycle Bin
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRecycleBin
```

### Scenario 4: System Restore Needed

**Symptoms:**
- All shortcuts missing
- No backups found
- System restore points available

**Solution:**
```powershell
# List restore points
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRestorePoint

# Restore to specific point (requires admin)
.\scripts\powershell\scotty-restore-shortcuts.ps1 -FromRestorePoint -RestorePointSequence <number>
```

**⚠️ Warning:** System Restore affects the entire system, not just shortcuts.

## Manual Investigation Steps

### Check Desktop Locations

```powershell
# User Desktop
Get-ChildItem "$env:USERPROFILE\Desktop" -Filter "*.lnk"

# Public Desktop
Get-ChildItem "$env:PUBLIC\Desktop" -Filter "*.lnk"
```

### Check Taskbar Registry

```powershell
# Taskbar pins
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Taskband"
```

### Check Windows Event Log

```powershell
# Profile-related events
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    ProviderName = 'Microsoft-Windows-User Profiles Service'
    StartTime = (Get-Date).AddDays(-7)
} | Select-Object TimeCreated, Message
```

### Check Recycle Bin

```powershell
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.Namespace(0x0a)
$recycleBin.Items() | Where-Object { $_.Name -like "*.lnk" }
```

## Prevention

### 1. Enable File History

```powershell
# Check File History status
Get-WmiObject -Class Win32_UserProfile | Select-Object LocalPath, LastUseTime
```

### 2. Regular Desktop Backup

Create a scheduled task to backup desktop shortcuts:

```powershell
# Backup desktop shortcuts
$backupPath = "D:\Backups\Desktop"
New-Item -ItemType Directory -Path $backupPath -Force
Copy-Item "$env:USERPROFILE\Desktop\*.lnk" -Destination $backupPath -Recurse
```

### 3. OneDrive Desktop Sync

If using OneDrive, ensure Desktop sync is enabled and working properly.

## Integration with @SCOTTY's Reboot Optimization

The shortcut investigation can be integrated into @SCOTTY's reboot cycle:

```python
# In scotty_peak_reboot_optimization.py
def verify_shortcuts_after_reboot(self):
    """Verify shortcuts after reboot"""
    result = subprocess.run(
        ["powershell", "-File", "scripts/powershell/scotty-investigate-shortcuts.ps1"],
        capture_output=True
    )
    # Parse results and alert if shortcuts missing
```

## Troubleshooting

### Script Requires Admin Privileges

Some checks require administrator privileges. Run PowerShell as Administrator:

```powershell
# Right-click PowerShell -> Run as Administrator
```

### Shortcuts Exist But Don't Work

If shortcuts exist but don't launch applications:

1. Check target path is valid
2. Verify application still installed
3. Recreate shortcut if needed

### Profile Won't Load

If Windows keeps loading temporary profile:

1. Check Event Viewer for profile errors
2. Verify disk space available
3. Check registry permissions
4. May need to repair user profile

## Related Tools

- `scotty_peak_reboot_optimization.py` - Reboot cycle management
- `emergency_system_backup.ps1` - System backup tool
- Windows System Restore
- File History

## Support

For issues or questions:
- Check investigation report: `data/scotty_shortcut_investigation.json`
- Review Windows Event Viewer
- Check @SCOTTY logs: `data/scotty_peak_optimization.jsonl`

---

**USS Lumina - @scotty (Windows Systems Architect)**

*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
