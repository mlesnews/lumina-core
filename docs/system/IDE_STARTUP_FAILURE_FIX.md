# IDE Startup Failure - Exit Code 64 Fix

**Date**: 2025-01-24  
**Status**: 🔴 **CRITICAL - REPEATED FAILURE**  
**Priority**: HIGHEST - Blocks IDE startup

---

## Problem

**Error Message**:
```
The terminal process "C:\Program Files\PowerShell\7-preview\pwsh.exe -NoProfile & "C:\Program Files\PowerShell\7-preview\pwsh.exe" -ExecutionPolicy Bypass -NoProfile -File "C:\Users\mlesn\Dropbox\my_projects\cedarbrook-financial-services_llc-env\scripts\powershell\direct_fix_mcp.ps1"" terminated with exit code: 64.
```

**Root Cause**: 
The command is **malformed** - it's trying to run:
```
pwsh.exe -NoProfile & pwsh.exe -ExecutionPolicy Bypass -NoProfile -File "path\to\direct_fix_mcp.ps1"
```

The `&` is being interpreted as a command separator, causing the first `pwsh.exe -NoProfile` to run without arguments, which fails with exit code 64.

**Correct Command Should Be**:
```
pwsh.exe -ExecutionPolicy Bypass -NoProfile -File "C:\Users\mlesn\Dropbox\my_projects\cedarbrook-financial-services_llc-env\scripts\powershell\direct_fix_mcp.ps1"
```

---

## Where This Is Configured

The malformed command is likely configured in one of these locations:

1. **VS Code/Cursor Settings** (`settings.json`):
   - `terminal.integrated.profiles.windows`
   - `terminal.integrated.automationProfile.windows`
   - `terminal.integrated.shellArgs.windows`

2. **Task Configuration** (`.vscode/tasks.json` or `.cursor/tasks.json`):
   - Task that runs on startup
   - Task with `"runOn": "folderOpen"`

3. **PowerShell Profile** (`$PROFILE`):
   - Profile script that runs on startup
   - May be calling the script incorrectly

4. **Extension Configuration**:
   - Extension that runs scripts on startup
   - MCP-related extension

---

## Solution

### Step 1: Find the Configuration

Search for the malformed command in:

```powershell
# Search VS Code settings
Get-Content "$env:APPDATA\Code\User\settings.json" | Select-String "direct_fix_mcp"

# Search Cursor settings
Get-Content "$env:APPDATA\Cursor\User\settings.json" | Select-String "direct_fix_mcp"

# Search workspace settings
Get-ChildItem -Path "C:\Users\mlesn\Dropbox\my_projects" -Recurse -Filter "settings.json" | Select-String "direct_fix_mcp"

# Search tasks.json
Get-ChildItem -Path "C:\Users\mlesn\Dropbox\my_projects" -Recurse -Filter "tasks.json" | Select-String "direct_fix_mcp"
```

### Step 2: Fix the Command

**Find this (WRONG)**:
```json
{
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "path": "C:\\Program Files\\PowerShell\\7-preview\\pwsh.exe",
      "args": ["-NoProfile", "&", "\"C:\\Program Files\\PowerShell\\7-preview\\pwsh.exe\"", "-ExecutionPolicy", "Bypass", "-NoProfile", "-File", "\"C:\\Users\\mlesn\\Dropbox\\my_projects\\cedarbrook-financial-services_llc-env\\scripts\\powershell\\direct_fix_mcp.ps1\""]
    }
  }
}
```

**Replace with this (CORRECT)**:
```json
{
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "path": "C:\\Program Files\\PowerShell\\7-preview\\pwsh.exe",
      "args": ["-ExecutionPolicy", "Bypass", "-NoProfile", "-File", "C:\\Users\\mlesn\\Dropbox\\my_projects\\cedarbrook-financial-services_llc-env\\scripts\\powershell\\direct_fix_mcp.ps1"]
    }
  }
}
```

**Or in tasks.json (WRONG)**:
```json
{
  "type": "shell",
  "command": "pwsh.exe -NoProfile & \"pwsh.exe\" -ExecutionPolicy Bypass -NoProfile -File \"path\\to\\direct_fix_mcp.ps1\""
}
```

**Replace with (CORRECT)**:
```json
{
  "type": "shell",
  "command": "pwsh.exe",
  "args": [
    "-ExecutionPolicy",
    "Bypass",
    "-NoProfile",
    "-File",
    "C:\\Users\\mlesn\\Dropbox\\my_projects\\cedarbrook-financial-services_llc-env\\scripts\\powershell\\direct_fix_mcp.ps1"
  ]
}
```

### Step 3: Alternative - Disable Startup Script

If the script isn't critical for startup, disable it:

**Option A: Remove from terminal profile**
- Remove the script from `terminal.integrated.profiles.windows`
- Run script manually when needed

**Option B: Make script optional**
- Add error handling to script to exit gracefully
- Check if conditions are met before running

**Option C: Run as background task**
- Don't run in terminal on startup
- Run as background process instead

---

## Prevention

### 1. Validate Commands Before Adding

Always test commands in terminal before adding to configuration:

```powershell
# Test the command
pwsh.exe -ExecutionPolicy Bypass -NoProfile -File "C:\Users\mlesn\Dropbox\my_projects\cedarbrook-financial-services_llc-env\scripts\powershell\direct_fix_mcp.ps1"
```

### 2. Use Proper JSON Formatting

When adding to `settings.json` or `tasks.json`:
- Use `args` array instead of string concatenation
- Don't use `&` in command strings
- Escape paths properly

### 3. Add Error Handling to Scripts

Ensure `direct_fix_mcp.ps1` has proper error handling:

```powershell
# At start of script
$ErrorActionPreference = "Stop"

# Trap unhandled errors
trap {
    Write-Host "Script error: $_" -ForegroundColor Red
    exit 1  # Use 1 for expected errors, not 64
}

# Validate prerequisites
if (-not (Test-Path $ConfigPath)) {
    Write-Host "Config path not found: $ConfigPath" -ForegroundColor Yellow
    exit 0  # Exit gracefully if not needed
}
```

### 4. Make Startup Scripts Optional

Don't make critical startup scripts required:
- Check if conditions are met
- Exit gracefully if not needed
- Log what happened

---

## Quick Fix Script

Create `scripts/python/fix_ide_startup_command.py`:

```python
#!/usr/bin/env python3
"""Fix malformed IDE startup command"""

import json
import sys
from pathlib import Path

def fix_settings_json(settings_path: Path):
    """Fix settings.json with malformed command"""
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = json.load(f)
    
    fixed = False
    
    # Fix terminal profiles
    if "terminal.integrated.profiles.windows" in settings:
        profiles = settings["terminal.integrated.profiles.windows"]
        for profile_name, profile_config in profiles.items():
            if isinstance(profile_config, dict) and "args" in profile_config:
                args = profile_config["args"]
                # Check for malformed command with &
                if "&" in args or (len(args) > 0 and "&" in str(args)):
                    # Remove & and fix command
                    fixed_args = [arg for arg in args if arg != "&"]
                    # Remove duplicate pwsh.exe if present
                    if fixed_args and "pwsh.exe" in str(fixed_args[0]):
                        # Keep only the file path and proper args
                        fixed_args = [
                            "-ExecutionPolicy", "Bypass",
                            "-NoProfile",
                            "-File",
                            "C:\\Users\\mlesn\\Dropbox\\my_projects\\cedarbrook-financial-services_llc-env\\scripts\\powershell\\direct_fix_mcp.ps1"
                        ]
                    profile_config["args"] = fixed_args
                    fixed = True
    
    if fixed:
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        print(f"✅ Fixed {settings_path}")
        return True
    else:
        print(f"ℹ️  No issues found in {settings_path}")
        return False

if __name__ == "__main__":
    # Check common locations
    appdata = Path.home() / "AppData" / "Roaming"
    
    locations = [
        appdata / "Code" / "User" / "settings.json",
        appdata / "Cursor" / "User" / "settings.json",
    ]
    
    fixed_any = False
    for location in locations:
        if location.exists():
            if fix_settings_json(location):
                fixed_any = True
    
    if not fixed_any:
        print("⚠️  No settings.json files found or no issues detected")
        print("   Please check your IDE settings manually")
        sys.exit(1)
    else:
        print("\n✅ Fixed IDE startup command!")
        print("   Please restart your IDE for changes to take effect")
```

---

## Immediate Action

1. **Stop IDE startup failures**:
   - Find and fix the malformed command
   - Or disable the startup script temporarily

2. **Run fix script** (when created):
   ```bash
   python scripts/python/fix_ide_startup_command.py
   ```

3. **Manual fix**:
   - Open IDE settings
   - Search for "direct_fix_mcp"
   - Remove the `&` and duplicate `pwsh.exe`
   - Use proper `args` array format

4. **Verify**:
   - Restart IDE
   - Check that startup completes without errors
   - Verify terminal works correctly

---

## Related Files

- `scripts/powershell/direct_fix_mcp.ps1` - The script being called
- `docs/TASK_ERROR_FIXES.md` - Previous error fixes
- `docs/system/UNIVERSAL_IDE_NOTIFICATION_HANDLING.md` - Related documentation
- `docs/system/KNOWN_ISSUES.md` - Known issues tracking

---

## Status

- 🔴 **CRITICAL**: Startup failures occurring repeatedly
- ⏳ **IN PROGRESS**: Fix script being created
- 📝 **ACTION REQUIRED**: Find and fix malformed command in IDE settings

---

**Last Updated**: 2025-01-24

