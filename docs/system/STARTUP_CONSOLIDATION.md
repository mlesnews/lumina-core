# LUMINA Consolidated Startup System

**Date**: 2026-01-27
**Status**: ✅ IMPLEMENTED

## Overview

The LUMINA Consolidated Startup Daemon (`scripts/python/lumina_consolidated_startup.py`) eliminates all duplicate service initializations by using a singleton ServiceRegistry pattern.

## Problem Solved

Before consolidation, the startup log showed massive duplication:
- **13+** Azure Service Bus client initializations
- **15+** ElevenLabs API key retrievals
- **6+** JARVIS Full-Time Super Agent initializations
- **10+** R5 Living Context Matrix integrations
- **8+** JARVIS Persistent Memory initializations
- Multiple terminal windows
- Redundant FN lock toggle testing

## Architecture

### ServiceRegistry Singleton

```python
class ServiceRegistry:
    """Singleton registry - each service initialized ONCE and reused."""
```

| Service | Before | After |
|---------|--------|-------|
| Azure Key Vault Client | ~13 retrievals | 1 singleton |
| Azure Service Bus Client | ~13 connections | 1 singleton |
| ElevenLabs API Key | ~15 retrievals | 1 singleton |
| Memory Database | ~8 connections | 1 singleton |
| R5 Living Context Matrix | ~10 integrations | 1 singleton |
| JARVIS Agent | ~6 spawns | 1 singleton |

### Key Optimizations

1. **Single Azure Key Vault Client**: Cached and reused (not application-level cached since NAS proxy handles 30-min TTL)
2. **Single Azure Service Bus Client**: Singleton pattern
3. **Single ElevenLabs TTS Client**: Shared across all JARVIS instances
4. **Single Memory Database**: One session, reused
5. **Single R5 Living Context Matrix**: One instance, reused
6. **No Duplicate Agent Spawns**: One JARVIS Full-Time Super Agent
7. **FN Key Testing**: REMOVED (lighting via registry/@MANUS only)
8. **No terminals at logon**: All startup runs headless (pythonw / Hidden). Monitor via logs only. One terminal besides WSL is the goal.

### Single-terminal policy (no extra terminals)

- **At logon**: Use only the **headless daemon** (`lumina_headless_startup_daemon.py`). It runs as `pythonw`, no console. All child processes (lighting, router, VAs) are started with `pythonw` or `-WindowStyle Hidden`.
- **Unified startup** (if used): Uses `pythonw` for all Python child processes; Task Scheduler runs the PS1 with `-WindowStyle Hidden`.
- **post_reboot_startup / start_all_vas_on_boot**: Use `pythonw` and `Start-Process -WindowStyle Hidden -NoNewWindow`; no terminals.
- **Monitor via logs**: `logs/unified_startup_*.log`, `logs/lumina_startup_*.log`, `logs/vas_startup_*.log`, etc. No need to open extra terminals.

### Recommended single startup path (avoid duplicates)

To avoid extra console windows and lighting running more than once:

1. **At logon**: Have **only one** startup entry: the headless daemon (`lumina_headless_startup_daemon.py --install`). Do **not** also run unified startup, `post_reboot_startup.ps1`, or separate lighting/VAs tasks at logon.
2. **Lighting**: The headless daemon runs lighting once per session (via `lighting_startup_guard.py`). Do not run `keyboard_lighting_auto_daemon.py` or `ac_force_enable_lighting.py` at startup separately.
3. **Cleanup**: Use `scripts/startup/cleanup_redundant_startup.ps1 -DryRun` to list other logon entries; remove duplicates so only the headless daemon runs.

## Usage

**Preferred (no terminals at logon):**

```bash
# Install headless daemon as the only logon startup (one process, pythonw, no windows)
python scripts/python/lumina_headless_startup_daemon.py --install
```

**Optional (consolidated startup, if not using headless daemon):**

```bash
# Run consolidated startup
python scripts/python/lumina_consolidated_startup.py

# Skip specific phases
python scripts/python/lumina_consolidated_startup.py --skip-lighting --skip-vas

# Install as scheduled task
python scripts/python/lumina_consolidated_startup.py --install
```

## Phases

| Phase | Description |
|-------|-------------|
| Phase 1 | Service Registry Initialization (singleton creation) |
| Phase 2 | Lighting Control (simple state check, no FN toggle) |
| Phase 3 | Core Services (Ultron Router) |
| Phase 4 | Virtual Assistants (single JARVIS instance) |

## NAS Proxy Cache

API keys are cached by the NAS proxy cache at infrastructure level (30-minute TTL). The ServiceRegistry does NOT duplicate this caching - it simply retrieves secrets once per session through the vault client.

## Reboot: Network Drives Slow to Connect (Timeout Fix)

On reboot, network drives (e.g. Z:, L:) can be slow to connect. If LUMINA startup runs at logon before drives are ready, scripts that use project root or NAS logging hit timeouts and errors.

**Fix applied:**

1. **Phase 0: Wait for network drives** – Before any other phase, startup runs `scripts/powershell/Wait-ForNetworkDrives.ps1`, which polls until configured drives (from `config/lumina_network_drives.json`) and L: are available, or timeout (90s, check every 5s). Prevents "device not ready" / timeout errors.
2. **Task Scheduler delay** – The LUMINA startup task (unified and headless) uses a **1-minute delay** after logon (`Trigger.Delay = "PT1M"`), so the task runs after the system and drive-mapping task have had time to connect shares.
3. **Cleanup redundant startup items** – Fewer terminals and scripts at logon reduce contention. Run `scripts/startup/cleanup_redundant_startup.ps1 -DryRun` to see what can be removed; use `-InstallHeadless` to migrate to the single headless daemon.

**Manual check:** Run `.\scripts\powershell\Wait-ForNetworkDrives.ps1` (no `-Silent`) to see which drives are waited for and how long they take.

## Related Files

- `scripts/python/lumina_consolidated_startup.py` - Main consolidated startup daemon
- `scripts/powershell/Wait-ForNetworkDrives.ps1` - Wait for network drives before startup
- `scripts/startup/cleanup_redundant_startup.ps1` - Remove redundant startup items
- `IRONMAN_VIRTUAL_ASSISTANT_STARTUP.LOG` - Original log showing all redundancies
- `.kilocode/rules/secrets.md` - Secrets management policy

## Success Metrics

- ✅ Zero duplicate Azure Service Bus initializations
- ✅ Zero duplicate ElevenLabs API key retrievals
- ✅ Zero duplicate JARVIS agent spawns
- ✅ Single headless terminal session
- ✅ FN key testing REMOVED (lighting via registry/@MANUS only)
- ✅ Stabilization delay reduced from 5s to 3s
