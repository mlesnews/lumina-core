# GPU Usage Verification for AI/LLM Endpoints
                    -LUM THE MODERN

## 📊 Current GPU Status

### Local Host (MILLENNIUM-FALC):
- **GPU**: NVIDIA GeForce RTX 5090 Laptop GPU
- **VRAM**: 24GB total
- **Current Usage**: 3% utilization, ~2.1GB memory used
- **Status**: ✅ GPU detected and available

### ULTRON Local (localhost:11434):
- **GPU**: RTX 5090 Mobile (24GB VRAM)
- **Status**: Should use GPU (if models are loaded)
- **Current**: No models loaded (needs model pull)

### ULTRON KAIJU (NAS - 10.17.17.32:11434):
- **GPU**: ❌ **CPU-only** (Synology NAS has no GPU)
- **Status**: Runs on CPU
- **Models**: smollm:135m (CPU inference)

### IRON LEGION (KAIJU_NO_8 - 10.17.17.11):
- **GPU**: RTX 3090 (24GB VRAM)
- **Status**: ✅ Should use GPU (shared across 7 nodes)
- **Nodes**: 7 Iron Legion endpoints (ports 3001-3007)

---

## 🔍 How to Verify GPU Usage

### 1. Check nvidia-smi
```bash
nvidia-smi
```
Look for:
- GPU utilization percentage
- Memory usage (should increase during inference)
- Process names (ollama, python, etc.)

### 2. Check Ollama Model Status
```bash
curl http://localhost:11434/api/ps
```
Look for `size_vram` field - if > 0, model is using GPU memory.

### 3. Monitor During Inference
```bash
# Run inference and watch GPU
watch -n 1 nvidia-smi
```

### 4. Check Docker Container GPU Access
```bash
docker exec ollama nvidia-smi
```
If this works, GPU is accessible to Ollama container.

---

## ⚠️ Important Notes

### ULTRON Local:
- **Should use GPU** (RTX 5090 Mobile)
- **Verify**: Check if Ollama has GPU access in Docker
- **Action**: May need to configure Docker GPU passthrough

### ULTRON KAIJU (NAS):
- **CPU-only** - This is expected (NAS has no GPU)
- **Models**: Will run slower but still functional

### IRON LEGION:
- **Should use GPU** (RTX 3090 on desktop)
- **Shared**: All 7 nodes share the same GPU
- **Verify**: Check GPU usage on KAIJU_NO_8 desktop

---

## 🔧 Troubleshooting

### If GPU Not Being Used:

1. **Check Docker GPU Access**:
   ```bash
   docker exec ollama nvidia-smi
   ```

2. **Check Ollama Configuration**:
   ```bash
   docker exec ollama env | grep -i cuda
   ```

3. **Verify NVIDIA Container Runtime**:
   ```bash
   docker info | grep -i runtime
   ```

4. **Check Model Quantization**:
   - Some quantized models may use CPU
   - Check model file for GPU settings

---

## 📈 Expected GPU Usage

### During Inference:
- **ULTRON Local**: 5-15% GPU utilization, 2-8GB VRAM
- **IRON LEGION**: 10-30% GPU utilization, 4-12GB VRAM (shared)
- **ULTRON KAIJU**: 0% (CPU-only)

### Idle:
- **ULTRON Local**: 0-3% GPU utilization, ~2GB VRAM (if models loaded)
- **IRON LEGION**: 0-5% GPU utilization, ~2-4GB VRAM (if models loaded)

---

*Document generated: 2026-01-17*
*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
