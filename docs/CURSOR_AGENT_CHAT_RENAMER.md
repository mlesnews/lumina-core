# Cursor Agent Chat History Renamer - Dynamic Scaling

**Status**: ✅ OPERATIONAL  
**Purpose**: Automatically rename active Cursor IDE agent chat histories with dynamic scaling based on activity

---

## 🎯 Overview

Renames agent chat histories in Cursor IDE dynamically:
- **Baseline**: 30 minutes
- **Active work**: Extends to 1 hour or longer
- **Activity reset**: Like screensaver - resets timer on activity (20 min window)
- **Monitors**: All agent chats (pinned and unpinned)

**Location in Cursor IDE**: 
- New Agent button → Pinned agents / More (three dots) → All agent chats

---

## 🔄 How It Works

### Dynamic Scaling

1. **Baseline Interval**: 30 minutes
   - Default rename interval for idle chats

2. **Active Extension**: Up to 1+ hour
   - When actively working, extends interval
   - Adds 15 minutes per rename cycle (max 1 hour extension)

3. **Activity Reset** (Screensaver Concept):
   - 20-minute activity window
   - Any activity in last 20 minutes resets timer
   - Like a screensaver - activity prevents timeout

### Activity Detection

Checks for activity by:
- File modification time (recent changes)
- File size changes
- Recent activity in tracking log

### Rename Strategy

Generates names from:
- First user message content (first 50 chars)
- Timestamp
- Status (ACTIVE/IDLE)

Example: `Add_SYPHON_video_audio_20251228_0325_ACTIVE`

---

## 🚀 Usage

### Run Once

```bash
python scripts/python/cursor_agent_chat_renamer.py
```

### Run as Background Service

```bash
python scripts/python/cursor_agent_chat_renamer_service.py
```

### VSCode Tasks

- `💬 Cursor Agent Chat: Start Renamer (Background)` - Runs continuously in background
- `💬 Cursor Agent Chat: Run Renamer Once` - Single check and rename

---

## 📋 Configuration

```python
baseline_interval = 30 * 60      # 30 minutes
active_extension = 60 * 60       # 1 hour when active
activity_reset_window = 20 * 60  # 20 minutes (screensaver)
max_interval = 2 * 60 * 60       # 2 hours max
```

---

## 📁 Storage Locations

Cursor IDE stores chat histories in:
- `%LOCALAPPDATA%\Cursor\User\globalStorage\...`
- `%APPDATA%\Cursor\User\globalStorage\...`
- `~/.cursor/User/globalStorage/...`

Script automatically detects the correct location.

---

## 🔍 Features

1. **Automatic Detection** - Finds Cursor chat history directory
2. **Activity Tracking** - Monitors file modification times
3. **Dynamic Scaling** - Adjusts intervals based on activity
4. **Screensaver Logic** - Resets timer on activity
5. **Meaningful Names** - Creates names from chat content

---

## 📊 Monitoring

The script logs:
- Found chat files
- Rename operations
- Activity detection
- Interval calculations

---

**Status**: Ready for use  
**Last Updated**: 2025-01-28  
**Maintained By**: JARVIS, MARVIN, Human Operator

