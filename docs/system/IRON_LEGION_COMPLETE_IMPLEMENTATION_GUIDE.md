# IRON LEGION Complete Implementation & Activation Guide

**Date**: 2025-01-24  
**Status**: ⚠️ **PARTIALLY IMPLEMENTED - NEEDS COMPLETE ACTIVATION**  
**Tag**: @IRON_LEGION #local-ai #implementation #activation

---

## Executive Summary

**IRON LEGION** (KAIJU NAS 7-Model Cluster) was configured but **never fully committed to documentation and implementation/execution/activation**. This guide provides complete documentation and activation steps.

---

## Current Status

### ✅ What Exists (Partially Configured)

1. **Configuration Files**:
   - ✅ `config/kaiju_iron_legion_config.json` - KAIJU Iron Legion configuration
   - ✅ `config/local_ai_config.json` - Local AI config with Iron Legion endpoints
   - ✅ `config/ollama_model_mapping.json` - Model mappings

2. **Model Definitions**:
   - ✅ 7 models defined (codellama:13b, llama3.2:11b, etc.)
   - ✅ Endpoints configured (kaiju_no_8:11437, 10.17.17.32:11437)
   - ✅ Hardware specs documented (RTX 3090, 64GB RAM)

3. **Documentation** (Scattered):
   - ⚠️ Multiple partial docs exist but no comprehensive guide
   - ⚠️ No activation checklist
   - ⚠️ No verification steps

### ❌ What's Missing (Not Fully Implemented)

1. **Activation**:
   - ❌ Connection status unknown
   - ❌ Models not verified on KAIJU
   - ❌ Health checks not automated
   - ❌ Router/load balancer not tested

2. **Documentation**:
   - ❌ No comprehensive implementation guide
   - ❌ No activation checklist
   - ❌ No troubleshooting guide
   - ❌ No model verification procedures

3. **Integration**:
   - ❌ Not fully integrated with ULTRON
   - ❌ Auto-selection not verified
   - ❌ Failover not tested

---

## IRON LEGION Architecture

### Definition

**IRON LEGION**: 7-Model LLM Cluster on KAIJU NAS
- **Hardware**: AMD Ryzen 9 5950X, RTX 3090 (24GB VRAM), 64GB RAM
- **Endpoint**: `http://kaiju_no_8:11437` or `http://10.17.17.32:11437`
- **Role**: Primary node for ULTRON cluster
- **Provider**: Ollama-based cluster

### The 7 Models

1. **codellama:13b** (7.5GB)
   - **Role**: Primary code generation
   - **Use Cases**: Complex code generation, refactoring, architecture
   - **Context**: High complexity

2. **llama3.2:11b** (6.5GB)
   - **Role**: Secondary general purpose
   - **Use Cases**: General tasks, medium complexity decisions
   - **Context**: Medium complexity

3. **qwen2.5-coder:1.5b-base** (1.0GB)
   - **Role**: Lightweight quick
   - **Use Cases**: Quick completions, simple tasks
   - **Context**: Low complexity

4. **llama3:8b** (4.7GB)
   - **Role**: General purpose
   - **Use Cases**: Instruction following, reasoning
   - **Context**: Medium complexity

5. **mistral:7b** (4.1GB)
   - **Role**: General reasoning
   - **Use Cases**: Analysis, decision support
   - **Context**: Medium complexity

6. **mixtral-8x7b** (26.0GB, Q4: 13GB)
   - **Role**: High complexity
   - **Use Cases**: Multi-step reasoning, complex decisions
   - **Context**: Very high complexity
   - **Note**: Requires Q4/Q5 quantization for RTX 3090

7. **gemma:2b** (1.4GB)
   - **Role**: Lightweight fallback
   - **Use Cases**: Quick responses, resource-constrained
   - **Context**: Low complexity

**Total Size**: ~51.2GB (unquantized), ~38GB (Q4 quantized)

### Endpoints

**Primary Endpoints**:
- `http://kaiju_no_8:11437` (hostname)
- `http://10.17.17.32:11437` (IP address)
- `http://lesnewski.local:11437` (Bonjour/mDNS)

**Health Check**: `http://10.17.17.32:11437/api/tags`

---

## Complete Activation Guide

### Step 1: Verify KAIJU Access

#### 1.1 Check Network Connectivity

```powershell
# Ping KAIJU
ping 10.17.17.32

# Test port
Test-NetConnection -ComputerName 10.17.17.32 -Port 11437

# Test hostname resolution
Test-NetConnection -ComputerName kaiju_no_8 -Port 11437
```

**Expected**: Connection successful

#### 1.2 Verify Ollama on KAIJU

```powershell
# Check Ollama API
Invoke-WebRequest -Uri http://10.17.17.32:11437/api/tags -UseBasicParsing

# Or with curl
curl http://kaiju_no_8:11437/api/tags
```

**Expected**: JSON response with list of 7 models

#### 1.3 Verify All 7 Models

Check that all models are available on KAIJU:

```powershell
$models = @(
    "codellama:13b",
    "llama3.2:11b",
    "qwen2.5-coder:1.5b-base",
    "llama3",
    "mistral",
    "mixtral-8x7b",
    "gemma:2b"
)

foreach ($model in $models) {
    Write-Host "Checking $model..."
    # Test model availability via API
    # (Implementation depends on Ollama API structure)
}
```

**Expected**: All 7 models available

---

### Step 2: Configure Local Access

#### 2.1 Update Hosts File (If Needed)

If hostname `kaiju_no_8` doesn't resolve:

```powershell
# Run as Administrator
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "10.17.17.32`tkaiju_no_8"
```

#### 2.2 Test All Endpoints

```powershell
# Test primary endpoint
Invoke-WebRequest -Uri http://kaiju_no_8:11437/api/tags -UseBasicParsing

# Test IP endpoint
Invoke-WebRequest -Uri http://10.17.17.32:11437/api/tags -UseBasicParsing

# Test Bonjour endpoint (if available)
Invoke-WebRequest -Uri http://lesnewski.local:11437/api/tags -UseBasicParsing
```

**Expected**: All endpoints respond with same models

---

### Step 3: Integrate with ULTRON

#### 3.1 Update ULTRON Configuration

Ensure `config/cursor_ultron_model_config.json` references KAIJU Iron Legion:

```json
{
  "endpoints": {
    "primary": {
      "name": "KAIJU Iron Legion",
      "url": "http://kaiju_no_8:11437",
      "healthCheck": "http://kaiju_no_8:11437/api/tags",
      "node_role": "primary",
      "priority": 1
    }
  }
}
```

#### 3.2 Update Local AI Config

Verify `config/local_ai_config.json` has KAIJU as priority:

```json
{
  "endpoints": {
    "priority_order": [
      {
        "name": "KAIJU IRON LEGION",
        "endpoints": [
          "http://kaiju_no_8:11437",
          "http://10.17.17.32:11437"
        ],
        "priority": 1
      }
    ]
  }
}
```

---

### Step 4: Test Model Selection

#### 4.1 Test Auto-Selection

The system should automatically select the best model based on task:

- **Code Generation**: `codellama:13b`
- **General Tasks**: `llama3.2:11b`
- **Quick Tasks**: `qwen2.5-coder:1.5b-base`
- **Complex Reasoning**: `mixtral-8x7b`

#### 4.2 Manual Model Selection

If auto-selection doesn't work, manually specify model:

```json
{
  "cursor.chat.customModels": [
    {
      "name": "KAIJU Iron Legion",
      "provider": "ollama",
      "model": "codellama:13b",
      "apiBase": "http://kaiju_no_8:11437"
    }
  ]
}
```

---

### Step 5: Verify Activation

#### 5.1 Test Connection

1. Open Cursor Chat
2. Select KAIJU Iron Legion model (if available in dropdown)
3. Send test message
4. Verify response comes from KAIJU

#### 5.2 Test Model Performance

1. Test code generation with `codellama:13b`
2. Test general tasks with `llama3.2:11b`
3. Test quick tasks with `qwen2.5-coder:1.5b-base`
4. Verify response quality

#### 5.3 Monitor Resource Usage

Check KAIJU system resources:
- GPU utilization (RTX 3090 VRAM)
- CPU usage
- Memory usage
- Model loading times

---

## Configuration Files Reference

### Primary Config Files

1. **`config/kaiju_iron_legion_config.json`**
   - KAIJU Iron Legion configuration
   - Model definitions
   - Hardware specs
   - Endpoint configuration

2. **`config/local_ai_config.json`**
   - Local AI endpoints
   - Priority order
   - Iron Legion integration
   - Docker setup

3. **`config/ollama_model_mapping.json`**
   - Complete model mappings
   - HuggingFace repositories
   - Download methods
   - Roles and responsibilities

4. **`config/cursor_ultron_model_config.json`**
   - ULTRON cluster config
   - KAIJU as primary node
   - Failover configuration

---

## Troubleshooting

### Problem: Cannot Connect to KAIJU

**Solution**:
1. Verify KAIJU is powered on
2. Check network connectivity: `ping 10.17.17.32`
3. Verify Ollama is running on KAIJU
4. Check firewall settings
5. Test port: `Test-NetConnection -ComputerName 10.17.17.32 -Port 11437`
6. Update hosts file if hostname doesn't resolve

### Problem: Models Not Available

**Solution**:
1. SSH into KAIJU and check: `ollama list`
2. Pull missing models: `ollama pull codellama:13b`
3. Verify models are on correct port (11437)
4. Check Ollama configuration on KAIJU

### Problem: Slow Performance

**Solution**:
1. Check GPU utilization on KAIJU
2. Verify models are using GPU (not CPU)
3. Check network latency
4. Consider using local fallback for quick tasks
5. Verify quantization (Q4/Q5 for large models)

### Problem: Out of Memory

**Solution**:
1. Check RTX 3090 VRAM usage (24GB limit)
2. Verify mixtral-8x7b uses Q4 quantization (13GB vs 26GB)
3. Don't load all 7 models simultaneously
4. Use model offloading/swap if available

---

## Verification Checklist

- [ ] KAIJU powered on and accessible
- [ ] Network connectivity verified (ping, port test)
- [ ] Ollama running on KAIJU (`http://10.17.17.32:11437/api/tags`)
- [ ] All 7 models available on KAIJU
- [ ] Hostname resolution working (`kaiju_no_8`)
- [ ] All endpoints tested (hostname, IP, Bonjour)
- [ ] ULTRON configuration references KAIJU as primary
- [ ] Local AI config has KAIJU in priority order
- [ ] Connection tested from Cursor
- [ ] Models selectable in Cursor
- [ ] Test messages work
- [ ] Model performance verified
- [ ] Resource usage acceptable
- [ ] Failover to local works (if KAIJU unavailable)

---

## Integration with ULTRON

**IRON LEGION is the PRIMARY NODE for ULTRON cluster**:
- ULTRON uses KAIJU Iron Legion as primary
- Falls back to local laptop if KAIJU unavailable
- Auto-selects best model from 7 available

See: `docs/system/ULTRON_COMPLETE_IMPLEMENTATION_GUIDE.md`

---

## Next Steps

1. ✅ Complete this documentation
2. ⏳ Verify all 7 models on KAIJU
3. ⏳ Test model auto-selection
4. ⏳ Create health check automation
5. ⏳ Create monitoring dashboard
6. ⏳ Document model performance benchmarks

---

## Related Documentation

- **Configuration**: `config/kaiju_iron_legion_config.json`
- **Local AI Config**: `config/local_ai_config.json`
- **Model Mapping**: `config/ollama_model_mapping.json`
- **ULTRON Guide**: `docs/system/ULTRON_COMPLETE_IMPLEMENTATION_GUIDE.md`
- **Kilo Code Config**: `docs/system/KILO_CODE_PEAK_IRON_LEGION_CONFIGURATION.md`

---

**Last Updated**: 2025-01-24  
**Status**: ⚠️ **NEEDS COMPLETE ACTIVATION**  
**Maintained By**: @IRON_LEGION #local-ai