# Heartbeat Monitor - JARVIS Master Chat to Sub-Agent Chats

**Date**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

---

## Overview

**Heartbeat monitoring from JARVIS master chat to sub-agent chats with:**
1. ✅ Follow through
2. ✅ Follow-up confirmation
3. ✅ Workflow checks and balances

---

## Features

### 1. Heartbeat Monitoring

**Continuous heartbeat from master to sub-agent chats:**
- Sends heartbeat every 30 seconds (configurable)
- Monitors response time
- Tracks heartbeat status (ALIVE, RESPONDING, NO_RESPONSE, STALE, DEAD)
- Detects unresponsive sub-agent chats

### 2. Follow Through

**Ensures heartbeats are followed through:**
- Tracks heartbeat responses
- Monitors follow-up requirements
- Handles timeout scenarios
- Takes recovery actions when needed

### 3. Follow-Up Confirmation

**Confirms follow-up actions:**
- Pending follow-ups tracked
- Confirmation status monitored
- Timeout handling
- Failed follow-up detection

### 4. Workflow Checks and Balances

**Performs checks and balances on workflows:**
- Progress checks
- Completion checks
- Error checks
- Resource checks
- Balance actions when needed

---

## Heartbeat Status

### Status Types

- **ALIVE** - Sub-agent chat responding normally
- **RESPONDING** - Sub-agent chat responding but slow
- **NO_RESPONSE** - No response to heartbeat
- **STALE** - No response for > 60 seconds
- **DEAD** - No response for > 5 minutes

### Thresholds

- **Response Timeout**: 10 seconds
- **Stale Threshold**: 60 seconds
- **Dead Threshold**: 300 seconds (5 minutes)
- **Heartbeat Interval**: 30 seconds

---

## Follow-Up Process

### Follow-Up Required

Follow-up is required when:
- Heartbeat status is NO_RESPONSE
- Heartbeat status is STALE
- Heartbeat status is DEAD

### Follow-Up Status

- **PENDING** - Follow-up scheduled
- **CONFIRMED** - Follow-up confirmed
- **FAILED** - Follow-up failed
- **TIMEOUT** - Follow-up timed out

### Follow-Up Actions

**When follow-up timeout:**
- DEAD status → Recovery action
- STALE status → Investigation
- NO_RESPONSE → Retry heartbeat

---

## Workflow Checks and Balances

### Check Types

1. **Progress Check**
   - Verifies workflow is making progress
   - Checks completion rate
   - Identifies stalled workflows
   - Balance action: Increase progress rate

2. **Completion Check**
   - Verifies workflow completion
   - Checks workflow_completed flag
   - Identifies incomplete workflows
   - Balance action: Complete workflow

3. **Error Check**
   - Checks for workflow errors
   - Monitors error rate
   - Identifies error patterns
   - Balance action: Fix errors

4. **Resource Check**
   - Checks resource availability
   - Monitors resource usage
   - Identifies resource constraints
   - Balance action: Allocate resources

### Check Status

- **passed** - Check passed
- **warning** - Check warning (needs attention)
- **failed** - Check failed (needs action)
- **pending** - Check pending

---

## Usage

### Start Monitoring

```python
from heartbeat_monitor import HeartbeatMonitor

monitor = HeartbeatMonitor()

# Start monitoring (runs in background)
monitor.start_monitoring()
```

### Send Heartbeat Manually

```python
heartbeat = monitor.send_heartbeat(
    master_session_id="master_123",
    sub_agent_chat_id="chat_456",
    workflow_status="in_progress"
)

print(f"Status: {heartbeat.status.value}")
print(f"Response Time: {heartbeat.response_time_ms}ms")
print(f"Follow-up Required: {heartbeat.follow_up_required}")
```

### Follow-Up Confirmation

```python
# Confirm follow-up
confirmed = monitor.follow_up_confirmation(
    heartbeat_id="heartbeat_123",
    confirmed=True
)
```

### Workflow Check and Balance

```python
# Check workflow progress
check = monitor.workflow_check_balance(
    sub_agent_chat_id="chat_456",
    workflow_id="workflow_789",
    check_type="progress"
)

print(f"Status: {check.status}")
print(f"Balance Action: {check.balance_action}")
```

### Get Sub-Agent Status

```python
status = monitor.get_sub_agent_status("chat_456")

print(f"Status: {status['status']}")
print(f"Last Heartbeat: {status['last_heartbeat']}")
print(f"Response Time: {status['response_time_ms']}ms")
```

---

## Integration

### With Master Workflow Orchestrator

**Automatically integrated:**
- Heartbeat monitor starts when orchestrator initializes
- Monitors all sub-agent chats
- Performs workflow checks automatically
- Handles follow-ups automatically

### With Sub-Ask Manager

**Uses sub-ask manager to:**
- Get list of sub-agent chats
- Check chat session status
- Verify workflow completion
- Track progress

---

## Monitoring Loop

**Background monitoring loop:**
1. Get master session ID
2. Get all active sub-agent chats
3. Send heartbeat to each chat
4. Perform workflow checks (if ALIVE)
5. Handle follow-ups (if needed)
6. Wait for heartbeat interval
7. Repeat

---

## Data Storage

**Files:**
- `data/heartbeat_monitor/heartbeats.jsonl` - Heartbeat log
- `data/heartbeat_monitor/workflow_checks.jsonl` - Workflow checks log
- `data/heartbeat_monitor/monitor_state.json` - Monitor state

---

## Status

✅ **FULLY OPERATIONAL**

- ✅ Heartbeat monitoring (master to sub-agent chats)
- ✅ Follow through
- ✅ Follow-up confirmation
- ✅ Workflow checks and balances
- ✅ Automatic monitoring loop
- ✅ Recovery actions
- ✅ Integration with master orchestrator

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **COMPLETE**

