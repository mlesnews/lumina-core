# AI Technology Heartbeat Watchdog

**Date**: 2025-12-27  
**Status**: ✅ **OPERATIONAL**  
**Mission**: "WE MUST ESTABLISH A HEARTBEAT WATCHDOG ON 'AI TECHNOLOGY' FROM ALL @ASKS AND @SOURCES."

---

## Overview

The AI Technology Heartbeat Watchdog monitors all @ASKS and @SOURCES for mentions of "AI Technology" and tracks their health status through a heartbeat mechanism.

---

## Core Functionality

### Heartbeat Monitoring

- **Heartbeat Interval**: 30 seconds (configurable)
- **Timeout**: 60 seconds
- **Warning Threshold**: 45 seconds
- **Critical Threshold**: 90 seconds
- **Max Missed Heartbeats**: 3

### AI Technology Detection

Monitors for mentions of:
- "AI Technology"
- "artificial intelligence"
- "machine learning"
- "AI"
- "ML"
- "deep learning"
- "neural network"
- "GPT"
- "LLM"
- "AI model"
- "AI system"

### Source Types

1. **@ASKS** - All ask/query sources
2. **@SOURCES** - All data/intelligence sources
3. **BOTH** - Sources that are both ASKS and SOURCES

---

## Status Levels

### Healthy ✅
- Heartbeat received within timeout
- No errors
- Normal response time

### Warning ⚠️
- Heartbeat delayed (45-90 seconds)
- Slow response time
- Minor issues

### Critical 🔴
- Heartbeat delayed (>90 seconds)
- Errors detected
- High response time

### Dead ❌
- No heartbeat for >60 seconds
- Source unresponsive

### Unknown ❓
- Never received a heartbeat
- Source not yet active

---

## Features

### 1. Automatic Source Discovery

Discovers and registers:
- @ASKS sources (jarvis_asks, lumina_asks, ai_asks, etc.)
- @SOURCES (syphon_sources, data_sources, intelligence_sources, etc.)

### 2. Heartbeat Recording

Records heartbeats with:
- Source ID and type
- Timestamp
- Status (healthy/warning/critical/dead)
- AI Technology mentions
- Response time
- Errors

### 3. AI Technology Detection

Detects and tracks:
- Mentions of AI Technology keywords
- Context around mentions
- Frequency of mentions per source
- Last mention timestamp

### 4. Health Monitoring

Tracks:
- Last heartbeat timestamp
- Consecutive missed heartbeats
- Total heartbeats received
- Average response time
- Error history

### 5. Real-time Monitoring

- Continuous monitoring loop
- Automatic status updates
- Alert generation
- Status dashboard

---

## Usage

### Start Monitoring

```bash
python scripts/python/ai_technology_heartbeat_watchdog.py --start
```

### Record Heartbeat

```bash
python scripts/python/ai_technology_heartbeat_watchdog.py --heartbeat SOURCE_ID "Content with AI Technology mention" 150.5
```

### Register Source

```bash
python scripts/python/ai_technology_heartbeat_watchdog.py --register SOURCE_ID ASKS
```

### Get Status

```bash
python scripts/python/ai_technology_heartbeat_watchdog.py --status
```

### Stop Monitoring

```bash
python scripts/python/ai_technology_heartbeat_watchdog.py --stop
```

---

## Integration

### With @ASKS

The watchdog automatically monitors all @ASKS sources:
- Records heartbeats from ask operations
- Detects AI Technology mentions in queries
- Tracks response times
- Monitors for errors

### With @SOURCES

The watchdog automatically monitors all @SOURCES:
- Records heartbeats from data sources
- Detects AI Technology mentions in content
- Tracks data freshness
- Monitors source availability

---

## Configuration

### WatchdogConfig

```python
WatchdogConfig(
    heartbeat_interval_seconds=30.0,
    timeout_seconds=60.0,
    warning_threshold_seconds=45.0,
    critical_threshold_seconds=90.0,
    max_missed_heartbeats=3,
    monitor_ai_technology=True,
    ai_technology_keywords=[
        "AI Technology",
        "artificial intelligence",
        "machine learning",
        # ... more keywords
    ],
    enabled=True
)
```

---

## Data Storage

### Heartbeats

Stored in: `data/ai_technology_heartbeat_watchdog/heartbeats/`

Each heartbeat saved as JSON:
```json
{
  "heartbeat_id": "heartbeat_1234567890_source_id",
  "source_id": "source_id",
  "source_type": "asks",
  "timestamp": "2025-12-27T23:00:00",
  "status": "healthy",
  "ai_technology_mentioned": true,
  "ai_technology_context": "...",
  "response_time_ms": 150.5,
  "error": null
}
```

---

## Status Dashboard

### Summary

- **Total Sources**: Number of registered sources
- **Healthy**: Sources with healthy status
- **Warning**: Sources with warning status
- **Critical**: Sources with critical status
- **Dead**: Sources with dead status
- **Unknown**: Sources with unknown status

### Per-Source Status

- Last heartbeat timestamp
- Current status
- Consecutive missed heartbeats
- Total heartbeats received
- AI Technology mentions count
- Last AI Technology mention
- Average response time
- Error history

---

## Alerts

### Warning Alerts

- Heartbeat delayed (45-90 seconds)
- Slow response time
- Minor errors

### Critical Alerts

- Heartbeat delayed (>90 seconds)
- Multiple consecutive misses
- Errors detected
- High response time

### Dead Alerts

- No heartbeat for >60 seconds
- Source unresponsive
- Connection lost

---

## Example Output

```
💓 AI Technology Heartbeat Watchdog Status
   Monitoring Active: True
   Total Sources: 8
   Healthy: 6
   Warning: 1
   Critical: 1
   Dead: 0
   Unknown: 0
   Total Heartbeats: 1247
   AI Technology Mentions: 89
```

---

## Files

- `scripts/python/ai_technology_heartbeat_watchdog.py` - Main watchdog system
- `docs/system/AI_TECHNOLOGY_HEARTBEAT_WATCHDOG.md` - This documentation
- `data/ai_technology_heartbeat_watchdog/heartbeats/` - Heartbeat records

---

## Quotes

**"WE MUST ESTABLISH A HEARTBEAT WATCHDOG ON 'AI TECHNOLOGY' FROM ALL @ASKS AND @SOURCES."**

---

**This is the Way.**

