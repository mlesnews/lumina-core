# Cursor IDE Keyboard Shortcuts - Complete Mapping

## Overview

Complete mapping of all Cursor IDE keyboard shortcuts for all function keys (@FF).

## Function Keys (@FF)

| Key | Default Action | Alternate | Category |
|-----|---------------|-----------|----------|
| F1 | Show Command Palette | Toggle Help | navigation |
| F2 | Rename Symbol | Quick Rename | refactoring |
| F3 | Find Next | Go to Next Search Result | navigation |
| F4 | Go to Definition | Peek Definition | navigation |
| F5 | Start Debugging | Continue | debugging |
| F6 | Step Over | Next Line | debugging |
| F7 | Step Into | Step In | debugging |
| F8 | Step Out | Step Return | debugging |
| F9 | Toggle Breakpoint | Add/Remove Breakpoint | debugging |
| F10 | Step Over (Alternative) | Next Statement | debugging |
| F11 | Toggle Full Screen | Zen Mode | view |
| F12 | Go to Definition | Peek Definition | navigation |

## Function Key Combinations

### Ctrl Combinations

- **Ctrl+F1**: Toggle Terminal
- **Ctrl+F2**: Toggle Sidebar
- **Ctrl+F3**: Find in Files
- **Ctrl+F4**: Close Editor
- **Ctrl+F5**: Restart Debugging
- **Ctrl+F12**: Go to Implementation

### Shift Combinations

- **Shift+F1**: Show All Commands
- **Shift+F2**: Find Previous
- **Shift+F3**: Find Previous
- **Shift+F4**: Find Previous
- **Shift+F5**: Stop Debugging
- **Shift+F11**: Exit Full Screen
- **Shift+F12**: Go to References

### Alt Combinations

- **Alt+F1**: Show Accessibility Options
- **Alt+F4**: Close Window (Windows standard)
- **Alt+F12**: Peek Definition

## Cursor-Specific Shortcuts

- **Ctrl+K Ctrl+S**: Open Keyboard Shortcuts
- **Ctrl+Shift+P**: Command Palette
- **Ctrl+P**: Quick Open
- **Ctrl+Shift+F**: Search in Files
- **Ctrl+`**: Toggle Terminal
- **Ctrl+B**: Toggle Sidebar

## AI-Specific Shortcuts (Cursor AI)

- **Ctrl+L**: Open Chat (Cursor AI)
- **Ctrl+K**: Inline Edit (Cursor AI)
- **Ctrl+I**: Composer (Cursor AI)
- **Ctrl+Shift+L**: Chat History

## Hardware Conflicts

### fn+F4 (ASUS AURA Lighting Control)

- **Hardware Action**: ASUS AURA Lighting Control
- **IDE Action**: Go to Definition
- **Conflict**: Hardware-level shortcut takes precedence
- **Solution**: Disable hardware lighting or use Ctrl+F4 for IDE action
- **Note**: This is the persistent lock issue we're addressing

### fn+F11 (Some Laptops)

- **Hardware Action**: Toggle Full Screen (some laptops)
- **IDE Action**: Toggle Full Screen
- **Conflict**: May conflict with IDE full screen
- **Solution**: Use F11 directly or configure hardware

## Customization

All shortcuts can be customized in Cursor IDE settings:

- **Settings Path**: File > Preferences > Keyboard Shortcuts
- **Keybindings File**: `.cursor/keybindings.json`

## Usage

View the complete mapping:

```bash
python scripts/python/jarvis_cursor_shortcuts_mapper.py
```

## Configuration

The mapping is stored in:
- **Config File**: `config/cursor_ide_keyboard_shortcuts.json`

## Tags

`@FF` `@CURSOR` `@IDE` `@KEYBOARD` `@SHORTCUTS` `@MAPPING`
