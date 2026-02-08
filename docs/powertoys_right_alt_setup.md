# PowerToys Right Alt Remap Setup

**Purpose**: Map Right Alt key to execute @RETRY_MANAGER processing and trigger voice input in Cursor IDE

---

## Overview

PowerToys Keyboard Manager can remap keys, but it **cannot directly execute scripts**. We'll use a two-part approach:

1. **Remap Right Alt → Ctrl+Shift+V** (for voice input in Cursor IDE)
2. **Use PowerToys Run** (Alt+Space) to trigger retry processing script

---

## Setup Instructions

### Step 1: Open PowerToys Settings

1. Press **Windows Key + I** (Settings)
2. Search for **"PowerToys"**
3. Click **"PowerToys"** in results
4. Or right-click the **PowerToys icon** in system tray → **Settings**

### Step 2: Configure Keyboard Manager

1. In PowerToys Settings, click **"Keyboard Manager"** in left sidebar
2. Click **"Remap a key"** button
3. Click **"+"** to add new remap

### Step 3: Remap Right Alt to Ctrl+Shift+V

**Remap Configuration:**
- **Key to remap**: `Right Alt`
- **Mapped to**: `Ctrl` + `Shift` + `V`

**Steps:**
1. Click **"Type"** under "Key to remap"
2. Press **Right Alt** key
3. Click **"Type"** under "Mapped to"
4. Press **Ctrl + Shift + V** (or select from dropdown)
5. Click **"OK"**
6. Click **"OK"** to save

### Step 4: Test Voice Input

1. Open **Cursor IDE**
2. Press **Right Alt**
3. Voice input should activate (Ctrl+Shift+V)

---

## Retry Processing Setup

Since PowerToys Keyboard Manager cannot execute scripts directly, use **PowerToys Run**:

### Option 1: PowerToys Run (Recommended)

1. Press **Alt + Space** (PowerToys Run)
2. Type: **"retry"** or **"LUMINA Retry Processing"**
3. Press **Enter** to execute

### Option 2: Create Windows Shortcut

A shortcut has been created at:
```
%APPDATA%\Microsoft\Windows\Start Menu\Programs\LUMINA Retry Processing.lnk
```

You can:
- Pin to Start Menu
- Pin to Taskbar
- Add to PowerToys Run index
- Create a custom keyboard shortcut in PowerToys

### Option 3: PowerToys Shortcut Guide

1. Hold **Windows Key** to see all shortcuts
2. Look for **"LUMINA Retry Processing"** in Start Menu
3. Click to execute

---

## Alternative: Use PowerToys Run for Both

If you prefer to use PowerToys Run for everything:

1. **Right Alt → Voice Input**: Already configured (Ctrl+Shift+V)
2. **Alt+Space → Type "retry"**: Triggers retry processing

This gives you:
- **Right Alt**: Voice input (immediate)
- **Alt+Space → "retry"**: Retry processing (when needed)

---

## Files Created

1. **`scripts/python/trigger_retry_processing.ps1`**
   - PowerShell script to execute retry processing
   - Can be run directly or via shortcut

2. **`scripts/python/setup_powertoys_right_alt_remap.ps1`**
   - Setup script (creates shortcut)
   - Run this to set up the shortcut

3. **`config/powertoys_keyboard_remap.json`**
   - Configuration reference
   - Documents the remap setup

---

## Testing

### Test Voice Input:
1. Open Cursor IDE
2. Press **Right Alt**
3. Voice input should activate

### Test Retry Processing:
1. Press **Alt + Space** (PowerToys Run)
2. Type: **"retry"**
3. Press **Enter**
4. Check console output for retry processing status

---

## Troubleshooting

### PowerToys Not Found
- Install from: https://github.com/microsoft/PowerToys/releases
- Or install via Microsoft Store

### Remap Not Working
- Ensure PowerToys is running (check system tray)
- Restart PowerToys if needed
- Check Keyboard Manager is enabled in PowerToys settings

### Script Not Executing
- Verify PowerShell execution policy: `Get-ExecutionPolicy`
- If restricted, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Or run script manually to test

---

## Notes

- **PowerToys Keyboard Manager** can only remap keys, not execute scripts
- **PowerToys Run** (Alt+Space) can execute scripts via shortcuts
- **Right Alt** is now mapped to **Ctrl+Shift+V** for voice input
- **Retry processing** is available via **PowerToys Run** or shortcut

---

**Tags**: `#POWERTOYS` `#KEYBOARD_REMAP` `@RETRY_MANAGER` `#VOICE_INPUT` `@MANUS` `@LUMINA`
