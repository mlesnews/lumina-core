# Reboot Monitor – Graceful Shutdown & Fast Startup (Fully Automatic)

**Purpose**: Shutdown, reboot, and post-reboot verify run **automatically**—no manual steps. Logs are written for monitoring and refactoring.

**Tag**: `@reboot` `@monitor` `#automation`

---

## Fully automatic flow (no human intervention)

1. **One-time setup**: Install the post-reboot verify task so it runs automatically at logon (2 min delay).
2. **When you want to reboot**: Run one command. It closes Cursor, stops Ollama/Docker, logs state, and restarts the PC.
3. **After login**: Post-reboot verify runs automatically (Task Scheduler). Headless daemon (or unified startup) starts services. No manual run.

---

## One command: restart PC (fully automatic)

From the repo root (e.g. `.lumina` or workspace that contains `.lumina`):

```powershell
.\scripts\powershell\lumina_reboot_auto.ps1 -Restart
```

**What it does (no prompts)**:

- Ensures the post-reboot verify task is installed (so it runs at next logon).
- Closes **Cursor** automatically (graceful close, then force if needed).
- Stops **Ollama** and **Docker** gracefully.
- Logs pre-shutdown state to `data/reboot_monitor/pre_shutdown_*.json`.
- Restarts the PC in 30 seconds (configurable in `config/reboot_shutdown_startup.json`).

After login, **post-reboot verify** runs automatically (2 min after logon) and writes `data/reboot_monitor/post_reboot_*.json`. **Headless daemon** (if installed) starts lighting, router, VAs.

---

## One-time: install post-reboot verify at logon

So that after every boot the verify script runs automatically (no manual step):

```powershell
.\scripts\powershell\lumina_post_reboot_verify.ps1 -Install
```

Or use the wrapper (which also installs the task when you first run `-Restart`):

```powershell
.\scripts\powershell\lumina_reboot_auto.ps1 -Install
```

**If you see "Access is denied"**: Run **PowerShell as Administrator** (right‑click PowerShell → Run as administrator), then run the same `-Install` command again from the repo root. The task is created for your user and only needs admin once to register it.

---

## Other commands

| Command | Effect |
|--------|--------|
| `lumina_reboot_auto.ps1 -Restart` | Full automatic: close Cursor, stop Ollama/Docker, restart PC. Verify runs at logon. |
| `lumina_reboot_auto.ps1 -Shutdown` | Same but power off instead of restart. |
| `lumina_reboot_auto.ps1 -Install` | Install post-reboot verify task (runs at logon). |
| `lumina_reboot_auto.ps1 -Uninstall` | Remove post-reboot verify task. |
| `lumina_graceful_shutdown.ps1 -Restart` | Same as reboot_auto -Restart (no task check). |
| `lumina_graceful_shutdown.ps1 -Shutdown` | Graceful close + power off. |

---

## What runs automatically (no manual step)

- **Before reboot**: You run one command (`lumina_reboot_auto.ps1 -Restart`). Cursor closes, Ollama/Docker stop, PC restarts.
- **After logon**: **LUMINA-Headless-Startup-Daemon** runs at 1 min (lighting, router, VAs). **LUMINA-Post-Reboot-Verify** runs at 3 min (waits for drives, checks Ollama/Iron Legion, writes report). Order avoids out-of-sequence checks (Docker/WSL already up before verify). See **docs/system/STARTUP_TROUBLESHOOTING.md** if you see duplicate Cursor or multiple cmd/PowerShell windows.

---

## What to share when you’re back (for refactoring)

After a reboot, logs are written automatically. When you return to this chat, share:

1. **Pre-shutdown log**: `data/reboot_monitor/pre_shutdown_*.json` (latest).
2. **Post-reboot report**: `data/reboot_monitor/post_reboot_*.json` (latest).
3. **Startup log** (if present): `data/scotty_monitor/startup_*.json` (latest).
4. Any errors in `logs/` (e.g. `unified_startup_*.log`, `lumina_startup_*.log`).

With those, we can **streamline and enhance** shutdown order, timeouts, and startup checks.

---

## Single startup path (avoid duplicate startups)

- **Preferred**: One startup entry — **headless daemon**.
  Install: `python scripts/python/lumina_headless_startup_daemon.py --install`
  See `docs/system/STARTUP_CONSOLIDATION.md` and `config/unified_startup_config.json`.
- **Post-reboot verify** runs automatically 3 min after logon (Task Scheduler) if you ran `lumina_post_reboot_verify.ps1 -Install` or `lumina_reboot_auto.ps1 -Install` (or `-Restart` once). It only checks readiness (drives, Ollama) and writes a report; it does **not** start services. Services are started by the headless daemon (1 min). **Duplicate Cursor or multiple startup windows?** See **docs/system/STARTUP_TROUBLESHOOTING.md** and run `.\scripts\powershell\audit_startup_lumina.ps1`.

---

## References

- **Config**: `config/reboot_shutdown_startup.json`
- **Graceful stop (Ollama/Docker)**: `scripts/powershell/stop_ollama_docker.ps1`
- **Startup consolidation**: `docs/system/STARTUP_CONSOLIDATION.md`
- **Startup troubleshooting** (duplicate Cursor, out-of-order windows): `docs/system/STARTUP_TROUBLESHOOTING.md`, `scripts/powershell/audit_startup_lumina.ps1`
- **Pre-reboot checklist**: `docs/system/PRE_REBOOT_CHECKLIST_2026-01-29.md`
- **JARVIS after reboot**: `docs/system/JARVIS_CHAT_AFTER_REBOOT_5W1H_AND_GAPS.md`
- **Scotty startup/focus monitor**: `docs/operations/SCOTTY_FOCUS_AND_STARTUP_MONITOR.md`
