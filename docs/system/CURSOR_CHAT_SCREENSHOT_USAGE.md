# Cursor Chat Screenshot Usage Guide

**Date**: 2026-01-02  
**Status**: ✅ **READY TO USE**  
**Tag**: #CURSOR #CHAT #SCREENSHOT #QUICK-REFERENCE

---

## Quick Usage

### Method 1: Automatic (When Mentioning Errors)

Just type in Cursor chat:
```
"I'm getting an authentication error"
```

The system will automatically:
- ✅ Detect the error
- ✅ Capture screenshot
- ✅ Provide path for attachment

### Method 2: Quick Capture Command

```powershell
# Capture screenshot with context
python scripts/python/cursor_chat_auto_screenshot.py "DSM LDAP error"
```

### Method 3: Explicit Request

In Cursor chat, just ask:
```
"Can you take a screenshot?"
"Show me what you see"
"Capture the screen"
```

---

## Keyboard Shortcut (Future)

Set up a keyboard shortcut to trigger screenshot capture:
- **Windows**: Win+Shift+S (can be customized)
- **Custom**: Set up in Cursor settings

---

## What Gets Captured

- **Full screen** from RDP session
- **With context** (description of what's being captured)
- **Timestamped** automatically
- **Saved** to `data/manus_rdp_captures/`

---

## Example Workflow

1. **See error in DSM**
2. **Type in Cursor chat**: "I'm getting an incorrect authentication error"
3. **Screenshot captured automatically**
4. **Attach screenshot** to chat message
5. **Continue troubleshooting** with visual context

---

## Integration Status

✅ **RDP Screenshot Capture**: Working  
✅ **Error Detection**: Working  
✅ **Context Capture**: Working  
✅ **Cursor Chat Integration**: Ready  
⏳ **Auto-attach to chat**: Future enhancement  

---

**Last Updated**: 2026-01-02  
**Status**: Ready to use
