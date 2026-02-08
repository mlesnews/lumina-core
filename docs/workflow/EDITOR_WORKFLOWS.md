# Editor Workflows

**Purpose:** Index for editor workflows: **request workflow** (snapshot before/after every @ask), **file cleanup → validation → close → archive** (primary), plus Git, Cursor IDE, and rule-based workflows.

**Tags:** #EDITOR #WORKFLOW #CLEANUP #VALIDATION #ARCHIVE #GIT #CURSOR #RULES @JARVIS @LUMINA

---

## Request Workflow (before and after every @ask / milestone)

**Breadcrumb path:** Rules point here → concrete actions.

- **Snapshot before** — Step 0: capture state before starting (script or git commit).
- **Do the work** — One-shot, accept changes, file cleanup, validate.
- **Snapshot after** — Step 2: commit when request/milestone is complete.

**Full doc:** [REQUEST_WORKFLOW](REQUEST_WORKFLOW.md) (actions: `jarvis_git_milestone_snapshots.py`, git, links to [GIT_MILESTONE_SNAPSHOTS](../GIT_MILESTONE_SNAPSHOTS.md)).

---

## 0. Primary: File Cleanup, Validation, Close & Archive

**The workflow:** When the agent proposes edits → **accept changes** (Accept All / Keep All) so the fix lands → review diagnostics → clean up the file → validate → close → archive.

**Full doc:** [FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW](FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW.md)

**Steps (short):**
0. **Accept changes** — Accept AI-proposed edits (Accept All / Keep All or shortcut) so they're in the buffer; with autosave, that's what gets saved. See [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md).
1. **Review** — All diagnostics (errors, warnings, informationals) for the file.
2. **Clean up** — Fix every flagged item until the file is clean.
3. **Close** — (Optional) Close the file after cleanup.
4. **Validate** — Run tests / script / manual check; confirm the file works as intended.
5. **Close** — If successful and complete, close the file so it leaves the editor.
6. **Archive** — Archive the file (if applicable) and archive the agent chat history for that work.

**Quick checklist:** See the full doc for the step-by-step checklist.

---

## 1. Git Workflow (Pre/Post Change)

**Rule:** `.cursor/rules/git_workflow_validation.mdc` (always applied)

- **Before changes:** Create/ref issue, feature branch, GitLens analysis (graph, history, blame, conflicts), risk assessment.
- **After changes:** Run tests, lint, verify; create/update PR; wait for CI/CD; get approvals; re-verify before merge.
- **Risk-based approvals:** Low (1), Medium (2), High (3+), Critical (4+).

**Reference:** See the rule file for full checklists.

---

## 2. Cursor IDE Workflow

### Entry points

- **Lumina AI Chat:** Command `Lumina: Open Lumina AI Chat` or **Ctrl+L** — Cursor Chat + Lumina (voice, queue, status).
- **Voice Request Queue:** Command `Lumina: Open Voice Request Queue` — multiple voice items, edit, send to chat.
- **Listening modes:** `Lumina: Set Listening Mode - Active` / `Passive` (active = auto-send or add to queue; passive = queue only).

### Pain points and solutions

| Pain point | Solution / status |
|------------|-------------------|
| Accept All / Keep All | **Lumina:** Run `Lumina: Accept All Changes (Chat / Composer)` (`lumina.acceptAllChanges`). In Lumina AI Chat the AI can trigger this to execute the Accept All UI. See [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md). |
| Send message (no Enter) | Shortcut or Lumina voice auto-send; see [CURSOR_KEYBOARD_SHORTCUTS](CURSOR_KEYBOARD_SHORTCUTS.md). |
| No pause for voice | Lumina Voice Request Queue + passive mode (queue only); see [LUMINA_AI_CHAT](../LUMINA_AI_CHAT.md). |
| Sequential voice processing | Lumina Voice Request Queue (multiple items, editable); see [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md). |

### Docs

- [CURSOR_IDE_WORKFLOW_PAIN_POINTS](CURSOR_IDE_WORKFLOW_PAIN_POINTS.md) — issues and options.
- [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md) — implemented fixes and workarounds.
- [CURSOR_KEYBOARD_SHORTCUTS](CURSOR_KEYBOARD_SHORTCUTS.md) — shortcuts and how to find/set them.
- [LUMINA_AI_CHAT](../LUMINA_AI_CHAT.md) — Lumina AI Chat, voice queue, passive/active modes.

---

## 3. Rule-Based Workflows

### Context & intent (before implementing)

**Rule:** `.cursor/rules/context_intent_baseline.mdc`

- Self-assess **context rating** and **user intent** before non-trivial or workflow-sensitive changes.
- If score is LOW or MEDIUM: do not implement; state what’s missing; ask or route to support workflow.

### Troubleshooting / decisioning

**Rule:** `.cursor/rules/troubleshooting_decisioning_workflow.mdc`

- For #TROUBLESHOOTING or #DECISIONING: get full context first; follow support workflow (RCA, brief, QA); do not fix immediately without context.

### Other rules

- **Check local resources first:** `.cursor/rules/check_local_resources_first.mdc` — search before creating; read before modifying.
- **Automation first:** `.cursor/rules/automation_first.mdc` — prefer scripts and automation over manual steps.
- **No secrets broadcast:** `.cursor/rules/no_secrets_broadcast.mdc` — no secrets in docs, config, or logs.

---

## 4. Quick checklist (editor session)

1. **Starting work:** Git pre-change (issue, branch, GitLens); context/intent if non-trivial.
2. **During work:** Cursor shortcuts; Lumina AI Chat / Voice Request Queue as needed; for a given file, use [file cleanup → validation → close → archive](FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW.md).
3. **After work:** Git post-change (tests, lint, PR, CI/CD, approvals); archive file + chat when a file is done.

---

**See also:** [FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW](FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW.md) (primary file workflow), [agent_chat_history_lifecycle_workflow](agent_chat_history_lifecycle_workflow.md), [IDE_WORKFLOW_OPTIMIZATION](../system/IDE_WORKFLOW_OPTIMIZATION.md).
