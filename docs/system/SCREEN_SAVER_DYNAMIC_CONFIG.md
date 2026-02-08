# Screen Saver/Blackout Dynamic Configuration

**Status:** ✅ **ACTIVE**  
**Date:** 2026-01-08  
**Default:** 30 minutes

---

## Overview

Dynamic screen saver/blackout timer configuration that:
- Sets default timeout to **30 minutes**
- Dynamically scales according to **context and complexity**
- Adapts to activity level

---

## Implementation

### Script

**File:** `scripts/python/screen_saver_dynamic_config.py`

**Features:**
- Default 30-minute timeout
- Dynamic scaling based on context
- Context detection
- Windows powercfg integration

### Configuration

**File:** `config/screen_saver_dynamic_config.json`

**Scaling Factors:**
- **High Complexity:** 1.5x (45 minutes)
  - Active coding
  - Active writing
  
- **Medium Complexity:** 1.0x (30 minutes)
  - Active reading
  - Default
  
- **Low Complexity:** 0.75x (22.5 minutes)
  - Passive watching
  
- **Idle:** 0.5x (15 minutes)
  - No activity

---

## Usage

### Set Default 30-Minute Timeout

```bash
python scripts/python/screen_saver_dynamic_config.py --set-default
```

### Set Dynamic Timeout (Based on Context)

```bash
python scripts/python/screen_saver_dynamic_config.py --set-dynamic
```

### Set Specific Timeout

```bash
python scripts/python/screen_saver_dynamic_config.py --set-timeout 45
```

### Detect Current Context

```bash
python scripts/python/screen_saver_dynamic_config.py --detect-context
```

### Calculate Timeout for Context

```bash
python scripts/python/screen_saver_dynamic_config.py --calculate-timeout
```

---

## Context Detection

### Current Implementation

- **Default:** Medium complexity (30 minutes)
- **Future:** Will detect actual activity level

### Planned Context Types

1. **High Complexity**
   - Active coding sessions
   - Active writing/editing
   - Complex problem-solving

2. **Medium Complexity**
   - Active reading
   - General browsing
   - Default state

3. **Low Complexity**
   - Passive watching
   - Light browsing

4. **Idle**
   - No activity detected
   - System idle

---

## Windows Integration

### Power Configuration

Uses Windows `powercfg` command:
- Sets monitor timeout for AC power
- Sets monitor timeout for DC power (battery)
- Applies immediately

### Configuration Records

Stored in: `data/screen_saver/screen_saver_config_*.json`

Each configuration change is recorded with:
- Timeout value
- Context detected
- Timestamp
- Platform

---

## Mental TODO

**Preserved:** ✅  
**Location:** `data/mental_todos/mental_todos.json`

**Note:**
> "NOTE-TO-SELF: OBSERVATION: Setting the screen to blackout/saver-mode timer to thirty minutes, and dynamically scale according to the context & complexity."

---

## Status

✅ **Default Timeout:** 30 minutes  
✅ **Dynamic Scaling:** Configured  
✅ **Windows Integration:** Active  
✅ **Configuration System:** Implemented  
⏳ **Context Detection:** Basic (will be enhanced)

---

## Tags

#SCREEN_SAVER #BLACKOUT #DYNAMIC_SCALING #CONTEXT_AWARE #NOTE_TO_SELF @JARVIS @LUMINA

---

**Created:** 2026-01-08T03:15:00  
**Status:** ✅ **ACTIVE - DEFAULT 30 MINUTES SET**
