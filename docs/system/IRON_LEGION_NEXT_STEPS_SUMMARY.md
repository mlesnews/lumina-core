# Iron Legion Setup - Next Steps Summary

**Date**: 2026-01-09  
**Status**: ⏳ **IN PROGRESS**

## Current Status

### ✅ Working (3/7)
- Mark I (codellama) - Port 3001
- Mark IV (llama3) - Port 3004  
- Mark V (mistral) - Port 3005

### ⚠️ Needs Fix (4/7)
- Mark II (llama3.2) - Model file incomplete (0 GB, needs 5.55 GB)
- Mark III (qwen) - AssertionError
- Mark VI (mixtral) - AssertionError
- Mark VII (gemma) - Restarting

### ⏳ In Progress
- Router deployment on NAS (Neo automation running)
- Llama model copy to KAIJU

## Next Steps (Priority Order)

### 1. Complete Llama Model Copy → Fix Mark II
**Action:**
- Re-copy Llama model from M drive to KAIJU
- Copy to Docker volume
- Restart Mark II container

### 2. Verify Router Deployment
**Action:**
- Check Neo browser for DSM deployment
- Test: `http://10.17.17.32:3000/health`
- Deploy manually if needed

### 3. Fix Mark III & VI AssertionErrors
**Action:**
- Investigate model file integrity
- Check llama.cpp compatibility
- Adjust GPU memory allocation

### 4. Fix Mark VII
**Action:**
- Verify model file in Docker volume
- Check container logs
- Restart container

### 5. Test All Endpoints
**Action:**
- Test ports 3001-3007
- Verify all models respond

### 6. Test Expert Router
**Action:**
- Test router endpoints
- Verify intelligent routing

### 7. Integrate JARVIS
**Action:**
- Add to health check system
- Configure monitoring

---

**Priority**: Fix Mark II first (complete Llama copy)
