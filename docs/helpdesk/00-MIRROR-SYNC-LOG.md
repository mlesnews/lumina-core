# Public Mirror — Helpdesk Sync Log

This file tracks closures applied to the public mirror that lag behind the private operator tree. Maintained so external reviewers (Glasswing program, etc.) can trust the public ticket state.

---

## 2026-05-07 — Stale Ticket Sweep

Two long-open tickets were closed in the public mirror to bring the public state in line with operator-tree reality. Both had been silently resolved internally; only the public-facing markdown was lagging.

### `HELPDESK-20260116-DNS-HOMELAB`
- **Was**: 🔍 OPEN (HIGH) in the public `.md`
- **Now**: ✅ RESOLVED (closed 2026-01-16)
- **Why this lagged**: The companion JSON ticket file was updated to RESOLVED at close-out, but the human-readable markdown narrative wasn't refreshed. The public mirror snapshot taken on 2026-02-08 captured the pre-close markdown.
- **Verification**: `nslookup` queries against pfSense (10.17.17.1) and NAS (10.17.17.32) succeed; workflow-monitor auto-close criteria all met.

### `PROTONPASS_CLI_BUG_CONFIRMED`
- **Was**: 🔴 BLOCKED / CRITICAL in the public `.md`
- **Now**: ✅ RESOLVED — WORKAROUND IN PLACE (closed 2026-05-07)
- **Why this lagged**: The upstream Proton bug was never patched, so the ticket was kept open as a placeholder. In practice, `scripts/python/protonpass_auto_login.py` has been a reliable workaround since 2026-01-21 — credential retrieval is unblocked, automation flows work. The ticket should have been closed (with workaround note) after roughly two weeks of stable operation; it was missed.
- **Re-open trigger**: Major Proton CLI release that changes session handling — re-test and re-open if behavior regresses.

---

## How the public mirror is supposed to track the operator tree

- The operator tree (`.lumina/`) is the source of truth.
- Tickets resolve in the operator tree first.
- The public mirror (this file's repo) gets a periodic push that includes resolved tickets.
- When the daily internal sweep flags "stale public tickets," it usually means a push lag, not a real open issue. The fix is to update the public `.md` (or the daily sweep view of it) and push the mirror.

---

## Next sync checklist (template)

When closing future stale-public tickets:
1. Read the operator-tree status (`.lumina/docs/helpdesk/<ticket>` or `.lumina/helpdesk/tickets/`).
2. If RESOLVED there, update the public-mirror `.md` to match — keep the closure timestamp from the operator tree.
3. If the resolution is "workaround," document the workaround path, the date workaround went into production, and the re-open trigger.
4. Append an entry to this log with a one-paragraph "why this lagged."
5. Push to GitHub.
