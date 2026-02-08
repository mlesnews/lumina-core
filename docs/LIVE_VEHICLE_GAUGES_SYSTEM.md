# 🚗 LUMINA Live Vehicle Gauges System

**Real-time monitoring dashboard with vehicle-style gauges for all critical metrics**

---

## 🎯 Overview

Live monitoring system representing LUMINA "STATE" at particular/special layers, workflows, utilization, and flow rate % per second.

**Think:** Speedometer, RPM, Fuel, Temperature, Weight, Intensity, and other important statistics requiring @LIVE #MONITORING, #ESCALATION, #DECISIONING, #OPERATOR, #ARTIFICIAL-INTELLIGENCE

---

## 📊 Gauge Types

### Core Gauges

| Gauge | Description | Unit | Max Value |
|-------|-------------|------|-----------|
| **Speedometer** | Workflow speed | wpm (workflows per minute) | 6000 |
| **RPM** | Operations per second | ops/s | 1000 |
| **Fuel** | Resource utilization | % | 100 |
| **Temperature** | System load | °C | 100 |
| **Weight** | Data/queue size | % | 100 |
| **Intensity** | Activity level | % or sessions | 100 |
| **Flow Rate** | Data flow per second | B/s or sessions/s | Variable |
| **Pressure** | System pressure | psi | 100 |
| **Voltage** | Power/energy | V | 100 |
| **Efficiency** | Performance efficiency | % | 100 |

---

## 🏗️ System Layers

### Layer Types

1. **Application** - Application layer metrics
2. **Workflow** - Workflow execution metrics
3. **System** - System-level metrics
4. **Network** - Network traffic metrics
5. **Storage** - Storage utilization metrics
6. **Memory** - Memory usage metrics
7. **CPU** - CPU performance metrics
8. **AI** - AI/ML processing metrics
9. **Database** - Database performance metrics
10. **API** - API endpoint metrics

---

## 📈 Real-Time Metrics

### Per-Layer Metrics

Each layer tracks:
- **Workflow Count** - Number of active workflows
- **Utilization %** - Current utilization percentage
- **Flow Rate** - Operations/data per second
- **Gauge Readings** - All relevant gauges for that layer

### Flow Rate Calculation

Flow rate is calculated as **change per second**:
```
Flow Rate = (Current Value - Previous Value) / Time Difference
```

This provides real-time rate of change for all metrics.

---

## 🚨 Escalation & Decisioning

### Escalation Levels

| Level | Threshold | Action |
|-------|-----------|--------|
| **INFO** | < 70% | Normal operation |
| **WARNING** | 70-85% | Monitor closely |
| **CRITICAL** | 85-95% | Action needed soon |
| **EMERGENCY** | ≥ 95% | Immediate action required |

### Decision Types

1. **AUTOMATED** - AI handles automatically (WARNING level)
2. **HYBRID** - AI recommends, operator decides (CRITICAL level)
3. **OPERATOR** - Requires operator intervention (EMERGENCY level)

### Escalation Triggers

- **Memory Fuel** > 85% → "Consider freeing memory or scaling up resources"
- **CPU RPM** > 85% → "Reduce CPU load or add processing capacity"
- **Storage Weight** > 85% → "Clean up storage or expand capacity"
- **Network Intensity** > 85% → "Optimize network traffic or increase bandwidth"
- **System Temperature** > 85% → "Reduce system load or improve cooling"
- **Workflow Speedometer** > 85% → "Optimize workflows or reduce concurrent operations"
- **AI Intensity** > 85% → "Throttle AI requests or scale AI infrastructure"

---

## 🚀 Usage

### View Dashboard

```bash
python scripts/python/lumina_live_vehicle_gauges.py --dashboard
```

### Start Live Monitoring

```bash
python scripts/python/lumina_live_vehicle_gauges.py --monitor --interval 1.0
```

### Check Escalations

```bash
python scripts/python/lumina_gauges_escalation_decisioning.py --report
```

### Operator Alerts

```bash
python scripts/python/lumina_gauges_escalation_decisioning.py --operator-alerts
```

### AI Recommendations

```bash
python scripts/python/lumina_gauges_escalation_decisioning.py --ai-recommendations
```

---

## 📊 Dashboard Output

### Example Dashboard

```
================================================================================
🚗 LUMINA LIVE VEHICLE GAUGES DASHBOARD
================================================================================
Timestamp: 2026-01-03T13:40:45

📊 SUMMARY
   Total Layers: 10
   Active Gauges: 9
   Critical: 0 ⚠️
   Warning: 1 ⚠️

📊 LAYER: STORAGE
--------------------------------------------------------------------------------
   Utilization: 89.2%
   Flow Rate: 0.00/s

   🟡 WEIGHT: 89.20 %
      [█████████████████░░░] 89.2% (warning)

📊 LAYER: CPU
--------------------------------------------------------------------------------
   🟢 RPM: 494.00 ops/s
      [█████████░░░░░░░░░░░] 49.4% (normal)
```

---

## 🎯 Key Features

### @LIVE Monitoring

- **Real-time updates** - Gauges update every second (configurable)
- **Multi-layer tracking** - All system layers monitored simultaneously
- **Flow rate calculation** - Per-second rate of change for all metrics
- **Historical tracking** - Last 1000 readings stored for analysis

### #ESCALATION

- **Automatic threshold detection** - WARNING (70%), CRITICAL (85%), EMERGENCY (95%)
- **Event generation** - Escalation events with recommendations
- **History tracking** - All escalations logged for review

### #DECISIONING

- **Automated decisions** - AI handles WARNING level automatically
- **Hybrid decisions** - AI recommends, operator decides for CRITICAL
- **Operator decisions** - Manual intervention required for EMERGENCY

### #OPERATOR

- **Operator alerts** - Critical events requiring human attention
- **Actionable recommendations** - Specific actions to resolve issues
- **Priority-based** - Most critical issues shown first

### #ARTIFICIAL-INTELLIGENCE

- **AI recommendations** - Automated suggestions for optimization
- **Predictive analysis** - Flow rate trends indicate future issues
- **Automated responses** - AI can handle non-critical escalations

---

## 📋 Current State Example

### Storage Layer (CRITICAL)

- **Weight Gauge:** 89.2% (WARNING)
- **Status:** Critical - Action needed soon
- **Recommendation:** Clean up storage or expand capacity
- **Decision Type:** Hybrid (AI recommends, operator decides)

### CPU Layer (NORMAL)

- **RPM Gauge:** 494 ops/s (49.4%)
- **Status:** Normal
- **Flow Rate:** Calculated per second

### Memory Layer (NORMAL)

- **Fuel Gauge:** 41.1%
- **Status:** Normal
- **Available:** Sufficient resources

---

## 🔄 Continuous Monitoring

### Start Monitoring Loop

```python
from lumina_live_vehicle_gauges import LUMINALiveVehicleGauges

gauges = LUMINALiveVehicleGauges()
gauges.start_monitoring(interval_seconds=1.0)  # Update every second
```

### Stop Monitoring

```python
gauges.stop_monitoring()
```

---

## 💾 Data Storage

### Dashboard Snapshots

Saved to: `data/live_gauges/dashboard_snapshot_YYYYMMDD_HHMMSS.json`

### Escalation Events

Saved to: `data/escalation_decisioning/`

---

## 🎯 Integration Points

### With Chain of Command

- Escalations can trigger delegation to appropriate agents
- Operator alerts routed through @ACS system
- AI recommendations integrated with automated decisioning

### With Ask Stack

- Gauges can track @ASK processing rates
- Workflow gauges show @ASK execution speed
- Escalations can create new @ASKS for resolution

---

## ✅ Benefits

1. **Real-time visibility** - Always know LUMINA state
2. **Proactive alerts** - Issues detected before they become critical
3. **Automated responses** - AI handles routine escalations
4. **Operator efficiency** - Focus on critical issues only
5. **Data-driven decisions** - Metrics inform all actions
6. **Flow rate tracking** - See trends and predict issues

---

## 📊 Metrics Tracked

### System Metrics (via psutil)

- CPU percentage
- Memory usage
- Disk utilization
- Network I/O

### Workflow Metrics

- Active workflow count
- Workflow execution rate
- Workflow queue size

### AI Metrics

- Active AI sessions
- AI request rate
- AI processing load

### Custom Metrics

- Application-specific gauges
- Layer-specific metrics
- Custom flow rates

---

## 🎯 Future Enhancements

- Web dashboard interface
- Real-time WebSocket updates
- Historical trend analysis
- Predictive alerting
- Automated remediation actions
- Integration with external monitoring tools

---

**Tags:** #live_gauges #monitoring #dashboard #real_time #metrics #escalation #decisioning #operator #ai

**Last Updated:** 2026-01-03

---

*"Always be able to tell LUMINA STATE at particular/special layers, workflows, utilization & flow rate % per second."*
