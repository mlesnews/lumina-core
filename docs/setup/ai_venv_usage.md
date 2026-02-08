# AI Venv Usage Guidelines

## Overview
This document ensures that all AI-executed commands use the virtual environment (venv) automatically.

## Automatic Venv Activation

### PowerShell Profile
The PowerShell profile (`Microsoft.PowerShell_profile.ps1`) automatically activates venv when:
- PowerShell starts
- Entering the `.lumina` project directory

### AI Command Execution
When the AI executes terminal commands, it should:

1. **Check for venv activation**:
   ```powershell
   if (-not $env:VIRTUAL_ENV) {
       & "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv\Scripts\Activate.ps1"
   }
   ```

2. **Use venv Python directly**:
   ```powershell
   & "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv\Scripts\python.exe" scripts/python/your_script.py
   ```

3. **Use the wrapper script**:
   ```powershell
   python scripts/python/run_with_venv.py scripts/python/your_script.py
   ```

## Tools Available

### 1. `run_with_venv.py`
Python wrapper that automatically finds and uses venv Python:
```bash
python scripts/python/run_with_venv.py scripts/python/your_script.py
```

### 2. `ensure_venv_for_ai.ps1`
PowerShell script to ensure venv is activated:
```powershell
. scripts/setup/ensure_venv_for_ai.ps1
```

### 3. `activate_venv_wrapper.ps1`
PowerShell wrapper for commands:
```powershell
. scripts/python/activate_venv_wrapper.ps1 -Command "python scripts/python/your_script.py"
```

## Best Practices

1. **Always check venv first**: Before running Python commands, verify venv is activated
2. **Use absolute paths**: When possible, use absolute paths to venv Python
3. **Fallback gracefully**: If venv is not found, warn but continue (for flexibility)
4. **Document venv usage**: In scripts, document venv requirements

## Verification

To verify venv is being used:
```powershell
# Check if venv is activated
$env:VIRTUAL_ENV

# Check Python path
python -c "import sys; print(sys.executable)"
```

The Python executable should point to `venv\Scripts\python.exe` (Windows) or `venv/bin/python` (Unix).

## Integration with Cursor IDE

Cursor IDE's terminal commands should automatically use the PowerShell profile, which activates venv. However, the AI should still verify venv activation for critical commands.

## Troubleshooting

### Venv not activating
1. Check PowerShell profile exists: `Test-Path $PROFILE`
2. Check venv exists: `Test-Path "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv"`
3. Manually activate: `& "C:\Users\mlesn\Dropbox\my_projects\.lumina\venv\Scripts\Activate.ps1"`

### Commands not using venv
1. Use absolute path to venv Python
2. Check `$env:VIRTUAL_ENV` is set
3. Use wrapper scripts provided
