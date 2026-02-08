# Lumina Virtual Environment - Auto-Activation

## Overview

The Lumina project virtual environment is configured to **automatically activate** in all terminals and PowerShell sessions when working in the project.

## Auto-Activation Methods

### 1. VS Code/Cursor Terminal (Primary Method)

**Configuration:** `.vscode/settings.json`

The workspace is configured to:
- Automatically detect the venv at `venv/`
- Auto-activate in all new terminals
- Set Python interpreter to `venv/Scripts/python.exe`
- Use "PowerShell (Lumina)" as the default terminal profile

**How it works:**
- When you open a new terminal in VS Code/Cursor, the venv activates automatically
- The Python extension detects and uses the venv interpreter
- All Python commands use the venv Python 3.11.9

### 2. Quick Activation Scripts

**Root Level:**
```powershell
.\activate.ps1
```

**Alternative:**
```powershell
. .venv-activate.ps1
```

### 3. Manual Activation

If auto-activation doesn't work:
```powershell
.\venv\Scripts\Activate.ps1
```

## Verification

**Check if venv is active:**
```powershell
# Should show the venv path
$env:VIRTUAL_ENV

# Should show Python 3.11.9
python --version

# Should point to venv
where.exe python
```

**Expected output when active:**
```
(venv) PS D:\Dropbox\my_projects> python --version
Python 3.11.9
```

## Configuration Files

### VS Code Settings
- **File:** `.vscode/settings.json`
- **Settings:**
  - `python.defaultInterpreterPath`: Points to venv Python
  - `python.terminal.activateEnvironment`: `true`
  - `terminal.integrated.defaultProfile.windows`: "PowerShell (Lumina)"

### Activation Scripts
- `activate.ps1` - Root-level quick activation
- `.venv-activate.ps1` - Alternative activation
- `scripts/powershell/Auto-ActivateVenv.ps1` - Auto-activation helper

## Troubleshooting

### Venv not auto-activating in VS Code

1. **Reload VS Code/Cursor**
   - Press `Ctrl+Shift+P`
   - Run "Developer: Reload Window"

2. **Select Python Interpreter**
   - Press `Ctrl+Shift+P`
   - Run "Python: Select Interpreter"
   - Choose `.\venv\Scripts\python.exe`

3. **Check Terminal Profile**
   - Open terminal settings
   - Verify "PowerShell (Lumina)" is selected

### Venv not found

If you see "Virtual environment not found":
```powershell
.\scripts\powershell\Setup-LuminaVenv.ps1
```

## Best Practices

1. **Always use the venv** - Never install packages globally
2. **Check activation** - Verify `$env:VIRTUAL_ENV` is set before installing packages
3. **Use activate.ps1** - Quick activation from project root
4. **VS Code integration** - Let VS Code handle auto-activation in terminals

## Related Documentation

- [Lumina Python Configuration](../config/lumina_python_config.json)
- [Lumina Setup Complete](./LUMINA_SETUP_COMPLETE.md)

---

**Remember:** The venv should activate automatically. If it doesn't, use `.\activate.ps1` or check VS Code settings.

