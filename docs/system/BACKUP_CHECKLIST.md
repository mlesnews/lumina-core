# Backup Checklist — Don't Skip Backups

**Purpose**: One place for the backup stack so we don't forget. Git/local Git + Active Backup for Business + Hyper Backup.

---

## The backup stack

| What | Role | Where / How |
|------|------|-------------|
| **Git / local Git** | Repo and local enterprise backup; sync to NAS Git Server | `execute_all_backups.py` → `local_enterprise_backup.py`; NAS DSM Git Server. See [NAS_DSM_GIT_SERVER_SETUP.md](NAS_DSM_GIT_SERVER_SETUP.md). |
| **Active Backup for Business** | Back up PCs/servers to NAS (Synology) | Synology DSM → Active Backup for Business. Configure tasks for this machine and others. |
| **Hyper Backup** | Back up NAS data (to another volume, USB, or cloud) | Synology DSM → Hyper Backup. Backs up NAS shares/data to a second destination. |

---

## One command (Lumina backups)

From repo root, **in a normal terminal** (not Cursor Agent — needs network for B: drive and NAS):

```powershell
python execute_all_backups.py
```

This maps B: to `\\10.17.17.32\backups`, runs **local_enterprise_backup.py** (Git/local backup), optional MariaDB backup to B:, and **backup_laptop_state.ps1**. If you're in Cursor and Agent can't reach the network, run the same command in PowerShell or Task Scheduler, or use:

```powershell
python scripts/python/lumina_sandbox_request.py execute_all_backups --wait 0
```

and have the B-Side daemon run it (see [LUMINA_SANDBOX_AB_MATRIX.md](LUMINA_SANDBOX_AB_MATRIX.md)).

---

## Checklist (don't skip)

- [ ] **Git / local backup** — Run `python execute_all_backups.py` (or ensure it runs on schedule). Confirms local_enterprise_backup and laptop state run.
- [ ] **Active Backup for Business** — In DSM, confirm backup tasks for this PC (and others) have run recently.
- [ ] **Hyper Backup** — In DSM, confirm Hyper Backup tasks (NAS → second destination) have run recently.

---

## Token burn reminder

We're burning cloud AI token allotment fast (e.g. 11% before the new month). Getting **local AI clusters online** (ULTRON, Iron Legion) + **working Lumina extension** + **JARVIS** is the main goal to cut that burn. See [MAIN_GOAL_LOCAL_AI_CLUSTERS.md](MAIN_GOAL_LOCAL_AI_CLUSTERS.md).

---

**Related**: [LUMINA_NETWORK_DRIVES.md](LUMINA_NETWORK_DRIVES.md) (B: = backups), [CLI_FIRST.md](../CLI_FIRST.md), [AUTOMATION_FIRST.md](AUTOMATION_FIRST.md)
