# All Cron Scheduler Entries - Complete List

**Date**: 2025-01-24  
**Status**: ✅ **COMPLETE LISTING**  
**Total Recurring Tasks**: 11 cron entries

---

## Overview

Complete list of ALL cron scheduler entries for recurring tasks managed by NAS Kron.

---

## Cron Entries

### 1. Dropbox Optimized Processor Daemon
**File**: `dropbox_optimized_daemon.cron`  
**Schedule**: Every hour at minute 0  
**Cron**: `0 * * * *`  
**Command**: 
```bash
cd C:\Users\mlesn\Dropbox\my_projects\.lumina && python scripts/python/dropbox_optimized_daemon.py start --path "C:\Users\mlesn\Dropbox" --interval 60 >> logs/dropbox_daemon.log 2>&1
```
**Purpose**: Process Dropbox files with caching and resource-aware processing  
**Frequency**: Hourly

---

### 2. WOPR Daily Operations Check
**File**: `wopr_automation.cron`  
**Schedule**: Daily at 00:00 (midnight)  
**Cron**: `0 0 * * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_ops.py >> logs/wopr_daily_ops.log 2>&1
```
**Purpose**: Daily operations check, containment status, threat indicators  
**Frequency**: Daily

---

### 3. WOPR Status Report Generation
**File**: `wopr_automation.cron`  
**Schedule**: Daily at 06:00  
**Cron**: `0 6 * * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_status_report.py >> logs/wopr_status_report.log 2>&1
```
**Purpose**: Generate status reports, update metrics, create summaries  
**Frequency**: Daily

---

### 4. WOPR Threat Feed Check
**File**: `wopr_automation.cron`  
**Schedule**: Daily at 12:00 (noon)  
**Cron**: `0 12 * * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/holocron_threat_monitor.py --check >> logs/wopr_threat_feed.log 2>&1
```
**Purpose**: Check threat intelligence feed, detect threat indicators  
**Frequency**: Daily

---

### 5. WOPR Containment Status Check
**File**: `wopr_automation.cron`  
**Schedule**: Daily at 18:00 (6 PM)  
**Cron**: `0 18 * * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_ops.py --containment-check >> logs/wopr_containment.log 2>&1
```
**Purpose**: Check containment status, verify protocols  
**Frequency**: Daily

---

### 6. WOPR Weekly Summary Report
**File**: `wopr_automation.cron`  
**Schedule**: Weekly on Monday at 00:00  
**Cron**: `0 0 * * 1`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_status_report.py --weekly >> logs/wopr_weekly_report.log 2>&1
```
**Purpose**: Generate weekly summary report  
**Frequency**: Weekly (Monday)

---

### 7. WOPR Integration Verification
**File**: `wopr_automation.cron`  
**Schedule**: Weekly on Wednesday at 00:00  
**Cron**: `0 0 * * 3`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_integration.py --verify >> logs/wopr_integration.log 2>&1
```
**Purpose**: Verify integration status, sync with Holocron Archive  
**Frequency**: Weekly (Wednesday)

---

### 8. WOPR Threat Assessment Update
**File**: `wopr_automation.cron`  
**Schedule**: Weekly on Friday at 00:00  
**Cron**: `0 0 * * 5`  
**Command**: 
```bash
cd {project_root} && python scripts/python/holocron_threat_monitor.py --assessment >> logs/wopr_threat_assessment.log 2>&1
```
**Purpose**: Update threat assessment, review threat indicators  
**Frequency**: Weekly (Friday)

---

### 9. WOPR Monthly Review
**File**: `wopr_automation.cron`  
**Schedule**: Monthly on day 1 at 00:00  
**Cron**: `0 0 1 * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_ops.py --monthly-review >> logs/wopr_monthly_review.log 2>&1
```
**Purpose**: Monthly review, comprehensive status check  
**Frequency**: Monthly (1st of month)

---

### 10. WOPR Killswitch Testing
**File**: `wopr_automation.cron`  
**Schedule**: Monthly on day 15 at 00:00  
**Cron**: `0 0 15 * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_ops.py --killswitch-test >> logs/wopr_killswitch_test.log 2>&1
```
**Purpose**: Test killswitch functionality, verify emergency protocols  
**Frequency**: Monthly (15th of month)

---

### 11. WOPR Metrics Compilation
**File**: `wopr_automation.cron`  
**Schedule**: Monthly on day 28 at 00:00  
**Cron**: `0 0 28 * *`  
**Command**: 
```bash
cd {project_root} && python scripts/python/wopr_status_report.py --monthly >> logs/wopr_monthly_metrics.log 2>&1
```
**Purpose**: Compile monthly metrics, generate comprehensive reports  
**Frequency**: Monthly (28th of month - approximates last of month)

---

## Schedule Summary

### Hourly
- **Every hour**: Dropbox Optimized Processor Daemon

### Daily
- **00:00**: WOPR Daily Operations Check
- **06:00**: WOPR Status Report Generation
- **12:00**: WOPR Threat Feed Check
- **18:00**: WOPR Containment Status Check

### Weekly
- **Monday 00:00**: WOPR Weekly Summary Report
- **Wednesday 00:00**: WOPR Integration Verification
- **Friday 00:00**: WOPR Threat Assessment Update

### Monthly
- **1st at 00:00**: WOPR Monthly Review
- **15th at 00:00**: WOPR Killswitch Testing
- **28th at 00:00**: WOPR Metrics Compilation

---

## Deployment Status

### Local Cron Files
- ✅ `dropbox_optimized_daemon.cron` - Created
- ✅ `wopr_automation.cron` - Created

### NAS Kron Deployment
- ⏳ Pending (NAS SSH authentication needs configuration)
- ⏳ Cron files ready for deployment

---

## Deployment

### View All Entries
```bash
python scripts/python/show_all_scheduled_tasks.py
```

### Deploy All to NAS Kron
```bash
python scripts/python/deploy_all_cron_to_nas.py
```

### Deploy Individual Files
```bash
python nas_kron_daemon_manager.py --deploy data/tasks/nas_kron/dropbox_optimized_daemon.cron
python nas_kron_daemon_manager.py --deploy data/tasks/nas_kron/wopr_automation.cron
```

---

## Files

1. **Cron Files**:
   - `data/tasks/nas_kron/dropbox_optimized_daemon.cron`
   - `data/tasks/nas_kron/wopr_automation.cron`

2. **Scripts**:
   - `scripts/python/list_all_cron_entries.py` - List cron entries
   - `scripts/python/show_all_scheduled_tasks.py` - Comprehensive view
   - `scripts/python/create_all_cron_entries.py` - Create cron entries
   - `scripts/python/deploy_all_cron_to_nas.py` - Deploy to NAS

3. **Documentation**:
   - `docs/system/ALL_CRON_SCHEDULER_ENTRIES.md` - This file
   - `data/tasks/nas_kron/all_scheduled_tasks.json` - JSON export

---

## Status

✅ **11 Recurring Tasks Scheduled**
- 1 Hourly task
- 4 Daily tasks
- 3 Weekly tasks
- 3 Monthly tasks

⏳ **Deployment**: Pending NAS SSH configuration

---

**Last Updated**: 2025-01-24

