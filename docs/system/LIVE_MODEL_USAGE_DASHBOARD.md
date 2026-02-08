# Live Model Usage Dashboard

## Overview

Real-time dashboard showing actively used AI models with routing decisions.

## Features

- ✅ **Real-time monitoring** of model usage
- ✅ **Active model tracking** (last 5 minutes)
- ✅ **Routing decisions** displayed
- ✅ **Cloud blocking** status shown
- ✅ **Usage statistics** tracked
- ✅ **Recent requests** history

## Usage

### Quick View
```bash
python scripts/python/show_active_models.py
```

### Live Dashboard
```bash
python scripts/python/show_active_models.py --live
```

### With Simulation
```bash
python scripts/python/show_active_models.py --live --simulate
```

### JSON Output
```bash
python scripts/python/show_active_models.py --json
```

### Track Usage
```bash
python scripts/python/intercept_and_track_model_usage.py --test --show
```

## Dashboard Display

The dashboard shows:

1. **Statistics**
   - Uptime
   - Total requests
   - Local vs Cloud percentage
   - Blocked cloud requests

2. **Actively Used Models** (Last 5 minutes)
   - Model name
   - Routed to (ULTRON/KAIJU/R5 or cloud)
   - Usage count
   - Time since last use
   - Blocked status

3. **Recent Routing Decisions** (Last 10)
   - Timestamp
   - Model requested
   - Routing decision
   - Blocked status

4. **All Models Summary** (Top 10 by usage)
   - Model name
   - Routed to
   - Total usage count

## Status Indicators

- ✅ **LOCAL** - Routed to ULTRON/KAIJU/R5
- 🚫 **BLOCKED** - Cloud provider blocked, routed to local
- ☁️ **CLOUD** - Using cloud provider (requires approval)

## Data Storage

Usage data is saved to:
- `data/model_usage.json` - Persistent storage

## Integration

The dashboard integrates with:
- `enforce_local_first_ai_routing.py` - Routing system
- `intercept_and_track_model_usage.py` - Usage tracking
- `live_model_usage_dashboard.py` - Dashboard display

## Example Output

```
================================================================================
🔄 ACTIVELY USED MODELS
================================================================================

✅ LOCAL qwen2.5:72b
   → Routed to: ULTRON
   → Used 5 times
   → Last used: 0:00:30 ago

🚫 BLOCKED gpt-4
   → Routed to: ULTRON
   → Used 2 times
   → Last used: 0:01:15 ago

✅ LOCAL llama3.2:3b
   → Routed to: ULTRON
   → Used 3 times
   → Last used: 0:02:00 ago
```

---

**Last Updated**: 2026-01-06  
**Status**: ✅ Operational
