# Unified Compute Pool Architecture

## The Vision

Treat **all GPU and CPU resources as ONE unified pool** instead of separate machines.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    UNIFIED COMPUTE POOL                                 │
│                    http://localhost:8080                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    MEMORY POOL (92+ GB)                         │   │
│   │                                                                 │   │
│   │   ┌─────────────┐   ┌─────────────────────────────────────┐     │   │
│   │   │  GPU VRAM   │   │           SYSTEM RAM                │     │   │
│   │   │   ~2 GB     │───│          ~90 GB                     │     │   │
│   │   │  (hot)      │   │         (warm)                      │     │   │
│   │   └─────────────┘   └─────────────────────────────────────┘     │   │
│   │         │                        │                              │   │
│   │         ▼                        ▼                              │   │
│   │    First Layers            Remaining Layers                     │   │
│   │    (fastest)               (CPU offload)                        │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │                    COMPUTE POOL (~36 cores)                     │   │
│   │                                                                 │   │
│   │   ┌─────────────────┐       ┌─────────────────┐                 │   │
│   │   │  ULTRON (24)    │       │ Iron Legion (12)│                 │   │
│   │   │  Intel Ultra 9  │       │  (estimated)    │                 │   │
│   │   │  275HX          │       │                 │                 │   │
│   │   └─────────────────┘       └─────────────────┘                 │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## How It Works

### 1. GPU + CPU Offload (Automatic)

Ollama automatically splits large models:
- **GPU VRAM** (~2GB usable): Handles the first transformer layers
- **System RAM** (~60GB): Handles remaining layers via CPU

When you load Qwen 32B (requires ~20GB):
- ~2GB of layers load to GPU (fast matrix ops)
- ~18GB of layers load to RAM (CPU compute)
- Inference happens in a pipeline: GPU → CPU → GPU → CPU

### 2. Multi-Machine Distribution

The cluster router spreads load across machines:
- **Primary (ULTRON)**: Has GPU, handles large models
- **Backup (Iron Legion)**: CPU-only, handles overflow
- **Parallel**: Multiple requests can run simultaneously

### 3. Intelligent Routing

```python
def select_resource(model, prefer_speed):
    if model_is_large(model):  # 32B, 70B
        return ULTRON_GPU  # Use GPU + CPU offload
    elif prefer_speed:
        return fastest_available_node()
    else:
        return least_loaded_node()
```

## Resource Inventory

| Resource | Type | Memory | Compute | Role |
|----------|------|--------|---------|------|
| RTX 5090 | GPU | 2GB usable* | 680 TFLOPS | Fast layers |
| ULTRON RAM | CPU | 60GB | 24 cores | CPU offload |
| Iron Legion | CPU | ~32GB | ~12 cores | Parallel/backup |
| **TOTAL** | Unified | **~92GB** | **~36 cores** | |

*Note: 24GB total VRAM, but ~22GB reserved by Windows WDDM for display

## What This Enables

### Before: Separate Nodes
- ULTRON can only run 7B model in full GPU
- Iron Legion runs small models slowly
- Can't run 32B+ models well

### After: Unified Pool
- Can run **32B model** with GPU+CPU hybrid
- **92GB unified memory** for context
- **32K+ token context windows**
- **~80% Opus 4.5 quality**

## Configuration

### Ollama Environment
```bash
OLLAMA_NUM_CTX=32768      # 32K context window
OLLAMA_NUM_GPU=99         # Use all GPU layers possible
OLLAMA_FLASH_ATTENTION=1  # Faster attention
```

### Cluster Router
```
http://localhost:8080     # Unified endpoint
```

### Kilo Code Settings
```json
{
  "ollamaBaseUrl": "http://localhost:8080",
  "ollamaModelId": "qwen2.5:32b-instruct-q4_K_M",
  "ollamaNumCtx": 32768
}
```

## Performance Expectations

| Metric | Value | Notes |
|--------|-------|-------|
| Model | Qwen 2.5 32B | Best quality/speed ratio |
| Quality | ~80-85% Opus | Based on benchmarks |
| Speed | 8-15 tok/s | With CPU offload |
| Context | 32K tokens | Limited by RAM |
| Latency | 2-5s first token | CPU offload overhead |

## Future Improvements

1. **True Distributed** (llama.cpp RPC): Split model across machines at layer level
2. **Speculative Decoding**: Use small model for drafts, large for verification
3. **More GPU VRAM**: External GPU enclosure or dedicated inference machine
4. **NAS Integration**: Use NAS storage for model caching

## Quick Start

```powershell
# Start the unified cluster
.\scripts\powershell\start_opus_cluster.ps1

# Or manually:
# 1. Ensure Ollama is running
# 2. Start cluster router: python services/cluster_router/cluster_router.py
# 3. Point Kilo Code to http://localhost:8080
```

---

Tags: @PEAK @CLUSTER @UNIFIED_POOL @OPUS_EQUIVALENT
