# AI Venv Integration - Complete Setup

## Overview
Complete integration to ensure the AI assistant uses venv for all Python commands and terminal executions.

## What Was Implemented

### 1. PowerShell Profile Updates
**File**: `C:\Users\mlesn\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`

**New Functions**:
- `Ensure-VenvForAI` - Ensures venv is activated for AI commands
- `Invoke-PythonWithVenv` - Runs Python commands with venv automatically
- Alias `pyvenv` - Shortcut for `Invoke-PythonWithVenv`

**Usage**:
```powershell
# Automatic activation on PowerShell startup
# Manual activation
Ensure-VenvForAI

# Run Python with venv
pyvenv scripts/python/your_script.py
```

### 2. Helper Scripts Created

#### `scripts/python/ai_command_wrapper.ps1`
Wrapper script for AI commands that ensures venv is activated:
```powershell
. scripts/python/ai_command_wrapper.ps1 -Command "python scripts/python/your_script.py"
```

#### `scripts/python/run_with_venv.py`
Python wrapper that finds and uses venv Python:
```bash
python scripts/python/run_with_venv.py scripts/python/your_script.py
```

#### `scripts/setup/ensure_venv_for_ai.ps1`
Standalone script to ensure venv is activated:
```powershell
. scripts/setup/ensure_venv_for_ai.ps1
```

### 3. .cursorrules Updates
Added mandatory venv usage guidelines for the AI assistant:
- **CRITICAL**: AI MUST use venv for all Python commands
- Standard patterns provided for AI command execution
- Multiple implementation options documented

## How the AI Should Use Venv

### Pattern 1: Check and Activate (Recommended)
```powershell
# Check if venv is activated
if (-not $env:VIRTUAL_ENV) {
    & "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv\Scripts\Activate.ps1"
}
python scripts/python/your_script.py
```

### Pattern 2: Use Wrapper Script
```powershell
. scripts/python/ai_command_wrapper.ps1 -Command "python scripts/python/your_script.py"
```

### Pattern 3: Direct Venv Python Path
```powershell
& "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv\Scripts\python.exe" scripts/python/your_script.py
```

### Pattern 4: Use PowerShell Function
```powershell
pyvenv scripts/python/your_script.py
```

## Automatic Activation

### PowerShell Profile
The PowerShell profile automatically:
- Activates venv on PowerShell startup
- Activates venv when entering `.lumina` directory
- Provides helper functions for manual activation

### AI Commands
The AI should:
1. **ALWAYS** check `$env:VIRTUAL_ENV` before running Python commands
2. **ALWAYS** activate venv if not already activated
3. Use one of the standard patterns provided

## Verification

### Check Venv Status
```powershell
# Check if venv is activated
$env:VIRTUAL_ENV

# Check Python executable
python -c "import sys; print(sys.executable)"
```

The Python executable should point to:
- Windows: `venv\Scripts\python.exe`
- Unix: `venv/bin/python`

## Files Created/Modified

1. **PowerShell Profile**: `C:\Users\mlesn\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`
   - Added `Ensure-VenvForAI` function
   - Added `Invoke-PythonWithVenv` function
   - Added `pyvenv` alias

2. **Helper Scripts**:
   - `scripts/python/ai_command_wrapper.ps1`
   - `scripts/python/run_with_venv.py`
   - `scripts/setup/ensure_venv_for_ai.ps1`

3. **Documentation**:
   - `docs/setup/ai_venv_usage.md`
   - `docs/setup/ai_venv_integration_complete.md`

4. **Rules**:
   - `.cursorrules` - Added mandatory venv usage guidelines

## Next Steps

1. **Create venv** (if not exists):
   ```powershell
   cd C:\Users\mlesn\Dropbox\my_projects\.lumina
   python -m venv venv
   ```

2. **Install dependencies** (when venv is created):
   ```powershell
   . venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **Test venv activation**:
   ```powershell
   . $PROFILE
   Ensure-VenvForAI
   python -c "import sys; print(sys.executable)"
   ```

## Status

✅ **PowerShell Profile**: Updated with venv functions
✅ **Helper Scripts**: Created and ready
✅ **Documentation**: Complete
✅ **Rules**: Updated with mandatory venv usage
✅ **AI Integration**: Ready for use

The AI will now automatically use venv for all Python commands when following the documented patterns.
