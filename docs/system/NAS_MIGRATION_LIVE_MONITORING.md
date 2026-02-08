# NAS Storage Engineering Migration - Live Monitoring

**Date**: 2026-01-01  
**Status**: 🟢 **ACTIVE MONITORING**  
**Tag**: #MIGRATION #NAS #MONITORING #LIVE

---

## 🎯 Overview

Live monitoring system for the NAS storage engineering migration of `my_projects` from C: drive to NAS.

**Migration Details**:
- **Source**: `C:\Users\mlesn\Dropbox\my_projects`
- **Destination**: `\\10.17.17.32\backups\MATT_Backups\my_projects`
- **Method**: Robocopy with /MIR (mirror)
- **Size**: ~2.98 TB
- **Status**: IN PROGRESS

---

## 📊 Monitoring Tools

### **1. Live Monitor (Real-Time)**

**Script**: `scripts/powershell/monitor_nas_migration_live.ps1`

**Features**:
- ✅ Real-time progress updates (every 5 seconds)
- ✅ Robocopy process status
- ✅ Source and destination statistics
- ✅ Progress percentage and remaining data
- ✅ Transfer speed calculation
- ✅ ETA (Estimated Time to Arrival)
- ✅ Recent log entries
- ✅ File count progress

**Usage**:
```powershell
# Start live monitoring
.\scripts\powershell\monitor_nas_migration_live.ps1

# With custom paths
.\scripts\powershell\monitor_nas_migration_live.ps1 `
  -SourcePath "C:\Users\mlesn\Dropbox\my_projects" `
  -DestPath "\\10.17.17.32\backups\MATT_Backups\my_projects" `
  -UpdateInterval 5
```

**What It Shows**:
- Robocopy process status (RUNNING/NOT RUNNING)
- Source directory size and file count
- Destination directory size and file count
- Progress percentage
- Remaining data (GB)
- Transfer speed (MB/s)
- ETA (hours:minutes:seconds)
- Elapsed time
- Recent log entries

---

### **2. Quick Status Check**

**Script**: `scripts/powershell/check_migration_status.ps1`

**Features**:
- ✅ One-time snapshot of migration status
- ✅ Quick progress check
- ✅ No continuous monitoring

**Usage**:
```powershell
# Quick status check
.\scripts\powershell\check_migration_status.ps1
```

**What It Shows**:
- Robocopy process status
- Source size and file count
- Destination size and file count
- Progress percentage
- Remaining data

---

## 🔍 Monitoring Metrics

### **Process Status**
- **RUNNING**: Robocopy is actively copying files
- **NOT RUNNING**: Migration completed or not started

### **Progress Metrics**
- **Completed**: Percentage of data copied
- **Remaining**: GB of data still to copy
- **Speed**: MB/s transfer rate
- **ETA**: Estimated time to completion

### **File Statistics**
- **Source Files**: Total files in source directory
- **Destination Files**: Files copied to destination
- **File Progress**: Percentage of files copied

---

## 📋 Log Files

### **Auto-Detection**
The monitor automatically detects the most recent log file from:
- `C:\Users\mlesn\Dropbox\my_projects\.lumina\migration_log_*.txt`
- `M:\migration_log_*.txt`
- `\\10.17.17.32\backups\MATT_Backups\migration_log_*.txt`

### **Manual Log File**
```powershell
# Specify log file manually
.\scripts\powershell\monitor_nas_migration_live.ps1 `
  -LogFile "M:\migration_log_20260101_190827.txt"
```

---

## 🚀 Quick Start

### **Start Live Monitoring**
```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\powershell\monitor_nas_migration_live.ps1
```

### **Quick Status Check**
```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\powershell\check_migration_status.ps1
```

---

## 📊 Example Output

### **Live Monitor Output**
```
╔════════════════════════════════════════════════════════════════╗
║   NAS STORAGE ENGINEERING MIGRATION - LIVE MONITOR            ║
╚════════════════════════════════════════════════════════════════╝

✅ Robocopy Process: RUNNING (PID: 49384)

📁 SOURCE: C:\Users\mlesn\Dropbox\my_projects
   Size: 2980.45 GB
   Files: 1,234,567
   Directories: 45,678

📁 DESTINATION: \\10.17.17.32\backups\MATT_Backups\my_projects
   Size: 1245.23 GB
   Files: 512,345
   Directories: 18,234

📊 PROGRESS:
   Completed: 41.78 percent
   Remaining: 1735.22 GB
   Speed: 45.67 MB/s
   ETA: 10:23:45

📈 FILE PROGRESS: 512,345 / 1,234,567 (41.50 percent)

⏱️  Elapsed Time: 08:15:32

📋 RECENT LOG ENTRIES:
   New File          12345   C:\Users\...\file.txt
   New Dir              123   C:\Users\...\directory\
```

---

## ⚙️ Configuration

### **Update Interval**
Default: 5 seconds

```powershell
# Change update interval (seconds)
.\scripts\powershell\monitor_nas_migration_live.ps1 -UpdateInterval 10
```

### **Custom Paths**
```powershell
.\scripts\powershell\monitor_nas_migration_live.ps1 `
  -SourcePath "C:\Custom\Source" `
  -DestPath "\\NAS\Custom\Dest"
```

---

## 🛑 Stopping Monitor

Press **Ctrl+C** to stop the live monitor.

---

## 📈 Interpreting Results

### **Progress Indicators**
- **0-25%**: Early stage, initial file structure being copied
- **25-50%**: Mid-stage, bulk data transfer
- **50-75%**: Late stage, most files copied
- **75-100%**: Final stage, completing remaining files

### **Speed Indicators**
- **>100 MB/s**: Excellent (1 Gbps network)
- **50-100 MB/s**: Good (500 Mbps network)
- **10-50 MB/s**: Acceptable (100 Mbps network)
- **<10 MB/s**: Slow (check network/NAS)

### **ETA Accuracy**
- ETA becomes more accurate as migration progresses
- Early ETA may be inaccurate due to varying file sizes
- Final 10% may take longer (small files, verification)

---

## ⚠️ Troubleshooting

### **Monitor Shows "NOT RUNNING"**
- Migration may have completed
- Check destination directory for completion
- Verify robocopy process manually: `Get-Process robocopy`

### **Destination Not Accessible**
- Check NAS connectivity: `ping 10.17.17.32`
- Verify network drive mapping: `net use`
- Check NAS credentials

### **Progress Not Updating**
- Destination may be slow to update
- Network latency may affect statistics
- Wait a few update cycles

### **Speed Shows 0 MB/s**
- Migration may be paused
- Network issue
- NAS I/O bottleneck

---

## 📚 Related Documentation

- [Dropbox Space Crisis Migration Plan](./DROPBOX_SPACE_CRISIS_MIGRATION_PLAN.md)
- [LUMINA Dropbox to NAS Migration](./LUMINA_DROPBOX_TO_NAS_MIGRATION.md)
- [Migration Execution Checklist](./MIGRATION_EXECUTION_CHECKLIST.md)

---

## ✅ Status

**Live Monitor**: ✅ **ACTIVE**  
**Quick Status**: ✅ **AVAILABLE**  
**Migration**: 🟢 **IN PROGRESS**

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: 🟢 ACTIVE MONITORING
