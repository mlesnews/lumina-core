# Sync Status — core

**Last sync from operator tree:** 2026-02-08 (initial commit)
**Mirror status check:** 2026-05-07 (this commit)
**Archive state:** active (unarchived 2026-05-07; was archived 2026-02-08 → 2026-05-07)

---

## What this repo is

This is one of nine **public snapshot mirrors** of Project Lumina, partitioned in 2026-02-08 to fit GitHub's 2GB pack-size limit. Each repo holds a slice of the operator tree as it stood on that date.

## Where active development happens

These nine snapshot repos are intentionally **content-frozen at the 2026-02-08 baseline**. Active Lumina development now lives in:

- **[lumina-oss](https://github.com/mlesnews/lumina-oss)** — AI-native workflow primitives (open-source slice)
- **[lumina-homelab](https://github.com/mlesnews/lumina-homelab)** — Defensive-focused AI homelab plugin (Castle Doctrine)

Glasswing reviewers should look at those two repos for current code.

## Why these snapshots are still useful

- **Reviewer evidence** — captures the 2026-02-08 state for audit / Glasswing application history
- **Helpdesk tickets** — historical ticket close-outs land here (see `docs/helpdesk/` in lumina-core)
- **Anchor for diffs** — the operator tree's evolution can be measured against this baseline

## Sync cadence going forward

The mirror sync log lives at [`lumina-core/docs/helpdesk/00-MIRROR-SYNC-LOG.md`](https://github.com/mlesnews/lumina-core/blob/main/docs/helpdesk/00-MIRROR-SYNC-LOG.md). Closure events (tickets resolved, status corrections) get pushed here as discovered. Full-content refreshes from operator tree are operator-gated and rare.
