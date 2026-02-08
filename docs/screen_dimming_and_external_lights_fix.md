# Screen Dimming & External Lights Fix

## 5W1H Analysis

### WHO (Causes)
- **Automation rules** in Armoury Crate with `screen_brightness` triggers
- **Windows power management** auto-adjusting brightness
- **Armoury Crate automation system** checking triggers periodically

### WHAT (Problems)
- **Screen randomly dimming and brightening** - Very distracting!
- **External laptop lights ON** - Disturbing wife's sleep
- **Keyboard and screen should remain functional** - Only external lights need to be OFF

### WHEN (Timing)
- **Randomly** - When automation rules check triggers
- **During system state changes** - Power management may interfere
- **Periodic trigger checks** - Automation system evaluates rules

### WHERE (Location)
- **Armoury Crate automation rules**: `data/armoury_crate/automation/rules.json`
- **Windows registry**: `HKCU\SOFTWARE\ASUS\ArmouryDevice`
- **Armoury Crate service processes**: Running in background

### WHY (Root Causes)
1. **Automation rules with `screen_brightness` trigger type**
   - Rules check screen brightness periodically
   - When brightness threshold is met, rule triggers
   - Rule applies profile/action (may change brightness again)
   - **This creates a feedback loop causing random dimming/brightening**

2. **External lights not specifically disabled**
   - `disable_all_lighting` disables all lighting
   - But external lights (VUE, monitor lights) may not be properly targeted
   - Need to ensure external lights are explicitly OFF

3. **Windows power management**
   - May be auto-adjusting brightness based on ambient light
   - Can interfere with manual brightness settings

### HOW (Mechanism)
1. **Screen Brightness Trigger Loop**:
   ```
   Automation Rule checks brightness
   → Brightness threshold met
   → Rule triggers and applies profile
   → Profile changes brightness
   → Rule checks again (new brightness)
   → Loop continues (random dimming/brightening)
   ```

2. **External Lights**:
   - External lights controlled via Armoury Crate
   - Need to explicitly disable VUE lighting zones
   - Keyboard and screen should remain functional

## Fixes Applied

### 1. Screen Brightness Trigger Disabled

**Location**: `src/cfservices/services/jarvis_core/integrations/armoury_crate.py`

**Change**: Disabled `screen_brightness` trigger type to prevent feedback loops:

```python
elif rule.trigger_type == "screen_brightness":
    # Screen brightness trigger - DISABLED to prevent dimming cycles
    # This trigger type causes feedback loops where brightness changes trigger
    # rules that change brightness again, causing random dimming/brightening
    # Skip this trigger type to prevent the issue
    self.logger.debug(f"Skipping screen_brightness trigger '{rule.name}' to prevent dimming cycles")
    should_trigger = False
```

**Result**: Screen brightness triggers are now skipped, preventing the feedback loop.

### 2. External Lights Fix

**Script**: `scripts/python/jarvis_fix_screen_dimming_and_external_lights.py`

**Actions**:
- Checks for problematic automation rules
- Disables/deletes `screen_brightness` trigger rules
- Disables all external lighting (preserves keyboard control)

### 3. Automation Rules Cleanup

The fix script:
- Lists all automation rules
- Identifies problematic rules (screen_brightness triggers)
- Deletes or disables problematic rules
- Prevents future trigger loops

## Usage

### Run Comprehensive Fix

```bash
python scripts/python/jarvis_fix_screen_dimming_and_external_lights.py
```

This will:
1. Perform 5W1H analysis
2. Check automation rules
3. Fix screen dimming (disable problematic triggers)
4. Fix external lights (disable all except keyboard/screen)

### Manual Fix Steps

If automated fix doesn't work:

1. **Disable Screen Brightness Triggers**:
   ```python
   from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration
   
   integration = create_armoury_crate_integration()
   
   # List rules
   rules = await integration.process_request({"action": "list_automation_rules"})
   
   # Delete screen_brightness trigger rules
   for rule in rules.get("rules", []):
       if rule.get("trigger_type") == "screen_brightness":
           await integration.process_request({
               "action": "delete_automation_rule",
               "rule_name": rule.get("name")
           })
   ```

2. **Disable External Lights**:
   ```python
   # Disable all lighting (preserves keyboard)
   result = await integration.process_request({
       "action": "disable_all_lighting"
   })
   ```

3. **Check Windows Power Settings**:
   - Open Windows Settings → System → Power & Sleep
   - Disable "Change brightness automatically when lighting changes"
   - Set brightness manually to desired level

## Prevention

### 1. Don't Create Screen Brightness Triggers

Avoid creating automation rules with `screen_brightness` trigger type:

```python
# ❌ DON'T DO THIS (causes feedback loops)
await integration.process_request({
    "action": "create_automation_rule",
    "name": "bad_rule",
    "trigger_type": "screen_brightness",  # BAD!
    "trigger_config": {"brightness": 50}
})

# ✅ USE TIME-BASED TRIGGERS INSTEAD
await integration.process_request({
    "action": "create_automation_rule",
    "name": "good_rule",
    "trigger_type": "time",  # GOOD!
    "trigger_config": {"time": "22:00"}
})
```

### 2. Monitor Automation Rules

Regularly check for problematic rules:

```python
rules = await integration.process_request({"action": "list_automation_rules"})
for rule in rules.get("rules", []):
    if rule.get("trigger_type") == "screen_brightness":
        print(f"⚠️  Problematic rule found: {rule.get('name')}")
```

## Verification

After applying fixes:

1. **Screen Dimming**:
   - Monitor screen brightness for 10-15 minutes
   - Should remain stable (no random changes)
   - If still dimming, check Windows power settings

2. **External Lights**:
   - Check VUE lighting zones (should be OFF)
   - Check monitor lights (should be OFF)
   - Keyboard backlight should still work
   - Screen should still work

## Troubleshooting

### Screen Still Dimming

1. **Check Windows Power Settings**:
   - Disable auto-brightness
   - Disable adaptive brightness
   - Set manual brightness level

2. **Check Other Software**:
   - Other automation software may be interfering
   - Check for brightness control apps
   - Check for power management software

3. **Check Automation Rules**:
   - Verify no `screen_brightness` triggers exist
   - Check for time-based rules that change brightness

### External Lights Still ON

1. **Manual Disable**:
   - Open Armoury Crate app
   - Manually disable VUE lighting zones
   - Save profile

2. **Registry Check**:
   - Check registry brightness values
   - Ensure all lighting brightness = 0
   - Keep Enable flags = 1 (for keyboard control)

3. **Service Restart**:
   - Restart Armoury Crate services
   - Restart lighting services
   - Reapply disable_all_lighting

## Summary

✅ **Screen Brightness Triggers Disabled** - Prevents feedback loops
✅ **External Lights Fix Available** - Comprehensive fix script
✅ **Automation Rules Cleanup** - Removes problematic rules
✅ **Prevention Measures** - Guidelines to avoid future issues

**"This is the way." - MANDO**
