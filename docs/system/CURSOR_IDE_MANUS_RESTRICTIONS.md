# Cursor IDE MANUS Restrictions

## Problem

MANUS was interacting with Cursor IDE menus, popups, and clipboard operations, causing unwanted UI interactions:
- Menus popping up unexpectedly
- Right-click context menus appearing
- Cut/copy/paste operations interfering with user workflow

## Solution

Added comprehensive restrictions to prevent MANUS from interacting with Cursor IDE UI elements.

## Restrictions

### 1. Menu Interactions - BLOCKED

**Blocked Actions**:
- `menu_click` - Clicking on menus
- `popup_interaction` - Interacting with popups
- `dialog_interaction` - Interacting with dialogs
- `context_menu` - Context menus
- `dropdown_menu` - Dropdown menus

**Penalty**: -100 XP (MAJOR)

**Reason**: "MANUS must not interact with Cursor IDE menus or popups"

### 2. Right-Click Operations - BLOCKED

**Blocked Actions**:
- `right_click` - Right mouse button clicks
- `context_menu` - Context menu triggers
- `Button-3` - Button 3 (right-click) events

**Penalty**: -100 XP (MAJOR)

**Reason**: "MANUS must not perform right-click operations in Cursor IDE"

### 3. Clipboard Operations - BLOCKED

**Blocked Actions**:
- `clipboard_copy` - Copy operations
- `clipboard_cut` - Cut operations
- `clipboard_paste` - Paste operations
- `Ctrl+C` - Copy keyboard shortcut
- `Ctrl+X` - Cut keyboard shortcut
- `Ctrl+V` - Paste keyboard shortcut

**Penalty**: -100 XP (MAJOR)

**Reason**: "MANUS must not perform clipboard operations (cut/copy/paste) in Cursor IDE"

## Integration

### MANUS Unified Control

The restrictions are enforced in `manus_unified_control.py` before executing any IDE control operations:

```python
# Check for Cursor IDE menu interactions
if operation.area == ControlArea.IDE_CONTROL:
    # Check menu interactions
    allowed, reason = blacklist_enforcer.check_cursor_menu_interaction(operation.action)
    if not allowed:
        # Block and apply penalty
        return OperationResult(success=False, ...)
    
    # Check right-click operations
    if 'right_click' in operation.action.lower():
        allowed, reason = blacklist_enforcer.check_cursor_right_click(operation.action)
        if not allowed:
            # Block and apply penalty
            return OperationResult(success=False, ...)
    
    # Check clipboard operations
    if 'clipboard' in operation.action.lower():
        allowed, reason = blacklist_enforcer.check_cursor_clipboard(operation.action)
        if not allowed:
            # Block and apply penalty
            return OperationResult(success=False, ...)
```

## Enforcement

All violations are automatically:
1. **Blocked** - Operation is prevented from executing
2. **Penalized** - -100 XP penalty applied
3. **Logged** - Violation recorded in penalty system

## Testing

```bash
# List all restrictions
python scripts/python/jarvis_blacklist_restriction_enforcer.py --list

# Check if action is blocked
python scripts/python/jarvis_blacklist_restriction_enforcer.py --check-menu "menu_click"
```

## Benefits

1. **No More Popups**: Menus and popups no longer appear unexpectedly
2. **No Right-Click Menus**: Right-click context menus are blocked
3. **No Clipboard Interference**: Cut/copy/paste operations don't interfere with user workflow
4. **Automatic Enforcement**: Violations are automatically blocked and penalized
5. **Transparent**: Full visibility into all restrictions

## Tags

@MANUS @JARVIS @CURSOR #RESTRICTION #BLACKLIST #POLICY #ENFORCEMENT #MENU #CLIPBOARD #RIGHTCLICK
