# JARVIS Remote Compute Architecture

## Overview

The JARVIS Iron Legion now offloads heavy computation to Azure cloud services, minimizing local CPU/GPU usage. The framework intelligently routes compute-intensive tasks to remote servers while maintaining responsive local display.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LOCAL CLIENT (Minimal)                     │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Iron Legion Core (Display Only)                       │  │
│  │  - Tkinter Canvas (Display)                            │  │
│  │  - Input Handling (Mouse, Keyboard)                   │  │
│  │  - State Management (Lightweight)                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                          ↕ HTTP/HTTPS                         │
└─────────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────────┐
│              AZURE FRAMEWORK (Heavy Compute)                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Azure Functions - RenderIronLegion                    │  │
│  │  - Image Rendering (PIL/ImageDraw)                     │  │
│  │  - Complex Graphics Processing                         │  │
│  │  - Frame Generation                                    │  │
│  └────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Azure Cognitive Services - Vision                     │  │
│  │  - VLM Processing                                      │  │
│  │  - Screenshot Analysis                                  │  │
│  │  - Visual Context Understanding                         │  │
│  └────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Azure Functions - Compute Tasks                       │  │
│  │  - State Machine Logic                                  │  │
│  │  - Physics Calculations                                 │  │
│  │  - AI Decision Making                                   │  │
│  └────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Components

### 1. Hybrid Renderer (`jarvis_remote_renderer.py`)

**Purpose**: Intelligently routes rendering requests to remote servers with automatic fallback.

**Features**:
- Remote rendering via Azure Functions
- Automatic fallback to local rendering on failure
- Caching for offline resilience
- VLM processing via Azure Cognitive Services
- Generic computation offloading

**Usage**:
```python
from jarvis_remote_renderer import HybridRenderer

renderer = HybridRenderer()
image_bytes = renderer.render(
    state="armor",
    animation_frame=0,
    transformation_progress=1.0,
    size=180
)
```

### 2. Remote Render Service

**Endpoints**:
- **Render Endpoint**: `https://{function_app}.azurewebsites.net/api/RenderIronLegion`
- **VLM Endpoint**: `https://{vision_service}.cognitiveservices.azure.com/vision/v3.2/analyze`
- **Compute Endpoint**: Configurable custom API

**Request Format**:
```json
{
  "state": "armor",
  "animation_frame": 42,
  "transformation_progress": 1.0,
  "size": 180,
  "timestamp": "2026-01-14T00:00:00"
}
```

**Response Format**:
```json
{
  "image": "base64_encoded_png_bytes",
  "render_time_ms": 45,
  "server": "azure-functions"
}
```

### 3. Azure Function Template

The remote renderer expects an Azure Function with the following structure:

**Function Name**: `RenderIronLegion`
**Trigger**: HTTP POST
**Input**: JSON payload with rendering parameters
**Output**: PNG image (base64 encoded or binary)

## Benefits

### 1. **Reduced Local CPU/GPU Usage**
- Heavy PIL/ImageDraw rendering happens on Azure
- Local machine only handles display and input
- Minimal memory footprint

### 2. **Scalability**
- Azure Functions auto-scale based on demand
- Multiple instances can handle concurrent requests
- No local resource constraints

### 3. **Reliability**
- Automatic fallback to local rendering
- Caching for offline resilience
- Health monitoring and retry logic

### 4. **Cost Efficiency**
- Pay-per-use Azure Functions pricing
- No need for high-end local GPU
- Shared compute resources

## Configuration

### Azure Services Config

Located at: `config/azure_services_config.json`

Key settings:
```json
{
  "azure_functions": {
    "function_app_name": "jarvis-lumina-functions",
    "enabled": true
  },
  "cognitive_services": {
    "services": {
      "vision": {
        "name": "jarvis-lumina-vision",
        "enabled": true
      }
    }
  }
}
```

### Environment Variables

- `AZURE_VISION_KEY`: Azure Cognitive Services Vision API key
- `AZURE_FUNCTION_KEY`: Azure Function authentication key (if required)

## Fallback Strategy

1. **Primary**: Remote rendering via Azure Functions
2. **Secondary**: Cached frame from last successful render
3. **Tertiary**: Local rendering (full PIL/ImageDraw pipeline)

The system automatically switches to local rendering after 3 consecutive remote failures.

## Performance

### Remote Rendering
- **Latency**: ~50-200ms (depending on network)
- **Throughput**: Scales with Azure Functions
- **Cost**: Pay-per-execution

### Local Rendering
- **Latency**: ~10-30ms (no network)
- **Throughput**: Limited by local CPU
- **Cost**: Free (but uses local resources)

## Monitoring

The remote renderer logs:
- Remote render success/failure rates
- Fallback triggers
- Response times
- Error details

Check logs for:
```
✅ Remote render successful: 12345 bytes
⚠️  Remote render timeout, using fallback
🔄 Falling back to local rendering
```

## Future Enhancements

1. **WebSocket Streaming**: Real-time frame streaming for lower latency
2. **GPU Acceleration**: Azure GPU instances for faster rendering
3. **Edge Computing**: Azure Edge locations for reduced latency
4. **Batch Processing**: Queue multiple frames for batch rendering
5. **Predictive Pre-rendering**: Pre-render likely next frames

## Troubleshooting

### Remote Rendering Not Working

1. Check Azure Functions are deployed and running
2. Verify network connectivity
3. Check authentication keys in Azure Key Vault
4. Review function logs in Azure Portal

### High Latency

1. Check network connection speed
2. Consider using Azure Edge locations
3. Enable frame caching
4. Reduce frame resolution if needed

### Fallback to Local

1. Check remote endpoint configuration
2. Verify Azure Function is accessible
3. Review error logs for specific failures
4. Test endpoint manually with curl/Postman

## Security

- All API keys stored in Azure Key Vault
- HTTPS-only communication
- Managed Identity authentication preferred
- Service Principal fallback
- No sensitive data in request payloads
