# Right Alt → @DOIT + Enter Macro

**Macro Button:** Right Alt (R-ALT)  
**Function:** Types "@DOIT" + Enter (Return/Send button)

## Quick Start

```powershell
.\scripts\startup\START_RIGHT_ALT_DOIT_MACRO.ps1
```

## Available Software

### ✅ AutoHotkey (Preferred)
- **Location:**** `C:\Users\mlesn\AppData\Local\Microsoft\WindowsApps\AutoHotkey.exe`
- **Status:** ✅ Available
- **Script:** `data/manus_shortcuts/right_alt_doit.ahk`
- **Method:** System-wide, low-level keyboard hook

### ✅ Python (Fallback)
- **Libraries:** `keyboard`, `pyautogui`
- **Status:** ✅ Available
- **Script:** `scripts/python/right_alt_doit_remap.py`
- **Method:** Python-based keyboard automation

## How It Works

### AutoHotkey Method (Preferred)

**Script:** `data/manus_shortcuts/right_alt_doit.ahk`

```autohotkey
RAlt::
    Send, @DOIT{Enter}
    return
```

**Features:**
- System-wide (works in all applications)
- Low-level keyboard hook
- Minimal resource usage
- Instant response

### Python Method (Fallback)

**Script:** `scripts/python/right_alt_doit_remap.py`

**Features:**
- Cross-platform compatible
- More flexible for complex macros
- Requires Python libraries

## Installation

### AutoHotkey (Recommended)

1. **Check if installed:**
   ```powershell
   Get-Command autohotkey
   ```

2. **If not installed, download:**
   - https://www.autohotkey.com/
   - Install AutoHotkey v2 (or v1.1)

3. **Start macro:**
   ```powershell
   .\scripts\startup\START_RIGHT_ALT_DOIT_MACRO.ps1
   ```

### Python Method

1. **Install libraries:**
   ```powershell
   pip install keyboard pyautogui
   ```

2. **Start macro:**
   ```powershell
   python scripts\python\right_alt_doit_remap.py
   ```

## Usage

1. **Start the macro** (see Quick Start above)
2. **Press Right Alt** in any application
3. **Result:** "@DOIT" is typed + Enter is pressed automatically

## Troubleshooting

### Right Alt doesn't work

**Solutions:**
1. Try Right Alt + Space
2. Check if another program is using Right Alt
3. Restart the macro script
4. Use AutoHotkey method (more reliable)

### Macro not typing

**Solutions:**
1. Check if macro is running:
   ```powershell
   Get-Process -Name "AutoHotkey" -ErrorAction SilentlyContinue
   Get-Process python | Where-Object { $_.CommandLine -like "*right_alt*" }
   ```

2. Check permissions (may need admin for system-wide hooks)

3. Try Python method if AutoHotkey fails

### Alternative Key Combinations

If Right Alt conflicts with other software, edit the script:

**AutoHotkey:**
```autohotkey
; Change to Ctrl+Right Alt
^RAlt::
    Send, @DOIT{Enter}
    return
```

**Python:**
Edit `right_alt_doit_remap.py` to use different key

## Auto-Start on Boot

To start automatically on Windows login:

1. **Create shortcut** to `START_RIGHT_ALT_DOIT_MACRO.ps1`
2. **Place in Startup folder:**
   ```
   %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
   ```

Or use Task Scheduler to run on login.

## Status

- ✅ AutoHotkey: Available
- ✅ Python libraries: Available
- ✅ Scripts: Created
- ✅ Documentation: Complete

---

**Last Updated:** 2026-01-10
