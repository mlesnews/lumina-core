# LOCKS BEFORE LIGHTS - Critical Priority Rule

## The Rule

**🔓 LOCKS BEFORE LIGHTS!**

**ALWAYS fix keyboard locks BEFORE attempting to fix lighting issues.**

## Why This Matters

### The Infinite Loop Problem

Without fixing locks first:

1. **Locks are stuck** → Function keys don't work
2. **Can't use fn+F4** → Can't control lighting
3. **Stuck in degraded state** → Complete loss of @ff (function keys)
4. **Infinite loop** → Can't fix locks without function keys, can't fix lighting without locks

### The Solution

**Fix locks FIRST, then lighting:**

1. ✅ **Fix locks** → Function keys work
2. ✅ **Use fn+F4** → Can control lighting
3. ✅ **System functional** → No infinite loop

## Implementation

### In `disable_all_lighting`

**STEP 0 (NEW)**: Fix locks FIRST
```python
# STEP 0: FIX LOCKS FIRST (CRITICAL - LOCKS BEFORE LIGHTS!)
locks_result = await self._toggle_all_locks()
```

**Then proceed with lighting fix:**
- STEP 1: Troubleshoot
- STEP 2: Repair keyboard control
- STEP 3: Simulate fn+F4 (now works because locks are fixed!)
- STEP 4: UI automation (fallback)
- STEP 5: Registry method (fallback)

### In Priority Fix Script

**Order enforced:**
1. Fix locks FIRST
2. Verify function keys work
3. Then fix lighting
4. Then kill ambient lighting

## Code Locations

### Main Integration
- `src/cfservices/services/jarvis_core/integrations/armoury_crate.py`
  - `_handle_disable_all_lighting()` - Now fixes locks FIRST

### Priority Fix Script
- `scripts/python/jarvis_priority_lock_fix_then_lighting.py`
  - Enforces correct order
  - Prevents infinite loop

## Verification

After fixing locks, verify:
- FN Lock: OFF
- Num Lock: OFF
- Caps Lock: OFF
- Scroll Lock: OFF
- Function keys work (fn+F4 test)

## Error Prevention

If locks aren't fixed first:
- ⚠️ Function keys won't work
- ⚠️ fn+F4 won't work
- ⚠️ Lighting can't be controlled
- ⚠️ System stuck in degraded state

## Success Criteria

✅ **Locks fixed** → All locks OFF
✅ **Function keys work** → fn+F4 works
✅ **Lighting fixed** → Using fn+F4
✅ **No infinite loop** → System functional

---

**"LOCKS BEFORE LIGHTS!" - This is the way. - MANDO**
