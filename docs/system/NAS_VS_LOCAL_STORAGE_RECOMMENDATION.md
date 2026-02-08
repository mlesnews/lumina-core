# NAS vs Local Storage Recommendation for Iron Legion Models

**Date**: 2026-01-09
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT @JARVIS
**Status**: ✅ **RECOMMENDATION PROVIDED**

## Question

Should Iron Legion models be loaded from NAS (M drive) or local SSD on KAIJU?

## Analysis

### Current Situation
- **Models Location**: NAS (M drive) at `\\10.17.17.32\models`
- **KAIJU Local**: `D:\Ollama\models` (SSD)
- **Docker Volume**: `/var/lib/docker/volumes/iron-legion-llamacpp_iron-legion-models/_data`
- **Model Sizes**: 1-25 GB each

### Model Loading Behavior

**Critical Understanding**: LLM models are loaded **once** at container startup:
1. Container starts
2. Model file read from disk → loaded into GPU memory
3. All inference uses GPU memory (not disk)
4. Disk I/O only happens at startup

### Performance Comparison

#### NAS (M Drive) - Network Storage
**Pros:**
- ✅ No local disk space usage (saves ~50GB+ on KAIJU)
- ✅ Centralized storage (easier management)
- ✅ Models accessible from multiple hosts
- ✅ No need to copy large files

**Cons:**
- ⚠️ Network latency (initial load time)
- ⚠️ Network dependency (NAS must be available)
- ⚠️ Potential bandwidth constraints during startup

**Expected Impact:**
- **Startup Time**: +30-60 seconds per container (one-time)
- **Inference Performance**: **ZERO impact** (uses GPU memory)
- **Reliability**: Depends on network/NAS availability

#### Local SSD (D:\Ollama\models)
**Pros:**
- ✅ Faster initial load (no network latency)
- ✅ No network dependency
- ✅ More reliable (local storage)

**Cons:**
- ❌ Uses local disk space (~50GB+)
- ❌ Need to copy files from NAS
- ❌ Models duplicated across systems

**Expected Impact:**
- **Startup Time**: Faster (local disk)
- **Inference Performance**: **SAME** (uses GPU memory)
- **Reliability**: Higher (local storage)

## Recommendation

### **Hybrid Approach (Recommended)**

1. **Primary Storage**: NAS (M drive)
   - Store all models on NAS
   - Single source of truth
   - Accessible from all hosts

2. **Local Cache**: Local SSD (optional)
   - Copy frequently-used models to local SSD
   - Use for critical production models
   - Faster startup for those specific models

3. **Docker Volume Strategy**:
   - **Option A**: Mount NAS directly into containers
     - Pros: Always up-to-date, no duplication
     - Cons: Network dependency
   - **Option B**: Copy from NAS to local, then mount local
     - Pros: Faster startup, more reliable
     - Cons: Disk space usage, need sync mechanism

### **For Iron Legion Specifically**

**Recommendation: Load from NAS (M drive)**

**Rationale:**
1. ✅ Models are large (5-25 GB) - saves significant local disk space
2. ✅ Startup time impact is minimal (one-time, 30-60 sec)
3. ✅ Inference performance is identical (GPU memory)
4. ✅ Centralized management is valuable
5. ✅ Network is likely gigabit (fast enough for sequential reads)
6. ✅ NAS is reliable (Synology system)

**Implementation:**
- Mount M drive on KAIJU (if not already)
- Point Docker volume to NAS location OR
- Copy models from NAS to local on first use (lazy loading)
- Use symbolic links or bind mounts

### **Alternative: Smart Caching**

If startup time becomes an issue:
- Keep most models on NAS
- Cache frequently-used models locally
- Implement sync script to update local cache from NAS

## Implementation Options

### Option 1: Direct NAS Mount (Simplest)
```powershell
# On KAIJU, ensure M drive is mapped
# Docker volume points to M:\models
docker volume create --driver local \
  --opt type=none \
  --opt device=M:\models \
  --opt o=bind \
  iron-legion-models-nas
```

### Option 2: Local Copy with Sync (Recommended)
```powershell
# Copy from NAS to local on first use
# Keep NAS as source of truth
# Sync periodically or on-demand
```

### Option 3: Hybrid (Best of Both)
- Critical models (Mark I, IV, V): Local SSD
- Less critical models: NAS
- Implement smart caching

## Conclusion

**For Iron Legion: NAS is acceptable and recommended**

The one-time startup delay (30-60 seconds) is worth the benefits:
- Disk space savings
- Centralized management
- No performance impact on inference
- Easier updates and maintenance

**Action**: Proceed with loading models from NAS (M drive) on KAIJU.

---

**Last Updated**: 2026-01-09
**Status**: ✅ **RECOMMENDATION: USE NAS**
