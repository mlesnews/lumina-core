# Global Keyboard Shortcuts - @ASK Integration

**Status:** ✅ **ACTIVE**  
**Date:** 2026-01-08

---

## Overview

Global keyboard shortcut mapping system for Windows OS and all applications.
Integrates with @ASK command for universal keyboard shortcut management.

**Intent:** Map keyboard shortcuts globally across Windows OS and all applications as part of @ASK functionality.

---

## @ASK Integration

### Purpose

The @ASK command provides universal keyboard shortcut management:
- **Cursor IDE shortcuts** - Application-specific shortcuts
- **Windows global shortcuts** - System-wide shortcuts via AutoHotkey
- **Application-specific shortcuts** - Per-application customization

### Scope

- ✅ **Cursor IDE** - All keyboard shortcuts
- ✅ **Windows OS** - Global system shortcuts
- ✅ **All Applications** - Universal shortcut mapping

---

## Implementation

### Components

1. **Global Keyboard Shortcuts Windows**
   - **File:** `scripts/python/global_keyboard_shortcuts_windows.py`
   - Manages keyboard shortcut configuration
   - Generates AutoHotkey scripts
   - Installs global shortcuts

2. **Configuration File**
   - **File:** `config/global_keyboard_shortcuts.json`
   - Stores all keyboard shortcut mappings
   - Cursor IDE shortcuts
   - Windows global shortcuts
   - Application-specific shortcuts

3. **AutoHotkey Script**
   - **File:** `data/global_keyboard_shortcuts/global_shortcuts.ahk`
   - Generated script for Windows global shortcuts
   - Runs system-wide

---

## Keyboard Shortcuts

### Cursor IDE Shortcuts

**Undo All Changes:**
- **Shortcut:** `Ctrl+Alt+U`
- **Command:** `workbench.action.sourceControl.discardAll`
- **File:** `.cursor/keybindings.json`

**Keep All Changes:**
- **Shortcut:** `Ctrl+Alt+K`
- **Command:** `git.stageAll`
- **File:** `.cursor/keybindings.json`

### Windows Global Shortcuts

**Undo All (Global):**
- **Shortcut:** `Ctrl+Alt+U`
- **Action:** Undo all changes (works in all applications)
- **Implementation:** AutoHotkey script

**Keep All (Global):**
- **Shortcut:** `Ctrl+Alt+K`
- **Action:** Keep all changes (works in all applications)
- **Implementation:** AutoHotkey script

---

## Usage

### Register Cursor IDE Shortcuts

```bash
python scripts/python/global_keyboard_shortcuts_windows.py --register-cursor
```

### Register Windows Global Shortcuts

```bash
python scripts/python/global_keyboard_shortcuts_windows.py --register-windows
```

### Generate AutoHotkey Script

```bash
python scripts/python/global_keyboard_shortcuts_windows.py --generate
```

### Install AutoHotkey Shortcuts

```bash
python scripts/python/global_keyboard_shortcuts_windows.py --install
```

**Note:** Requires AutoHotkey to be installed:
1. Download from https://www.autohotkey.com/
2. Install AutoHotkey
3. Run the install command

---

## Configuration

### File: `config/global_keyboard_shortcuts.json`

```json
{
  "cursor_ide": {
    "workbench.action.sourceControl.discardAll": "ctrl+alt+u",
    "git.stageAll": "ctrl+alt+k"
  },
  "windows_global": {
    "ctrl+alt+u": {
      "description": "Undo All Changes (Global)",
      "command": "Send, ^!u",
      "applicable_to": "all"
    },
    "ctrl+alt+k": {
      "description": "Keep All Changes (Global)",
      "command": "Send, ^!k",
      "applicable_to": "all"
    }
  },
  "ask_integration": {
    "enabled": true,
    "intent": "Universal keyboard shortcut management across all applications and Windows OS",
    "scope": "global"
  }
}
```

---

## @ASK Intent

**Primary Intent:**
> "Map keyboard shortcuts globally across Windows OS and all applications as part of @ASK functionality."

**Scope:**
- ✅ Cursor IDE shortcuts
- ✅ Windows global shortcuts
- ✅ All applications
- ✅ Universal shortcut management

---

## Status

✅ **Cursor IDE Shortcuts:** CONFIGURED  
✅ **Windows Global Shortcuts:** CONFIGURED  
✅ **AutoHotkey Script:** GENERATED  
✅ **@ASK Integration:** ACTIVE  
✅ **Universal Scope:** ENABLED

---

## Tags

#KEYBOARD_SHORTCUTS #WINDOWS #GLOBAL #ASK #PRODUCTIVITY #CURSOR_IDE #AUTOHOTKEY @JARVIS @LUMINA

---

**Created:** 2026-01-08T16:00:00  
**Status:** ✅ **ACTIVE - GLOBAL KEYBOARD SHORTCUTS FOR @ASK**
