# Iron Legion Setup - DOIT Progress Report

**Date**: 2026-01-10  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT @JARVIS  
**Status**: ⏳ **IN PROGRESS**

## Actions Taken

### ✅ Completed
1. ✅ **IDM Path Issue Fixed**: Created directory structure for model checkpoint files
2. ✅ **HTTP Server Setup**: Started Python HTTP server on FALC (port 8888) to serve Llama model
3. ✅ **Llama Model Download Initiated**: Background download from FALC to KAIJU (5.55 GB)

### ⏳ In Progress
1. ⏳ **Llama Model Download**: HTTP download from FALC to KAIJU (5.55 GB) - running in background
2. ⏳ **Router Deployment**: Not yet deployed on NAS (Neo automation may need manual completion)

### ⚠️ Issues Identified

#### Mark III, VI, VII - AssertionError
**Error**: All three containers failing with same error:
```
assert self.model is not None
AssertionError
```

**Root Cause**: Model files exist but llama.cpp cannot load them. Possible causes:
- Model file corruption
- llama.cpp version incompatibility
- GPU memory/configuration issues
- Model file format issues

**Containers Affected**:
- `iron-legion-mark-iii-qwen-llamacpp` (qwen 1.1 GB)
- `iron-legion-mark-vi-mixtral-llamacpp` (mixtral 25 GB)
- `iron-legion-mark-vii-gemma-llamacpp` (gemma 1.6 GB)

#### Router Not Deployed
- Router endpoint `http://10.17.17.32:3000/health` not responding
- Files are on NAS but containers not started
- May need manual deployment via DSM Container Manager

## Next Steps (Priority Order)

### 1. Complete Llama Model Copy → Fix Mark II
**Status**: Download in progress

**Actions**:
1. Wait for HTTP download to complete (check file size)
2. Verify file is complete (should be ~5.55 GB)
3. Copy to Docker volume if needed
4. Restart Mark II container
5. Test endpoint: `http://10.17.17.11:3002/v1/models`

**Expected Result**: Mark II container starts successfully

---

### 2. Fix Mark III, VI, VII AssertionErrors
**Priority**: High - 3 containers affected

**Investigation Steps**:
1. Verify model file integrity (check GGUF magic bytes)
2. Check llama.cpp version in containers
3. Test model loading manually in container
4. Check GPU memory allocation
5. Verify model file paths in container

**Possible Solutions**:
- Re-download models if corrupted
- Update llama.cpp version
- Adjust container configuration (N_GPU_LAYERS, N_CTX)
- Use different quantization
- Check container resource limits

---

### 3. Deploy Router on NAS
**Status**: Files on NAS, containers not started

**Actions**:
1. Check Neo browser automation status
2. If not deployed, use DSM Container Manager GUI:
   - Navigate to Container Manager
   - Import project from `/volume1/docker/iron-legion-router`
   - Start containers
3. Or deploy via SSH: `sudo sh /volume1/docker/iron-legion-router/deploy.sh`
4. Test: `http://10.17.17.32:3000/health`

**Expected Result**: Router responds at `http://10.17.17.32:3000`

---

### 4. Test All Endpoints
**After fixes complete**:

Test all 7 model endpoints:
- Mark I: `http://10.17.17.11:3001/v1/models`
- Mark II: `http://10.17.17.11:3002/v1/models`
- Mark III: `http://10.17.17.11:3003/v1/models`
- Mark IV: `http://10.17.17.11:3004/v1/models`
- Mark V: `http://10.17.17.11:3005/v1/models`
- Mark VI: `http://10.17.17.11:3006/v1/models`
- Mark VII: `http://10.17.17.11:3007/v1/models`

---

### 5. Test Expert Router
**After router deployed**:

Test endpoints:
- Health: `http://10.17.17.32:3000/health`
- Status: `http://10.17.17.32:3000/status`
- Expert routing: `POST http://10.17.17.32:3000/expert`
- OpenAI API: `POST http://10.17.17.32:3000/v1/chat/completions`

---

### 6. Integrate JARVIS
**After all components working**:

1. Add Iron Legion models to JARVIS health check system
2. Add router/loadbalancer monitoring
3. Configure alerting for failures
4. Set up automatic failover testing

---

## Current Container Status

| Container | Status | Port | Issue |
|-----------|--------|------|-------|
| Mark I (codellama) | Up (unhealthy) | 3001 | ⚠️ Unhealthy but running |
| Mark II (llama3.2) | Restarting | 3002 | ⚠️ Model file incomplete (download in progress) |
| Mark III (qwen) | Restarting | 3003 | ❌ AssertionError - model won't load |
| Mark IV (llama3) | Up (unhealthy) | 3004 | ⚠️ Unhealthy but running |
| Mark V (mistral) | Up (unhealthy) | 3005 | ⚠️ Unhealthy but running |
| Mark VI (mixtral) | Restarting | 3006 | ❌ AssertionError - model won't load |
| Mark VII (gemma) | Restarting | 3007 | ❌ AssertionError - model won't load |

**Working**: 3/7 (Mark I, IV, V - but unhealthy)  
**Needs Fix**: 4/7 (Mark II, III, VI, VII)

---

## Immediate Actions

1. **Monitor Llama download**: Check file size on KAIJU periodically
2. **Investigate AssertionError**: Check model file integrity and llama.cpp compatibility
3. **Deploy router**: Complete router deployment on NAS
4. **Fix unhealthy containers**: Investigate why Mark I, IV, V are unhealthy

---

**Last Updated**: 2026-01-10  
**Status**: ⏳ **IN PROGRESS - DOWNLOAD RUNNING, ISSUES IDENTIFIED**
