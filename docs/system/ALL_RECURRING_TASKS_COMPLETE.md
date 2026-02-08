# All Recurring Tasks - Complete Inventory

**Date**: 2025-01-24  
**Status**: ✅ **14 RECURRING TASKS IDENTIFIED**  
**Migration Status**: 3 tasks migrated from host-level

---

## Complete List of All 14 Recurring Tasks

### HOURLY TASKS (1)

#### 1. Dropbox Optimized Processor Daemon
- **Schedule**: Every hour at minute 0
- **Cron**: `0 * * * *`
- **File**: `dropbox_optimized_daemon.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/dropbox_optimized_daemon.py start --path "C:\Users\mlesn\Dropbox" --interval 60 >> logs/dropbox_daemon.log 2>&1
  ```
- **Purpose**: Process Dropbox files with caching and resource-aware processing
- **Status**: ✅ Created, ready for NAS Kron

---

### DAILY TASKS (8)

#### 2. Jocasta Nu Daily Operations ⚠️ **MIGRATED FROM HOST**
- **Schedule**: Daily at 05:30
- **Cron**: `30 5 * * *`
- **File**: `jocasta_nu_daily_ops.cron`
- **Command**: 
  ```bash
  cd {project_root} && python /volume1/docker/jarvis/Dropbox/my_projects/fvh/scripts/python/jocastanu_scheduled_ops.py >> logs/jocasta_daily_ops.log 2>&1
  ```
- **Purpose**: Scan, classify, catalog holocrons (Jupyter Notebooks). Collection development decisions, catalog maintenance, organization.
- **Status**: ✅ **MIGRATED** from Windows Task Scheduler (`Lumina_JocastaNu_DailyOps`)
- **Original**: Windows Task Scheduler (daily at 5:30 AM)

#### 3. Scheduled System Diagnostics ⚠️ **NEW**
- **Schedule**: Daily at 02:00
- **Cron**: `0 2 * * *`
- **File**: `scheduled_diagnostics.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/run_scheduled_diagnostics.py >> logs/scheduled_diagnostics.log 2>&1
  ```
- **Purpose**: Runs memory integrity and event viewer diagnostics
- **Status**: ✅ Created, ready for NAS Kron

#### 4. WOPR Daily Operations Check
- **Schedule**: Daily at 00:00 (midnight)
- **Cron**: `0 0 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_ops.py >> logs/wopr_daily_ops.log 2>&1
  ```
- **Purpose**: Daily operations check, containment status, threat indicators
- **Status**: ✅ Created, ready for NAS Kron

#### 5. WOPR Status Report Generation
- **Schedule**: Daily at 06:00
- **Cron**: `0 6 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_status_report.py >> logs/wopr_status_report.log 2>&1
  ```
- **Purpose**: Generate status reports, update metrics, create summaries
- **Status**: ✅ Created, ready for NAS Kron

#### 6. WOPR Threat Feed Check
- **Schedule**: Daily at 12:00 (noon)
- **Cron**: `0 12 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/holocron_threat_monitor.py --check >> logs/wopr_threat_feed.log 2>&1
  ```
- **Purpose**: Check threat intelligence feed, detect threat indicators
- **Status**: ✅ Created, ready for NAS Kron

#### 7. WOPR Containment Status Check
- **Schedule**: Daily at 18:00 (6 PM)
- **Cron**: `0 18 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_ops.py --containment-check >> logs/wopr_containment.log 2>&1
  ```
- **Purpose**: Check containment status, verify protocols
- **Status**: ✅ Created, ready for NAS Kron

#### 8. Cursor Workspace Sync ⚠️ **NEW**
- **Schedule**: Every 6 hours
- **Cron**: `0 */6 * * *`
- **File**: `cursor_workspace_sync.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/cursor_workspace_sync_cron.py >> logs/cursor_workspace_sync.log 2>&1
  ```
- **Purpose**: Syncs workspace settings between workspace and non-workspace modes
- **Status**: ✅ Created, ready for NAS Kron

---

### WEEKLY TASKS (3)

#### 9. WOPR Weekly Summary Report
- **Schedule**: Weekly on Monday at 00:00
- **Cron**: `0 0 * * 1`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_status_report.py --weekly >> logs/wopr_weekly_report.log 2>&1
  ```
- **Purpose**: Generate weekly summary report
- **Status**: ✅ Created, ready for NAS Kron

#### 10. WOPR Integration Verification
- **Schedule**: Weekly on Wednesday at 00:00
- **Cron**: `0 0 * * 3`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_integration.py --verify >> logs/wopr_integration.log 2>&1
  ```
- **Purpose**: Verify integration status, sync with Holocron Archive
- **Status**: ✅ Created, ready for NAS Kron

#### 11. WOPR Threat Assessment Update
- **Schedule**: Weekly on Friday at 00:00
- **Cron**: `0 0 * * 5`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/holocron_threat_monitor.py --assessment >> logs/wopr_threat_assessment.log 2>&1
  ```
- **Purpose**: Update threat assessment, review threat indicators
- **Status**: ✅ Created, ready for NAS Kron

---

### MONTHLY TASKS (3)

#### 12. WOPR Monthly Review
- **Schedule**: Monthly on day 1 at 00:00
- **Cron**: `0 0 1 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_ops.py --monthly-review >> logs/wopr_monthly_review.log 2>&1
  ```
- **Purpose**: Monthly review, comprehensive status check
- **Status**: ✅ Created, ready for NAS Kron

#### 13. WOPR Killswitch Testing
- **Schedule**: Monthly on day 15 at 00:00
- **Cron**: `0 0 15 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_ops.py --killswitch-test >> logs/wopr_killswitch_test.log 2>&1
  ```
- **Purpose**: Test killswitch functionality, verify emergency protocols
- **Status**: ✅ Created, ready for NAS Kron

#### 14. WOPR Metrics Compilation
- **Schedule**: Monthly on day 28 at 00:00
- **Cron**: `0 0 28 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd {project_root} && python scripts/python/wopr_status_report.py --monthly >> logs/wopr_monthly_metrics.log 2>&1
  ```
- **Purpose**: Compile monthly metrics, generate comprehensive reports
- **Status**: ✅ Created, ready for NAS Kron

---

## Migration Summary

### Tasks Migrated from Host-Level (3)

1. ✅ **Jocasta Nu Daily Operations**
   - **From**: Windows Task Scheduler (`Lumina_JocastaNu_DailyOps`)
   - **To**: NAS Kron (`jocasta_nu_daily_ops.cron`)
   - **Schedule**: Daily at 5:30 AM (preserved)
   - **Status**: ✅ Migrated

2. ✅ **Cursor Workspace Sync**
   - **From**: Not scheduled (script exists but wasn't scheduled)
   - **To**: NAS Kron (`cursor_workspace_sync.cron`)
   - **Schedule**: Every 6 hours
   - **Status**: ✅ Newly scheduled

3. ✅ **Scheduled Diagnostics**
   - **From**: Not scheduled (script exists but wasn't scheduled)
   - **To**: NAS Kron (`scheduled_diagnostics.cron`)
   - **Schedule**: Daily at 2:00 AM
   - **Status**: ✅ Newly scheduled

---

## Schedule Overview

| Frequency | Count | Times |
|-----------|-------|-------|
| **Hourly** | 1 | Every hour at :00 |
| **Every 6 Hours** | 1 | :00, :06, :12, :18 |
| **Daily** | 6 | 00:00, 02:00, 05:30, 06:00, 12:00, 18:00 |
| **Weekly** | 3 | Monday, Wednesday, Friday (all at 00:00) |
| **Monthly** | 3 | 1st, 15th, 28th (all at 00:00) |
| **TOTAL** | **14** | **14 recurring tasks** |

---

## Cron Files

### 1. `dropbox_optimized_daemon.cron`
- **Entries**: 1
- **Tasks**: Dropbox optimization daemon

### 2. `jocasta_nu_daily_ops.cron` ⚠️ **MIGRATED**
- **Entries**: 1
- **Tasks**: Jocasta Nu daily operations (migrated from Windows)

### 3. `cursor_workspace_sync.cron` ⚠️ **NEW**
- **Entries**: 1
- **Tasks**: Cursor workspace sync

### 4. `scheduled_diagnostics.cron` ⚠️ **NEW**
- **Entries**: 1
- **Tasks**: System diagnostics

### 5. `wopr_automation.cron`
- **Entries**: 10
- **Tasks**: All WOPR automation tasks (daily, weekly, monthly)

---

## Host-Level Tasks Still on Windows

### Windows Task Scheduler
- **Lumina_JocastaNu_DailyOps** - ⚠️ **SHOULD BE DISABLED** after NAS migration verified

### Other Windows Tasks
- All other Windows tasks are system tasks (Microsoft, Windows, etc.) - **KEEP ON HOST**

---

## Deployment Status

### ✅ Created
- All 14 cron entries created in `data/tasks/nas_kron/`
- Ready for deployment

### ⏳ Pending Deployment
- NAS SSH authentication needs configuration
- Once configured, deploy with: `python deploy_all_cron_to_nas.py`

### ⚠️ Post-Migration
- Disable Windows Task Scheduler task: `Lumina_JocastaNu_DailyOps`
- Verify NAS Kron execution before disabling Windows task

---

## Viewing All Entries

### Quick View
```bash
python scripts/python/list_all_cron_entries.py
```

### Comprehensive View
```bash
python scripts/python/show_all_scheduled_tasks.py
```

### Audit Host Tasks
```bash
python scripts/python/audit_host_scheduled_tasks.py
```

### Deploy All
```bash
python scripts/python/deploy_all_cron_to_nas.py
```

---

## Files Location

- **Cron Files**: `data/tasks/nas_kron/*.cron`
- **Audit Report**: `data/tasks/nas_kron/host_tasks_audit.json`
- **JSON Export**: `data/tasks/nas_kron/all_scheduled_tasks.json`
- **Documentation**: `docs/system/ALL_RECURRING_TASKS_COMPLETE.md` (this file)

---

## Status

✅ **14 Recurring Tasks Identified and Scheduled**

- ✅ 1 Hourly task
- ✅ 1 Every 6 hours task
- ✅ 6 Daily tasks
- ✅ 3 Weekly tasks
- ✅ 3 Monthly tasks

✅ **3 Tasks Migrated from Host-Level**

- ✅ Jocasta Nu Daily Operations (from Windows Task Scheduler)
- ✅ Cursor Workspace Sync (newly scheduled)
- ✅ Scheduled Diagnostics (newly scheduled)

⏳ **Deployment**: Pending NAS SSH configuration

---

**Last Updated**: 2025-01-24




