# Armoury Crate Automation Guide

**Status**: ✅ ACTIVE  
**Version**: 2.0.0  
**Date**: 2025-01-24

## Overview

The Armoury Crate integration includes full automation capabilities alongside manual control. You can create lighting profiles, set up automation rules, and schedule automatic lighting changes.

## Features

- ✅ **Lighting Profiles** - Pre-configured lighting settings
- ✅ **Automation Rules** - Time-based and event-based automation
- ✅ **Scheduled Automation** - Automatic profile switching
- ✅ **Event Triggers** - Screen brightness, time, and custom triggers
- ✅ **Profile Management** - Create, list, and delete profiles

## Default Profiles

The integration comes with these default profiles:

### 1. **sleep** - Complete Blackout
- Screen brightness: 0%
- Lighting: Off
- Use case: Sleeping, dark room work

### 2. **work** - Work Mode
- Screen brightness: 50%
- Lighting: Off
- Use case: Normal work, daytime

### 3. **gaming** - Gaming Mode
- Screen brightness: 80%
- Lighting: On (50% brightness)
- Use case: Gaming, entertainment

### 4. **night** - Night Mode
- Screen brightness: 10%
- Lighting: Off
- Use case: Late night work, minimal light

## Creating Profiles

### Via Python API

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import (
    create_armoury_crate_integration
)
import asyncio

async def create_custom_profile():
    integration = create_armoury_crate_integration()
    
    result = await integration.process_request({
        "action": "create_profile",
        "name": "my_custom_profile",
        "description": "My custom lighting setup",
        "screen_brightness": 30,
        "lighting_enabled": False,
        "lighting_brightness": 0,
        "effect": "off"
    })
    print(result)

asyncio.run(create_custom_profile())
```

### Via CLI

```bash
python scripts/python/lumina_armoury_crate_control.py
# Select option 10: Create Profile
```

## Applying Profiles

### Via Python API

```python
# Apply sleep profile
result = await integration.process_request({
    "action": "apply_profile",
    "profile_name": "sleep"
})
```

### Via CLI

```bash
# Select option 8: Apply Profile
```

## Automation Rules

### Time-Based Automation

Automatically apply a profile at a specific time:

```python
result = await integration.process_request({
    "action": "create_automation_rule",
    "name": "sleep_at_10pm",
    "trigger_type": "time",
    "trigger_config": {
        "time": "22:00"  # 10:00 PM
    },
    "profile_name": "sleep"
})
```

### Screen Brightness-Based Automation

Apply a profile when screen brightness reaches a certain level:

```python
result = await integration.process_request({
    "action": "create_automation_rule",
    "name": "dim_when_brightness_low",
    "trigger_type": "screen_brightness",
    "trigger_config": {
        "brightness": 0,
        "threshold": 5
    },
    "profile_name": "sleep"
})
```

## Running Automation

### Check Triggers

Check if any automation rules should trigger:

```python
result = await integration.process_request({
    "action": "check_automation_triggers"
})
print(result)
```

### Run Automation

Check triggers and apply profiles automatically:

```python
result = await integration.process_request({
    "action": "run_automation"
})
print(result)
```

## Example: Complete Sleep Automation

```python
async def setup_sleep_automation():
    integration = create_armoury_crate_integration()
    
    # Create automation rule for 10 PM
    await integration.process_request({
        "action": "create_automation_rule",
        "name": "auto_sleep_10pm",
        "trigger_type": "time",
        "trigger_config": {"time": "22:00"},
        "profile_name": "sleep"
    })
    
    # Run automation to check and apply
    result = await integration.process_request({
        "action": "run_automation"
    })
    print("Automation result:", result)

asyncio.run(setup_sleep_automation())
```

## Managing Automation Rules

### List Rules

```python
result = await integration.process_request({
    "action": "list_automation_rules"
})
```

### Enable/Disable Rules

```python
# Enable
await integration.process_request({
    "action": "enable_automation_rule",
    "rule_name": "auto_sleep_10pm"
})

# Disable
await integration.process_request({
    "action": "disable_automation_rule",
    "rule_name": "auto_sleep_10pm"
})
```

### Delete Rules

```python
await integration.process_request({
    "action": "delete_automation_rule",
    "rule_name": "auto_sleep_10pm"
})
```

## Scheduled Automation

To run automation on a schedule, you can:

1. **Use Windows Task Scheduler** - Schedule `run_automation` action
2. **Use Lumina's scheduled tasks** - Add to `config/lumina_scheduled_tasks.json`
3. **Use a background service** - Continuously check triggers

### Example: Scheduled Task

Add to your scheduled tasks:

```json
{
  "name": "armoury_crate_automation",
  "schedule": "*/5 * * * *",
  "action": "run_automation",
  "module": "armoury_crate_integration"
}
```

This runs automation every 5 minutes.

## Automation Best Practices

1. **Use Profiles** - Create reusable profiles instead of one-off settings
2. **Test Rules** - Test automation rules before enabling
3. **Monitor Triggers** - Regularly check if triggers are working
4. **Time-Based Rules** - Use specific times for predictable automation
5. **Event-Based Rules** - Use screen brightness for responsive automation

## Troubleshooting

### Automation Not Running

1. Check if automation is enabled:
   ```python
   capabilities = integration.get_capabilities()
   print(capabilities["automation"])
   ```

2. Check rule status:
   ```python
   rules = await integration.process_request({
       "action": "list_automation_rules"
   })
   # Check if rules are enabled
   ```

3. Manually check triggers:
   ```python
   triggers = await integration.process_request({
       "action": "check_automation_triggers"
   })
   ```

### Profile Not Applying

1. Verify profile exists:
   ```python
   profiles = await integration.process_request({
       "action": "list_profiles"
   })
   ```

2. Check application result:
   ```python
   result = await integration.process_request({
       "action": "apply_profile",
       "profile_name": "sleep"
   })
   print(result)
   ```

## Integration with Lumina Scheduled Tasks

You can integrate automation with Lumina's scheduled task system:

```python
# In your scheduled task configuration
{
  "name": "armoury_crate_night_mode",
  "schedule": "0 22 * * *",  # 10 PM daily
  "action": "apply_profile",
  "module": "armoury_crate_integration",
  "params": {
    "profile_name": "sleep"
  }
}
```

---

**Automation Status**: ✅ FULLY OPERATIONAL  
**Manual Control**: ✅ STILL AVAILABLE  
**Profiles**: ✅ 4 DEFAULT + CUSTOM
