# Tail Compound Log Guide

**Date**: 2026-01-06  
**Status**: ✅ **OPERATIONAL**  
**Purpose**: Tail compound log in external terminal console

---

## Overview

Tail the compound log file in an external terminal console for real-time monitoring. Similar to `tail -f` on Linux or `Get-Content -Wait` on PowerShell.

---

## Usage

### Windows (PowerShell)

```bash
# Open external terminal and tail compound log
python scripts/python/jarvis_tail_compound_log.py
```

This will:
1. Open a new PowerShell window
2. Display the compound log file path
3. Tail the log file with last 50 lines
4. Show real-time updates as new log entries are written

### Manual PowerShell Command

```powershell
# Navigate to project root
cd "C:\Users\mlesn\Dropbox\my_projects\.lumina"

# Tail the compound log
Get-Content -Path "data\compound_log_health\compound.log" -Wait -Tail 50
```

### Linux/Mac

```bash
# Open external terminal and tail compound log
python scripts/python/jarvis_tail_compound_log.py
```

Or manually:
```bash
tail -f data/compound_log_health/compound.log
```

---

## Compound Log Location

- **Path**: `data/compound_log_health/compound.log`
- **Format**: `[TIMESTAMP] [SOURCE] MESSAGE`
- **Tailing**: Real-time updates

---

## Log Format

### Entry Format

```
[YYYY-MM-DD HH:MM:SS] [SOURCE] MESSAGE
```

### Sources

- `ASK_PROCESSOR`: Ask processing operations
- `HEALTH_CHECK`: Health check results
- `UNIFIED_HEALTH`: Unified health system
- `SYSTEM`: System operations
- `APPLICATION`: Application operations

### Examples

```
[2026-01-06 12:03:08] [ASK_PROCESSOR] Starting batch processing: 100 asks, limit: 100
[2026-01-06 12:03:15] [ASK_PROCESSOR] Processing: scripts\python\jarvis_ask_stack_analyzer.py (Priority: HIGH)
[2026-01-06 12:03:20] [ASK_PROCESSOR] Batch processing complete: Processed=100, Skipped=0, Failed=0
[2026-01-06 12:03:25] [HEALTH_CHECK] Health check: ask_processor - HEALTHY
[2026-01-06 12:03:30] [UNIFIED_HEALTH] Overall health: HEALTHY
```

---

## Features

### Real-Time Updates

- **Tailing**: Shows last 50 lines initially
- **Updates**: New entries appear in real-time
- **Scroll**: Automatically scrolls to show new entries

### External Terminal

- **New Window**: Opens in separate terminal window
- **Independent**: Doesn't block main terminal
- **Multiple**: Can open multiple tail windows

### Stop Tailing

- **Windows**: Press `Ctrl+C` in the tail window
- **Linux/Mac**: Press `Ctrl+C` in the tail window

---

## Integration

### With Health Monitoring

The compound log is automatically tailed by:
- **Compound Log Health Monitor**: Real-time parsing
- **Unified Health System**: Health status monitoring
- **System Health Checker**: Health check results

### With Systems

All systems write to compound log:
- **Ask Processor**: Batch operations
- **Live Monitor**: Status updates
- **Health Checker**: Health check results
- **Unified Health**: Overall health status

---

## Scripts

### 1. Python Script
- **File**: `scripts/python/jarvis_tail_compound_log.py`
- **Purpose**: Open external terminal and tail log
- **Platform**: Windows, Linux, Mac

### 2. PowerShell Script
- **File**: `scripts/python/tail_compound_log.ps1`
- **Purpose**: Tail log in PowerShell
- **Platform**: Windows

---

## Troubleshooting

### Log File Not Found

If the log file doesn't exist, it will be created automatically.

### Terminal Not Opening

- **Windows**: Ensure PowerShell is available
- **Linux**: Ensure `gnome-terminal` or `xterm` is installed
- **Mac**: Ensure terminal is available

### No Updates

- Check if systems are writing to compound log
- Verify compound log health monitor is running
- Check log file permissions

---

## Conclusion

**Tail compound log in external terminal**:
- ✅ Opens new terminal window
- ✅ Shows real-time log updates
- ✅ Easy to use
- ✅ Platform-independent

---

**Date**: 2026-01-06  
**Status**: Operational  
**Next**: Use `python scripts/python/jarvis_tail_compound_log.py` to tail the log

@JARVIS @LUMINA #TAIL #COMPOUND_LOG #EXTERNAL_TERMINAL #LIVE_MONITORING
