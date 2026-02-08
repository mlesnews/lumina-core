# Startup Troubleshooting – Duplicate Cursor, Out-of-Order Windows, Lumina Stalling

**Purpose:** Fix “Lumina still loading/stalling,” “more than one Cursor starts,” “multiple cmd/PowerShell windows,” and “scripts run after Docker/WSL have long started.”

**Tag:** `@startup` `@troubleshooting` `#automation`

---

## What’s going wrong

- **Lumina still loading/stalling** – Extension or startup scripts doing heavy work at logon; multiple things activating.
- **Second Cursor starts minutes after the first** – Two different things are launching Cursor (e.g. Startup folder + Task Scheduler, or two tasks).
- **Multiple cmd.exe / PowerShell windows** – Several startup scripts or tasks run at logon with different delays; some run visible (not hidden).
- **Out-of-order** – Scripts that “check Docker/WSL” run at 2 min when Docker/WSL are already up; windows appear in the wrong order.

---

## Single startup path (what should run)

| When   | What runs                               | Window      |
|--------|-----------------------------------------|------------|
| Logon  | **Nothing** from Lumina (no Startup folder items; no extra tasks). | —          |
| +1 min | **LUMINA-Headless-Startup-Daemon**     | None (pythonw) |
| +3 min | **LUMINA-Post-Reboot-Verify**           | None (PowerShell -WindowStyle Hidden) |

- **Cursor:** Lumina does **not** start Cursor. Start Cursor **once** yourself (shortcut or Start menu). If two Cursors appear, something **other than Lumina** is launching Cursor twice (Startup folder or a second task).
- **Docker/WSL:** Usually ready early. Post-reboot verify runs at **3 min** so it runs **after** the headless daemon (1 min) and after Docker/WSL are up; checks are in order and you avoid “checking after they’ve long started.”

---

## Step 1: Audit what actually runs

From repo root:

```powershell
.\scripts\powershell\audit_startup_lumina.ps1
```

Then with a dry-run of cleanup:

```powershell
.\scripts\powershell\audit_startup_lumina.ps1 -Fix
```

This shows:

- Everything in your **Startup folder** (and flags Lumina/Cursor-related items).
- All **logon-triggered** Task Scheduler tasks (and their delays).
- Recommended single path and a cleanup suggestion.

---

## Step 2: Remove duplicates and align with single path

1. **Startup folder**
   Remove everything Lumina-related (and any **duplicate** Cursor launcher).
   Keep at most **one** Cursor shortcut if you want Cursor at logon.

2. **Task Scheduler**
   Keep only:
   - **LUMINA-Headless-Startup-Daemon** (1 min)
   - **LUMINA-Post-Reboot-Verify** (3 min)

   Remove deprecated Lumina tasks if present:
   - LUMINA-Start-All-VAs-On-Boot
   - LUMINA-Complete-System-Startup
   - JARVIS-Light-Profile-Startup
   - LUMINA-Unified-Startup

3. **Apply cleanup and reinstall headless daemon only**

   From repo root (PowerShell; Admin if task registration fails):

   ```powershell
   .\scripts\startup\cleanup_redundant_startup.ps1 -InstallHeadless
   ```

   This removes the redundant startup items above and ensures only the headless daemon (1 min) is installed. Then ensure post-reboot verify is installed with a **3 min** delay (see Step 3).

---

## Step 3: Post-reboot verify delay (3 min)

So that “check Docker/WSL” runs **after** headless and after Docker/WSL are up:

- Config: `config/reboot_shutdown_startup.json` → `post_reboot.task_delay_after_logon` = `"PT3M"`.
- Reinstall the verify task so it uses 3 min:

  ```powershell
  .\scripts\powershell\lumina_post_reboot_verify.ps1 -Uninstall
  .\scripts\powershell\lumina_post_reboot_verify.ps1 -Install
  ```

(If you use `Install-PostRebootVerifyTask.ps1`, run that after the config change so the new delay is applied.)

---

## Step 4: If two Cursors still start

Lumina **never** starts Cursor. So:

1. Run the audit again: `.\scripts\powershell\audit_startup_lumina.ps1`
2. In **Startup folder**: look for two Cursor shortcuts or two items that launch Cursor — remove one.
3. In **Task Scheduler**: look for any task that runs “Cursor” or “cursor.exe” — remove the duplicate (keep only one way to start Cursor at logon, if any).

---

## Lumina extension stalling

- Extension now uses **onStartupFinished** and defers heavy init in `setImmediate(runLuminaFullActivation)` so the sidebar can show quickly.
- If the UI still stalls: **Developer: Reload Window** after a rebuild; check **Help → Toggle Developer Tools → Console** for `[Lumina Core] Full activation failed:`.
- See `docs/system/LUMINA_SIDEBAR_SKELETON_CLINE_PATTERN.md` and `docs/system/CURSOR_IDE_QOL_INDEX.md`.

---

## References

- **Audit script:** `scripts/powershell/audit_startup_lumina.ps1`
- **Cleanup script:** `scripts/startup/cleanup_redundant_startup.ps1`
- **Config:** `config/reboot_shutdown_startup.json`, `config/unified_startup_config.json`
- **Single path:** `docs/system/STARTUP_CONSOLIDATION.md`, `docs/system/REBOOT_MONITOR_SHUTDOWN_STARTUP.md`
