# Cursor IDE Status Integration Guide

## Quick Start

### Current Status

**@AGENT@MASTER.TODOLIST:**
- **@PEAK**: 49.26%
- **Total**: 135 todos
- **Active**: 86 todos
- **Complete**: 49 todos

**@SUBAGENT@PADAWAN.LIST:**
- **@PEAK**: 0.0%
- **Total**: 1 todo
- **Active**: 1 todo
- **Complete**: 0 todos

**OVERALL @PEAK**: 48.9%

## Status File Location

**Path**: `data/cursor_ide_status/todo_status.json`

**Update Command**:
```bash
python scripts/python/cursor_ide_todo_status_display.py
```

## Cursor IDE Integration Options

### Option 1: Status Bar Display

**Manual Setup:**
1. Open Cursor IDE Settings
2. Add custom status bar item
3. Point to `data/cursor_ide_status/todo_status.json`
4. Display: `@MASTER: XX.X% | @PADAWAN: XX.X% | @PEAK: XX.X%`

### Option 2: Webview Panel

**Create Extension:**
1. Create VS Code/Cursor extension
2. Add webview panel
3. Read `todo_status.json`
4. Display formatted status
5. Auto-refresh on file change

### Option 3: Command Palette

**Add Command:**
1. Create command: `lumina.showTodoStatus`
2. Execute: `python scripts/python/cursor_ide_todo_status_display.py`
3. Display results in output panel

### Option 4: File Watcher

**Auto-Update:**
1. Watch `master_todos.json` and `master_padawan_todos.json`
2. On change, run status update
3. Update status file automatically
4. Refresh UI if open

## Status Bar Text

**Format**: `@MASTER: 49.26% | @PADAWAN: 0.0% | @PEAK: 48.9%`

**Color Coding:**
- **Green**: @PEAK > 75%
- **Yellow**: @PEAK 25-75%
- **Red**: @PEAK < 25%

## Always Visible

**At All Times:**
- Status file: `data/cursor_ide_status/todo_status.json`
- Status bar: Custom status bar item
- Webview: Keep panel open
- Command: Run anytime via command palette

## Auto-Refresh

**Recommended Setup:**
1. File watcher on todo JSON files
2. Auto-run status update on change
3. Update status file
4. Refresh UI automatically

## Next Steps

1. **Create Cursor IDE Extension** (recommended)
2. **Set up file watcher** for auto-updates
3. **Add status bar item** for always-visible status
4. **Create webview panel** for detailed view

---

**Status File**: `data/cursor_ide_status/todo_status.json`
**Update Script**: `scripts/python/cursor_ide_todo_status_display.py`
**Documentation**: `docs/CURSOR_IDE_TODO_STATUS_DISPLAY.md`
