# UIA-v2 Setup Guide - Finding Cursor IDE Chat Input

## ✅ Installation Complete!

UIA-v2 is now installed at: `scripts\autohotkey\UIA-v2`

## 🔍 Step 1: Inspect Cursor IDE with UIATreeInspector

### How to Run UIATreeInspector

1. **Open AutoHotkey v2** (if you have it installed)
2. **Run**: `scripts\autohotkey\UIA-v2\UIATreeInspector.ahk`
   - Or compile it to .exe first
3. **Point the inspector at Cursor IDE**:
   - Click the "Target" button in UIATreeInspector
   - Hover over Cursor IDE's chat input field
   - Click on it

### What to Look For

In UIATreeInspector, find the chat input element and note:
- **Name**: What the element is called (e.g., "Chat input", "Message", etc.)
- **ControlType**: Usually "Edit" or "Document" for text inputs
- **IsKeyboardFocusable**: Should be `True`
- **AutomationId**: Unique identifier (if available)

### Example Properties You Might See

```
Name: "Chat input" or "Type a message"
ControlType: Edit
IsKeyboardFocusable: True
AutomationId: "chat-input" (or similar)
```

## 📝 Step 2: Update the AutoHotkey Script

Once you have the properties, update `left_alt_doit_UIA.ahk`:

```autohotkey
FocusChatWithUIA() {
    if (!UIA_AVAILABLE) {
        ; Fallback to basic method
        return
    }
    
    ; Get Cursor window
    cursorWindow := WinGet("ahk_exe Cursor.exe")
    if (!cursorWindow) {
        ; Cursor not running
        return
    }
    
    ; Get UIA element from window
    cursorElement := UIA.ElementFromHandle(cursorWindow)
    
    ; Find chat input using properties from UIATreeInspector
    ; UPDATE THESE PROPERTIES based on what you find:
    chatInput := cursorElement.FindFirst({
        Name: "Chat input",  ; UPDATE THIS
        ControlType: "Edit",  ; UPDATE THIS
        IsKeyboardFocusable: True
    })
    
    if (chatInput) {
        chatInput.SetFocus()
        return True
    }
    
    ; If not found, try alternative properties
    ; (Add more FindFirst attempts based on what you see)
    
    return False
}
```

## 🧪 Step 3: Test

1. **Load the script**: `left_alt_doit_UIA.ahk`
2. **Press RAlt** (short press)
3. **Check if chat input gets focus** properly
4. **Check the log** for any errors

## 🆘 Troubleshooting

### If UIATreeInspector doesn't find the element:
- The chat might be in a web view (browser control)
- Try using `UIA_Browser.ahk` instead
- Or use the fallback method (mouse click)

### If the script can't find the element:
- Double-check the properties in UIATreeInspector
- Try using partial name matching
- Try finding parent elements first, then child

### If it works but is slow:
- Use caching (see UIA-v2 examples)
- Cache the element after first find

## 📚 Resources

- **UIA-v2 Documentation**: https://deepwiki.com/Descolada/UIA-v2/
- **Examples**: `UIA-v2\Examples\` folder
- **Browser Automation**: `UIA-v2\Lib\UIA_Browser.ahk` (if chat is web-based)

## 🎯 Next Steps

1. ✅ UIA-v2 installed
2. ⏳ Run UIATreeInspector
3. ⏳ Find chat input properties
4. ⏳ Update script with properties
5. ⏳ Test and refine
