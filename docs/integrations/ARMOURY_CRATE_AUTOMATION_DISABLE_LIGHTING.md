# 🤖 JARVIS Automation: Disable All External Lighting

## ✅ FULLY AUTOMATED - NO MANUAL STEPS REQUIRED!

Jarvis can now automatically disable ALL external lighting on your ASUS laptop through complete automation.

---

## 🚀 Quick Start

### **Command Line (Direct)**
```bash
python scripts/python/jarvis_disable_all_lighting.py
```

### **Via Integration API**
```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration
import asyncio

integration = create_armoury_crate_integration()
result = asyncio.run(integration.process_request({
    'action': 'disable_all_lighting'
}))

print(result['message'])  # ✅ ALL external lighting disabled automatically!
```

### **Via Jarvis Core**
```python
# Jarvis can trigger this automatically
await jarvis.process_request({
    'agent': 'armoury_crate',
    'action': 'disable_all_lighting'
})
```

---

## 🔧 What the Automation Does

The automation performs **8 comprehensive steps** automatically:

1. **Stops ALL lighting services** (ROGLiveService, LightingService, AuraService, ArmouryCrateService)
2. **Kills ALL lighting processes** (multiple attempts with different methods)
3. **Disables auto-start** for all lighting services (prevents restart)
4. **Sets screen brightness to 0%** (display off)
5. **Applies sleep profile** (all lighting zones off)
6. **Updates registry settings** (if accessible)
7. **Final aggressive kill attempt** (ensures everything stops)
8. **Verification** (confirms services are stopped)

---

## 📊 Automation Results

When you run the automation, you'll see:

```
🤖 JARVIS AUTOMATION: Disabling ALL External Lighting
======================================================================

AUTOMATION RESULTS:
----------------------------------------------------------------------
✅ Success: True
📢 Message: ✅ ALL external lighting disabled automatically via automation!
🛑 Services Stopped: 4
💀 Processes Killed: 5
✔️  Verification: AllStopped

🎉 ALL EXTERNAL LIGHTING DISABLED AUTOMATICALLY!
======================================================================
```

---

## ⚙️ Automation Features

### **Multiple Stop Methods**
- PowerShell `Stop-Service`
- Process termination
- `sc stop` command
- `taskkill` as final fallback

### **Persistence**
- Disables auto-start for services
- Applies sleep profile (saved settings)
- Registry updates (if accessible)

### **Verification**
- Checks service status after stopping
- Verifies processes are killed
- Reports any remaining services

---

## 🎯 Use Cases

### **1. Sleep Mode Automation**
```python
# Automatically disable lighting when going to sleep
await integration.process_request({
    'action': 'disable_all_lighting'
})
```

### **2. Scheduled Automation**
Create an automation rule:
```python
await integration.process_request({
    'action': 'create_automation_rule',
    'name': 'night_mode',
    'trigger_type': 'time',
    'trigger_config': {'time': '22:00'},
    'profile_name': 'sleep',
    'enabled': True
})
```

### **3. Event-Based Automation**
```python
# Disable lighting when screen brightness goes below threshold
await integration.process_request({
    'action': 'create_automation_rule',
    'name': 'low_brightness_disable',
    'trigger_type': 'screen_brightness',
    'trigger_config': {'threshold': 10},
    'profile_name': 'sleep',
    'enabled': True
})
```

---

## 🔄 Integration with Other Automation

The `disable_all_lighting` action can be combined with other automation:

```python
# Complete sleep automation
async def sleep_mode():
    integration = create_armoury_crate_integration()
    
    # 1. Disable all lighting
    await integration.process_request({'action': 'disable_all_lighting'})
    
    # 2. Set screen brightness to 0
    await integration.process_request({
        'action': 'set_screen_brightness',
        'brightness': 0
    })
    
    # 3. Apply sleep profile
    await integration.process_request({
        'action': 'apply_profile',
        'profile_name': 'sleep'
    })
```

---

## ⚠️ Notes

- **Services may restart**: Some services are managed by Windows and may restart. The automation disables auto-start to prevent this.
- **Hardware control**: Some lighting zones are hardware-controlled and may require Armoury Crate UI for initial setup. Once disabled via automation, they should stay off.
- **Verification**: The automation verifies services are stopped, but some may restart if Windows requires them.

---

## 🎮 Available Actions

| Action | Description | Automated |
|--------|-------------|-----------|
| `disable_all_lighting` | **Disable ALL external lighting** | ✅ Yes |
| `disable_vue_lighting` | Disable VUE lighting (redirects to disable_all_lighting) | ✅ Yes |
| `stop_lighting_service` | Stop RGB lighting service | ✅ Yes |
| `set_screen_brightness` | Set screen brightness (0-100) | ✅ Yes |
| `apply_profile` | Apply lighting profile | ✅ Yes |

---

## 📝 Example: Full Automation Script

```python
#!/usr/bin/env python3
"""Complete lighting automation"""

import asyncio
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration

async def main():
    integration = create_armoury_crate_integration()
    
    # Disable all lighting
    result = await integration.process_request({
        'action': 'disable_all_lighting'
    })
    
    if result['success']:
        print("✅ All lighting disabled!")
        print(f"   Services stopped: {result['services_stopped']}")
        print(f"   Processes killed: {result['processes_killed']}")
    else:
        print("⚠️ Some services may still be running")
        print(f"   Verification: {result['verification']}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🎉 Success!

**Jarvis automation is now fully operational!** All external lighting can be disabled automatically without any manual steps.

Use `disable_all_lighting` action for complete automation! 🤖
