# Lumina vs Other CAs: Setup & Activation Comparison

**Purpose:** Compare Lumina Core’s setup and startup to other Coding Assistants (CAs) and Lumina sibling extensions so we reuse patterns that work instead of reinventing the wheel.

**Tags:** #LUMINA #ACTIVATION #CA #SETUP #STARTUP

---

## Summary

| Area | Other CAs / sibling extensions | Lumina Core (before) | Lumina Core (now) |
|------|--------------------------------|----------------------|-------------------|
| **Activation** | `onStartupFinished` (Cline, file-auto-close, cursor-active-model-status, lumina-footer-ticker, etc.) | Only `onView` + 2 `onCommand` → extension often not active when user runs a command | **`onStartupFinished`** added so extension activates when workbench is ready |
| **Commands** | All commands registered in `activate()`; available as soon as extension is active | Same, but extension rarely active until user opened a view → "command not found" | Same code; activation at startup makes all commands available from start |
| **Heavy init** | Cline: async init in `activate()`; others: light sync init | Deferred with `setTimeout(runLuminaFullActivation, 300)` | Unchanged: still deferred 300ms so startup doesn’t stall |
| **Status bar / progress** | Created in `activate()` after extension starts | Created in `runLuminaFullActivation()`; never ran if extension never activated | Now runs ~300ms after startup because `onStartupFinished` triggers `activate()` |

---

## What Was Going Wrong

1. **Lumina Core** activated only when:
   - User opened the **Lumina welcome** view (sidebar), or
   - User opened the **File Cleanup Stack** view, or
   - User ran **Reset LUMINA Progress Display** or **Show LUMINA Progress**.

2. If the user ran any **other** Lumina command (e.g. Show Status, Show Todo Status, Show Git Status) or expected the **progress/todo status bar** without having opened a view or run one of those two commands, the extension was not active → **"command not found"** or missing UI.

3. **Other CAs and our other extensions** use **`onStartupFinished`**: they activate once the workbench is ready, so all their commands and UI are registered and available from the start.

---

## What We Changed (Align With Other CAs)

- **Added `onStartupFinished`** to Lumina Core’s `activationEvents` in `package.json`.
- Kept existing `onView` and `onCommand` events for compatibility.
- No change to `activate()` or `runLuminaFullActivation()`: heavy init is still deferred by 300ms so startup stays fast.

Result: Lumina Core now activates when Cursor is ready (like Cline and the other Lumina extensions). All Lumina commands and status bars (progress, todo, footer, etc.) are registered and work without the user having to open the Lumina sidebar first.

---

## Reference: Activation Events in This Repo

| Extension | Activation events |
|-----------|--------------------|
| **lumina-core** | `onStartupFinished`, `onView:lumina.fileCleanupStack`, `onView:lumina.welcome`, `onCommand:lumina.resetProgressDisplay`, `onCommand:lumina.showProgress` |
| lumina-premium | `onStartupFinished` |
| lumina-unified-queue | `onStartupFinished` |
| lumina-footer-ticker | `onStartupFinished` |
| file-auto-close | `onStartupFinished` |
| cursor-voice-controls | `onStartupFinished` |
| cursor-active-model-status | `onStartupFinished` |
| **Cline (external)** | `onStartupFinished`, `onLanguage`, `workspaceContains:evals.env` |

---

## References

- `vscode-extensions/lumina-core/package.json` → `activationEvents`
- `docs/system/LUMINA_SIDEBAR_SKELETON_CLINE_PATTERN.md` → Activation section
- VS Code: [Activation Events](https://code.visualstudio.com/api/references/activation-events)
