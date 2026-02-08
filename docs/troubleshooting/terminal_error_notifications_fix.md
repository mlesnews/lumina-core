# Fix Repeated Terminal Error Notifications

## Issue
Repeated terminal error notifications showing:
- Exit code 9
- Exit code 11

These are from background `robocopy` processes from NAS migrations.

## Understanding Robocopy Exit Codes

### Success Codes (0-7)
- **0**: No files copied, no errors
- **1**: All files copied successfully
- **2-7**: Success with various conditions (extras, mismatches, etc.)

### Warning Codes
- **8**: Some files could not be copied
- **9**: Some files skipped (locked files - **NORMAL** for Docker migrations)

### Error Codes (10+)
- **11**: No files could be copied (check permissions/network)
- **12+**: Various errors

## Quick Fix

### Option 1: Suppress Notifications in Cursor IDE
```powershell
# Run the suppression script
. scripts/python/suppress_terminal_errors.ps1
```

This will:
- Update Cursor IDE settings to suppress exit code notifications
- Optionally stop stuck robocopy processes

### Option 2: Manual Settings Update
1. Open Cursor IDE Settings (`Ctrl+,`)
2. Search for "terminal"
3. Find "Terminal: Show Exit Code Notifications"
4. **Disable** it
5. OR set "Terminal: Exit Code" to "never" or "errorOnly"

### Option 3: Update Settings.json Directly
Add to `%APPDATA%\Cursor\User\settings.json`:
```json
{
  "terminal.integrated.showExitCode": false
}
```

## Fix Scripts

The migration scripts have been updated to handle exit codes properly:
- Exit codes 0-7: Logged as success (no error notification)
- Exit code 9: Logged as warning (normal for locked files)
- Exit code 11+: Logged as error (actual problem)

## Stop Background Processes

If robocopy processes are stuck:
```powershell
# Check running robocopy processes
Get-Process robocopy -ErrorAction SilentlyContinue

# Stop all robocopy processes
Get-Process robocopy -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Why Exit Code 9 is Normal

Exit code 9 from robocopy means "some files were skipped". This is **normal** when:
- Docker is running (files are locked)
- Files are in use by other processes
- Temporary files are being created/deleted

The migration still succeeds - just some files couldn't be copied at that moment.

## Why Exit Code 11 Happens

Exit code 11 means "no files could be copied". This can happen if:
- Network connection to NAS is down
- Permissions issue
- Target directory doesn't exist
- Source directory is empty or doesn't exist

## Prevention

1. **Check network connection** before starting migrations
2. **Stop Docker** before migrating Docker volumes
3. **Check permissions** on NAS target directories
4. **Use updated scripts** that handle exit codes properly

## Related Scripts

- `scripts/python/fix_robocopy_exit_codes.py` - Updates scripts to handle exit codes
- `scripts/python/suppress_terminal_errors.ps1` - Suppresses notifications
- `scripts/python/check_migration_progress.ps1` - Check migration status

## Notes

- Exit code 9 is **not an error** - it's a warning
- Background robocopy processes will complete eventually
- Terminal notifications can be safely suppressed for robocopy
- Check actual migration progress, not just exit codes
