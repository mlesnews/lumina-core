# Cursor IDE Macros & Keyboard Shortcuts Setup

**Date**: 2026-01-02  
**Status**: ✅ **CONFIGURED**  
**Tag**: #CURSOR #MACROS #SHORTCUTS #AUTOMATION

---

## Overview

Cursor IDE has been configured with keyboard shortcuts (macros) and tasks for quick access to LUMINA automation features.

---

## Keyboard Shortcuts (Macros)

### Screenshot Macros

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl+Shift+S` | Capture Screenshot | Quick screenshot capture |
| `Ctrl+Shift+C` | Capture Screenshot with Context | Screenshot with description prompt |
| `Ctrl+Alt+S` | Quick Screenshot | Silent screenshot (no panel) |

### MANUS Macros

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl+Shift+M` | MANUS Control | Execute MANUS command (prompts for command) |

---

## Tasks (Run via Command Palette)

Access via: **Ctrl+Shift+P** → **"Tasks: Run Task"** → Select task

### Screenshot Tasks

- **Capture Screenshot** - Quick screenshot capture
- **Capture Screenshot with Context** - Screenshot with description prompt
- **Quick Screenshot** - Silent screenshot capture

### Automation Tasks

- **MANUS Control** - Execute MANUS commands
- **SAML SSO Setup** - Setup SAML SSO for DSM
- **Troubleshoot LDAP Auth** - Diagnose LDAP authentication issues
- **Verify SSO Readiness** - Check SSO configuration status

### JARVIS Tasks (Existing)

- **JARVIS: Auto Git Commit** - Auto-commit changes
- **JARVIS: Health Check** - System health check
- **JARVIS: Cursor IDE Optimization** - Optimize Cursor settings
- **JARVIS: Monitor IDE Notifications** - Monitor IDE notifications

---

## Usage Examples

### Quick Screenshot

1. Press `Ctrl+Shift+S`
2. Screenshot captured automatically
3. Saved to `data/manus_rdp_captures/`

### Screenshot with Context

1. Press `Ctrl+Shift+C`
2. Enter description when prompted (e.g., "DSM LDAP error")
3. Screenshot captured with context
4. Ready for attachment to chat

### MANUS Control

1. Press `Ctrl+Shift+M`
2. Enter MANUS command when prompted
3. Command executed via MANUS Unified Control

### Via Command Palette

1. Press `Ctrl+Shift+P`
2. Type "Tasks: Run Task"
3. Select task from list
4. Task executes automatically

---

## Configuration Files

- **Keybindings**: `.cursor/keybindings.json`
- **Tasks**: `.cursor/tasks.json`

---

## Adding New Macros

### Add Keyboard Shortcut

Edit `.cursor/keybindings.json`:

```json
{
  "key": "ctrl+shift+x",
  "command": "workbench.action.tasks.runTask",
  "args": "Your Task Name",
  "when": "editorTextFocus"
}
```

### Add Task

Edit `.cursor/tasks.json`:

```json
{
  "label": "Your Task Name",
  "type": "shell",
  "command": "python",
  "args": [
    "${workspaceFolder}/scripts/python/your_script.py",
    "--arg",
    "value"
  ],
  "problemMatcher": [],
  "presentation": {
    "reveal": "always",
    "panel": "new"
  }
}
```

---

## Benefits

✅ **Quick Access**: Keyboard shortcuts for common tasks  
✅ **No Command Line**: Run scripts without typing commands  
✅ **Integrated**: Works seamlessly with Cursor IDE  
✅ **Context-Aware**: Screenshots include context descriptions  
✅ **Automated**: MANUS and JARVIS integration  

---

## Troubleshooting

### Shortcut Not Working

1. Check if keybinding conflicts with existing shortcuts
2. Verify task name matches exactly in `tasks.json`
3. Reload Cursor window: `Ctrl+Shift+P` → "Reload Window"

### Task Not Found

1. Verify task exists in `.cursor/tasks.json`
2. Check task label matches exactly
3. Ensure script path is correct

### Script Execution Error

1. Check Python path is correct
2. Verify script exists at specified path
3. Check script permissions

---

**Last Updated**: 2026-01-02  
**Status**: Ready to use  
**Files**: `.cursor/keybindings.json`, `.cursor/tasks.json`
