# Cursor Stability Issues

## Issues Reported

### 1. Keyboard Shortcuts Executing Automatically
**Reported:** 2025-01-02
**Status:** Investigating

**Symptoms:**
- Keyboard shortcuts being executed automatically
- No mouse movement (cursor stays in place)
- UI buttons clicking on/off by themselves
- User not triggering these actions

**Possible Causes:**
- Background automation scripts running
- Cursor IDE automation features enabled
- Windows accessibility/sticky keys
- Other automation software

**Investigation Notes:**
- @OP @INPUTS watcher does not appear to be running
- Multiple Python processes running (need to identify which are automation scripts)
- Many automation scripts exist in codebase (jarvis_cursor_ide_keyboard_integration.py, etc.)
- Cursor has various auto-features enabled (autoRefresh, autoFocus, autoIndex, etc.)

**Actions Taken:**
- None (user requested no changes while active)

---

### 2. Layout Mode Changing (Popping Out of "Jarvis" Layout)
**Reported:** 2025-01-02
**Status:** Documented

**Symptoms:**
- Cursor keeps popping out of "Jarvis" layout mode
- Layout mode changes unexpectedly
- User not intentionally changing layout

**Possible Causes:**
- Automation scripts modifying layout
- Cursor settings being changed
- Background processes affecting layout
- Cursor's auto-layout features
- Layout persistence issues

**Investigation Needed:**
- Check for scripts that modify Cursor layout
- Check Cursor layout settings/persistence
- Check if any automation is changing workspace layouts
- Check Cursor's layout auto-save/restore behavior

**Actions Taken:**
- None (user requested no changes while active)

---

## Related Files

- `.cursor/settings.json` - Cursor configuration
- `scripts/python/jarvis_cursor_ide_keyboard_integration.py` - Keyboard automation
- `scripts/python/jarvis_op_inputs_watcher_learner.py` - Input watcher
- Various automation scripts in `scripts/python/`

## User Instructions

**Per user request:**
- Do NOT modify Cursor settings while user is actively using it
- Wait for 10 minutes of inactivity before making experimental changes
- Only diagnose/document issues while user is active
- Make fixes only when explicitly requested or during idle time

## Tags

#STABILITY #CURSOR #ISSUES #DIAGNOSTIC #TROUBLESHOOTING
