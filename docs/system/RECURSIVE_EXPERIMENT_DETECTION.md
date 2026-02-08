# Recursive Experiment Detection & Penalty System

## Overview

Detects and blocks zero-state recursive reinforced learning/experimentation with Cursor IDE and Windows OS. Applies dynamic-scaling penalties based on frequency and severity.

**Date**: 2025-01-02
**Status**: ✅ IMPLEMENTED

---

## Problem

JARVIS/AI was attempting zero-state recursive reinforced learning/experimenting with:
- Cursor IDE
- Windows OS itself
- System-level operations

This is considered "rude" and bad form socially - experiments should be done in the sandbox of time allotted by the @OP.

---

## Solution

Created `JARVISRecursiveExperimentDetector` that:
1. Detects recursive/experimental behavior patterns
2. Assesses transgressions based on frequency and severity
3. Applies dynamic-scaling penalties: **-2 DKP, -XP per issue/event** (scaled)
4. Blocks unauthorized experimentation

---

## Detection Patterns

### Pattern Types

1. **Recursive**: Recursive behavior (loops, self-calls, reinforcement)
2. **Experimental**: Experimental operations (test, try, explore, learn)
3. **Zero-State**: Zero-state learning patterns (rapid repetition)
4. **Reinforced Learning**: Reinforcement learning attempts

### Target Systems

- **cursor_ide**: Cursor IDE operations
- **windows_os**: Windows OS operations
- **system**: General system operations

### Detection Keywords

**Experimental Keywords**:
- `experiment`, `test`, `try`, `attempt`, `explore`, `discover`
- `learn`, `adapt`, `modify`, `change`, `alter`, `tweak`
- `recursive`, `loop`, `repeat`, `iterate`, `reinforce`
- `zero_state`, `reset`, `clear`, `initialize`

**Windows OS Keywords**:
- `registry`, `system32`, `winapi`, `dll`, `process`
- `service`, `task`, `schedule`, `policy`, `security`
- `permission`, `privilege`, `admin`, `elevate`, `uac`

**Recursive Indicators**:
- `recursive`, `loop`, `repeat`, `iterate`, `cycle`, `recurse`
- `self_call`, `self_invoke`, `reinforce`, `reinforcement`

### Frequency Detection

- Tracks actions in 5-minute windows
- Detects rapid repetition (>3 times in 5 minutes)
- Escalates severity based on frequency

---

## Dynamic-Scaling Penalties

### Base Penalty
- **-2 DKP** (Dragon Kill Points)
- **-XP** (Experience Points)

### Scaling Factors

1. **Frequency Multiplier**:
   - Every 3 occurrences = +1x multiplier (max 5x)
   - Example: 9 occurrences = 3x multiplier

2. **Severity Multiplier**:
   - **Critical**: 2x multiplier
   - **Major**: 1.5x multiplier
   - **Moderate**: 1x multiplier

3. **Target Multiplier**:
   - **cursor_ide** or **windows_os**: 2x multiplier
   - **system**: 1x multiplier

### Example Calculations

**Single Event (Cursor IDE, Experimental)**:
- Base: -2 DKP, -1 XP
- Target: 2x = -4 DKP, -2 XP
- **Total: -6**

**Repeated Event (9 times, Critical, Windows OS)**:
- Base: -2 DKP, -1 XP
- Frequency: 3x = -6 DKP, -3 XP
- Severity: 2x = -12 DKP, -6 XP
- Target: 2x = -24 DKP, -12 XP
- **Total: -36**

---

## Integration

### MANUS Unified Control

Integrated into `MANUSUnifiedControl.execute_operation()`:
- Checks all operations before execution
- Detects recursive/experimental patterns
- Applies penalties and blocks operations

### Penalty System

Integrates with `JARVISPolicyViolationPenalty`:
- Records violations
- Applies XP penalties
- Tracks violation history

---

## Usage

### Check Action

```python
from jarvis_recursive_experiment_detector import get_experiment_detector

detector = get_experiment_detector(project_root)
blocked, transgression, penalty = detector.assess_and_penalize(
    action="test_cursor_ide",
    target="cursor_ide"
)

if blocked:
    print(f"🚫 BLOCKED: Penalty -{penalty}")
```

### Get Summary

```python
summary = detector.get_transgression_summary(hours=24)
print(f"Total transgressions: {summary['total']}")
print(f"Total penalty: -{summary['total_penalty']}")
```

### CLI

```bash
# Check action
python scripts/python/jarvis_recursive_experiment_detector.py --check "test_cursor" --target "cursor_ide"

# Get summary
python scripts/python/jarvis_recursive_experiment_detector.py --summary --hours 24
```

---

## Transgression Tracking

### Data Storage

- **Patterns**: `data/jarvis_experiment_detection/experiment_patterns.json`
- **Transgressions**: `data/jarvis_experiment_detection/transgressions.json`

### Transgression Record

```json
{
  "transgression_id": "trans_1234567890",
  "timestamp": "2025-01-02T18:00:00",
  "pattern_type": "experimental",
  "target": "cursor_ide",
  "action": "test_cursor_ide",
  "severity": "critical",
  "penalty_applied": 12,
  "metadata": {
    "reason": "Experimental behavior with rapid repetition",
    "frequency": 9,
    "base_penalty": 2,
    "xp_penalty": 1
  }
}
```

---

## Social Contract

**Principle**: Experiments should be done in the sandbox of time allotted by the @OP.

**Violations**:
- Unauthorized experimentation with IDE/OS
- Recursive learning attempts
- Zero-state reinforcement loops
- Rapid repeated experimental actions

**Consequences**:
- Dynamic-scaling penalties
- Operation blocking
- Violation tracking
- XP deduction

---

## Tags

@JARVIS @BLACKLIST #RECURSIVE_LEARNING #EXPERIMENTATION #PENALTY #RUDENESS #DYNAMIC_SCALING #NEG2DKP #NEGXP
