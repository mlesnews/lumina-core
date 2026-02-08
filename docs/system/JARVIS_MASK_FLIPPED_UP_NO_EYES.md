# JARVIS Mask Flipped Up - No Eyes Mode

**Status:** 📋 **DESIGN SPECIFICATION**
**Date:** 2026-01-08

---

## Current Implementation

### When Faceplate is Open (`faceplate_open = True`)

**Current Design:**
1. **Faceplate moves up** (offset: -45*s)
2. **Dark face area** - Dark oval (#0a0a0a) visible inside
3. **Scanning data lines** - Horizontal dashed lines (Android App style)
4. **JARVIS glowing eye** - Central glowing eye (cyan/blue) - **THIS SHOULD BE REMOVED**

---

## Requested Design: "Mask Flipped Up with No Eyes"

### Visual Description

**What it should look like:**

1. **Helmet Structure:**
   - Iron Man helmet with faceplate/visor **flipped up and retracted**
   - Faceplate slides up above the helmet (visible above head)
   - Helmet remains on head (sides and top visible)

2. **Inside the Helmet (Face Area):**
   - **Dark interior** - Very dark (#0a0a0a or black)
   - **No eyes visible** - Empty/dark space where eyes would be
   - **No glowing elements** - No JARVIS eye, no HUD elements
   - **Minimal detail** - Just the dark interior of the helmet

3. **Optional Elements (if any):**
   - **Scanning lines** - Subtle horizontal data lines (optional, very dim)
   - **No central eye** - The glowing JARVIS eye should NOT be present
   - **Clean, empty look** - Just the dark helmet interior

---

## Visual Reference

### Iron Man Helmet Reference
- **Mask Up:** Like when Tony Stark flips up his faceplate
- **No Eyes:** The interior is dark/empty - no glowing eyes visible
- **Helmet Visible:** The helmet structure (sides, top) remains visible
- **Faceplate Above:** The faceplate is visible above the helmet

### Current Code Location

**File:** `scripts/python/jarvis_ironman_bobblehead_gui.py`

**Lines 217-235:** Faceplate open drawing code

**Current Code:**
```python
if self.faceplate_open:
    # High-tech HUD inside
    self.canvas.create_oval(...)  # Dark face area
    # Scanning data lines
    for i in range(-4, 5):
        self.canvas.create_line(...)  # Horizontal lines
    # JARVIS glowing eye  <-- THIS SHOULD BE REMOVED
    self.canvas.create_oval(
        cx-8*s, cy-8*s, cx+8*s, cy+8*s,
        fill=p["primary"], outline="white", tags="helmet"
    )
```

---

## Recommended Changes

### Remove the Glowing Eye

**Change:**
- Remove or comment out the JARVIS glowing eye (lines 232-235)
- Keep the dark face area
- Keep or make scanning lines optional/subtle
- Result: Dark, empty helmet interior with no eyes

### Alternative: Make Eyes Optional

**Option:**
- Add a configuration flag: `show_eyes_when_open = False`
- Only show the glowing eye if flag is True
- Default to False (no eyes when mask is up)

---

## Visual Comparison

### Current (With Eyes):
```
    [Faceplate Up]
    ┌─────────────┐
    │  [Glowing]  │  ← JARVIS eye visible
    │     Eye     │
    │  [Scanning] │  ← Data lines
    │    Lines    │
    └─────────────┘
    [Helmet Sides]
```

### Requested (No Eyes):
```
    [Faceplate Up]
    ┌─────────────┐
    │             │  ← Empty/dark
    │   [Dark]    │  ← No eyes
    │  Interior   │  ← Just darkness
    │             │
    └─────────────┘
    [Helmet Sides]
```

---

## Implementation

### Code Change Needed

**File:** `scripts/python/jarvis_ironman_bobblehead_gui.py`

**Remove or conditionally disable:**
```python
# JARVIS glowing eye
self.canvas.create_oval(
    cx-8*s, cy-8*s, cx+8*s, cy+8*s,
    fill=p["primary"], outline="white", tags="helmet"
)
```

**Result:** When mask is flipped up, only dark interior is visible - no glowing eyes.

---

## Status

📋 **Design Specification:** COMPLETE
🔧 **Implementation:** PENDING (needs code change)

---

## Tags

#JARVIS #MASK #HELMET #FACEPLATE #NO_EYES #DESIGN @JARVIS @LUMINA

---

**Created:** 2026-01-08T23:32:00
**Status:** 📋 **DESIGN SPECIFICATION - MASK UP, NO EYES**
