# Homelab Opus 4.5 Equivalent - Maximum Local AI Setup

**Goal**: Utilize 100% of all local resources to achieve the closest possible equivalent to Claude Opus 4.5.

## Current Hardware Inventory

### ULTRON (Laptop)
| Component | Specs | AI Capacity |
|-----------|-------|-------------|
| GPU | NVIDIA RTX 5090 Laptop | 24GB VRAM, Compute 12.0 |
| CPU | Intel Core Ultra 9 275HX | 24 cores, great for BitNet |
| RAM | 64GB DDR5 | Massive CPU offloading capacity |
| Storage | NVMe SSD | Fast model loading |

### Iron Legion (Kaiju Desktop)
| Component | Specs | AI Capacity |
|-----------|-------|-------------|
| GPU | TBD (checking) | Ollama running, 13B models |
| CPU | TBD | Can run BitNet |
| RAM | TBD | CPU offloading |

### NAS (Synology DS1821+)
| Component | Specs | AI Capacity |
|-----------|-------|-------------|
| CPU | AMD Ryzen V1500B | 4 cores, limited |
| RAM | ~32GB | Can run small inference |
| Storage | Massive | Model storage, caching |

---

## Target Metrics vs Claude Opus 4.5

| Metric | Opus 4.5 (est.) | Our Target | Strategy |
|--------|-----------------|------------|----------|
| Parameters | 100B+ | 70-72B | Qwen 2.5 72B or Llama 3.1 70B |
| Context Window | 200K | 128K | Qwen 2.5 supports 128K native |
| Tokens/sec | 50-100 | 15-30 | Distributed + batching |
| Quality | State-of-art | 85-90% | Largest feasible model |

---

## Recommended Model: Qwen 2.5 72B

**Why Qwen 2.5 72B?**
- 72B parameters (closest to frontier models)
- 128K native context window
- Excellent coding and reasoning
- Available in efficient quantizations

### Quantization Options

| Quant | Size | VRAM Needed | Quality | Speed |
|-------|------|-------------|---------|-------|
| Q8_0 | ~75GB | 80GB+ | 99% | Slow |
| Q6_K | ~57GB | 60GB+ | 98% | Medium |
| Q5_K_M | ~50GB | 52GB+ | 96% | Medium |
| Q4_K_M | ~42GB | 45GB+ | 94% | Fast |
| Q3_K_M | ~33GB | 35GB+ | 90% | Fastest |

**Our choice: Q4_K_M** - Best balance of quality/speed for our hardware.

---

## Architecture: Distributed Inference

Since 72B Q4 (~42GB) won't fit in a single 24GB GPU, we need distributed inference.

### Option 1: llama.cpp with RPC (Recommended)

```
┌─────────────────────────────────────────────────────────────┐
│                    DISTRIBUTED INFERENCE                    │
│                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │  ULTRON     │     │ Iron Legion │     │    NAS      │   │
│  │  RTX 5090   │◄───►│  Desktop GPU│◄───►│  CPU Only   │   │
│  │  24GB VRAM  │     │  ??GB VRAM  │     │  Container  │   │
│  │  Layers 0-15│     │  Layers 16-30│    │  Embedding  │   │
│  └─────────────┘     └─────────────┘     └─────────────┘   │
│                                                             │
│  Total: 42GB model split across GPUs + CPU offload          │
└─────────────────────────────────────────────────────────────┘
```

### Option 2: Exo - Peer-to-Peer Inference

Exo allows heterogeneous devices to run inference together:
- Automatic model sharding
- Works across different GPU types
- Supports Mac, Windows, Linux

### Option 3: CPU Offloading (Single Machine)

If Iron Legion GPU is small, use ULTRON with massive CPU offload:
- 24GB GPU for hot layers
- 64GB RAM for cold layers
- Slower but works

---

## Implementation Plan

### Phase 1: Determine Iron Legion GPU
```bash
# Run on Kaiju
nvidia-smi --query-gpu=name,memory.total --format=csv
```

### Phase 2: Download Large Model
```bash
# On ULTRON or Iron Legion (whichever has more space)
ollama pull qwen2.5:72b-instruct-q4_K_M
```

### Phase 3: Configure Distributed Inference

**If Iron Legion has good GPU (16GB+):**
- Use llama.cpp RPC or Exo for distributed inference
- Split model across both GPUs

**If Iron Legion has weak/no GPU:**
- Run on ULTRON with CPU offload
- Use ~40 layers on GPU, rest on CPU

### Phase 4: Optimize for Maximum Throughput

1. **Continuous Batching**: Process multiple requests simultaneously
2. **Speculative Decoding**: Use small model to draft, large to verify
3. **KV Cache Optimization**: Quantized KV cache for longer context

---

## Maximum Achievable Specs

### Conservative Estimate (ULTRON only, CPU offload)
| Metric | Value |
|--------|-------|
| Model | Qwen 2.5 72B Q4_K_M |
| Context | 32K tokens |
| Speed | 5-10 tokens/sec |
| Quality | ~90% of Opus |

### Optimistic Estimate (Distributed, both GPUs)
| Metric | Value |
|--------|-------|
| Model | Qwen 2.5 72B Q4_K_M |
| Context | 128K tokens |
| Speed | 15-25 tokens/sec |
| Quality | ~90% of Opus |

### Maximum Context Configuration
| Metric | Value |
|--------|-------|
| Model | Qwen 2.5 32B (fits fully in GPU) |
| Context | 128K tokens |
| Speed | 25-40 tokens/sec |
| Quality | ~80% of Opus |

---

## Quick Start Commands

### 1. Pull larger model on ULTRON
```powershell
ollama pull qwen2.5:32b-instruct-q4_K_M  # 18GB, fits in GPU
```

### 2. Configure for max context
```powershell
# Set OLLAMA_NUM_CTX environment variable
$env:OLLAMA_NUM_CTX = 32768
```

### 3. Test throughput
```powershell
# Benchmark tokens/sec
ollama run qwen2.5:32b-instruct-q4_K_M "Write a 1000 word essay about AI"
```

---

## Next Steps

1. **Determine Iron Legion GPU specs** (critical for planning)
2. **Free ULTRON GPU memory** (close apps to get full 24GB)
3. **Pull Qwen 2.5 32B** as intermediate step
4. **Set up distributed inference** if Iron Legion has good GPU
5. **Benchmark and optimize**

---

## References

- [llama.cpp RPC distributed inference](https://github.com/ggerganov/llama.cpp/blob/master/examples/rpc/README.md)
- [Exo - distributed inference](https://github.com/exo-explore/exo)
- [Qwen 2.5 models](https://huggingface.co/Qwen)
- [Ollama model library](https://ollama.com/library)

---

**Tags**: @PEAK @CLUSTER @OPUS_EQUIVALENT #automation
