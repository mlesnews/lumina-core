# Bones + Lumina onboard — optionals completed

**Purpose**: Record completion of optional steps (verify, branch, snapshot, GitHub issue) for the Bones and Lumina onboard implementation.

**Date**: 2026-02-01
**Branch**: `feature/bones-lumina-onboard`

---

## Optionals completed

| Optional | Status | Notes |
|----------|--------|--------|
| **Verify Bones** | ✅ Done | Ran `python scripts/python/bones.py --skip-full`. Quick checks OK; bindings audit reported findings (expected on Windows). |
| **Verify Lumina onboard** | ✅ Done | Ran `python scripts/python/lumina_onboard.py --yes --skip-bones`. Keybindings, JARVIS pin, router test completed. |
| **Feature branch** | ✅ Done | Created `feature/bones-lumina-onboard`. |
| **Milestone snapshot** | ⚠️ Blocked | Pre-commit security validator blocks commit when staging 3458+ files. **Action**: Commit only Bones/onboard/control-plane files in a batch (see list below), then run snapshot or commit with message "Bones and Lumina onboard implementation". |
| **GitHub issue** | 📋 Manual | Create issue on GitHub if you use a project board (e.g. "Bones + Lumina onboard — health-check and wizard"). Optional. |

---

## Files to commit in a batch (for snapshot / small commit)

Stage and commit only these for a clean snapshot that passes pre-commit:

- `scripts/python/bones.py`
- `scripts/python/lumina_onboard.py`
- `docs/system/CONTROL_PLANE_CONTRACT.md`
- `docs/system/OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT.md`
- `docs/system/BONES_LUMINA_ONBOARD_OPTIONALS_COMPLETED.md` (this file)
- `config/cursor_ide_qol_registry.json`
- `docs/system/CURSOR_IDE_QOL_INDEX.md`
- `docs/system/WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE.md` (related link only)

Then run:

```powershell
python scripts/python/jarvis_git_milestone_snapshots.py --snapshot --type feature --description "Bones and Lumina onboard implementation"
```

Or commit manually with message: `feat: Bones (Lumina doctor) + Lumina onboard wizard + control plane contract`.

---

## GitHub issue (optional)

If you use GitHub issues, create one with title and description along the lines of:

- **Title**: Bones + Lumina onboard — health-check and wizard
- **Description**: Implemented Bones (Lumina doctor) health-check script, Lumina onboard wizard (Bones → keybindings → JARVIS pin → router test → MCP info), control plane contract doc, and QOL registry/index updates. Branch: `feature/bones-lumina-onboard`.
