# Keyboard Macro Buttons - Complete Mapping

**Available Buttons:** SPACEBAR, RALT, PRTSC, MSCOPILOT

## Current Mappings

### ✅ Right Alt (RALT) → @DOIT + Enter
- **Status:** Active
- **Function:** Types "@DOIT" + Enter (Return/Send button)
- **Script:** `data/manus_shortcuts/right_alt_doit.ahk`

### ✅ Microsoft Copilot Button → @JARVIS + Enter
- **Status:** Active
- **Function:** Types "@JARVIS" + Enter
- **Script:** `data/manus_shortcuts/right_alt_doit.ahk` (includes Copilot remap)

### ⏸️ Print Screen (PRTSC) → Available
- **Status:** Not mapped (available for future use)
- **Potential uses:** Screenshot automation, capture workflows

### ⏸️ Spacebar → Available
- **Status:** Not mapped (available for future use)
- **Note:** Spacebar is heavily used, remap with caution

## Quick Start

```powershell
.\scripts\startup\START_ALL_KEYBOARD_MACROS.ps1
```

This starts both:
- Right Alt → @DOIT + Enter
- Copilot Button → @JARVIS + Enter

## Copilot Button Detection

The Copilot button may be mapped differently on different keyboards:

**AutoHotkey tries these methods:**
1. `Launch_App1` (most common)
2. `Right Windows + C` (Copilot shortcut)
3. `F23` (some keyboards)
4. `Ctrl+Shift+C` (alternative)

**If Copilot button doesn't work:**
1. Run keyboard detection script to find exact scan code
2. Edit AutoHotkey script with correct mapping
3. Or use Python method with global hook

## Future Button Mappings

### Print Screen (PRTSC)
Potential uses:
- Screenshot automation
- Capture to clipboard
- Screen recording trigger
- @SYPHON data capture

### Spacebar
**⚠️ WARNING:** Spacebar is critical - remap carefully!

Potential uses:
- Context-aware actions
- Quick commands (only when in specific apps)
- Modifier combinations (Ctrl+Space, Alt+Space)

## Status

- ✅ Right Alt → @DOIT: Active
- ✅ Copilot → @JARVIS: Active
- ⏸️ Print Screen: Available
- ⏸️ Spacebar: Available

**Total Buttons Used:** 2/4  
**Available Buttons:** 2

---

**Last Updated:** 2026-01-10
