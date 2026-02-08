# Adaptive Logging System

**Intelligent, Context-Aware Logging That Scales With System State**

---

## 🎯 Philosophy

**"Like a human would, but better"**

- **When everything works**: Concise, minimal logging (no noise)
- **When issues detected**: Detailed, granular logging (full diagnostics)
- **Adaptive granularity**: Dynamically adjusts based on system state
- **Intelligent filtering**: Reduces noise without losing critical information

---

## 🧠 How It Works

### System States

1. **Normal** (All Good)
   - Logging Level: WARNING+
   - Only warnings, errors, critical
   - Minimal noise

2. **Degraded** (Some Issues)
   - Logging Level: INFO+
   - Shows info messages
   - More context for troubleshooting

3. **Critical** (Major Issues)
   - Logging Level: DEBUG+
   - Maximum detail
   - Full diagnostic information

### Adaptive Behavior

```python
# Normal state - minimal logging
logger.info("System normal")  # Suppressed
logger.warning("Issue detected")  # Shown

# Issue detected - logging escalates
logger.update_system_state("degraded", issue_count=1)
logger.info("Now showing info")  # Now visible

# Critical issue - maximum detail
logger.update_system_state("critical", issue_count=2)
logger.debug("Debug messages visible")  # Now visible
```

---

## 📊 Features

### 1. Dynamic Level Adjustment

- Automatically adjusts based on system state
- Escalates when issues found
- Reduces when issues resolved

### 2. Noise Reduction

- Suppresses duplicate messages (within 5 seconds)
- Filters repetitive logs
- Focuses on actionable information

### 3. Context-Aware Logging

```python
with logger.context("troubleshooting", min_level=logging.DEBUG):
    logger.debug("Detailed troubleshooting info")
    # Detailed logging only in this context
```

### 4. Issue Tracking

- Tracks error/warning frequency
- Adjusts granularity based on issue count
- Provides state summary

---

## 🚀 Usage

### Basic Usage

```python
from lumina_adaptive_logger import get_adaptive_logger

logger = get_adaptive_logger("MyService")

# Normal logging
logger.info("Service started")
logger.warning("High CPU usage")
logger.error("Connection failed")

# Update system state (triggers adaptive adjustment)
logger.update_system_state("degraded", issue_count=1)
logger.info("Now showing detailed info")
```

### Startup Health Check Integration

```python
from lumina_startup_health_check import LuminaStartupHealthCheck

health_check = LuminaStartupHealthCheck()
results = health_check.run_health_check()

# Automatically escalates logging if issues found
# - Normal: Minimal logging
# - Issues: Detailed logging
# - Critical: Maximum detail
```

---

## 📋 Log Levels

1. **CRITICAL** (50): System failures
2. **ERROR** (40): Errors requiring attention
3. **WARNING** (30): Warnings (always shown)
4. **INFO** (20): Informational (shown when degraded/critical)
5. **DEBUG** (10): Detailed diagnostics (shown when critical)
6. **TRACE** (5): Ultra-detailed (troubleshooting only)

---

## 🔍 Startup Health Check

**Comprehensive health check on startup:**

1. **Hardware**: CPU, Memory, Disk
2. **Services**: N8N, SYPHON API, AutoHotkey
3. **Integrations**: Azure Key Vault, Python packages
4. **Home Lab**: NAS connectivity

**Features:**
- Identifies everything working or broken
- Escalates logging when issues found
- Provides actionable diagnostics
- Adapts granularity based on findings

---

## ✅ Benefits

1. **No Noise When Working**: Minimal logging when all good
2. **Full Detail When Needed**: Maximum detail when issues found
3. **Intelligent Adaptation**: Automatically adjusts to context
4. **Actionable Diagnostics**: Clear, focused information
5. **Human-Like Intelligence**: Knows when to be verbose, when to be concise

---

## 🎯 Integration Points

- **Startup**: `lumina_startup_health_check.py`
- **Post-Reboot**: `lumina_post_reboot_evaluation.py`
- **System Evaluation**: `lumina_holistic_system_evaluation.py`
- **All Services**: Use `get_adaptive_logger()` instead of standard logging

---

**Tags**: `#LOGGING #ADAPTIVE #INTELLIGENT #LUMINA_CORE @JARVIS @LUMINA`
