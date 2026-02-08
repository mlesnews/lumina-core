# JARVIS Restrictions and Penalties System

## Overview

**YES** - Restrictions apply to @JARVIS, -XP penalties are enforced, and @BLACKLISTED actions are blocked.

## Three-Layer Protection System

### 1. @JARVIS Restrictions (Idleness)

**Applies To**: @JARVIS, AI, MANUS, @DOIT, @ASK Chains

**When**: Operator idle for >10 minutes

**Actions Blocked**:
- `ai_action` - AI actions
- `jarvis_action` - JARVIS actions
- `manus_action` - MANUS control operations
- `autonomous_execution` - @DOIT autonomous execution
- `ask_chain_execution` - @ask chain execution

**XP Penalties**:
- **@DOIT Violation**: -500 XP (CRITICAL)
- **@ASK Chain Violation**: -100 XP (MAJOR)
- **MANUS Violation**: -50 XP (MODERATE)

**Integration Points**:
- `jarvis_doit_executor.py` - Blocks @DOIT execution
- `jarvis_execute_ask_chains.py` - Blocks @ask chain execution
- `manus_unified_control.py` - Blocks MANUS operations

### 2. -XP Penalties (Policy Violations)

**System**: `jarvis_policy_violation_penalty.py`

**Penalty Levels**:
- **CRITICAL**: -500 XP (e.g., @DOIT while idle)
- **MAJOR**: -100 XP (e.g., @ASK chain while idle)
- **MODERATE**: -50 XP (e.g., MANUS while idle)
- **MINOR**: -10 XP (e.g., minor policy violations)

**Policy Types**:
- `IDLENESS_RESTRICTION` - Operator idle violations
- `DOIT_VIOLATION` - @DOIT execution violations
- `ASK_CHAIN_VIOLATION` - @ask chain violations
- `MANUS_ACTION_VIOLATION` - MANUS action violations
- `CLOUD_API_VIOLATION` - Cloud API usage violations
- `FORBIDDEN_MODEL_VIOLATION` - Forbidden model usage
- `RESTRICTED_COMMAND_VIOLATION` - Restricted command execution
- `AIR_GAP_VIOLATION` - Air-gap policy violations
- `SECURITY_VIOLATION` - Security policy violations
- `CURSOR_MENU_INTERACTION` - Cursor IDE menu interactions
- `CURSOR_RIGHT_CLICK` - Cursor IDE right-click operations
- `CURSOR_CLIPBOARD_OPERATION` - Cursor IDE clipboard operations
- `FORCE_SENSITIVE_RESTRICTION` - Force-sensitive listing violations

**Tracking**:
- JARVIS XP tracked in `data/jarvis_xp/xp_data.json`
- Violations logged in `data/jarvis_xp/violations.json`
- Current XP displayed in violation logs

### 3. @BLACKLISTED Actions

**System**: `jarvis_blacklist_restriction_enforcer.py`

**Blacklist Types**:
- **Cloud API Blacklist**: Blocked cloud API providers
- **Forbidden Models**: Blocked AI models
- **Restricted Commands**: Blocked command execution
- **Air-Gap Violations**: Network access restrictions
- **Security Violations**: Security policy violations
- **Cursor IDE Interactions**: Menu, right-click, clipboard operations
- **Force-Sensitive Listings**: Sith blacklist, Jedi whitelist, Gray Jedi greylist

**Enforcement**:
- Actions checked before execution
- Blocked actions logged with reason
- XP penalties applied for violations
- Violations tracked in penalty system

**Integration Points**:
- `jarvis_doit_executor.py` - Checks before @DOIT execution
- `jarvis_execute_ask_chains.py` - Checks before @ask chain execution
- `manus_unified_control.py` - Checks before MANUS operations

## Complete Flow

### Example: @DOIT Execution Attempt While Operator Idle

1. **@DOIT Executor** (`jarvis_doit_executor.py`):
   - Checks operator idleness restriction
   - Operator idle for >10 minutes → **BLOCKED**

2. **Penalty System** (`jarvis_policy_violation_penalty.py`):
   - Records violation: `DOIT_VIOLATION`
   - Severity: `CRITICAL`
   - **Applies -500 XP penalty**
   - Logs: `🚫 POLICY VIOLATION: @DOIT execution blocked - Penalty: -500 XP`

3. **Blacklist Enforcer** (`jarvis_blacklist_restriction_enforcer.py`):
   - Checks for blacklisted actions
   - If action is blacklisted → **BLOCKED**
   - Applies additional XP penalty if violation

4. **Result**:
   - @DOIT execution **BLOCKED**
   - -500 XP penalty applied
   - Violation logged
   - Operator notified

## Verification

### Check JARVIS XP
```bash
python scripts/python/jarvis_policy_violation_penalty.py --status
```

### Check Restrictions
```bash
python scripts/python/operator_idleness_restriction.py --status
```

### Check Blacklists
```bash
python scripts/python/jarvis_blacklist_restriction_enforcer.py --list
```

## Summary

**YES** - All three layers are active:

1. ✅ **@JARVIS Restrictions**: Blocks JARVIS/AI/MANUS actions when operator idle >10 minutes
2. ✅ **-XP Penalties**: Applies XP penalties for all violations (CRITICAL: -500, MAJOR: -100, MODERATE: -50)
3. ✅ **@BLACKLISTED Actions**: Blocks blacklisted actions (cloud APIs, models, commands, Cursor IDE interactions)

**All restrictions apply to @JARVIS, penalties are enforced, and blacklisted actions are blocked.**

## Tags

@JARVIS #RESTRICTIONS #PENALTIES #BLACKLIST #XP #POLICY #ENFORCEMENT #IDLENESS
