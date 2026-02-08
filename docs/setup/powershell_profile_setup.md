# PowerShell Profile Setup for LUMINA

## Overview
The PowerShell profile automatically activates the virtual environment (venv) and ensures proper startup sequence, including git initialization before other processes.

## Features

1. **Auto-activate venv**: Automatically activates venv when entering the .lumina project directory
2. **Git initialization**: Ensures git is initialized before other processes start (fixes startup sequence warnings)
3. **Project root detection**: Automatically finds and sets the LUMINA project root
4. **Environment variables**: Sets `$env:LUMINA_PROJECT_ROOT` for use in scripts

## Installation

The profile is automatically installed at:
```
C:\Users\mlesn\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

## Manual Setup

If you need to recreate the profile:

```powershell
# Run the setup script
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
powershell -ExecutionPolicy Bypass -File scripts\setup\setup_powershell_profile.ps1

# Reload the profile
. $PROFILE
```

## Functions

### Activate-LuminaVenv
Activates the LUMINA virtual environment. Checks for venv in:
- `venv/`
- `.venv/`
- `env/`

### Initialize-GitIfNeeded
Ensures git repository is initialized before other processes start. This fixes warnings about being "out of sequence" with process startup.

## Startup Sequence

The profile ensures proper startup sequence:
1. **Git initialization** (if needed) - CRITICAL: Must happen first
2. **Project root detection**
3. **Venv activation**
4. **Environment setup**

This prevents warnings about processes starting out of sequence.

## Troubleshooting

### Profile not loading
```powershell
# Check execution policy
Get-ExecutionPolicy

# If restricted, set to RemoteSigned
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Venv not found
```powershell
# Create venv
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
python -m venv venv
```

### Git warnings
The profile automatically initializes git if needed, which should resolve "out of sequence" warnings.

## Notes

- The profile only activates when you're in a directory containing ".lumina" in the path
- Git initialization happens automatically and silently if needed
- Venv activation is skipped if already activated
