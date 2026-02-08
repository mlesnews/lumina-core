# VSCode Extension Cache Manual Cleanup Guide

## Problem Statement

**Error**: `Cannot activate the 'Lumina Core - Open Source Lumina Ecosystem' extension because it depends on an unknown 'github.copilot' extension.`

## Root Cause

This error occurs due to **cached extension state** in VSCode/Cursor that still references `github.copilot` even though:
- The workspace configuration files (`.cursor/extensions.json`, `.vscode/extensions.json`) are clean
- The lumina-core extension manifest only depends on `eamodio.gitlens`

VSCode/Cursor caches extension metadata, and stale cache entries can cause dependency resolution errors.

## Manual Cleanup Steps

### Step 1: Close All VSCode/Cursor Instances

1. Save all your work
2. Close all VSCode and Cursor windows completely
3. Check Task Manager (Ctrl+Shift+Esc) to ensure no `Code.exe` or `cursor.exe` processes are running

### Step 2: Clear VSCode Extension Cache

Delete the following directories (or rename them to keep backups):

```powershell
# VSCode
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\Cache"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\CachedData"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\logs"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\Local Storage"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\Session Storage"
```

### Step 3: Clear VSCode Insider Cache (if applicable)

```powershell
# VSCode Insider
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code - Insiders\Cache"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code - Insiders\CachedData"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code - Insiders\logs"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code - Insiders\Local Storage"
```

### Step 4: Clear Cursor Extension Cache

```powershell
# Cursor
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\Cache"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\CachedData"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\logs"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\Local Storage"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\Session Storage"
```

### Step 5: Clear Extension Global Storage

```powershell
# Backup globalStorage first
Copy-Item -Recurse "$env:APPDATA\Code\User\globalStorage" "$env:USERPROFILE\Desktop\VSCode_globalStorage_backup" -ErrorAction SilentlyContinue
Copy-Item -Recurse "$env:APPDATA\Cursor\User\globalStorage" "$env:USERPROFILE\Desktop\Cursor_globalStorage_backup" -ErrorAction SilentlyContinue

# Then clear
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code\User\globalStorage"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor\User\globalStorage"
```

### Step 6: Restart Your Computer

A full system restart ensures all cached processes are terminated and caches are cleared.

### Step 7: Reopen and Verify

1. Open VSCode/Cursor
2. Check the Extensions view (Ctrl+Shift+X)
3. Verify lumina-core is listed and shows no errors
4. The extension should now activate correctly

## If Error Persists

### Option A: Reinstall lumina-core Extension

1. Open Extensions view
2. Search for "Lumina Core"
3. Click the gear icon → Uninstall
4. Reload VSCode/Cursor
5. Reinstall from the VSIX file in `vscode-extensions/lumina-core/`

### Option B: Reset All Extension State

```powershell
# Warning: This removes all extension settings and preferences

# Clear VSCode completely
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Code"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:USERPROFILE\.vscode"

# Clear Cursor completely
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:APPDATA\Cursor"
Remove-Item -Recurse -ErrorAction SilentlyContinue "$env:USERPROFILE\.cursor"
```

### Option C: Manual Extension State File Edit

The extension state is stored in:
- `%APPDATA%\Code\User\globalStorage\state.json`
- `%APPDATA%\Cursor\User\globalStorage\state.json`

Edit these files and remove any entries referencing `github.copilot`.

## Verification Commands

Check if lumina-core dependencies are correct:

```powershell
# Check current workspace extensions
Get-Content .cursor/extensions.json | ConvertFrom-Json | Select-Object -ExpandProperty recommendations

# Check lumina-core manifest
Get-Content vscode-extensions/lumina-core/package.json | ConvertFrom-Json | Select-Object extensionDependencies
```

## Prevention

To prevent this issue in the future:
1. Always clear extension cache when removing extensions
2. Use the batch script `scripts/powershell/fix_vscode_extension_cache_cleanup.bat` for cleanup
3. Avoid manually editing extension cache files

## Related Files

- `scripts/powershell/fix_vscode_extension_cache_cleanup.bat` - Automated cleanup script
- `scripts/powershell/fix_vscode_extension_errors.ps1` - PowerShell version
- `.cursor/extensions.json` - Current workspace extensions (clean)
- `vscode-extensions/lumina-core/package.json` - Extension manifest (verified clean)
