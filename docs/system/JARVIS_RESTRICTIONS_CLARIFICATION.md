# JARVIS Restrictions Clarification

**Date**: 2026-01-02  
**Status**: ✅ **CLARIFIED**  
**Version**: 1.0.0

---

## ⚠️ IMPORTANT CLARIFICATION

**RESTRICTIONS ARE PLACED ON JARVIS/AI/MANUS, NOT ON THE @OP (OPERATOR)**

When the operator is idle for 10+ minutes, **JARVIS and other AI systems are temporarily restricted** from autonomous actions. **The operator is NEVER restricted** - only JARVIS/AI/MANUS are restricted.

---

## Key Points

1. **Operator is NEVER Restricted**
   - The @OP (operator) can always take actions
   - The @OP is never blocked or restricted
   - Restrictions only apply to autonomous AI systems

2. **JARVIS/AI/MANUS are Temporarily Restricted**
   - When operator is idle for 10+ minutes
   - JARVIS autonomous actions are temporarily blocked
   - AI/MANUS autonomous actions are temporarily blocked
   - This is a **TEMPORARY** restriction, not permanent

3. **Purpose of Restrictions**
   - Prevents autonomous systems from taking control when operator is away
   - Ensures operator has minimum 10-minute breather
   - Protects against unintended autonomous actions during operator absence

4. **Restriction Scope**
   - **Restricted**: JARVIS autonomous actions, AI autonomous actions, MANUS autonomous actions
   - **NOT Restricted**: Operator actions, emergency actions (with override), manual operator commands

---

## System Behavior

### When Operator is Active
- ✅ All JARVIS/AI/MANUS actions allowed
- ✅ Operator actions always allowed
- ✅ No restrictions

### When Operator is Idle (< 10 minutes)
- ✅ All JARVIS/AI/MANUS actions allowed (with monitoring)
- ✅ Operator actions always allowed
- ⚠️  System monitors and warns

### When Operator is Idle (≥ 10 minutes)
- 🚫 JARVIS autonomous actions temporarily restricted
- 🚫 AI autonomous actions temporarily restricted
- 🚫 MANUS autonomous actions temporarily restricted
- ✅ Operator actions always allowed
- ✅ Emergency actions allowed (with override)

---

## Implementation Files

- `scripts/python/operator_idleness_restriction.py` - Core restriction system
- `scripts/python/jarvis_execute_ask_chains.py` - JARVIS @ask chain execution
- `scripts/python/jarvis_doit_executor.py` - JARVIS @DOIT execution
- `scripts/python/manus_unified_control.py` - MANUS control system

---

## Message Format

All restriction messages now include clarification:

```
⚠️  Operator idle for {duration}s - TEMPORARY RESTRICTIONS PLACED ON JARVIS/AI/MANUS (NOT ON @OP)
🚫 BLOCKED: JARVIS/AI/MANUS action '{action}' - Operator idle for >{threshold}s (TEMPORARY RESTRICTION ON JARVIS, NOT ON @OP)
```

---

## Tags

`#TEMPORARY_RESTRICTIONS_ON_JARVIS_NOT_OP` `@JARVIS` `@OP` `#IDLENESS` `#RESTRICTION`
