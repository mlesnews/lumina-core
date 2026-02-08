# Ollama Performance Tuning Guide

**Date**: 2026-02-02
**Status**: ✅ ACTIVE
**Hardware**: NVIDIA RTX 5090 Laptop GPU (24GB VRAM)

---

## Problem Diagnosed

`qwen2-72b:latest` (47GB) significantly exceeds 24GB VRAM:
- **57% CPU / 43% GPU split** observed
- CPU inference is 10-50x slower than GPU
- Result: Very slow response times

---

## Quick Reference: Model Selection by Speed

| Model | Size | Fits in GPU | Speed vs 72B |
|-------|------|-------------|--------------|
| `qwen2.5:7b` | 4.7GB | ✅ Yes | ~10x faster |
| `qwen2.5:14b` | 8GB | ✅ Yes | ~5x faster |
| `qwen2.5:32b` | 18GB | ✅ Yes | ~2-3x faster |
| `qwen2-72b:latest` | 47GB | ❌ No | Baseline (slow) |

---

## Immediate Actions

### Option 1: Use Faster Model (RECOMMENDED)

```bash
# Best balance of quality and speed (18GB fits in 24GB VRAM)
ollama run qwen2.5:32b

# Fastest option (4.7GB)
ollama run qwen2.5:7b

# Good balance (8GB)
ollama run qwen2.5:14b
```

### Option 2: Optimize Current 72B Model

```bash
# Reduced context (saves ~2-4GB VRAM)
ollama run qwen2-72b:latest --num-ctx 2048

# Use optimized Modelfile
ollama create qwen2-72b-optimized -f "config/ollama_modelfiles/Modelfile.qwen2-72b-latest-balanced"
ollama run qwen2-72b-optimized
```

---

## Performance Tuning Script

```bash
# Full diagnosis and recommendations
python scripts/python/ollama_performance_tuner.py --optimize --model qwen2-72b:latest

# Just diagnose
python scripts/python/ollama_performance_tuner.py --diagnose

# Benchmark a model
python scripts/python/ollama_performance_tuner.py --benchmark --model qwen2.5:32b
```

---

## Tuning Profiles

### max_speed
- Context: 2048 tokens
- Best for: Quick responses, simple tasks
- Models: qwen2.5:14b, qwen2.5:7b

### balanced (default)
- Context: 4096 tokens
- Best for: General use, coding assistance
- Models: qwen2.5:32b, codellama:13b

### max_quality
- Context: 8192 tokens
- Best for: Complex reasoning, long documents
- Models: qwen2.5:72b (with CPU offload accepted)

---

## Key Parameters

| Parameter | Description | Impact |
|-----------|-------------|--------|
| `num_ctx` | Context window size | Lower = less VRAM, faster |
| `num_batch` | Batch size | Lower = less VRAM |
| `num_gpu` | GPU layers | 99 = max GPU |
| `num_thread` | CPU threads | Higher = faster CPU parts |

---

## Files Created

- `scripts/python/ollama_performance_tuner.py` - AI-ML Scientist tuning agent
- `scripts/python/local_ai_context_bridge.py` - RAG-lite context injection for local AI
- `scripts/powershell/optimize_gpu_for_ollama.ps1` - GPU memory cleanup utility
- `config/ollama_modelfiles/Modelfile.qwen2-72b-latest-balanced` - Optimized Modelfile
- `config/ollama_model_mapping.json` - Updated with RTX 5090 specs
- `data/local_ai_context/` - Document index for context injection (3,110 docs, 8,128 topics)

---

## Local AI Context Bridge

The Context Bridge solves the "I don't have access to local files" problem by:
1. Indexing project documentation (3,110 docs)
2. Retrieving relevant docs based on query keywords
3. Injecting context into Ollama system prompts

### Usage

```bash
# Index project docs (run periodically to update)
python scripts/python/local_ai_context_bridge.py --index

# Search for relevant docs
python scripts/python/local_ai_context_bridge.py --search "footer"

# Chat with context-aware AI (now knows about project!)
python scripts/python/local_ai_context_bridge.py --chat "What is the footer ticker config?" --model qwen2.5:7b
```

---

## GPU Memory Management

On Windows laptops, many apps share GPU memory (Edge, Docker, Cursor, etc.), causing Ollama to offload to CPU.

```powershell
# Check GPU status and get recommendations
.\scripts\powershell\optimize_gpu_for_ollama.ps1

# Close Edge WebView processes (often uses 2-4GB GPU)
.\scripts\powershell\optimize_gpu_for_ollama.ps1 -CloseEdge

# Full cleanup and restart Ollama
.\scripts\powershell\optimize_gpu_for_ollama.ps1 -All
```

---

## References

- [Ollama Model Library](https://ollama.com/library)
- `docs/system/ROSETTA_STONE_PERFORMANCE_TUNING.md`
- `config/ollama_model_mapping.json`
