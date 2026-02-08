# Main Goal: Local AI Clusters Online and Active

**Date**: 2026-01-30  
**Priority**: **#1** — Everything else supports this.

---

## Why this is the main goal

**Every AI token request to the cloud is burning money.** Getting local AI clusters online and active is the way to stop that. To do it we need:

1. **A working Lumina extension** — so the IDE (Cursor) and our tooling are integrated, visible, and reliable.
2. **Our superagent JARVIS** — so requests are routed to local clusters (ULTRON, Iron Legion/KAIJU) first, with cloud only as fallback.

---

## What “local AI clusters” means

| Cluster | Endpoint | Role |
|---------|----------|------|
| **ULTRON** | `http://localhost:11434` (laptop Ollama) | Default local; fast coding on this machine. |
| **ULTRON_72B** | `http://localhost:11434` | Heavier tasks, same machine. |
| **Iron Legion** (KAIJU) | `http://10.17.17.11:11434` (Kaiju_no_8 desktop) | When desktop is on; more capacity. |

When both are online and Cursor/JARVIS use them, **we don’t pay per token** for those requests. Cloud is fallback only.

---

## What we need to get there

### 1. Working Lumina extension

- **What**: Lumina Core extension (vscode-extensions/lumina-core) built, installed in Cursor, and active.
- **Why**: Gives us status, queue, workflow, and integration surfaces in the IDE so we can see and control what’s happening.
- **How**: BDA (Build, Deploy, Activate). See [LUMINA_EXTENSION_BDA.md](LUMINA_EXTENSION_BDA.md).
- **Check**: Extension shows in Cursor; commands/features work; no “depends on unknown extension” or load errors.

### 2. Superagent JARVIS

- **What**: JARVIS as the layer that routes AI token requests to local clusters first (ULTRON, KAIJU), then cloud only if needed.
- **Why**: Without this, Cursor/IDE may still hit cloud by default; with it, local-first is enforced and we stop burning money on every request.
- **Where**: Cursor model selection (ULTRON, Iron Legion in settings); Lumina `ai_connection.py` (prefer_local, ULTRON/KAIJU); configs: `config/cursor_ultron_model_config.json`, `config/cluster_endpoint_registry.json`, `.vscode/settings.json` (custom models).
- **Check**: Cursor shows ULTRON and Iron Legion; default is ULTRON (or Iron Legion when chosen); requests go to local endpoints when clusters are up.

### 3. Clusters actually online

- **ULTRON (laptop)**: Ollama running on this machine (`http://localhost:11434/api/tags`). See [CURSOR_LOCAL_AI_FIX_CHECKLIST.md](CURSOR_LOCAL_AI_FIX_CHECKLIST.md).
- **Iron Legion (Kaiju)**: Kaiju_no_8 powered, Ollama (or cluster) running at `10.17.17.11:11434` (or :11437 per config). See [PRE_REBOOT_CHECKLIST_2026-01-29.md](PRE_REBOOT_CHECKLIST_2026-01-29.md).

---

## Order of operations

1. **Lumina extension working** — BDA, reload Cursor, confirm extension loads and works.
2. **Cursor pointed at local models** — ULTRON and Iron Legion in model selector; default = ULTRON (or local).
3. **Clusters online** — Ollama on laptop; Ollama/cluster on Kaiju if you want Iron Legion.
4. **JARVIS/superagent** — Local-first routing in place (Cursor settings + any JARVIS orchestration that routes token requests). Verify requests hit local endpoints when clusters are up.

---

## Success

- **Main goal achieved when**: Most AI token requests from Cursor/IDE go to ULTRON or Iron Legion; cloud is used only when local is down or explicitly chosen. Money burn from token requests drops.
- **Dependencies**: Working Lumina extension + JARVIS (routing/orchestration) + clusters online. All three are required.

---

## Links

- [CURSOR_LOCAL_AI_FIX_CHECKLIST.md](CURSOR_LOCAL_AI_FIX_CHECKLIST.md) — Fix and verify Cursor + local AI.
- [LUMINA_EXTENSION_BDA.md](LUMINA_EXTENSION_BDA.md) — Build, deploy, activate Lumina extension.
- [PRE_REBOOT_CHECKLIST_2026-01-29.md](PRE_REBOOT_CHECKLIST_2026-01-29.md) — Pre/post reboot checks for clusters and Cursor.
- [ROADMAP_WHERE_WE_ARE_2026-01.md](ROADMAP_WHERE_WE_ARE_2026-01.md) — Where we are / been / going (this is the top priority there).
