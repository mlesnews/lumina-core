# JARVIS – our personal, virtual digital assistant (@LUMINA & @HOMELAB)

**Purpose**: **JARVIS** is **our own personal, virtual digital assistant**. This doc describes how JARVIS is **connected into @LUMINA** and **@HOMELAB**.

**Config**: `config/jarvis_lumina_homelab_connection.json`  
**Tags**: `@LUMINA` `@HOMELAB` `@JARVIS`  
**Last updated**: 2026-01-31

---

## JARVIS role

- **Primary identity**: Our own **personal, virtual digital assistant** (PDA / VDA).
- **Aliases**: Master Agent, CTO/Superagent, Primary Orchestrator.
- **Scope**: One JARVIS across **Lumina framework** and **Homelab ecosystem** — IDE, desktop, widget, homelab.

---

## Connection into @LUMINA

JARVIS is wired into **Lumina** as follows:

| Area | Config / ref | JARVIS role |
|------|--------------|-------------|
| **Framework** | ca_pa_ide_framework_alignment.json | Tier 3 character; same framework for all CAs/PA/IDEs; primary orchestrator face. |
| **IP character tiers** | ip_character_cluster_tiers.json | JARVIS = Tier 3 only; orchestrates Tony, Mace, Gandalf, Marvin; JHC member. |
| **Rules & decisioning** | .kilocode/rules, R5, SYPHON, JC, JHC | Executes and coordinates; cloud only with R5 + AIQ + JHC approval. |
| **Unified CA @PEAK** | unified_ca_peak_spec.json | JARVIS chat and all CAs use same framework; JARVIS is the PA/orchestrator face. |
| **JARVIS chat** | jarvis_master_chat_cursor_config.json, JARVIS_CHAT_UI_UX_EXPECTATION | JARVIS-to-human interface (chat UI/UX); voice + text; IDE, desktop, widget. |
| **Lumina SSOT** | lumina_ssot_registry.json | Project backbone (extensions, Python, network drives); JARVIS operates within and across it. |
| **Cursor QOL** | cursor_ide_qol_registry.json | JARVIS chat, hotkeys (F23 → @JARVIS + Voice), footer, workflows. |

---

## Connection into @HOMELAB

JARVIS is wired into **Homelab** as follows:

| Area | Config / ref | JARVIS role |
|------|--------------|-------------|
| **Digital employees** | homelab_ai_ecosystem.json → master_agents.jarvis | EMP-001, Master Agent – Primary Orchestrator; direct_reports: Samantha, Tony, Mace, Gandalf, etc.; orchestration, workflow, escalation. |
| **Technical systems** | homelab_ai_ecosystem.json → technical_systems | R5, Syphon, NAS, MCP servers; JARVIS uses and orchestrates. |
| **Applications** | homelab_ai_ecosystem.json → applications | Cursor IDE, VS Code, n8n; JARVIS integrates via Lumina. |
| **Services** | homelab_ai_ecosystem.json → services | Ticket monitoring, syntax validation; JARVIS can trigger and monitor. |
| **Iron Legion & NAS** | host_identity_registry, cluster_endpoint_registry | Kaiju (10.17.17.11) = LLM cluster; NAS (10.17.17.32) = DSM, backups, MCP; JARVIS-aware. |
| **Key Vault & identity** | service_level_accounts, lumina_network_drives | jarvis-lumina vault; secrets for Lumina/JARVIS; no secrets in configs. |

---

## Single personal assistant principle

- **One identity**: JARVIS is the single **personal / virtual digital assistant** identity.
- **Many surfaces**: IDE chat (Cursor/VS Code), desktop app, Windows widget, local WoW-style chat, homelab orchestration.
- **One backend**: Same decisioning chain, rules, tiers, and homelab ecosystem; one API contract where applicable.
- **Connected everywhere**: **Lumina** = framework and project. **Homelab** = digital employees and infrastructure. **JARVIS** is connected into both.

---

## References

- **Connection config**: `config/jarvis_lumina_homelab_connection.json`
- **Homelab ecosystem**: `config/homelab_ai_ecosystem.json`
- **IP character tiers**: `config/ip_character_cluster_tiers.json`
- **CA/PA framework**: `config/ca_pa_ide_framework_alignment.json`
- **JARVIS chat**: `config/jarvis_master_chat_cursor_config.json`, `docs/system/JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`
- **Lumina SSOT**: `config/lumina_ssot_registry.json`
- **Unified CA**: `config/unified_ca_peak_spec.json`, `docs/system/UNIFIED_CA_PEAK_SPEC.md`
