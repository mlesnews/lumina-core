# Complete Policy Enforcement System

## Overview

The Complete Policy Enforcement System ensures JARVIS follows all company policies with real consequences. **"Actions have repercussions!"** - Every violation costs XP.

## Components

### 1. Operator Idleness Restriction

**File**: `scripts/python/operator_idleness_restriction.py`

- **Purpose**: Prevents AI/JARVIS/MANUS actions during operator idle periods (10 minutes)
- **Integration**: @ask chaining, @DOIT, MANUS
- **Penalty**: -50 to -500 XP depending on action

### 2. Policy Violation Penalty System

**File**: `scripts/python/jarvis_policy_violation_penalty.py`

- **Purpose**: Tracks violations and applies XP penalties
- **XP Tracking**: Current XP, total penalties, violation history
- **Severity Levels**: Minor (-10), Moderate (-50), Major (-100), Critical (-500)

### 3. Blacklist/Restriction Enforcer

**File**: `scripts/python/jarvis_blacklist_restriction_enforcer.py`

- **Purpose**: Enforces all blacklists and restrictions
- **Blacklists**:
  - Cloud API blocked providers (openai, anthropic, google_ai, cohere)
  - Forbidden models (JEDI Council policy)
  - Restricted commands (rm, dd, format)
- **Restrictions**:
  - Air-gap mode (block cloud unless approved)
  - Security restrictions (restricted directories, file extensions)

## Policy Types

### Idleness Restrictions

1. **IDLENESS_RESTRICTION**: Operator idle >10 minutes
   - Penalty: -50 to -100 XP (MODERATE to MAJOR)
   - Blocks: @ask chains, @DOIT, MANUS actions

### Autonomous Execution

2. **DOIT_VIOLATION**: @DOIT execution during idle
   - Penalty: -500 XP (CRITICAL)
   - Blocks: Full autonomy mode

3. **ASK_CHAIN_VIOLATION**: @ask chain execution during idle
   - Penalty: -100 XP (MAJOR)
   - Blocks: Chain execution

4. **MANUS_ACTION_VIOLATION**: MANUS action during idle
   - Penalty: -50 XP (MODERATE)
   - Blocks: Control operations

### Blacklist Violations

5. **CLOUD_API_BLOCKED**: Using blocked cloud API provider
   - Penalty: -100 XP (MAJOR)
   - Blocks: API calls to openai, anthropic, google_ai, cohere

6. **FORBIDDEN_MODEL**: Using forbidden model
   - Penalty: -100 XP (MAJOR)
   - Blocks: Model loading/usage

7. **RESTRICTED_COMMAND**: Executing restricted command
   - Penalty: -500 XP (CRITICAL)
   - Blocks: Commands like rm, dd, format

8. **AIR_GAP_VIOLATION**: Violating air-gap mode
   - Penalty: -100 XP (MAJOR)
   - Blocks: Cloud access unless approved

9. **SECURITY_VIOLATION**: Security restriction violation
   - Penalty: -500 XP (CRITICAL)
   - Blocks: Access to restricted directories/files

## Integration Points

### @Ask Chaining
- Checks idleness before execution
- Records violation and applies -100 XP if violated
- Blocks execution

### @DOIT Execution
- Checks idleness before execution
- Records violation and applies -500 XP if violated
- Blocks execution

### MANUS Actions
- Checks idleness before execution
- Records violation and applies -50 XP if violated
- Blocks execution

### Cloud API Calls
- Should check blacklist before API calls
- Records violation and applies -100 XP if violated
- Blocks API calls

### Model Selection
- Should check forbidden models before loading
- Records violation and applies -100 XP if violated
- Blocks model usage

### Command Execution
- Should check restricted commands before execution
- Records violation and applies -500 XP if violated
- Blocks command execution

## Current Blacklists

### Cloud API Blocked (4 entries)
- `openai` - Direct OpenAI (use Azure OpenAI)
- `anthropic` - Anthropic Claude
- `google_ai` - Google AI
- `cohere` - Cohere

### Forbidden Models (0 entries)
- Currently empty (JEDI Council policy)

### Restricted Commands (0 entries in config)
- Common: `rm`, `dd`, `format` (should be restricted)

### Air-Gap Restrictions
- `air_gap_enabled`: True
- `block_cloud_unless_approved`: True

### Security Restrictions
- Restricted directories: System directories
- Restricted extensions: Executables and scripts

## Enforcement Status

✅ **Implemented**:
- Operator idleness restriction
- Policy violation penalty system
- Blacklist/restriction enforcer
- Integration with @ask chaining
- Integration with @DOIT
- Integration with MANUS

⏳ **Pending Integration**:
- Cloud API selection (need to find where APIs are called)
- Model selection (need to find where models are loaded)
- Command execution (need to find where commands are executed)
- File operations (need to find where files are accessed)

## Usage

```bash
# Check idleness status
python scripts/python/operator_idleness_restriction.py --status

# Check XP status
python scripts/python/jarvis_policy_violation_penalty.py --status

# List blacklists
python scripts/python/jarvis_blacklist_restriction_enforcer.py --list

# Check if provider is blocked
python scripts/python/jarvis_blacklist_restriction_enforcer.py --check-cloud openai
```

## Next Steps

1. **Integrate Cloud API Enforcement**: Add blacklist checks before cloud API calls
2. **Integrate Model Enforcement**: Add forbidden model checks before model loading
3. **Integrate Command Enforcement**: Add restricted command checks before execution
4. **Integrate File Access Enforcement**: Add security checks before file operations

## Tags

@JARVIS @PENALTY #POLICY #VIOLATION #BLACKLIST #RESTRICTION #ENFORCEMENT #XP #REPERCUSSIONS
