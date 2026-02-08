# File Cleanup, Validation, Close & Archive Workflow

**Purpose:** Workflow for reviewing and fixing all diagnostics in a file, validating it works, closing it from the editor, and archiving the file plus agent chat history when done.

**Tags:** #EDITOR #WORKFLOW #CLEANUP #VALIDATION #ARCHIVE #CHAT_HISTORY @JARVIS @LUMINA

---

## Overview

0. **Accept changes** — When the agent proposes edits, **accept them** (Accept All / Keep All or shortcut) so the fix lands in your buffer. With autosave enabled, that becomes the saved file. If you skip this, the fix never applies and diagnostics will still show the old content. See [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md) for shortcuts and auto-accept options.
1. **Review** all errors, problems, warnings, and informationals flagged in the file (IDE diagnostics).
2. **Clean up** the file — fix every flagged item until the file is clean.
3. **Close** the file (optional intermediate close after cleanup).
4. **Validate** the file works as intended (run tests, run the script, or manual check).
5. If changes are **successful and complete** → **close** the file so it **leaves the editor**.
6. **Archive** the file (if applicable) and **archive the agent chat history** for that work.

---

## Step 1: Review diagnostics in the file

- Open the **Problems** panel (or equivalent) and ensure the **current file** is in scope.
- Review every **Error**, **Warning**, **Problem**, and **Informational** (linter, type checker, etc.) reported for that file.
- Optionally: Run **mypy**, **pylint**, **ruff**, or other checkers on the file and treat their output as part of the review.
- **Do not** move to close until all items for this file are either fixed or explicitly accepted (e.g. documented as deferred).

**Cursor/VS Code:** View → Problems; or click the count in the status bar. Filter by file if needed.

---

## Step 2: Clean up the file

- Fix each flagged item (errors first, then warnings, then informationals as desired).
- Re-run or re-check diagnostics after edits so the file shows **no remaining issues** (or only accepted/deferred ones).
- Save the file.

**Done when:** The file has no errors and no warnings (or only those you’ve explicitly decided to leave).

---

## Step 3: Close the file (optional at this point)

- You can **close the file** after cleanup so it’s no longer in the editor.
- If you prefer to validate before closing, skip to Step 4 and close after validation.

---

## Step 4: Validate the file works as intended

- **Run** the file or the feature that uses it (tests, script, manual run).
- Confirm behavior is correct and nothing is broken.
- If validation fails, reopen the file, fix, and repeat from Step 1 as needed.

**Done when:** You’re satisfied the file works as intended.

---

## Step 5: Close the file so it leaves the editor

- If changes are **successful and complete** and you’ve validated:
  - **Close the file** so it no longer has an open tab in the editor.
- This keeps the editor focused on the next file or task.

---

## Step 6: Archive the file and agent chat history

- **File:** If your process includes archiving or moving the file (e.g. to an archive folder or branch), do that according to your project’s rules.
- **Agent chat history:** Archive the Cursor/agent chat session that produced these changes:
  - Use Cursor’s **Chat history** or **Composer history** to find the session.
  - **Archive** (or **Pin** then archive) the conversation so it’s preserved and out of the active list.
  - Optionally export or copy the conversation to a project location (e.g. `data/agent_sessions/` or a doc) if you keep session backups.

**See also:** [agent_chat_history_lifecycle_workflow](agent_chat_history_lifecycle_workflow.md) for full session lifecycle (creation → active → completion → V3 verification → archive).

---

## Quick checklist

| Step | Action | Done |
|------|--------|------|
| 1 | Review all errors/problems/warnings/informationals in the file | ☐ |
| 2 | Clean up the file (fix all; re-check until clean) | ☐ |
| 3 | (Optional) Close file after cleanup | ☐ |
| 4 | Validate file works as intended | ☐ |
| 5 | Close file so it leaves the editor | ☐ |
| 6 | Archive file (if applicable) and archive agent chat history | ☐ |

---

## Relation to other workflows

- **Git workflow:** If the changes in the file are part of a branch/PR, follow pre- and post-change Git steps (see [EDITOR_WORKFLOWS](EDITOR_WORKFLOWS.md)).
- **Session lifecycle:** For full agent session flow including V3 verification and archive instructions, see [agent_chat_history_lifecycle_workflow](agent_chat_history_lifecycle_workflow.md).
