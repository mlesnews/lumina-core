# Cursor IDE UI Auto-Hide Implementation

**Date**: 2026-01-04  
**Status**: 🚧 **IN PROGRESS**  
**Tags**: #CURSOR #UI #AUTO_HIDE #QUALITY_OF_LIFE @JARVIS @LUMINA

---

## Overview

Implement auto-hide functionality for Cursor IDE UI sections to reduce visual clutter and improve focus. Sections auto-hide unless actively hovered over.

---

## Features

### 1. Top Header Bar Auto-Hide
- **Location**: Top header bar (File, Edit, Selection, View, etc.)
- **Behavior**: Hides after 2 seconds of no hover, shows on hover
- **Exception**: Always visible when active/editing

### 2. Chat Pane Details Auto-Hide
- **Location**: Chat interface pane
- **Sections**:
  - Lines added (green) / removed (red) box
  - Model mode selection (e.g., "Lava")
- **Behavior**: Hides after 3 seconds of no hover, shows on hover

### 3. Bird Static Text Collapse
- **Location**: Static text showing original ask/AI token request/task description
- **Behavior**: 
  - Collapses to one line with preview text ("Original task: ...")
  - Expands on hover to show full content
  - Hides after 5 seconds of no hover

### 4. Bottom Transcription Area
- **Status**: Stays visible (disabled auto-hide by default)
- **Reason**: Active use area - should remain accessible

---

## Transcription Improvements

### Pause/Resume Functionality
- **Problem**: Currently can't pause/resume without losing text
- **Solution**: 
  - Add pause button that preserves current text
  - Resume button restores text and continues transcription
  - Keyboard shortcut: `Ctrl+Space`

### Auto-Send After Silence
- **Problem**: Manual send required (Enter or Send button)
- **Solution**: 
  - Auto-send after 2 seconds of silence
  - Only if transcription length >= 10 characters
  - Toggle with `Ctrl+Shift+S`

### Expanded Button Controls
- **Problem**: Limited buttons (stop/send/play only)
- **Solution**: 
  - Wider, expanded button set:
    - Pause
    - Resume
    - Stop
    - Send
    - Clear
    - Save Draft
  - Horizontal layout with comfortable spacing
  - Large button size for easier clicking

---

## Implementation Status

### ✅ Completed
- Configuration file created (`config/cursor_ui_auto_hide_config.json`)
- Extension script created (`scripts/python/cursor_ui_auto_hide_extension.py`)
- CSS/JavaScript generation functions
- Extension manifest structure

### 🚧 In Progress
- CSS/JavaScript injection into Cursor IDE
- Transcription pause/resume API integration
- Button control expansion
- Auto-send functionality

### ⏳ Pending
- Cursor IDE extension packaging
- Testing auto-hide behavior
- User testing and feedback
- Performance optimization

---

## Technical Details

### CSS Injection
- Uses CSS transitions for smooth hide/show
- Opacity and transform animations
- Hover states for immediate show

### JavaScript Injection
- Event listeners for mouse enter/leave
- Timers for auto-hide delays
- Transcription state management
- Auto-send timer logic

### Extension Structure
- VS Code/Cursor extension format
- Commands for toggle, pause, resume
- Keyboard shortcuts integration
- Settings configuration

---

## Usage

### Generate CSS
```bash
python scripts/python/cursor_ui_auto_hide_extension.py --generate-css
```

### Generate JavaScript
```bash
python scripts/python/cursor_ui_auto_hide_extension.py --generate-js
```

### Generate Extension Manifest
```bash
python scripts/python/cursor_ui_auto_hide_extension.py --generate-manifest
```

### Show Implementation Guide
```bash
python scripts/python/cursor_ui_auto_hide_extension.py --guide
```

---

## Next Steps

1. **Test CSS/JavaScript injection** - Verify auto-hide works in Cursor IDE
2. **Create extension package** - Package as Cursor IDE extension
3. **Implement transcription API** - Integrate pause/resume with Cursor API
4. **Add button controls** - Expand button set in UI
5. **User testing** - Get feedback on auto-hide behavior

---

## Configuration

Edit `config/cursor_ui_auto_hide_config.json` to customize:
- Hide delays
- Which sections auto-hide
- Transcription settings
- Button controls

---

**Tags**: #CURSOR #UI #AUTO_HIDE #QUALITY_OF_LIFE #TRANSCRIPTION @JARVIS @LUMINA
