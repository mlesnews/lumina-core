# Snippet Fix - System Engineer Action Plan

**Date**: 2026-01-14  
**Status**: 🔧 **FIX READY TO APPLY**  
**Tags**: `#TROUBLESHOOTING` `#WINDOWS` `#SNIPPET` `#SYSTEM_ENGINEER` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Issue Summary

**Problem**: Snippet functionality not working in Cursor IDE

**Root Cause**: 
1. Cursor snippets directory is empty (no snippet files)
2. Snippet suggestions setting may not be configured

**Fix**: Enable snippets and create initial snippet files

---

## 🔧 Fix Steps

### Step 1: Enable Snippet Suggestions in Cursor

**Option A: Via Settings UI**
1. Open Cursor IDE
2. Press `Ctrl+,` to open Settings
3. Search for "snippet"
4. Enable:
   - `Editor: Snippet Suggestions` → Set to "top" or "inline"
   - `Editor: Suggest Snippets` → Check this box

**Option B: Via settings.json**
1. Press `Ctrl+Shift+P`
2. Type "Preferences: Open User Settings (JSON)"
3. Add:
```json
{
  "editor.snippetSuggestions": "top",
  "editor.suggest.snippetsPreventQuickSuggestions": false,
  "editor.suggest.showSnippets": true
}
```

---

### Step 2: Copy VS Code Snippets to Cursor

**Since VS Code has working snippets, copy them:**

```powershell
# Copy VS Code snippets to Cursor
$vscodeSnippets = "$env:APPDATA\Code\User\snippets"
$cursorSnippets = "$env:APPDATA\Cursor\User\snippets"

if (Test-Path $vscodeSnippets) {
    Copy-Item "$vscodeSnippets\*" -Destination $cursorSnippets -Force
    Write-Host "✅ Snippets copied from VS Code to Cursor"
}
```

---

### Step 3: Create Test Snippet (Verify Functionality)

**Create**: `C:\Users\mlesn\AppData\Roaming\Cursor\User\snippets\test.code-snippets`

**Content**:
```json
{
  "Test Snippet": {
    "prefix": "test",
    "body": [
      "This is a test snippet",
      "Snippets are working!"
    ],
    "description": "Test snippet functionality"
  },
  "JARVIS Comment": {
    "prefix": "jarvis",
    "body": [
      "// JARVIS: $1",
      "$0"
    ],
    "description": "JARVIS comment snippet"
  }
}
```

---

### Step 4: Reload Cursor

1. Press `Ctrl+Shift+P`
2. Type "Developer: Reload Window"
3. Press Enter

---

### Step 5: Test Snippet

1. Open any file in Cursor
2. Type "test" (for test snippet) or "jarvis" (for JARVIS snippet)
3. Should see snippet suggestion appear
4. Press Tab to expand snippet

---

## 📋 Verification Checklist

- [ ] Snippet suggestions enabled in settings
- [ ] Snippet files exist in Cursor directory
- [ ] Cursor window reloaded
- [ ] Test snippet works (type "test" → see suggestion)
- [ ] Snippet expands when Tab pressed

---

## 🚨 If Still Not Working

### Additional Checks

1. **Check Extensions**:
   - Disable snippet-related extensions
   - Re-enable one at a time
   - Check for conflicts

2. **Check Language Mode**:
   - Snippets are language-specific
   - Ensure correct language mode is active

3. **Check Keyboard Shortcuts**:
   - Verify Tab key works
   - Check for conflicting shortcuts

4. **Check Cursor Version**:
   - Update Cursor to latest version
   - Check release notes for snippet changes

---

## 📝 Quick Fix Script

**PowerShell script to apply fix**:

```powershell
# Enable snippets in Cursor
$cursorSettings = "$env:APPDATA\Cursor\User\settings.json"
$cursorSnippets = "$env:APPDATA\Cursor\User\snippets"
$vscodeSnippets = "$env:APPDATA\Code\User\snippets"

# Ensure snippets directory exists
if (-not (Test-Path $cursorSnippets)) {
    New-Item -ItemType Directory -Path $cursorSnippets -Force
}

# Copy VS Code snippets
if (Test-Path $vscodeSnippets) {
    Copy-Item "$vscodeSnippets\*" -Destination $cursorSnippets -Force
    Write-Host "✅ Snippets copied"
}

# Update settings.json
if (Test-Path $cursorSettings) {
    $settings = Get-Content $cursorSettings -Raw | ConvertFrom-Json
    $settings | Add-Member -NotePropertyName "editor.snippetSuggestions" -NotePropertyValue "top" -Force
    $settings | Add-Member -NotePropertyName "editor.suggest.showSnippets" -NotePropertyValue $true -Force
    $settings | ConvertTo-Json -Depth 10 | Set-Content $cursorSettings
    Write-Host "✅ Settings updated"
}

Write-Host "✅ Fix applied! Reload Cursor window to test."
```

---

**Status**: 🔧 **FIX READY TO APPLY**  
**Next Action**: System Engineer to apply fix and verify  
**Tags**: `#TROUBLESHOOTING` `#WINDOWS` `#SNIPPET` `#SYSTEM_ENGINEER` `@LUMINA` `@JARVIS` `#PEAK`
