# Environment Policy Rules

**Date**: 2026-01-02  
**Status**: ✅ **IMPLEMENTED**  
**Tags**: @cr @policy @environments @nas @cron @SMART @AI @JARVIS

---

## Overview

Environment-specific policy rules for DEV, STAGING, and PROD environments with two main policies:

1. **Change Request Policy**: Auto-execute or schedule based on duration
2. **AI Exploration Policy**: Limit explorations to idle time only

---

## 1. Change Request Policy (@cr)

### Policy Rule

**If a @cr (change request) to environment-specific policy rules:**
- **Takes < 2 minutes**: Execute immediately
- **Takes >= 2 minutes**: Schedule with NAS cron scheduler (multi-platform)

### Implementation

**File**: `scripts/python/change_request_policy_handler.py`

**Usage**:
```bash
python scripts/python/change_request_policy_handler.py \
  --cr-id CR001 \
  --env DEV \
  --duration 90 \
  --type policy_update \
  --description "Update policy rule X"
```

### Features

- ✅ Automatic duration estimation
- ✅ Immediate execution for fast changes (< 2 minutes)
- ✅ NAS cron scheduling for longer changes (>= 2 minutes)
- ✅ Multi-platform support (Windows, Linux, macOS, Synology DSM, QNAP, Docker)
- ✅ Environment-specific handling (DEV/STAGING/PROD)
- ✅ Fallback scheduling if NAS cron unavailable

### Environment Differences

| Environment | Immediate Threshold | Approval Required | Rollback Plan |
|-------------|---------------------|-------------------|---------------|
| **DEV** | 120 seconds | ❌ No | ❌ No |
| **STAGING** | 120 seconds | ✅ Yes | ❌ No |
| **PROD** | 120 seconds | ✅ Yes | ✅ Yes |

### NAS Cron Integration

- Uses `convert_jarvis_tasks_to_nas_cron.py` for scheduling
- Supports all platforms: Windows, Linux, macOS, Synology DSM, QNAP, Docker
- Priority-based scheduling:
  - **High**: Immediate next slot
  - **Medium**: Within 1 hour
  - **Low**: Within 24 hours

---

## 2. AI Exploration Idle Limiter

### Policy Rule

**Limit AI/JARVIS @SMART explorations to idle time of more than 5 minutes.**

**Restrictions**:
- ❌ Do not interrupt active workflows
- ❌ Do not take over @op @input @manus @controls
- ✅ Only run during idle periods > 5 minutes

### Implementation

**File**: `scripts/python/ai_exploration_idle_limiter.py`

**Usage**:
```bash
# Check if exploration can run
python scripts/python/ai_exploration_idle_limiter.py --check

# Wait for idle time
python scripts/python/ai_exploration_idle_limiter.py --wait --max-wait 3600
```

### Activity Checks

The system monitors:

1. **Workflow Activity**
   - Check interval: 10 seconds
   - Activity timeout: 60 seconds
   - Blocks exploration if workflows active

2. **User Input**
   - Check interval: 5 seconds
   - Input timeout: 30 seconds
   - Blocks exploration if user input detected

3. **MANUS Controls**
   - Check interval: 5 seconds
   - Control timeout: 30 seconds
   - Blocks exploration if MANUS controls active

4. **Operator Controls**
   - Check interval: 5 seconds
   - Control timeout: 30 seconds
   - Blocks exploration if operator controls active

### Allowed During Idle

- ✅ Background analysis
- ✅ Pattern discovery
- ✅ Codebase exploration
- ✅ Optimization suggestions
- ✅ Documentation generation

### Forbidden During Active

- ❌ Workflow interruption
- ❌ Control takeover
- ❌ Input override
- ❌ MANUS control override
- ❌ Operator control override

---

## Configuration

**File**: `config/environment_policy_rules.json`

### Change Request Policy

```json
{
  "change_request_policy": {
    "immediate_execution_threshold_seconds": 120,
    "environments": {
      "DEV": { "immediate_threshold_seconds": 120 },
      "STAGING": { "immediate_threshold_seconds": 120 },
      "PROD": { "immediate_threshold_seconds": 120 }
    }
  }
}
```

### AI Exploration Policy

```json
{
  "ai_exploration_policy": {
    "idle_time_threshold_seconds": 300,
    "restrictions": {
      "min_idle_time_seconds": 300,
      "check_workflow_activity": true,
      "check_user_input": true,
      "check_manus_controls": true,
      "check_operator_controls": true
    }
  }
}
```

---

## Integration Points

### Change Request Handler

- **JARVIS Helpdesk**: Integrates with change request workflow
- **NAS Cron Scheduler**: Schedules long-running changes
- **Environment Config**: Reads environment-specific rules

### AI Exploration Limiter

- **Workflow System**: Monitors workflow activity
- **MANUS System**: Monitors MANUS controls
- **Operator System**: Monitors operator controls
- **User Input System**: Monitors user input

---

## Examples

### Example 1: Quick Policy Update (Immediate)

```bash
python scripts/python/change_request_policy_handler.py \
  --cr-id CR001 \
  --env DEV \
  --duration 30 \
  --type policy_update \
  --description "Update logging level"
```

**Result**: ✅ Executed immediately (30s < 120s threshold)

### Example 2: Complex Policy Change (Scheduled)

```bash
python scripts/python/change_request_policy_handler.py \
  --cr-id CR002 \
  --env PROD \
  --duration 300 \
  --type environment_migration \
  --description "Migrate policy rules to new format"
```

**Result**: 📅 Scheduled with NAS cron (300s >= 120s threshold)

### Example 3: AI Exploration Check

```bash
python scripts/python/ai_exploration_idle_limiter.py --check
```

**Output**:
```
Can Run: ✅ YES
Idle Time: 450 seconds
Idle Sufficient: ✅
Activity Status:
  Workflow: 🟢 Idle
  User Input: 🟢 Idle
  MANUS: 🟢 Idle
  Operator: 🟢 Idle
```

---

## Status

✅ **Change Request Policy**: Implemented and operational  
✅ **AI Exploration Limiter**: Implemented and operational  
✅ **NAS Cron Integration**: Integrated with multi-platform support  
✅ **Environment Configuration**: DEV/STAGING/PROD rules configured

---

## Related Files

- `config/environment_policy_rules.json` - Policy configuration
- `scripts/python/change_request_policy_handler.py` - Change request handler
- `scripts/python/ai_exploration_idle_limiter.py` - AI exploration limiter
- `scripts/python/convert_jarvis_tasks_to_nas_cron.py` - NAS cron scheduler

---

**Created**: 2026-01-02  
**Last Updated**: 2026-01-02
