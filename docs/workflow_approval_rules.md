# Workflow Approval Rules

## Core Approval Rule

**Rule**: `#decisioning + #troubleshooting = approval for @cr @helpdesk @workflows`

### Definition

When both **#decisioning** and **#troubleshooting** capabilities are present and active, this constitutes automatic approval for:

- **@cr** (Code Review)
- **@helpdesk** (Helpdesk Operations)
- **@workflows** (Workflow Execution)

### Rationale

1. **#decisioning**: Provides decision-making capability and analysis
2. **#troubleshooting**: Provides diagnostic and problem-solving capability
3. **Combined**: These two capabilities together provide sufficient context and analysis to proceed with code review, helpdesk operations, and workflow execution without additional approval

### Implementation

This rule should be checked before:
- Executing workflows
- Performing code reviews
- Initiating helpdesk operations
- Escalating to JARVIS

### Workflow Integration

```python
def has_approval_for_operation(operation_type: str) -> bool:
    """
    Check if approval exists for operation based on decisioning + troubleshooting rule.
    
    Args:
        operation_type: One of '@cr', '@helpdesk', '@workflows'
    
    Returns:
        True if approval exists (decisioning + troubleshooting active)
    """
    decisioning_active = check_decisioning_capability()
    troubleshooting_active = check_troubleshooting_capability()
    
    if operation_type in ['@cr', '@helpdesk', '@workflows']:
        return decisioning_active and troubleshooting_active
    
    return False
```

### Tags and Markers

- **#decisioning**: Decision-making and analysis capability
- **#troubleshooting**: Diagnostic and problem-solving capability
- **@cr**: Code review operations
- **@helpdesk**: Helpdesk operations (C-3PO coordination)
- **@workflows**: Workflow execution

### Examples

#### Example 1: Workflow Execution
```
User Request: "Execute workflow X"
System Check:
  ✅ #decisioning: Active (diagnostics module available)
  ✅ #troubleshooting: Active (troubleshooter available)
Result: APPROVED - Proceed with workflow execution
```

#### Example 2: Code Review
```
User Request: "Review code changes"
System Check:
  ✅ #decisioning: Active
  ✅ #troubleshooting: Active
Result: APPROVED - Proceed with code review
```

#### Example 3: Helpdesk Operation
```
User Request: "Route to @helpdesk"
System Check:
  ✅ #decisioning: Active
  ✅ #troubleshooting: Active
Result: APPROVED - Proceed with helpdesk routing
```

### Integration Points

1. **JARVIS Helpdesk Integration** (`jarvis_helpdesk_integration.py`)
   - Check approval before workflow execution
   - Check approval before escalation

2. **Workflow Executors**
   - Check approval before executing workflows
   - Log approval status

3. **Code Review Systems**
   - Check approval before code review
   - Use decisioning + troubleshooting for analysis

### Status

- **Status**: ✅ **ACTIVE**
- **Date**: 2026-01-02
- **Version**: 1.0
- **Tags**: `#decisioning` `#troubleshooting` `@cr` `@helpdesk` `@workflows` `@jarvis`

---

## Related Systems

- **Diagnostics Module**: Provides troubleshooting capability
- **JARVIS Helpdesk Integration**: Workflow execution and helpdesk routing
- **Droid Actor System**: Helpdesk operations (@helpdesk)
- **@v3 Verification**: Code review and quality assurance

---

## Notes

- This rule applies to all operations that require approval
- Both capabilities must be active (not just available)
- This is an automatic approval - no manual intervention required
- Log all approval checks for audit purposes
