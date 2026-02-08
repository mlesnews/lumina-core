# ⚡ JARVIS God Cycle

## Overview

The ultimate hands-free continuous conversation system. Enhanced version of the chained ask cycle with self-healing, context memory, and intelligent features.

```
🎤 LISTEN → 📝 TRANSCRIBE → 🧠 PROCESS → ⚡ EXECUTE → 🔊 RESPOND → 🔄 LOOP
```

## Quick Start

```bash
python scripts/python/jarvis_god_cycle.py
```

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Always Listening** | Mic continuously open |
| **Chained Cycles** | Seamless conversation loops |
| **Self-Healing** | Auto-recovery from errors |
| **Context Memory** | Remembers conversation history |
| **Proactive Suggestions** | Helpful prompts during silence |
| **Auto Warm-Recycle** | Cursor IDE recycled when needed |
| **Performance Metrics** | Real-time tracking |

### Self-Healing

- Tracks consecutive errors
- Auto-recovers after 5 failed cycles
- Reinitializes components automatically
- Logs recovery events

### Context Memory

- Remembers recent commands (last 20)
- Tracks current task
- Provides context for responses
- Persists across restarts

### Performance Metrics

- Total cycles count
- Success/failure rate
- Average response time
- Commands executed
- Errors recovered
- Warm recycles performed
- Uptime tracking

## Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║                     JARVIS God Cycle                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌────────────────┐     ┌────────────────────────────────────┐  ║
║  │ Always         │────▶│ Command Handler                    │  ║
║  │ Listening      │     │ - Parse intent                     │  ║
║  │ (Azure Speech) │     │ - Execute action                   │  ║
║  └────────────────┘     │ - Generate response                │  ║
║                         └────────────────────────────────────┘  ║
║          │                           │                          ║
║          ▼                           ▼                          ║
║  ┌────────────────┐     ┌────────────────────────────────────┐  ║
║  │ Health Monitor │     │ Hands-Free Cursor Control          │  ║
║  │ - Auto-recycle │     │ - Keyboard shortcuts (primary)     │  ║
║  │ - Error track  │     │ - Mouse fallback                   │  ║
║  │ - Metrics log  │     └────────────────────────────────────┘  ║
║  └────────────────┘                                             ║
║          │                                                      ║
║          ▼                                                      ║
║  ┌────────────────┐     ┌────────────────────────────────────┐  ║
║  │ Context Memory │     │ Intelligent Warm Recycle           │  ║
║  │ - Task track   │     │ - Memory monitoring                │  ║
║  │ - History      │     │ - CPU monitoring                   │  ║
║  │ - Preferences  │     │ - Auto-recycle                     │  ║
║  └────────────────┘     └────────────────────────────────────┘  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

## Commands

### Stop Commands
```
"goodbye JARVIS"
"stop listening"
"exit god mode"
"quit"
"shutdown"
```

### Status Commands
```
"status"
"how are you"
"health check"
```

### Memory Commands
```
"remember my task is [task]"
"working on [task]"
"what am I working on"
"current task"
```

### Recycle Commands
```
"recycle cursor"
"restart cursor"
"refresh"
```

### Cursor Control
```
"open chat"
"open file"
"save file"
"format code"
"toggle terminal"
"go to definition"
"start debug"
"open composer"
```

## Configuration

```python
CONFIG = {
    "silence_timeout": 30,           # Seconds before proactive prompt
    "error_recovery_delay": 2,       # Seconds before retry
    "max_consecutive_errors": 5,     # Before recovery mode
    "recycle_check_interval": 120,   # Seconds between checks
    "metrics_log_interval": 300,     # Seconds between logs
    "proactive_suggestion_interval": 60,  # Seconds of silence
}
```

## Testing

Run the test suite:

```bash
python scripts/python/jarvis_god_cycle.py --test
```

**Tests:**
1. ✅ Initialization
2. ✅ Metrics tracking
3. ✅ Conversation memory
4. ✅ Status reporting
5. ✅ Command handling

## Metrics Output

```json
{
  "metrics": {
    "total_cycles": 150,
    "successful_cycles": 148,
    "failed_cycles": 2,
    "success_rate": 0.987,
    "avg_response_time_ms": 245.3,
    "commands_executed": 120,
    "errors_recovered": 1,
    "warm_recycles": 2,
    "uptime_seconds": 3600
  }
}
```

## Usage Examples

### Start God Cycle

```bash
python scripts/python/jarvis_god_cycle.py
```

Output:
```
⚡ Starting JARVIS God Cycle...
   ╔══════════════════════════════════════════╗
   ║  🎤 LISTEN  →  📝 TRANSCRIBE            ║
   ║      ↓                                   ║
   ║  🧠 PROCESS  ←  🔄 LOOP                 ║
   ║      ↓                                   ║
   ║  ⚡ EXECUTE  →  🔊 RESPOND              ║
   ╚══════════════════════════════════════════╝

   Speak naturally - JARVIS is always listening.
   Say 'goodbye JARVIS' to stop.

✅ God Cycle active
```

### Set Current Task

You: "Remember I'm working on the authentication module"
JARVIS: "Got it, I'll remember you're working on: authentication module"

### Get Status

You: "Status"
JARVIS: "I'm running in God Cycle mode. Uptime: 0:45:23. Cycles: 85, Success rate: 98.8%. Health: healthy."

### Auto-Recycle

```
⚠️  Auto-recycle triggered: high_memory
🔊 JARVIS: "I'm recycling Cursor for better performance."
[Cursor restarts]
🔊 JARVIS: "Ready."
```

## Error Recovery

When errors occur:

1. Error logged
2. Consecutive error count incremented
3. If count ≥ 5:
   - Enter recovery mode
   - Stop current listeners
   - Wait 2 seconds
   - Reinitialize components
   - Restart listening
   - Reset error count
4. Continue operation

## Files

- `jarvis_god_cycle.py` - Main God Cycle
- `jarvis_always_listening.py` - Continuous speech recognition
- `jarvis_hands_free_cursor_control.py` - Cursor IDE control
- `cursor_intelligent_warm_recycle.py` - Auto-recycle system
- `data/jarvis/god_cycle/metrics.json` - Saved metrics

## Docker

Run in Docker:

```bash
docker run -it --entrypoint python3 manus-mcp-server scripts/python/jarvis_god_cycle.py
```

## Comparison: God Cycle vs Chained Ask Cycle

| Feature | Chained Ask Cycle | God Cycle |
|---------|------------------|-----------|
| Basic cycling | ✅ | ✅ |
| Self-healing | ❌ | ✅ |
| Context memory | ❌ | ✅ |
| Performance metrics | Basic | Comprehensive |
| Proactive suggestions | ❌ | ✅ |
| Error recovery | Basic | Advanced |
| Status commands | ❌ | ✅ |
| Task tracking | ❌ | ✅ |

---

**Created**: 2025-12-31  
**Status**: ✅ All Tests Passed  
**Mode**: Ultimate Hands-Free Continuous Conversation
