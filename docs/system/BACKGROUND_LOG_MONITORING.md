# Background Log Monitoring

**Date**: 2026-01-01  
**Status**: ✅ **ACTIVE**  
**Tag**: #MIGRATION #MONITORING #BACKGROUND

---

## Overview

Background log monitor tracks migration progress continuously without blocking your terminal.

---

## How It Works

### Background Monitor
- Runs in hidden PowerShell window
- Monitors log file every 10 seconds
- Tracks errors and progress
- Updates status file (`migration_status.json`)

### Status File
- Location: `C:\Users\mlesn\Dropbox\my_projects\.lumina\migration_status.json`
- Updated every 10 seconds
- Contains: files copied, errors, error rates, timestamps

---

## Usage

### Start Background Monitor
```powershell
powershell -File scripts/powershell/monitor_logs_background.ps1
```

Or run in hidden window:
```powershell
Start-Process powershell -ArgumentList "-WindowStyle Hidden", "-File", "scripts/powershell/monitor_logs_background.ps1"
```

### Check Status Anytime
```powershell
powershell -File scripts/powershell/show_log_status.ps1
```

### Tail Logs Live
```powershell
powershell -File scripts/powershell/tail_logs_with_analysis.ps1
```

---

## Status Information

**Shows:**
- Files copied count
- Total errors
- ERROR 59 (Network errors)
- ERROR 5 (Access denied)
- Error rate (last 5 minutes)
- Success rate (last 5 minutes)
- Log file size

---

## Benefits

✅ **Runs in background** - Doesn't block terminal  
✅ **Continuous monitoring** - Tracks progress 24/7  
✅ **Error tracking** - Identifies problems immediately  
✅ **Quick status checks** - See progress anytime  
✅ **Team coordination** - All teams can check status  

---

## Integration with Teams

**NETWORK TEAM**: Check ERROR 59 rates  
**STORAGE TEAM**: Check ERROR 5 rates  
**SYSTEM TEAM**: Monitor overall progress  

All teams can check status file to coordinate fixes!

---

**Status**: Background monitor running  
**Update Interval**: 10 seconds  
**Status File**: `migration_status.json`
