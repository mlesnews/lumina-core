# AutoHotkey Key Mappings & Features

## Current Key Mappings

### RAlt (Right Alt)

**Short Press (< 500ms):**
- Action: Focus chat, type `@doit`, Enter/Return
- Workflow:
  1. Send Ctrl+L (open chat)
  2. Wait 700ms (for layout to stabilize)
  3. Click on chat input area (bottom-right)
  4. Type `@doit`
  5. Send Enter

**Long Press (> 500ms):**
- Action: **Keep All** (Accept All Changes)
- Sends: Ctrl+Enter
- Accepts all pending changes in the editor

### F23 (MS-Copilot Key)

**Short Press (< 500ms):**
- Action: Smart focus + Voice Input
- Workflow:
  1. Check if Cursor is active
  2. Send Ctrl+L (focus chat)
  3. If needed, Alt+Tab to Cursor
  4. Send Ctrl+Shift+Space (activate voice input)

**Long Press (> 500ms):**
- Action: Pause + Move Mouse
- Workflow:
  1. Send Escape (pause)
  2. Move mouse to previous input location
  3. Or move to default chat input area

## Model Detection & Display

### Current Implementation
- Python script: `scripts\python\detect_active_model.py`
- Detects active AI model from:
  - Cursor settings.json
  - Environment variables
  - Default assumption (Claude)

### Display Format
Would show in chat title like:
```
AutoHotkeyScriptExecuteLog [Claude Sonnet 4.5]
```

### Future Enhancement
- Full UI integration would require Cursor extension
- Could display model name in chat title automatically
- Would help track which models work best for different tasks

## Keep All Functionality

### Keyboard Shortcut
- **Windows/Linux:** Ctrl+Enter
- **macOS:** Cmd+Enter

### Current Mappings
- **Alt+K** → Keep All (Ctrl+Enter) - **Standard mapping**
- **RAlt Long Press** → Keep All (Ctrl+Enter) - Alternative

### Mappings
- **Alt+K** - Standard mapping (recommended)
- RAlt Long Press - Alternative
- Both trigger the same Keep All action (Ctrl+Enter)

## Testing

### Test Script
File: `scripts\autohotkey\left_alt_doit_TEST.ahk`

### Test Flags
```autohotkey
TEST_RALT_SHORT := 1      ; Test RAlt short press
TEST_RALT_LONG := 0       ; Test RAlt long press (Keep All)
TEST_F23_SHORT := 0       ; Test F23 short press
TEST_F23_LONG := 0        ; Test F23 long press
TEST_KEEP_ALL := 0        ; Test Keep All separately
```

### Log Files
- Test logs: `logs\RAltMacro_TEST_YYYYMMDD.log`
- Diagnostic logs: `logs\ChatFocus_Diagnostic_YYYYMMDD.log`

## Recommendations

### For This Problem (Chat Focus Debugging)
**Best AI Model:** Claude Sonnet 4.5 or Opus (Anthropic)
- Excellent at systematic debugging
- Great at understanding complex system interactions
- Strong pattern recognition
- Good at analyzing logs and traces

**Why:** This problem requires understanding:
- System state changes (layout, focus)
- Timing dependencies
- Multiple interaction methods
- Log analysis and pattern matching

## Next Steps

1. ✅ Test RAlt short press (chat focus + @doit)
2. ✅ Test RAlt long press (Keep All)
3. ⏳ Test F23 short press (voice input)
4. ⏳ Test F23 long press (pause + mouse)
5. ⏳ Implement model display in chat title
6. ⏳ Fine-tune key combinations based on preference
