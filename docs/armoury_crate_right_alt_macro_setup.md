# Armoury Crate Macro Setup - Right Alt Key

**Purpose**: Configure Armoury Crate macro to execute @RETRY_MANAGER processing and trigger voice input when Right Alt is pressed

---

## Overview

Armoury Crate macros can:
- ✅ Execute programs/scripts
- ✅ Send key combinations
- ✅ Create complex multi-action sequences
- ✅ Be assigned to specific keys (like Right Alt)

This is a **better solution** than PowerToys for ASUS laptop users since:
- Direct script execution (no need for shortcuts)
- Hardware-level key remapping
- Integrated with ASUS keyboard controls
- Can combine multiple actions in one macro

---

## Setup Instructions

### Step 1: Run Setup Script

```powershell
powershell -ExecutionPolicy Bypass -File scripts\python\setup_armoury_crate_right_alt_macro.ps1
```

This creates:
- Batch files for Armoury Crate to execute
- PowerShell scripts for retry processing and voice input
- Combined script that does both

### Step 2: Open Armoury Crate

1. Open **Armoury Crate** (usually in system tray or Start Menu)
2. Navigate to **"Device"** → **"Keyboard"** → **"Macro"**
3. Click **"Create New Macro"** or **"+"** button

### Step 3: Configure Macro

#### Option A: Simple - Execute Combined Script (Recommended)

1. **Macro Name**: `Right Alt - Retry + Voice Input`
2. **Assign Key**: Click **"Right Alt"** key on keyboard diagram
3. **Add Action**: Click **"+"** → Select **"Execute Program"**
4. **Browse**: Navigate to:
   ```
   scripts\python\trigger_retry_and_voice.bat
   ```
5. **Save**: Click **"Save"** or **"OK"**

#### Option B: Multi-Action Macro (More Control)

1. **Macro Name**: `Right Alt - Retry + Voice Input`
2. **Assign Key**: Click **"Right Alt"** key
3. **Add Actions** (in sequence):
   
   **Action 1: Execute Retry Processing**
   - Type: **"Execute Program"**
   - Program: `scripts\python\trigger_retry_processing.bat`
   - Delay: **0ms** (or 100ms if needed)
   
   **Action 2: Send Voice Input Keys**
   - Type: **"Send Keys"** or **"Key Combination"**
   - Keys: **Ctrl + Shift + V**
   - Delay: **100ms** (after retry processing starts)
   
4. **Save**: Click **"Save"** or **"OK"**

#### Option C: Voice Input Only

1. **Macro Name**: `Right Alt - Voice Input`
2. **Assign Key**: **Right Alt**
3. **Add Action**: **"Send Keys"** → **Ctrl + Shift + V**
4. **Save**

---

## Testing

### Test Voice Input:
1. Open **Cursor IDE**
2. Press **Right Alt**
3. Voice input should activate

### Test Retry Processing:
1. Check console output (if visible)
2. Or check logs: `data\diagnostics\request_id_tracking_*.json`
3. Or check connection error logs: `data\connection_errors\error_*.json`

### Test Combined:
1. Press **Right Alt** in Cursor IDE
2. Both retry processing and voice input should activate
3. Retry processing runs in background (hidden window)

---

## Macro Configuration Details

### Recommended Settings:

- **Trigger**: **Right Alt** (single press)
- **Mode**: **Toggle** or **Hold** (your preference)
- **Delay between actions**: **100ms** (if using multi-action)
- **Execution**: **Background** (for retry processing)

### Advanced Options:

- **Repeat**: Disabled (single execution)
- **Delay**: 100ms between actions
- **Priority**: Normal
- **Profile**: Default or create custom profile

---

## Files Created

1. **`scripts/python/trigger_retry_processing.bat`**
   - Executes retry processing script
   - Can be used standalone or in macro

2. **`scripts/python/trigger_retry_and_voice.bat`**
   - **RECOMMENDED**: Executes both retry + voice input
   - Use this for the macro

3. **`scripts/python/trigger_voice_input.ps1`**
   - Sends Ctrl+Shift+V for voice input
   - Can be used standalone

4. **`scripts/python/trigger_retry_and_voice.ps1`**
   - Combined PowerShell script
   - Executes retry processing in background
   - Triggers voice input

---

## Troubleshooting

### Macro Not Executing
- Check Armoury Crate is running (system tray)
- Verify macro is assigned to correct key
- Check macro is enabled (not disabled)
- Restart Armoury Crate if needed

### Script Not Running
- Verify PowerShell execution policy:
  ```powershell
  Get-ExecutionPolicy
  ```
- If restricted, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- Test batch file manually:
  ```cmd
  scripts\python\trigger_retry_and_voice.bat
  ```

### Voice Input Not Working
- Verify Cursor IDE is active window
- Check Cursor IDE voice input shortcut (should be Ctrl+Shift+V)
- Test voice input manually: Press Ctrl+Shift+V in Cursor IDE

### Retry Processing Not Visible
- Retry processing runs in hidden window (by design)
- Check logs: `data\diagnostics\` and `data\connection_errors\`
- Or modify script to show window (remove `-WindowStyle Hidden`)

---

## Advantages Over PowerToys

✅ **Direct script execution** - No need for shortcuts  
✅ **Hardware-level remapping** - More reliable  
✅ **Multi-action support** - Can combine multiple actions  
✅ **Integrated with ASUS** - Works with other Armoury Crate features  
✅ **Profile support** - Can create different profiles  
✅ **No external dependencies** - Uses built-in ASUS software  

---

## Notes

- **Armoury Crate macros** can execute batch files and programs
- **Right Alt** is now mapped to execute retry processing + voice input
- **Retry processing** runs in background (hidden window)
- **Voice input** activates immediately in Cursor IDE
- **Macro settings** are saved in Armoury Crate profile

---

**Tags**: `#ARMOURY_CRATE` `#MACRO` `#KEYBOARD_REMAP` `@RETRY_MANAGER` `#VOICE_INPUT` `@MANUS` `@LUMINA` `#ASUS`
