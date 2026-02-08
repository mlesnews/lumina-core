# Cursor Tasks to NAS Cron Scheduler Conversion

**Date**: 2026-01-02  
**Status**: ✅ **IMPLEMENTED**  
**Tag**: #CURSOR #NAS #CRON #SCHEDULER #AUTOMATION

---

## Overview

Automatically converts Cursor IDE tasks (`.cursor/tasks.json`) to NAS (Synology) cron scheduler tasks. This allows scheduled automation tasks to run on the NAS instead of requiring manual execution from Cursor IDE.

**Problem Solved**: Convert Cursor tasks to NAS cron format for automated execution on NAS.

---

## How It Works

### Conversion Process

1. **Reads** `.cursor/tasks.json` from Cursor IDE
2. **Filters** manual-only tasks (screenshots, troubleshooting, etc.)
3. **Converts** to NAS cron format with appropriate schedules
4. **Generates** multiple output formats:
   - JSON config file
   - Standard crontab format
   - DSM Task Scheduler script

### Task Scheduling

Tasks are automatically scheduled based on their purpose:

| Task | Schedule | Description |
|------|----------|-------------|
| JARVIS: Auto Git Commit | `0 */6 * * *` | Every 6 hours |
| JARVIS: Health Check | `0 */2 * * *` | Every 2 hours |
| JARVIS: Cursor IDE Optimization | `0 0 * * 0` | Weekly (Sunday) |
| JARVIS: Monitor IDE Notifications | `*/15 * * * *` | Every 15 minutes |
| SSO: Verify Readiness | `0 8 * * *` | Daily at 8 AM |

**Manual-Only Tasks** (not scheduled):
- MANUS: Quick Screenshot
- MANUS: Capture Screenshot with Context
- MANUS: Capture Screenshot
- LDAP: Troubleshoot Authentication
- SSO: Setup SAML

---

## Usage

### Convert All Tasks

```powershell
# Convert all Cursor tasks to NAS cron
python scripts/python/convert_cursor_tasks_to_nas_cron.py
```

### List Available Tasks

```powershell
# List all tasks and their schedules
python scripts/python/convert_cursor_tasks_to_nas_cron.py --list
```

### Custom Schedules

```powershell
# Set custom schedule for specific task
python scripts/python/convert_cursor_tasks_to_nas_cron.py \
  --custom-schedule "JARVIS: Health Check" "0 */1 * * *"
```

---

## Generated Files

### 1. JSON Config (`cursor_tasks_cron.json`)

Structured JSON with all cron task definitions:

```json
{
  "version": "1.0.0",
  "source": "Cursor IDE tasks.json",
  "generated": "2026-01-02T22:49:51",
  "tasks": [
    {
      "name": "JARVIS: Auto Git Commit",
      "schedule": "0 */6 * * *",
      "command": "python /volume1/lumina/scripts/python/jarvis_auto_git_manager.py --auto-commit --message '[AUTO] Auto-commit changes'",
      "enabled": true,
      "description": "Auto-generated from Cursor task: JARVIS: Auto Git Commit"
    }
  ]
}
```

### 2. Crontab Format (`cursor_tasks_crontab.txt`)

Standard crontab format for direct import:

```cron
# Cursor IDE Tasks - Converted to NAS Cron
# Generated: 2026-01-02T22:49:51
# Source: .cursor/tasks.json

# JARVIS: Auto Git Commit
0 */6 * * * python /volume1/lumina/scripts/python/jarvis_auto_git_manager.py --auto-commit --message '[AUTO] Auto-commit changes'

# JARVIS: Health Check
0 */2 * * * python /volume1/lumina/scripts/python/jarvis_health_check.py
```

### 3. DSM Script (`dsm_scheduler_import.sh`)

Shell script for DSM Task Scheduler import:

```bash
#!/bin/bash
# DSM Task Scheduler Import Script
# Generated: 2026-01-02T22:49:51
# Source: Cursor IDE tasks.json

# Task: JARVIS: Auto Git Commit
# Schedule: 0 */6 * * *
# Command: python /volume1/lumina/scripts/python/jarvis_auto_git_manager.py --auto-commit --message '[AUTO] Auto-commit changes'
echo "Adding task: JARVIS: Auto Git Commit"
```

---

## Deployment to NAS

### Method 1: Direct Crontab Import

1. **Copy crontab file to NAS**:
   ```bash
   scp scripts/nas/cron/cursor_tasks_crontab.txt admin@10.17.17.32:/tmp/
   ```

2. **SSH to NAS and import**:
   ```bash
   ssh admin@10.17.17.32
   crontab -l > /tmp/crontab_backup.txt  # Backup existing
   cat /tmp/cursor_tasks_crontab.txt >> /tmp/crontab_new.txt
   crontab /tmp/crontab_new.txt
   ```

### Method 2: DSM Task Scheduler

1. **Open DSM** → **Control Panel** → **Task Scheduler**
2. **Create** → **Scheduled Task** → **User-defined script**
3. **Copy** command from `cursor_tasks_crontab.txt`
4. **Set** schedule from cron format
5. **Save** and enable

### Method 3: Using NAS Kron Daemon Manager

```powershell
# Use existing NAS Kron Daemon Manager
python scripts/python/nas_kron_daemon_manager.py \
  --deploy scripts/nas/cron/cursor_tasks_crontab.txt
```

---

## Path Conversion

The converter automatically converts paths:

- **Cursor**: `${workspaceFolder}/scripts/python/script.py`
- **NAS**: `/volume1/lumina/scripts/python/script.py`

- **Cursor**: `scripts/python/script.py` (relative)
- **NAS**: `/volume1/lumina/scripts/python/script.py` (absolute)

---

## Customization

### Add Custom Schedule

Edit `DEFAULT_SCHEDULES` in `convert_cursor_tasks_to_nas_cron.py`:

```python
DEFAULT_SCHEDULES = {
    "JARVIS: Auto Git Commit": "0 */6 * * *",  # Every 6 hours
    "My Custom Task": "0 0 * * *",  # Daily at midnight
}
```

### Mark Task as Manual-Only

Add to `MANUAL_ONLY_TASKS` list:

```python
MANUAL_ONLY_TASKS = [
    "MANUS: Quick Screenshot",
    "My Manual Task",
]
```

---

## Cron Schedule Format

Standard cron format: `minute hour day month weekday`

| Field | Range | Example |
|-------|-------|---------|
| minute | 0-59 | `0`, `*/15` (every 15 min) |
| hour | 0-23 | `8`, `*/2` (every 2 hours) |
| day | 1-31 | `1`, `*` (every day) |
| month | 1-12 | `1`, `*` (every month) |
| weekday | 0-7 | `0` (Sunday), `*` (every day) |

**Examples**:
- `0 */6 * * *` - Every 6 hours
- `0 8 * * *` - Daily at 8 AM
- `*/15 * * * *` - Every 15 minutes
- `0 0 * * 0` - Weekly on Sunday

---

## Integration with Existing Systems

### NAS Kron Daemon Manager

The generated cron files work with the existing `nas_kron_daemon_manager.py`:

```python
from nas_kron_daemon_manager import NASKronDaemonManager

manager = NASKronDaemonManager()
manager.deploy_cron_to_nas(
    cron_file=Path("scripts/nas/cron/cursor_tasks_crontab.txt")
)
```

### JARVIS Task System

Cursor tasks integrate with JARVIS scheduled tasks:
- JARVIS tasks are automatically converted
- Schedules are preserved
- Commands are adapted for NAS environment

---

## Examples

### Example 1: Convert and Deploy

```powershell
# 1. Convert tasks
python scripts/python/convert_cursor_tasks_to_nas_cron.py

# 2. Review generated files
cat scripts/nas/cron/cursor_tasks_crontab.txt

# 3. Deploy to NAS
python scripts/python/nas_kron_daemon_manager.py \
  --deploy scripts/nas/cron/cursor_tasks_crontab.txt
```

### Example 2: Custom Schedule

```powershell
# Convert with custom schedule for health check
python scripts/python/convert_cursor_tasks_to_nas_cron.py \
  --custom-schedule "JARVIS: Health Check" "*/30 * * * *"
```

### Example 3: List Tasks

```powershell
# See all tasks and their schedules
python scripts/python/convert_cursor_tasks_to_nas_cron.py --list
```

---

## Troubleshooting

### Issue: Script Path Not Found

**Solution**: Ensure task uses `${workspaceFolder}` or relative path:
```json
{
  "args": [
    "${workspaceFolder}/scripts/python/script.py"
  ]
}
```

### Issue: Task Not Converted

**Solution**: Check if task is in `MANUAL_ONLY_TASKS` list. Manual tasks are intentionally skipped.

### Issue: Cron Not Running on NAS

**Solutions**:
- Verify Python path on NAS: `which python`
- Check cron service: `systemctl status cron`
- Review cron logs: `/var/log/cron.log`
- Test command manually on NAS first

---

## Benefits

✅ **Automated Execution**: Tasks run on NAS without manual intervention  
✅ **Centralized Scheduling**: All tasks managed in one place  
✅ **NAS Integration**: Works with existing NAS Kron Daemon Manager  
✅ **Easy Conversion**: One command converts all tasks  
✅ **Multiple Formats**: JSON, crontab, and DSM script outputs  

---

**Last Updated**: 2026-01-02  
**Status**: Ready to use  
**Script**: `scripts/python/convert_cursor_tasks_to_nas_cron.py`  
**Output**: `scripts/nas/cron/`
