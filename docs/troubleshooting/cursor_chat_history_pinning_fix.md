# Cursor IDE Chat History & Pinning Fix

## Issue
Unable to pull up older agent chat histories or pin anything - nothing happens when clicking.

## Quick Fixes

### 1. Restart Cursor IDE
**Simplest solution** - Often fixes UI issues:
1. Close all Cursor IDE windows
2. Wait 5 seconds
3. Restart Cursor IDE

### 2. Clear Cursor Cache
```powershell
# Run the fix script
python scripts/python/fix_cursor_chat_history_pinning.py --clear-cache
```

### 3. Check for Multiple Cursor Processes
Multiple Cursor instances can cause conflicts:
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*cursor*"}
# If multiple found, close all and restart
```

### 4. Check Workspace Storage
Corrupted workspace storage can cause UI issues:
```powershell
python scripts/python/fix_cursor_chat_history_pinning.py
```

## Common Causes

1. **Corrupted State Files** - JSON files in workspace storage are corrupted
2. **Multiple Processes** - Multiple Cursor instances running
3. **Cache Issues** - Stale cache data
4. **Extension Conflicts** - Extensions interfering with chat UI
5. **Storage Full** - Disk space issues (we're addressing this with NAS migration)

## Diagnostic Script

Run the diagnostic:
```powershell
python scripts/python/fix_cursor_chat_history_pinning.py
```

This will:
- Check workspace storage for issues
- Check for multiple Cursor processes
- Fix corrupted state files
- Provide recommendations

## Manual Fixes

### Clear Cache Manually
1. Close Cursor IDE
2. Navigate to: `%APPDATA%\Cursor\User\`
3. Delete or rename:
   - `Cache\`
   - `Code Cache\`
   - `GPUCache\`
4. Restart Cursor IDE

### Reset Workspace Storage
1. Close Cursor IDE
2. Navigate to: `%APPDATA%\Cursor\User\workspaceStorage\`
3. Backup the folder
4. Delete contents (or specific workspace folder)
5. Restart Cursor IDE

## Prevention

1. **Regular Restarts** - Restart Cursor IDE daily
2. **Monitor Disk Space** - Keep free space above 10%
3. **Update Cursor** - Keep Cursor IDE updated
4. **Extension Management** - Disable problematic extensions

## Related Scripts

- `scripts/python/fix_cursor_chat_history_pinning.py` - Main fix script
- `scripts/python/troubleshoot_cursor_chat_history.py` - Troubleshooting
- `scripts/python/cursor_agent_history_processor.py` - History processor

## Notes

- Chat history is stored in workspace storage
- Pinning data is in state files
- Corrupted JSON can break UI functionality
- Multiple processes can cause race conditions
