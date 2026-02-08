# Screen Brightness Dimming Fix

## Issue
The PC screen was repeatedly dimming and undimming within short time moments, causing distraction.

## Root Cause
The `disable_all_lighting` function was setting screen brightness to 0 (dimming the screen) in STEP 5. If this function was being called repeatedly (by scheduled tasks, automation rules, or manual execution), it would cause a dim/undim cycle.

## Solution
**Disabled screen brightness control in the `disable_all_lighting` function** to prevent distracting dim/undim cycles.

### Changes Made

1. **`src/cfservices/services/jarvis_core/integrations/armoury_crate.py`**:
   - Modified STEP 5 to skip screen brightness setting
   - Added comment explaining why it's disabled
   - Updated summary to reflect that screen brightness is disabled

2. **`scripts/python/jarvis_disable_all_lighting.py`**:
   - Updated output message to indicate screen brightness is skipped

## Impact
- ✅ Screen will no longer dim when disabling lighting
- ✅ No more distracting dim/undim cycles
- ✅ Lighting control still works (only screen brightness is disabled)
- ✅ Keyboard shortcut (fn+F4) still preserved

## Alternative
If screen brightness control is needed, use the dedicated `set_screen_brightness` action instead of the `disable_all_lighting` function.

## Tags
`@JARVIS` `#FIX` `#SCREEN` `#BRIGHTNESS` `#DISTRACTION`
