# Kenny Self-Attack Bug - Analysis & Fix

**Date**: 2026-01-04  
**Status**: 🔍 **INVESTIGATING**  
**Tags**: #BUG #KENNY #COLLISION #SELF_ATTACK @LUMINA @JARVIS

---

## The Problem

**User Observation:**
- "Kenny's still attacking himself"
- "When he attacks, his life bar disappears"
- "Hurting himself"
- "I watch his life bar disappear when he attacks"

**Issue**: Kenny appears to be attacking himself instead of Ace, and his "life bar" disappears.

---

## Investigation

### Current System

**Collision Detection:**
- `_check_collisions()` compares `kenny_pos` vs `ace_pos`
- Sends collision warnings when too close
- No attack/damage system exists (combat system is DESIGNED but not IMPLEMENTED)

**No Health/Attack System:**
- Combat system is designed but NOT implemented
- No health bar rendering code exists
- No attack/damage logic exists
- Only collision warnings exist

### Possible Root Causes

1. **Position Tracking Bug**
   - Kenny's position equals Ace's position (same coordinates)
   - Collision detection thinks Kenny is colliding with himself
   - Need to verify: Are positions being updated correctly?

2. **Stale Position Data**
   - Ace's position not updating (old/stale data)
   - Kenny's position compared against stale Ace position
   - Collision detection using wrong data

3. **Visual Bug**
   - User seeing visual glitch that looks like "life bar"
   - No actual health system, but visual appears to show damage
   - Need to verify: What is the user actually seeing?

4. **Missing Validation**
   - No check: `kenny_pos != ace_pos` before collision detection
   - No check: Positions are valid/not identical
   - No check: Positions are from different assistants

---

## The Fix

### 1. Add Position Validation

**Before collision detection:**
- Verify Kenny and Ace positions are not identical
- Verify positions are valid (not None, not zero)
- Verify positions are from different assistants

### 2. Add Debug Logging

**Log collision detection:**
- Log Kenny's position
- Log Ace's position
- Log distance calculation
- Log collision warnings

### 3. Add Identity Check

**Prevent self-collision:**
- Check: `kenny_pos.x != ace_pos.x or kenny_pos.y != ace_pos.y`
- If positions identical, skip collision detection
- Log warning if positions are identical

---

## Implementation

### Code Changes Needed

**File**: `scripts/python/kenny_aces_collaboration.py`

**Method**: `_check_collisions()`

**Add validation:**
```python
def _check_collisions(self):
    """Check for potential collisions between assistants"""
    with self.state_lock:
        if not self.shared_state.kenny_position or not self.shared_state.ace_position:
            return
        
        kenny_pos = self.shared_state.kenny_position
        ace_pos = self.shared_state.ace_position
        
        # VALIDATION: Check positions are not identical (prevent self-collision)
        if kenny_pos.x == ace_pos.x and kenny_pos.y == ace_pos.y:
            logger.warning(f"⚠️  IDENTICAL POSITIONS DETECTED: Kenny and Ace at same location ({kenny_pos.x:.1f}, {kenny_pos.y:.1f})")
            return  # Skip collision detection - positions are identical
        
        # Calculate distance
        distance = ((kenny_pos.x - ace_pos.x) ** 2 + (kenny_pos.y - ace_pos.y) ** 2) ** 0.5
        
        # Log positions for debugging
        logger.debug(f"🔍 Collision check: Kenny=({kenny_pos.x:.1f}, {kenny_pos.y:.1f}), Ace=({ace_pos.x:.1f}, {ace_pos.y:.1f}), distance={distance:.1f}px")
        
        # ... rest of collision detection ...
```

---

## Testing

1. **Start Kenny and Ace**
2. **Monitor collision detection logs**
3. **Verify positions are different**
4. **Verify no self-collision warnings**
5. **Verify collision detection works correctly**

---

## Status

**Investigation**: In progress  
**Fix**: Position validation needed  
**Testing**: Pending

---

**Tags**: #BUG #KENNY #COLLISION #SELF_ATTACK #POSITION_VALIDATION @LUMINA @JARVIS
