# Operator Breather Protection System

## Overview

The Operator Breather Protection System ensures **@OP gets at least a 10-minute breather** before any AI/JARVIS/MANUS restrictions apply. This prevents the system from being too aggressive and gives the operator time to step away without immediate restrictions.

## Philosophy

**"AT LEAST FOR TEN MIN BREATHER FOR THE @OP"**

The operator should have a minimum 10-minute break before the system starts restricting actions. This ensures:
- Operator can step away without immediate restrictions
- System doesn't become too aggressive
- Natural workflow isn't interrupted
- Operator has time to return before restrictions kick in

## Configuration

### Minimum Breather Time
- **Default**: 600 seconds (10 minutes)
- **Minimum**: 600 seconds (10 minutes) - enforced
- **Configurable**: Can be increased, but never decreased below 10 minutes

### Current Settings
- **Idle Timeout**: 600 seconds (10 minutes)
- **Restriction Enabled**: True
- **Minimum Breather**: 600 seconds (10 minutes) - **ENFORCED**

## How It Works

1. **Operator Activity Tracking**: System tracks all operator activity (keyboard, mouse, voice, chat)
2. **10-Minute Breather**: Operator gets full 10 minutes of idle time before restrictions
3. **Restriction Activation**: After 10 minutes of idleness, restrictions activate
4. **Action Blocking**: AI/JARVIS/MANUS actions are blocked during restricted state
5. **Activity Resumption**: When operator becomes active again, restrictions are lifted immediately

## Protected Actions

When operator is idle for >10 minutes, these actions are blocked:
- `ai_action` - AI actions
- `jarvis_action` - JARVIS actions
- `manus_action` - MANUS control operations
- `autonomous_execution` - @DOIT autonomous execution
- `ask_chain_execution` - @ask chain execution

## Integration

### With @DOIT
- Blocks @DOIT execution if operator idle >10 minutes
- Applies -500 XP (CRITICAL) penalty for violations
- Requires operator activity to resume

### With @ASK Chains
- Blocks @ask chain execution if operator idle >10 minutes
- Applies -100 XP (MAJOR) penalty for violations
- Requires operator activity to resume

### With MANUS
- Blocks MANUS operations if operator idle >10 minutes
- Applies -50 XP (MODERATE) penalty for violations
- Requires operator activity to resume

## Status Display

```
================================================================================
OPERATOR IDLENESS RESTRICTION STATUS
================================================================================
State: restricted
Idle Duration: 1846s
Last Activity: 2026-01-02T06:42:44.911928
Restriction Enabled: True
Idle Timeout: 600s (10.0 minutes)
Actions Blocked: True
🛡️  @OP had 10.0-minute breather - restrictions now active
================================================================================
```

## Usage

```bash
# Check status
python scripts/python/operator_idleness_restriction.py --status

# Record activity (resets idle timer)
python scripts/python/operator_idleness_restriction.py --activity keyboard

# Get time until restriction
python scripts/python/operator_idleness_restriction.py --time-until-restriction
```

## Enforcement

The system **enforces** the minimum 10-minute breather:
- If timeout is set to less than 10 minutes, it's automatically increased to 10 minutes
- System logs a warning if timeout is too short
- Minimum breather is always respected

## Benefits

1. **Operator Freedom**: Operator can step away without immediate restrictions
2. **Natural Workflow**: Doesn't interrupt natural breaks
3. **System Safety**: Still provides protection after reasonable idle time
4. **Flexibility**: Can be increased if needed, but never decreased below 10 minutes

## Tags

@OP #BREATHER #PROTECTION #10_MINUTES #IDLENESS #RESTRICTION #SAFETY
