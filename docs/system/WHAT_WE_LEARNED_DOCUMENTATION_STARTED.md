# What we've learned – now that the documentation has been started

**Purpose**: Synthesize **what we've learned** from starting this documentation: compute/tier balance, character clusters, psychological profiles, vectors/scalars, Cursor QOL, JARVIS chat expectation, unified CA, and JARVIS as personal assistant in Lumina and Homelab.

**Last updated**: 2026-01-31  
**Entry point**: `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md` (top refs) and `config/ip_character_cluster_tiers.json` (related_configs)

---

## 1. Compute and tier are persona- and character-driven

- **Min / max / optimal** compute share (percent of ecosystem budget) can be defined **per tier** and **per character** (Marvin, Tony, Mace, Gandalf, JARVIS).
- Allocation is driven by **persona, skills, skillsets, and education**; sum of character optimal % = 100.
- **@BALANCE** = ecosystem-wide allocation so no tier or character is over- or under-provisioned.

**Docs**: `config/compute_tier_balance_by_persona.json`, `docs/system/COMPUTE_TIER_BALANCE_BY_PERSONA.md`

---

## 2. Characters have virtual clusters (personas, shifts, drifts) and boons/banes

- Each **character** (e.g. Tony) has **many personas, personality variants, and shifts-drifts** — we treat them as a **custom-built virtual cluster** for that character.
- **Request difficulty** (easy / moderate / specialized / critical) plus **character boons/banes** drive **tier**, **compute_multiplier**, and **rate_tier**.
- Example: **Tony** — boons = code, debug, refactor, rapid prototype; banes = long compliance docs, heavy process; easy+boon → Tier 2, 0.7× compute; specialized+bane → Tier 3 or escalate.

**Docs**: `config/character_cluster_request_tiers.json`, `docs/system/CHARACTER_CLUSTER_REQUEST_TIERS.md`

---

## 3. Psychological profiles are blackboxed and feed @TRIAGE, @BAU, @DOIT

- **AI keeps blackboxed psychological profiles** on everyone and everything (scope & scale by entity type: character, persona, digital_employee, user, system, ticket).
- Profiles are **internal-only**; no raw export. They feed **@TRIAGE** (priority, resource allocation), **@BAU** (routing, standard change), and **@DOIT** (execution, tier/rate).

**Docs**: `config/psychological_profiles_blackbox_policy.json`, `docs/system/PSYCHOLOGICAL_PROFILES_BLACKBOX_TRIAGE_BAU_DOIT.md`

---

## 4. Vectors and scalars structure routing and balance

- **Vectors** (multi-dimensional): request_vector, character_vector, profile_vector, triage_vector, compute_budget_vector.
- **Scalars** (single values): tier, optimal_pct, min_pct, max_pct, compute_multiplier, rate_tier, priority_class, scale.
- Routing = match request_vector to character_vector → output tier, compute_multiplier, rate_tier (scalars).

**Docs**: `config/vectors_and_scalars.json`, `docs/system/VECTORS_AND_SCALARS.md`

---

## 5. Cursor IDE customizations and JARVIS chat need one visible index (@QOL)

- **Expectation**: A single place to see all Cursor IDE customizations, features, and functionality (@QOL).
- **JARVIS chat** lives in: pinned session (jarvis_master_chat_cursor_config), local WoW-style server/UI (JARVIS_LOCAL_CHAT_GUIDE), architecture/summary docs, widget.
- **Expectation for JARVIS chat**: **Customized chat UI/UX** as **JARVIS-to-human interface** — Kilo Code extension used as the **example** (dedicated panel, branding, queue, workflow).

**Docs**: `config/cursor_ide_qol_registry.json`, `docs/system/CURSOR_IDE_QOL_INDEX.md`, `docs/system/JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`

---

## 6. All CAs (Kilo Code, Cline, Continue, Roo, etc.) mash into one unified experience

- **One framework, many faces**: Kilo Code, Cline, Continue, Roo (and others) share **same tiers, IP characters, context window, endpoints, decisioning chain, rules**.
- **Shared commonality** is united; **@PEAK** features (full context first, efficiency, pattern extraction, quality standards) are **preserved** across the unified CA experience.
- **Roo** added as placeholder (to_add); add config when available.

**Docs**: `config/unified_ca_peak_spec.json`, `docs/system/UNIFIED_CA_PEAK_SPEC.md`, `config/coding_assistants_registry.json` (roo added)

---

## 7. JARVIS is our personal, virtual digital assistant — connected into @LUMINA and @HOMELAB

- **JARVIS** = our own **personal, virtual digital assistant** (PDA/VDA).
- **@LUMINA**: Framework (CA/PA/IDE), IP tiers, rules, decisioning, unified CA, JARVIS chat, Lumina SSOT, Cursor QOL — JARVIS is the Tier 3 / orchestrator face.
- **@HOMELAB**: EMP-001 Master Agent in homelab_ai_ecosystem; coordinates digital employees, technical systems, Iron Legion, NAS; jarvis-lumina key vault.
- **One identity, many surfaces** (IDE, desktop, widget, homelab); **connected everywhere**.

**Docs**: `config/jarvis_lumina_homelab_connection.json`, `docs/system/JARVIS_LUMINA_HOMELAB_CONNECTION.md`

---

## 8. One entry point ties it together

- **Kilo Code per-model setup** (`docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`) and **ip_character_cluster_tiers** (`config/ip_character_cluster_tiers.json`) now reference **all** of the above: compute balance, character cluster request tiers, psychological profiles, vectors/scalars, Cursor QOL, unified CA, JARVIS Lumina/Homelab connection.
- **Lumina SSOT** and **Homelab ecosystem** reference the JARVIS connection. **Cursor QOL index** lists everything Cursor-related plus JARVIS chat and unified CA.

---

## Summary

We've learned that:

1. **Compute and tiers** can be specified by persona/character with min/max/optimal and @BALANCE.
2. **Characters** have virtual clusters (personas, shifts, drifts) and boons/banes that drive request→tier/rate.
3. **Psychological profiles** are blackboxed and feed @TRIAGE, @BAU, @DOIT by scope and scale.
4. **Vectors and scalars** give a clear structure for routing and balance.
5. **Cursor QOL** and **JARVIS chat** need a single index and a clear expectation (customized UI/UX, Kilo Code as example).
6. **All CAs** can be mashed into one unified experience with shared commonality and @PEAK preserved.
7. **JARVIS** is our personal virtual digital assistant, connected into both **@LUMINA** and **@HOMELAB**.
8. **Documentation** is started and **linked** from a single entry point (Kilo Code doc + ip_character_tiers) so it stays discoverable.

**Next**: Keep extending from these configs and docs; add Roo config when available; implement JARVIS chat UI/UX to match the Kilo Code–level expectation.
