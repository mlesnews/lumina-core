# VA Auto-Start Setup

**Status**: ✅ **CONFIGURED**

**Date**: 2026-01-06

## Overview

Virtual Assistants (VAs) are now configured to automatically start when the PC boots or when the user logs in.

## Installation Methods

### Method 1: User-Level Startup (Recommended - No Admin Required)

**Script**: `scripts/python/install_va_startup_user.py`

This method uses the Windows Startup folder and requires no administrator privileges.

**Installation:**
```bash
python scripts/python/install_va_startup_user.py
```

**What it does:**
- Creates a batch script to start the VA orchestrator
- Creates a VBS wrapper to run it hidden
- Copies the VBS script to Windows Startup folder
- VAs start automatically on user logon

**Location:**
- Startup folder: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Lumina VA Orchestrator.vbs`

### Method 2: Windows Task Scheduler (Requires Admin)

**Script**: `scripts/python/install_va_startup_task.py`

This method uses Windows Task Scheduler and requires administrator privileges.

**Installation:**
```bash
# Run PowerShell as Administrator, then:
python scripts/python/install_va_startup_task.py
```

**What it does:**
- Creates a Windows Task Scheduler task
- Triggers on system boot (1 minute delay)
- Triggers on user logon (30 second delay)
- Runs with highest available privileges

**Task Name:** `LuminaVAOrchestrator`

## How It Works

1. **On Boot/Logon:**
   - Startup script/VBS runs automatically
   - Starts `ai_managed_va_orchestrator.py` with `--start --daemon`
   - Orchestrator runs in headless mode (no visible window)

2. **VA Auto-Start:**
   - Orchestrator checks all VAs in monitoring loop
   - VAs with `auto_start: true` are automatically started
   - Currently configured VAs:
     - ✅ **ironman**: `auto_start: true`
     - ✅ **jarvis**: `auto_start: true`
     - ❌ **kenny**: `auto_start: false` (disabled)
     - ❌ **anakin**: `auto_start: false` (disabled)

3. **Headless Operation:**
   - All VAs run in headless/daemon mode
   - All output logged to `logs/{va_name}_{date}.log`
   - JARVIS workflow tracking active

## Configuration

### VA Auto-Start Settings

VAs are configured in `ai_managed_va_orchestrator.py`:

```python
manifests = {
    "ironman": VAManifest(
        name="ironman",
        script_path=project_root / "scripts" / "python" / "ironman_virtual_assistant.py",
        enabled=True,
        auto_start=True,  # ✅ Auto-starts
        ...
    ),
    "jarvis": VAManifest(
        name="jarvis",
        script_path=project_root / "scripts" / "python" / "jarvis_virtual_assistant.py",
        enabled=True,
        auto_start=True,  # ✅ Auto-starts
        ...
    ),
    "kenny": VAManifest(
        name="kenny",
        script_path=project_root / "scripts" / "python" / "kenny_imva_enhanced.py",
        enabled=True,
        auto_start=False,  # ❌ Manual start only
        ...
    ),
    "anakin": VAManifest(
        name="anakin",
        script_path=project_root / "scripts" / "python" / "anakin_combat_virtual_assistant.py",
        enabled=True,
        auto_start=False,  # ❌ Manual start only
        ...
    )
}
```

### Enable/Disable Auto-Start

To change which VAs auto-start, edit `scripts/python/ai_managed_va_orchestrator.py` and modify the `auto_start` parameter for each VA.

## Verification

### Check if Startup is Installed

**User-Level Startup:**
```powershell
Test-Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\Lumina VA Orchestrator.vbs"
```

**Task Scheduler:**
```powershell
schtasks /Query /TN LuminaVAOrchestrator
```

### Test Startup

**Manual Test:**
```powershell
# Test the VBS wrapper
cd "C:\Users\mlesn\Dropbox\my_projects\.lumina"
.\scripts\python\start_va_orchestrator.vbs
```

**Check Running VAs:**
```powershell
python scripts/python/ai_managed_va_orchestrator.py --status
```

### Check Logs

```powershell
# View orchestrator log
Get-Content logs/AIManagedVAOrchestrator_20260106.log -Tail 50

# View VA logs
Get-Content logs/ironman_20260106.log -Tail 50
Get-Content logs/jarvis_20260106.log -Tail 50
```

## Troubleshooting

### VAs Not Starting on Boot

1. **Check if startup script is installed:**
   ```powershell
   Test-Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\Lumina VA Orchestrator.vbs"
   ```

2. **Check orchestrator is running:**
   ```powershell
   Get-Process python | Where-Object { $_.CommandLine -like "*ai_managed_va_orchestrator*" }
   ```

3. **Check logs for errors:**
   ```powershell
   Get-Content logs/AIManagedVAOrchestrator_20260106.log -Tail 100
   ```

4. **Verify VA auto_start settings:**
   - Check `scripts/python/ai_managed_va_orchestrator.py`
   - Ensure `auto_start=True` for VAs you want to start

### Startup Script Not Running

1. **Check Windows Startup folder:**
   - Open: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
   - Verify `Lumina VA Orchestrator.vbs` exists

2. **Check file permissions:**
   - Ensure script has execute permissions
   - Try running VBS manually to test

3. **Reinstall:**
   ```bash
   python scripts/python/install_va_startup_user.py
   ```

## Uninstallation

### Remove User-Level Startup

1. Delete from Startup folder:
   ```powershell
   Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\Lumina VA Orchestrator.vbs"
   ```

2. Or manually:
   - Open: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
   - Delete `Lumina VA Orchestrator.vbs`

### Remove Task Scheduler Task

```powershell
# Run as Administrator
schtasks /Delete /TN LuminaVAOrchestrator /F
```

## Benefits

1. **Automatic Startup**: VAs start automatically on boot/logon
2. **No Manual Intervention**: Set it and forget it
3. **Headless Operation**: Runs silently in background
4. **Full Logging**: All output captured to log files
5. **JARVIS Tracking**: All workflows tracked automatically
6. **Resource Aware**: Smart startup with resource checking

## Tags

#AUTO_START #VA #STARTUP #WINDOWS #ORCHESTRATOR @JARVIS @LUMINA
