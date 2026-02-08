# Cursor Auto-Accept & Notification Relocation

**Fixing Manual "Keep All" Clicks & Notification Positioning**

---

## 🎯 Problems Solved

### 1. Manual "Keep All" Button Clicking

**Problem**: Still had to manually click "Keep All" / "Accept Changes" in Cursor IDE.

**Solution**: Automatic acceptance using UI automation and #DECISIONING workflow.

**File**: `scripts/python/cursor_ide_auto_accept.py`

**Features**:
- ✅ Automatically detects "Keep All" / "Accept Changes" dialog
- ✅ Uses #DECISIONING workflow to make decision
- ✅ Clicks button automatically (no manual intervention)
- ✅ Can monitor continuously or check once

**Usage**:
```bash
# Check once
python scripts/python/cursor_ide_auto_accept.py --once

# Monitor continuously (runs in background)
python scripts/python/cursor_ide_auto_accept.py --monitor --interval 2.0
```

---

### 2. Notification Relocation

**Problem**: Notifications still blocking:
- Cursor IDE microphone recording indicator (top-left)
- Voice input area (top area)
- General screen area

**Solution**: Notifications now positioned in **bottom-right corner** (safe zone).

**File**: `scripts/python/lumina_notification_system.py`

**Changes Made**:
- ✅ Uses `winotify` (better positioning) or `win10toast` (fallback)
- ✅ Windows toast notifications appear in bottom-right by default
- ✅ Away from:
  - Top-left: Recording indicator
  - Top area: Cursor IDE
  - Bottom-right: Safe zone (notifications)

**Positioning**:
- **X**: Right edge
- **Y**: Bottom (above taskbar)
- **Offset**: 20px from right, 80px from bottom

---

## 🔧 Implementation

### Auto-Accept System

**How It Works**:
1. Monitors Cursor IDE window for "Keep All" / "Accept Changes" buttons
2. Uses `pywinauto` to find button
3. Uses #DECISIONING engine to make decision
4. Automatically clicks button
5. Saves state (all work preserved)

**Integration**:
- Works with `lumina_decisioning_engine.py`
- Tracks decisions in history
- Always saves state before accepting

### Notification System

**How It Works**:
1. Uses Windows toast notification API
2. Appears in bottom-right (system default)
3. Doesn't block UI elements
4. Falls back to logging if UI unavailable

**Installation**:
```bash
pip install winotify
# or
pip install win10toast
```

---

## 🚀 Usage

### Auto-Accept

**One-time check**:
```bash
python scripts/python/cursor_ide_auto_accept.py --once
```

**Continuous monitoring** (recommended):
```bash
python scripts/python/cursor_ide_auto_accept.py --monitor
```

**Add to startup** (optional):
- Add to Windows startup
- Runs in background
- Automatically accepts changes

### Notifications

**Show notification**:
```python
from lumina_notification_system import LuminaNotificationSystem

notification = LuminaNotificationSystem()
notification.show_notification(
    title="LUMINA",
    message="Changes accepted automatically",
    notification_type="info"
)
```

---

## ✅ Status

- ✅ Auto-accept system created
- ✅ Notification relocation implemented
- ✅ Bottom-right positioning (safe zone)
- ⚠️ **Testing Needed**: Verify auto-accept works in real scenarios
- ⚠️ **Installation Needed**: `pip install pyautogui pywinauto winotify`

---

**Tags**: `#CURSOR_IDE #AUTOMATION #NOTIFICATIONS #DECISIONING @JARVIS @LUMINA`
