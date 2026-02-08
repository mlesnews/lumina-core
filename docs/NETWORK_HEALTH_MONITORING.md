# Network Health Monitor - JARVIS's Body Health System

## 🏠 Overview

The Network Health Monitor treats your **home lab as JARVIS's body** and monitors all components continuously. It provides **three distinct paths to resolution** with **real-time action visibility** so you can distinguish between noise, data, and actionable information.

## 🎯 Three Paths to Resolution

### Path 1: 🔵 AUTOMATIC FIX (Self-Healing)
- **Purpose**: Self-healing, automatic remediation
- **When Used**: Timeout errors, DNS issues, temporary connection problems
- **Actions**: Automatic retries, DNS flush, connection restoration
- **Visibility**: Shows when fixes are attempted and whether they succeed

### Path 2: 🟡 INTELLIGENT REVIEW (AI-Assisted)
- **Purpose**: Smart suggestions and recommendations
- **When Used**: Permission issues, service problems, configuration errors
- **Actions**: AI-generated suggestions, diagnostic information
- **Visibility**: Shows suggestions and diagnostic data

### Path 3: 🔴 ESCALATE HUMAN (Manual Intervention)
- **Purpose**: Requires human operator attention
- **When Used**: Critical issues, complex problems, unknown errors
- **Actions**: Escalates to operator with full context
- **Visibility**: Alerts operator with detailed information

## 📊 Information Filtering

The system classifies all actions into three types:

### ⚪ NOISE
- Routine healthy checks
- Successful operations
- **Action**: Can be ignored, not actionable

### 📈 DATA
- Raw information
- Diagnostic data
- **Action**: Needs analysis, may be useful

### 📊 INFORMATION
- Actionable intelligence
- Requires attention
- **Action**: Review and act on

## 🔌 Monitoring

### Components Monitored

The system automatically monitors:

1. **Core Servers**
   - KAIJU (home lab server)
   - NAS (storage)
   - Gateway/router

2. **Services**
   - IRON LEGION Ollama (LLM cluster)
   - Jupyter server
   - Other services on known ports

3. **Network Infrastructure**
   - Gateway connectivity
   - DNS resolution
   - Network paths

### Health Checks

- **ICMP Ping**: For hosts without specific services
- **TCP Port Check**: For services with known ports
- **Response Time**: Tracks latency
- **Error Detection**: Identifies specific error types

## 🚀 Usage

### Start Monitoring
```bash
python scripts/python/network_health_monitor.py start
```

### Check Status
```bash
python scripts/python/network_health_monitor.py status
```

### View Real-Time Dashboard
```bash
python scripts/python/network_health_dashboard.py
```

### Filter by Information Type
```bash
# Show only actionable information
python scripts/python/network_health_dashboard.py --mode information

# Show all data
python scripts/python/network_health_dashboard.py --mode data

# Show everything
python scripts/python/network_health_dashboard.py --mode all
```

## 📋 Example Output

### Real-Time Actions
```
[14:32:15] 🔵 PATH 1 ⚪ ✅ KAIJU: Attempting automatic fix (success)
[14:32:16] 🟡 PATH 2 📈 ⏳ NAS: AI-assisted review (in_progress)
         → issue: Port not accessible
         → suggestions: ['Verify service is listening', 'Check firewall rules']
[14:32:17] 🔴 PATH 3 📊 🚨 IRON_LEGION_OLLAMA: Escalated to human operator (escalated)
         → component: IRON_LEGION_OLLAMA
         → host: kaiju.lesnewski.local
         → port: 11434
         → health: unhealthy
         → error: Connection timeout
```

### Status Report
```
🔌 NETWORK HEALTH MONITOR - STATUS
================================================================================
Monitoring: ✅ ACTIVE
Components: 8/10 healthy

Three-Path Resolution:
  Path 1 (Auto-Fix): 12 actions | 10/12 successful
  Path 2 (Review): 5 actions
  Path 3 (Escalate): 2 actions

Components:
  ✅ KAIJU (kaiju.lesnewski.local) - healthy
  ✅ NAS (10.17.17.32) - healthy
     → Path: automatic_fix
  ❌ IRON_LEGION_OLLAMA (kaiju.lesnewski.local:11434) - unhealthy
     → Path: escalate_human
```

## 🎛️ Dashboard Features

### Real-Time Visibility
- All actions shown as they happen
- Timestamped for tracking
- Path indicators for each action
- Status updates in real-time

### Filtering Options
- **All**: Show everything
- **Information**: Only actionable items
- **Data**: Only diagnostic data
- **Noise**: Only routine checks

### Statistics
- Component health summary
- Path distribution
- Success rates
- Auto-fix statistics

## 🔧 Configuration

### Register New Components
```python
from network_health_monitor import NetworkHealthMonitor

monitor = NetworkHealthMonitor()
monitor.register_component(
    name="MY_SERVICE",
    host="192.168.1.100",
    port=8080,
    component_type="service"
)
```

### Custom Action Callbacks
```python
def my_callback(action: ResolutionAction):
    # Do something with action
    print(f"Action: {action.action}")

monitor.register_action_callback(my_callback)
```

## 📈 Benefits

### ✅ **Three-Path Resolution**
- Clear strategy for every issue
- Automatic fixes where possible
- Intelligent suggestions for complex issues
- Human escalation when needed

### ✅ **Real-Time Visibility**
- See all actions as they happen
- Understand what's happening
- Filter noise from information
- Make informed decisions

### ✅ **Information Classification**
- Know what to ignore (noise)
- Know what to analyze (data)
- Know what to act on (information)

### ✅ **Comprehensive Monitoring**
- All home lab components
- Network infrastructure
- Services and applications
- Health status tracking

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│         COMPONENT DISCOVERY                             │
│  • Known components (KAIJU, NAS, etc.)                  │
│  • Registered components                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         HEALTH CHECKING                                 │
│  • Ping/TCP checks                                      │
│  • Response time tracking                               │
│  • Error detection                                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         PATH DETERMINATION                              │
│  • Analyze error type                                   │
│  • Determine resolution path                            │
│  • Route to appropriate handler                         │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   PATH 1    │ │   PATH 2    │ │   PATH 3    │
│ Auto-Fix    │ │   Review    │ │  Escalate   │
└─────────────┘ └─────────────┘ └─────────────┘
         │           │           │
         └───────────┼───────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         REAL-TIME VISIBILITY                            │
│  • Action recording                                     │
│  • Information classification                           │
│  • Dashboard display                                    │
│  • Filtering (noise/data/information)                   │
└─────────────────────────────────────────────────────────┘
```

## 🎯 Best Practices

### ✅ Do:
- Run monitoring continuously
- Review escalated issues promptly
- Check dashboard periodically
- Register all important components

### ❌ Don't:
- Ignore Path 3 escalations
- Disable monitoring
- Overlook information-type alerts
- Skip regular status checks

---

## ✨ Summary

The **Network Health Monitor** provides:

1. ✅ **Three-Path Resolution** - Clear strategy for every issue
2. ✅ **Real-Time Visibility** - See all actions as they happen
3. ✅ **Information Filtering** - Distinguish noise from data from information
4. ✅ **Comprehensive Monitoring** - All home lab components
5. ✅ **JARVIS's Body Health** - Complete network health system

**Your home lab = JARVIS's body. Keep it healthy!** 🏠✨

