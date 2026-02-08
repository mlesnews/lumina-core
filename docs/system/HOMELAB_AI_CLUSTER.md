# Homelab AI Cluster - Unified Virtual AI Brain

## Overview

The homelab operates as **one unified AI cluster**, distributing workloads across GPU (Ollama) and CPU (BitNet) nodes to optimize for cost, speed, and capability.

**Total Inference Endpoints: 5**
- 2 GPU nodes (Ultron RTX 5090, Kaiju RTX 3090)
- 3 CPU nodes (Ultron CPU, Kaiju CPU, NAS CPU via BitNet)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        HOMELAB AI CLUSTER                                │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐      │
│   │     ULTRON       │  │      KAIJU       │  │       NAS        │      │
│   │     Laptop       │  │     Desktop      │  │    Synology      │      │
│   ├──────────────────┤  ├──────────────────┤  ├──────────────────┤      │
│   │ 🎮 GPU: RTX 5090 │  │ 🎮 GPU: RTX 3090 │  │ 🖥️ CPU: BitNet   │      │
│   │    24GB VRAM     │  │    24GB VRAM     │  │    (0.7B, 2B)    │      │
│   │ 🖥️ CPU: BitNet   │  │ 🖥️ CPU: BitNet   │  │                  │      │
│   │    (2B, 3B, 8B)  │  │    (2B, 3B, 8B)  │  │   10.17.17.32    │      │
│   │   localhost      │  │   10.17.17.11    │  │   4 cores        │      │
│   └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘      │
│            │                     │                     │                 │
│            └──────────┬──────────┴─────────────────────┘                 │
│                       │                                                  │
│               ┌───────▼────────┐                                         │
│               │ SMART ROUTER   │                                         │
│               │ ─────────────  │                                         │
│               │ 1. Try GPU     │                                         │
│               │ 2. If busy →   │                                         │
│               │    BitNet CPU  │                                         │
│               └───────┬────────┘                                         │
│                       │                                                  │
└───────────────────────┼──────────────────────────────────────────────────┘
                        │
               ┌────────▼────────┐
               │   USER QUERY    │
               └─────────────────┘
```

## Cost-Saving Strategy

**Goal**: Use local compute to offset cloud API costs, save cloud tokens for hard problems.

### Standard Ollama Tiers (GPU)

| Tier | Model | Context | Speed | Cost | Use Case |
|------|-------|---------|-------|------|----------|
| **fast** | 1.5B | 2K | 2-3s | FREE | Simple math, quick lookups |
| **balanced** | 3B | 6K | 10-20s | FREE | Project questions |
| **cluster** | 3B | 8K | 10-15s | FREE | Distributed across homelab |
| **quality** | 7B | 12K | 30-60s | FREE | Detailed analysis |
| **cloud** | Claude | 16K | 3-5s | $$$ | Complex problems |

### BitNet Tiers (CPU) - Microsoft Breakthrough

BitNet enables **100B models on CPU at human reading speed** (5-7 tok/s)!

| Tier | Model | Speed on CPU | Energy | Use Case |
|------|-------|--------------|--------|----------|
| **bitnet-2b** | 2.4B | 50+ tok/s | -80% | Fast CPU inference |
| **bitnet-8b** | 8B (Llama3) | 20+ tok/s | -75% | Quality on CPU |
| **bitnet-100b** | 100B | 5-7 tok/s | -70% | Maximum quality, NAS-compatible |

### REAL Monthly Savings (Power User)

| Use Case | Daily Volume | Cloud Cost | Local Cost | Savings |
|----------|--------------|------------|------------|---------|
| Code generation | 500 queries | $7.50/day | $0 | 100% |
| Chat queries | 200 queries | $2.00/day | $0 | 100% |
| Document processing | 50 queries | $1.00/day | $0 | 100% |
| Background agents | 24/7 | $5.00/day | $0 | 100% |
| **Daily Total** | - | **$15.50** | ~$0.30 | **98%** |
| **Monthly Total** | - | **$465** | ~$10 | **$455** |

**Plus subscriptions replaced:**
- GitHub Copilot: $19/month → $0
- ChatGPT Plus: $20/month → $0
- Claude Pro: $20/month → $0

**Total potential savings: $450-500/month**

## Quick Start

### Check Cluster Status

```bash
python scripts/python/homelab_ai_cluster.py --status
```

### Chat with Auto-Routing

```bash
# Simple query - auto-routes to best node
python scripts/python/homelab_ai_cluster.py --chat "What is 2+2?"

# Project-aware query with context injection
python scripts/python/local_ai_context_bridge.py --chat "What is footer config?" --tier cluster
```

### Tier Selection

```bash
# Fast tier (simple queries, 2-3s)
python scripts/python/local_ai_context_bridge.py --chat "Factorial of 5?" --tier fast

# Balanced tier (project queries, 10-20s)
python scripts/python/local_ai_context_bridge.py --chat "What is the footer config?" --tier balanced

# Cluster tier (distributed across homelab)
python scripts/python/local_ai_context_bridge.py --chat "What is the footer config?" --tier cluster

# Cloud tier (complex problems, costs tokens)
python scripts/python/local_ai_context_bridge.py --chat "Design a microservices architecture" --tier cloud
```

### @PEAK Workflow (Distributed Analysis)

```bash
python scripts/python/homelab_ai_cluster.py --peak "Analyze project architecture"
```

This runs a three-phase workflow distributed across the cluster:
1. **Pattern Recognition** - Parallel on all nodes
2. **Deep Analysis** - Best available node with quality model
3. **Knowledge Synthesis** - Combines results

## Architecture Components

### 1. Homelab AI Cluster (`homelab_ai_cluster.py`)

- Discovers online nodes
- Routes queries to best available node
- Prefers node with model already loaded
- Runs @PEAK workflows distributed

### 2. Local AI Context Bridge (`local_ai_context_bridge.py`)

- Indexes 5000+ project docs
- Injects relevant context into prompts
- Tier-based routing (fast/balanced/cluster/cloud)
- Integrates R5 Living Context Matrix

### 3. Cluster Nodes

| Node | IP | GPU | Ollama Port | Role |
|------|----|----|-------------|------|
| Ultron | localhost | RTX 5090 (24GB) | 11434 | Primary local |
| Kaiju | 10.17.17.11 | RTX 3090 (24GB) | 11434 | Secondary, desktop |
| NAS | 10.17.17.32 | None | - | Coordinator, storage |

## Configuration

### Host Registry

`config/host_identity_registry.json` - Single source of truth for host IPs

### Cluster Endpoints

```json
{
  "ultron": {"ip": "127.0.0.1", "port": 11434, "gpu": "RTX 5090"},
  "kaiju": {"ip": "10.17.17.11", "port": 11434, "gpu": "RTX 3090"}
}
```

### Tier Configuration

```python
MODEL_TIERS = {
    "fast": {"model": "qwen2.5-coder:1.5b-base", "max_context": 2000},
    "balanced": {"model": "llama3.2:3b", "max_context": 6000},
    "cluster": {"model": "llama3.2:3b", "max_context": 8000},
    "quality": {"model": "qwen2.5:7b", "max_context": 12000},
    "cloud": {"model": "claude-3-haiku-20240307", "max_context": 16000}
}
```

## Troubleshooting

### Node Offline

```bash
# Check specific node
curl http://10.17.17.11:11434/api/tags

# Restart Ollama on Kaiju (RDP or SSH)
ollama serve
```

### Slow Inference

1. Check GPU memory: `nvidia-smi`
2. Close GPU-heavy apps: Edge, Steam, Docker
3. Use smaller model or `--tier fast`
4. Run `scripts/powershell/optimize_gpu_for_ollama.ps1`

### Model Not Found

```bash
# Pull model on node
ollama pull llama3.2:3b

# List available models
ollama list
```

## BitNet Setup (Microsoft CPU Breakthrough)

BitNet is Microsoft's 1-bit LLM framework that enables efficient CPU inference:
- **100B models at 5-7 tokens/sec** on CPU alone
- **2.37x to 6.17x faster** than standard CPU inference
- **71.9%-82.2% energy reduction**

### Quick Setup

```powershell
# Install and benchmark
.\scripts\powershell\setup_bitnet_homelab.ps1 -InstallDependencies -DownloadModels -Benchmark
```

### Available Models

| Model | Params | CPU Speed | Quality |
|-------|--------|-----------|---------|
| BitNet-b1.58-2B-4T | 2.4B | 50+ tok/s | Good |
| Llama3-8B-1.58 | 8B | 20+ tok/s | Great |
| 100B BitNet | 100B | 5-7 tok/s | Excellent |

### Cluster Expansion with BitNet

```
┌─────────────────────────────────────────────────────────────┐
│                   WITH BITNET                               │
├─────────────────────────────────────────────────────────────┤
│  ULTRON          │  KAIJU           │  NAS                  │
│  GPU: RTX 5090   │  GPU: RTX 3090   │  GPU: None            │
│  CPU: BitNet ✓   │  CPU: BitNet ✓   │  CPU: BitNet ✓ (NEW!) │
│  Parallel: 2x    │  Parallel: 2x    │  Now capable!         │
└─────────────────────────────────────────────────────────────┘

Total inference endpoints: 6 (3 GPU + 3 CPU)
NAS can now run AI inference (previously impossible!)
```

## Related Documents

- `config/host_identity_registry.json` - Host IPs (SSOT)
- `config/homelab_mcp_hybrid_config.json` - MCP hybrid config
- `docs/system/OLLAMA_PERFORMANCE_TUNING_GUIDE.md` - Model tuning
- `docs/system/R5_CONTEXT_BRIDGE_INTEGRATION.md` - Context injection
- `scripts/powershell/setup_bitnet_homelab.ps1` - BitNet setup

---

**Strategy**: Local compute for routine queries, cloud for complex problems. With BitNet, even your NAS can run inference. The cluster auto-routes to minimize cost while maintaining capability.
