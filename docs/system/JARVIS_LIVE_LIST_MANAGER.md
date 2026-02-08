# JARVIS Live List Manager

## Overview

The JARVIS Live List Manager maintains active/live blacklist, whitelist, and greylist with real-time monitoring and dynamic updates. It integrates with the penalty system to apply -xp for violations.

**"Actions have repercussions!"** - Every blacklist violation has real consequences.

## List Types

### Blacklist
- **Purpose**: Block forbidden actions/values
- **Enforcement**: Automatic blocking with -xp penalty
- **Example**: Cursor menu interactions, restricted commands

### Whitelist
- **Purpose**: Explicitly allow specific actions/values
- **Enforcement**: Highest priority - overrides blacklist
- **Example**: Approved cloud APIs, safe commands

### Greylist
- **Purpose**: Conditionally allow actions/values (requires approval)
- **Enforcement**: Requires callback approval or auto-approval flag
- **Example**: Experimental features, temporary access

## Features

1. **Live Monitoring**: Continuous monitoring and automatic cleanup
2. **Dynamic Updates**: Add/remove entries in real-time
3. **Expiration**: Entries can expire automatically
4. **Violation Tracking**: Tracks violation counts and timestamps
5. **Penalty Integration**: Automatically applies -xp for violations
6. **Persistent Storage**: Saves to JSON for persistence

## Current Blacklist Entries

### Cursor IDE Interactions (BLACKLISTED)

1. **cursor_menu_interaction**
   - Category: `ide_interaction`
   - Description: MANUS should not interact with Cursor IDE menus that keep popping up
   - Status: ACTIVE

2. **cursor_right_click**
   - Category: `ide_interaction`
   - Description: MANUS should not trigger right-click context menus in Cursor IDE
   - Status: ACTIVE

3. **cursor_clipboard_cut_paste**
   - Category: `ide_interaction`
   - Description: MANUS should not use cut/paste operations that trigger Cursor IDE menus
   - Status: ACTIVE

## Usage

### CLI Interface

```bash
# Add to blacklist
python scripts/python/jarvis_live_list_manager.py --add-blacklist "value" "category" "description"

# Add to whitelist
python scripts/python/jarvis_live_list_manager.py --add-whitelist "value" "category" "description"

# Add to greylist
python scripts/python/jarvis_live_list_manager.py --add-greylist "value" "category" "description"

# Check value
python scripts/python/jarvis_live_list_manager.py --check "value" "category"

# List entries
python scripts/python/jarvis_live_list_manager.py --list blacklist
python scripts/python/jarvis_live_list_manager.py --list whitelist
python scripts/python/jarvis_live_list_manager.py --list greylist
python scripts/python/jarvis_live_list_manager.py --list all

# Show statistics
python scripts/python/jarvis_live_list_manager.py --stats

# Remove entry
python scripts/python/jarvis_live_list_manager.py --remove "entry_id"

# Add with expiration
python scripts/python/jarvis_live_list_manager.py --add-blacklist "value" "category" "description" --expires 24
```

### Programmatic Usage

```python
from scripts.python.jarvis_live_list_manager import (
    get_live_list_manager,
    ListType
)

manager = get_live_list_manager()

# Add to blacklist
entry = manager.add_entry(
    ListType.BLACKLIST,
    "cursor_menu_interaction",
    "ide_interaction",
    "MANUS should not interact with Cursor IDE menus",
    expires_in_hours=24  # Optional expiration
)

# Check value
allowed, reason, entry = manager.check_value(
    "cursor_menu_interaction",
    category="ide_interaction"
)

if not allowed:
    # Blocked - violation recorded, penalty applied
    print(f"Blocked: {reason}")
```

## Integration Points

### MANUS Unified Control
- Checks blacklist before executing operations
- Blocks Cursor menu interactions, right-click, clipboard operations
- Records violations and applies penalties

### Penalty System
- All blacklist violations automatically penalized with -xp
- Severity: MAJOR (-100 XP)
- Policy Type: `BLACKLIST_VIOLATION`

## Storage

Lists are stored in:
- `data/jarvis_live_lists/live_lists.json` - Current lists
- `data/jarvis_live_lists/list_history.json` - History (future)

## Monitoring

The system runs a background monitoring thread that:
- Cleans up expired entries
- Updates entry statuses
- Saves lists periodically (every minute)

## Example Output

```
================================================================================
JARVIS LIVE LIST STATISTICS
================================================================================

BLACKLIST:
   Total: 3
   Active: 3
   Expired: 0

WHITELIST:
   Total: 0
   Active: 0
   Expired: 0

GREYLIST:
   Total: 0
   Active: 0
   Expired: 0
================================================================================
```

## Benefits

1. **Prevents Unwanted Interactions**: Blocks MANUS from triggering Cursor menus
2. **Real-Time Updates**: Add/remove entries without restarting
3. **Automatic Enforcement**: Violations automatically penalized
4. **Flexible Control**: Whitelist overrides, greylist for conditional access
5. **Transparency**: Full visibility into all lists and violations

## Tags

@JARVIS @PENALTY #BLACKLIST #WHITELIST #GREYLIST #LIVE #MONITORING #CURSOR #IDE #MANUS
