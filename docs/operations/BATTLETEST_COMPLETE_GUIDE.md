# #BATTLETEST - ULTRON & IRON LEGION Complete Guide
                    -LUM THE MODERN

## 🎯 MISSION OVERVIEW

Comprehensive battle test of both ULTRON and IRON LEGION AI clusters with three phases:
1. **ESTABLISH FUNCTIONALITY** - Test and fix all issues
2. **PUSH TO MAX** - Stress test to find maximum capacity  
3. **SET BASELINE AT 50%** - Balanced, holistic ecosystem

---

## 📋 PHASE 1: ESTABLISH FUNCTIONALITY

### Current Status: ✅ **IN PROGRESS**

**Goal**: Test all endpoints, identify issues, and fix them.

### ULTRON Cluster:
- ✅ **ULTRON KAIJU** (NAS): ✅ Working - smollm:135m, llama3.2:3b
- ⚠️ **ULTRON Local**: ⚠️ No models - **FIXING** (pulling models in background)
- ❌ **ULTRON KUBE**: Health check passes, inference needs verification

### IRON LEGION Cluster:
- ✅ **Mark III - Quick**: ✅ Working - qwen2.5-coder:1.5b (18.79s)
- ✅ **Mark VI - Complex**: ✅ Working - qwen2.5-coder:1.5b (2.50s)
- ✅ **Mark VII - Fallback**: ✅ Working - qwen2.5-coder:1.5b (2.49s)
- ⚠️ **Mark I - Code**: Health check passes, inference needs fix
- ⚠️ **Mark IV - Balanced**: Health check passes, inference needs fix
- ⚠️ **Mark V - Reasoning**: Health check passes, inference needs fix
- ⚠️ **Mark II - General**: Timeout issues

### Fixes Applied:
1. ✅ Auto-detect available models
2. ✅ Improved error handling
3. ✅ Model pulling script created
4. 🔄 **IN PROGRESS**: Pulling models to ULTRON Local

---

## 🔥 PHASE 2: PUSH TO MAX

### Goal: Find Maximum Capacity

**Process**:
1. Gradually increase concurrent requests
2. Measure throughput and latency
3. Find breaking point
4. Record maximum capacity

**Expected Results**:
- Maximum concurrent requests per node
- Maximum throughput (req/s) per node
- Latency at max load
- Error rates at max load

---

## ⚖️ PHASE 3: SET BASELINE AT 50%

### Goal: Balanced, Holistic Ecosystem

**Configuration**:
- Baseline = 50% of maximum capacity
- Balanced load distribution
- Sustainable long-term operation
- Room for spikes (50% headroom)

**Output**:
- Baseline configuration saved to `config/ultron_iron_legion_baseline.json`
- Per-node baseline concurrent requests
- Per-node baseline throughput
- Total cluster baseline metrics

---

## 🚀 USAGE

### Run All Phases:
```bash
python scripts/python/battletest_ultron_iron_legion_comprehensive.py
```

### Run Specific Phase:
```bash
# Phase 1: Establish functionality
python scripts/python/battletest_ultron_iron_legion_comprehensive.py --phase 1

# Phase 2: Push to max
python scripts/python/battletest_ultron_iron_legion_comprehensive.py --phase 2

# Phase 3: Set baseline at 50%
python scripts/python/battletest_ultron_iron_legion_comprehensive.py --phase 3
```

### Fix Missing Models:
```bash
python scripts/python/fix_missing_models.py
```

### Check Available Models:
```bash
python scripts/python/check_available_models.py
```

---

## 📊 EXPECTED RESULTS

### Phase 1 Complete:
- ✅ All ULTRON nodes functional
- ✅ All IRON LEGION nodes functional
- ✅ All models available and responding

### Phase 2 Complete:
- 🔥 Maximum capacity identified for each node
- 🔥 Total cluster max throughput
- 🔥 Total cluster max concurrent

### Phase 3 Complete:
- ⚖️ Baseline configuration at 50%
- ⚖️ Balanced ecosystem operational
- ⚖️ Configuration saved

---

## 🎯 SUCCESS CRITERIA

### Phase 1:
- ✅ 80%+ nodes passing health checks
- ✅ 80%+ nodes passing inference tests
- ✅ All critical nodes functional

### Phase 2:
- 🔥 Maximum capacity identified
- 🔥 Stress test completed without crashes
- 🔥 Metrics recorded

### Phase 3:
- ⚖️ Baseline set at 50% of max
- ⚖️ Configuration saved
- ⚖️ Ecosystem balanced

---

## 📝 NOTES

- Model pulling may take time (especially large models like qwen2.5:72b)
- Some Iron Legion nodes may need Docker container restarts
- KUBE endpoint may need different API format verification
- Baseline at 50% provides 50% headroom for spikes

---

*Document generated: 2026-01-17*
*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
