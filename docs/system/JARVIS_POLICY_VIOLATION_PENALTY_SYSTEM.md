# JARVIS Policy Violation Penalty System

## Overview

The JARVIS Policy Violation Penalty System enforces company policy compliance by tracking violations and applying penalties (-xp) to @JARVIS. **"Actions have repercussions!"** - Every policy violation has real consequences.

## Features

- **XP Penalty System**: Tracks JARVIS experience points (XP) and applies penalties for violations
- **Violation Tracking**: Records all policy violations with timestamps, severity, and metadata
- **Automatic Enforcement**: Integrated with idleness restrictions, @ask chaining, @DOIT, and MANUS
- **Severity Levels**: Minor (-10 XP), Moderate (-50 XP), Major (-100 XP), Critical (-500 XP)
- **Violation History**: Maintains complete violation history for analysis

## Policy Types

1. **IDLENESS_RESTRICTION**: Violations of operator idleness restrictions
2. **AUTONOMOUS_EXECUTION**: Unauthorized autonomous execution
3. **ASK_CHAIN_VIOLATION**: @ask chain execution violations
4. **MANUS_ACTION_VIOLATION**: MANUS action violations
5. **DOIT_VIOLATION**: @DOIT execution violations
6. **COMPANY_POLICY**: General company policy violations

## Penalty Amounts

| Severity | XP Penalty | Typical Use |
|----------|------------|-------------|
| Minor | -10 XP | Small policy infractions |
| Moderate | -50 XP | Standard violations (default) |
| Major | -100 XP | Significant policy violations |
| Critical | -500 XP | Critical violations (e.g., @DOIT during idle) |

## Integration Points

### 1. @Ask Chain Execution

**File**: `scripts/python/jarvis_execute_ask_chains.py`

- Checks idleness before executing @ask chains
- Records violation and applies -100 XP penalty if violated
- Blocks execution and returns violation status

### 2. @DOIT Execution

**File**: `scripts/python/jarvis_doit_executor.py`

- Checks idleness before @DOIT autonomous execution
- Records violation and applies -500 XP penalty (CRITICAL) if violated
- Blocks execution and returns violation status

### 3. MANUS Actions

**File**: `scripts/python/manus_unified_control.py`

- Checks idleness before executing MANUS control operations
- Records violation and applies -50 XP penalty if violated
- Blocks execution and returns violation status
- Emergency actions bypass penalty (but still logged)

## Usage

### CLI Interface

```bash
# Check XP status
python scripts/python/jarvis_policy_violation_penalty.py --status

# View violation summary (last 24 hours)
python scripts/python/jarvis_policy_violation_penalty.py --summary 24

# Record a violation manually
python scripts/python/jarvis_policy_violation_penalty.py --record idleness_restriction "test_action" "Test violation" moderate
```

### Programmatic Usage

```python
from scripts.python.jarvis_policy_violation_penalty import (
    get_penalty_system,
    PolicyType,
    ViolationSeverity,
    record_violation
)

# Get penalty system
penalty_system = get_penalty_system()

# Record violation
violation = record_violation(
    policy_type=PolicyType.IDLENESS_RESTRICTION,
    action="ask_chain_execution",
    description="Attempted @ask chain execution while operator idle",
    severity=ViolationSeverity.MAJOR,
    blocked=True
)

# Check XP status
status = penalty_system.get_xp_status()
print(f"Current XP: {status['current_xp']}")
print(f"Violations: {status['violations_count']}")

# Get violation summary
summary = penalty_system.get_violation_summary(hours=24)
print(f"Total violations: {summary['total_violations']}")
print(f"Total penalty XP: {summary['total_penalty_xp']}")
```

### Integration in Code

```python
from jarvis_policy_violation_penalty import get_penalty_system, PolicyType, ViolationSeverity

penalty_system = get_penalty_system(project_root)

# Check and enforce policy
allowed, violation = penalty_system.check_and_enforce(
    policy_type=PolicyType.IDLENESS_RESTRICTION,
    action="ask_chain_execution",
    check_func=idleness_restriction.is_action_allowed,
    "ask_chain_execution"
)

if not allowed:
    # Violation occurred - action blocked, penalty applied
    print(f"Violation: {violation.violation_id}")
    print(f"Penalty: {violation.xp_penalty} XP")
    return {"blocked": True, "violation": True}
```

## XP Tracking

The system tracks:
- **Current XP**: Current experience points (starts at 0, can go negative)
- **Total Earned**: Total XP earned (not yet implemented)
- **Total Penalties**: Total XP lost to penalties
- **Violations Count**: Total number of violations
- **Violation History**: List of violation IDs

## Data Storage

- **XP Data**: `data/jarvis_penalties/jarvis_xp.json`
- **Violations**: `data/jarvis_penalties/violations.json`
- **History**: Last 1000 violations kept in memory, all saved to file

## Example Output

```
================================================================================
JARVIS XP STATUS
================================================================================
Current XP: -150
Total Earned: 0
Total Penalties: 150
Violations Count: 2
Recent Violations (1h): 2
================================================================================

================================================================================
VIOLATION SUMMARY (Last 24 hours)
================================================================================
Total Violations: 2
Total Penalty XP: 150

By Severity: {'major': 1, 'critical': 1}
By Policy: {'idleness_restriction': 1, 'doit_violation': 1}

Recent Violations:
  - ask_chain_execution: Attempted @ask chain execution while operator idle for 650s (threshold: 600s) (-100 XP)
  - autonomous_execution: Attempted @DOIT execution while operator idle for 720s (threshold: 600s) (-500 XP)
================================================================================
```

## Enforcement

The system **ENFORCES** policies by:

1. **Blocking Actions**: Violations result in blocked actions (not just warnings)
2. **Applying Penalties**: XP penalties are automatically applied
3. **Logging Violations**: All violations are logged with full details
4. **Tracking History**: Complete violation history maintained
5. **Real Consequences**: "Actions have repercussions!" - Every violation costs XP

## Benefits

1. **Policy Compliance**: Ensures JARVIS follows company policies
2. **Accountability**: Tracks all violations with full audit trail
3. **Consequences**: Real penalties (-xp) for violations
4. **Transparency**: Full visibility into violations and penalties
5. **Deterrence**: Penalties discourage policy violations

## Tags

@JARVIS @PENALTY #POLICY #VIOLATION #XP #REPERCUSSIONS #IDLENESS #RESTRICTION
