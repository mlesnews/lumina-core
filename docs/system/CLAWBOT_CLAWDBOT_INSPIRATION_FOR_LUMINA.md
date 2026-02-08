# Clawbot / ClawDBot inspiration for Project Lumina

**Purpose**: Document what of **Clawbot** (or **ClawDBot**) we use as inspiration — logic that is **applicable**, **actionable**, and **viable** for Project Lumina.

**Last updated**: 2026-01-31
**Tags**: `@JARVIS` `#inspiration` `#attribution`

---

## What “Clawbot” refers to in this repo

1. **ClawDBot** – Database management and automation assistant under `jarvis/agents/coding-assistants/clawdbot`. Integrated with JARVIS: model routing (ULTRON primary, KAIJU fallback), MCP (database-connector, monitoring), Iron Legion agents (R2-D2 data, K-2SO optimization). See `jarvis/agents/coding-assistants/clawdbot/README.md` and `ACCREDITATION.md`.
2. **Cline** – Coding assistant (CA) extension; sometimes pronounced or recalled as “Clawbot.” Treated in Lumina as one **face** of the unified CA (@PEAK). See `config/unified_ca_peak_spec.json`, `docs/system/UNIFIED_CA_PEAK_SPEC.md`.
3. **Agent attribution** – Referenced in `config/marvin_intelligence_tasks.json` (e.g. “Investigate Clawdbot or other agent attribution” for RR tasks).

### OpenClaw (external — not our ClawDBot)

**[OpenClaw](https://github.com/openclaw/openclaw)** is a separate, external open-source project: “Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞” ([openclaw.ai](https://openclaw.ai)). It provides a **personal AI assistant** you run on your own devices: multi-channel inbox (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, BlueBubbles, Microsoft Teams, Matrix, Zalo, WebChat), local-first **Gateway** control plane (WebSocket), Voice Wake + Talk Mode, Live Canvas (A2UI), skills registry (ClawHub), agent workspace, and companion apps (macOS, iOS, Android). MIT license. Not the same as our **ClawDBot** (in-repo database assistant). If we ever reference “personal AI assistant” architecture (gateway, channels, skills), OpenClaw is a useful external reference; our **ClawDBot** remains the in-repo **database** specialist.

**What we can learn from OpenClaw (open source)** — new features, enhancements, @PEAK logic, process: **`docs/system/WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE.md`**.

---

## What we use from ClawDBot as inspiration for Lumina (applicable, actionable, viable)

| Inspiration | Applicable / actionable / viable use in Lumina |
|-------------|--------------------------------------------------|
| **Specialized-assistant pattern** | One focused capability surface (e.g. DB: schema, query, pipeline) with clear entry points. **Lumina**: Request-type → character/tier routing (`character_cluster_request_tiers.json`, `request_tier_router.py`), boons/banes, escalate_to. Same idea: match request to the right “specialist” (Tony, Mace, Marvin, JARVIS). |
| **Model routing (primary + fallback)** | ClawDBot: ULTRON primary, KAIJU fallback. **Lumina**: Tier 1/2/3, compute_multiplier, rate_tier; `ip_character_cluster_tiers.json`, `compute_tier_balance_by_persona.json`. One-shot delegation when bane → re-route to first `escalate_to` character. |
| **Config-driven integration** | ClawDBotConfig: enabled, primary_model, fallback_model, databases, mcp_servers. **Lumina**: All behavior driven by config (character_cluster_request_tiers, vectors_and_scalars, unified_ca_peak_spec, jarvis_lumina_homelab_connection). Scripts read config as contract; no hardcoded routing. |
| **MCP + agent assignment** | ClawDBot: MCP servers (database-connector, monitoring) and Iron Legion agents (R2-D2, K-2SO). **Lumina**: MCP in unified CA and NAS services; characters (Tony, Mace, Gandalf, Marvin, JARVIS) as virtual clusters with boons/banes and escalate_to for handoff. |
| **Clear capability surface** | ClawDBot: `analyze_schema`, `optimize_query`, etc. **Lumina**: request_type (e.g. code_generation, review, long_form_compliance_docs) mapped to boon/bane/neutral; router returns tier, compute_multiplier, rate_tier, run_as. Same idea: explicit capabilities and a single “run as X” outcome. |

---

## What we use from Cline (if “Clawbot” meant Cline)

- **Unified CA @PEAK**: Cline is one face of the same framework — same tiers, IP characters, context, rules, decisioning. See `config/unified_ca_peak_spec.json` (cas_unified.cline), `docs/system/UNIFIED_CA_PEAK_SPEC.md`.
- **Shared config loader (target)**: One loader for tiers, endpoints, rules used by Kilo Code, Cline, Continue, Roo. Cline consumes the same contract as other CAs. See `docs/system/CONNECT_THE_DOTS_IMPLEMENTATION_ACTION.md` Phase 2.

---

## One-line summary

**ClawDBot**: We use its **specialized-assistant pattern**, **model primary/fallback**, **config-driven integration**, **MCP + agent assignment**, and **clear capability surface** as inspiration for Lumina’s request→tier/character routing, one-shot delegation, and unified CA. **Cline** (if that’s what “Clawbot” referred to): We use it as one face of the unified CA with shared tiers, rules, and config.

---

## First-Level Jedi Council perspective on ClawDBot

Whether **ClawDBot (C-L-A-W-D-B-O-T)** should be implemented or expanded in Lumina: **`docs/system/JEDI_COUNCIL_LEVEL_ZERO_PERSPECTIVE_CLAWDBOT.md`**. Council (Tony, Mace, Gandalf) verdict: **Implement** within defined scope (database management and automation); wire into request-tier/delegation; keep scope and attribution clear; use as pattern for other domain specialists.

---

## References

- `jarvis/agents/coding-assistants/clawdbot/README.md`, `ACCREDITATION.md`
- `config/character_cluster_request_tiers.json`, `config/unified_ca_peak_spec.json`
- `scripts/python/request_tier_router.py`
- `docs/system/CONNECT_THE_DOTS_IMPLEMENTATION_ACTION.md`, `docs/system/UNIFIED_CA_PEAK_SPEC.md`
- `docs/system/JEDI_COUNCIL_LEVEL_ZERO_PERSPECTIVE_CLAWDBOT.md` (JC perspective on ClawDBot)
- `config/marvin_intelligence_tasks.json` (Clawdbot/agent attribution)
- **External**: [OpenClaw](https://github.com/openclaw/openclaw) — personal AI assistant (gateway, multi-channel, voice, canvas, skills); [openclaw.ai](https://openclaw.ai). Not our ClawDBot.
