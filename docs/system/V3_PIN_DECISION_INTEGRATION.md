# @v3 Pin Decision System Integration

**Date:** 2026-01-14  
**Status:** ✅ **IMPLEMENTED**  
**Integration:** @v3 Judicial Approval Framework + Pin/Unpin Operations

---

## Overview

All pin/unpin operations now require judicial approval through the @v3 Judicial Approval Framework. The system uses #syphon for finding and analyzing pin-related code, and integrates with the existing auto-pin/unpin/archive system.

## Implementation

### 1. V3 Pin Decision System (`scripts/python/v3_pin_decision_system.py`)

**Key Features:**
- ✅ All pin operations require judicial approval
- ✅ All unpin operations require judicial approval
- ✅ All archive operations require judicial approval
- ✅ Uses #syphon for finding pin-related code
- ✅ Integrates with #decisioning process
- ✅ Creates change control tickets for each operation
- ✅ Comprehensive audit trail

**Main Classes:**
- `V3PinDecisionSystem`: Main decision system for pin operations
- `PinOperationTicket`: Creates change control tickets for pin/unpin operations

### 2. Integration with Auto Pin System

**Modified:** `scripts/python/auto_pin_unpin_autoarchive_system.py`

The `evaluate_session()` method now:
1. Attempts to use V3 judicial approval first
2. Falls back to original logic if V3 not available
3. Returns V3 ticket ID and status in decision results

### 3. #Syphon Integration

The system uses #syphon (grep) to find all pin-related operations:
- `.pin_file(`
- `.unpin_file(`
- `is_pinned`
- `pin_reason`
- `auto.*pin`
- `pin.*manager`

## Usage

### Python API

```python
from v3_pin_decision_system import V3PinDecisionSystem

system = V3PinDecisionSystem()

# Pin decision with judicial approval
pin_decision = system.should_pin_file(
    file_path="test_file.py",
    reason="High line count requires pinning",
    context={
        "line_count": 50000,
        "age_hours": 12,
        "crashes": 0
    }
)

if pin_decision["should_pin"]:
    print(f"✅ Approved to pin: {pin_decision['rationale']}")
    print(f"Ticket ID: {pin_decision['ticket_id']}")
else:
    print(f"❌ Not approved: {pin_decision['rationale']}")

# Unpin decision with judicial approval
unpin_decision = system.should_unpin_file(
    file_path="test_file.py",
    reason="File completed, ready to unpin",
    context={
        "line_count": 150000,
        "age_hours": 30,
        "crashes": 3,
        "completed": True
    }
)
```

### Automatic Integration

The auto-pin system automatically uses V3 approval:

```python
from auto_pin_unpin_autoarchive_system import AutoPinUnpinAutoArchive

system = AutoPinUnpinAutoArchive(project_root)

# This now uses V3 judicial approval internally
decision = system.evaluate_session({
    "file_path": "session_file.py",
    "line_count": 150000,
    "crashes": 3,
    "age_hours": 30
})

# Decision includes V3 ticket information
print(f"V3 Status: {decision.get('v3_status')}")
print(f"V3 Ticket ID: {decision.get('v3_ticket_id')}")
```

## Decision Criteria

### Pin Operations
- **Priority:** Based on context (crashes, line_count)
- **Environment:** DEV (pin operations are low-risk)
- **Approval:** Typically auto-approved for low-risk pins

### Unpin Operations
- **Priority:** Based on context (crashes, line_count, age)
- **Environment:** DEV
- **Approval:** Requires verification that unpin is safe

### Archive Operations
- **Priority:** Low (unless crashes >= 3)
- **Environment:** DEV
- **Approval:** Requires verification before archiving

## #Syphon Usage

The system uses #syphon to find pin-related code:

```python
from v3_pin_decision_system import syphon_pin_operations

pin_ops = syphon_pin_operations(project_root)
for op in pin_ops:
    print(f"{op['file']}:{op['line']} - {op['content']}")
```

## Audit Trail

All pin/unpin/archive decisions are logged with:
- Ticket ID
- Decision status (approved/rejected/conditional)
- Rationale
- Conditions (if conditional)
- Timestamp
- Context information

Log location: `data/v3_verification/pin_decisions.jsonl`

## Benefits

1. **Judicial Oversight:** All pin operations require approval
2. **Audit Trail:** Complete record of all pin decisions
3. **Consistency:** Same approval process for all operations
4. **Transparency:** Clear rationale for each decision
5. **Integration:** Works seamlessly with existing systems
6. **#Syphon Integration:** Easy to find and analyze pin-related code

## Example Decision Flow

```
Pin Request
    ↓
Create Change Control Ticket
    ↓
V3 Judicial Approval (3 tiers)
    ↓
#Decisioning Process
    ↓
Approval Decision
    ↓
Execute Pin/Unpin/Archive
    ↓
Log to Audit Trail
```

## Integration Points

1. **Auto Pin System:** `auto_pin_unpin_autoarchive_system.py`
2. **File Pin Manager:** `file_pin_manager.py` (can be enhanced)
3. **V3 Framework:** `lumina_core/workflow/v3_judicial_approval.py`
4. **Decisioning:** `universal_decision_tree.py`
5. **#Syphon:** Built-in grep/search functionality

## Next Steps

1. ✅ Integrate with file_pin_manager.py
2. ⏳ Add webhook notifications for pin decisions
3. ⏳ Create dashboard for pin decision tracking
4. ⏳ Add machine learning for pin pattern recognition

## Tags

**Tags:** #V3 #JUDICIAL_APPROVAL #PIN #UNPIN #SYPHON #DECISIONING 
         #AUTOARCHIVE #AUTOMATION @JARVIS @LUMINA

---

**Status:** ✅ **INTEGRATION COMPLETE - ALL PIN OPERATIONS USE V3 JUDICIAL APPROVAL**
