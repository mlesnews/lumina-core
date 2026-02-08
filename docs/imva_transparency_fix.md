# IMVA Transparency & Flickering Fix

## Issues Fixed

### 1. **Flickering**
**Problem**: IMVA was flickering during animation
**Root Cause**: 
- Multiple `update()` calls causing excessive redraws
- Transparency being re-set during each redraw
- Geometry updates happening even when position didn't change

**Fixes Applied**:
- ✅ Added `transparency_set` flag to prevent re-setting transparency during redraw
- ✅ Changed `update()` to `update_idletasks()` in animation loops (less aggressive)
- ✅ Only update window geometry when position actually changes
- ✅ Removed duplicate transparency setting code from `_draw_ironman()`

### 2. **Transparency (More Transparent Than ACVA)**
**Problem**: IMVA was more transparent than ACVA
**Root Cause**: 
- Using `LWA_COLORKEY` only with alpha value 0 (fully transparent)
- Not using alpha blending to control opacity

**Fixes Applied**:
- ✅ Changed from `LWA_COLORKEY` only to `LWA_BOTH` (LWA_COLORKEY | LWA_ALPHA)
- ✅ Set alpha value to 255 (fully opaque) to match ACVA opacity
- ✅ Combined color key transparency (black pixels) with alpha blending
- ✅ Transparency now matches ACVA's opacity level

## Code Changes

### Transparency Setting (lines 715-733)
```python
# OLD: Only color key, alpha = 0 (too transparent)
LWA_COLORKEY = 0x1
result = ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0x000000, 0, LWA_COLORKEY)

# NEW: Both color key and alpha, alpha = 255 (matches ACVA)
LWA_COLORKEY = 0x1
LWA_ALPHA = 0x2
LWA_BOTH = LWA_COLORKEY | LWA_ALPHA
alpha_value = 255  # Fully opaque (matching ACVA)
result = ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0x000000, alpha_value, LWA_BOTH)
```

### Flickering Prevention
- Added `self.transparency_set = False` in `__init__`
- Set flag to `True` after transparency is applied
- Removed transparency re-setting from `_draw_ironman()`
- Changed `update()` to `update_idletasks()` in animation loops
- Only update geometry when position changes

## Result

- ✅ No more flickering
- ✅ Opacity matches ACVA (not more transparent)
- ✅ Smooth animation
- ✅ Better performance (fewer unnecessary updates)
