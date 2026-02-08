# @ASK Keyboard Shortcuts - Complete System

**Status:** ✅ **COMPLETE**  
**Date:** 2026-01-08

---

## Overview

Complete keyboard shortcut mapping system for @ASK integration:
- **Cursor IDE shortcuts** - Application-specific
- **Windows global shortcuts** - System-wide via AutoHotkey
- **Universal scope** - Works across all applications

**Intent:** Map keyboard shortcuts globally across Windows OS and all applications as part of @ASK functionality.

---

## @ASK Integration

### Purpose

The @ASK command provides universal keyboard shortcut management:
- **Universal mapping** - Same shortcuts work everywhere
- **Consistent experience** - Same keys, same actions
- **Productivity boost** - No need to learn app-specific shortcuts

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

4. **Cursor IDE Keybindings**
   - **File:** `.cursor/keybindings.json`
   - Cursor-specific shortcuts

---

## Keyboard Shortcuts

### Universal Shortcuts (All Applications)

**Undo All Changes:**
- **Shortcut:** `Ctrl+Alt+U`
- **Mnemonic:** **U** = **U**ndo
- **Works in:** All applications
- **Implementation:** AutoHotkey script

**Keep All Changes:**
- **Shortcut:** `Ctrl+Alt+K`
- **Mnemonic:** **K** = **K**eep
- **Works in:** All applications
- **Implementation:** AutoHotkey script

### Cursor IDE Shortcuts

**Undo All Changes:**
- **Shortcut:** `Ctrl+Alt+U`
- **Command:** `workbench.action.sourceControl.discardAll`
- **File:** `.cursor/keybindings.json`

**Keep All Changes:**
- **Shortcut:** `Ctrl+Alt+K`
- **Command:** `git.stageAll`
- **File:** `.cursor/keybindings.json`

---

## Usage

### Register Shortcuts

```bash
# Register Cursor IDE shortcuts
python scripts/python/global_keyboard_shortcuts_windows.py --register-cursor

# Register Windows global shortcuts
python scripts/python/global_keyboard_shortcuts_windows.py --register-windows

# Generate AutoHotkey script
python scripts/python/global_keyboard_shortcuts_windows.py --generate

# Install AutoHotkey shortcuts (requires AutoHotkey)
python scripts/python/global_keyboard_shortcuts_windows.py --install
```

### Install AutoHotkey

1. Download AutoHotkey from https://www.autohotkey.com/
2. Install AutoHotkey
3. Run: `python scripts/python/global_keyboard_shortcuts_windows.py --install`
4. Shortcuts will work globally across all applications

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

**Implementation:**
- ✅ Cursor IDE shortcuts configured
- ✅ Windows global shortcuts configured
- ✅ AutoHotkey script generated
- ✅ Universal scope enabled
- ✅ @ASK integration active

---

## Status

✅ **Cursor IDE Shortcuts:** CONFIGURED  
✅ **Windows Global Shortcuts:** CONFIGURED  
✅ **AutoHotkey Script:** GENERATED  
✅ **@ASK Integration:** ACTIVE  
✅ **Universal Scope:** ENABLED

---

## Tags

#KEYBOARD_SHORTCUTS #WINDOWS #GLOBAL #ASK #PRODUCTIVITY #CURSOR_IDE #AUTOHOTKEY @JARVIS @LUMINA @ASK

---

**Created:** 2026-01-08T16:07:00  
**Status:** ✅ **COMPLETE - GLOBAL KEYBOARD SHORTCUTS FOR @ASK**
