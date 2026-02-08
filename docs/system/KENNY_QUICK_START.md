# Kenny Quick Start Guide

**Quick Start:** Get Kenny and Ace visible on your desktop NOW

---

## 🚀 Fastest Way to Start

### Option 1: Start Both VAs (Recommended)
```powershell
python scripts/python/start_animated_vas_wandering.py
```

This starts:
- ✅ Kenny (IMVA) - Iron Man Virtual Assistant
- ✅ Ace (ACVA) - Armoury Crate Virtual Assistant (if running)

### Option 2: Start Just Kenny
```powershell
python scripts/python/start_kenny_visible.py
```

### Option 3: Ensure VAs Are Visible
```powershell
python scripts/python/ensure_vas_visible.py
```

---

## 👀 What to Look For

### Kenny (IMVA):
- **Appearance:** Red circle (Hot Rod Red) with hexagonal helmet
- **Size:** 120x120px window
- **Location:** Should appear on desktop, wandering around borders
- **Movement:** Slow, steady, casual (stoic movement)

### Ace (ACVA):
- **Appearance:** Armoury Crate Virtual Assistant (if Armoury Crate is running)
- **Location:** Desktop (managed by Armoury Crate)
- **Movement:** Casual, confident (stoic)

---

## 🔍 If You Don't See Them

### Check 1: Are They Running?
- Open Task Manager
- Look for Python processes
- Check if `kenny_imva_enhanced.py` is running

### Check 2: Window Position
- Windows might be off-screen
- Try: `python scripts/python/ensure_vas_visible.py`
- This will attempt to recover window positions

### Check 3: Window Size
- Kenny should be 120x120px
- If too small, might be hard to see
- Check desktop corners and edges

### Check 4: Transparency
- Windows might be transparent
- Look for red/orange circles on desktop
- Check if windows are minimized

---

## 🎯 Troubleshooting

### Kenny Not Visible:
1. Run: `python scripts/python/start_kenny_visible.py`
2. Check logs for errors
3. Verify tkinter is installed: `python -c "import tkinter"`
4. Check window position (might be off-screen)

### Ace Not Visible:
1. Make sure Armoury Crate is running
2. Check if ACVA is enabled in Armoury Crate settings
3. Run: `python scripts/python/start_animated_vas_wandering.py`
4. Check if Ace window is found

### Both Not Visible:
1. Run: `python scripts/python/ensure_vas_visible.py`
2. Check Task Manager for Python processes
3. Look for error messages in terminal
4. Verify all dependencies are installed

---

## 📋 Startup Commands Summary

| Command | Purpose |
|---------|---------|
| `start_animated_vas_wandering.py` | Start both Kenny and Ace |
| `start_kenny_visible.py` | Start just Kenny |
| `ensure_vas_visible.py` | Ensure VAs are visible (recovery) |
| `kenny_imva_enhanced.py` | Direct Kenny startup |

---

## ✅ Success Indicators

### Kenny Running:
- ✅ Red circle with hexagonal helmet visible
- ✅ Wandering around desktop borders
- ✅ Slow, steady movement (stoic)
- ✅ Window size: 120x120px

### Ace Running:
- ✅ Armoury Crate VA visible (if Armoury Crate running)
- ✅ Integration active
- ✅ Position updates working

---

**Tags:** #KENNY #ACE #QUICK_START #VISIBILITY @JARVIS @LUMINA
