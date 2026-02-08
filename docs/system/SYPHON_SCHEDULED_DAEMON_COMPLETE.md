# SYPHON Scheduled Daemon - Complete Integration

**Status**: ✅ **COMPLETE**  
**Date**: 2026-01-05  
**NAS KronScheduler**: kronscheduler.lesnewski.local  
**NAS Email Hub**: email-hub.lesnewski.local

#JARVIS #LUMINA #SYPHON #DAEMON #NAS #KRONSCHEDULER #INTERNAL #EXTERNAL

---

## Overview

Regularly scheduled task daemon for @SYPHON'ing @sources (both #internal and #external) via NAS KronScheduler.

**Priority Order:**
1. **#internal**: Filesystems (FIRST PRIORITY)
2. **#external**: Email sources (Gmail, ProtonMail, NAS Email Hub)
3. **#external**: Financial accounts (Personal + Business)

---

## Features

### ✅ Scheduled Execution
- Runs every 6 hours via NAS KronScheduler
- Single cycle mode (for cron execution)
- Continuous daemon mode (optional)
- Configurable intervals per source

### ✅ Source Types

**#internal Sources:**
- Filesystems (Priority 1)
- Local data sources
- Internal databases

**#external Sources:**
- Email: Gmail, ProtonMail, NAS Email Hub
- Financial: Personal + Business accounts
- APIs and external services

### ✅ Integration Points

**NAS KronScheduler:**
- Host: kronscheduler.lesnewski.local
- Cron schedule: Every 6 hours
- Automated deployment

**NAS Email Hub:**
- Host: email-hub.lesnewski.local
- N8N webhook: `/webhook/email/hub/receive`
- Integrated with email workflows

**N8N:**
- Host: 10.17.17.32:5678
- Workflow integration
- Email processing

---

## Configuration

### Source Configuration

**File**: `config/syphon_scheduled_sources.json`

**Sources:**
1. **filesystems** (#internal, Priority 1, 24h interval)
2. **email_gmail** (#external, Priority 2, 6h interval)
3. **email_protonmail** (#external, Priority 2, 6h interval)
4. **email_nas_hub** (#external, Priority 2, 5h interval)
5. **financial_personal** (#external, Priority 3, 24h interval)
6. **financial_business** (#external, Priority 3, 24h interval)

### Schedule

**Default**: Every 6 hours (`0 */6 * * *`)

**Alternative**: Every 4 hours (`0 */4 * * *`)

**Per Source**: Configurable intervals in source config

---

## Usage

### Run Single Cycle (for Cron)

```bash
python scripts/python/syphon_scheduled_daemon_nas_kron.py --cycle
```

**Output:**
- SYPHONs all sources (internal + external)
- Saves results to `data/syphon_scheduled/results/`
- Logs to `data/syphon_scheduled/logs/`

### Run as Continuous Daemon

```bash
python scripts/python/syphon_scheduled_daemon_nas_kron.py --daemon --interval 6
```

**Features:**
- Runs continuously
- Checks every minute for scheduled execution
- Runs cycle at configured intervals
- Graceful shutdown (Ctrl+C)

### Deploy to NAS KronScheduler

```bash
python scripts/python/syphon_scheduled_daemon_nas_kron.py --deploy
```

**Actions:**
- Creates cron file
- Deploys to NAS KronScheduler
- Configures scheduled execution

---

## NAS KronScheduler Integration

### Cron File

**Location**: `data/syphon_scheduled/syphon_scheduled.cron`

**Schedule**: `0 */6 * * *` (every 6 hours)

**Command**: 
```bash
python /path/to/syphon_scheduled_daemon_nas_kron.py --cycle >> /path/to/logs/syphon_scheduled.log 2>&1
```

### Deployment

**Automated**:
```bash
python scripts/python/syphon_scheduled_daemon_nas_kron.py --deploy
```

**Manual**:
1. Copy cron file to NAS
2. Add to NAS KronScheduler
3. Verify execution

---

## Source Processing

### Internal Sources (#internal)

**Filesystems:**
- Priority: 1 (FIRST)
- Interval: 24 hours
- Uses: Comprehensive SYPHON System
- Extracts: File intelligence, patterns, data

### External Sources (#external)

**Email Sources:**
- Gmail: 6h interval
- ProtonMail: 6h interval
- NAS Email Hub: 5h interval (via N8N)
- Uses: Unified Email Service, N8N webhooks

**Financial Sources:**
- Personal: 24h interval
- Business: 24h interval (CEDARBROOK-FINANCIAL-SERVICES-LLC)
- Uses: Comprehensive SYPHON System

---

## Results

### Output Files

**Results**: `data/syphon_scheduled/results/cycle_YYYYMMDD_HHMMSS.json`

**Logs**: `data/syphon_scheduled/logs/syphon_scheduled.log`

**PID File**: `data/syphon_scheduled/syphon_daemon.pid` (daemon mode)

### Result Structure

```json
{
  "timestamp": "2026-01-05T12:00:00",
  "cycle_id": "20260105_120000",
  "internal": {
    "source_type": "internal",
    "sources": [...],
    "total_items": 150,
    "success": true
  },
  "external": {
    "source_type": "external",
    "sources": [...],
    "total_items": 45,
    "success": true
  },
  "success": true
}
```

---

## Integration with Email Hub

### NAS Email Hub

**Host**: email-hub.lesnewski.local  
**N8N Webhook**: `http://10.17.17.32:5678/webhook/email/hub/receive`

**Process:**
1. Daemon triggers N8N webhook
2. N8N workflow checks NAS Email Hub IMAP
3. Retrieves new emails
4. Processes via SYPHON
5. Returns email count

### Gmail & ProtonMail

**Process:**
1. Daemon uses Unified Email Service
2. Searches for recent emails (last 24 hours)
3. Counts emails found
4. Logs results

---

## Monitoring

### Logs

**Location**: `data/syphon_scheduled/logs/`

**Files:**
- `syphon_scheduled.log` - Main log file
- `cycle_*.json` - Individual cycle results

### Status

**Check Status**:
```bash
# Check if daemon is running (daemon mode)
cat data/syphon_scheduled/syphon_daemon.pid

# Check last cycle result
ls -lt data/syphon_scheduled/results/ | head -1
```

### Metrics

**Tracked:**
- Cycles executed
- Items extracted (internal + external)
- Success rate
- Last execution time
- Source-specific metrics

---

## Troubleshooting

### Common Issues

1. **NAS KronScheduler Not Accessible**
   - Check network connectivity
   - Verify hostname: kronscheduler.lesnewski.local
   - Check SSH credentials

2. **Email Hub Not Responding**
   - Check N8N webhook: http://10.17.17.32:5678/webhook/email/hub/receive
   - Verify email hub is running
   - Check N8N workflow status

3. **Sources Not SYPHON'ing**
   - Check source configuration: `config/syphon_scheduled_sources.json`
   - Verify sources are enabled
   - Check credentials (Azure Key Vault)

---

## Summary

✅ **SYPHON Scheduled Daemon Complete**

**Features:**
- ✅ Scheduled execution via NAS KronScheduler
- ✅ Internal sources (#internal) - Filesystems
- ✅ External sources (#external) - Email, Financial
- ✅ NAS Email Hub integration
- ✅ N8N workflow integration
- ✅ Configurable intervals
- ✅ Results tracking
- ✅ Logging and monitoring

**Status**: ✅ **READY FOR DEPLOYMENT**

---

**Last Updated**: 2026-01-05  
**Next Action**: Deploy to NAS KronScheduler
