# Control plane contract

**Purpose**: Define the **single control plane** for Lumina: one conceptual API surface for “route request,” “list sessions,” “send to session,” and “run tool.” All CAs and JARVIS go through this contract. @PEAK: one brain, many faces.

**Related**: [JARVIS_LUMINA_HOMELAB_CONNECTION](JARVIS_LUMINA_HOMELAB_CONNECTION.md), [UNIFIED_CA_PEAK_SPEC](UNIFIED_CA_PEAK_SPEC.md), [OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT](OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT.md)

**Last updated**: 2026-02-01
**Tags**: `@JARVIS` `@PEAK` `#control_plane` `#contract`

---

## 1. What the control plane is

- **One entry point** for routing, sessions, and tools so that Cursor, JARVIS Chat, and any future channel use the same decisioning and execution model.
- **Not** a single daemon (today): the “contract” is the **documented API surface** and the config/scripts that implement it. A future Gateway (e.g. WebSocket) could implement this contract as a single service.

---

## 2. Contract surface (conceptual)

| Operation | Description | Current implementation | Config / script |
|-----------|-------------|-------------------------|------------------|
| **Route request** | Given character, difficulty, request_type → tier, compute_multiplier, rate_tier, run_as. | Request-tier router. | `request_tier_router.py`; `config/character_cluster_request_tiers.json`. |
| **List sessions** | List active JARVIS/character sessions (e.g. Master Chat, per-CA sessions). | Cursor/JARVIS chat sessions; no single “list” API yet. | `config/jarvis_master_chat_cursor_config.json`; future: session tools. |
| **Send to session** | Send a message or task to another session (e.g. “delegate to Mace”). | Routing via request_tier; no explicit “send to session” yet. | Future: `sessions_send`-style tool. |
| **Run tool** | Execute a tool (MCP, script, or CA action) in the context of a session/character. | MCP tools, Cursor commands, scripts. | `config/homelab_mcp_hybrid_config.json`; `.cursor/commands/`; scripts. |

---

## 3. Who uses the contract

- **JARVIS**: Primary orchestrator; routes requests, coordinates characters, uses tiers and homelab ecosystem. Config: `jarvis_lumina_homelab_connection.json`, `unified_ca_peak_spec.json`, `character_cluster_request_tiers.json`.
- **CAs (Kilo Code, Cline, Continue, Roo)**: Consume same tiers, rules, and config; JARVIS is the PA/orchestrator face. Config: `unified_ca_peak_spec.json`, `ca_pa_ide_framework_alignment.json`.
- **Future channels** (e.g. Slack, Teams): Would go through the same “route request” and “run tool” contract; session list/send when implemented.

---

## 4. Config as contract

- **Route request**: `config/character_cluster_request_tiers.json` — request_type → boon/bane/neutral, tier, compute_multiplier, rate_tier, run_as, escalate_to.
- **JARVIS / Homelab**: `config/jarvis_lumina_homelab_connection.json` — JARVIS role, connection into Lumina and Homelab.
- **Unified CA**: `config/unified_ca_peak_spec.json` — CAs share framework; JARVIS chat and all CAs use same contract.
- **SSOT**: `config/lumina_ssot_registry.json` — Project backbone; control plane operates within and across it.

---

## 5. Session tools (implemented)

- **List sessions**: `sessions_list` — `python scripts/python/session_tools.py list`; discover master + data/agent_sessions.
- **Send to session**: `sessions_send` — `python scripts/python/session_tools.py send "message" [--agent-id delegate] [--reply-back]`; append to master session.
- **Session history**: `sessions_history` — `python scripts/python/session_tools.py history [session_id]`; fetch transcript/summary.

Script: `scripts/python/session_tools.py`. Part of the control plane contract.

---

## 6. One-line summary

The **control plane contract** is: route request (request_tier_router + character_cluster_request_tiers), list/send/history sessions (future), run tool (MCP, commands, scripts). JARVIS and all CAs use the same config and contract; one brain, many faces.

---

## References

- `config/jarvis_lumina_homelab_connection.json`
- `config/unified_ca_peak_spec.json`
- `config/character_cluster_request_tiers.json`
- `config/per_session_tool_allowlists.json` — per-character tool allowlist/denylist
- `scripts/python/request_tier_router.py`
- `scripts/python/session_tools.py` — sessions_list, sessions_history, sessions_send
- `docs/system/TRIGGER_CONTRACT.md` — cron, webhook, pub/sub
- `docs/system/JARVIS_LUMINA_HOMELAB_CONNECTION.md`
- `docs/system/UNIFIED_CA_PEAK_SPEC.md`
