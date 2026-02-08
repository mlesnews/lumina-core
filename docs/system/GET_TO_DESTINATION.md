# Get to Destination — Fast, Effective, Efficient (#PEAK)

**Destination**: Local AI clusters online + working Lumina extension + JARVIS (stop token burn) + backups in place + clean git.

---

## Order of operations (do in order)

### 1. Lumina extension — DONE this session
- BDA run: Lumina Core **2.0.0** built and installed.
- **You do**: **Developer: Reload Window** in Cursor so the extension activates.

### 2. Cursor → local AI (main goal)
- In Cursor: open model selector (top-right). You should see **ULTRON** and **Iron Legion**.
- Default = **ULTRON** (localhost). Use it so requests hit local Ollama, not cloud.
- **Ollama on laptop**: If ULTRON fails, run `ollama serve` and ensure `http://localhost:11434/api/tags` works. See [CURSOR_LOCAL_AI_FIX_CHECKLIST.md](CURSOR_LOCAL_AI_FIX_CHECKLIST.md).

### 3. Backups (don’t skip)
- **Lumina backups**: In a **normal terminal** (not Cursor Agent): `python execute_all_backups.py`. Maps B:, runs local_enterprise_backup + laptop state.
- **Active Backup for Business**: In DSM, confirm PC backup tasks ran.
- **Hyper Backup**: In DSM, confirm NAS backup tasks ran.  
  See [BACKUP_CHECKLIST.md](BACKUP_CHECKLIST.md).

### 4. Git — batch commits (no --no-verify)
- Commit in **batches** so the pre-commit security validator runs. See [no_commit_no_verify.mdc](.cursor/rules/no_commit_no_verify.mdc).
- First batch: rules + main-goal/roadmap/backup docs (already staged or stage and commit). Then more batches until clean.

---

## One-line summary

Reload Cursor → use **ULTRON** in model selector → run `python execute_all_backups.py` in a normal terminal → check ABB + Hyper Backup in DSM → batch-commit remaining changes (no --no-verify).

---

**Main goal**: [MAIN_GOAL_LOCAL_AI_CLUSTERS.md](MAIN_GOAL_LOCAL_AI_CLUSTERS.md)  
**Backup**: [BACKUP_CHECKLIST.md](BACKUP_CHECKLIST.md)  
**Local AI fix**: [CURSOR_LOCAL_AI_FIX_CHECKLIST.md](CURSOR_LOCAL_AI_FIX_CHECKLIST.md)
