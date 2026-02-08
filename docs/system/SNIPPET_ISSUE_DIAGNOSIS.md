# Snippet Functionality Issue - System Engineer Review

**Date**: 2026-01-14  
**Status**: 🔧 **ASSIGNED TO WINDOWS SYSTEM ENGINEER**  
**Tags**: `#TROUBLESHOOTING` `#WINDOWS` `#SNIPPET` `#SYSTEM_ENGINEER` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Issue Report

**User Report**: "Snippet doesn't seem to be working right now"

**Requested Action**: Have Windows System Engineer look at it

**Priority**: Medium (functionality not working)

---

## 🔍 Initial Diagnosis

### Possible Snippet Types

1. **VS Code/Cursor Snippets**
   - Code completion snippets
   - Custom user snippets
   - Extension snippets

2. **Clipboard Snippets**
   - Clipboard manager
   - Text expansion
   - Snippet manager tool

3. **Custom Snippet System**
   - LUMINA-specific snippet functionality
   - Integration snippets

4. **AutoHotkey Snippets**
   - Text expansion via AutoHotkey
   - Keyboard shortcuts

---

## 📋 Diagnostic Steps for System Engineer

### Step 1: Identify Snippet Type

**Check**:
- What application/tool is the snippet in?
- Is it VS Code/Cursor snippets?
- Is it a clipboard manager?
- Is it AutoHotkey text expansion?

**Commands**:
```powershell
# Check VS Code/Cursor snippets
Get-ChildItem "$env:APPDATA\Code\User\snippets" -ErrorAction SilentlyContinue
Get-ChildItem "$env:APPDATA\Cursor\User\snippets" -ErrorAction SilentlyContinue

# Check AutoHotkey running
Get-Process | Where-Object {$_.ProcessName -like "*autohotkey*"}

# Check clipboard managers
Get-Process | Where-Object {$_.ProcessName -like "*clipboard*" -or $_.ProcessName -like "*snippet*"}
```

---

### Step 2: Check Common Issues

**VS Code/Cursor Snippets**:
- Snippet files corrupted
- Extension conflicts
- Settings misconfigured
- File permissions

**AutoHotkey Snippets**:
- Script not running
- Hotkey conflicts
- Script errors
- File path issues

**Clipboard Snippets**:
- Service not running
- Database corrupted
- Configuration issues

---

### Step 3: System Checks

**Windows Services**:
```powershell
Get-Service | Where-Object {$_.DisplayName -like "*snippet*" -or $_.DisplayName -like "*clipboard*"}
```

**Event Logs**:
```powershell
Get-EventLog -LogName Application -Newest 50 | Where-Object {$_.Source -like "*snippet*" -or $_.Message -like "*snippet*"}
```

**File System**:
```powershell
# Check snippet directories
$snippetPaths = @(
    "$env:APPDATA\Code\User\snippets",
    "$env:APPDATA\Cursor\User\snippets",
    "$env:USERPROFILE\.cursor\snippets",
    "$env:LOCALAPPDATA\snippets"
)

foreach ($path in $snippetPaths) {
    if (Test-Path $path) {
        Write-Host "Found: $path"
        Get-ChildItem $path -Recurse | Select-Object FullName, LastWriteTime
    }
}
```

---

### Step 4: Application-Specific Checks

**If VS Code/Cursor**:
1. Check snippet files exist
2. Verify JSON syntax
3. Check extension status
4. Review settings.json

**If AutoHotkey**:
1. Check script is running
2. Review script for errors
3. Check hotkey conflicts
4. Verify file paths

**If Custom Tool**:
1. Check service/process running
2. Review configuration files
3. Check logs
4. Verify dependencies

---

## 🔧 Common Fixes

### VS Code/Cursor Snippets

**Fix 1: Reload Window**
- Command Palette: "Developer: Reload Window"

**Fix 2: Check Snippet Files**
- Verify JSON syntax
- Check file permissions
- Ensure files are in correct location

**Fix 3: Extension Issues**
- Disable/re-enable snippet extensions
- Check for conflicts
- Update extensions

### AutoHotkey Snippets

**Fix 1: Restart Script**
```powershell
# Stop AutoHotkey
Get-Process | Where-Object {$_.ProcessName -like "*autohotkey*"} | Stop-Process

# Restart script
Start-Process "path\to\snippet_script.ahk"
```

**Fix 2: Check Script Errors**
- Review AutoHotkey error logs
- Check syntax
- Verify file paths

### Clipboard Snippets

**Fix 1: Restart Service**
```powershell
Restart-Service -Name "ClipboardService" -ErrorAction SilentlyContinue
```

**Fix 2: Reset Database**
- Backup current database
- Reset to defaults
- Re-import snippets

---

## 📝 System Engineer Action Items

1. **Identify**: What type of snippet system is being used?
2. **Diagnose**: What specific error or behavior is occurring?
3. **Check**: System logs, processes, and configuration
4. **Fix**: Apply appropriate fix based on snippet type
5. **Verify**: Test snippet functionality after fix
6. **Document**: Record solution for future reference

---

## 🎯 Expected Outcome

**Goal**: Restore snippet functionality to working state

**Success Criteria**:
- Snippets trigger correctly
- No errors in logs
- User can use snippets as expected

---

## 📚 Related Documentation

- Windows System Engineering: `docs/organizational/STORAGE_ENGINEERING_INDIVIDUAL_ROLES.md`
- Troubleshooting Guide: [To be created]
- System Engineer Role: Storage Engineer / System Engineer

---

**Status**: 🔧 **ASSIGNED TO WINDOWS SYSTEM ENGINEER**  
**Next Action**: System Engineer to diagnose and fix snippet issue  
**Tags**: `#TROUBLESHOOTING` `#WINDOWS` `#SNIPPET` `#SYSTEM_ENGINEER` `@LUMINA` `@JARVIS` `#PEAK`
