# Homelab Unified Compute Fabric

**Vision**: All nodes in the homelab act as ONE GIANT CLUSTER - a unified compute fabric.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HOMELAB UNIFIED COMPUTE FABRIC                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────┐ │
│  │   LAPTOP    │    │   KAIJU     │    │      NAS-DSM            │ │
│  │  (Primary)  │◄──►│  (Compute)  │◄──►│  (Storage + Containers) │ │
│  └─────────────┘    └─────────────┘    └─────────────────────────┘ │
│        │                  │                       │                 │
│        │                  │                       │                 │
│        ▼                  ▼                       ▼                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────┐ │
│  │ Docker      │    │ Ollama      │    │ Lightweight Containers  │ │
│  │ Desktop     │    │ Iron Legion │    │ - MCP Servers           │ │
│  │ + K8s Kind  │    │ llama.cpp   │    │ - Storage Services      │ │
│  └─────────────┘    └─────────────┘    │ - Automation            │ │
│                                        └─────────────────────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    ULTRON VIRTUAL CLUSTER                     │  │
│  │  Failover + Load Balancing across all compute nodes          │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Node Responsibilities

### Laptop (Primary Workstation)
- **Role**: User interface, IDE, primary development
- **Services**: Cursor IDE, Docker Desktop, Kubernetes (Kind)
- **Storage**: Local SSD for hot data, Dropbox sync
- **Offload Strategy**: Heavy containers → NAS-DSM, Heavy models → KAIJU

### KAIJU (10.17.17.11)
- **Role**: Heavy compute, AI inference
- **Services**: Ollama, Iron Legion (llama.cpp), ULTRON models
- **Ports**:
  - 3001: Iron Legion (Tony Stark memorial port reserved at 3000)
  - 11434: Native Ollama
- **Models**: `codellama:13b`, `qwen2.5:72b` (target)

### NAS-DSM (10.17.17.32)
- **Role**: Central storage, lightweight containers
- **Services**:
  - Container Station (DSM)
  - Ollama model storage (backup)
  - Project data backups
  - Lightweight MCP servers
- **Storage Paths**:
  - `\\10.17.17.32\backups\OllamaModels` - AI model storage
  - `\\10.17.17.32\backups\MATT_Backups` - Project backups
  - `\\10.17.17.32\snapshots` - System snapshots

### FALC / Millennium Falcon (localhost:11436)
- **Role**: Secondary AI inference (Docker-based)
- **Services**: Ollama container via Docker Desktop
- **Status**: Active when Docker Desktop running

## Offload Strategy

### What to Offload to NAS-DSM
✅ Lightweight containers (no GPU needed)
✅ Storage-intensive services
✅ Backup/archive operations
✅ MCP servers for file operations
✅ Automation jobs (cron-style)

### What to Keep Local/KAIJU
❌ GPU-dependent AI inference
❌ Real-time processing
❌ Low-latency requirements
❌ Heavy compute workloads

## NAS Migration Status

| Component | Status | Location |
|-----------|--------|----------|
| Ollama Models | PARTIAL | NAS (download issues) |
| Project Backups | COMPLETE | NAS |
| LUMINA Data | PARTIAL | Mixed |
| Docker Images | PARTIAL | Local + NAS |
| MCP Servers | READY | DSM Containers |

## Port Allocation

| Port | Service | Host |
|------|---------|------|
| 3000 | **RESERVED** (Tony Stark) | - |
| 3001 | Iron Legion llama.cpp | KAIJU |
| 11434 | Ollama Native | localhost |
| 11435 | ULTRON SSH Forward | localhost→KAIJU |
| 11436 | FALC Ollama | Docker |

## Load Balancing

The ULTRON Virtual Cluster provides:
1. **Failover**: If one node fails, others take over
2. **Load Distribution**: Round-robin or least-loaded
3. **Health Monitoring**: Continuous node health checks

## Related Documentation

- [Tony Stark Port 3000 Reservation](./TONY_STARK_PORT_3000_RESERVATION.md)
- [ULTRON Cursor Validation](./ULTRON_CURSOR_VALIDATION_LIMITATION.md)
- [LLM Port Allocation](../config/llm_port_allocation.json)
- [NAS Snapshot Mount](../config/nas_snapshot_mount.json)
