# JARVIS Phase 3–4: Integration and Automation – Next Steps

**Date**: 2026-01-29  
**Reference**: `docs/JARVIS_CA_IDE_CONSOLIDATION_PLAN.md` §8 Migration Plan, §6 Auto-Update Mechanism

---

## Phase 3: Integration (Week 3)

- [ ] **Configure JARVIS routing** – Route commands/agents through the new `jarvis/` structure or keep `.cursor/commands/` as source of truth and wire references from `jarvis/agents/` READMEs.
- [ ] **Test all agents** – Verify each orchestrator, droid, specialized, and task agent still works after any path or config change.
- [ ] **Verify author display** – Ensure JARVIS (or Cursor) shows author credits when invoking agents; add display logic if needed.

**Config:** `.cursor/` and `.vscode/` remain primary; `jarvis/` is skeleton for future restructure. No mandatory move of commands yet.

**Validation:** Run `python scripts/python/jarvis_phase3_check.py` from repo root to verify .cursor/commands and jarvis/ skeleton exist and print the Phase 3 checklist.

---

## Phase 4: Automation (Week 4)

- [x] **Implement auto-update script** – Script that reads `config/auto_update.yaml`, fetches from sources (GitHub, NPM), validates, merges with author credit preserved. **Done:** `scripts/python/jarvis_auto_update.py`.
- [x] **Configure monitoring** – Cron or scheduled task to run auto-update (e.g. daily at 03:00 per config). **Done:** Run `.\scripts\powershell\schedule_jarvis_auto_update.ps1` from repo root to register Windows task **JARVIS_Auto_Update** (daily 03:00). Remove with `-Remove`.
- [x] **Set up notifications** – Internal log: `data/jarvis_auto_update.log`. Optional Slack/Discord: set `notifications.webhook_url` in config (script POSTs summary; do not commit real URLs).

**Config:** `config/auto_update.yaml` exists; replace placeholder `your-org` URLs with real upstream repos before running.

---

## Run the auto-update script (#automation)

From repo root (`.lumina/`):

```bash
# Check only (no changes)
python scripts/python/jarvis_auto_update.py --check-only

# Dry run (report what would be applied)
python scripts/python/jarvis_auto_update.py --dry-run

# Apply updates (requires real URLs in config; placeholder URLs are skipped)
python scripts/python/jarvis_auto_update.py

# Verbose
python scripts/python/jarvis_auto_update.py -v
```

**Requirements:** Python 3.9+, PyYAML (`pip install pyyaml` or `pip install -r scripts/python/requirements.txt`). Git and npm on PATH for GitHub/NPM sources. Placeholder `your-org` URLs are skipped; replace with real upstream repos in `config/auto_update.yaml` to enable updates.

**PowerShell (single entry):** From repo root: `.\scripts\powershell\run_jarvis_auto_update.ps1` or with `-CheckOnly`, `-DryRun`, `-Verbose`.

**Do-it-all:** From repo root: `.\scripts\powershell\jarvis_do_all.ps1` — registers scheduled task (if missing), runs Phase 3 check, auto-update --check-only, --dry-run. Use `-Apply` to run auto-update for real. Use `-SkipSchedule` to skip task registration.

---

## Scheduling / monitoring (Phase 4)

Run auto-update daily (e.g. 03:00 UTC per `config/auto_update.yaml`).

**Windows Task Scheduler:** From repo root run once: `.\scripts\powershell\schedule_jarvis_auto_update.ps1`. This registers task **JARVIS_Auto_Update** (daily at 03:00, working directory = repo root). To remove: `.\scripts\powershell\schedule_jarvis_auto_update.ps1 -Remove`.

**Cron (Linux/WSL):** Add to crontab:
```cron
0 3 * * * cd /path/to/.lumina && python scripts/python/jarvis_auto_update.py >> data/jarvis_auto_update.log 2>&1
```

**Notifications:** Internal log is written to `data/jarvis_auto_update.log` when `internal_log` is in notifications.channels. Optional Slack/Discord: set `notifications.webhook_url` in `config/auto_update.yaml` (or via env); script POSTs a JSON `{"text": "JARVIS Auto-Update: N ok, M failed"}`. Do not commit real webhook URLs.

---

## Quick reference

| Item | Location |
|------|----------|
| Auto-update config | `config/auto_update.yaml` |
| Auto-update script | `scripts/python/jarvis_auto_update.py` |
| Schedule script (register task) | `scripts/powershell/schedule_jarvis_auto_update.ps1` |
| Windows task name | `JARVIS_Auto_Update` (daily 03:00) |
| Phase 3 check script | `scripts/python/jarvis_phase3_check.py` |
| Do-it-all script | `scripts/powershell/jarvis_do_all.ps1` [-Apply] [-SkipSchedule] |
| Internal log | `data/jarvis_auto_update.log` |
| JARVIS skeleton | `jarvis/` (agents, ide, lib, data, scripts, docs) |
| Plan (full) | `docs/JARVIS_CA_IDE_CONSOLIDATION_PLAN.md` |
| CA/PA/IDE deep-dive | `docs/system/CA_OEM_AND_CE_CONFIG_DEEP_DIVE.md` |
