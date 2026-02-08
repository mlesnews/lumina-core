# Intelligent Staggered Startup Configuration

## Overview

Configured intelligent staggered startup for all development tools to prevent system overload and ensure proper initialization order.

## ✅ Microsoft Teams Removal

**Status:** ✅ Removed from startup and uninstalled

- Removed from Windows startup registry
- Uninstalled AppX package (MSTeams)
- Stopped all running Teams processes

Teams will no longer start automatically on boot.

## 🚀 Startup Sequence

Applications start in this order with intelligent delays:

| Priority | Application | Delay | Reason |
|----------|------------|-------|--------|
| 1 | Docker Desktop | 0s | Base service - needs to start first |
| 2 | WSL Services | 15s | Depends on Docker, needs time to initialize |
| 3 | Ollama Service | 30s | Depends on WSL, starts after WSL ready |
| 4 | Cursor IDE | 45s | Depends on Ollama, needs models available |
| 5 | Network Drives | 60s | Final step - maps M:, Z:, Y: drives |

**Total startup time:** ~75 seconds for full sequence

## 📁 Configuration Files

- **Startup Script:** `%APPDATA%\Lumina\Startup\Lumina_Startup.ps1`
- **Startup Shortcut:** `Start Menu\Programs\Startup\Lumina Startup.lnk`
- **Configuration Script:** `scripts/powershell/setup_intelligent_startup.ps1`

## 🔧 Management

### View Current Startup Items

```powershell
.\scripts\powershell\setup_intelligent_startup.ps1 -ShowCurrent
```

### Modify Startup Sequence

Edit the startup script:
```
%APPDATA%\Lumina\Startup\Lumina_Startup.ps1
```

### Disable Startup

Remove the shortcut:
```powershell
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\Lumina Startup.lnk"
```

### Reconfigure

```powershell
.\scripts\powershell\setup_intelligent_startup.ps1
```

## 🎯 Benefits

1. **Prevents System Overload** - Staggered startup avoids resource spikes
2. **Proper Initialization Order** - Services start in dependency order
3. **Faster Overall Startup** - Parallel initialization where possible
4. **Reliable Startup** - Each service ready before next one starts

## 📊 Current Status

✅ **Teams:** Removed from startup  
✅ **Docker:** Configured for immediate startup  
✅ **WSL:** Configured with 15s delay  
✅ **Ollama:** Configured with 30s delay  
✅ **Cursor:** Configured with 45s delay  
✅ **Network Drives:** Configured with 60s delay  

## 🔍 Verification

After next boot, verify:

1. **Docker Desktop** starts immediately
2. **WSL** initializes after Docker
3. **Ollama** starts after WSL
4. **Cursor IDE** opens after Ollama
5. **Network drives** (M:, Z:, Y:) are mapped

Check logs:
```powershell
Get-Content "$env:APPDATA\Lumina\Startup\Lumina_Startup.log"
```

## 🐛 Troubleshooting

### Application Not Starting

1. Check if path exists in startup script
2. Verify application is installed
3. Check Windows Event Viewer for errors

### Startup Too Slow

- Reduce delays in startup script
- Remove unnecessary applications from sequence

### Application Starts Before Dependencies Ready

- Increase delay before that application
- Add dependency checks to script

## 📝 Notes

- Cursor IDE has built-in restart functionality for updates
- Network drives require NAS to be accessible
- All delays are configurable in the startup script
- Script runs with current user permissions

---

**Last Updated:** 2025-12-31  
**Status:** ✅ Configured and Active
