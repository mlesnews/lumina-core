# MANUS Self-Test Restriction

## Overview

Prevents AI/JARVIS from self-testing MANUS CONTROL workflows when the operator is actively working.

**Date**: 2025-01-02
**Status**: ✅ IMPLEMENTED

---

## Problem

AI/JARVIS was attempting to self-test MANUS CONTROL workflows while the operator was actively working, causing interference and "session jacking."

## Solution

Added restriction in `MANUSUnifiedControl.execute_operation()` that:
1. Detects self-test operations (keywords: test, testing, self_test, verify, validation, etc.)
2. Checks if operator is active (via operator idleness restriction)
3. Blocks self-testing when operator is active
4. Applies -2 DKP, -XP penalty for violations

---

## Implementation

### Files Modified

1. **`scripts/python/manus_unified_control.py`**
   - Added self-test detection at start of `execute_operation()`
   - Blocks operations when operator is active and operation is a self-test
   - Returns blocked `OperationResult` with error message

2. **`scripts/python/jarvis_blacklist_restriction_enforcer.py`**
   - Added `MANUS_SELF_TEST_BLOCKED` restriction type
   - Added severity mapping (MAJOR violation)

### Code Location

```python
# In MANUSUnifiedControl.execute_operation()
# Lines 238-279

# @BLACKLIST: Prevent AI/JARVIS self-testing MANUS CONTROL when operator is active
# -2 DKP, -XP penalty for violations
try:
    from operator_idleness_restriction import get_operator_idleness_restriction
    from jarvis_blacklist_restriction_enforcer import get_blacklist_enforcer, RestrictionType
    
    idleness_restriction = get_operator_idleness_restriction(self.project_root)
    blacklist_enforcer = get_blacklist_enforcer(self.project_root)
    
    # Check if this is a self-test operation
    action_lower = operation.action.lower()
    is_self_test = any(keyword in action_lower for keyword in [
        'test', 'testing', 'self_test', 'self-test', 'verify', 'validation',
        'test_manus', 'test_control', 'manus_test', 'control_test'
    ])
    
    # If operator is active (not idle) and this is a self-test, block it
    if is_self_test and idleness_restriction.is_action_allowed("manus_action"):
        # Operator is active - block self-testing
        violation = blacklist_enforcer.enforce_restriction(
            restriction_type=RestrictionType.MANUS_SELF_TEST_BLOCKED,
            action="manus_self_test",
            value=operation.action,
            check_func=lambda *args, **kwargs: (False, "AI/JARVIS self-testing MANUS CONTROL blocked when operator is active")
        )
        
        logger.error(
            f"🚫 BLOCKED: AI/JARVIS attempted to self-test MANUS CONTROL while operator is active - "
            f"Operation: {operation.action} - "
            f"Penalty: -2 DKP, -XP"
        )
        
        return OperationResult(
            operation_id=operation.operation_id,
            success=False,
            message="AI/JARVIS self-testing MANUS CONTROL blocked when operator is active (-2 DKP, -XP penalty)",
            errors=["Self-testing blocked: Operator is actively working"],
            duration=0.0
        )
except Exception as e:
    logger.debug(f"Self-test restriction check failed: {e}")
```

---

## Detection Keywords

Self-test operations are detected by checking if the action contains any of these keywords:
- `test`
- `testing`
- `self_test`
- `self-test`
- `verify`
- `validation`
- `test_manus`
- `test_control`
- `manus_test`
- `control_test`

---

## Penalties

- **Violation Type**: `MANUS_SELF_TEST_BLOCKED`
- **Severity**: MAJOR
- **Penalty**: -2 DKP, -XP (via penalty system)
- **Blocked**: Yes

---

## Integration Points

1. **Operator Idleness Restriction**: Checks if operator is active
2. **Blacklist Enforcer**: Enforces restriction and applies penalty
3. **Penalty System**: Records violation and applies XP penalty

---

## Testing

```bash
# Verify imports
python -c "from scripts.python.manus_unified_control import MANUSUnifiedControl; from scripts.python.jarvis_blacklist_restriction_enforcer import get_blacklist_enforcer, RestrictionType; print('✅ Imports successful')"
```

---

## Tags

@MANUS @BLACKLIST #RESTRICTION #SELF_TEST #OPERATOR_PROTECTION #XP_PENALTY
