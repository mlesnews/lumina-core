# Cron Scheduler - Complete List of All Recurring Tasks

**Date**: 2025-01-24  
**Status**: ✅ **11 RECURRING TASKS SCHEDULED**  
**Total**: 1 Hourly + 4 Daily + 3 Weekly + 3 Monthly

---

## Complete Cron Entry List

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
- **Frequency**: **Every hour**

---

### DAILY TASKS (4)

#### 2. WOPR Daily Operations Check
- **Schedule**: Daily at 00:00 (midnight)
- **Cron**: `0 0 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_ops.py >> logs/wopr_daily_ops.log 2>&1
  ```
- **Purpose**: Daily operations check, containment status, threat indicators
- **Frequency**: **Daily at midnight**

#### 3. WOPR Status Report Generation
- **Schedule**: Daily at 06:00
- **Cron**: `0 6 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_status_report.py >> logs/wopr_status_report.log 2>&1
  ```
- **Purpose**: Generate status reports, update metrics, create summaries
- **Frequency**: **Daily at 6 AM**

#### 4. WOPR Threat Feed Check
- **Schedule**: Daily at 12:00 (noon)
- **Cron**: `0 12 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/holocron_threat_monitor.py --check >> logs/wopr_threat_feed.log 2>&1
  ```
- **Purpose**: Check threat intelligence feed, detect threat indicators
- **Frequency**: **Daily at noon**

#### 5. WOPR Containment Status Check
- **Schedule**: Daily at 18:00 (6 PM)
- **Cron**: `0 18 * * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_ops.py --containment-check >> logs/wopr_containment.log 2>&1
  ```
- **Purpose**: Check containment status, verify protocols
- **Frequency**: **Daily at 6 PM**

---

### WEEKLY TASKS (3)

#### 6. WOPR Weekly Summary Report
- **Schedule**: Weekly on Monday at 00:00
- **Cron**: `0 0 * * 1`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_status_report.py --weekly >> logs/wopr_weekly_report.log 2>&1
  ```
- **Purpose**: Generate weekly summary report
- **Frequency**: **Every Monday at midnight**

#### 7. WOPR Integration Verification
- **Schedule**: Weekly on Wednesday at 00:00
- **Cron**: `0 0 * * 3`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_integration.py --verify >> logs/wopr_integration.log 2>&1
  ```
- **Purpose**: Verify integration status, sync with Holocron Archive
- **Frequency**: **Every Wednesday at midnight**

#### 8. WOPR Threat Assessment Update
- **Schedule**: Weekly on Friday at 00:00
- **Cron**: `0 0 * * 5`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/holocron_threat_monitor.py --assessment >> logs/wopr_threat_assessment.log 2>&1
  ```
- **Purpose**: Update threat assessment, review threat indicators
- **Frequency**: **Every Friday at midnight**

---

### MONTHLY TASKS (3)

#### 9. WOPR Monthly Review
- **Schedule**: Monthly on day 1 at 00:00
- **Cron**: `0 0 1 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_ops.py --monthly-review >> logs/wopr_monthly_review.log 2>&1
  ```
- **Purpose**: Monthly review, comprehensive status check
- **Frequency**: **1st of every month at midnight**

#### 10. WOPR Killswitch Testing
- **Schedule**: Monthly on day 15 at 00:00
- **Cron**: `0 0 15 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_ops.py --killswitch-test >> logs/wopr_killswitch_test.log 2>&1
  ```
- **Purpose**: Test killswitch functionality, verify emergency protocols
- **Frequency**: **15th of every month at midnight**

#### 11. WOPR Metrics Compilation
- **Schedule**: Monthly on day 28 at 00:00
- **Cron**: `0 0 28 * *`
- **File**: `wopr_automation.cron`
- **Command**: 
  ```bash
  cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/wopr_status_report.py --monthly >> logs/wopr_monthly_metrics.log 2>&1
  ```
- **Purpose**: Compile monthly metrics, generate comprehensive reports
- **Frequency**: **28th of every month at midnight** (approximates last of month)

---

## Schedule Overview

| Frequency | Count | Times |
|-----------|-------|-------|
| **Hourly** | 1 | Every hour at :00 |
| **Daily** | 4 | 00:00, 06:00, 12:00, 18:00 |
| **Weekly** | 3 | Monday, Wednesday, Friday (all at 00:00) |
| **Monthly** | 3 | 1st, 15th, 28th (all at 00:00) |
| **TOTAL** | **11** | **11 recurring tasks** |

---

## Cron Files

### 1. `dropbox_optimized_daemon.cron`
- **Entries**: 1
- **Tasks**: Dropbox optimization daemon

### 2. `wopr_automation.cron`
- **Entries**: 10
- **Tasks**: All WOPR automation tasks (daily, weekly, monthly)

---

## Deployment Status

### ✅ Created
- All cron files created in `data/tasks/nas_kron/`
- Ready for deployment

### ⏳ Pending Deployment
- NAS SSH authentication needs configuration
- Once configured, deploy with: `python deploy_all_cron_to_nas.py`

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

### Deploy All
```bash
python scripts/python/deploy_all_cron_to_nas.py
```

---

## Files Location

- **Cron Files**: `data/tasks/nas_kron/*.cron`
- **JSON Export**: `data/tasks/nas_kron/all_scheduled_tasks.json`
- **Documentation**: `docs/system/ALL_CRON_SCHEDULER_ENTRIES.md`

---

## Status

✅ **11 Recurring Tasks Scheduled and Ready**

- ✅ 1 Hourly task (Dropbox optimization)
- ✅ 4 Daily tasks (WOPR operations)
- ✅ 3 Weekly tasks (WOPR reports)
- ✅ 3 Monthly tasks (WOPR reviews)

⏳ **Deployment**: Pending NAS SSH configuration

---

**Last Updated**: 2025-01-24

