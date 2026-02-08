# Keyboard Shortcut Improvement Proposals

**Date**: 2026-01-14
**Purpose**: Proposals for closing automation gaps in keyboard shortcuts
**Status**: 📋 **PROPOSALS - READY FOR REVIEW**
**Tags**: `#AUTOMATION` `#IMPROVEMENTS` `#PROPOSALS` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Overview

Detailed proposals for improving Right Alt and F23 keyboard shortcuts to close automation gaps while maintaining current stopgap functionality.

---

## 💡 Proposal 1: Smart Focus Detection (Right Alt)

### Current Gap

Right Alt requires manual chat field focus before use.

### Proposal

**Smart Focus Detection**: Automatically detect if chat is focused, only focus if needed.

### Implementation Options

#### Option A: Window Focus Detection

```autohotkey
RAlt::
    ; Check if chat field is already focused
    ; Method: Check active window class or title
    if (!IsChatFocused()) {
        SendInput, ^l  ; Only focus if not already focused
        Sleep, 150
    }

    ; Send /doit
    SendInput, /doit{Space}
    Sleep, 200
    SendInput, {Enter}
    return

IsChatFocused() {
    ; Check if Cursor IDE chat is focused
    ; Implementation: Window class detection or UI element check
    WinGetClass, class, A
    ; Logic to determine if chat is focused
    return (class contains "chat" or "agent")
}
```

**Pros**: Only focuses when needed
**Cons**: Requires window detection logic
**Complexity**: Medium

---

#### Option B: Focus State File

```autohotkey
RAlt::
    ; Check focus state file (updated by Python script)
    FileRead, focusState, %A_Temp%\cursor_chat_focus_state.txt
    if (focusState != "focused") {
        SendInput, ^l
        Sleep, 150
    }

    SendInput, /doit{Space}
    Sleep, 200
    SendInput, {Enter}
    return
```

**Pros**: Simple, reliable
**Cons**: Requires Python script to track state
**Complexity**: Low-Medium

---

#### Option C: Layout-Safe Focus

```autohotkey
RAlt::
    ; Try to focus without layout switching
    ; Method: Use alternative focus method or detect layout first
    if (!IsInAgentMode()) {
        ; Only focus if not in agent mode
        SendInput, ^l
        Sleep, 150
    }

    SendInput, /doit{Space}
    Sleep, 200
    SendInput, {Enter}
    return
```

**Pros**: Prevents layout switching
**Cons**: Requires layout detection
**Complexity**: Medium

---

### Recommendation

**Option B (Focus State File)**: Simple, reliable, doesn't require complex detection. Python script can track focus state continuously.

---

## 💡 Proposal 2: Better Detection Method (F23)

### Current Gap

F23 uses clipboard method for detection - not ideal, has edge cases.

### Proposal

**Hybrid Detection Method**: Combine multiple detection methods for reliability.

### Implementation Options

#### Option A: Multi-Method Voting

```autohotkey
F23::
    SendInput, ^l
    Sleep, 150

    ; Method 1: Clipboard check
    clipboard1 := CheckClipboard()

    ; Method 2: Window title check
    clipboard2 := CheckWindowTitle()

    ; Method 3: State file check
    clipboard3 := CheckStateFile()

    ; Vote: If 2+ methods say "has content", treat as active
    hasContent := (clipboard1 + clipboard2 + clipboard3 >= 2)

    if (!hasContent) {
        ; New chat
        SendInput, ^+{Space}
    } else {
        ; Pause and edit
        SendInput, {Esc}
        Sleep, 200
        SendInput, ^+{Space}
    }
    return
```

**Pros**: More reliable, handles edge cases
**Cons**: More complex, multiple methods
**Complexity**: Medium-High

---

#### Option B: Python Bridge Detection

```autohotkey
F23::
    ; Call Python script to detect chat state
    RunWait, python check_chat_state.py, , Hide
    FileRead, chatState, %A_Temp%\cursor_chat_state.txt

    if (chatState = "empty") {
        ; New chat
        SendInput, ^+{Space}
    } else {
        ; Pause and edit
        SendInput, {Esc}
        Sleep, 200
        SendInput, ^+{Space}
    }
    return
```

**Python Script** (`check_chat_state.py`):
```python
# Check Cursor IDE chat state via extension API or UI detection
# Write state to temp file for AutoHotkey to read
```

**Pros**: More powerful, can use APIs
**Cons**: Requires Python script
**Complexity**: Medium

---

#### Option C: State File with Updates

```autohotkey
F23::
    ; Read state file (updated continuously by background script)
    FileRead, chatState, %A_Temp%\cursor_chat_state.json

    ; Parse JSON: { "has_content": true, "agent_running": false }
    ; Use state to determine action

    if (!hasContent) {
        SendInput, ^+{Space}
    } else {
        SendInput, {Esc}
        Sleep, 200
        SendInput, ^+{Space}
    }
    return
```

**Pros**: Real-time state, no detection needed
**Cons**: Requires background state tracker
**Complexity**: Medium

---

### Recommendation

**Option C (State File with Updates)**: Most reliable, real-time state, no detection overhead. Background Python script tracks state continuously.

---

## 💡 Proposal 3: Layout-Safe Focus (F23)

### Current Gap

F23 uses Ctrl+L which causes layout switching.

### Proposal

**Layout-Safe Focus**: Focus chat without causing layout switching.

### Implementation Options

#### Option A: Detect Layout Before Focus

```autohotkey
F23::
    ; Check current layout mode
    if (IsInEditorMode()) {
        ; Only focus if in editor mode
        SendInput, ^l
        Sleep, 150
    }
    ; If already in agent mode, skip focus

    ; Continue with detection and voice input
    return
```

**Pros**: Prevents unnecessary layout switching
**Cons**: Requires layout detection
**Complexity**: Medium

---

#### Option B: Alternative Focus Method

```autohotkey
F23::
    ; Use alternative focus method that doesn't switch layout
    ; Method: Click chat field directly, or use different shortcut
    ; Research: Is there a layout-safe focus method?

    ; For now: Skip focus if in agent mode
    if (!IsInAgentMode()) {
        SendInput, ^l
        Sleep, 150
    }

    ; Continue with detection
    return
```

**Pros**: Avoids layout switching
**Cons**: Requires research on alternative methods
**Complexity**: Medium-High

---

#### Option C: Accept One-Time Layout Switch

```autohotkey
F23::
    ; Accept that Ctrl+L will switch layout once
    ; But ensure we stay in agent mode after
    SendInput, ^l
    Sleep, 150

    ; After detection and voice input, ensure agent mode
    ; (Voice input might keep us in agent mode)

    return
```

**Pros**: Simple, works
**Cons**: Still causes layout switch
**Complexity**: Low

---

### Recommendation

**Option A (Detect Layout Before Focus)**: Best balance - prevents unnecessary switching, relatively simple to implement.

---

## 💡 Proposal 4: Python State Bridge

### Concept

Create Python bridge script that tracks Cursor IDE state and provides it to AutoHotkey.

### Architecture

```
Cursor IDE
    ↓
Python State Tracker (background service)
    ↓
State File/Registry
    ↓
AutoHotkey Scripts (read state)
```

### Components

1. **State Tracker** (`cursor_state_tracker.py`):
   - Monitors Cursor IDE state
   - Tracks: chat focus, chat content, agent state, layout mode
   - Updates state file/registry continuously

2. **State File** (`cursor_state.json`):
   - JSON file with current state
   - Updated in real-time
   - Read by AutoHotkey scripts

3. **AutoHotkey Integration**:
   - Read state file before actions
   - Make decisions based on state
   - No detection needed - just read state

### Benefits

- ✅ Real-time state tracking
- ✅ No detection overhead
- ✅ More reliable than detection
- ✅ Can track multiple state variables
- ✅ Foundation for future automation

### Implementation

**Python Script**:
```python
# cursor_state_tracker.py
import json
import time
from pathlib import Path

def track_cursor_state():
    state = {
        "chat_focused": check_chat_focus(),
        "chat_has_content": check_chat_content(),
        "agent_running": check_agent_state(),
        "layout_mode": check_layout_mode(),
        "timestamp": time.time()
    }

    # Write to state file
    state_file = Path(temp_dir) / "cursor_state.json"
    state_file.write_text(json.dumps(state))
```

**AutoHotkey Integration**:
```autohotkey
ReadState() {
    FileRead, stateJson, %A_Temp%\cursor_state.json
    ; Parse JSON and return state object
    return ParseJSON(stateJson)
}
```

---

## 💡 Proposal 5: Cursor IDE Extension

### Concept

Create Cursor IDE extension that provides keyboard shortcut handlers and state API.

### Capabilities

- Register custom keyboard shortcuts
- Provide state API for external scripts
- Handle focus management
- Control agent programmatically
- Expose events for state changes

### Benefits

- ✅ Direct API access
- ✅ Native integration
- ✅ No workarounds
- ✅ Better state detection
- ✅ Event-driven architecture

### Implementation

**Extension Structure**:
```typescript
// cursor-shortcuts extension
export function activate(context: vscode.ExtensionContext) {
    // Register commands
    vscode.commands.registerCommand('lumina.doit', () => {
        // Execute /doit
    });

    // Provide state API
    vscode.commands.registerCommand('lumina.getState', () => {
        return {
            chatFocused: isChatFocused(),
            chatContent: getChatContent(),
            agentRunning: isAgentRunning()
        };
    });
}
```

**Status**: 🔄 **RESEARCH NEEDED** - Requires VS Code extension API knowledge

---

## 🎯 Recommended Implementation Plan

### Phase 1: Quick Wins (This Week)

1. **Remove Ctrl+L from F23** ✅ **HIGH PRIORITY**
   - Detect layout before focusing
   - Only focus if in editor mode
   - **Impact**: Prevents layout switching

2. **Add Smart Focus to Right Alt** ✅ **MEDIUM PRIORITY**
   - Check focus state before focusing
   - Use state file or window detection
   - **Impact**: Reduces manual steps

### Phase 2: Better Detection (Next Week)

3. **Implement State File System** 🔄 **MEDIUM PRIORITY**
   - Create Python state tracker
   - Update state file continuously
   - AutoHotkey reads state file
   - **Impact**: More reliable detection

4. **Replace Clipboard Method** 🔄 **MEDIUM PRIORITY**
   - Use state file instead of clipboard
   - More reliable, no clipboard impact
   - **Impact**: Better detection, no side effects

### Phase 3: API Integration (Future)

5. **Research Cursor IDE Extension API** 🔄 **LOW PRIORITY**
   - Investigate VS Code extension API
   - Design extension architecture
   - **Impact**: Foundation for full automation

6. **Implement Extension** 🔄 **LOW PRIORITY**
   - Create Cursor IDE extension
   - Provide state API
   - **Impact**: Complete automation

---

## 📊 Comparison Matrix

| Proposal | Complexity | Reliability | Impact | Priority |
|----------|-----------|-------------|--------|----------|
| **Smart Focus (Right Alt)** | Low-Medium | High | Medium | 🟠 High |
| **Better Detection (F23)** | Medium | High | Medium | 🟠 High |
| **Layout-Safe Focus (F23)** | Medium | High | High | 🔴 Critical |
| **Python State Bridge** | Medium | Very High | High | 🟡 Medium |
| **Cursor IDE Extension** | High | Very High | Very High | 🟢 Low (Future) |

---

## ✅ Recommendations Summary

### Immediate (This Week)

1. ✅ **Remove Ctrl+L from F23** - Prevent layout switching
2. ✅ **Add Smart Focus to Right Alt** - Reduce manual steps

### Short-Term (Next 2 Weeks)

3. ✅ **Implement State File System** - Better state tracking
4. ✅ **Replace Clipboard Method** - More reliable detection

### Long-Term (Future)

5. ✅ **Research Extension API** - Foundation for automation
6. ✅ **Implement Extension** - Complete automation

---

## 📝 Questions for Consideration

1. **Q**: Should we prioritize layout switching fix (F23) or smart focus (Right Alt)?
   - **Recommendation**: Layout switching fix first (higher user impact)

2. **Q**: Is Python state bridge worth the complexity?
   - **Recommendation**: Yes - provides foundation for future automation

3. **Q**: Should we pursue Cursor IDE extension now or later?
   - **Recommendation**: Later - research first, implement after stopgaps improved

4. **Q**: Can we use voice commands as alternative?
   - **Recommendation**: Yes - good complement to physical keys

---

**Status**: 📋 **PROPOSALS READY - AWAITING DECISION**
**Next Action**: Review proposals and prioritize implementation
**Tags**: `#AUTOMATION` `#IMPROVEMENTS` `#PROPOSALS` `@LUMINA` `@JARVIS` `#PEAK`
