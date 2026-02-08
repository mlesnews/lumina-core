# Armoury Crate AI/API Integration

## Overview

Tight integration with ASUS Armoury Crate's AI/API system, providing direct communication with Armoury Crate services, devices, and AI features.

## Architecture

### Integration Layers

1. **Direct Process Communication**
   - Communicates with `ArmouryCrateControlInterface` process
   - Direct service queries via Windows services

2. **Registry-Based Communication**
   - Reads/writes to Armoury Crate registry keys
   - Device discovery via registry enumeration
   - State management through registry values

3. **COM Interface** (if available)
   - Windows COM interface for Armoury Crate
   - Direct object model access

4. **AI-Powered Learning**
   - Learns from control actions
   - Predicts best actions based on success rates
   - Pattern recognition and optimization

## API Endpoints

### Device Management

#### List Devices
```python
response = await api.call_api("/devices")
# Returns: List of all discovered devices
```

#### Get Device State
```python
response = await api.call_api(f"/devices/{device_id}/state")
# Returns: Current device state
```

#### Control Device
```python
response = await api.call_api(
    f"/devices/{device_id}/control",
    method="POST",
    data={
        "command": "set_lighting",
        "params": {"brightness": 50, "effect": "static"}
    }
)
```

### Lighting Control

#### Get Lighting State
```python
response = await api.call_api("/lighting", method="GET")
# Returns: Current lighting configuration
```

#### Set Lighting
```python
response = await api.call_api(
    "/lighting",
    method="POST",
    data={
        "action": "set",
        "config": {
            "brightness": 0,
            "effect": "off",
            "zones": {...}
        }
    }
)
```

### Performance Control

#### Get Performance Settings
```python
response = await api.call_api("/performance", method="GET")
```

#### Set Performance Settings
```python
response = await api.call_api(
    "/performance",
    method="POST",
    data={
        "action": "set",
        "settings": {
            "mode": "performance",
            "fan_curve": {...}
        }
    }
)
```

### AI Features

#### AI Prediction
```python
response = await api.call_api(
    "/ai/predict",
    method="POST",
    data={
        "type": "action",
        "context": {
            "device": "keyboard",
            "action": "set_lighting"
        }
    }
)
# Returns: Predicted best action with confidence score
```

## Usage

### Basic Integration

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate_api import create_armoury_crate_api

# Create API instance
api = create_armoury_crate_api(project_root=project_root)

# List devices
response = await api.call_api("/devices")
if response.success:
    devices = response.data["devices"]
    print(f"Found {len(devices)} devices")
```

### Integrated with Main Integration

The API is automatically integrated into the main `ArmouryCrateIntegration`:

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration

# Create integration (API is automatically included)
integration = create_armoury_crate_integration()

# Access API
if integration.api:
    response = await integration.api.call_api("/devices")
```

## AI Learning System

### Learning Mechanism

The API learns from every control action:

1. **Success Rate Tracking**
   - Tracks success rate for each action type
   - Uses moving average for reliability
   - Updates after each control attempt

2. **Pattern Recognition**
   - Stores patterns of successful actions
   - Context-aware learning
   - Device-specific patterns

3. **Prediction**
   - Predicts best action based on:
     - Historical success rates
     - Context similarity
     - Device capabilities

### Learning Data Storage

Learning data is stored in:
```
data/armoury_crate/ai_cache/learning_data.json
```

Contains:
- `patterns`: Historical action patterns
- `success_rates`: Success rates per action
- `predictions`: Cached predictions

## Device Discovery

### Automatic Discovery

Devices are automatically discovered on initialization:

1. **Registry Enumeration**
   - Scans `HKCU\SOFTWARE\ASUS\ArmouryDevice`
   - Scans `HKLM\SOFTWARE\ASUS\ArmouryDevice`
   - Enumerates all device subkeys

2. **Device Registration**
   - Creates `ArmouryCrateDevice` objects
   - Stores capabilities and current state
   - Available via `/devices` endpoint

### Manual Discovery

```python
# Refresh device list
api._discover_devices()

# Access discovered devices
for device_id, device in api.devices.items():
    print(f"{device.name} ({device.device_type})")
```

## Registry Communication

### Registry Paths

- **HKCU**: `HKCU\SOFTWARE\ASUS\ArmouryDevice`
- **HKLM**: `HKLM\SOFTWARE\ASUS\ArmouryDevice`
- **Aura**: `HKCU\SOFTWARE\ASUS\ArmouryDevice\Aura`
- **Lighting**: `HKCU\SOFTWARE\ASUS\ArmouryDevice\Lighting`

### Reading State

```python
# Query device state
state = await api._query_device_state(device_id)

# Get lighting state
lighting = await api._get_lighting_state()
```

### Writing State

```python
# Set lighting
result = await api._set_lighting({
    "brightness": 0,
    "effect": "off"
})
```

## COM Interface (Optional)

If `pywin32` is available, COM interface is attempted:

```python
# COM interface names tried:
- "ArmouryCrate.Application"
- "ASUS.ArmouryCrate"
- "ArmouryCrate.Control"
```

If COM is available, direct object model access is enabled.

## Error Handling

All API calls return `ArmouryCrateAPIResponse`:

```python
@dataclass
class ArmouryCrateAPIResponse:
    success: bool
    data: Dict[str, Any]
    message: str
    error: Optional[str]
    timestamp: datetime
```

Example:
```python
response = await api.call_api("/devices")
if response.success:
    # Process data
    devices = response.data["devices"]
else:
    # Handle error
    print(f"Error: {response.error}")
```

## Testing

Run the API test script:

```bash
python scripts/python/jarvis_armoury_crate_api_test.py
```

Tests:
1. Device listing
2. Lighting state retrieval
3. AI prediction
4. Device control

## Integration Points

### With Main Integration

The API is tightly integrated with `ArmouryCrateIntegration`:

- Automatic initialization on integration creation
- Shared device registry
- Unified error handling
- Combined capabilities

### With JARVIS Workflows

The API can be used in JARVIS workflows:

```python
# In workflow executor
async def workflow_executor(data):
    api = create_armoury_crate_api()
    response = await api.call_api("/lighting", method="POST", data={
        "action": "set",
        "config": data.get("lighting_config", {})
    })
    return response.data
```

## Future Enhancements

1. **WebSocket Support**
   - Real-time device state updates
   - Event streaming

2. **Advanced AI**
   - Machine learning models
   - Predictive maintenance
   - User preference learning

3. **Official API Support**
   - If ASUS releases official API
   - Direct SDK integration

4. **Multi-Device Coordination**
   - Synchronized lighting
   - Device group management

---

**"This is the way." - MANDO**
