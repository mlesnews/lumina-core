# ULTRON Auto Agent Selection System - Syphon Documentation

**Date**: 2025-12-31  
**Status**: ✅ ACTIVE  
**Purpose**: Intelligent local agent model selection with automatic failover

---

## Overview

ULTRON is a **two-node failover virtual cluster** that intelligently selects the best LOCAL agent model available, with automatic failover between nodes:

1. **Primary Node**: KAIJU Iron Legion (7 models, high capability)
2. **Fallback Node**: Laptop Local Model (qwen2.5:72b, always available)

### Key Features

- ✅ **Intelligent Selection**: Chooses best model based on task requirements
- ✅ **Automatic Failover**: Seamlessly switches if primary node goes down
- ✅ **Local-Only**: All models are local (no cloud dependencies)
- ✅ **Zero Downtime**: Automatic failover ensures continuous operation
- ✅ **Performance Tracking**: Monitors node health and performance

---

## Architecture

### Two-Node Virtual Cluster

```
┌─────────────────────────────────────────────────────────┐
│                    ULTRON Cluster                       │
│          (Virtual Cluster with Auto-Failover)           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  PRIMARY NODE (KAIJU Iron Legion)                       │
│  ┌──────────────────────────────────────────┐          │
│  │ Endpoint: http://kaiju_no_8:11437        │          │
│  │ Status: ✅ HEALTHY / ❌ DOWN              │          │
│  │ Models: 7 (codellama, llama3, etc.)      │          │
│  │ Capability: High (diverse model selection)│          │
│  └──────────────────────────────────────────┘          │
│            │                                            │
│            │ [Health Check Every 30s]                   │
│            │                                            │
│            ▼                                            │
│  ┌──────────────────────────────────────────┐          │
│  │      AUTO-FAILOVER ROUTER                │          │
│  │  • Detects node failures                 │          │
│  │  • Routes to available node              │          │
│  │  • Tracks performance metrics            │          │
│  │  • Automatic recovery detection          │          │
│  └──────────────────────────────────────────┘          │
│            │                                            │
│            │ [Fallback if Primary Down]                 │
│            │                                            │
│            ▼                                            │
│  FALLBACK NODE (Laptop Local)                          │
│  ┌──────────────────────────────────────────┐          │
│  │ Endpoint: http://localhost:11434         │          │
│  │ Status: ✅ ALWAYS AVAILABLE              │          │
│  │ Models: 1 (qwen2.5:72b)                  │          │
│  │ Capability: High (single powerful model) │          │
│  └──────────────────────────────────────────┘          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## How Auto Agent Selection Works

### 1. Request Flow

```
User Request
    │
    ▼
[Intelligent Router]
    │
    ├─► Check Primary Node (KAIJU) Health
    │   │
    │   ├─► ✅ Available → Route to KAIJU
    │   │   │
    │   │   └─► Select Best Model from KAIJU (7 models)
    │   │       • codellama:13b (code generation)
    │   │       • llama3.2:11b (general purpose)
    │   │       • qwen2.5-coder:1.5b (lightweight)
    │   │       • llama3:8b (balanced)
    │   │       • mistral:7b (reasoning)
    │   │       • mixtral-8x7b (complex tasks)
    │   │       • gemma:2b (fast fallback)
    │   │
    │   └─► ❌ Unavailable → Auto-Failover
    │       │
    │       └─► Route to Fallback (Laptop)
    │           │
    │           └─► Use qwen2.5:72b (single model)
    │
    └─► Return Response
```

### 2. Model Selection Logic

#### For KAIJU (Primary Node)

The system selects the best model based on task characteristics:

- **Code Generation**: `codellama:13b` (Mark I)
- **General Purpose**: `llama3.2:11b` (Mark II) or `llama3:8b` (Mark IV)
- **Lightweight/Quick**: `qwen2.5-coder:1.5b-base` (Mark III) or `gemma:2b` (Mark VII)
- **Complex Reasoning**: `mixtral-8x7b` (Mark VI)
- **General Reasoning**: `mistral:7b` (Mark V)

#### For Laptop (Fallback Node)

- **All Tasks**: `qwen2.5:72b` (single powerful model, handles all tasks)

### 3. Health Checking

**Health Check Interval**: Every 30 seconds  
**Failure Threshold**: 3 consecutive failures  
**Recovery Detection**: Immediate (checks on each request)

```python
# Pseudo-code for health checking
def check_node_health(endpoint):
    try:
        response = requests.get(f"{endpoint}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

# Health check runs continuously
while True:
    kaiju_healthy = check_node_health("http://kaiju_no_8:11437")
    laptop_healthy = check_node_health("http://localhost:11434")
    
    # Update cluster state
    cluster_state = {
        "primary": {"healthy": kaiju_healthy, "endpoint": "kaiju"},
        "fallback": {"healthy": laptop_healthy, "endpoint": "laptop"}
    }
    
    sleep(30)
```

### 4. Automatic Failover

**Failover Trigger**:
- Primary node health check fails
- Request to primary node times out
- Primary node returns error

**Failover Process**:
1. Detect primary node failure
2. Immediately route to fallback node
3. Log failover event
4. Continue monitoring primary node
5. Auto-recover when primary node is back online

**Recovery Process**:
1. Primary node health check succeeds
2. Test request to primary node succeeds
3. Gradually migrate traffic back (optional)
4. Update cluster state

---

## Configuration

### ULTRON Cluster Configuration

```json
{
  "cluster_name": "ULTRON",
  "type": "two_node_failover_virtual_cluster",
  "nodes": {
    "primary": {
      "name": "KAIJU Iron Legion",
      "endpoint": "http://kaiju_no_8:11437",
      "alternative_endpoints": [
        "http://10.17.17.32:11437",
        "http://lesnewski.local:11437"
      ],
      "models": 7,
      "capability": "high",
      "priority": 1
    },
    "fallback": {
      "name": "Laptop Local",
      "endpoint": "http://localhost:11434",
      "alternative_endpoints": [
        "http://127.0.0.1:11434"
      ],
      "models": 1,
      "model_name": "qwen2.5:72b",
      "capability": "high",
      "priority": 2
    }
  },
  "failover": {
    "enabled": true,
    "health_check_interval_seconds": 30,
    "failure_threshold": 3,
    "auto_recovery": true
  }
}
```

---

## Implementation Files

### Core Components

1. **`scripts/python/auto_mode_model_selector.py`**
   - Model selection logic
   - Provider enumeration
   - Selection strategy

2. **`scripts/python/intelligent_llm_router.py`**
   - Advanced routing strategies
   - Performance metrics tracking
   - Health checking
   - Failover logic

3. **`config/cursor_ultron_model_config.json`**
   - ULTRON cluster configuration
   - Node endpoints
   - Model definitions

4. **`scripts/python/fix_kaiju_iron_legion_models.py`** (Enhanced)
   - Validates KAIJU node health
   - Checks model availability
   - Reports cluster status

---

## Usage Examples

### Basic Usage (Auto Selection)

```python
from intelligent_llm_router import IntelligentLLMRouter

router = IntelligentLLMRouter()
router.configure_ultron_cluster()

# Auto-selects best model from available node
response = router.route_request(
    prompt="Write a Python function to calculate fibonacci",
    task_type="code_generation",
    auto_select=True  # Use auto agent selection
)
```

### Manual Node Selection

```python
# Force primary node
response = router.route_request(
    prompt="...",
    preferred_node="primary"  # KAIJU
)

# Force fallback node
response = router.route_request(
    prompt="...",
    preferred_node="fallback"  # Laptop
)
```

### Check Cluster Status

```python
status = router.get_cluster_status()
# Returns:
# {
#     "primary": {"healthy": True, "endpoint": "kaiju"},
#     "fallback": {"healthy": True, "endpoint": "laptop"},
#     "active_node": "primary"
# }
```

---

## Performance Metrics

The system tracks:

- **Node Availability**: % uptime per node
- **Request Latency**: Average response time per node
- **Success Rate**: % successful requests per node
- **Failover Events**: Number of failovers in time period
- **Model Performance**: Tokens/second per model

---

## Benefits

1. **High Availability**: Zero downtime with automatic failover
2. **Intelligent Selection**: Chooses best model for each task
3. **Local Sovereignty**: All processing stays local
4. **Cost Effective**: No cloud API costs
5. **Performance**: Fast response times (local network)
6. **Reliability**: Automatic recovery when nodes come back online

---

## Future Enhancements

- [ ] Load balancing between nodes (when both healthy)
- [ ] Predictive failover (pre-emptive switching)
- [ ] Model performance learning (ML-based selection)
- [ ] Multi-node cluster expansion
- [ ] Real-time performance dashboards

---

## Related Documentation

- `docs/system/IRON_LEGION_BACKSTORY.md` - Iron Legion architecture
- `config/kaiju_iron_legion_config.json` - KAIJU configuration
- `docs/ULTRON_CURSOR_MODEL_SETUP.md` - Cursor IDE setup

---

**@SYPHON**: This document extracts the auto agent selection system architecture and failover mechanisms for ULTRON cluster.
