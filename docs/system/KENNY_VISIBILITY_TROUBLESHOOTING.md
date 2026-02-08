# Kenny Visibility Troubleshooting Guide

**Issue:** Kenny window not visible on desktop

---

## 🔍 Current Status

**Diagnostics Show:**
- ✅ tkinter available (Kenny can run)
- ✅ Ace found and visible (HWND 132026, position 82, 909)
- ❌ Kenny window not found (no 120x120 window detected)

**Possible Issues:**
1. Window is off-screen (at -32000, -32000 or similar)
2. Window is minimized
3. Window is behind other windows
4. Window creation is failing silently
5. Window size is wrong (not 120x120)

---

## 🚀 Solutions

### Solution 1: Force Start with Visibility Check
```powershell
python scripts/python/test_kenny_window_creation.py
```

### Solution 2: Find and Show Window
```powershell
python scripts/python/find_and_show_kenny_window.py
```

### Solution 3: Direct Start
```powershell
python scripts/python/start_kenny_direct.py
```

### Solution 4: Check Window Title
Look for window titled: **"Kenny (@IMVA) - Enhanced Desktop Assistant"**

---

## 🔧 What Was Fixed

### Priority 1 Enhancements:
- ✅ Initial position validation (ensures on-screen)
- ✅ Windows API force visibility
- ✅ Auto-recovery from off-screen positions

### Window Creation:
- ✅ Window title: "Kenny (@IMVA) - Enhanced Desktop Assistant"
- ✅ Window size: 120x120px (fixed)
- ✅ Initial position: Validated to be on-screen
- ✅ Force visibility: Windows API calls

---

## 📋 Manual Check Steps

1. **Check Task Manager:**
   - Look for Python processes
   - Check if `kenny_imva_enhanced.py` is running

2. **Check Window Position:**
   - Run: `python scripts/python/find_and_show_kenny_window.py`
   - Look for 120x120 windows
   - Check for "Kenny" in title

3. **Check Desktop:**
   - Look for red circle (Hot Rod Red)
   - Check desktop corners and edges
   - Check if window is minimized

4. **Check Logs:**
   - Look for error messages
   - Check if window creation succeeded

---

## 🎯 Expected Window Properties

- **Title:** "Kenny (@IMVA) - Enhanced Desktop Assistant"
- **Size:** 120x120px
- **Position:** On-screen (validated)
- **Visible:** Yes (forced via Windows API)
- **Content:** Hot Rod Red circle with hexagonal helmet

---

## 🐛 Known Issues

1. **Window at (-32000, -32000):**
   - This is Windows' "minimized" position
   - Fixed by: Priority 1 auto-recovery
   - Manual fix: `find_and_show_kenny_window.py`

2. **Window Size Wrong:**
   - Should be 120x120px
   - Fixed by: Window size validation in `create_window()`

3. **Window Not Visible:**
   - Fixed by: Windows API force visibility calls
   - Fixed by: `topmost` attribute

---

**Tags:** #KENNY #TROUBLESHOOTING #VISIBILITY @JARVIS @LUMINA
