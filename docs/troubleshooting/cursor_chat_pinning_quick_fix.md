# Cursor IDE Chat History & Pinning - Quick Fix

## 🚨 Issue
Unable to pull up older agent chat histories or pin anything - nothing happens when clicking.

## 🔍 Root Cause Found
**31 Cursor processes running** - This is causing conflicts and UI issues!

## ✅ Immediate Fix

### Option 1: Restart Cursor IDE (Recommended)
```powershell
# Close all Cursor processes and restart
. scripts/python/restart_cursor_for_chat_fix.ps1
```

### Option 2: Manual Restart
1. **Close ALL Cursor IDE windows** (including background processes)
2. **Wait 5 seconds**
3. **Restart Cursor IDE**
4. **Wait for full load** (30-60 seconds)
5. **Try accessing chat history again**

### Option 3: Clear Cache & Restart
```powershell
# Clear cache and restart
python scripts/python/fix_cursor_chat_history_pinning.py --clear-cache
```

## Why This Happens

**Multiple Cursor Processes** cause:
- UI conflicts (buttons don't respond)
- Chat history loading issues
- Pinning functionality breaks
- Race conditions in state management

## Prevention

1. **Always close Cursor properly** - Don't force-close
2. **Check for multiple processes** before reporting issues
3. **Restart daily** - Prevents process accumulation
4. **Monitor process count**:
   ```powershell
   (Get-Process -Name "*cursor*").Count
   ```

## Verification

After restart, verify:
1. Chat history loads
2. Pinning works
3. Only 1-2 Cursor processes running (normal)

## If Issues Persist

1. **Run diagnostics**:
   ```powershell
   python scripts/python/fix_cursor_chat_history_pinning.py
   ```

2. **Check Cursor IDE version** - Update if available

3. **Check extensions** - Disable extensions that might interfere

4. **Check disk space** - Low disk space can cause UI issues (we're fixing this with NAS migration)

## Related Scripts

- `scripts/python/fix_cursor_chat_history_pinning.py` - Main fix script
- `scripts/python/restart_cursor_for_chat_fix.ps1` - Restart script
- `scripts/python/troubleshoot_cursor_chat_history.py` - Full troubleshooting
