# Cursor IDE Footer Management

**Date:** 2026-01-09  
**Issue:** Footer bar is cluttered, not all items fit  
**Tags:** #JARVIS @LUMINA #CURSOR #FOOTER #UI

---

## Problem

The Cursor IDE footer/status bar is a "hot mess" - not all items fit on the same footer bar, causing:
- Items overflow or get cut off
- Important information hidden
- Cluttered appearance
- Poor user experience

---

## Solutions

### Option 1: Two Footer Bars

**If Cursor supports secondary status bar:**
- Split items across two bars
- Bar 1: Critical/High priority items
- Bar 2: Medium/Low priority items
- Or: Editor items on bar 1, System items on bar 2

**Pros:**
- All items visible
- Clear separation
- No information loss

**Cons:**
- Requires Cursor to support secondary status bar
- Takes more vertical space

### Option 2: Priority-Based Visibility (Recommended)

**Show only important items, hide others:**
- **Always Show:** Critical items (Cursor Model, Git Branch, Errors, Warnings)
- **Show When Space:** High priority items (Language, Encoding, Line Endings)
- **Hide by Default:** Medium/Low priority items (Cursor Position, Selection, File Size)
- **Expand on Hover/Click:** Show hidden items when needed

**Pros:**
- Clean, uncluttered footer
- Important info always visible
- Access to all items when needed
- Works with single footer bar

**Cons:**
- Some items hidden by default
- Requires interaction to see all

### Option 3: Grouping & Collapsing

**Group related items:**
- Editor group (Language, Encoding, Line Endings, Cursor Position)
- Git group (Branch, Changes, Status)
- Problems group (Errors, Warnings, Info)
- AI group (Cursor Model, AI Status)

**Collapse groups when not needed**

**Pros:**
- Organized appearance
- Related items together
- Can collapse entire groups

**Cons:**
- More complex UI
- May require custom extension

### Option 4: Rotating/Cycling Display

**Cycle through items:**
- Show most important items
- Rotate through less important items
- Time-based or event-based rotation

**Pros:**
- All items eventually visible
- Keeps footer clean

**Cons:**
- Items not always visible
- May miss information

---

## Recommended Solution

**Priority-Based Visibility** (Option 2)

**Why:**
- Works with current Cursor IDE
- Clean, professional appearance
- Important info always visible
- Access to all items when needed
- No extension required

**Implementation:**
1. Configure items by priority
2. Show Critical + High priority items (typically 7-8 items)
3. Hide Medium/Low priority items
4. Add hover/click to expand and show hidden items
5. Group related items together

---

## Configuration

### Priority Levels

1. **CRITICAL** - Always show
   - Cursor Model
   - Git Branch
   - Errors
   - Warnings

2. **HIGH** - Show when space available
   - Language
   - Encoding
   - Line Endings

3. **MEDIUM** - Show when space available, hide if crowded
   - Cursor Position
   - Selection
   - Indent Size

4. **LOW** - Hide by default, show on hover/expand
   - File Size
   - Line Count
   - Spaces/Tabs

5. **HIDDEN** - Always hidden
   - Debug items
   - Development tools

---

## Usage

### Get Suggestion

```bash
python scripts/python/jarvis_cursor_footer_manager.py --suggest
```

### View Single Bar Layout

```bash
python scripts/python/jarvis_cursor_footer_manager.py --layout
```

### View Two Bar Layout

```bash
python scripts/python/jarvis_cursor_footer_manager.py --two-bars
```

---

## Current Configuration

**Total Items:** 10
- **Critical:** 4 (Cursor Model, Git Branch, Errors, Warnings)
- **High:** 3 (Language, Encoding, Line Endings)
- **Medium:** 3 (Cursor Position, Selection, Indent Size)
- **Low:** 0

**Recommendation:** Use priority-based visibility
- Show: Critical + High (7 items) - fits comfortably
- Hide: Medium items (3 items) - show on expand

---

## Cursor IDE Settings

To implement in Cursor IDE:

1. **Open Settings:** `Ctrl+,` (or `Cmd+,` on Mac)
2. **Search:** "status bar"
3. **Configure:**
   - Enable/disable specific status bar items
   - Set visibility preferences
   - Configure item order

**Settings to check:
- `workbench.statusBar.visible` - Show/hide status bar
- `workbench.statusBar.feedback.visible` - Show/hide feedback
- Individual item settings (search for specific items)

---

## Future Enhancements

1. **Custom Footer Extension**
   - Create Cursor extension for advanced footer management
   - Drag-and-drop item ordering
   - Custom grouping
   - Collapsible sections

2. **Smart Hiding**
   - Auto-hide items when not relevant
   - Show items based on context
   - Learn from usage patterns

3. **Two Bar Support**
   - If Cursor adds secondary status bar support
   - Automatic split configuration
   - Balanced item distribution

---

## Summary

**Problem:** Footer bar cluttered, items don't fit  
**Solution:** Priority-based visibility (recommended) or Two footer bars  
**Result:** Clean footer with important info always visible, all items accessible when needed

**The footer manager will help organize and prioritize footer items!** 📊

---

**Tags:** #JARVIS @LUMINA #CURSOR #FOOTER #UI #STATUSBAR
