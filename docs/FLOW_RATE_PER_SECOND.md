# FLOW RATE PER SECOND - Primary Metric

**Date**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

---

## Overview

**FLOW RATE PER SECOND** is the **PRIMARY METRIC** for monitoring system performance.

---

## Definition

**FLOW RATE PER SECOND** = Number of flow events per second

Calculated from:
- Recent flow events (last 60 seconds)
- Flow events = workflow executions, pattern discoveries, agent actions, etc.

---

## Primary Metric

**FLOW RATE PER SECOND** is displayed prominently in:
- Real-time logging
- Metrics reports
- WACA time integration
- AI Token Request Tracking Rates

---

## Usage

### Get Current Flow Rate Per Second

```python
from flow_rate_monitor import FlowRateMonitor

monitor = FlowRateMonitor()

# PRIMARY METRIC: Get current flow rate per second
flow_rate_per_second = monitor.get_flow_rate_per_second()
print(f"FLOW RATE PER SECOND: {flow_rate_per_second:.4f}/s")
```

### Record Flow Event

```python
# Record flow event (automatically updates flow rate per second)
monitor.record_flow_event(
    waca_time=0.5,
    ai_token_requests=1,
    ai_tokens_used=100,
    agent="jarvis",
    metadata={"workflow": "test"}
)

# Flow rate per second is automatically calculated and updated
```

### Get Flow Rate Metrics

```python
metrics = monitor.get_flow_rate_metrics()

print(f"⭐ CURRENT FLOW RATE PER SECOND: {metrics.current_flow_rate:.4f}/s")
print(f"📈 Average Flow Rate Per Second: {metrics.average_flow_rate:.4f}/s")
print(f"📊 Peak Flow Rate Per Second: {metrics.peak_flow_rate:.4f}/s")
```

---

## Integration

### WACA Time Integration

```python
waca = monitor.get_waca_time_integration()

print(f"⭐ FLOW RATE PER SECOND: {waca['flow_rate_per_second']:.4f}/s")
print(f"WACA Time Total: {waca['waca_time_total']:.2f}s")
print(f"WACA Time per Flow Rate: {waca['waca_time_per_flow_rate']:.4f}s")
```

### AI Token Request Tracking Rates

```python
ai_tracking = monitor.get_ai_token_request_tracking()

print(f"⭐ FLOW RATE PER SECOND: {ai_tracking['flow_rate_per_second']:.4f}/s")
print(f"AI Token Requests Total: {ai_tracking['ai_token_requests_total']}")
print(f"Requests per Flow Rate: {ai_tracking['requests_per_flow_rate']:.4f}")
```

---

## Display Format

**FLOW RATE PER SECOND** is always displayed with:
- ⭐ Star indicator (primary metric)
- `/s` suffix (per second)
- 4 decimal places precision
- Prominent placement in output

**Example:**
```
🚀 FLOW RATE PER SECOND (PRIMARY METRIC): 0.4833/s
⭐ CURRENT FLOW RATE PER SECOND: 0.4833/s
⭐ FLOW RATE PER SECOND: 0.4833/s
```

---

## Real-Time Tracking

Every flow event automatically:
1. Updates flow rate per second
2. Logs with "FLOW RATE PER SECOND" prefix
3. Saves to history
4. Updates metrics

**Log Output:**
```
INFO:FlowRateMonitor:📊 FLOW RATE PER SECOND: 0.4833/s (WACA: 0.50s, AI Token Requests: 1, AI Tokens: 190, Agent: github_copilot)
```

---

## Status

✅ **FLOW RATE PER SECOND** is the **PRIMARY METRIC**

- ✅ Prominently displayed
- ✅ Real-time calculation
- ✅ Historical tracking
- ✅ Integrated with WACA time
- ✅ Integrated with AI Token Request Tracking Rates
- ✅ Dedicated getter method
- ✅ Always shown first in metrics

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **PRIMARY METRIC OPERATIONAL**

