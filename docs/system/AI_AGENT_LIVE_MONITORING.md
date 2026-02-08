# AI Agent Live Monitoring - Real-Time Transparency System

## Overview

The AI Agent Live Monitor provides **REAL-TIME TRANSPARENCY** into which AI agent/model is currently working on issues, with live updates and color-coded status indicators.

## Key Features

### 1. Real-Time Monitoring
- **Live Updates**: Updates every 2 seconds
- **Always Visible**: Status file always available for UI display
- **Transparency**: Always know which AI agent is working

### 2. Color-Coded Status
- **🟢 GREEN**: Optimal service
  - Success rate > 90%
  - Uptime > 95%
  - Response time < 2s
  - No critical issues

- **🟡 YELLOW**: Degraded service
  - Success rate 80-90%
  - Uptime 90-95%
  - Response time 2-5s
  - Minor issues detected

- **🔴 RED**: Critical/Offline service
  - Success rate < 80%
  - Uptime < 90%
  - Response time > 5s
  - Critical issues detected

### 3. Live Status Information
- **Active Agent**: Current provider and model
- **Service Health**: Real-time health metrics
- **Current Task**: What the agent is working on
- **@WOPR Patterns**: Deep pattern research results

### 4. @WOPR Integration
- **Pattern Research**: Uses @WOPR for deep pattern analysis
- **Pattern Extraction**: Extracts patterns related to current agent
- **Simulation**: Runs WOPR simulations for pattern research

## Status File

Live status is written to:
- `data/ai_agent_monitor/live_status.json`

Format:
```json
{
  "timestamp": "2026-01-15T12:00:00",
  "active_agent": {
    "agent_id": "agent_20260115_120000",
    "provider": "ULTRON",
    "model": "qwen2.5:72b",
    "provider_type": "ULTRON",
    "status": "active",
    "current_task": "code_generation: generate_function",
    "health": {
      "status": "optimal",
      "color": "GREEN",
      "status_text": "OPTIMAL",
      "response_time": 0.5,
      "success_rate": 0.95,
      "error_rate": 0.05,
      "uptime": 99.5,
      "issues": []
    },
    "wopr_patterns": [
      "provider:ULTRON",
      "model:qwen2.5:72b",
      "status:active"
    ]
  },
  "monitoring": true,
  "update_interval": 2.0
}
```

## Usage

### Start Monitoring

```python
from ai_agent_live_monitor import get_live_monitor

monitor = get_live_monitor()
# Monitoring starts automatically
```

### Display Status

```python
from ai_agent_status_display import AIAgentStatusDisplay

display = AIAgentStatusDisplay()
display.display_status()  # Full display
display.display_compact()  # One-line display
```

### Command Line

```bash
# Start monitor
python scripts/python/ai_agent_live_monitor.py

# Display status
python scripts/python/ai_agent_status_display.py
```

## Integration Points

### #Decisioning Integration
- Automatically updates when decisions are made
- Shows current task being worked on
- Tracks agent selection

### Provider Tracker Integration
- Uses provider tracker for health metrics
- Tracks provider performance
- Monitors service availability

### Cursor Integration
- Tracks active Cursor IDE model
- Monitors model selection
- Updates on model changes

### @WOPR Integration
- Runs WOPR simulations for pattern research
- Extracts patterns from agent usage
- Deep pattern analysis

## Health Metrics

### Response Time
- **Optimal**: < 2 seconds
- **Degraded**: 2-5 seconds
- **Critical**: > 5 seconds

### Success Rate
- **Optimal**: > 90%
- **Degraded**: 80-90%
- **Critical**: < 80%

### Uptime
- **Optimal**: > 95%
- **Degraded**: 90-95%
- **Critical**: < 90%

## Display Examples

### Full Display
```
================================================================================
🖥️  AI AGENT LIVE STATUS
================================================================================

Active Agent:
  Provider: ULTRON
  Model: qwen2.5:72b
  Type: ULTRON
  Status: active
  Current Task: code_generation: generate_function

Service Health:
  ✅ Status: OPTIMAL
  Success Rate: 95.0%
  Error Rate: 5.0%
  Response Time: 0.50s
  Uptime: 99.5%

@WOPR Patterns:
  🔍 provider:ULTRON
  🔍 model:qwen2.5:72b
  🔍 status:active

Last Updated: 2026-01-15T12:00:00
================================================================================
```

### Compact Display
```
✅ [OPTIMAL] ULTRON / qwen2.5:72b | Success: 95.0% | Response: 0.50s
```

## Tags

`#TRANSPARENCY` `#LIVE_MONITORING` `#AI_AGENT` `#WOPR` `#PATTERN_RESEARCH` `@LUMINA` `@JARVIS`

---

**Status**: ✅ **OPERATIONAL**  
**Update Interval**: 2 seconds  
**Transparency**: Always visible
