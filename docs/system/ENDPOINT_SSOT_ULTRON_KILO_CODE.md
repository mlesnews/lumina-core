# Endpoint SSOT: Ultron (Laptop) and Kilo Code

**Purpose**: Single reference for Ultron (laptop local Ollama) and Kilo Code–relevant endpoints. Use when configuring Kilo Code, Cursor, or any CA for local Ollama.  
**Last updated**: 2026-01-30

---

## Ultron (Laptop Local)

| Service | Port | URL | Use |
|---------|------|-----|-----|
| **Ollama** | **11434** | http://localhost:11434 | Default Ollama; use for Kilo Code, Cursor ULTRON, any local LLM |
| Router (optional) | 8080 | http://localhost:8080 | Cursor cluster face if used |
| MCP / WS | 11437 | ws://localhost:11437, http://localhost:11437 | MCP toolkit; **not** Ollama |

**Critical**: On the laptop, **Ollama is 11434 only**. Port **11437** is MCP/WS, not Ollama. Do not point Kilo Code or Cursor at localhost:11437 for Ollama.

---

## Iron Legion (Kaiju Desktop)

| Service | Host | Port | URL |
|---------|------|------|-----|
| Ollama | 10.17.17.11 | 11434 or 11437 | http://10.17.17.11:11434 or :11437 per Kaiju config |

Confirm on Kaiju which port Ollama uses (11434 vs 11437). See `docs/system/PRE_REBOOT_CHECKLIST_2026-01-29.md`.

---

## Kilo Code

- **Kilo Code** uses its **own settings** (gear in Kilo Code panel). Set API profile base URL to **http://localhost:11434** (or http://localhost:11434/v1) for Ultron.
- **Repo** `config/kilo_code_optimized_config.json`: `primary_llm.base_url` = http://localhost:11434 (for tooling/consistency).
- **Using as a cluster (multiple LLMs)**: Create multiple API profiles (e.g. ULTRON = localhost:11434, Iron Legion = 10.17.17.11:11434 or gateway :3000), or point one profile at a router. See **`docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md` §9**.

---

## SSOT Sources

- `config/host_identity_registry.json` – ultron.primary = http://localhost:11434
- `config/cluster_endpoint_registry.json` – ultron_cluster, iron_legion
- `docs/helpdesk/KILO_CODE_ULTRON_INVESTIGATION_BRIEF.md` – acceptance criteria and done-right state
- `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md` – user-facing fix steps

---

**Reference**: `config/host_identity_registry.json`, `.cursor/memories/host_identity_kaiju_nas_critical.md`, `docs/helpdesk/CURSOR_LOCAL_AI_INVESTIGATION_BRIEF.md`.
