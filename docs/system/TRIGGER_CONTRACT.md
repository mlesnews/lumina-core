# Trigger contract

**Purpose**: Single contract for “run on schedule” and “run on event” — cron, webhook, pub/sub. Aligns NAS KRON, Syphon, n8n, and Lumina workflows. Automation-first.

**Related**: [CONTROL_PLANE_CONTRACT](CONTROL_PLANE_CONTRACT.md), [OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT](OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT.md)

**Last updated**: 2026-02-01
**Tags**: `#automation` `#trigger` `#cron` `#webhook` `@PEAK`

---

## 1. Contract surface

| Trigger type | Description | Config / implementation |
|--------------|-------------|--------------------------|
| **Cron / schedule** | Run at fixed times (daily, weekly, interval). | `config/lumina_scheduled_tasks.json` — tasks with schedule.type (daily, weekly), time, script. Executor: NAS KRON or local task scheduler. |
| **Webhook** | Run on HTTP POST (event). | `config/teams_webhook_config.json.example`, n8n workflows; docs reference webhook endpoints. |
| **Pub/Sub** | Run on message (e.g. Gmail Pub/Sub). | Gmail Pub/Sub triggers; n8n; config references in docs. |

---

## 2. Config as contract

- **Scheduled tasks**: `config/lumina_scheduled_tasks.json` — `tasks[].name`, `script`, `schedule.type`, `schedule.time`, `enabled`, `priority`.
- **Syphon scheduled**: `config/syphon_scheduled_sources.json` — Syphon sources and schedules.
- **n8n**: `config/n8n/*.json` — workflow definitions; webhooks and schedules inside workflows.
- **Webhook example**: `config/teams_webhook_config.json.example` — pattern for webhook-driven triggers.

---

## 3. Entry points

- **Cron**: Scripts referenced in `lumina_scheduled_tasks.json` (e.g. `scripts/python/wopr_ops.py`); run by NAS KRON or system cron/task scheduler.
- **Webhook**: n8n webhook nodes or dedicated Lumina webhook handler; URL and auth per config.
- **Pub/Sub**: Gmail Pub/Sub → n8n or Lumina handler; see docs for Gmail integration.

---

## 4. One-line summary

The **trigger contract** is: one conceptual surface for cron (schedule), webhook (HTTP event), and pub/sub (message). Config: `lumina_scheduled_tasks.json`, `syphon_scheduled_sources.json`, n8n configs, webhook examples. Run on schedule or run on event — same contract.

---

## References

- `config/lumina_scheduled_tasks.json`
- `config/syphon_scheduled_sources.json`
- `config/teams_webhook_config.json.example`
- `config/n8n/` (workflows)
- `docs/system/CONTROL_PLANE_CONTRACT.md`
