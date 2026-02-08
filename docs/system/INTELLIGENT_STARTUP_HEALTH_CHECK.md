# Intelligent Startup Health Check

**"Like a human would, but better"**

---

## 🎯 Philosophy

**Human-like intelligence with AI precision:**

- **On startup**: Check everything - working or broken
- **Intelligent logging**: Granular enough to identify issues, not so granular we get lost
- **Dynamic adaptation**: Escalates logging when issues found, reduces when all good
- **Smart AI processes**: Dynamically scale, adjust, adapt, and overcome

---

## 🧠 How It Works

### Startup Process

1. **Comprehensive Health Check**
   - Hardware (CPU, Memory, Disk)
   - Services (N8N, SYPHON API, AutoHotkey)
   - Integrations (Azure Key Vault, Python packages)
   - Home Lab (NAS connectivity)

2. **Intelligent Logging**
   - **Normal state**: Minimal logging (WARNING+)
   - **Issues detected**: Escalates to INFO+
   - **Critical issues**: Maximum detail (DEBUG+)

3. **Adaptive Granularity**
   - If we don't know what's wrong → logging not granular enough
   - If we're lost in noise → logging too granular
   - **Solution**: Dynamic adjustment based on findings

---

## 📊 Adaptive Logging Levels

### Normal State (All Good)
```
Level: WARNING+
- Only warnings, errors, critical
- Minimal noise
- System working as intended
```

### Degraded State (Some Issues)
```
Level: INFO+
- Shows info messages
- More context for troubleshooting
- Issues identified, investigating
```

### Critical State (Major Issues)
```
Level: DEBUG+
- Maximum detail
- Full diagnostic information
- Everything visible for troubleshooting
```

---

## 🔍 Health Check Categories

### 1. Hardware
- **CPU Usage**: Alert if >75% (warning), >90% (critical)
- **Memory Usage**: Alert if >80% (warning), >90% (critical)
- **C: Drive Space**: Alert if >90% (warning), >95% (critical)

### 2. Services
- **N8N**: Check API connectivity
- **SYPHON API**: Verify service online
- **AutoHotkey**: Verify process running

### 3. Integrations
- **Azure Key Vault**: Test connection
- **Python Packages**: Verify required packages installed

### 4. Home Lab
- **NAS Connectivity**: Test network reachability

---

## 🚀 Usage

### Automatic (Post-Reboot)

Runs automatically after system reboot via `lumina_post_reboot_evaluation.pyw`

### Manual

```bash
python scripts/python/lumina_startup_health_check.py
```

### Integration

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

## 📋 Results

### Output Format

```json
{
  "timestamp": "2026-01-11T19:38:43",
  "total_checks": 12,
  "issues": 3,
  "critical": 0,
  "results": [
    {
      "name": "C: Drive Space",
      "status": "warning",
      "details": "Disk at 93.1% - low space",
      "severity": "warning"
    }
  ]
}
```

### Logging Behavior

**When issues found:**
```
🔍 ISSUES DETECTED - Escalating logging granularity
   Detailed logging now active for troubleshooting
   Debug messages now visible
```

**When all good:**
```
✅ All systems operational
   Minimal logging (no noise)
```

---

## ✅ Benefits

1. **Human-Like Intelligence**: Checks everything on startup
2. **Adaptive Granularity**: Right level of detail for the situation
3. **No Noise When Working**: Minimal logging when all good
4. **Full Detail When Needed**: Maximum detail when issues found
5. **Smart AI Processes**: Dynamically scales and adapts

---

## 🔄 Integration with Reboot Feedback Loop

1. **Pre-Reboot**: Run evaluation
2. **Reboot**: System restart
3. **Post-Reboot**: Automatic health check
4. **Analysis**: Identify pain points
5. **Adaptation**: Adjust logging granularity
6. **Tracking**: Monitor improvements

---

## 🎯 Key Principles

1. **Identify Everything**: Know what's working or broken
2. **Right Granularity**: Not too detailed, not too sparse
3. **Dynamic Adaptation**: Escalate when needed, reduce when not
4. **Smart AI**: Processes that scale, adjust, adapt, overcome

---

**Tags**: `#HEALTH_CHECK #STARTUP #ADAPTIVE #INTELLIGENT #LUMINA_CORE @JARVIS @LUMINA`
