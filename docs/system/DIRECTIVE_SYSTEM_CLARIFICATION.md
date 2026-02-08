# Directive System Clarification

**Date**: 2026-01-03  
**Status**: ✅ **ACTIVE**  
**Tag**: @JARVIS @MARVIN @AI

---

## Directive System Overview

### Default Mode: `@fullauto`

**`@fullauto` is the default mode** - Full automation without requiring approval.

- ✅ Execute autonomously
- ✅ No manual intervention required
- ✅ Complete automation enabled
- ✅ Default behavior for all operations

### AI Interaction Mode: `@ask` (lowercase)

**`@ask` is for AI** - Request approval or interaction before proceeding.

- 🤖 Request approval before proceeding
- 🤖 Ask for confirmation on actions
- 🤖 Override default `@fullauto` mode
- 🤖 Enable AI-to-human interaction

### AI Token Request System: `@ASK` (uppercase)

**`@ASK` = ONE AI TOKEN REQUEST** - Individual AI token request tracking system.

- 📝 Each `@ASK` represents one AI token request
- 📝 Tracks individual AI requests/tasks
- 📝 Used for request management and chaining
- 📝 Part of the @asks system for task tracking

---

## Precedence Rule: UPPERCASE TRUMPS LOWERCASE

**CRITICAL RULE**: In agent chat context metadata, **UPPERCASE tags have higher precedence than lowercase tags**.

- ✅ **`@ASK`** (uppercase) > **`@ask`** (lowercase)
- ✅ **`@DOIT`** (uppercase) > **`@doit`** (lowercase)
- ✅ **`@FULLAUTO`** (uppercase) > **`@fullauto`** (lowercase)
- ✅ **UPPERCASE = Higher priority, stronger directive**
- ✅ **lowercase = Lower priority, weaker directive**

**Why**: Subconscious pattern - uppercase naturally draws attention and indicates importance/priority.

See `docs/system/SHORT_TAG_PRECEDENCE_ORDER.md` for complete precedence hierarchy.

---

## Important Distinction: `@ask` vs `@ASK`

### `@ask` (lowercase) - Directive
- **Purpose**: AI interaction directive
- **Usage**: Request approval before proceeding
- **Type**: Command/behavior modifier
- **Example**: `@ask python script.py` (requests approval before running)

### `@ASK` (uppercase) - Token Request System
- **Purpose**: ONE AI TOKEN REQUEST
- **Usage**: Individual AI token request tracking
- **Type**: Task/request tracking system
- **Example**: `@ASK: Fix the email aggregation system` (one token request entry)

**Key Difference:**
- `@ask` = "Ask for approval" (directive)
- `@ASK` = "One AI token request" (tracking system)

---

## Directive Usage

### When to Use `@fullauto` (Default)

- **Default behavior** - No directive needed
- Autonomous execution
- Full automation workflows
- Background tasks
- Scheduled operations
- System maintenance

### When to Use `@ask`

- **AI interaction required** - Need human approval
- Critical decisions
- Destructive operations
- Configuration changes
- Resource-intensive tasks
- When uncertainty exists

---

## Directive Hierarchy

1. **`@fullauto`** (Default)
   - Full automation
   - No approval needed
   - Autonomous execution

2. **`@ask`** (Override)
   - Request approval
   - AI interaction mode
   - Overrides `@fullauto`

3. **`@manual`** (Override)
   - User handles manually
   - Skip automation
   - Overrides both `@fullauto` and `@ask`

---

## Examples

### Default Behavior (No Directive = `@fullauto`)

```
# This runs with full automation (default)
python scripts/python/setup_mailplus_email_hub.py
```

### AI Interaction (`@ask`)

```
# This requests approval before proceeding
@ask python scripts/python/setup_mailplus_email_hub.py
```

### Manual Override (`@manual`)

```
# This skips automation, user handles manually
@manual python scripts/python/setup_mailplus_email_hub.py
```

---

## Integration with Other Systems

### JARVIS Workflows

- **Default**: `@fullauto` - JARVIS executes autonomously
- **With `@ask`**: JARVIS requests approval before execution
- **With `@manual`**: JARVIS skips automation

### Email Aggregation

- **Default**: `@fullauto` - Automatic email aggregation
- **With `@ask`**: Request approval before aggregating
- **With `@manual`**: Skip automatic aggregation

### NAS Operations

- **Default**: `@fullauto` - Automatic NAS operations
- **With `@ask`**: Request approval before NAS changes
- **With `@manual`**: Skip automatic NAS operations

---

## Summary

✅ **`@fullauto` is the default** - Full automation without approval  
✅ **`@ask` (lowercase) is for AI** - Request approval/interaction before proceeding  
✅ **`@ASK` (uppercase) = ONE AI TOKEN REQUEST** - Individual AI token request tracking  
✅ **`@manual` overrides both** - User handles manually

**Default behavior**: All operations run with `@fullauto` unless explicitly overridden with `@ask` or `@manual`.

**Important Distinction:**
- **`@ask`** (lowercase) = Directive for AI interaction/approval
- **`@ASK`** (uppercase) = ONE AI TOKEN REQUEST (task tracking system)

---

**Last Updated**: 2026-01-03  
**Maintained By**: @JARVIS @MARVIN
