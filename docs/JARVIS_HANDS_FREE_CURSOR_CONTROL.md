# 🎤 JARVIS Hands-Free Cursor Control

## Overview

Complete hands-free conversation system where JARVIS controls Cursor IDE automatically. No clicking required - voice commands are processed and executed via **keyboard shortcuts** (primary) with **mouse control** as backup.

## Architecture

```
🎤 Voice Input → JARVIS Processing → Cursor IDE Control
                                          ↓
                              ⌨️ Keyboard Shortcuts (Primary)
                                      ↓
                              🖱️ Mouse Control (Backup)
```

## Features

✅ **Hands-Free Operation** - No clicking required  
✅ **Voice Commands** - Natural language control  
✅ **Keyboard Shortcuts** - Fast, reliable execution  
✅ **Mouse Fallback** - Automatic fallback if keyboard fails  
✅ **Intelligent Parsing** - Understands natural language commands  
✅ **Voice Responses** - JARVIS speaks back to confirm actions  

## Quick Start

### 1. Start Hands-Free Mode

```bash
python scripts/python/jarvis_conversation_cursor_bridge.py --start
```

### 2. Execute Single Command

```bash
python scripts/python/jarvis_conversation_cursor_bridge.py --command "open chat"
```

### 3. Test Keyboard Shortcuts

```bash
python scripts/python/jarvis_conversation_cursor_bridge.py --test
```

## Available Commands

### Chat & Conversation
- **"open chat"** / **"start chat"** → Opens Cursor chat (`Ctrl+L`)
- **"open composer"** → Opens Cursor Composer (`Ctrl+I`)

### File Operations
- **"open file"** → Opens file dialog (`Ctrl+P`)
- **"new file"** → Creates new file (`Ctrl+N`)
- **"save file"** / **"save"** → Saves current file (`Ctrl+S`)
- **"close file"** → Closes current file (`Ctrl+W`)

### Code Actions
- **"format code"** / **"format"** → Formats document (`Shift+Alt+F`)
- **"comment"** / **"comment out"** → Comments/uncomments line (`Ctrl+/`)

### Navigation
- **"go to definition"** / **"definition"** → Navigates to definition (`F12`)
- **"go to references"** → Shows references (`Shift+F12`)

### Terminal
- **"toggle terminal"** / **"terminal"** → Toggles terminal (`Ctrl+``)
- **"new terminal"** → Opens new terminal (`Ctrl+Shift+``)

### Debug
- **"start debug"** / **"debug"** → Starts debugging (`F5`)
- **"stop debug"** → Stops debugging (`Shift+F5`)
- **"toggle breakpoint"** → Toggles breakpoint (`F9`)

## Keyboard Shortcuts Reference

All shortcuts are executed via `pynput` keyboard controller:

| Action | Shortcut | Command |
|--------|----------|---------|
| Open Chat | `Ctrl+L` | "open chat" |
| Composer | `Ctrl+I` | "open composer" |
| Open File | `Ctrl+P` | "open file" |
| New File | `Ctrl+N` | "new file" |
| Save File | `Ctrl+S` | "save file" |
| Format Code | `Shift+Alt+F` | "format code" |
| Comment Line | `Ctrl+/` | "comment" |
| Go to Definition | `F12` | "go to definition" |
| Toggle Terminal | `Ctrl+` ` | "toggle terminal" |
| Start Debug | `F5` | "start debug" |

## System Components

### 1. KeyboardShortcutExecutor

Primary execution engine that:
- Finds and activates Cursor window
- Executes keyboard shortcuts via `pynput`
- Falls back to mouse if keyboard fails
- Handles modifier keys correctly

**Location**: `jarvis_hands_free_cursor_control.py`

### 2. JARVISHandsFreeCursorControl

Main control system that:
- Parses voice commands into intents
- Generates action sequences
- Executes via keyboard shortcuts
- Provides voice responses

**Location**: `jarvis_hands_free_cursor_control.py`

### 3. JARVISConversationCursorBridge

Bridge between voice and Cursor that:
- Integrates with JARVIS voice interface
- Processes commands continuously
- Maintains conversation context

**Location**: `jarvis_conversation_cursor_bridge.py`

## Usage Examples

### Example 1: Open Chat and Type

```bash
# Open chat
python scripts/python/jarvis_conversation_cursor_bridge.py --command "open chat"

# In hands-free mode, after chat opens:
# Say: "create a new function that..."
# JARVIS will type your request into the chat
```

### Example 2: Format Code

```bash
python scripts/python/jarvis_conversation_cursor_bridge.py --command "format code"
```

### Example 3: Debug Session

```bash
python scripts/python/jarvis_conversation_cursor_bridge.py --command "start debug"
```

## Integration with Voice Interface

The system integrates with `JARVISVoiceActivated` for full hands-free operation:

1. **Voice Input** → Azure Speech-to-Text
2. **Intent Parsing** → Natural language understanding
3. **Action Generation** → Keyboard shortcut mapping
4. **Execution** → Automated Cursor control
5. **Voice Response** → Text-to-Speech confirmation

## Mouse Fallback

When keyboard shortcuts fail, the system automatically falls back to mouse control:

- Finds UI elements via screen coordinates
- Clicks buttons and menu items
- Navigates menus when needed

**Note**: Mouse fallback is less reliable than keyboard shortcuts and should only be used when keyboard fails.

## Technical Details

### Dependencies

```python
pynput          # Keyboard and mouse control
pygetwindow     # Window management
jarvis_voice_activated  # Voice interface
manus_cursor_controller  # MANUS framework
```

### Window Detection

The system finds Cursor windows by:
1. Exact title match: "Cursor"
2. Case-insensitive match: "cursor"
3. Partial match in all windows

### Keyboard Execution

1. Release all modifier keys
2. Press modifier keys in order
3. Press regular keys with delays
4. Release modifiers in reverse order
5. Wait for action completion

## Troubleshooting

### Keyboard Shortcuts Not Working

1. **Check Window Focus**: Ensure Cursor window is active
2. **Verify Shortcuts**: Some shortcuts may differ by OS/configuration
3. **Check Permissions**: `pynput` may need permissions on macOS/Linux

### Mouse Fallback Issues

- Mouse fallback requires accurate screen coordinates
- May fail if UI layout changes
- Use keyboard shortcuts as primary method

### Voice Not Working

- Ensure Azure Speech credentials are configured
- Check microphone permissions
- Verify voice interface is initialized

## Advanced Usage

### Custom Shortcuts

Add custom shortcuts to `KeyboardShortcutExecutor.CURSOR_SHORTCUTS`:

```python
CURSOR_SHORTCUTS = {
    "custom_action": [Key.ctrl, Key.shift, 'c'],
    ...
}
```

### Custom Commands

Add command parsing logic in `_parse_command_intent()`:

```python
if "custom action" in command_lower:
    intent["type"] = "custom_action"
    intent["action"] = "custom_action"
```

## Status

✅ **Fully Operational**

- Keyboard shortcut execution: ✅ Working
- Voice command parsing: ✅ Working
- Mouse fallback: ✅ Implemented
- Integration with JARVIS: ✅ Complete

## Next Steps

1. **Continuous Voice Mode**: Full integration with voice interface for hands-free conversations
2. **More Commands**: Expand command vocabulary
3. **Context Awareness**: Remember previous actions and state
4. **Multi-Step Actions**: Complex workflows via voice

## Files

- `jarvis_hands_free_cursor_control.py` - Core control system
- `jarvis_conversation_cursor_bridge.py` - Voice-Cursor bridge
- `manus_cursor_controller.py` - MANUS framework integration

---

**Created**: 2025-12-31  
**Status**: ✅ Operational  
**Primary Method**: Keyboard Shortcuts  
**Backup Method**: Mouse Control
