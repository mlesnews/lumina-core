# Kenny Window Visibility - Critical Fix

**Problem**: Kenny's window doesn't appear when run in background processes.

**Root Cause**: Tkinter windows require a foreground process with a message loop to display properly.

**Solution**: Run Kenny in a **foreground terminal window**.

---

## How to Start Kenny (So Window Appears)

### Method 1: Direct Command (Foreground)

Open a **new PowerShell/terminal window** and run:

```powershell
cd "C:\Users\mlesn\Dropbox\my_projects\.lumina"
python scripts/python/kenny_imva_enhanced.py --match-ace
```

**Important**: This must run in a **foreground terminal** (not background) for the window to appear!

### Method 2: Use the Foreground Script

```powershell
python scripts/python/start_kenny_foreground.py
```

---

## What You Should See

When Kenny starts correctly, you should see:
- ✅ A window with beige/light background
- ✅ Orange circle (Kenny's body)
- ✅ Black circle in center (Kenny's face)
- ✅ White dots (eyes)
- ✅ Gold outline (zipper detail)
- ✅ Window stays open and Kenny moves slowly

---

## Current Status

- ✅ Window creation code is correct
- ✅ Sprite rendering is fixed (PhotoImage reference kept)
- ✅ Face/details are drawn (black circle, eyes, gold outline)
- ✅ Animation loop is running
- ⚠️  **Window only appears in foreground processes**

---

## Why Background Doesn't Work

Tkinter's `mainloop()` requires:
- A foreground process
- Access to the display
- Message pump running

Background processes can't display GUI windows on Windows.

---

## Next Steps

1. **Run in foreground terminal** - Window will appear
2. **Verify sprite is visible** - Orange donut with black face
3. **Check animation** - Kenny should move slowly
4. **Test collaboration** - Check if position is tracked

---

**Tags**: #KENNY #WINDOW #VISIBILITY #FIX @JARVIS @LUMINA
