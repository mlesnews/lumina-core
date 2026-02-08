# NAS Migration Real-Time Monitoring

**Date**: 2025-01-14  
**Status**: ✅ **MONITORING SYSTEM ACTIVE**

---

## 🎯 Overview

Real-time monitoring system that provides NAS migration status updates **every 15 minutes** automatically.

---

## 📊 Monitoring Features

### What It Monitors

1. **Disk Usage**
   - Current usage (GB and %)
   - Free space
   - Status (OK/WARNING/CRITICAL)

2. **Migration Status**
   - time_travel (2847 GB)
   - cursor_chat_archive (16.46 GB)
   - .lumina (67.39 GB)
   - cedarbrook-financial-services_llc-env (45.17 GB)
   - Docker AppData (133.84 GB)

3. **Robocopy Status**
   - Running processes
   - Log files
   - Progress tracking

4. **Summary Statistics**
   - Total migrated
   - In progress
   - Pending
   - Estimated space freed

---

## 🔧 Setup Options

### Option 1: Windows Scheduled Task (Recommended)

**Requires**: Administrator privileges

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell
powershell -ExecutionPolicy Bypass -File setup_nas_monitor_scheduled_task.ps1
```

**Benefits**:
- Runs automatically even after reboot
- No user session required
- System-level scheduling

### Option 2: Background Job

**Requires**: No admin privileges

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell
powershell -ExecutionPolicy Bypass -File start_nas_monitor_background.ps1
```

**Benefits**:
- No admin needed
- Runs in PowerShell background
- Easy to manage

### Option 3: Foreground Scheduler

**For**: Manual monitoring sessions

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell
powershell -ExecutionPolicy Bypass -File nas_migration_scheduler.ps1
```

**Benefits**:
- See output in real-time
- Easy to stop (Ctrl+C)
- Good for testing

---

## 📁 Output Files

### Status Report (JSON)
**Location**: `C:\Users\mlesn\Dropbox\my_projects\.lumina\data\nas_migration_status.json`

**Updated**: Every 15 minutes

**Contains**:
- Timestamp
- Disk usage details
- Migration status for each folder
- Robocopy status
- Summary statistics

### Monitor Log
**Location**: `C:\Users\mlesn\Dropbox\my_projects\.lumina\data\nas_migration_monitor.log`

**Contains**:
- All monitor runs
- Status messages
- Errors/warnings

---

## 📋 Viewing Status

### Quick Status View

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell
powershell -ExecutionPolicy Bypass -File view_nas_migration_status.ps1
```

### Manual Monitor Run

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\powershell
powershell -ExecutionPolicy Bypass -File nas_migration_realtime_monitor.ps1
```

---

## 🔍 Status Report Structure

```json
{
  "Timestamp": "2025-01-14 20:30:00",
  "DiskUsage": {
    "UsedGB": 3640.1,
    "FreeGB": 54.9,
    "TotalGB": 3695.0,
    "PercentUsed": 98.5,
    "Status": "🔴 CRITICAL"
  },
  "Migrations": [
    {
      "Name": "time_travel",
      "Status": "🔄 Copying (0.1%)",
      "LocalSizeGB": 2847.27,
      "NasSizeGB": 0.21,
      "Progress": 0.1,
      "IsSymlink": false
    }
  ],
  "Robocopy": {
    "IsRunning": true,
    "ProcessId": 30748
  },
  "Summary": {
    "MigratedCount": 0,
    "InProgressCount": 1,
    "PendingCount": 4,
    "EstimatedFreedGB": 0.21
  }
}
```

---

## 🎛️ Managing the Monitor

### Check Scheduled Task Status

```powershell
Get-ScheduledTask -TaskName "NAS_Migration_RealTime_Monitor"
```

### Start Task Manually

```powershell
Start-ScheduledTask -TaskName "NAS_Migration_RealTime_Monitor"
```

### Stop Task

```powershell
Stop-ScheduledTask -TaskName "NAS_Migration_RealTime_Monitor"
```

### Remove Task

```powershell
Unregister-ScheduledTask -TaskName "NAS_Migration_RealTime_Monitor" -Confirm:$false
```

### Check Background Job

```powershell
Get-Job -Name "NAS_Migration_Monitor"
Receive-Job -Name "NAS_Migration_Monitor" -Keep
```

### Remove Background Job

```powershell
Unregister-ScheduledJob -Name "NAS_Migration_Monitor"
```

---

## 📊 Example Output

```
================================================================================
NAS Migration Status Report
================================================================================

Last Updated: 2025-01-14 20:30:00

DISK USAGE:
  Used: 3640.1 GB / 3695.0 GB
  Free: 54.9 GB
  Usage: 98.5% - 🔴 CRITICAL

MIGRATION STATUS:
  time_travel:
    Status: 🔄 Copying (0.1%)
    Local: 2847.27 GB
    NAS: 0.21 GB
    Progress: 0.1%

  cursor_chat_archive:
    Status: Local Directory
    Local: 16.46 GB

SUMMARY:
  Migrated: 0
  In Progress: 1
  Pending: 4
  Estimated Freed: 0.21 GB

ROBOCOPY: Running (PID: 30748)
================================================================================
```

---

## ⚙️ Configuration

### Change Update Interval

Edit `nas_migration_scheduler.ps1` or `setup_nas_monitor_scheduled_task.ps1`:

```powershell
$intervalMinutes = 15  # Change to desired interval
```

### Add More Folders to Monitor

Edit `nas_migration_realtime_monitor.ps1`:

```powershell
$migrations = @(
    # Add new migration here
    @{
        Name = "new_folder"
        LocalPath = "C:\path\to\local"
        NasPath = "\\10.17.17.32\homes\mlesn\path\to\nas"
    }
)
```

---

## 🎯 Success Indicators

- ✅ Disk usage decreasing over time
- ✅ Migration progress increasing
- ✅ Symlinks appearing (migrations complete)
- ✅ Robocopy completing successfully
- ✅ Status reports updating every 15 minutes

---

**Last Updated**: 2025-01-14  
**Monitor Status**: Active  
**Update Interval**: 15 minutes
