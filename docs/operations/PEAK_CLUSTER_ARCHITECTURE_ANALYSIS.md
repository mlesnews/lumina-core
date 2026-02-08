# @PEAK CLUSTER ARCHITECTURE FOR @LUMINA

## Executive Summary

This document analyzes cluster configuration options and identifies the @PEAK architecture for LUMINA.

---

## 1. CLOUD FRAMEWORKS WITH FLAT-RATE PRICING

### ✅ SUBSCRIPTION-BASED (OFFLOAD COMPUTE FOR FREE*)

| Service | Pricing Model | Compute Limits | Best For |
|---------|---------------|----------------|----------|
| **Cursor Pro** | $20/month | 500 fast + unlimited slow | IDE coding, chat |
| **GitHub Copilot** | $10/month | Unlimited completions | Code completion |
| **Cline** | FREE (local) | Unlimited (your hardware) | Custom workflows |
| **Continue** | FREE (local) | Unlimited (your hardware) | Multi-IDE support |
| **Kilo Code** | FREE (local) | Unlimited (your hardware) | @PEAK patterns |
| **Windsurf** | $15/month | 500 fast requests | Alternative IDE |
| **Cody (Sourcegraph)** | $9/month | Unlimited completions | Code search |
| **Tabnine Pro** | $12/month | Unlimited completions | Team features |

### ⚠️ PAY-PER-TOKEN (USE SPARINGLY)

| Service | Input Cost | Output Cost | When to Use |
|---------|------------|-------------|-------------|
| Claude API | $15-75/1M | Direct API calls |
| OpenAI API | $2.50-30/1M | Direct API calls |
| Azure OpenAI | $1-15/1M | Enterprise compliance |

### 🎯 STRATEGY: MAXIMIZE FLAT-RATE, MINIMIZE PAY-PER-TOKEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      COMPUTE OFFLOAD HIERARCHY                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. ULTRON LOCAL CLUSTER (FREE after hardware)                             │
│     └── 90% of workload - coding, iteration, quick queries                 │
│                                                                             │
│  2. SUBSCRIPTION SERVICES (FLAT RATE)                                      │
│     └── Cursor Pro - complex IDE operations                                │
│     └── GitHub Copilot - code completion boost                             │
│     └── Kilo Code / Cline - custom workflows                               │
│                                                                             │
│  3. PAY-PER-TOKEN (LAST RESORT)                                            │
│     └── Only for: massive context, frontier reasoning                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. CLUSTER CONFIGURATION OPTIONS

### Option A: OLLAMA-ONLY (Current)

```
Pros:
✅ Simple setup and management
✅ Works now, battle-tested
✅ Low overhead
✅ Good for single-node and small clusters

Cons:
❌ No built-in load balancing
❌ Manual failover
❌ No container orchestration
❌ Scaling requires custom code
```

### Option B: KUBERNETES (k3s/k8s)

```
Pros:
✅ Industry-standard orchestration
✅ Built-in load balancing
✅ Auto-scaling and failover
✅ Declarative configuration
✅ Massive ecosystem

Cons:
❌ Complex setup and maintenance
❌ Resource overhead (etcd, controllers)
❌ Overkill for homelab scale
❌ Steep learning curve
❌ Harder to debug
```

### Option C: HYBRID (RECOMMENDED @PEAK)

```
Pros:
✅ Best of both worlds
✅ Ollama for LLM inference (simple)
✅ Docker/Compose for services (flexible)
✅ Custom ULTRON router for orchestration
✅ NAS Container Manager for shared services
✅ Appropriate complexity for homelab scale

Cons:
❌ Custom code maintenance
❌ Not "standard" infrastructure
```

---

## 3. @PEAK ARCHITECTURE FOR @LUMINA

### RECOMMENDATION: HYBRID APPROACH

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    @PEAK ARCHITECTURE FOR @LUMINA                             ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  LAYER 1: INFERENCE ENGINE                                                    ║
║  ─────────────────────────                                                    ║
║  • Ollama (simple, proven, works)                                            ║
║  • One instance per node                                                      ║
║  • Direct HTTP API                                                           ║
║                                                                               ║
║  LAYER 2: ORCHESTRATION                                                       ║
║  ──────────────────────                                                       ║
║  • ULTRON Unified Cluster (custom Python)                                    ║
║  • CPU-architecture routing                                                   ║
║  • Load balancing + failover                                                 ║
║  • Multiplier stacking                                                       ║
║                                                                               ║
║  LAYER 3: SERVICES                                                            ║
║  ────────────────                                                             ║
║  • NAS Container Manager (DSM)                                               ║
║  • Docker Compose for auxiliary services                                     ║
║  • n8n, Jupyter, monitoring                                                  ║
║                                                                               ║
║  LAYER 4: CLOUD OFFLOAD                                                       ║
║  ─────────────────────                                                        ║
║  • Subscription services (Cursor, Copilot)                                   ║
║  • Azure AI Foundry (model testing)                                          ║
║  • Pay-per-token only for edge cases                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### WHY NOT KUBERNETES?

For @LUMINA's homelab scale, Kubernetes adds complexity without proportional benefit:

| Factor | Kubernetes | ULTRON Hybrid |
|--------|------------|---------------|
| Setup Time | Days | Hours |
| Maintenance | High | Low |
| Resource Overhead | 2-4GB RAM just for k8s | Minimal |
| Learning Curve | Steep | Moderate |
| Debugging | Complex | Straightforward |
| Appropriate Scale | 10+ nodes | 2-10 nodes |

### WHEN TO RECONSIDER KUBERNETES

- If cluster grows beyond 10 nodes
- If multiple teams need access
- If enterprise compliance required
- If auto-scaling is critical

---

## 4. IDM FOR MODEL DOWNLOADS

### ALWAYS USE IDM FOR:

- LLM models (GGUF, GGML)
- Large files (>1GB)
- Any HuggingFace download
- Model quantizations

### IDM BENEFITS:

- ✅ Resume capability (critical for 10GB+ models)
- ✅ Speed acceleration (8-16 connections)
- ✅ Queue management
- ✅ Schedule downloads

### CONFIGURATION:

See `config/lumina_idm_config.json` for full setup.

```powershell
# Download model with IDM
& 'scripts/powershell/Invoke-IDMGGUFDownload.ps1' `
    -Url "https://huggingface.co/TheBloke/..." `
    -ModelName "llama3:8b" `
    -Destination "D:\Ollama\models"
```

---

## 5. IMPLEMENTATION ROADMAP

### Phase 1: IMMEDIATE (Today)
- [ ] Restart Iron Legion offline nodes (Mark II, III, VI, VII)
- [x] ULTRON Unified Cluster operational
- [x] IDM configured for model downloads

### Phase 2: SHORT-TERM (This Week)
- [ ] Verify all subscription services active
- [ ] Configure cloud offload routing
- [ ] Document failover procedures

### Phase 3: OPTIMIZATION (This Month)
- [ ] Benchmark local vs cloud response times
- [ ] Tune load balancing weights
- [ ] Implement usage tracking/analytics

---

## Summary

**@PEAK for @LUMINA = HYBRID APPROACH**

1. **Ollama** for inference (simple, works)
2. **ULTRON router** for orchestration (custom, flexible)
3. **NAS Container Manager** for shared services
4. **Subscription services** for flat-rate cloud compute
5. **Pay-per-token** only as last resort

This gives you the power of distributed computing without the overhead of Kubernetes, while maximizing value from flat-rate subscriptions.

---

*Document generated: 2026-01-17*
*@LUMINA @JARVIS @ULTRON @PEAK*
