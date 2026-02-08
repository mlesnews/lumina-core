# Request Workflow — Before and After Every @ask / Milestone

**Purpose:** Single breadcrumb path for handling any request (@ask, major/minor milestone). Follow this workflow so the rule leads to the right actions.

**Tags:** #WORKFLOW #REQUEST #ASK #MILESTONE #SNAPSHOT @JARVIS @LUMINA

---

## Steps (breadcrumbs → actions)

### 0. Snapshot before (pre-request)

**Action:** Capture current state before starting so you can revert or compare.

- **Automated (if workflow executor runs):** Snapshot is created by executor; see [GIT_MILESTONE_SNAPSHOTS](GIT_MILESTONE_SNAPSHOTS.md).
- **Manual:** From repo root:
  - **Option A:** `python scripts/python/jarvis_git_milestone_snapshots.py --snapshot --type minor --description "Pre: <short request summary>"`
  - **Option B:** `git add -A && git status && git commit -m "chore: snapshot before <request summary>"`

**Breadcrumb:** [GIT_MILESTONE_SNAPSHOTS](../../GIT_MILESTONE_SNAPSHOTS.md) · [GIT_MILESTONE_SNAPSHOTS_ACTIVE](../../GIT_MILESTONE_SNAPSHOTS_ACTIVE.md)

---

### 1. Do the work (request execution)

- Follow **one_shot_no_mess** rule (`.cursor/rules/one_shot_no_mess.mdc`): check local resources first, then implement; verify; leave no mess.
- Accept changes (Accept All / Keep All) so edits land; see [CURSOR_WORKFLOW_SOLUTIONS](CURSOR_WORKFLOW_SOLUTIONS.md).
- File cleanup → validate → close when done: [FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW](FILE_CLEANUP_VALIDATION_CLOSE_ARCHIVE_WORKFLOW.md).

---

### 2. Snapshot after (post-request / milestone complete)

**Action:** Commit state after the request or milestone so "last commit" is not left for days.

- **Automated (if workflow executor runs):** Snapshot created by executor.
- **Manual:** From repo root:
  - **Option A:** `python scripts/python/jarvis_git_milestone_snapshots.py --snapshot --type minor --description "Post: <short request summary>"`
  - **Option B:** `git add -A && git status && git commit -m "chore: snapshot after <request summary>"`

**Breadcrumb:** [GIT_MILESTONE_SNAPSHOTS](../../GIT_MILESTONE_SNAPSHOTS.md)

---

## Quick reference

| When | Action |
|------|--------|
| Before starting a request / milestone | Snapshot before → see [GIT_MILESTONE_SNAPSHOTS](../GIT_MILESTONE_SNAPSHOTS.md) or run `jarvis_git_milestone_snapshots.py --snapshot` / `git commit` |
| During | One-shot, accept changes, verify, cleanup — see [EDITOR_WORKFLOWS](EDITOR_WORKFLOWS.md), [one_shot_no_mess](.cursor/rules/one_shot_no_mess.mdc) |
| After request / milestone complete | Snapshot after → same as above |

---

## Rule → breadcrumbs

- **Git workflow rule** (milestone snapshots): Follow → **this doc** → [REQUEST_WORKFLOW](REQUEST_WORKFLOW.md) → Step 0 (snapshot before), Step 2 (snapshot after) → concrete actions above.
- **One-shot / @ask:** This workflow wraps the request; snapshot before + after are part of it. See also [@ask command](../../.cursor/commands/@ask.md).
