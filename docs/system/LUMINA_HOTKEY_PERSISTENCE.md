# LUMINA Hotkey Persistence - Core Feature

**Persistent Global Hotkeys That Survive Reboot**

---

## 🎹 Hotkeys

1. **Right Alt (RAlt)** → `@DOIT + Enter`
   - Single press sends `@DOIT` command to Cursor IDE
   - No combinations needed

2. **F23 (MS-Copilot Key)** → `@JARVIS + Enter + Voice Input`
   - Single press:
     - Sends `@JARVIS` command to Cursor IDE
     - Activates voice input
     - Starts passive voice listening mode

---

## ✅ Persistence Setup

**Status**: ✅ **CONFIGURED**

The hotkeys are now **persistent** and will:
- ✅ Start automatically on Windows boot
- ✅ Survive reboots
- ✅ Part of LUMINA core initialization

---

## 🔧 Configuration

**Config File**: `config/lumina_hotkeys.json`

```json
{
  "version": "1.0.0",
  "enabled": true,
  "autostart": true,
  "hotkeys": {
    "right_alt": {
      "key": "RAlt",
      "action": "@DOIT + Enter",
      "description": "Right Alt → @DOIT + Enter",
      "enabled": true
    },
    "f23": {
      "key": "F23",
      "action": "@JARVIS + Enter + Voice Input",
      "description": "F23 (MS-Copilot Key) → @JARVIS + Enter + Voice Input",
      "enabled": true
    }
  }
}
```

---

## 🚀 How It Works

### 1. Windows Registry Autostart

The hotkeys are registered in Windows Registry:
- **Path**: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
- **Value**: `LUMINA_Hotkeys`
- **Command**: `pythonw.exe lumina_hotkey_autostart.pyw`

### 2. AutoHotkey Script

The AutoHotkey script (`left_alt_doit_fixed.ahk`) is automatically launched on boot.

### 3. LUMINA Core Integration

Part of LUMINA core initialization - hotkeys start automatically.

---

## 📋 Management Commands

### Start Hotkeys Now
```bash
python scripts/python/lumina_hotkey_manager.py --start
```

### Enable Autostart (Persistent)
```bash
python scripts/python/lumina_hotkey_manager.py --enable-autostart
```

### Disable Autostart
```bash
python scripts/python/lumina_hotkey_manager.py --disable-autostart
```

### Check Status
```bash
python scripts/python/lumina_hotkey_manager.py --status
```

---

## 🔍 Verification

After reboot, verify hotkeys are working:

1. **Right Alt**: Press Right Alt → Should send `@DOIT + Enter` to Cursor IDE
2. **F23**: Press F23 (MS-Copilot key) → Should send `@JARVIS + Enter` and activate voice input

---

## 🛠️ Troubleshooting

### Hotkeys Not Working After Reboot

1. **Check if AutoHotkey is running**:
   ```bash
   tasklist | findstr AutoHotkey
   ```

2. **Check Registry**:
   - Open Registry Editor
   - Navigate to: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
   - Verify `LUMINA_Hotkeys` entry exists

3. **Manually start**:
   ```bash
   python scripts/python/lumina_hotkey_manager.py --start
   ```

4. **Check logs**:
   - `%TEMP%\jarvis_errors.log` (AutoHotkey errors)
   - `%USERPROFILE%\lumina_hotkey_errors.log` (Python errors)

---

## 📁 Files

- **Manager**: `scripts/python/lumina_hotkey_manager.py`
- **Autostart Launcher**: `scripts/python/lumina_hotkey_autostart.pyw`
- **AutoHotkey Script**: `scripts/autohotkey/left_alt_doit_fixed.ahk`
- **Config**: `config/lumina_hotkeys.json`

---

## ✅ Status

**✅ PERSISTENT HOTKEYS CONFIGURED**

- ✅ Right Alt → @DOIT + Enter
- ✅ F23 → @JARVIS + Enter + Voice Input
- ✅ Autostart enabled in Windows Registry
- ✅ Part of LUMINA core
- ✅ Survives reboots

**Tags**: `#LUMINA_CORE #HOTKEYS #PERSISTENT #AUTOHOTKEY @JARVIS @LUMINA`
