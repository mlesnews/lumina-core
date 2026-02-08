# CRITICAL MEMORY: System Freeze Prevention (+++++)

**Priority**: 🔴🔴🔴🔴🔴 CRITICAL (5/5)
**Category**: System Stability - Highest Priority Memory
**Date**: 2026-01-07
**Status**: ACTIVE PREVENTION REQUIRED

## Critical Issue Summary

**Laptop completely hardlocks/freezes after ~5 minutes of uptime due to process proliferation.**

### Root Cause

**158+ Python processes** were running simultaneously, with **156+ instances of `jarvis_auto_accept_monitor.py`** spawning uncontrollably. This caused:
- Complete system freeze requiring hard reboot
- Resource exhaustion (CPU, memory, I/O)
- Data loss risk
- System instability

### Emergency Resolution

**Emergency Stop Script**: `scripts/python/emergency_stop_all_monitors.py`
- Successfully stopped **158 processes** on first run
- Must be run immediately when system shows signs of freezing

## Prevention Rules (MANDATORY)

### 1. Process Count Limits

**NEVER allow more than 10 Python processes running simultaneously.**

- **Check before starting any monitoring script:**
  ```powershell
  Get-Process | Where-Object {$_.ProcessName -like "*python*"} | Measure-Object
  ```
- **If count > 10**: Run `emergency_stop_all_monitors.py` FIRST
- **Maximum allowed**: 10 Python processes total

### 2. Auto-Accept Monitor Restrictions

**`jarvis_auto_accept_monitor.py` is FORBIDDEN from running multiple instances.**

- **MUST implement singleton pattern**
- **MUST check for existing instance before starting**
- **MUST use process lock file**
- **MUST auto-terminate duplicate instances**

### 3. Monitoring Script Consolidation

**NEVER run multiple monitoring scripts simultaneously without coordination.**

**Forbidden combinations:**
- ❌ `jarvis_compound_log_admin.py` + `jarvis_unified_health_system.py` + `jarvis_compound_log_health_monitor.py`
- ❌ Multiple instances of any monitoring script
- ❌ `jarvis_auto_accept_monitor.py` + any other monitor

**Allowed:**
- ✅ Single unified monitoring script
- ✅ One monitoring script at a time
- ✅ Coordinated monitoring through `jarvis_compound_log_admin.py` only

### 4. Resource Monitoring

**ALWAYS run diagnostic before starting new processes:**

```bash
python scripts/python/system_resource_diagnostic.py
```

**Stop if:**
- Python process count > 10
- Memory usage > 70%
- CPU usage > 70%
- Disk usage > 90%

### 5. Emergency Procedures

**If system shows signs of freezing:**

1. **IMMEDIATELY run:**
   ```bash
   python scripts/python/emergency_stop_all_monitors.py
   ```

2. **Wait 10 seconds, then verify:**
   ```bash
   python scripts/python/system_resource_diagnostic.py
   ```

3. **If still > 10 processes:**
   - Hard reboot if necessary
   - Run emergency stop again after reboot
   - Investigate root cause

## Implementation Requirements

### Immediate Actions Required

1. **Fix `jarvis_auto_accept_monitor.py`:** ✅ COMPLETED
   - [x] Add singleton pattern
   - [x] Add duplicate instance detection
   - [x] Add auto-termination of duplicates
   - **Status**: Singleton check added in `check_singleton()` function

2. **Add Process Count Monitoring:** ✅ COMPLETED
   - [x] Created `process_watchdog.py` - Continuous monitoring and auto-kill
   - [x] Created `startup_safety_check.py` - Pre-startup safety validation
   - [x] Auto-stop if count > 10
   - **Status**: Watchdog runs continuously, safety check runs before startup

3. **Consolidate Monitoring:** ✅ IN PROGRESS
   - [x] Created unified monitoring system (`monitoring/monitor.py`)
   - [ ] Remove duplicate monitoring scripts (Phase 2 consolidation)
   - [ ] Coordinate through admin script only

### Code Patterns Required

**All monitoring scripts MUST:**

```python
import psutil
import fcntl  # or msvcrt on Windows
from pathlib import Path

# Singleton check
LOCK_FILE = Path("/tmp/jarvis_monitor.lock")  # or Windows equivalent

def check_singleton():
    """Ensure only one instance runs"""
    try:
        # Check for existing processes
        count = sum(1 for p in psutil.process_iter(['name', 'cmdline'])
                   if 'python' in p.info.get('name', '').lower()
                   and 'jarvis_auto_accept_monitor.py' in ' '.join(p.info.get('cmdline', [])))
        
        if count > 1:
            print(f"❌ Already running ({count} instances). Exiting.")
            sys.exit(1)
    except Exception as e:
        logger.error(f"Singleton check failed: {e}")
        sys.exit(1)
```

## Monitoring Checklist

**Before starting ANY monitoring script:**

- [ ] Run `system_resource_diagnostic.py`
- [ ] Verify Python process count < 10
- [ ] Verify memory usage < 70%
- [ ] Verify CPU usage < 70%
- [ ] Check for existing instances of target script
- [ ] If auto-accept monitor: verify no other instances running

**After starting monitoring:**

- [ ] Wait 30 seconds
- [ ] Run diagnostic again
- [ ] Verify process count didn't increase unexpectedly
- [ ] Monitor for 5 minutes
- [ ] If process count grows: IMMEDIATELY stop

## Emergency Contacts

**If system freezes:**
1. Hard reboot
2. Run emergency stop script
3. Review this document
4. Fix root cause before restarting

## Related Files

- `scripts/python/emergency_stop_all_monitors.py` - Emergency process termination
- `scripts/python/system_resource_diagnostic.py` - Resource monitoring
- `scripts/python/process_watchdog.py` - **NEW**: Continuous process monitoring and auto-kill
- `scripts/python/startup_safety_check.py` - **NEW**: Pre-startup safety validation
- `scripts/python/jarvis_auto_accept_monitor.py` - **FIXED**: Now has singleton protection
- `docs/system/CRITICAL_SYSTEM_FREEZE_ISSUE.md` - Full incident report

## New Safety Tools

### Process Watchdog
```bash
# Run continuously (recommended)
python scripts/python/process_watchdog.py

# One-time check
python scripts/python/process_watchdog.py --check

# Kill excess processes immediately
python scripts/python/process_watchdog.py --kill
```

### Startup Safety Check
```bash
# Run before starting any monitoring script
python scripts/python/startup_safety_check.py
```

**RECOMMENDED WORKFLOW:**
1. Before starting any monitor: `python scripts/python/startup_safety_check.py`
2. If safe, start your monitor
3. Run watchdog in background: `python scripts/python/process_watchdog.py`

## Tags

#CRITICAL #MEMORY #SYSTEM_STABILITY #PROCESS_MANAGEMENT #EMERGENCY #FREEZE #PREVENTION @JARVIS @LUMINA

---

**THIS IS A CRITICAL MEMORY - ALWAYS CHECK PROCESS COUNT BEFORE STARTING MONITORING**
