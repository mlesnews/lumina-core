# ULTRON Virtual Cluster - Health Check Documentation

**Status**: ✅ **IMPLEMENTED**

---

## ULTRON Virtual Cluster Architecture

**ULTRON** is a **virtual cluster** that combines three local AI nodes into a unified failover system:

### Cluster Nodes

1. **Node 1: ULTRON Standalone**
   - **Location**: Localhost (Laptop)
   - **Endpoint**: `http://localhost:11434`
   - **Model**: `qwen2.5:72b`
   - **Type**: Standalone
   - **Role**: Quick local responses, offline operation

2. **Node 2: KAIJU/Iron Legion**
   - **Location**: KAIJU_NO_8 (10.17.17.11)
   - **Endpoint**: `http://10.17.17.11:3000` (expert router) or `http://10.17.17.11:3001` (individual)
   - **Model**: `codellama:13b`
   - **Type**: Iron Legion Expert Cluster (7 Expert Specialists)
   - **Role**: Primary cluster, expert routing, high-performance code generation

3. **Node 3: FALC/Millennium Falcon**
   - **Location**: Localhost (Laptop - separate instance)
   - **Endpoint**: `http://localhost:11436`
   - **Model**: PERSPECTIVE models
   - **Type**: Millennium Falcon Failover Cluster
   - **Role**: Failover when Iron Legion unavailable, PERSPECTIVE model testing

---

## Cluster Configuration

### Configuration File

**Location**: `config/ultron_cluster_selection.json`

**Structure**:
```json
{
  "available_clusters": {
    "ultron_standalone": {
      "endpoint": "http://localhost:11434",
      "type": "standalone",
      "priority": 3
    },
    "iron_legion": {
      "endpoint": "http://10.17.17.11:3000",
      "type": "expert_cluster",
      "priority": 1
    },
    "millennium_falcon": {
      "endpoint": "http://localhost:11436",
      "type": "failover_cluster",
      "priority": 2
    }
  },
  "failover_config": {
    "primary": "iron_legion",
    "secondary": "millennium_falcon",
    "tertiary": "ultron_standalone",
    "auto_failover": true
  }
}
```

---

## Health Check Implementation

### Check Name

**`ULTRON Virtual Cluster`**

### What It Checks

1. **Node Connectivity**
   - Tests API connectivity to each node
   - Verifies Ollama API is responding
   - Checks model availability

2. **Cluster Health**
   - Counts operational nodes
   - Verifies failover capability (requires 2+ nodes)
   - Reports cluster status

3. **Configuration**
   - Loads `ultron_cluster_selection.json`
   - Verifies Cursor IDE configuration
   - Checks cluster description

### Status Levels

| Status | Meaning | Requirements |
|--------|---------|-------------|
| **[  OK  ]** | All nodes operational | 3/3 nodes operational |
| **[WARN ]** | Degraded cluster | 2/3 nodes operational (failover capable) |
| **[FAILED]** | Critical cluster failure | < 2 nodes operational (failover not possible) |

---

## Failover Configuration

### Failover Chain

1. **Primary**: KAIJU/Iron Legion (10.17.17.11:3000)
2. **Secondary**: FALC/Millennium Falcon (localhost:11436)
3. **Tertiary**: ULTRON Standalone (localhost:11434)

### Failover Requirements

- **Minimum Nodes**: 2 nodes must be operational for failover capability
- **Auto-Failover**: Enabled
- **Auto-Failback**: Enabled
- **Failover Threshold**: 3 consecutive failures

---

## Health Check Output

### Example Output

```
================================================================================
Starting local AI configurations...
================================================================================

[  OK  ] Cursor IDE Connection
[  OK  ] Ollama
[  OK  ] ULTRON Virtual Cluster
[  OK  ] Local LLM Configs
```

### Debug Details (when `--debug` enabled)

```
[  OK  ] ULTRON Virtual Cluster
         cluster_type: Virtual Cluster - Three-Node Failover
         cluster_description: ULTRON Virtual Cluster: Localhost + KAIJU + FALC
         nodes_total: 3
         nodes_operational: 3
         cluster_health: 3/3 nodes operational
         cluster_status: OPERATIONAL - All nodes available
         failover_capable: True
         node_ultron_standalone: {operational: True, ...}
         node_kaiju: {operational: True, ...}
         node_falc: {operational: True, ...}
```

---

## Node Details

### Node Status Structure

Each node check returns:

```json
{
  "name": "Node Name",
  "ip": "IP address",
  "port": 11434,
  "type": "Node Type",
  "model": "Model name",
  "endpoint": "http://ip:port",
  "operational": true,
  "api_accessible": true,
  "api_models": 5,
  "available_models": ["model1", "model2", ...],
  "model_available": true
}
```

---

## Integration with Cursor IDE

### Cursor Configuration

**File**: `data/cursor_models/cursor_models_config.json`

**ULTRON Entry**:
```json
{
  "title": "ULTRON",
  "name": "ultron",
  "provider": "ollama",
  "model": "qwen2.5:72b",
  "apiBase": "http://localhost:11434",
  "description": "ULTRON Cluster - Two-Node Failover Virtual Cluster (KAIJU Iron Legion + Laptop Local) - LOCAL ONLY, NO API KEY",
  "localOnly": true,
  "requiresApiKey": false
}
```

**Note**: Cursor IDE may show "Invalid Model" errors despite correct configuration. This is a Cursor IDE bug, not a LUMINA system failure. The cluster works via Ollama API directly.

---

## Troubleshooting

### Node Not Operational

**Symptoms**: Node shows `operational: false`

**Checks**:
1. Verify Ollama is running on that node
2. Check network connectivity to node IP
3. Verify port is correct
4. Check firewall rules

**Commands**:
```bash
# Check localhost node
curl http://localhost:11434/api/tags

# Check KAIJU node
curl http://10.17.17.11:3000/api/tags

# Check FALC node
curl http://localhost:11436/api/tags
```

### Cluster Degraded

**Symptoms**: `[WARN ]` status, 2/3 nodes operational

**Impact**: Failover still works, but one node unavailable

**Action**: Review node details to identify which node is down

### Cluster Critical

**Symptoms**: `[FAILED]` status, < 2 nodes operational

**Impact**: Failover not possible

**Action**:
1. Fix down nodes immediately
2. Verify network connectivity
3. Check Ollama services
4. Review cluster configuration

---

## Related Systems

- **@JARVIS**: Orchestrates cluster selection and failover
- **@R5**: Aggregates cluster patterns and knowledge
- **@BONES**: Monitors cluster health
- **@UATU**: Observes cluster operations

---

## Configuration Files

1. **`config/ultron_cluster_selection.json`**: Cluster configuration
2. **`config/iron_legion_cluster_config.json`**: Iron Legion details
3. **`config/homelab_cpu_architecture.json`**: Homelab architecture
4. **`data/cursor_models/cursor_models_config.json`**: Cursor IDE config

---

## Status

**Health Check**: ✅ **IMPLEMENTED**

**Cluster Verification**: ✅ **OPERATIONAL**

**Failover Capability**: ✅ **VERIFIED**

---

**Tags:** `#ULTRON` `#VIRTUAL_CLUSTER` `#KAIJU` `#FALC` `#FAILOVER` `#HEALTH_CHECK` `@JARVIS` `@BONES` `@LUMINA`

**Status:** ✅ **ULTRON VIRTUAL CLUSTER HEALTH CHECK OPERATIONAL**
