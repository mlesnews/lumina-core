# Notification Queue Aligned with Helpdesk (Problems Queue)

**Date**: 2026-01-29  
**Status**: ✅ Aligned  
**Tag**: @helpdesk @C3PO @notifications

---

## Overview

The **notifications queue** is structured like the **problems queue** (helpdesk tickets) so both can be worked the same way: one file per item, index for listing, and clear link to PM/C/T tickets when C-3PO has created them.

---

## Structure (Mirror of Helpdesk)

| Helpdesk (problems) | Notifications queue |
|--------------------|---------------------|
| `data/helpdesk/ticket_counter.json` | (no counter; notification IDs are hashes) |
| `data/helpdesk/tickets/PM*.json`, `C*.json`, `T*.json` | `data/notification_tickets/tickets/<ticket_id>.json` |
| One file per ticket | One file per notification record |

- **Index**: `data/notification_tickets/tickets.json` — `last_updated` + `tickets` dict (key = ticket_id).
- **Per-ticket files**: `data/notification_tickets/tickets/<ticket_id>.json` — one JSON file per notification (same shape as each entry in the index).

Load order: if `tickets/` has any `.json` files, load from there; otherwise load from `tickets.json` (and migrate writes into `tickets/` on first save).

---

## Schema (Notification Record)

Each notification record (in index and in its file) can have:

- `ticket_id` — unique id (hash or legacy)
- `title`, `description`, `status`, `priority`, `created_at`, `updated_at`, `resolved_at`
- `notification_type`, `severity`, `source` (e.g. `vscode_monitor`)
- **Link to helpdesk**: `pm_ticket`, `c_ticket`, `t_ticket` (or `tickets.PM`, `tickets.C`, `tickets.T`) when C-3PO has created PM/C/T
- `request_id`, `team`, `metadata`, `c3po_result`, etc.

Older records may have `cursor_request_id`, `tracking_numbers`, `help_desk_ticket`; newer ones use `pm_ticket`/`c_ticket`/`t_ticket` and optional `tickets` + `c3po_result`.

---

## How to Work the Stack (Fix Open Notifications)

1. **List open notifications**
   - Read from `data/notification_tickets/tickets.json` or scan `data/notification_tickets/tickets/*.json`.
   - Filter by `status != "resolved"` and `status != "closed"`.

2. **Use linked PM/C/T**
   - For each open notification, check `pm_ticket`, `c_ticket`, `t_ticket` (or `tickets.PM`, `tickets.C`, `tickets.T`).
   - Work the corresponding helpdesk tickets under `data/helpdesk/tickets/` (same workflow as problems queue).

3. **Update and close**
   - When the issue is fixed, update the notification record: set `status` to `resolved`, set `resolved_at`, and optionally update `metadata`.
   - Save the notification file under `tickets/<ticket_id>.json` and keep the index in sync (monitor script does this on save).

4. **Automation**
   - `python scripts/python/monitor_vscode_notifications.py --report` — loads/saves notification tickets (and creates PM/C/T for known issues if configured).
   - Use helpdesk scripts/triage for the linked PM/C/T tickets as you would for any other problem.

---

## References

- **Helpdesk structure**: `docs/HELPDESK_PROBLEM_CHANGE_MANAGEMENT_STRUCTURE.md`, `docs/system/HELPDESK_TICKET_NUMBERING.md`
- **Monitor script**: `scripts/python/monitor_vscode_notifications.py` (load/save use `_load_notification_tickets_from_storage`, `_save_notification_tickets_to_storage`)
- **Diagnostics**: `scripts/python/notification_lifecycle_diagnostics.py` (correlate uses same load from index + `tickets/`)
