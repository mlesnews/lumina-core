# Environment Issues Fixed

## Overview
Documentation of environment issues found and fixed related to venv usage.

## Issues Found

### 1. Not Using Venv
**Status**: ❌ **ISSUE FOUND**
- **Current**: Using system Python (`C:\Users\mlesn\AppData\Local\Programs\Python\Python311\python.exe`)
- **Should be**: Using venv Python (`venv\Scripts\python.exe`)
- **Impact**: Scripts may use wrong Python version or packages

### 2. No Venv Created
**Status**: ⚠️ **WARNING**
- **Issue**: No venv directory exists in project root
- **Solution**: Create venv with `python -m venv venv`

### 3. Scripts Using Hardcoded "python"
**Status**: ✅ **FIXED**
- **Files Fixed**:
  - `scripts/python/hybrid_framework_end2end_workflow.py` - Changed to `sys.executable`
  - `scripts/python/manus_mcp_key_vault_wrapper.py` - Changed to `sys.executable`
- **Note**: `execute_nas_migration.py` already uses `sys.executable` ✅

## Fixes Applied

### 1. Script Updates
All scripts that used hardcoded `"python"` in subprocess calls have been updated to use `sys.executable`:
- Ensures same Python environment is used
- Respects venv if activated
- More reliable across environments

### 2. Environment Diagnostics
Created `scripts/python/check_environment_issues.py`:
- Diagnoses environment issues
- Checks venv usage
- Provides recommendations

### 3. Shell Selection Guide
Created `docs/setup/shell_selection_guide.md`:
- Guidance on PowerShell vs Bash/Korn
- When to use each shell
- Best practices

## Current Status

### Environment
- ❌ **Not using venv** (system Python)
- ⚠️ **No venv exists** (needs to be created)
- ✅ **Scripts fixed** (use `sys.executable`)

### Shell Usage
- ✅ **PowerShell**: Primary shell (venv support, Windows integration)
- ✅ **Bash/Korn**: Secondary (Docker/Linux operations)
- ✅ **Guidance**: Documented in shell selection guide

## Recommendations

### Immediate Actions
1. **Create venv**:
   ```powershell
   cd C:\Users\mlesn\Dropbox\my_projects\.lumina
   python -m venv venv
   ```

2. **Activate venv**:
   ```powershell
   . venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

### Long-term
1. **Always use venv** for Python development
2. **Use PowerShell** for Windows operations (default)
3. **Use Bash/Korn** only for Docker/Linux operations
4. **Check environment** regularly with `check_environment_issues.py`

## Verification

Run environment check:
```powershell
python scripts/python/check_environment_issues.py
```

Expected output after venv is created and activated:
- ✅ Using virtual environment
- ✅ Venv found
- ✅ No issues

## Files Modified

1. `scripts/python/hybrid_framework_end2end_workflow.py`
   - Changed `["python", "--version"]` to `[sys.executable, "--version"]`

2. `scripts/python/manus_mcp_key_vault_wrapper.py`
   - Changed `["python", "-m", "elevenlabs_mcp"]` to `[sys.executable, "-m", "elevenlabs_mcp"]`

3. `scripts/python/check_environment_issues.py` (NEW)
   - Environment diagnostics tool

4. `docs/setup/shell_selection_guide.md` (NEW)
   - Shell selection guidance

5. `docs/setup/environment_issues_fixed.md` (THIS FILE)
   - Documentation of fixes

6. `.cursorrules`
   - Added shell selection guidelines

## Next Steps

1. Create venv when ready
2. Activate venv in PowerShell profile (already configured)
3. Install project dependencies
4. Verify with environment check script
5. Continue using PowerShell for Windows operations
6. Use Bash/Korn only when needed (Docker/Linux)
