# KAIJU IRON LEGION - Local LLM Cluster on KAIJU

## 🎯 Overview

**KAIJU IRON LEGION** is a **LOCAL LLM resource cluster** running directly on the **KAIJU** machine. It is NOT a remote or cloud service - it's a local Ollama-based LLM cluster providing high-performance AI inference on your local network.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    KAIJU MACHINE                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │        KAIJU IRON LEGION LLM CLUSTER             │  │
│  │          (LOCAL OLLAMA CLUSTER)                  │  │
│  │                                                   │  │
│  │  Port: 11437 (Ollama API)                        │  │
│  │  Hostname: kaiju_no_8 / lesnewski.local          │  │
│  │  Type: LOCAL (not remote/cloud)                  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  Models Available:                                       │
│  • Mark I:   codellama:13b (Primary code generation)    │
│  • Mark II:  llama3.2:11b (Secondary general)           │
│  • Mark III: qwen2.5-coder:1.5b-base (Lightweight)      │
│  • Mark IV:  llama3:8b (General purpose)                │
│  • Mark V:   mistral:7b (General reasoning)             │
│  • Mark VI:  mixtral:8x7b (High complexity)             │
│  • Mark VII: gemma:2b (Lightweight fallback)            │
└─────────────────────────────────────────────────────────┘
```

## 🔌 Connection Endpoints

### Primary Endpoints (Local Network)
```python
IRON_LEGION_ENDPOINTS = [
    "http://kaiju_no_8:11437",      # KAIJU hostname (local network)
    "http://lesnewski.local:11437",  # Domain name (if DNS configured)
    "http://localhost:11437",        # Direct localhost (on KAIJU itself)
    "http://127.0.0.1:11437"         # IP localhost (on KAIJU itself)
]
```

### Access Methods

#### From Laptop/Desktop (Remote Access)
```python
# Use KAIJU hostname or domain
endpoint = "http://kaiju_no_8:11437"
# OR
endpoint = "http://lesnewski.local:11437"
```

#### From KAIJU Machine Itself (Local Access)
```python
# Use localhost
endpoint = "http://localhost:11437"
# OR
endpoint = "http://127.0.0.1:11437"
```

## 🚀 Key Characteristics

### ✅ **LOCAL Resource**
- **Location**: Runs on KAIJU machine hardware
- **Network**: Local network only (not internet-facing)
- **Latency**: Very low (local network latency)
- **Privacy**: All data stays on local network
- **Cost**: No cloud API costs

### 🔧 **Technical Stack**
- **Engine**: Ollama (local LLM runtime)
- **Protocol**: HTTP REST API (Ollama-compatible)
- **Port**: 11437 (default Ollama port on KAIJU)
- **Models**: Local model files stored on KAIJU

### 📊 **Performance**
- **Hardware**: KAIJU's local GPU/CPU resources
- **Parallel Processing**: Supports batch processing
- **Model Loading**: Models loaded into KAIJU's RAM/VRAM
- **Inference Speed**: Limited by KAIJU hardware specs

## 🎯 Use Cases

### Ideal For:
- ✅ Code generation and analysis
- ✅ Local data processing (privacy-sensitive)
- ✅ High-volume batch processing
- ✅ Offline AI workloads
- ✅ Cost-effective AI inference

### NOT Suitable For:
- ❌ Internet-accessible services (unless configured)
- ❌ Cloud-scale deployments
- ❌ Public API endpoints (by default)

## 🔧 Configuration

### Python Configuration
```python
# KAIJU IRON LEGION Configuration
IRON_LEGION_CONFIG = {
    "name": "KAIJU IRON LEGION",
    "type": "local_cluster",
    "location": "KAIJU machine",
    "endpoints": [
        "http://kaiju_no_8:11437",
        "http://lesnewski.local:11437"
    ],
    "api_type": "ollama",
    "is_local": True,
    "is_remote": False,
    "requires_network": True,  # Network connection to KAIJU
    "models": {
        "primary": "codellama:13b",
        "secondary": "llama3.2:11b",
        "lightweight": "qwen2.5-coder:1.5b-base"
    }
}
```

### Connection Testing
```python
import requests

def test_iron_legion_connection():
    """Test connection to KAIJU IRON LEGION local cluster"""
    endpoints = [
        "http://kaiju_no_8:11437",
        "http://lesnewski.local:11437",
        "http://localhost:11437"  # If running on KAIJU
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{endpoint}/api/tags", timeout=5)
            if response.status_code == 200:
                print(f"✅ Connected to IRON LEGION at {endpoint}")
                return endpoint
        except Exception as e:
            print(f"❌ {endpoint}: {e}")
    
    return None

# Test connection
active_endpoint = test_iron_legion_connection()
```

## 📝 Integration Examples

### Peak AI Orchestrator
```python
from peak_ai_orchestrator import PEAK_AI_Orchestrator

orchestrator = PEAK_AI_Orchestrator()

# KAIJU IRON LEGION models are configured as:
# - Provider: "kaiju"
# - Endpoint: "http://10.17.17.32:3000" or "http://kaiju_no_8:11437"
# - Type: LOCAL CLUSTER

# Use for local high-performance inference
task_id = await orchestrator.submit_task(
    content="Generate Python code for...",
    task_type="code_generation",
    complexity="high"
)
```

### Direct Ollama API Access
```python
import requests

# Connect to KAIJU IRON LEGION
IRON_LEGION_ENDPOINT = "http://kaiju_no_8:11437"

# Generate with local model
response = requests.post(
    f"{IRON_LEGION_ENDPOINT}/api/generate",
    json={
        "model": "codellama:13b",
        "prompt": "Write a Python function to...",
        "stream": False
    }
)

result = response.json()
print(result["response"])
```

## 🔍 Monitoring

### Status Check
```bash
# Check IRON LEGION status
python scripts/python/kaiju_iron_legion_monitor.py --once

# Continuous monitoring
python scripts/python/kaiju_iron_legion_monitor.py --interval 30
```

### Available Models
```bash
# List available models on KAIJU
curl http://kaiju_no_8:11437/api/tags

# Or using the monitor script
python scripts/python/show_ollama_model_files.py list
```

## ⚠️ Important Notes

### Network Requirements
- ✅ **Local Network**: KAIJU and client machines must be on same network
- ✅ **Hostname Resolution**: `kaiju_no_8` must resolve on network
- ✅ **Firewall**: Port 11437 must be open on KAIJU
- ⚠️ **KAIJU Must Be Running**: IRON LEGION requires KAIJU to be powered on

### Security Considerations
- 🔒 **Local Network Only**: By default, not accessible from internet
- 🔒 **No Authentication**: Typically runs without auth (local network assumed safe)
- 🔒 **Firewall**: Ensure proper firewall rules if exposing beyond local network

### Performance Notes
- ⚡ **Hardware Dependent**: Performance limited by KAIJU hardware
- ⚡ **Model Loading**: Large models take time to load into memory
- ⚡ **Concurrent Requests**: Limited by KAIJU's CPU/GPU capacity
- ⚡ **Network Latency**: Very low (local network)

## 📚 Related Documentation

- [KAIJU IRON LEGION Model Files](./KAIJU_IRON_LEGION_MODEL_FILES.md)
- [Peak AI Orchestrator](./../scripts/python/peak_ai_orchestrator.py)
- [Ollama Documentation](https://ollama.ai/docs)

## 🆘 Troubleshooting

### Connection Issues

**Problem**: Cannot connect to `http://kaiju_no_8:11437`

**Solutions**:
1. Verify KAIJU is powered on and network-connected
2. Check hostname resolution: `ping kaiju_no_8`
3. Try IP address: `http://10.17.17.32:11437` (if known)
4. Check firewall on KAIJU allows port 11437
5. Verify Ollama is running on KAIJU: `ssh kaiju_no_8 "docker ps | grep ollama"`

**Problem**: Models not found

**Solutions**:
1. Pull models on KAIJU: `ssh kaiju_no_8 "ollama pull codellama:13b"`
2. Check model list: `curl http://kaiju_no_8:11437/api/tags`
3. Verify model files exist on KAIJU

### Performance Issues

**Problem**: Slow inference

**Solutions**:
1. Check KAIJU system resources (CPU/GPU usage)
2. Use smaller/quantized models for faster inference
3. Limit concurrent requests
4. Verify network latency: `ping kaiju_no_8`

---

## ✅ Summary

**KAIJU IRON LEGION** is a **LOCAL LLM cluster** running on your **KAIJU** machine. It provides:
- ✅ High-performance local AI inference
- ✅ Privacy-preserving processing
- ✅ Cost-effective (no cloud costs)
- ✅ Low latency (local network)
- ✅ Full control over models and data

**Remember**: This is a **LOCAL** resource - KAIJU must be running and accessible on your local network to use IRON LEGION.

