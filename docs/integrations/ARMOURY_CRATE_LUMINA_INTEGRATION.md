# Armoury Crate Lumina Integration

**Status**: ✅ ACTIVE  
**Version**: 2.0.0  
**Date**: 2025-01-24

## Overview

Full manual control and automation integration for ASUS Armoury Crate within the Lumina ecosystem. This integration provides complete control over VUE lighting effects, keyboard backlight, screen brightness, and all Armoury Crate settings through Lumina's unified interface. Includes automation with profiles, scheduled rules, and event-based triggers.

## Features

- ✅ **Manual Control Interface** - Full manual control over all Armoury Crate settings
- ✅ **VUE Lighting Control** - Disable/enable VUE lighting effects
- ✅ **Screen Brightness Control** - Adjust screen brightness programmatically
- ✅ **Service Management** - Control RGB lighting services
- ✅ **Status Monitoring** - Get comprehensive status of all lighting zones
- ✅ **Manual Control Guide** - Step-by-step instructions for manual configuration
- ✅ **Lighting Profiles** - Pre-configured lighting settings (sleep, work, gaming, night)
- ✅ **Automation Rules** - Time-based and event-based automation
- ✅ **Scheduled Automation** - Automatic profile switching
- ✅ **Profile Management** - Create, list, apply, and delete profiles

## Quick Start

### Using the Command Line Interface

```bash
python scripts/python/lumina_armoury_crate_control.py
```

### Using Python API

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import (
    create_armoury_crate_integration
)
import asyncio

async def control_armoury():
    integration = create_armoury_crate_integration()
    
    # Open Armoury Crate app
    result = await integration.process_request({"action": "open_app"})
    print(result)
    
    # Disable VUE lighting
    result = await integration.process_request({"action": "disable_vue_lighting"})
    print(result)
    
    # Apply sleep profile (complete blackout)
    result = await integration.process_request({
        "action": "apply_profile",
        "profile_name": "sleep"
    })
    print(result)
    
    # Set screen brightness to 0
    result = await integration.process_request({
        "action": "set_screen_brightness",
        "brightness": 0
    })
    print(result)

asyncio.run(control_armoury())
```

## Available Actions

### 1. Open Armoury Crate App
Opens the Armoury Crate application for manual configuration.

```python
result = await integration.process_request({"action": "open_app"})
```

### 2. Disable VUE Lighting
Completely disables all VUE lighting effects:
- Stops ROGLiveService
- Sets screen brightness to 0
- Opens Armoury Crate for final manual configuration

```python
result = await integration.process_request({"action": "disable_vue_lighting"})
```

### 3. Get Lighting Status
Gets current status of lighting services and screen brightness.

```python
result = await integration.process_request({"action": "get_lighting_status"})
```

### 4. Stop Lighting Service
Stops the ROGLiveService (RGB lighting service).

```python
result = await integration.process_request({"action": "stop_lighting_service"})
```

### 5. Set Screen Brightness
Sets screen brightness (0-100).

```python
result = await integration.process_request({
    "action": "set_screen_brightness",
    "brightness": 0  # 0-100
})
```

### 6. Get Full Status
Gets comprehensive status of all systems.

```python
result = await integration.process_request({"action": "get_status"})
```

### 7. Manual Control Guide
Gets step-by-step manual control instructions.

```python
result = await integration.process_request({"action": "manual_control_guide"})
```

### 8. Apply Profile
Apply a lighting profile (sleep, work, gaming, night, or custom).

```python
result = await integration.process_request({
    "action": "apply_profile",
    "profile_name": "sleep"
})
```

### 9. Create Automation Rule
Create an automation rule for automatic profile switching.

```python
result = await integration.process_request({
    "action": "create_automation_rule",
    "name": "auto_sleep_10pm",
    "trigger_type": "time",
    "trigger_config": {"time": "22:00"},
    "profile_name": "sleep"
})
```

### 10. Run Automation
Check triggers and apply profiles automatically.

```python
result = await integration.process_request({"action": "run_automation"})
```

See [ARMOURY_CRATE_AUTOMATION.md](./ARMOURY_CRATE_AUTOMATION.md) for complete automation documentation.

## Manual Configuration Steps

When you need to manually configure Armoury Crate:

1. **Open Armoury Crate** (use `open_app` action or manually)
2. Click on **"Device"** tab (left sidebar)
3. Select your laptop model
4. Click on **"Lighting"** or **"Aura Sync"** section
5. For each lighting zone (Keyboard, Logo, etc.):
   - Set effect to **"Off"** OR
   - Set effect to **"Static"** with brightness **0**
6. Click **"Apply"** or **"Save"** to confirm changes

**Alternative**: Use keyboard shortcut **Fn + F3** or **Fn + F4** to cycle keyboard backlight until it's OFF.

## Integration with Lumina

The Armoury Crate integration follows Lumina's integration patterns:

- Implements `AgentInterface` protocol
- Registered with Jarvis Core
- Accessible through Lumina's unified command interface
- Full manual control support (Manus control)

## Architecture

```
┌─────────────────────────────────────┐
│      Lumina Ecosystem               │
│  ┌───────────────────────────────┐ │
│  │   Jarvis Core                 │ │
│  │  ┌──────────────────────────┐ │ │
│  │  │ ArmouryCrateIntegration  │ │ │
│  │  │  • Manual Control        │ │ │
│  │  │  • Service Management    │ │ │
│  │  │  • Lighting Control      │ │ │
│  │  └──────────────────────────┘ │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│   ASUS Armoury Crate                │
│   • VUE Lighting                    │
│   • Keyboard Backlight              │
│   • System Settings                 │
└─────────────────────────────────────┘
```

## Configuration

Configuration is done through the `ArmouryCrateConfig` dataclass:

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import (
    ArmouryCrateConfig,
    ArmouryCrateIntegration
)

config = ArmouryCrateConfig(
    auto_open_app=True,
    enable_manual_control=True,
    default_lighting_state="off",
    save_settings=True
)

integration = ArmouryCrateIntegration(config)
```

## Troubleshooting

### Armoury Crate Not Found
If Armoury Crate executable is not found, the integration will:
1. Try protocol handler (`armourycrate:`)
2. Provide manual steps to open it

### Services Won't Stop
Some services may restart automatically. Use the manual configuration in Armoury Crate to permanently disable lighting.

### Lighting Still Active
After stopping services, you must:
1. Open Armoury Crate
2. Manually disable lighting zones
3. Save settings

## Examples

### Complete Blackout (All Lighting Off)

```python
async def blackout_all_lighting():
    integration = create_armoury_crate_integration()
    
    # 1. Apply sleep profile (complete blackout)
    await integration.process_request({
        "action": "apply_profile",
        "profile_name": "sleep"
    })
    
    # 2. Get status
    status = await integration.process_request({"action": "get_status"})
    print("Blackout complete:", status)
```

### Quick Status Check

```python
async def quick_status():
    integration = create_armoury_crate_integration()
    status = await integration.process_request({"action": "get_status"})
    print(json.dumps(status, indent=2))
```

## Notes

- **Manual Control Required**: Some settings require manual configuration in Armoury Crate app
- **Service Restart**: Services may restart automatically; use Armoury Crate settings for permanent changes
- **Windows Only**: This integration is Windows-specific (ASUS laptops)
- **Admin Rights**: Some operations may require administrator privileges

## Support

For issues or questions:
1. Check the manual control guide (`manual_control_guide` action)
2. Review Armoury Crate app settings
3. Check service status (`get_status` action)

---

**Integration Status**: ✅ Fully Integrated with Lumina  
**Manual Control**: ✅ Full Manus Control Available  
**Automation**: ✅ Full Automation Available  
**Version**: 2.0.0
