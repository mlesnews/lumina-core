# JARVIS Unified AI Integration

## Overview

JARVIS now has a **comprehensive and robust** unified interface to interact with **ALL AI systems** installed on the laptop. This provides a single, consistent API for JARVIS to:

- Query any LLM (with intelligent routing)
- Coordinate with all AI systems
- Monitor health and usage
- Manage models and providers
- Synchronize AI state

## Architecture

### Components

1. **`JARVISUnifiedAIActions`** - Main unified interface
2. **`JARVISLocalFirstLLMRouter`** - Local-first LLM routing (enforces local resources first)
3. **`JARVISAICoordination`** - AI system coordination and synchronization
4. **`IntelligentLLMRouter`** - Advanced routing with multiple strategies
5. **JARVIS Unified API Integration** - Registered as `jarvis_unified_ai` system

## Available AI Systems

### LLM Providers (Local-First Priority)

1. **Local Ollama** (Priority 1)
   - Endpoint: `http://localhost:11434`
   - Models: `qwen2.5:72b`, `llama3.2:11b`, `codellama:13b`
   - Status: ✅ Healthy

2. **KAIJU Iron Legion** (Priority 2)
   - Endpoint: `http://10.17.17.32:11434`
   - Models: `llama3`, `codellama:13b`
   - Status: ✅ Healthy

3. **ULTRON Router** (Priority 3)
   - Endpoint: `http://10.17.17.32:3008`
   - Models: `qwen2.5:72b`
   - Status: ⚠️  Unavailable (when NAS is offline)

4. **ULTRON Local** (Priority 4)
   - Endpoint: `http://localhost:11434`
   - Models: `qwen2.5:72b`
   - Status: ✅ Healthy

### AI Systems (Coordination)

1. **Ollama Local** - Local LLM system
2. **JARVIS Master Agent** - Orchestration and delegation
3. **Droid Actor System** - Workflow verification and task routing
4. **R5 Living Context Matrix** - Knowledge aggregation
5. **AIOS Platform** - Holistic platform
6. **Trading System** - Financial analysis
7. **Voice Interface** - Voice recognition and TTS
8. **SiderAI Desktop** - Desktop AI assistant
9. **SiderAI Extension** - IDE extension
10. **Browser Extension** - Browser automation

## Usage

### Command Line Interface

```bash
# List all available AI systems
python scripts/python/jarvis_unified_ai_actions.py --action list_ais --json

# Query an LLM (auto-routed)
python scripts/python/jarvis_unified_ai_actions.py --action query_llm \
  --prompt "What is the capital of France?" \
  --json

# Get LLM health status
python scripts/python/jarvis_unified_ai_actions.py --action llm_health --json

# Get usage statistics
python scripts/python/jarvis_unified_ai_actions.py --action usage_stats --json

# Synchronize all AI systems
python scripts/python/jarvis_unified_ai_actions.py --action sync_ais --json
```

### Python API

```python
from jarvis_unified_ai_actions import JARVISUnifiedAIActions

with JARVISUnifiedAIActions() as jarvis:
    # List all AIs
    result = jarvis.list_available_ais()
    
    # Query LLM
    result = jarvis.query_llm("What is machine learning?")
    
    # Get health
    result = jarvis.get_llm_health()
    
    # Execute action
    result = jarvis.execute_action("list_ais")
```

### JARVIS Unified API

```python
from jarvis_unified_api import JARVISUnifiedAPI, RequestType

api = JARVISUnifiedAPI()

# Send command to Unified AI
request_id = api.send_request(
    request_type=RequestType.COMMAND,
    source="jarvis_core",
    target="jarvis_unified_ai",
    payload={
        "action": "query_llm",
        "kwargs": {
            "prompt": "Explain quantum computing",
            "allow_cloud": False
        }
    }
)

# Get response
response = api.get_response(request_id)
```

## Available Actions

### `list_ais`
List all available AI systems and their status

**Returns:**
```json
{
  "success": true,
  "ais": {
    "llm_providers": [...],
    "ai_systems": [...],
    "coordination_status": {...}
  }
}
```

### `query_llm`
Query an LLM (automatically routed to best available provider)

**Parameters:**
- `prompt`: The prompt to send
- `model`: Specific model to use (optional)
- `allow_cloud`: Allow cloud fallback (default: False)
- `provider`: Specific provider to use (optional)

**Returns:**
```json
{
  "success": true,
  "response": "...",
  "provider": "local_ollama",
  "model": "qwen2.5:72b",
  "usage_stats": {...}
}
```

### `llm_health`
Get health status of all LLM providers

**Returns:**
```json
{
  "success": true,
  "health": {
    "local_ollama": {
      "healthy": true,
      "enabled": true,
      "priority": 1
    },
    ...
  }
}
```

### `usage_stats`
Get usage statistics

**Returns:**
```json
{
  "success": true,
  "statistics": {
    "llm_router": {
      "local_requests": 100,
      "kaiju_requests": 50,
      "total_requests": 150
    }
  }
}
```

### `sync_ais`
Synchronize with all AI systems

**Returns:**
```json
{
  "success": true,
  "results": {
    "ollama_local": {"success": true},
    ...
  },
  "total": 10,
  "successful": 10
}
```

## Local-First Architecture

The system **enforces local-first** resource usage:

1. **Primary**: Local Ollama (laptop)
2. **Secondary**: KAIJU Iron Legion (NAS)
3. **Tertiary**: ULTRON Router (smart routing)
4. **LAST RESORT**: Cloud APIs (only if all local fail, and only if explicitly enabled)

This ensures:
- ✅ Maximum privacy (data stays local)
- ✅ No cloud costs (unless explicitly needed)
- ✅ Fast response times (local resources)
- ✅ Offline capability (works without internet)

## Routing Strategies

The Intelligent Router supports multiple strategies:

- **Adaptive** (default) - Learns from history
- **Round-robin** - Distributes load evenly
- **Load-balanced** - Based on current load
- **Performance-based** - Based on latency/throughput
- **Cost-aware** - Minimizes cost
- **Latency-based** - Minimizes response time
- **Priority-based** - Uses priority ordering

## Integration with JARVIS Systems

The Unified AI Actions are registered in the JARVIS Unified API as:
- **System ID**: `jarvis_unified_ai`
- **System Name**: "JARVIS Unified AI Actions"
- **Capabilities**: `["llm_routing", "ai_coordination", "model_management", "health_monitoring"]`

## Error Handling

All actions return structured responses:
```json
{
  "success": true/false,
  "data": {...},
  "error": "error message if failed",
  "action": "action_name",
  "timestamp": "ISO timestamp"
}
```

## Examples

### Example 1: List All AIs
```bash
python scripts/python/jarvis_unified_ai_actions.py --action list_ais --json
```

### Example 2: Query LLM
```bash
python scripts/python/jarvis_unified_ai_actions.py --action query_llm \
  --prompt "Write a Python function to calculate fibonacci" \
  --json
```

### Example 3: Check Health
```bash
python scripts/python/jarvis_unified_ai_actions.py --action llm_health --json
```

## Comparison with Synology Integration

| Feature | Synology AI | Unified AI |
|---------|-------------|------------|
| **Scope** | Synology DSM only | All AI systems on laptop |
| **Systems** | 1 (Synology) | 10+ (LLMs, Agents, Systems) |
| **Actions** | Task scheduling, system info | LLM queries, coordination, health |
| **Routing** | N/A | Intelligent multi-strategy routing |
| **Local-First** | N/A | ✅ Enforced |
| **Coordination** | N/A | ✅ Full AI coordination |

## Robustness Features

✅ **Health Monitoring** - Continuous health checks
✅ **Automatic Failover** - Falls back to next provider if one fails
✅ **Usage Tracking** - Statistics for all providers
✅ **Error Recovery** - Graceful handling of failures
✅ **Local-First** - Enforces local resources before cloud
✅ **Coordination** - Synchronizes state across all AIs
✅ **Unified API** - Single interface for all operations

## Future Enhancements

- [ ] Model management (pull, remove, update)
- [ ] Performance benchmarking
- [ ] Cost tracking and optimization
- [ ] Advanced routing strategies
- [ ] AI-to-AI communication protocols
- [ ] Distributed inference across multiple systems
