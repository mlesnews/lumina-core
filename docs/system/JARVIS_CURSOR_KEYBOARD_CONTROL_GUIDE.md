# JARVIS-Cursor IDE Complete Keyboard Control Guide

**Date**: 2025-01-24  
**Status**: ✅ **FULLY INTEGRATED**  
**Version**: 1.0.0

---

## Overview

Complete integration between **JARVIS Full-Time Super Agent** and **Cursor IDE**, enabling **100% keyboard-based control** with **zero mouse clicking required**. All Cursor IDE commands are accessible via natural language voice/text commands that map to keyboard shortcuts or command palette commands.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  JARVIS Full-Time Super Agent                │
│  (Voice/Text Commands)                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│      JARVIS-Cursor IDE Keyboard Integration Bridge           │
│  • Natural Language Parsing                                  │
│  • Command Mapping                                           │
│  • Intelligent Routing                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Keyboard   │ │   Command    │ │    MANUS     │
│  Shortcuts   │ │   Palette    │ │  Controller  │
│   (Primary)  │ │  (Fallback)  │ │  (Complex)   │
└──────────────┘ └──────────────┘ └──────────────┘
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      Cursor IDE                              │
│  Complete Control - No Mouse Required                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Features

### ✅ Complete Keyboard Control
- **All Cursor IDE commands** accessible via keyboard shortcuts
- **Command palette** fallback for commands without direct shortcuts
- **Zero mouse clicking** required
- **Natural language** command parsing

### ✅ Intelligent Command Routing
1. **Primary**: Direct keyboard shortcuts
2. **Secondary**: Command palette commands
3. **Tertiary**: MANUS controller for complex workflows
4. **Fallback**: Command palette with fuzzy matching

### ✅ Natural Language Support
- **Voice commands** from JARVIS
- **Text commands** from JARVIS
- **Intuitive aliases** for all commands
- **Fuzzy matching** for command recognition

---

## Usage

### Basic Usage

```python
from jarvis_cursor_ide_keyboard_integration import get_jarvis_cursor_integration

# Get integration instance
integration = get_jarvis_cursor_integration()

# Execute command (natural language)
result = integration.execute_command("open chat")
result = integration.execute_command("save file")
result = integration.execute_command("format code")

# Process command from JARVIS
result = integration.process_jarvis_command("open composer")
```

### Command Categories

#### File Operations
- `"create file"`, `"new file"` → Create new file
- `"open file"`, `"browse file"` → Open file dialog
- `"save"`, `"save file"` → Save current file
- `"save all"` → Save all files
- `"close file"`, `"close tab"` → Close current file
- `"close all"` → Close all files
- `"reopen file"`, `"undo close"` → Reopen closed file

#### Editing Operations
- `"undo"`, `"reverse"` → Undo last change
- `"redo"` → Redo last change
- `"cut"` → Cut selection
- `"copy"` → Copy selection
- `"paste"` → Paste
- `"select all"` → Select all text
- `"find"`, `"search"` → Find text
- `"replace"`, `"find and replace"` → Replace text
- `"find in files"`, `"global search"` → Find in all files
- `"goto line"`, `"line number"` → Go to line number
- `"delete line"` → Delete current line
- `"move line up"` → Move line up
- `"move line down"` → Move line down
- `"duplicate line"` → Duplicate line
- `"comment"`, `"toggle comment"` → Comment/uncomment line
- `"format"`, `"format code"`, `"beautify"` → Format code

#### Navigation
- `"definition"`, `"go to definition"` → Go to definition
- `"peek definition"` → Peek definition
- `"references"`, `"find references"` → Show references
- `"back"`, `"go back"` → Navigate back
- `"forward"`, `"go forward"` → Navigate forward
- `"next tab"`, `"next file"` → Next tab
- `"previous tab"`, `"prev file"` → Previous tab
- `"symbol"`, `"go to symbol"` → Go to symbol in file

#### Cursor AI Operations
- `"chat"`, `"open chat"`, `"cursor chat"` → Open Cursor chat
- `"composer"`, `"cursor composer"` → Open Cursor Composer
- `"inline chat"` → Open inline chat
- `"accept"`, `"accept suggestion"` → Accept AI suggestion
- `"dismiss"`, `"reject"` → Dismiss AI suggestion
- `"autocomplete"`, `"suggest"` → Trigger autocomplete

#### View/Panel Operations
- `"command palette"`, `"palette"` → Open command palette
- `"sidebar"`, `"toggle sidebar"` → Toggle sidebar
- `"explorer"`, `"file explorer"` → Focus file explorer
- `"search"`, `"search view"` → Focus search
- `"git"`, `"source control"` → Focus source control
- `"extensions"`, `"plugins"` → Focus extensions
- `"terminal"`, `"console"` → Toggle terminal
- `"output"`, `"log"` → Focus output panel
- `"problems"`, `"errors"` → Focus problems panel
- `"zoom in"` → Zoom in
- `"zoom out"` → Zoom out
- `"reset zoom"` → Reset zoom

#### Debug Operations
- `"debug"`, `"start debug"` → Start debugging
- `"stop debug"` → Stop debugging
- `"breakpoint"`, `"toggle breakpoint"` → Toggle breakpoint
- `"step over"`, `"next line"` → Step over
- `"step into"`, `"enter function"` → Step into
- `"step out"`, `"exit function"` → Step out

#### Git Operations (via Command Palette)
- `"stage all"`, `"git stage"` → Stage all changes
- `"unstage all"` → Unstage all changes
- `"commit"`, `"git commit"` → Commit changes
- `"push"`, `"git push"` → Push to remote
- `"pull"`, `"git pull"` → Pull from remote
- `"sync"`, `"git sync"` → Sync repository

#### Advanced Operations
- `"rename"`, `"refactor rename"` → Rename symbol
- `"quick fix"`, `"code actions"` → Show quick fix
- `"organize imports"`, `"sort imports"` → Organize imports
- `"reveal file"`, `"show in explorer"` → Reveal file in explorer
- `"word wrap"` → Toggle word wrap
- `"zen mode"` → Toggle zen mode

---

## Integration with JARVIS

### Voice Commands

JARVIS Full-Time Super Agent can process voice commands and execute them in Cursor IDE:

```python
# JARVIS processes voice command
jarvis_command = "open chat and ask about the code"

# Integration executes command
result = integration.process_jarvis_command(jarvis_command)
```

### Text Commands

JARVIS can also process text commands:

```python
# From JARVIS conversation
text_command = "format the current file and save it"

# Execute via integration
result = integration.execute_command(text_command, async_execution=True)
```

---

## Keyboard Shortcuts Reference

### File Operations
| Command | Shortcut | Aliases |
|---------|----------|---------|
| New File | `Ctrl+N` | create file, new file, new |
| Open File | `Ctrl+P` | open file, open, file picker |
| Save | `Ctrl+S` | save, save file |
| Save All | `Ctrl+K S` | save all, save everything |
| Close Editor | `Ctrl+W` | close, close file, close tab |
| Close All | `Ctrl+K W` | close all, close everything |
| Reopen Closed | `Ctrl+Shift+T` | reopen, undo close |

### Editing
| Command | Shortcut | Aliases |
|---------|----------|---------|
| Undo | `Ctrl+Z` | undo, reverse |
| Redo | `Ctrl+Y` | redo, repeat |
| Cut | `Ctrl+X` | cut |
| Copy | `Ctrl+C` | copy |
| Paste | `Ctrl+V` | paste |
| Select All | `Ctrl+A` | select all |
| Find | `Ctrl+F` | find, search |
| Replace | `Ctrl+H` | replace, find and replace |
| Find in Files | `Ctrl+Shift+F` | find in files, global search |
| Go to Line | `Ctrl+G` | goto line, line number |
| Delete Line | `Ctrl+Shift+K` | delete line |
| Move Line Up | `Alt+Up` | move line up |
| Move Line Down | `Alt+Down` | move line down |
| Comment Line | `Ctrl+/` | comment, toggle comment |
| Format Document | `Shift+Alt+F` | format, format code, beautify |

### Navigation
| Command | Shortcut | Aliases |
|---------|----------|---------|
| Go to Definition | `F12` | definition, go to definition |
| Peek Definition | `Alt+F12` | peek definition |
| Show References | `Shift+F12` | references, find references |
| Go Back | `Ctrl+Alt+-` | back, go back |
| Go Forward | `Ctrl+Shift+-` | forward, go forward |
| Next Editor | `Ctrl+PageDown` | next tab, next file |
| Previous Editor | `Ctrl+PageUp` | previous tab, prev file |

### Cursor AI
| Command | Shortcut | Aliases |
|---------|----------|---------|
| Cursor Chat | `Ctrl+L` | chat, open chat, cursor chat |
| Cursor Composer | `Ctrl+I` | composer, cursor composer |
| Inline Chat | `Ctrl+K` | inline chat, code chat |
| Accept Suggestion | `Tab` | accept, accept suggestion |
| Dismiss Suggestion | `Esc` | dismiss, reject |

### View/Panels
| Command | Shortcut | Aliases |
|---------|----------|---------|
| Command Palette | `Ctrl+Shift+P` | command palette, palette |
| Toggle Sidebar | `Ctrl+B` | sidebar, toggle sidebar |
| Toggle Explorer | `Ctrl+Shift+E` | explorer, file explorer |
| Toggle Search | `Ctrl+Shift+F` | search, search view |
| Toggle Git | `Ctrl+Shift+G` | git, source control |
| Toggle Terminal | `Ctrl+` ` | terminal, console |
| Toggle Output | `Ctrl+Shift+U` | output, log |
| Toggle Problems | `Ctrl+Shift+M` | problems, errors |

### Debug
| Command | Shortcut | Aliases |
|---------|----------|---------|
| Start Debugging | `F5` | debug, start debug |
| Stop Debugging | `Shift+F5` | stop debug |
| Toggle Breakpoint | `F9` | breakpoint, toggle breakpoint |
| Step Over | `F10` | step over, next line |
| Step Into | `F11` | step into, enter function |
| Step Out | `Shift+F11` | step out, exit function |

---

## Command Palette Commands

Commands without direct keyboard shortcuts are accessible via Command Palette (`Ctrl+Shift+P`):

### Git Commands
- `Git: Stage All Changes`
- `Git: Unstage All Changes`
- `Git: Commit`
- `Git: Push`
- `Git: Pull`
- `Git: Sync`
- `Git: Fetch`
- `Git: Create Branch`
- `Git: Checkout to`
- `Git: Merge Branch`

### Python Commands
- `Python: Select Interpreter`
- `Python: Create Terminal`
- `Python: Run Python File in Terminal`
- `Python: Run Selection/Line in Python Terminal`
- `Python: Debug Python File`

### Refactoring Commands
- `Refactor: Extract Function`
- `Refactor: Extract Variable`
- `Refactor: Extract Constant`

### View Commands
- `View: Split Editor`
- `View: Split Editor Right`
- `View: Join Editor Group`
- `View: Close Editor Group`
- `Preferences: Open Settings`
- `Preferences: Open Keyboard Shortcuts`

### Developer Commands
- `Developer: Reload Window`
- `Developer: Toggle Developer Tools`
- `Developer: Show Logs`

---

## Natural Language Patterns

The integration recognizes various natural language patterns:

### Common Prefixes (automatically removed)
- "please"
- "can you"
- "could you"
- "let me"
- "i want to"
- "i need to"
- "help me"

### Common Suffixes (automatically removed)
- "please"
- "now"
- "right now"

### Examples

```
"please open chat" → "open chat"
"can you save the file" → "save file"
"i want to format code now" → "format code"
"let me go to definition" → "definition"
```

---

## Advanced Features

### Async Command Execution

Commands can be queued for async execution:

```python
# Queue command for async execution
result = integration.execute_command("format code", async_execution=True)
# Returns immediately with queued status
```

### Command Search

Search for available commands:

```python
# Search commands
results = integration.search_commands("git")
for result in results:
    print(f"{result['name']}: {result['info']}")
```

### List All Commands

List all available commands, optionally filtered by category:

```python
# List all commands
all_commands = integration.get_available_commands()

# List commands by category
git_commands = integration.get_available_commands(category="git")
file_commands = integration.get_available_commands(category="file_operations")
```

---

## Configuration

### Keyboard Shortcuts Config

Keyboard shortcuts are configured in:
```
config/cursor_ide_complete_keyboard_shortcuts.json
```

This file contains:
- **All keyboard shortcuts** with key combinations
- **Command palette commands** for commands without shortcuts
- **Natural language aliases** for all commands
- **Command categories** for organization

### Customization

You can customize the keyboard shortcuts configuration:

1. Edit `config/cursor_ide_complete_keyboard_shortcuts.json`
2. Add new shortcuts or aliases
3. Restart the integration to load changes

---

## Integration Points

### With JARVIS Full-Time Super Agent

The integration connects to JARVIS for:
- **Voice command processing**
- **Text command processing**
- **Conversation context**
- **Command execution results**

### With MANUS Controller

The integration uses MANUS for:
- **Complex workflow execution**
- **Troubleshooting actions**
- **Decision-making support**

### With Cursor IDE Keyboard Controller

The integration uses the keyboard controller for:
- **Direct keyboard shortcut execution**
- **Command palette access**
- **Natural language command parsing**

---

## Best Practices

1. **Use Natural Language**: Prefer natural language commands over exact shortcut names
2. **Voice Commands**: Use voice commands for hands-free operation
3. **Async Execution**: Use async execution for non-blocking operations
4. **Error Handling**: Check `CommandExecutionResult.success` before proceeding
5. **Command Search**: Use `search_commands()` to discover available commands

---

## Troubleshooting

### Command Not Recognized

If a command is not recognized:
1. Check if the command exists in the mappings
2. Try different aliases or natural language variations
3. Use command search to find similar commands
4. Check command palette for the exact command name

### Command Execution Failed

If command execution fails:
1. Check if Cursor IDE window is active
2. Verify keyboard controller is initialized
3. Check error message in `CommandExecutionResult.error`
4. Try command palette fallback manually

### Integration Not Working

If integration is not working:
1. Verify all dependencies are installed (`pynput`, `pygetwindow`)
2. Check if Cursor IDE is running
3. Verify keyboard controller can find Cursor window
4. Check logs for error messages

---

## Future Enhancements

- [ ] Custom keyboard shortcut assignments
- [ ] Command history and replay
- [ ] Command macros and sequences
- [ ] Context-aware command suggestions
- [ ] Learning from user preferences
- [ ] Integration with more IDE features

---

## Related Documentation

- [JARVIS Full-Time Super Agent Guide](../system/JARVIS_REAL_TIME_CONVERSATION_GUIDE.md)
- [MANUS Cursor Controller](../system/MANUS_CURSOR_CONTROLLER.md)
- [Cursor IDE Keyboard Shortcuts Reference](../config/cursor_ide_complete_keyboard_shortcuts.json)

---

**Status**: ✅ **FULLY OPERATIONAL**

Complete keyboard control of Cursor IDE via JARVIS with natural language commands - **no mouse required**!
