# Operator Idleness Restriction System

## Overview

The Operator Idleness Restriction System prevents AI, JARVIS, and MANUS actions during operator idle periods (10 minutes). This ensures that autonomous systems do not take control when the operator is not actively working.

## Features

- **10-Minute Idle Timeout**: Restricts actions after 10 minutes (600 seconds) of operator inactivity
- **Real-Time Activity Tracking**: Monitors operator activity (keyboard, mouse, voice, chat, etc.)
- **Action Blocking**: Blocks AI, JARVIS, and MANUS actions during idle periods
- **@Ask Chaining Integration**: Prevents @ask chain execution when operator is idle
- **Emergency Override**: Allows emergency actions even during idle periods
- **Background Monitoring**: Continuous monitoring in background thread

## Integration Points

### 1. @Ask Chaining

**File**: `scripts/python/jarvis_execute_ask_chains.py`

- Checks idleness before executing @ask chains
- Blocks chain execution if operator is idle for >10 minutes
- Returns blocked status with idle duration

### 2. @DOIT Execution

**File**: `scripts/python/jarvis_doit_executor.py`

- Checks idleness before @DOIT autonomous execution
- Blocks @DOIT if operator is idle for >10 minutes
- Prevents full autonomy mode during idle periods

### 3. MANUS Actions

**File**: `scripts/python/manus_unified_control.py`

- Checks idleness before executing MANUS control operations
- Blocks MANUS actions if operator is idle for >10 minutes
- Supports emergency override for critical operations

## Usage

### CLI Interface

```bash
# Check current status
python scripts/python/operator_idleness_restriction.py --status

# Record operator activity
python scripts/python/operator_idleness_restriction.py --record keyboard

# Check if action is allowed
python scripts/python/operator_idleness_restriction.py --check ai_action

# Custom timeout (default: 600s = 10 minutes)
python scripts/python/operator_idleness_restriction.py --timeout 300 --status
```

### Programmatic Usage

```python
from scripts.python.operator_idleness_restriction import (
    get_operator_idleness_restriction,
    check_action_allowed,
    record_operator_activity
)

# Get restriction instance
restriction = get_operator_idleness_restriction()

# Record activity
record_operator_activity("keyboard", source="ide")
record_operator_activity("mouse", source="ide")
record_operator_activity("chat", source="cursor")

# Check if action is allowed
if check_action_allowed("ai_action"):
    # Execute AI action
    pass
else:
    # Action blocked - operator is idle
    pass

# Check with emergency override
if check_action_allowed("jarvis_action", emergency=True):
    # Emergency action allowed even if idle
    pass
```

### Integration in Code

```python
from operator_idleness_restriction import get_operator_idleness_restriction

restriction = get_operator_idleness_restriction()

# Before executing action
if not restriction.is_action_allowed("ask_chain_execution"):
    return {
        "success": False,
        "blocked": True,
        "reason": "Operator idle - action restricted"
    }

# Execute action
result = execute_action()
```

## Idleness States

1. **ACTIVE**: Operator is active (activity within last 10 minutes)
   - All actions allowed

2. **IDLE**: Operator approaching idle (80% of timeout elapsed)
   - Actions allowed but monitored
   - Warning logged

3. **RESTRICTED**: Operator idle for >10 minutes
   - Restricted actions blocked
   - Emergency actions still allowed

## Restricted Actions

By default, the following actions are restricted during idle periods:

- `ai_action` - AI actions
- `jarvis_action` - JARVIS actions
- `manus_action` - MANUS actions
- `autonomous_execution` - Autonomous execution
- `ask_chain_execution` - @ask chain execution

## Configuration

**File**: `scripts/python/operator_idleness_restriction.py`

```python
IdlenessRestriction(
    idle_timeout_seconds=600,  # 10 minutes
    restriction_enabled=True,
    restricted_actions=[
        "ai_action",
        "jarvis_action",
        "manus_action",
        "autonomous_execution",
        "ask_chain_execution"
    ],
    allow_emergency=True  # Allow emergency actions
)
```

## Activity Tracking

The system tracks various activity types:

- **keyboard** - Keyboard input
- **mouse** - Mouse movement/clicks
- **voice** - Voice commands
- **chat** - Chat messages
- **command_palette** - Command palette usage
- **file_system** - File operations
- **git** - Git operations
- **terminal** - Terminal commands

## State Persistence

- State is saved to: `data/operator_idleness/idleness_state.json`
- Last activity timestamp is persisted
- State is restored on system restart

## Monitoring

- Background monitoring thread checks idleness every 10 seconds
- State is automatically updated based on activity
- Logs warnings when actions are blocked

## Emergency Override

Emergency actions can override idleness restrictions:

```python
# Emergency action (always allowed)
restriction.is_action_allowed("manus_action", emergency=True)

# Or in operation parameters
operation.parameters['emergency'] = True
```

## Example Output

```
================================================================================
OPERATOR IDLENESS RESTRICTION STATUS
================================================================================
State: restricted
Idle Duration: 650s
Last Activity: 2026-01-02T06:32:00
Restriction Enabled: True
Idle Timeout: 600s
Actions Blocked: True
================================================================================
```

## Benefits

1. **Prevents Unwanted Automation**: Stops AI/JARVIS/MANUS from taking control when operator is away
2. **10-Minute Grace Period**: Allows natural workflow pauses without restriction
3. **Emergency Override**: Critical actions can still execute when needed
4. **Full Integration**: Works with @ask chaining, @DOIT, and MANUS systems
5. **Real-Time Monitoring**: Continuous tracking ensures accurate state

## Tags

#@OP #IDLENESS #RESTRICTION #ASKCHAINING @JARVIS @MANUS @DOIT
