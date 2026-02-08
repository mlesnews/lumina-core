# Iron Legion Setup - Next Steps ✅

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT @JARVIS  
**Status**: ⏳ **IN PROGRESS - NEXT STEPS OUTLINED**

## Current Status Summary

### ✅ Completed
1. ✅ **Router & Load Balancer**: Files deployed to NAS, Neo automation running
2. ✅ **Model Downloads**: Llama and Gemma downloaded to M drive (5.55 GB, 1.59 GB)
3. ✅ **Network Configuration**: Containers connected to Docker network
4. ✅ **Working Models**: Mark I, IV, V operational (3/7)

### ⏳ In Progress
1. ⏳ **Llama Model Copy**: SCP copy from FALC to KAIJU (5.55 GB) - background job
2. ⏳ **Router Deployment**: Neo automation deploying via DSM Container Manager

### ⚠️ Issues to Fix
1. ⚠️ **Mark II (llama3.2)**: Model file incomplete (64K, needs 5.55 GB)
2. ⚠️ **Mark III (qwen)**: AssertionError - model file exists but won't load
3. ⚠️ **Mark VI (mixtral)**: AssertionError - model file exists but won't load
4. ⚠️ **Mark VII (gemma)**: Restarting - may need model file verification

## Next Steps (Priority Order)

### Step 1: Complete Llama Model Copy ⏳
**Status**: SCP copy running in background

**Action:**
1. Wait for SCP copy to complete (check file size on KAIJU)
2. Verify file is complete: `ssh 10.17.17.11 "Get-Item 'D:\Ollama\models\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf' | Select-Object Length"`
3. Copy to Docker volume: `docker cp` from host to container
4. Restart Mark II container

**Expected Result**: Mark II container starts successfully

---

### Step 2: Verify Router Deployment ⏳
**Status**: Neo automation running

**Action:**
1. Check Neo browser window for deployment progress
2. Verify router responds: `http://10.17.17.32:3000/health`
3. If not deployed, complete via Container Manager GUI manually

**Expected Result**: Router available at `http://10.17.17.32:3000`

---

### Step 3: Fix Mark III (qwen) AssertionError ⚠️
**Issue**: Model file exists (1.1 GB) but llama.cpp fails with AssertionError

**Investigation Steps:**
1. Check model file integrity (GGUF magic bytes)
2. Verify llama.cpp version compatibility
3. Check GPU memory allocation
4. Test model loading manually in container
5. Adjust container configuration (N_GPU_LAYERS, N_CTX)

**Possible Solutions:**
- Re-download model if corrupted
- Update llama.cpp version in container
- Adjust GPU layer allocation
- Use different quantization

---

### Step 4: Fix Mark VI (mixtral) AssertionError ⚠️
**Issue**: Model file exists (25 GB) but llama.cpp fails with AssertionError

**Investigation Steps:**
1. Check model file integrity
2. Verify GPU memory (25 GB model needs significant memory)
3. Check container resource limits
4. Test with reduced GPU layers

**Possible Solutions:**
- Reduce N_GPU_LAYERS if memory constrained
- Verify model file not corrupted
- Check container memory limits
- Consider CPU-only fallback if GPU insufficient

---

### Step 5: Fix Mark VII (gemma) ⚠️
**Status**: Restarting

**Action:**
1. Verify model file in Docker volume (1.6 GB)
2. Check container logs for specific error
3. Restart container after verification

**Expected Result**: Mark VII starts successfully

---

### Step 6: Test All Model Endpoints ⏳
**After all models are running:**

**Test Script:**
```python
endpoints = [
    ("Mark I", "http://10.17.17.11:3001/v1/models"),
    ("Mark II", "http://10.17.17.11:3002/v1/models"),
    ("Mark III", "http://10.17.17.11:3003/v1/models"),
    ("Mark IV", "http://10.17.17.11:3004/v1/models"),
    ("Mark V", "http://10.17.17.11:3005/v1/models"),
    ("Mark VI", "http://10.17.17.11:3006/v1/models"),
    ("Mark VII", "http://10.17.17.11:3007/v1/models"),
]
```

**Expected Result**: All 7 endpoints respond with 200 OK

---

### Step 7: Test Expert Router ⏳
**After router is deployed:**

**Test:**
1. Test health endpoint: `http://10.17.17.32:3000/health`
2. Test status endpoint: `http://10.17.17.32:3000/status`
3. Test expert routing: `POST http://10.17.17.32:3000/expert`
4. Test OpenAI-compatible API: `POST http://10.17.17.32:3000/v1/chat/completions`

**Expected Result**: Router intelligently routes to best expert model

---

### Step 8: Integrate into JARVIS Health Checks ⏳
**After all components working:**

**Action:**
1. Add Iron Legion models to JARVIS health check system
2. Add router/loadbalancer health monitoring
3. Configure alerting for model failures
4. Set up automatic failover testing

**Expected Result**: JARVIS monitors all Iron Legion components

---

## Immediate Actions (Do Now)

1. **Check SCP copy status**: Verify Llama model file size on KAIJU
2. **Monitor Neo automation**: Check browser window for DSM deployment
3. **Verify router**: Test `http://10.17.17.32:3000/health` endpoint

## Priority Order

1. **High Priority**: Complete Llama copy → Fix Mark II
2. **High Priority**: Verify router deployment
3. **Medium Priority**: Fix Mark III and Mark VI AssertionErrors
4. **Medium Priority**: Fix Mark VII restart issue
5. **Low Priority**: Testing and integration (after fixes)

---

**Last Updated**: 2026-01-09  
**Status**: ⏳ **NEXT STEPS OUTLINED - PROCEED WITH PRIORITY ORDER**
