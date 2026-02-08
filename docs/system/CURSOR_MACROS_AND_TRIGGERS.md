# Cursor IDE Macros, Triggers, and Hooks Setup

**Date**: 2026-01-02  
**Status**: ✅ **CONFIGURED**  
**Tag**: #CURSOR #MACROS #TRIGGERS #KEYBINDINGS

---

## Overview

Cursor IDE supports macros, triggers, and hooks through:
- **Tasks** (`.cursor/tasks.json`) - Automated scripts
- **Keybindings** (`.cursor/keybindings.json`) - Keyboard shortcuts
- **Settings** (`.cursor/settings.json`) - Configuration hooks

---

## Configured Macros & Tasks

### 1. Screenshot Capture Tasks

#### Quick Screenshot
- **Task**: `MANUS: Quick Screenshot`
- **Shortcut**: `Ctrl+Shift+S`
- **Action**: Captures screenshot immediately
- **Use**: When you need a quick screenshot

#### Screenshot with Context
- **Task**: `MANUS: Capture Screenshot with Context`
- **Shortcut**: `Ctrl+Shift+C`
- **Action**: Prompts for context description, then captures
- **Use**: When you want to document what you're capturing

#### Full Screenshot
- **Task**: `MANUS: Capture Screenshot`
- **Shortcut**: `Ctrl+Alt+S`
- **Action**: Full screenshot capture
- **Use**: Standard screenshot capture

### 2. LDAP/SSO Tasks

#### Troubleshoot LDAP Auth
- **Task**: `LDAP: Troubleshoot Authentication`
- **Action**: Runs troubleshooting guide for LDAP errors
- **Use**: When getting authentication errors

#### Verify SSO Readiness
- **Task**: `SSO: Verify Readiness`
- **Action**: Checks SSO configuration status
- **Use**: Before or after SSO setup

#### Setup SAML SSO
- **Task**: `SSO: Setup SAML`
- **Action**: Shows SAML SSO setup guide
- **Use**: When setting up SAML SSO

---

## Keyboard Shortcuts

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl+Shift+S` | Quick Screenshot | Fast screenshot capture |
| `Ctrl+Shift+C` | Screenshot with Context | Capture with description |
| `Ctrl+Alt+S` | Full Screenshot | Standard screenshot |

---

## How to Use

### Method 1: Keyboard Shortcuts

1. **Press `Ctrl+Shift+S`** for quick screenshot
2. **Press `Ctrl+Shift+C`** for screenshot with context (will prompt for description)
3. **Press `Ctrl+Alt+S`** for full screenshot

### Method 2: Command Palette

1. **Press `Ctrl+Shift+P`** (Command Palette)
2. **Type**: `Tasks: Run Task`
3. **Select**: Task name (e.g., "MANUS: Quick Screenshot")

### Method 3: Terminal

```powershell
# Run task from terminal
python scripts/python/manus_rdp_screenshot_capture.py --screenshot
```

---

## Triggers & Hooks

### Automatic Triggers

The screenshot integration automatically triggers when:
- **Error keywords detected** in chat messages
- **Screenshot requested** explicitly
- **"show me"** or **"capture"** mentioned

### Manual Triggers

Use keyboard shortcuts or tasks to trigger manually.

---

## Future Enhancements

### Chat Hooks (Future)
- Monitor Cursor chat in real-time
- Auto-capture on error detection
- Auto-attach screenshots to chat

### File Watchers (Future)
- Watch for error logs
- Auto-capture when errors detected
- Trigger workflows on events

### Extension Integration (Future)
- Cursor extension for screenshot capture
- UI button for quick capture
- Chat integration panel

---

## Configuration Files

### Tasks Configuration
- **File**: `.cursor/tasks.json`
- **Location**: Project root
- **Format**: JSON with task definitions

### Keybindings Configuration
- **File**: `.cursor/keybindings.json`
- **Location**: Project root
- **Format**: JSON with keybinding definitions

### Settings Configuration
- **File**: `.cursor/settings.json`
- **Location**: Project root
- **Format**: JSON with settings

---

## Custom Macros

### Create Custom Task

Add to `.cursor/tasks.json`:

```json
{
  "label": "My Custom Task",
  "type": "shell",
  "command": "python",
  "args": [
    "${workspaceFolder}/scripts/python/my_script.py",
    "${input:myInput}"
  ],
  "inputs": [
    {
      "id": "myInput",
      "type": "promptString",
      "description": "Enter input"
    }
  ]
}
```

### Create Custom Keybinding

Add to `.cursor/keybindings.json`:

```json
{
  "key": "ctrl+shift+m",
  "command": "workbench.action.tasks.runTask",
  "args": "My Custom Task",
  "when": "editorTextFocus"
}
```

---

## Available Tasks

### Screenshot Tasks
- ✅ `MANUS: Quick Screenshot` - Fast capture
- ✅ `MANUS: Capture Screenshot with Context` - With description
- ✅ `MANUS: Capture Screenshot` - Full capture

### LDAP/SSO Tasks
- ✅ `LDAP: Troubleshoot Authentication` - Troubleshooting guide
- ✅ `SSO: Verify Readiness` - Check SSO status
- ✅ `SSO: Setup SAML` - SAML setup guide

### JARVIS Tasks
- ✅ `JARVIS: Auto Git Commit` - Auto commit changes
- ✅ `JARVIS: Health Check` - System health check
- ✅ `JARVIS: Cursor IDE Optimization` - Optimize Cursor
- ✅ `JARVIS: Monitor IDE Notifications` - Monitor notifications

---

## Usage Examples

### Example 1: Quick Screenshot
1. See error in DSM
2. Press `Ctrl+Shift+S`
3. Screenshot captured automatically
4. Path provided for attachment

### Example 2: Screenshot with Context
1. Press `Ctrl+Shift+C`
2. Enter: "DSM LDAP authentication error"
3. Screenshot captured with context
4. Ready for attachment

### Example 3: Troubleshoot Error
1. Get authentication error
2. Press `Ctrl+Shift+P`
3. Type: "LDAP: Troubleshoot"
4. Follow troubleshooting guide

---

## Integration with Chat

### Automatic (When Mentioning Errors)

In Cursor chat:
```
"I'm getting an error"
→ Automatically captures screenshot
```

### Manual (Keyboard Shortcut)

1. Press `Ctrl+Shift+S` (quick screenshot)
2. Screenshot captured
3. Attach to chat message

---

## Troubleshooting

### Issue: Shortcuts Not Working

**Solutions**:
- Check keybindings.json is valid JSON
- Restart Cursor IDE
- Check for conflicting shortcuts
- Verify tasks.json is correct

### Issue: Tasks Not Appearing

**Solutions**:
- Check tasks.json syntax
- Verify file paths are correct
- Check Python is in PATH
- Restart Cursor IDE

### Issue: Screenshot Not Capturing

**Solutions**:
- Check RDP connection is active
- Verify MANUS RDP Screenshot Capture script works
- Check output directory permissions
- Run script manually to test

---

## Advanced: Custom Hooks

### File Watcher Hook (Future)

```json
{
  "watchers": [
    {
      "pattern": "**/*.log",
      "command": "python scripts/python/auto_capture_on_error.py"
    }
  ]
}
```

### Chat Hook (Future)

```json
{
  "chatHooks": [
    {
      "trigger": "error",
      "action": "capture_screenshot"
    }
  ]
}
```

---

**Last Updated**: 2026-01-02  
**Status**: Configured and ready  
**Files**: `.cursor/tasks.json`, `.cursor/keybindings.json`
