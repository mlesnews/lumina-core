# Cursor Workspace Mode Workflow - Proper Programming Operations

**Date:** 2025-12-27  
**Status:** ✅ **COMPLETE**  
**Context:** Ensuring proper workflows, precedence, and operations for real-life programming

---

## Overview

This document describes the proper workflow for using Cursor IDE workspace modes:
- **Workspace Mode** (folder opened): For debugging (full project context)
- **Non-Workspace Mode** (files only): For normal programming operations

---

## 1. Workflow Principles

### Workspace Mode (Folder Opened) - Debugging

**When to use:**
- Debugging code with breakpoints
- Full project context needed
- Multi-file operations
- Refactoring across files
- Code lens and IntelliSense with project context
- Need for project-wide search and navigation

**Settings Applied:**
```json
{
  "debug.enabled": true,
  "debug.allowBreakpointsEverywhere": true,
  "debug.showBreakpointsInOverviewRuler": true,
  "debug.inlineValues": true,
  "editor.codeLens": true,
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/*/**": true
  },
  "search.exclude": {
    "**/node_modules": true
  }
}
```

### Non-Workspace Mode (Files Only) - Normal Programming

**When to use:**
- Quick edits to single files
- Code review
- Reading code
- Lightweight editing
- No need for full project context

**Settings Applied:**
```json
{
  "debug.enabled": false,
  "editor.codeLens": false,
  "files.watcherExclude": {},
  "search.exclude": {}
}
```

---

## 2. Precedence Rules

Settings precedence (highest to lowest):

1. **Workspace Settings** (`.cursor/settings.json` in project root)
2. **User Settings** (`~/.cursor/User/settings.json`)
3. **Default Settings** (Cursor IDE defaults)

**Example:**
- If workspace mode is active, workspace settings take precedence
- If non-workspace mode, user settings take precedence
- Shared settings (formatOnSave, rulers, etc.) are synced between modes

---

## 3. Automatic Synchronization

### How It Works

1. **Mode Detection**: System detects whether workspace folder is opened
2. **Settings Sync**: Shared settings are automatically synced between modes
3. **Precedence Application**: Correct settings are applied based on mode

### Syncable Settings

These settings are automatically synced between workspace and non-workspace modes:
- `editor.formatOnSave`
- `editor.formatOnPaste`
- `editor.rulers`
- `editor.suggestSelection`
- `editor.wordBasedSuggestions`
- `editor.fontSize`
- `editor.fontFamily`
- `editor.tabSize`
- `editor.insertSpaces`
- `editor.detectIndentation`

### Sync Trigger

- **Automatic**: Runs when mode changes are detected
- **Cron/Task Scheduler**: Runs periodically (default: every 60 minutes)
- **Manual**: Can be triggered via CLI

---

## 4. Usage Examples

### Verify Current Workflow

```bash
python scripts/python/cursor_workspace_mode_manager.py --verify
```

Output:
```json
{
  "current_mode": "workspace",
  "is_debug_mode": true,
  "workflow_correct": true,
  "issues": [],
  "recommendations": []
}
```

### Detect Current Mode

```bash
python scripts/python/cursor_workspace_mode_manager.py --detect
```

Output:
```
Mode: workspace
Workspace: True
Debug Mode: True
```

### Manual Sync

```bash
python scripts/python/cursor_workspace_mode_manager.py --sync
```

### Auto-Sync

```bash
python scripts/python/cursor_workspace_mode_manager.py --auto-sync
```

### Get Summary

```bash
python scripts/python/cursor_workspace_mode_manager.py --summary
```

---

## 5. Cron/Task Scheduler Integration

### Windows Task Scheduler

**Task Name:** Cursor Workspace Sync  
**Script:** `scripts/python/cursor_workspace_sync_cron.py`  
**Schedule:** Every 60 minutes  
**Run:** `python scripts/python/cursor_workspace_sync_cron.py`

### NAS Cron (Linux)

Add to `jarvis_crontab`:
```
# Cursor Workspace Settings Sync - Sync workspace and non-workspace mode settings
0 * * * * /volume1/@appstore/python3/bin/python3 /volume1/docker/jarvis/.lumina/scripts/python/cursor_workspace_sync_cron.py >> /volume1/docker/jarvis/.lumina/logs/cron_Cursor_WorkspaceSync.log 2>&1
```

This runs every hour (at minute 0).

---

## 6. Real-Life Programming Workflow

### Scenario 1: Debugging a Bug

1. **Open workspace folder** in Cursor IDE
2. System detects workspace mode → applies debugging settings
3. Set breakpoints, use debugger
4. Full project context available for navigation
5. Settings automatically applied for debugging

### Scenario 2: Quick Code Review

1. **Open single file** in Cursor IDE (no folder)
2. System detects non-workspace mode → applies lightweight settings
3. Review code without full project overhead
4. Quick edits if needed
5. No debugging overhead

### Scenario 3: Refactoring

1. **Open workspace folder** in Cursor IDE
2. Workspace mode enables:
   - Full project context
   - Multi-file operations
   - Code lens for references
   - Project-wide search
3. Perform refactoring with full context

### Scenario 4: Reading Documentation

1. **Open file(s) without workspace**
2. Non-workspace mode for lightweight viewing
3. No project indexing overhead
4. Fast file access

---

## 7. Configuration

Configuration file: `config/cursor_workspace_config.json`

### Key Settings

```json
{
  "auto_sync": true,
  "sync_interval_minutes": 60,
  "sync_settings": [
    "editor.formatOnSave",
    "editor.formatOnPaste",
    "editor.rulers"
  ]
}
```

---

## 8. Integration with Other Systems

### Cursor Agent Modes

- Workspace mode automatically enables debug capabilities for Debug mode
- Non-workspace mode uses Agent mode by default

### MANUS Framework

- Workspace mode detection integrated with MANUS monitoring
- Settings sync tracked in MANUS logs

### Universal IDE CA Manager

- Workspace settings synced with Universal IDE configuration
- Mode-specific optimizations applied

---

## 9. Verification Checklist

✅ **Workspace Mode Detection**
- Correctly detects when folder is opened
- Correctly detects when files-only are opened

✅ **Settings Application**
- Workspace mode gets debugging settings
- Non-workspace mode gets lightweight settings

✅ **Precedence Rules**
- Workspace settings > User settings > Defaults
- Correct settings applied based on mode

✅ **Synchronization**
- Shared settings synced automatically
- Sync works both directions
- Cron/task scheduler integration

✅ **Workflow Correctness**
- Proper mode for debugging vs normal programming
- No conflicts between modes
- Settings consistent and correct

---

## 10. Troubleshooting

### Issue: Settings not syncing

**Solution:**
1. Run `--verify` to check workflow
2. Run `--auto-sync` manually
3. Check logs in `logs/cron_Cursor_WorkspaceSync.log`

### Issue: Wrong mode detected

**Solution:**
1. Run `--detect` to see current detection
2. Ensure workspace folder is properly opened
3. Check `.cursor/settings.json` exists for workspace mode

### Issue: Settings conflicts

**Solution:**
1. Run `--verify` to see conflicts
2. Run `--sync` to resolve conflicts
3. Check `cursor_workspace_config.json` for sync settings list

---

## 11. Files

1. ✅ `scripts/python/cursor_workspace_mode_manager.py` - Main manager
2. ✅ `scripts/python/cursor_workspace_sync_cron.py` - Cron job script
3. ✅ `config/cursor_workspace_config.json` - Configuration
4. ✅ `docs/system/CURSOR_WORKSPACE_MODE_WORKFLOW.md` - This document

---

**Version:** 1.0.0  
**Last Updated:** 2025-12-27  
**Status:** ✅ **COMPLETE**

