# JARVIS Voice System Watchdog - Quick Start Guide

**Date:** 2026-01-13  
**Purpose:** Automatically start and monitor all voice system components

---

## 🚀 Quick Start

### Start Watchdog (Auto-Starts All Components)

```bash
cd "c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\python"
python jarvis_voice_watchdog.py --start
```

**What it does:**
- ✅ Starts Voice Interface System (listening for "Hey JARVIS")
- ✅ Starts Auto-Send Monitor (pause detection & auto-send)
- ✅ Starts Voice Transcript Queue (processes voice transcripts)
- ✅ Monitors all components and auto-restarts on failure
- ✅ Health checks every 5 seconds
- ✅ Status reports every 60 seconds

---

## 📊 Check Status

```bash
python jarvis_voice_watchdog.py --status
```

**Output:**
```
📊 Component Status:
----------------------------------------------------------------------
   ✅ Voice Interface System: RUNNING
      Health: 💚 OK
      Uptime: 120.5s
   
   ✅ Auto-Send Monitor: RUNNING
      Health: 💚 OK
      Uptime: 120.3s
   
   ✅ Voice Transcript Queue: RUNNING
      Health: 💚 OK
      Uptime: 120.1s
----------------------------------------------------------------------
```

---

## 🛑 Stop Watchdog

```bash
python jarvis_voice_watchdog.py --stop
```

Or press `Ctrl+C` when running.

---

## 🔍 Features

### Auto-Start
- Automatically starts all voice components in correct order
- Handles dependencies (monitor → queue → interface)

### Watchdog Monitoring
- Health checks every 5 seconds
- Automatic restart on component failure
- Restart delay: 2 seconds (prevents rapid restart loops)
- Tracks restart counts and error history

### Status Reporting
- Real-time component status
- Health check results
- Uptime tracking
- Error logging

### Graceful Shutdown
- Stops all components in reverse order
- Handles SIGINT/SIGTERM signals
- Clean thread termination

---

## 🧪 Testing

### Test 1: Start Watchdog
```bash
python jarvis_voice_watchdog.py --start
```

**Expected:**
- All components start successfully
- Status shows all components RUNNING
- Health checks pass

### Test 2: Say "Hey JARVIS, test"
- Voice interface should detect wake word
- Transcript should be processed
- Text should appear in Cursor IDE chat
- Auto-send should trigger after pause

### Test 3: Check Status
```bash
python jarvis_voice_watchdog.py --status
```

**Expected:**
- All components show RUNNING
- Health checks show OK
- No errors reported

### Test 4: Simulate Failure
- Manually stop a component (for testing)
- Watchdog should detect failure
- Component should auto-restart
- Restart count should increment

---

## 📝 Component Details

### Voice Interface System
- **Purpose:** Captures voice input, detects wake word, transcribes speech
- **Wake Word:** "Hey JARVIS"
- **Dependencies:** None (but uses transcript queue)
- **Health Check:** Verifies `listening_active` flag

### Auto-Send Monitor
- **Purpose:** Detects pauses and auto-sends messages to Cursor IDE
- **Dependencies:** None (but used by transcript queue)
- **Health Check:** Verifies `running` flag

### Voice Transcript Queue
- **Purpose:** Processes voice transcripts, applies Grammarly, types to chat
- **Dependencies:** Auto-Send Monitor (must be started first)
- **Health Check:** Verifies `processing` flag

---

## 🐛 Troubleshooting

### Issue 1: Components Won't Start

**Symptoms:**
- Watchdog reports component as STOPPED
- Error messages in logs

**Fix:**
1. Check component logs for specific errors
2. Verify dependencies are installed
3. Check if components are already running elsewhere
4. Restart watchdog

### Issue 2: Components Keep Restarting

**Symptoms:**
- Restart count keeps increasing
- Components start then immediately stop

**Fix:**
1. Check for configuration errors
2. Verify all dependencies are available
3. Check system resources (CPU, memory)
4. Review error logs for root cause

### Issue 3: Health Checks Fail

**Symptoms:**
- Health status shows FAILED
- Components appear running but health check fails

**Fix:**
1. Verify component APIs are accessible
2. Check for threading issues
3. Review component implementation
4. Restart component manually

---

## 🔧 Configuration

### Health Check Interval
Default: 5 seconds

To change, modify in `jarvis_voice_watchdog.py`:
```python
self.health_check_interval = 5.0  # Check every 5 seconds
```

### Restart Delay
Default: 2 seconds

To change, modify in `jarvis_voice_watchdog.py`:
```python
self.restart_delay = 2.0  # Wait 2 seconds before restarting
```

---

## 📋 Integration

### With Cursor IDE
The watchdog ensures all voice components are running when you need them. Just start the watchdog once, and it handles everything.

### With JARVIS
The watchdog can be integrated into JARVIS startup to ensure voice system is always available.

### With System Startup
Add to Windows startup or systemd service to auto-start on boot.

---

## 🎯 Best Practices

1. **Start Once:** Start watchdog once and let it run
2. **Monitor Status:** Check status periodically
3. **Review Logs:** Check logs if components keep restarting
4. **Graceful Shutdown:** Always use `--stop` or Ctrl+C
5. **Health Checks:** Trust the health check results

---

## 📚 Related Documentation

- `JARVIS_VOICE_SYSTEM_STATUS_CHECK.md` - Complete system status
- `VOICE_SYSTEM_DEBUGGING.md` - Debugging guide
- `JARVIS_VOICE_INTERACTION_SUBSYSTEM_MAP.md` - System architecture

---

**Tags:** `#JARVIS_VOICE` `#WATCHDOG` `#AUTO_START` `@JARVIS` `@LUMINA`
