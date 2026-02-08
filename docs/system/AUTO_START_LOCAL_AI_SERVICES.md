# Auto-Start Local AI Services with Smart Resource Awareness

## Status: ✅ OPERATIONAL

## Overview

Automatically starts and manages local AI services (ULTRON, KAIJU) with:
- ✅ **Auto-start on boot**
- ✅ **Smart resource awareness** (CPU/Memory monitoring)
- ✅ **Dynamic scaling** based on system load
- ✅ **CPU overload detection** (70-80% thresholds)
- ✅ **Automatic service health monitoring**

## Features

### 1. Auto-Start
- Automatically starts ULTRON and KAIJU on system boot
- Health checks ensure services are running
- Automatic restart on failure

### 2. Resource Awareness
- **CPU Monitoring**: Tracks CPU usage in real-time
- **Memory Monitoring**: Tracks memory usage
- **Threshold Detection**:
  - Low: < 30% (can scale up)
  - High: ≥ 70% (should scale down)
  - Critical: ≥ 80% (must scale down)

### 3. Dynamic Scaling
- **Scale Up**: When CPU < 30%, can add more instances
- **Scale Down**: When CPU ≥ 70%, reduces instances
- **Critical Mode**: When CPU ≥ 80%, stops non-essential services (KAIJU)

### 4. Service Management
- ULTRON: Always running (primary service)
- KAIJU: Scaled based on resources (secondary service)
- Automatic health checks every 10 seconds

## Usage

### Start Services
```bash
python scripts/python/auto_start_local_ai_services.py --start
```

### Start Monitoring (Daemon Mode)
```bash
python scripts/python/auto_start_local_ai_services.py --daemon
```

### Check Status
```bash
python scripts/python/auto_start_local_ai_services.py --status
```

### Install Auto-Start Service
```bash
python scripts/python/install_auto_start_service.py
```

## Configuration

**File**: `config/local_ai_auto_start_config.json`

### Thresholds
- **CPU Threshold Low**: 30% (scale up below this)
- **CPU Threshold High**: 70% (scale down above this)
- **CPU Threshold Critical**: 80% (critical state)
- **Memory Threshold**: 80%

### Services
- **ULTRON**: 
  - Always running
  - Priority: 1
  - Endpoint: http://localhost:11434
  
- **KAIJU**:
  - Scaled based on resources
  - Priority: 2
  - Endpoint: http://10.17.17.32:11434
  - Stops when CPU > 70%

## Dynamic Scaling Behavior

### Normal State (CPU < 70%)
- ✅ ULTRON: Running
- ✅ KAIJU: Running (if enabled)

### High CPU (70% ≤ CPU < 80%)
- ✅ ULTRON: Running
- ⚠️ KAIJU: Stopped (to reduce load)

### Critical State (CPU ≥ 80%)
- ✅ ULTRON: Running (always)
- 🚫 KAIJU: Stopped (critical mode)

### Low CPU (CPU < 30%)
- ✅ ULTRON: Running
- ✅ KAIJU: Can start (if resources allow)

## Monitoring

The system monitors:
- CPU usage (real-time)
- Memory usage
- Service health
- Scaling decisions

### Example Output
```
📊 SYSTEM STATUS
CPU: 68.0%
Memory: 51.9%
Current Scale: 1
CPU Threshold (High): 70.0%
CPU Threshold (Critical): 80.0%

Services:
  ✅ ULTRON: Running=True, Enabled=✓
  ✅ KAIJU: Running=True, Enabled=✓
```

## Integration

Integrates with:
- `enforce_local_first_ai_routing.py` - Routing system
- `live_model_usage_dashboard.py` - Usage monitoring
- Local-first AI enforcement system

## Windows Installation

Creates Windows Task Scheduler task:
- Task Name: `LuminaLocalAIAutoStart`
- Triggers: On system boot
- Runs: `auto_start_local_ai_services.py --daemon`

## Linux Installation

Creates systemd service:
- Service Name: `lumina-local-ai.service`
- Auto-starts on boot
- Auto-restarts on failure

## Status Indicators

- ✅ **Running**: Service is healthy and responding
- ❌ **Stopped**: Service is not running
- ⚠️ **Warning**: Resource threshold exceeded
- 🚫 **Critical**: System in critical state, services scaled down

## Current Status

**Last Check**: System operational
- ULTRON: ✅ Running
- KAIJU: ✅ Running (when resources allow)
- CPU Monitoring: ✅ Active
- Dynamic Scaling: ✅ Enabled

---

**Last Updated**: 2026-01-06  
**Status**: ✅ Operational  
**Auto-Start**: ✅ Enabled  
**Resource Awareness**: ✅ Active
