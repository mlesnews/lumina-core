# 🏥 JARVIS Windows Systems Engineer

## Status: ✅ IMPLEMENTED

JARVIS now operates in the job slot of a **Windows Systems Engineer**, managing the PC and all applications as parts of JARVIS's body with health baselines and continuous log monitoring.

---

## Overview

JARVIS treats:
- **PC Hardware** (CPU, RAM, Disk) as body parts
- **Windows OS Services** as body systems
- **All Applications** as body components
- **System & Application Logs** as body signals

Each component has:
- ✅ **Health baseline** (0.0 to 1.0)
- ✅ **Warning/critical thresholds**
- ✅ **Log pattern monitoring**
- ✅ **Continuous health tracking**

---

## Quick Start

### Check All Components

```bash
python scripts/python/jarvis_windows_systems_engineer.py --check-all
```

### Get Body Health Report

```bash
python scripts/python/jarvis_windows_systems_engineer.py --report
```

### Start Continuous Monitoring

```bash
python scripts/python/jarvis_windows_systems_engineer.py --monitor
```

### Register New Component

```bash
python scripts/python/jarvis_windows_systems_engineer.py --register "my_app" "My Application" "application" "0.85"
```

---

## Component Types

### Hardware Components
- `cpu` - CPU health (usage, temperature)
- `memory` - System RAM (usage, available)
- `disk_c` - C: Drive (usage, free space)
- `disk_d` - D: Drive (if exists)

### OS Services
- Windows services (running status)
- System processes

### Applications
- Cursor IDE
- VS Code
- Any installed application

### System Logs
- Windows Event Log
- Application logs
- Custom log files

---

## Health Baselines

### Default Baselines

| Component | Baseline | Warning | Critical |
|-----------|----------|---------|----------|
| CPU | 0.90 | 0.70 | 0.50 |
| Memory | 0.85 | 0.70 | 0.50 |
| Disk C: | 0.80 | 0.70 | 0.50 |
| Windows Event Log | 0.90 | 0.70 | 0.50 |
| Cursor IDE | 0.85 | 0.70 | 0.50 |

### Custom Baselines

You can register any component with custom baselines:

```python
from jarvis_windows_systems_engineer import JARVISWindowsSystemsEngineer, BodyComponentType

engineer = JARVISWindowsSystemsEngineer()

engineer.register_component(
    component_id="my_app",
    component_name="My Application",
    component_type=BodyComponentType.APPLICATION,
    baseline_health=0.90,
    metrics={'process_name': 'myapp.exe'},
    log_patterns=[
        {'pattern': r'error|exception', 'severity': 'critical'},
        {'pattern': r'warning', 'severity': 'warning'}
    ]
)
```

---

## Log Monitoring

### Automatic Log Tailing

JARVIS can tail and parse log files in real-time:

```python
# Start monitoring application log
engineer.start_log_monitoring(
    component_id="my_app",
    log_path=Path("C:/MyApp/logs/app.log")
)
```

### Log Pattern Matching

Logs are monitored for patterns:

```python
log_patterns = [
    {'pattern': r'error|failed|critical', 'severity': 'critical'},
    {'pattern': r'warning|degraded', 'severity': 'warning'},
    {'pattern': r'info|success', 'severity': 'info'}
]
```

When patterns match, JARVIS:
- ✅ Logs the issue
- ✅ Updates component health
- ✅ Triggers alerts if critical

---

## Continuous Monitoring

### Start Monitoring

```python
engineer = JARVISWindowsSystemsEngineer()

# Start continuous monitoring (checks every 60 seconds)
engineer.start_continuous_monitoring(interval_seconds=60)
```

### What Gets Monitored

- ✅ All registered components
- ✅ Hardware metrics (CPU, RAM, Disk)
- ✅ Service status
- ✅ Application processes
- ✅ System event logs
- ✅ Custom log files (if configured)

### Health History

All health checks are saved to:
- `data/jarvis_body_health/health_history.json`

Tracks health trends over time.

---

## Integration with Body Check System

### Anatomical Body Check

Works with existing body check system:

```python
from jarvis_body_check_anatomy import JARVISBodyCheckAnatomy
from jarvis_windows_systems_engineer import JARVISWindowsSystemsEngineer

# Body check includes Windows systems
body_check = JARVISBodyCheckAnatomy()
engineer = JARVISWindowsSystemsEngineer()

# Perform full body check
body_report = body_check.perform_full_body_check()

# Get Windows systems health
windows_report = engineer.get_body_health_report()
```

---

## Health Metrics

### CPU Health
- Usage percentage
- Temperature (if available)
- Baseline: 0.90
- Warning if usage > 80% or temp > 80°C

### Memory Health
- Usage percentage
- Available GB
- Baseline: 0.85
- Warning if usage > 85% or available < 2GB

### Disk Health
- Usage percentage
- Free space GB
- Baseline: 0.80
- Warning if usage > 85% or free < 20GB

### Application Health
- Process running status
- Memory/CPU usage
- Log errors/warnings
- Baseline: 0.85

---

## Example Usage

### Complete Health Check

```python
from jarvis_windows_systems_engineer import JARVISWindowsSystemsEngineer

engineer = JARVISWindowsSystemsEngineer()

# Check all components
for comp_id in engineer.components.keys():
    health = engineer.check_component_health(comp_id)
    print(f"{health.component_name}: {health.status} ({health.current_health_score:.2f})")

# Get full report
report = engineer.get_body_health_report()
print(f"Overall Health: {report['overall_health_score']:.2%}")
```

### Continuous Monitoring

```python
# Start monitoring
engineer.start_continuous_monitoring(interval_seconds=60)

# Monitor specific log
engineer.start_log_monitoring(
    component_id="cursor_ide",
    log_path=Path("C:/Users/.../.cursor/logs/main.log")
)

# Let it run...
# Health is checked every 60 seconds
# Logs are tailed in real-time
```

---

## Files Created

1. ✅ `scripts/python/jarvis_windows_systems_engineer.py` - **Main implementation**
2. ✅ `docs/JARVIS_WINDOWS_SYSTEMS_ENGINEER.md` - This guide

## Files Used

1. ✅ `monitor_windows_events.py` - Windows Event Log monitoring
2. ✅ `jarvis_body_check_anatomy.py` - Anatomical body check
3. ✅ `jarvis_body_check_triage.py` - Triage system

---

## Data Storage

- **Baselines**: `data/jarvis_body_health/health_baselines.json`
- **History**: `data/jarvis_body_health/health_history.json`

---

## Next Steps

1. **Start monitoring**: `python scripts/python/jarvis_windows_systems_engineer.py --monitor`
2. **Check health**: `python scripts/python/jarvis_windows_systems_engineer.py --report`
3. **Register apps**: Add your applications as body components
4. **Monitor logs**: Configure log monitoring for critical applications

---

**Status**: ✅ Implemented  
**Feature**: Windows Systems Engineer - PC as JARVIS's body  
**Created**: 2025-12-31
