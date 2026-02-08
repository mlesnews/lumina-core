# Cursor IDE Restart Guide - ULTRON Configuration

## ⚠️ Important: Full Restart Required

For **model configuration changes** (like ULTRON), you need a **complete IDE restart**, not just a window reload.

## Restart Options

### Option 1: Full Restart (Recommended for Model Changes)

**Why:** Model configurations are loaded at IDE startup. Window reloads don't reload model settings.

**Steps:**
1. Save all your work (`Ctrl+S` or `Cmd+S`)
2. Close Cursor IDE completely:
   - Click `File → Exit` (or `Alt+F4` on Windows)
   - Or use Task Manager to end all Cursor processes
3. Reopen Cursor IDE
4. Open Composer (`Ctrl+I` or `Cmd+I`)
5. ULTRON should now appear in the model dropdown

**Time:** ~10-15 seconds

### Option 2: Window Reload (Not Recommended for Model Changes)

**When to use:** For UI changes, extension updates, or theme changes.

**Steps:**
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Reload Window"
3. Select "Developer: Reload Window"
4. Or press `Ctrl+R` (Windows/Linux) / `Cmd+R` (Mac)

**Limitation:** Model configurations won't be reloaded with this method.

### Option 3: Developer Window Reload

**When to use:** For debugging or development changes only.

**Steps:**
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Reload Window"
3. Select "Developer: Reload Window"

**Limitation:** Same as Option 2 - won't reload model configs.

## Verification After Restart

After restarting, verify ULTRON is available:

1. **Open Composer:**
   - Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac)

2. **Check Model Dropdown:**
   - Click the model selector at the top
   - Look for "ULTRON" or "ULTRON Cluster (Local Docker/WSL)"
   - Should see: `http://localhost:11434`

3. **Test Connection:**
   - Select ULTRON
   - Send a test message
   - Should get a response from the local Ollama instance

## Quick Restart Script

Use the provided script for easy restart:

```powershell
.\scripts\powershell\restart_cursor.ps1
```

This script will:
- Detect running Cursor processes
- Close them safely
- Reopen Cursor automatically

## Troubleshooting

### ULTRON Still Not Visible After Restart

1. **Check Ollama is Running:**
   ```powershell
   Test-NetConnection -ComputerName localhost -Port 11434
   ```

2. **Verify Settings:**
   ```powershell
   python scripts/python/verify_ultron_cursor_config.py
   ```

3. **Check Cursor Settings:**
   - Press `Ctrl+,` to open Settings
   - Search for "ollama"
   - Verify endpoint is: `http://localhost:11434`

4. **Try Full System Restart:**
   - Sometimes Windows needs a full restart for network changes

### Model Dropdown Empty

- Check if Ollama is accessible: `curl http://localhost:11434/api/tags`
- Verify model is pulled: `ollama list`
- Check Cursor logs: Help → Toggle Developer Tools → Console

## Summary

| Change Type | Restart Type | Time |
|------------|--------------|------|
| Model Configuration | **Full Restart** | ~15 sec |
| UI/Theme Changes | Window Reload | ~3 sec |
| Extension Updates | Window Reload | ~3 sec |
| Settings Changes | Full Restart | ~15 sec |

**For ULTRON configuration: Use Full Restart (Option 1)**

---

**Last Updated:** 2025-12-31
