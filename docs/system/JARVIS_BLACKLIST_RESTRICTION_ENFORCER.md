# JARVIS Blacklist/Restriction Enforcer

## Overview

The JARVIS Blacklist/Restriction Enforcer enforces all blacklists, restrictions, and negative entries across the system. It integrates with the penalty system to apply -xp for violations.

**"Actions have repercussions!"** - Every blacklist violation has real consequences.

## Blacklists and Restrictions

### 1. Cloud API Blocker

**Source**: `config/cloud_api_blocker.json`

**Blocked Providers**:
- `openai` - Direct OpenAI API (use Azure OpenAI instead)
- `anthropic` - Anthropic Claude API
- `google_ai` - Google AI API
- `cohere` - Cohere API

**Allowed Providers**:
- `local_ollama` - Local Ollama
- `llama3.2:3b` - Local model
- `kaiju_iron_legion` - KAIJU Iron Legion
- `grok` - GROK (decision tree controlled)
- `azure_openai` - Azure OpenAI (enforced routing)

**Enforcement**: Blocks cloud API calls to blocked providers, applies -100 XP (MAJOR) penalty

### 2. Forbidden Models

**Source**: `config/council_policy.json`

**Enforcement**: `fail_closed` - JEDI Council policy

**Current**: Empty list (no models currently forbidden)

**Enforcement**: Blocks forbidden model usage, applies -100 XP (MAJOR) penalty

### 3. Restricted Commands

**Source**: `config/lumina_pfsense_ssh_config.json`

**Restricted Commands**:
- `rm` - Remove/delete
- `dd` - Disk dump
- `format` - Format disk

**Context**: pfSense SSH operations

**Enforcement**: Blocks restricted commands, applies -500 XP (CRITICAL) penalty

### 4. Air-Gap Mode Restrictions

**Source**: Multiple config files (`kilo_code_optimized_config.json`, `multi_ide_optimal_settings.json`)

**Restrictions**:
- `air_gap_enabled`: True
- `block_cloud_unless_approved`: True

**Enforcement**: Blocks cloud access unless approved, applies -100 XP (MAJOR) penalty

### 5. Security Restrictions

**Restricted Directories**:
- `C:\Windows\System32` (Windows)
- `/etc`, `/bin`, `/sbin` (Unix)
- `/usr/bin`, `/usr/sbin` (Unix)

**Restricted Extensions**:
- `.exe`, `.bat`, `.cmd` (Windows executables)
- `.sh`, `.ps1` (Scripts)

**Enforcement**: Blocks access to restricted directories/files, applies -500 XP (CRITICAL) penalty

### 6. Cursor IDE Interaction Restrictions

**Menu Interactions**:
- `menu_click` - Clicking on menus
- `popup_interaction` - Interacting with popups
- `dialog_interaction` - Interacting with dialogs
- `context_menu` - Context menus
- `dropdown_menu` - Dropdown menus

**Right-Click Operations**:
- `right_click` - Right mouse button clicks
- `context_menu` - Context menu triggers
- `Button-3` - Button 3 (right-click) events

**Clipboard Operations**:
- `clipboard_copy` - Copy operations
- `clipboard_cut` - Cut operations
- `clipboard_paste` - Paste operations
- `Ctrl+C` - Copy keyboard shortcut
- `Ctrl+X` - Cut keyboard shortcut
- `Ctrl+V` - Paste keyboard shortcut

**Enforcement**: Blocks all Cursor IDE menu, right-click, and clipboard operations, applies -100 XP (MAJOR) penalty

**Reason**: MANUS must not interact with Cursor IDE menus, popups, or clipboard operations to prevent unwanted UI interactions

## Integration Points

The enforcer should be integrated at:

1. **Cloud API Selection**: Before making cloud API calls
2. **Model Selection**: Before loading/using LLM models
3. **Command Execution**: Before executing SSH/terminal commands
4. **File Operations**: Before accessing files/directories
5. **Network Operations**: Before making network requests

## Usage

### CLI Interface

```bash
# List all blacklists and restrictions
python scripts/python/jarvis_blacklist_restriction_enforcer.py --list

# Check if cloud API provider is blocked
python scripts/python/jarvis_blacklist_restriction_enforcer.py --check-cloud openai

# Check if model is forbidden
python scripts/python/jarvis_blacklist_restriction_enforcer.py --check-model gpt-4

# Check if command is restricted
python scripts/python/jarvis_blacklist_restriction_enforcer.py --check-command rm
```

### Programmatic Usage

```python
from scripts.python.jarvis_blacklist_restriction_enforcer import (
    get_blacklist_enforcer,
    RestrictionType
)

enforcer = get_blacklist_enforcer()

# Check cloud API
allowed, reason = enforcer.check_cloud_api("openai")
if not allowed:
    # Blocked - violation will be recorded
    pass

# Check model
allowed, reason = enforcer.check_model("gpt-4")
if not allowed:
    # Forbidden - violation will be recorded
    pass

# Check command
allowed, reason = enforcer.check_command("rm -rf /")
if not allowed:
    # Restricted - violation will be recorded
    pass

# Enforce with penalty
allowed, violation = enforcer.enforce_restriction(
    restriction_type=RestrictionType.CLOUD_API_BLOCKED,
    action="api_call",
    value="openai",
    check_func=enforcer.check_cloud_api,
    "openai"
)
```

## Penalty Integration

All violations are automatically recorded with the penalty system:

- **Cloud API Blocked**: -100 XP (MAJOR)
- **Forbidden Model**: -100 XP (MAJOR)
- **Restricted Command**: -500 XP (CRITICAL)
- **Air-Gap Violation**: -100 XP (MAJOR)
- **Security Violation**: -500 XP (CRITICAL)
- **File Access Restricted**: -500 XP (CRITICAL)

## Example Output

```
================================================================================
JARVIS BLACKLISTS AND RESTRICTIONS
================================================================================

📋 Blacklists:
   cloud_api_blocked: 4 entries
      - google_ai
      - anthropic
      - openai
      - cohere
   forbidden_model: 0 entries
   restricted_command: 0 entries

🔒 Restrictions:
   cloud_api_blocked: {'enabled': True, 'emergency_mode': False, ...}
   air_gap_violation: {'air_gap_enabled': True, 'block_cloud_unless_approved': True}
   security_violation: {'restricted_dirs': [...], 'restricted_extensions': [...]}
================================================================================
```

## Benefits

1. **Centralized Enforcement**: Single system for all blacklists/restrictions
2. **Automatic Penalties**: Violations automatically penalized with -xp
3. **Policy Compliance**: Ensures JARVIS follows all company policies
4. **Transparency**: Full visibility into all restrictions
5. **Consistency**: Uniform enforcement across all systems

## Tags

@JARVIS @PENALTY #BLACKLIST #RESTRICTION #POLICY #ENFORCEMENT #CLOUD #API #MODEL #COMMAND #SECURITY
