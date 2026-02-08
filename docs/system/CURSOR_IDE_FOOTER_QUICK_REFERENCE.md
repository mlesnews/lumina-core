# Cursor IDE Footer Customization - Quick Reference ✅

**Status:** ✅ Footer customization complete

---

## 🎯 Footer Format

**Custom Footer:**
```
(#/#) #ask-heap-stack | (X) #problems | /_\ #warnings | (( i )) #information | (N) #notifications [IDE-QUEUE]
```

**Components:**
- **Prefix:** `(#/#) #ask-heap-stack` - Ask heap stack (current/total)
- **Problems:** `(X) #problems` - VS Code problems (stock)
- **Warnings:** `/_\\ #warnings` - VS Code warnings (stock)
- **Information:** `(( i )) #information` - VS Code information (stock)
- **Suffix:** `(N) #notifications [IDE-QUEUE]` - Notifications count

---

## 🚀 Quick Commands

### Update Settings
```bash
python scripts/python/cursor_ide_footer_customization.py --update
```

### Show Footer
```bash
python scripts/python/cursor_ide_footer_customization.py --display
```

### Add Ask
```bash
python scripts/python/cursor_ide_footer_customization.py --add-ask
```

### Remove Ask
```bash
python scripts/python/cursor_ide_footer_customization.py --remove-ask
```

### Get Status
```bash
python scripts/python/cursor_ide_footer_customization.py --status
```

---

## 📊 Data Files

- `data/ask_heap_stack/ask_heap_stack.json` - Ask-heap-stack data
- `data/ide_notifications/notifications.json` - Notifications data

---

## ✅ Status

- ✅ Prefix: (#/#) #ask-heap-stack
- ✅ Suffix: (N) #notifications [IDE-QUEUE]
- ✅ Settings integration
- ✅ VS Code extension ready
- ✅ Unified queue sync

**Footer customization complete!**

---

**Tags:** #CURSOR_IDE #FOOTER #QUICK_REFERENCE @JARVIS @LUMINA
