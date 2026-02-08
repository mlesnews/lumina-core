# Scheduled Automation Tasks

**Date**: 2025-01-24  
**Status**: 📋 **SCHEDULED TASKS CONFIGURED**  
**Tag**: @JARVIS @MARVIN

---

## Overview

Scheduled automation tasks for password rotation and sync operations.

---

## Daily Tasks

### Password Rotation Check

**Script**: `scripts/python/daily_password_rotation_check.py`  
**Schedule**: Daily at 02:00 AM  
**Purpose**: Check for credentials due for rotation and auto-rotate if enabled

**Tasks**:
- Check credentials due for rotation
- Auto-rotate if policy allows
- Check upcoming rotations (next 7 days)
- Log rotation status

**Cron (Linux/Mac)**:
```bash
0 2 * * * python /path/to/scripts/python/daily_password_rotation_check.py >> /path/to/logs/rotation_check.log 2>&1
```

**Scheduled Task (Windows PowerShell)**:
```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "scripts\python\daily_password_rotation_check.py"
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -TaskName "DailyPasswordRotationCheck" -Action $action -Trigger $trigger
```

---

## Weekly Tasks

### Password Manager Sync

**Script**: `scripts/python/weekly_password_sync.py`  
**Schedule**: Weekly on Sunday at 02:00 AM  
**Purpose**: Sync ProtonPass → Dashlane for backup

**Tasks**:
- Export from ProtonPass
- Convert to Dashlane format
- Generate CSV file for Dashlane import
- Log sync results

**Cron (Linux/Mac)**:
```bash
0 2 * * 0 python /path/to/scripts/python/weekly_password_sync.py >> /path/to/logs/password_sync.log 2>&1
```

**Scheduled Task (Windows PowerShell)**:
```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "scripts\python\weekly_password_sync.py"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
Register-ScheduledTask -TaskName "WeeklyPasswordSync" -Action $action -Trigger $trigger
```

---

## Manual Tasks

### Credential Inventory

**Script**: `scripts/python/inventory_credentials.py`  
**Schedule**: On-demand or monthly  
**Purpose**: Inventory all credentials and register with rotation manager

**Usage**:
```bash
# Create inventory
python scripts/python/inventory_credentials.py --inventory

# Register with rotation manager
python scripts/python/inventory_credentials.py --register

# Both
python scripts/python/inventory_credentials.py --all
```

---

## Integration with JARVIS

All scheduled tasks should be managed by JARVIS workflow automation:
- JARVIS monitors task execution
- JARVIS handles errors and alerts
- JARVIS integrates with MARVIN for compliance checking
- JARVIS integrates with HK-47 for threat monitoring

---

## Logging

All scheduled tasks log to:
- Console output
- Log files (if configured)
- JARVIS workflow system
- Audit logs for compliance

**No secrets are logged** - All logging complies with SECRET_MANAGEMENT_POLICY.

---

## References

- **Password Rotation**: `docs/security/PASSWORD_ROTATION_SECURITY_POLICY.md`
- **Password Sync**: `docs/system/PASSWORD_MANAGER_SYNC_STRATEGY.md`
- **Secret Management**: `docs/security/SECRET_MANAGEMENT_POLICY.md`
- **Triad System**: `docs/system/TRIAD_PASSWORD_MANAGER_SYSTEM.md`

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS