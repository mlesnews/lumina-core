# Unified CA @PEAK spec – Cline, Continue, Roo, and all CAs mashed into one

**Purpose**: **Kilo Code**, **Cline**, **Continue**, **Roo**, and **all other CAs** mashed into **one unified experience**. All **@PEAK** features and functionality preserved; all **shared commonality** united.

**Config**: `config/unified_ca_peak_spec.json`  
**Tag**: `@PEAK`  
**Last updated**: 2026-01-31  
**Related**: [ca_pa_ide_framework_alignment](config/ca_pa_ide_framework_alignment.json), [KILO_CODE_CLUSTER_PER_MODEL_SETUP](KILO_CODE_CLUSTER_PER_MODEL_SETUP.md), [JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE](JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md)

---

## Game plan

**One AI, many faces.** All CAs (Kilo Code, Cline, Continue, Roo, etc.) present **one unified interface**: same tiers, IP characters, rules, decisioning, context. Each CA is a **face** of the same framework.

---

## CAs unified (mashed into one)

| CA | Priority | Role | Config | Features contributed |
|----|----------|------|--------|----------------------|
| **Kilo Code** | 1 | primary | kilo_code_optimized_config, cluster_profiles | peak_patterns, r5_integration, inline_completion, chat_assistant, code_actions, refactoring, documentation, testing |
| **Continue** | 2 | secondary | continue_mcp_config | inline_completion, chat_assistant, code_actions |
| **Cline** | 3 | secondary | cline_mcp_config | chat_assistant, code_actions |
| **Roo** | 4 | secondary | roo_config (add when available) | TBD; align to shared_commonality and @PEAK |
| **GitHub Copilot** | 5 | standby | — | inline_completion, chat_assistant (cloud; approval required) |
| **AWS CodeWhisperer** | 6 | standby | — | inline_completion, chat_assistant (cloud; approval required) |

**Roo**: Add `config/roo_config.json` and extension IDs when available; align to shared_commonality and peak_features.

---

## Shared commonality (united across all CAs)

Apply the **same** to Kilo Code, Cline, Continue, Roo, and any other CA:

| Area | Source | Apply |
|------|--------|--------|
| **Tiers & IP characters** | ip_character_cluster_tiers.json | Tier 1/2/3 and JARVIS, Tony, Mace, Gandalf, Marvin per model. Set in each CA profile. |
| **Context window** | kilo_code_cluster_profiles.json | 16384 (T1), 32768 (T2), 65536/131072 (T3). Set same in each CA. |
| **Endpoints** | host_identity_registry.json | Ultron: http://localhost:11434; Iron Legion: http://10.17.17.11:11434. Same base URL per CA. |
| **Decisioning chain** | ip_character_cluster_tiers.json | SYPHON → data vs Information → R5 → Local → JC (3) → Extended (5) → JHC (9) → @BT/@SENATE → Cloud. Cloud only with R5 + AIQ + JHC approval. |
| **Rules** | .kilocode/rules/ | no_secrets_broadcast.md, secrets.md, ticket_number_syntax.md. Apply across all CAs/IDEs. |
| **Cloud policy** | — | Tier 2 = free cloud OK; Tier 3 = premium or local 72B; cloud use requires approval. |
| **Compute balance** | compute_tier_balance_by_persona.json | Min/max/optimal share per character; use for routing. |
| **Request tiers** | character_cluster_request_tiers.json | Difficulty + boons/banes → tier, compute_multiplier, rate_tier. |

---

## @PEAK features preserved

All @PEAK features and functionality apply to the **unified** CA experience:

| @PEAK quality | Meaning | Apply |
|---------------|---------|--------|
| **Full context first** | No jump-in fix; gather context, then act. | Every CA uses R5/Living Context and workspace context; escalation when context is low. |
| **Efficiency optimization** | Optimal model selection, latency minimization. | Task-aware routing; local preferred; streaming; minimal round-trips. Same across CAs. |
| **Pattern extraction** | @PEAK patterns; nutrient-dense solutions. | Responses favor reusable patterns; R5 aggregates; nutrient-dense next steps. Kilo Code peak_patterns; extend to others where supported. |
| **Quality standards** | @v3 / MARVIN verification; no secrets; confirm dangerous actions. | Same rules in all CAs; verification for high-impact actions. |
| **Assimilation + optimization** | @SYPHON gathers; @PEAK optimizes. | Unified CA can trigger SYPHON; responses optimized for clarity and actionability. |
| **Resource / performance** | Measure, monitor; low overhead; adaptive. | Lightweight UI; optional performance tracking; smart caching. |

---

## Single unified interface principle

- **One framework**: Tiers, IP characters, context window, endpoints, decisioning chain, rules — **same everywhere**.
- **One API contract**: Local LLM (Ollama-compatible); same model IDs and context per tier.
- **Many faces**: Kilo Code, Cline, Continue, Roo are **faces** of the same AI; choose by IDE or preference; behaviour aligned.
- **JARVIS chat**: The JARVIS-to-human interface (customized chat UI/UX) uses the **same** framework; see [JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE](JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md).

---

## How to apply (per CA)

1. **Kilo Code**: Already aligned via cluster_profiles and kilo_code_optimized_config; keep as primary.
2. **Continue**: Point models to same endpoints (Ultron, Iron Legion); set context_window per model from cluster_profiles; apply rules (no-secrets, etc.) in Continue config.
3. **Cline**: Same as Continue — same endpoints, context_window, rules.
4. **Roo**: When config exists, add roo_config.json with same endpoints, context_window, tiers, and rules; add to multi_ide_optimal_settings and recommended_extensions.
5. **Cloud CAs** (GitHub Copilot, CodeWhisperer): Use only with R5 + AIQ + JHC approval; same decisioning chain.

---

## References

- **Unified spec**: `config/unified_ca_peak_spec.json`
- **Framework alignment**: `config/ca_pa_ide_framework_alignment.json`
- **CA registry**: `config/coding_assistants_registry.json`
- **Multi-IDE**: `config/multi_ide_optimal_settings.json`
- **Kilo Code**: `config/kilo_code_cluster_profiles.json`, `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **IP character tiers**: `config/ip_character_cluster_tiers.json`
- **JARVIS chat expectation**: `docs/system/JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`
