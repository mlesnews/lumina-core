# What we can learn from OpenClaw (open source)

**Purpose**: Capture what Lumina can learn from **[OpenClaw](https://github.com/openclaw/openclaw)** (open-source personal AI assistant, formerly Clawdbot/Moltbot) — new features, enhancements to existing ones, improved @PEAK logic, and the way we do business. OpenClaw is MIT-licensed; we can study its design and adopt patterns where applicable.

**Last updated**: 2026-01-31
**Tags**: `@JARVIS` `@PEAK` `#inspiration` `#open_source`
**Related**: [CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA](CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA.md), [OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT](OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT.md) (explore which parts inspire vs work with Lumina), [PROJECT_IRON_CURTAIN_IMPLEMENTATION_PLAN](../security/PROJECT_IRON_CURTAIN_IMPLEMENTATION_PLAN.md), [CONNECT_THE_DOTS_IMPLEMENTATION_ACTION](CONNECT_THE_DOTS_IMPLEMENTATION_ACTION.md)

---

## 1. New features we could create (inspired by OpenClaw)

| OpenClaw concept | What we could build in Lumina |
|------------------|-------------------------------|
| **Skills registry (ClawHub)** | A **Lumina skills registry**: searchable, installable skills (e.g. `SKILL.md` under a canonical path). Agent or user can discover and pull skills on demand; gating for install. Complements existing `.cursor/skills` and agent skills; could unify under one registry contract. |
| **Agent-to-agent session tools** | OpenClaw has `sessions_list`, `sessions_history`, `sessions_send` (coordinate across sessions without switching chat). We have JARVIS Master Chat and agent coordination; we could add **explicit session tools**: list active JARVIS/character sessions, send a message to another session, request reply-back. Makes “delegate to Mace” not just routing but **messaging** the delegated session. |
| **Onboarding wizard** | OpenClaw: `openclaw onboard --install-daemon` walks through gateway, workspace, channels, skills. We could add **Lumina onboard**: one CLI wizard that sets up workspace root, Cursor/JARVIS config, request-tier router, keybindings, JARVIS pin, and optional MCP/SSOT. Single path for “new user” or “new machine.” |
| **Channel / group activation modes** | OpenClaw: per-channel activation (mention vs always), queue modes, reply-back. If we ever expose JARVIS on multiple channels (Slack, Teams, etc.), we could adopt **activation modes** and **allowlist/ pairing** (we already have DM pairing in Iron Curtain mindset) so each channel has explicit rules. |

---

## 2. Enhancements to existing Lumina features

| Existing Lumina | OpenClaw-inspired enhancement |
|-----------------|------------------------------|
| **Request-tier router** | **Session-aware routing**: route not only by character/difficulty/request_type but by **session** (e.g. “this session is Mace-led” or “this channel is support-only”). OpenClaw’s session model (main vs group vs channel) could inform our session metadata in JARVIS Master Chat. |
| **JARVIS Master Chat** | **Reply-back and queue modes**: OpenClaw has reply-back ping-pong and queue modes for multi-session work. We could add “reply to session X when done” or “queue this for JARVIS and notify when complete” so delegation (e.g. to Mace) has a clear handback. |
| **Unified CA @PEAK** | **Model failover + auth rotation**: OpenClaw documents model failover and OAuth vs API-key rotation. We have tier fallback; we could document **auth profile rotation** (e.g. when to rotate HuggingFace/Anthropic tokens, how JWT fits in) and make it part of @PEAK config. |
| **MCP + Iron Legion** | **Tool allowlist per session**: OpenClaw sandboxes non-main sessions (allowlist bash, read, write; denylist browser, nodes, cron). We could define **per-character or per-session tool allowlists** (e.g. Marvin gets only read/review tools; JARVIS gets full set) so @PEAK logic includes “who can call what.” |

---

## 3. Improved @PEAK logic and “the way we do business”

| Area | What we can learn from OpenClaw |
|------|---------------------------------|
| **Single control plane** | OpenClaw: one Gateway (WebSocket) for sessions, channels, tools, events. We have JARVIS as orchestrator and `jarvis_lumina_homelab_connection.json` as contract. We could make the **control plane contract** explicit: one entry point for “route request,” “list sessions,” “send to session,” “run tool” — and all CAs/channels go through it. That’s @PEAK: one brain, many faces. |
| **Config as contract** | OpenClaw: `openclaw.json` and full config reference. We already do config-as-contract (character_cluster_request_tiers, unified_ca_peak_spec, etc.). **Lesson**: keep a single **configuration reference** (we have CURSOR_IDE_QOL_INDEX and registry); ensure every new feature ships with a config key and doc. |
| **Wizard-first setup** | OpenClaw pushes `openclaw onboard` as the main path. We have many scripts and docs; we could add **one “Lumina onboard”** (or “JARVIS setup”) that chains: config check → keybinding fix → JARVIS pin → router test → optional MCP. Reduces “where do I start?” and aligns with “one path first.” |
| **Security by default** | OpenClaw’s failure (0.0.0.0, no auth, trustedProxies) taught the world. We already encode **loopback-only, mandatory auth, Tailscale/tunnel** in Project Iron Curtain and identity rules. **Lesson**: every new service or gateway in Lumina must default to **deny-all + loopback**; remote only via tunnel + auth. That’s how we do business. |
| **Skills as first-class** | OpenClaw: skills in workspace, ClawHub for discovery. We have `.cursor/skills` and rules. **Lesson**: treat **skills** as first-class: one registry, one install flow, one “agent can pull skill” contract. Improves @PEAK by making “add capability” a single, auditable path. |

---

## 4. Security and operational learnings (cross-reference)

| Learning | Where we already do it | OpenClaw lesson |
|----------|------------------------|------------------|
| **Loopback-only binding** | Project Iron Curtain, `audit_service_bindings.py`, identity_protection_rebranding.mdc | OpenClaw’s default 0.0.0.0 led to mass exposure. We black-hole 18789 and enforce 127.0.0.1/::1 for internal gateways. |
| **Mandatory auth** | Iron Curtain “MAA” (JWT, zero-trust defaults) | OpenClaw had zero-auth defaults; we mandate auth before service startup and Deny All by default. |
| **Remote via tunnel only** | Tailscale/Cloudflare Tunnel in identity and Iron Curtain | OpenClaw’s reverse-proxy localhost trust caused bypass. We broker remote only via Tailscale/tunnel with auth. |
| **Rootless / least privilege** | Iron Curtain Phase 3 (rootless Docker, read-only mounts, capability dropping) | OpenClaw containers gave root on host; we enforce rootless and least privilege for agents. |

So: we **don’t** copy OpenClaw’s defaults; we **learn** from their failure and double down on our existing policies (see [PROJECT_IRON_CURTAIN_IMPLEMENTATION_PLAN](../security/PROJECT_IRON_CURTAIN_IMPLEMENTATION_PLAN.md)).

---

## 5. Summary: what we can learn

- **New features**: Skills registry (ClawHub-style), agent-to-agent session tools (sessions_list / sessions_send), Lumina onboarding wizard, channel/group activation modes if we go multi-channel.
- **Enhancements**: Session-aware routing, reply-back/queue for JARVIS Master Chat, model failover + auth rotation in @PEAK, per-session/per-character tool allowlists.
- **@PEAK / process**: Single control plane contract, config-as-contract + single config reference, wizard-first setup (“Lumina onboard”), security-by-default (loopback, deny-all, tunnel-only remote), skills as first-class.
- **Security**: We already encode the right lessons in Iron Curtain; OpenClaw’s public failure reinforces our loopback-only, mandatory auth, and tunnel-only remote access.

**One line**: OpenClaw (open source) inspires us to add a **skills registry**, **session-level tools** for delegation and reply-back, a **Lumina onboard** wizard, and **session-aware routing**; to make the **control plane contract** and **security defaults** explicit; and to keep treating **config and skills** as first-class. We do **not** copy their binding or auth defaults — we learn from their failure and keep our own.

---

## References

- [OpenClaw](https://github.com/openclaw/openclaw) — “Your own personal AI assistant. Any OS. Any Platform. The lobster way.” ([openclaw.ai](https://openclaw.ai))
- `docs/system/CLAWBOT_CLAWDBOT_INSPIRATION_FOR_LUMINA.md` — ClawDBot (in-repo) vs OpenClaw (external)
- `docs/security/PROJECT_IRON_CURTAIN_IMPLEMENTATION_PLAN.md` — Security learnings (Clawdbot/Moltbot failure analysis)
- `docs/system/CONNECT_THE_DOTS_IMPLEMENTATION_ACTION.md` — Request → tier → CA → JARVIS flow
- `config/jarvis_lumina_homelab_connection.json`, `config/unified_ca_peak_spec.json`
