# OpenClaw unique features and Lumina fit

**Purpose**: Explore **which parts of OpenClaw we can take inspiration from** and **which will work with Project Lumina** — unique features and functionality, mapped to inspiration potential and compatibility.

**Related**: [WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE](WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE.md), [CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA](CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA.md), [RAPID report](../../data/syphon_intelligence/intelligence_report_20260201_openclaw_clawdbot.md)

**Last updated**: 2026-02-01
**Tags**: `@JARVIS` `@PEAK` `#inspiration` `#open_source` `#fit` `#Bones` `#Star_Trek`

---

## Naming: Bones (Lumina doctor / health-check)

The Lumina health-check tool (one command to verify config, bindings, keybindings, JARVIS connectivity) is themed after **Star Trek doctors**:

- **Primary**: **Bones** (Dr. Leonard McCoy, TOS) — the default persona for “is my Lumina setup healthy?”
- **Option / alternative**: Alternate Trek doctors (e.g. EMH, Bashir, Crusher, Phlox) can be offered as a configurable option so users can pick their preferred doctor persona for the same health-check behavior.

Scripts and config can use the internal name **Bones** (or `bones`) for the health-check; docs may say “Bones (Lumina doctor)” for clarity. See `docs/god_loop_tos_crew_reference.md` and `scripts/python/BONES_COMMAND_SYSTEM.md` for existing Bones/doctor references in Lumina.

---

## 1. Unique features: inspiration vs Lumina fit

| OpenClaw feature | What it is | Inspiration for Lumina? | Works with Lumina? | Notes |
|------------------|------------|--------------------------|--------------------|--------|
| **Gateway (single control plane)** | One WebSocket (ws://127.0.0.1:18789) for sessions, channels, tools, events. | ✅ Yes — “one brain, many faces” aligns with JARVIS + @PEAK. | ✅ Yes | We have JARVIS + `jarvis_lumina_homelab_connection.json`; making the **control plane contract** explicit (route, list sessions, send to session, run tool) would strengthen @PEAK. |
| **Multi-channel inbox** | WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams, Matrix, Zalo, WebChat. | ⚠️ Conditional — only if we add non-IDE channels. | ⚠️ Later | Lumina today is **IDE-first** (Cursor, JARVIS Chat). If we ever expose JARVIS on Slack/Teams/etc., OpenClaw’s channel config, activation modes, and pairing are the reference. |
| **Skills registry (ClawHub)** | Searchable, installable skills; agent can discover and pull skills. | ✅ Yes — we have `.cursor/skills` and rules; a **single registry contract** (discover, install, gate) would unify. | ✅ Yes | **Implemented**: `config/lumina_skills_registry.json` + `scripts/python/lumina_skills_registry.py` (list, discover, check). |
| **Agent-to-agent session tools** | `sessions_list`, `sessions_history`, `sessions_send` — coordinate across sessions without switching chat. | ✅ Yes — “delegate to Mace” as **messaging** the delegated session + reply-back. | ✅ Yes | **Implemented**: `scripts/python/session_tools.py` — list, history, send (with --reply-back). |
| **Onboarding wizard** | `openclaw onboard --install-daemon` — gateway, workspace, channels, skills in one flow. | ✅ Yes — **Lumina onboard**: one CLI that sets workspace, Cursor/JARVIS config, keybindings, JARVIS pin, optional MCP/SSOT. | ✅ Yes | Reduces “where do I start?”; automation-first. |
| **Voice Wake + Talk Mode** | Always-on speech (macOS/iOS/Android), ElevenLabs, push-to-talk. | ⚠️ Inspiration — we have F23 → @JARVIS + Voice in Cursor QOL. | ⚠️ Partial | Extending to “always-on” or desktop overlay would be a new surface; current fit is IDE hotkey + voice input. |
| **Live Canvas (A2UI)** | Agent-driven visual workspace on macOS; push/reset, eval, snapshot. | ⚠️ Inspiration — different paradigm (visual canvas vs IDE chat). | ❌ Not yet | No Lumina canvas today; could inspire a future “JARVIS whiteboard” or diagram surface if we add one. |
| **Browser control (CDP)** | Dedicated Chrome/Chromium, snapshots, actions, profiles. | ⚠️ Inspiration — we have MCP browser tools (cursor-ide-browser). | ✅ Yes | MCP already gives browser; OpenClaw’s **managed profile + CDP** could inspire a more controlled “JARVIS browser” for automation. |
| **Nodes (device actions)** | Camera, screen record, location.get, system.run/notify on macOS/iOS/Android. | ⚠️ Inspiration — device-as-node is outside current Lumina scope (IDE + homelab). | ❌ Not yet | If we add “JARVIS on phone” or device nodes, OpenClaw’s node.invoke and permission model are the reference. |
| **Cron + webhooks + Gmail Pub/Sub** | Time-based and event-based triggers. | ✅ Yes — we have NAS KRON, Syphon, workflows; **explicit trigger contract** (cron, webhook, pub/sub) could unify. | ✅ Yes | **Implemented**: `docs/system/TRIGGER_CONTRACT.md` — cron, webhook, pub/sub; refs lumina_scheduled_tasks, syphon_scheduled_sources, n8n. |
| **Doctor / health check** | `openclaw doctor` — misconfig, risky DM policy, migrations. | ✅ Yes — we have pre-commit, validators; **Bones** (Star Trek TOS doctor) is our health-check: config, bindings, keybindings, JARVIS connectivity. Alternate Trek doctors (EMH, Bashir, Crusher, Phlox) as configurable option. | ✅ Yes | Single command: “is my Lumina setup healthy?” |
| **DM pairing by default** | Unknown senders get pairing code; approve before processing. | ✅ Already aligned — Iron Curtain, deny-all, mandatory auth. | ✅ Yes | We don’t copy their old defaults; we already do “secure by default.” |
| **Sandbox per session** | Non-main sessions (e.g. groups) run in Docker with tool allowlist/denylist. | ✅ Yes — **per-character or per-session tool allowlists** (e.g. Marvin = read/review only; JARVIS = full). | ✅ Yes | **Implemented**: `config/per_session_tool_allowlists.json` — per-character allowlist/denylist. |
| **Model failover + auth rotation** | OAuth vs API keys, fallbacks, documented. | ✅ Yes — we have tier fallback; document **auth profile rotation** (when/how to rotate tokens) in @PEAK config. | ✅ Yes | Operational resilience. |
| **Config as single contract** | `openclaw.json` + full config reference; every feature has a key. | ✅ Yes — we already do this (CURSOR_IDE_QOL_INDEX, registries); **lesson**: every new feature ships with config key + doc. | ✅ Yes | Keep one configuration reference. |

---

## 2. What “works with Lumina” means here

- **✅ Yes**: Fits current architecture (JARVIS, @PEAK, Cursor, homelab); we can implement or extend without a paradigm shift.
- **⚠️ Partial / Later / Conditional**: Either we have a subset (e.g. voice only in IDE), or it only applies if we add a new surface (e.g. multi-channel, device nodes).
- **❌ Not yet**: No corresponding surface or priority in Lumina today; inspiration only for future work.

---

## 3. Top picks for Lumina (high inspiration + high fit)

1. **Single control plane contract** — Explicit “route request / list sessions / send to session / run tool” API so all CAs and JARVIS go through one brain. Strengthens @PEAK.
2. **Skills registry** — One discover/install/gate path for skills; first-class, auditable. Complements `.cursor/skills` and rules.
3. **Agent-to-agent session tools** — `sessions_list`, `sessions_send`, reply-back so delegation to Mace (or another character) is observable and completable.
4. **Lumina onboard wizard** — One CLI: config check → keybindings → JARVIS pin → router test → optional MCP. Wizard-first setup.
5. **Bones** (Lumina doctor) — One command to check config, bindings, keybindings, JARVIS connectivity; catch drift and misconfig. Themed after Star Trek TOS Bones (McCoy); alternate Trek doctors (EMH, Bashir, Crusher, Phlox) as option.
6. **Per-session / per-character tool allowlists** — Marvin = read/review only; JARVIS = full set. Tool safety as config.
7. **Cron/webhook/pub-sub as explicit trigger contract** — Align with automation_first; one entry for “run on schedule” and “run on event.”

---

## 4. Unique OpenClaw functionality we’re not adopting (and why)

| OpenClaw | Why not (for now) |
|----------|--------------------|
| **0.0.0.0 / no-auth defaults** | We already enforce loopback + mandatory auth (Iron Curtain). We learn from their failure; we don’t copy those defaults. |
| **Many messaging channels as primary** | Lumina is IDE-first; multi-channel is “later” if we expose JARVIS on Slack/Teams/etc. |
| **Canvas (A2UI)** | No Lumina canvas surface yet; inspiration for a future visual workspace if we add one. |
| **Device nodes (iOS/Android)** | Out of scope for current Lumina (IDE + homelab); reference for future “JARVIS on device.” |

---

## 5. One-line summary

**Inspiration**: Gateway-as-contract, skills registry, session tools, onboarding wizard, Bones (doctor/health-check), per-session tool allowlists, and trigger contract (cron/webhook/pub-sub) all map well to Lumina. **Fit**: All of the above work with current Lumina architecture; Voice/Canvas/Nodes are partial or future. We adopt patterns and security lessons, not OpenClaw’s historical binding or auth defaults.

---

## References

- [OpenClaw](https://github.com/openclaw/openclaw) — “Your own personal AI assistant. Any OS. Any Platform. The lobster way.” ([openclaw.ai](https://openclaw.ai), [docs.openclaw.ai](https://docs.openclaw.ai))
- [WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE](WHAT_WE_CAN_LEARN_FROM_OPENCLAW_OPEN_SOURCE.md) — New features, enhancements, @PEAK, security
- [CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA](CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA.md) — In-repo ClawDBot vs external OpenClaw
- [RAPID intelligence report](../../data/syphon_intelligence/intelligence_report_20260201_openclaw_clawdbot.md) — Source triage and pattern decomposition
- `config/jarvis_lumina_homelab_connection.json`, `config/unified_ca_peak_spec.json`
