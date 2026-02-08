# Locks Before Lighting - Order of Precedence Fix

## Problem

Even after Windows recycle (reboot), lighting effects don't sync with system state because we were applying lighting settings BEFORE fixing keyboard locks.

## Root Cause

**Order of Precedence Issue:**
- Lighting control (fn+F4) requires locks to be fixed FIRST
- If locks are not fixed, fn+F4 won't work
- Without fn+F4, lighting control fails
- System gets stuck in degraded state

## Solution

**LOCKS BEFORE LIGHTING** - Fixed the order of operations:

1. **STEP 0 (CRITICAL): Fix locks FIRST**
   - Run GOD LOOP to fix all keyboard locks
   - Ensures fn+F4 will work
   - Critical blocker - if this fails, lighting will fail

2. **STEP 1: Re-enable services**
   - Enable ArmouryCrateService, LightingService
   - Required for lighting control

3. **STEP 2: Disable display/keyboard lighting**
   - Keep display/keyboard lighting disabled
   - External lighting stays enabled

4. **STEP 3: Apply day/night settings**
   - Set screen brightness
   - Set external lighting brightness
   - Sync with day/night cycles

## Implementation

Updated `jarvis_smart_lighting_day_night_sync.py`:

```python
def fix_locks_first(self) -> Dict[str, Any]:
    """STEP 0 (CRITICAL): Fix locks BEFORE lighting operations"""
    # Uses GOD LOOP to fix all locks first
    # Ensures fn+F4 works before attempting lighting control
```

**New flow in `setup_smart_lighting()`:**
1. Fix locks FIRST (STEP 0)
2. Re-enable services (STEP 1)
3. Disable display/keyboard lighting (STEP 2)
4. Apply day/night settings (STEP 3)

## Benefits

1. **Prevents Infinite Loop**: Locks fixed first, so fn+F4 works
2. **Reliable Lighting Control**: Lighting operations succeed because locks are fixed
3. **Post-Reboot Recovery**: Works after Windows recycle because locks are fixed first
4. **System State Sync**: Lighting syncs with system state because locks are correct

## Files Updated

- `scripts/python/jarvis_smart_lighting_day_night_sync.py`
  - Added `fix_locks_first()` method
  - Updated `setup_smart_lighting()` to call locks fix FIRST
  - Added locks result to summary

## Related Files

- `scripts/python/jarvis_priority_lock_fix_then_lighting.py` - Priority fix order system
- `scripts/python/jarvis_god_loop_lock_repair.py` - GOD LOOP lock repair system
- `scripts/python/jarvis_continuous_day_night_monitor.py` - Continuous monitor (uses setup_smart_lighting)

## Usage

The smart lighting system now automatically fixes locks FIRST:

```python
from scripts.python.jarvis_smart_lighting_day_night_sync import SmartLightingDayNightSync

sync = SmartLightingDayNightSync(project_root)
result = sync.setup_smart_lighting()  # Automatically fixes locks FIRST
```

## Testing

After Windows recycle (reboot):
1. Run smart lighting setup
2. Locks are fixed FIRST (STEP 0)
3. Lighting settings are applied AFTER locks are fixed
4. Lighting should now sync correctly with system state

## Notes

- This fix addresses the "LOCKS BEFORE LIGHTING" logic requirement
- Ensures lighting control works after reboot
- Prevents infinite loop of disrepair
- Maintains proper order of operations
