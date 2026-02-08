# Route Lumina Unpublish Through Helpdesk (Create Tickets)

**Goal**: Route the “remove Lumina from all marketplaces” task through the Helpdesk by creating tickets (PM, C, T) so it is tracked and assigned like other work.

---

## Why use the Helpdesk

- **Tracking**: Tickets appear in the helpdesk ticket set and can be triaged, assigned, and closed.
- **Ownership**: C-3PO assigns tickets to **helpdesk_support** (or configured team); Technical Lead / assignee executes unpublish.
- **Audit**: PM (Problem), C (Change Request), T (Task) are linked; completion is visible in ticket status.

---

## Create tickets (one command)

From repo root:

```powershell
python scripts/python/create_lumina_unpublish_helpdesk_tickets.py
```

This script:

1. Creates **PM** (Problem): Lumina extensions published to marketplaces — policy breach; must unpublish.
2. Creates **C** (Change Request): Unpublish all five Lumina extensions from VS Code Marketplace and Open VSX; checklist and docs.
3. Creates **T** (Task): Execute unpublish (steps, links to PM/C, docs).
4. If C-3PO assigner is available, assigns all three to **helpdesk_support**.

Tickets reference [REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md](REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md) for the full checklist and steps.

---

## After tickets are created

- **Helpdesk / assignee**: Use REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md to perform unpublish (VS Code Marketplace, Open VSX, verification).
- **Closure**: When all sources are cleaned and verification is done, close PM, C, and T (resolved/closed).

---

## Summary

- **Create tickets**: Run `python scripts/python/create_lumina_unpublish_helpdesk_tickets.py` so the task goes through the Helpdesk.
- **Execute**: Assignee follows REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md and closes tickets when done.
