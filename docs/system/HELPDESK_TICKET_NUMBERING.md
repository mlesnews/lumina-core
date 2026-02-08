# Helpdesk Ticket Numbering Standard

**Date**: 2025-01-24  
**Status**: ✅ **STANDARDIZED**  
**Tag**: @helpdesk @C3PO @JARVIS

---

## Ticket Number Format

**ALL helpdesk tickets/CRs/tasks use the same 9-digit format with prefix:**

### Format: `PREFIX + 9 digits`

Examples:
- `PM000000001` - Problem Management ticket #1
- `CR000000001` - Change Request #1
- `T000000001` - Task #1

---

## Prefixes

| Prefix | Type | Full Name | Example |
|--------|------|-----------|---------|
| `PM` | Problem Management | Problem/Incident tickets | `PM000000001` |
| `CR` | Change Request | Change requests | `CR000000001` |
| `T` | Task | Task tickets | `T000000001` |

---

## Numbering Rules

1. **Consistent Format**: All ticket numbers use exactly 9 digits with leading zeros
2. **Sequential**: Numbers are sequential within each type
3. **Prefix Determines Type**: The prefix identifies the ticket type
4. **No Gaps**: Numbers are assigned sequentially (no skipping)

---

## Examples

### Problem Management Tickets
```
PM000000001
PM000000002
PM000000003
...
PM000003056
```

### Change Requests
```
CR000000001
CR000000002
CR000000003
...
CR000000018
```

### Tasks
```
T000000001
T000000002
T000000003
```

---

## File Naming

Ticket files are named using the ticket number:
- `PM000000001.json` - Problem Management ticket #1
- `CR000000001.json` - Change Request #1
- `T000000001.json` - Task #1

---

## Counter Management

**File**: `data/pr_tickets/ticket_counter.json`

```json
{
  "ticket_counter": 3057,
  "change_request_counter": 18,
  "task_counter": 1
}
```

Each type maintains its own counter.

---

## Normalization

All existing tickets have been normalized to use the 9-digit format.

**Script**: `scripts/python/normalize_ticket_numbers.py`

**Status**: ✅ **RETROACTIVELY APPLIED**

---

## Implementation

### Creating Tickets

Use the standardized format in all ticket creation scripts:

```python
# Problem Management ticket
ticket_number = f"PM{ticket_counter:09d}"  # PM000000001

# Change Request
cr_number = f"CR{cr_counter:09d}"  # CR000000001

# Task
task_number = f"T{task_counter:09d}"  # T000000001
```

---

## References

- **Ticket Counter**: `data/pr_tickets/ticket_counter.json`
- **Normalization Script**: `scripts/python/normalize_ticket_numbers.py`
- **Change Request Creator**: `scripts/python/create_change_requests.py`

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **STANDARDIZED**  
**Maintained By**: @helpdesk @C3PO