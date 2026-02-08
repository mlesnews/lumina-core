# Lumina Extension – BDA (Build, Deploy, Activate)

**Date**: 2026-01-29
**Status**: Active
**Tag**: #automation @extension lumina

---

## Overview

**BDA** = **Build** → **Deploy** → **Activate**. Single loop to circle back whenever you change the Lumina extension.

---

## One command (#automation)

From repo root or from `vscode-extensions/lumina-core`:

```powershell
.\vscode-extensions\lumina-core\build_and_install.ps1
```

Then in Cursor: **Developer: Reload Window** (or restart Cursor) to **activate**.

**Versioning (smart bump):** Each run bumps the **patch** version in `package.json` **only if** the last bump was more than **10 minutes** ago. If you run BDA twice within 10 minutes (e.g. two tiny changes in quick succession), the second run keeps the same version so you don't get 2.0.1, 2.0.2, 2.0.3 for rapid tweaks. To force no bump: `-NoVersionBump`.

**Rebuild after each request:** Run the **Lumina Core: BDA** task when you're done with a request so the VSIX is rebuilt and installed. **Tasks: Run Task** → **Lumina Core: BDA (Build Deploy Activate)**. Then **Developer: Reload Window** to activate.

**AI/agent:** After any change to `vscode-extensions/lumina-core` (e.g. `extension.ts`, `package.json`), run BDA at the end of the response: `.\vscode-extensions\lumina-core\build_and_install.ps1` (from repo root or from `lumina-core`). Do not leave Lumina Core changes without rebuilding and installing.

---

## Steps (what the script does)

| Phase    | What happens |
|----------|-------------------------------|
| **Version** | Bump patch in `package.json` (unless `-NoVersionBump`) |
| **Build**  | `npm run compile` → `npx vsce package` → `lumina-core-<version>.vsix` |
| **Deploy** | `cursor --install-extension lumina-core-<version>.vsix --force` (VSIX only — no marketplace) |
| **Activate** | You run **Developer: Reload Window** in Cursor (script only reminds) |

**VSIX only**: We do not publish to the marketplace until prod-ready. See [LUMINA_EXTENSION_VSIX_ONLY.md](LUMINA_EXTENSION_VSIX_ONLY.md).

---

## Manual BDA (if needed)

```bash
cd vscode-extensions/lumina-core
npm install   # once
npm run compile
npx vsce package
cursor --install-extension lumina-core-2.0.0.vsix --force
# Then: Developer: Reload Window in Cursor
```

---

## Circle back

- After editing `vscode-extensions/lumina-core/src/extension.ts` (or any extension code), run the script again for a full BDA.
- If activation fails (e.g. “depends on unknown extension”), see `docs/LUMINA_EXTENSION_FIX.md` and notification queue (Lumina Core / GitHub Copilot dependency).

---

## References

- Script: `vscode-extensions/lumina-core/build_and_install.ps1`
- README: `vscode-extensions/lumina-core/README.md`
- Fix guide: `docs/LUMINA_EXTENSION_FIX.md`
