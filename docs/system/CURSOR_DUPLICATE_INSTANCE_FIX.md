# Cursor Duplicate Instance Prevention (+++++ Memory Priority)

## Issue Summary
- **Date**: 2026-01-07
- **Problem**: Multiple Cursor instances appearing (user reported "two copies" - workstation vs vanilla)
- **Root Cause**: `cursor_intelligent_warm_recycle.py` was launching Cursor without checking if it was already running

## Diagnostic Findings
- **Main Cursor Processes**: 4 detected (should be 1)
- **Child Processes**: 9 (normal - renderer, utility, GPU, etc.)
- **Startup Shortcut**: `JARVIS_StartCursor.lnk` in Windows startup folder (no target configured)
- **Scripts That Launch Cursor**: 9 scripts using warm recycle system

## Fix Applied
Added `is_cursor_running()` check to `cursor_intelligent_warm_recycle.py`:
- Checks for main Cursor process (excludes child processes with `--type=` flag)
- Prevents launching new instance if Cursor is already running
- Logs informative message if Cursor is already running

## Prevention Rules (+++++ Priority)

### 1. Singleton Pattern for Cursor Launch
- **ALWAYS** check if Cursor is running before launching
- Use `is_cursor_running()` method before any `subprocess.Popen()` call
- Never launch Cursor without checking first

### 2. Warm Recycle System
- The `cursor_intelligent_warm_recycle.py` system now includes automatic checks
- If Cursor is already running, it will skip launch and log a message
- Only launches Cursor after graceful shutdown completes

### 3. Startup Scripts
- Review `JARVIS_StartCursor.lnk` in startup folder
- Ensure it has proper target and doesn't conflict with other launch mechanisms
- Consider removing if redundant with other startup systems

### 4. Scripts Using Warm Recycle
The following scripts use the warm recycle system (now protected):
- `jarvis_hands_free_startup.py`
- `jarvis_developer_reboot.py`
- `jarvis_god_cycle.py`
- `manus_chained_ask_cycle.py`
- `run_llm_recycle_check.py`
- Others that import `cursor_intelligent_warm_recycle`

## Action Items
- ✅ Added `is_cursor_running()` check to warm recycle system
- ⏳ Review and fix `JARVIS_StartCursor.lnk` startup shortcut
- ⏳ Consider adding singleton pattern to other Cursor launch scripts
- ⏳ Monitor for duplicate instances after fix

## Status
- **Issue**: IDENTIFIED AND FIXED
- **Prevention**: IMPLEMENTED (singleton check in warm recycle)
- **Vigilance**: HIGH (as @JEDI @PATHFINDER)
