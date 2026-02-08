# 🦾 IRON MAN Virtual Assistant - LUMINA Desktop Companion

**Status**: ✅ **READY**  
**Version**: 1.0.0  
**Date**: 2025-01-24

---

## Overview

The **IRON MAN Virtual Assistant** is a desktop companion inspired by Armory Crate's virtual assistant, but with a full IRON MAN theme, powercord tail, and comprehensive LUMINA ecosystem integration. It cycles through all IRONMAN (Mark I-VII) and ULTRON AI models, provides system monitoring, alerts, and full LUMINA feature access.

---

## ✨ Features

### Visual Design
- ✅ **IRON MAN Themed Appearance** - Orange-red and gold color scheme
- ✅ **Powercord Tail** - Animated powercord extending from IRON MAN
- ✅ **Arc Reactor** - Pulsing cyan arc reactor in center
- ✅ **Click-through Window** - Doesn't interfere with your work
- ✅ **Always on Top** - Always visible on your desktop
- ✅ **Smooth Animation** - Arc reactor pulse and powercord animation

### AI Model Cycling
- ✅ **IRONMAN Mark I-VII** - All KAIJU Iron Legion models
  - Mark I: codellama:13b (Primary code generation)
  - Mark II: llama3.2:11b (Secondary general)
  - Mark III: qwen2.5-coder:1.5b-base (Lightweight quick)
  - Mark IV: llama3:8b (General purpose)
  - Mark V: mistral:7b (General reasoning)
  - Mark VI: mixtral-8x7b (High complexity)
  - Mark VII: gemma:2b (Lightweight fallback)
- ✅ **ULTRON** - ULTRON Virtual Hybrid Cluster (qwen2.5:72b)
- ✅ **Automatic Cycling** - Cycles through models every 30 seconds
- ✅ **Click to Cycle** - Click IRON MAN to manually cycle models
- ✅ **Model Indicator** - Current model displayed below IRON MAN

### LUMINA Integration
- ✅ **JARVIS Integration** - Full JARVIS agent access
- ✅ **R5 System** - R5 Living Context Matrix monitoring
- ✅ **@helpdesk** - Helpdesk system status
- ✅ **ULTRON Cluster** - ULTRON status monitoring
- ✅ **KAIJU Iron Legion** - KAIJU cluster status monitoring
- ✅ **System Health Checks** - Automatic system status monitoring

### Alerts & Notifications
- ✅ **Multi-level Alerts** - INFO, WARNING, CRITICAL, SYSTEM
- ✅ **Visual Indicators** - Colored alert indicators
- ✅ **System Status Alerts** - Notifications when systems go online/offline
- ✅ **Alert Display** - Up to 3 most recent alerts shown
- ✅ **Alert Logging** - All alerts logged with timestamps

### Behavior
- ✅ **Wandering** - IRON MAN wanders around screen
- ✅ **Mouse Attraction** - Subtle attraction to mouse cursor
- ✅ **Idle Phrases** - Randomly speaks when idle
- ✅ **Voice Integration** - ElevenLabs TTS support (optional)
- ✅ **Conversation** - Can interact with JARVIS

---

## 🚀 Quick Start

### Start IRON MAN Virtual Assistant

```bash
python scripts/python/ironman_virtual_assistant.py --start
```

Or simply:

```bash
python scripts/python/ironman_virtual_assistant.py
```

---

## 🎯 How It Works

### AI Model Cycling

The assistant automatically cycles through all IRONMAN and ULTRON AI models:

1. **Automatic Cycling**: Every 30 seconds, cycles to next model
2. **Manual Cycling**: Click on IRON MAN to cycle immediately
3. **Model Display**: Current model shown below IRON MAN
4. **Alert Notification**: Alert shown when model changes

**Model Order**:
1. Mark I (codellama:13b)
2. Mark II (llama3.2:11b)
3. Mark III (qwen2.5-coder:1.5b-base)
4. Mark IV (llama3:8b)
5. Mark V (mistral:7b)
6. Mark VI (mixtral-8x7b)
7. Mark VII (gemma:2b)
8. ULTRON (qwen2.5:72b)
9. (Repeat cycle)

### System Monitoring

The assistant continuously monitors LUMINA systems:

- **JARVIS**: Checks JARVIS agent availability
- **R5**: Checks R5 API at `http://localhost:8000/r5/health`
- **ULTRON**: Checks local Ollama at `http://localhost:11434/api/tags`
- **KAIJU**: Checks KAIJU cluster at `http://10.17.17.32:11434/api/tags`
- **@helpdesk**: Checks helpdesk configuration directory

**Check Interval**: Every 10 seconds  
**Alerts**: Generated when systems go online/offline

### Alerts System

Alerts are displayed with colored indicators:

- 🟢 **INFO** (Green): Informational messages
- 🟡 **WARNING** (Yellow): Warning messages
- 🔴 **CRITICAL** (Red): Critical alerts
- 🔵 **SYSTEM** (Blue): System notifications

**Display**: Up to 3 most recent alerts shown above IRON MAN  
**Persistence**: Alerts stored in memory (up to 10)

### Visual Features

**IRON MAN Design**:
- Orange-red primary color (#FF6B35)
- Gold secondary color (#FFD700)
- Cyan arc reactor (#00FFFF) with pulsing animation
- Gray powercord tail with animated wave

**Powercord Tail**:
- Extends from bottom of IRON MAN
- Animated wave effect
- Power plug at end
- Length: 1.5x IRON MAN size

**Arc Reactor**:
- Pulsing animation (2 Hz)
- Cyan color
- Size: 30% of IRON MAN size
- Located in center

---

## ⚙️ Configuration

Configuration is stored in `data/ironman_assistant/config.json`:

```json
{
  "model_cycle_interval": 30.0,
  "status_check_interval": 10.0,
  "speed": 2,
  "size": 80
}
```

**Options**:
- `model_cycle_interval`: Seconds between automatic model cycles (default: 30.0)
- `status_check_interval`: Seconds between system status checks (default: 10.0)
- `speed`: Movement speed in pixels per frame (default: 2)
- `size`: IRON MAN size in pixels (default: 80)

---

## 🔧 Integration

### JARVIS Integration

If JARVIS is available:
- Full JARVIS agent access
- Conversation support
- Workflow integration

### R5 Integration

R5 system monitoring:
- API endpoint: `http://localhost:8000/r5/health`
- Status checks every 10 seconds
- Alerts when R5 goes online/offline

### @helpdesk Integration

Helpdesk system monitoring:
- Checks helpdesk configuration directory
- Status tracking
- Alert generation

### ULTRON/KAIJU Integration

AI cluster monitoring:
- ULTRON: `http://localhost:11434`
- KAIJU: `http://10.17.17.32:11434`
- Status checks for both clusters
- Alert generation for status changes

### ElevenLabs TTS (Optional)

If ElevenLabs TTS is available:
- Voice output for idle phrases
- Voice output for interactions
- JARVIS voice integration

---

## 📋 Usage

### Basic Usage

```python
from scripts.python.ironman_virtual_assistant import IRONMANVirtualAssistant
from pathlib import Path

project_root = Path("/path/to/lumina")
assistant = IRONMANVirtualAssistant(project_root)
assistant.run()
```

### Manual Model Cycling

```python
assistant.cycle_ai_model()  # Cycle to next model
```

### Adding Alerts

```python
from scripts.python.ironman_virtual_assistant import Alert, AlertLevel

assistant.add_alert(Alert(
    title="System Alert",
    message="This is an alert message",
    level=AlertLevel.WARNING,
    source="My Script"
))
```

### System Status

```python
status = assistant.system_status
print(f"JARVIS: {status.jarvis}")
print(f"R5: {status.r5}")
print(f"ULTRON: {status.ultron}")
print(f"KAIJU: {status.kaiju}")
```

---

## 🎨 Customization

### Colors

IRON MAN colors can be customized in code:

```python
assistant.ironman_colors = {
    "primary": "#FF6B35",      # Orange-red
    "secondary": "#FFD700",    # Gold
    "arc_reactor": "#00FFFF",  # Cyan
    "powercord": "#808080"     # Gray
}
```

### Idle Phrases

Customize idle phrases:

```python
assistant.idle_phrases = [
    "Custom phrase 1",
    "Custom phrase 2",
    # ...
]
```

### Size and Speed

Adjust IRON MAN size and movement speed:

```python
assistant.size = 100  # Larger IRON MAN
assistant.speed = 3   # Faster movement
```

---

## 🔍 Troubleshooting

### IRON MAN Not Appearing

1. Check tkinter is available: `python -c "import tkinter"`
2. Check window is not behind other windows
3. Check transparency settings

### Models Not Cycling

1. Check model cycle interval in config
2. Check system time is correct
3. Check logs for errors

### System Status Not Updating

1. Check network connectivity
2. Check system endpoints are accessible
3. Check logs for connection errors

### Alerts Not Showing

1. Check alert level is appropriate
2. Check alert list isn't full (max 10)
3. Check canvas is drawing correctly

---

## 📊 Architecture

```
IRONMANVirtualAssistant
├── AI Model Cycling
│   ├── Mark I-VII (KAIJU)
│   └── ULTRON
├── LUMINA Integration
│   ├── JARVIS
│   ├── R5 System
│   ├── @helpdesk
│   ├── ULTRON Cluster
│   └── KAIJU Cluster
├── System Monitoring
│   ├── Status Checks
│   ├── Alert Generation
│   └── Health Monitoring
├── Visual System
│   ├── IRON MAN Rendering
│   ├── Powercord Tail
│   ├── Arc Reactor Animation
│   └── Alert Display
└── Behavior
    ├── Wandering
    ├── Mouse Attraction
    ├── Conversation
    └── Interaction
```

---

## 🎯 Comparison with Armory Crate Assistant

| Feature | Armory Crate | IRON MAN Assistant |
|---------|--------------|-------------------|
| Theme | Generic | IRON MAN |
| Tail | No | Powercord tail |
| AI Models | Fixed | Cycles through 8 models |
| System Integration | Limited | Full LUMINA integration |
| Alerts | Basic | Comprehensive multi-level |
| Customization | Limited | Extensive |
| Open Source | No | Yes |

---

## 📝 Notes

- **Click-through Window**: Window is click-through to not interfere with work
- **Always on Top**: Window stays on top of other windows
- **Performance**: Lightweight, minimal CPU usage
- **Dependencies**: tkinter (standard), optional: JARVIS, ElevenLabs, requests

---

## 🚧 Future Enhancements

Potential future features:
- Custom action buttons
- Voice commands
- Gesture recognition
- Plugin system
- Custom themes
- Multiple IRON MAN instances
- Network sync
- Mobile companion

---

**Status**: ✅ **READY FOR USE**  
**Integration**: ✅ **FULL LUMINA INTEGRATION**  
**Documentation**: ✅ **COMPLETE**

---

**Last Updated**: 2025-01-24  
**Maintained by**: @JARVIS @TEAM
