# Editor & Validation Notes

**Purpose**: Quick reference for Ruff/Mypy validation and known environment issues.

---

## Automation (#automation)

**Single entry point** (from repo root):

```powershell
python scripts/python/run_editor_validation.py
```

- **With auto-fix (Ruff only)**: `python scripts/python/run_editor_validation.py --fix`
- **With markdownlint**: `python scripts/python/run_editor_validation.py --markdown`
- **Custom manifest**: `python scripts/python/run_editor_validation.py --manifest config/other_manifest.txt`

**VS Code / Cursor**: Run task **Editor validation (Ruff + Mypy)** (Terminal → Run Task).

File list is in `config/editor_validation_manifest.txt` (one path per line; add/remove paths there). Policy: fix underlying problems only; see `.cursor/rules/fix_underlying_problem.mdc`.

---

## Deferred run (focus buffer)

When **Lumina Core** is enabled, editor validation can run **only when focus is off the editor** and after a time buffer:

- **Don’t run** while the editor pane is focused (mouse/keyboard in editor) or window is focused on Cursor.
- **Do run** when focus is elsewhere (sidebar, terminal, another app) and:
  - At least **buffer minutes** have passed since the last file save (default **30**).
  - Then again every **interval minutes** (default **10**) while focus stays off the editor.

Settings (Cursor/VS Code → Settings → search “Lumina” → Editor Validation):

| Setting | Default | Meaning |
|--------|--------|--------|
| `lumina.editorValidation.enabled` | true | Turn deferred validation on/off |
| `lumina.editorValidation.bufferMinutes` | 30 | Minutes after last save before first run |
| `lumina.editorValidation.intervalMinutes` | 10 | Minutes between runs when focus is off editor |
| `lumina.editorValidation.checkIntervalSeconds` | 60 | How often to check focus/buffer (seconds) |

Recommendation: **10 minutes** for the interval is a good balance (not too noisy, not too rare). Use 5 for more frequent runs, 15 for gentler.

---

## Ruff + Mypy (V3) on fixed scripts

Scripts validated with **no suppressions** (fix underlying problems only) are listed in `config/editor_validation_manifest.txt`. Default set:

- `scripts/python/local_enterprise_backup.py`
- `scripts/python/homelab_architecture_discovery.py`
- `execute_all_backups.py`
- `temp_map_drive.py`

**Manual commands** (from repo root), if needed:

```powershell
# Ruff
python -m ruff check <paths from manifest>

# Mypy (script-only; does not follow imports)
python -m mypy <paths> --follow-imports=skip
```

---

## Mypy project-wide

- **Script-only check**: Use `--follow-imports=skip` so only the listed files are type-checked.
- **Full project**: Without that flag, Mypy may report:
  - Missing stubs (e.g. `paramiko`, `requests`) → install `types-paramiko`, `types-requests` if needed.
  - Duplicate module (e.g. `unified_secret_manager`) → resolve via `__init__.py` or `--explicit-package-bases` / MYPYPATH.

---

## pip / moshi-personaplex

- Installing the **root** `requirements.txt` can report a dependency conflict involving `moshi-personaplex` (e.g. `huggingface-hub` vs `torch`).
- **Workaround**: Use a separate venv for personaplex/moshi, or install only the dependencies you need for the scripts you run (e.g. `scripts/python/requirements.txt` for backup/discovery scripts).

---

## cSpell

- **Project word cloud:** `.vscode/lumina-wordlist.txt` — one word per line; add any word you use regularly to clear "Unknown word" informationals. cSpell loads this via `cSpell.customDictionaries` / `cSpell.dictionaries` in `.vscode/settings.json`. With `addWords: true`, adding a word from the editor (Add to dictionary) can append to this file.
- Inline fallback: `.vscode/settings.json` → `cSpell.words` for a few legacy entries; prefer the wordlist file for the full vocabulary.

---

## Related

- **fix_linting.sh** (bash): Runs Ruff `--fix` and Markdownlint on *all* git-tracked `.py` / `.md` files. Use when you want to fix everything; requires bash/WSL. For a curated V3 set and Windows, use `run_editor_validation.py` instead.
