# Pip Network Path Issue - Resolved

**Date**: 2026-01-14
**Status**: ✅ **FIXED**
**Tags**: `#PIP` `#NETWORK_PATH` `#FIX` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🚨 Problem

**Issue**: Pip was configured to use network path for cache directory:
```
:env:.cache-dir='\\\\10.17.17.32\\data\\cache\\pip'
```

**Symptoms**:
- Package installations failed with network path errors
- Build wheels failed: `[WinError 67] The network name cannot be found: '\\\\10.17.17.32\\data\\'`
- Affected packages: `pyautogui`, `pygetwindow`, `pyscreeze`, `pytweening`, `mouseinfo`, `pyrect`

**Root Cause**: Pip configuration pointing to non-existent or inaccessible network path.

---

## ✅ Solution

### Root Cause

**User-level environment variable** was set to network path:
```
PIP_CACHE_DIR = \\10.17.17.32\data\cache\pip
```

This environment variable takes precedence over pip.ini configuration.

### Fix Applied

1. **Updated User-level environment variable**:
   ```powershell
   [System.Environment]::SetEnvironmentVariable("PIP_CACHE_DIR", "$env:LOCALAPPDATA\pip\cache", "User")
   ```

2. **Set pip.ini configuration** (backup):
   ```powershell
   .\venv\Scripts\python.exe -m pip config set global.cache-dir "$env:LOCALAPPDATA\pip\cache"
   ```

**Result**: Pip now uses local cache directory: `C:\Users\mlesn\AppData\Local\pip\cache`

**Note**: Restart PowerShell/terminal for environment variable change to take effect in new sessions.

---

## 🔧 Verification

### Check Pip Configuration

```powershell
.\venv\Scripts\python.exe -m pip config list
```

**Expected**: No network path, local cache directory configured

### Check Cache Info

```powershell
.\venv\Scripts\python.exe -m pip cache info
```

**Expected**: Cache directory shows local path

---

## 📋 Permanent Fix

### Pip Configuration File

**Location**: `venv\pip.ini` or user-level pip config

**Configuration**:
```ini
[global]
cache-dir = C:\Users\mlesn\AppData\Local\pip\cache
```

### Environment Variables

**TEMP/TMP**: Already set correctly to local paths:
- `TEMP`: `C:\Users\mlesn\AppData\Local\Temp`
- `TMP`: `C:\Users\mlesn\AppData\Local\Temp`
- `TMPDIR`: `C:\Users\mlesn\AppData\Local\Temp`

---

## 🎯 Prevention

### For Future Installations

**Option 1: Use Local Cache (Recommended)**
```powershell
.\venv\Scripts\python.exe -m pip install <package> --cache-dir "$env:LOCALAPPDATA\pip\cache"
```

**Option 2: Disable Cache**
```powershell
.\venv\Scripts\python.exe -m pip install <package> --no-cache-dir
```

**Option 3: Use Local Temp**
```powershell
$env:TMPDIR = $env:TEMP
$env:TMP = $env:TEMP
$env:TEMP = $env:LOCALAPPDATA + "\Temp"
.\venv\Scripts\python.exe -m pip install <package>
```

---

## ✅ Status

**Before**:
- ❌ Pip cache: `\\10.17.17.32\data\cache\pip` (network path, inaccessible)
- ❌ Package installations failing

**After**:
- ✅ Pip cache: `C:\Users\mlesn\AppData\Local\pip\cache` (local path)
- ✅ Package installations working
- ✅ All dependencies installed successfully

---

## 📝 Notes

- Network path `\\10.17.17.32\data\` doesn't exist or isn't accessible
- Local cache is faster and more reliable
- Configuration is now permanent for this venv

---

**Status**: ✅ **FIXED**
**Pip Cache**: ✅ **USING LOCAL PATH**
**Package Installations**: ✅ **WORKING**
**Tags**: `#PIP` `#NETWORK_PATH` `#FIX` `@LUMINA` `@JARVIS` `#PEAK`
