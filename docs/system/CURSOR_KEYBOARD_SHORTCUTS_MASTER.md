# Cursor IDE Keyboard Shortcuts - Master Reference

**Last Updated:** 2026-01-13

## ⚠️ CRITICAL CLARIFICATION

### Reload Window (CORRECT)
```
Ctrl+Shift+P → Type "Reload Window" → Enter
```

### New AI Agent Chat (NOT Reload!)
```
Ctrl+R = Opens NEW AI AGENT Chat window
```

**WARNING:** `Ctrl+R` does **NOT** reload the window! It opens a new chat session.

---

## Essential Shortcuts

| Action | Shortcut | Notes |
|--------|----------|-------|
| **Command Palette** | `Ctrl+Shift+P` | Access all commands |
| **Reload Window** | `Ctrl+Shift+P` → "Reload Window" | Reloads IDE settings |
| **New Chat** | `Ctrl+R` | Opens new AI Agent chat |
| **Toggle Sidebar** | `Ctrl+B` | Show/hide file explorer |
| **Quick Open** | `Ctrl+P` | Open files quickly |
| **Find in Files** | `Ctrl+Shift+F` | Search across project |

## AI/Chat Shortcuts

| Action | Shortcut | Notes |
|--------|----------|-------|
| **New AI Chat** | `Ctrl+R` | Start new conversation |
| **Inline Edit** | `Ctrl+K` | AI-assisted inline edit |
| **Accept Suggestion** | `Tab` | Accept AI completion |
| **Reject Suggestion** | `Esc` | Dismiss suggestion |

## Code Editing

| Action | Shortcut | Notes |
|--------|----------|-------|
| **Refactor** | `Ctrl+K Ctrl+R` | Refactor selected code |
| **Format Document** | `Shift+Alt+F` | Auto-format |
| **Go to Definition** | `F12` | Jump to definition |
| **Peek Definition** | `Alt+F12` | Preview definition |
| **Rename Symbol** | `F2` | Rename across files |

## Error Recovery

| Situation | Action |
|-----------|--------|
| **ConnectError** | `Ctrl+Shift+P` → "Reload Window" |
| **Model not found** | Check settings, then reload |
| **Session stuck** | `Ctrl+Shift+P` → "Reload Window" |
| **Complete reset** | Close Cursor, clear cache, restart |

---

## Common Mistakes

| Wrong | Right | What Happens If Wrong |
|-------|-------|----------------------|
| `Ctrl+R` to reload | `Ctrl+Shift+P` → "Reload Window" | Opens new chat instead |
| `Ctrl+R` multiple times | Once is enough | Spawns multiple agent processes |

---

## Cache Clear (Emergency)

If reload doesn't work:

```powershell
# Close Cursor first!
Stop-Process -Name "Cursor" -Force -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:APPDATA\Cursor\Cache" -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force "$env:APPDATA\Cursor\CachedData" -ErrorAction SilentlyContinue
Start-Process "C:\Program Files\cursor\Cursor.exe"
```

---

*Remember: `Ctrl+R` ≠ Reload. Use `Ctrl+Shift+P` → "Reload Window"*
