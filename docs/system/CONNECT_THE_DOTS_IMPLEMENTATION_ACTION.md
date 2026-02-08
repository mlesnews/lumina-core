# Connect all the dots – implementation to begin. ACTION.

**Purpose**: **Connect all the dots** (documentation → implementation). **JARVIS, what would Tony do?** Tony = The Innovative Builder: rapid iteration, ship one path first, then expand. **Documentation is started; implementation to begin. ACTION.**

**Last updated**: 2026-01-31  
**Tags**: `@DOIT` `@JARVIS` `#ACTION`  
**Related**: [WHAT_WE_LEARNED_DOCUMENTATION_STARTED](WHAT_WE_LEARNED_DOCUMENTATION_STARTED.md), [KILO_CODE_CLUSTER_PER_MODEL_SETUP](KILO_CODE_CLUSTER_PER_MODEL_SETUP.md), [JARVIS_LUMINA_HOMELAB_CONNECTION](JARVIS_LUMINA_HOMELAB_CONNECTION.md)

**Implementation status**: Phase 1 ✅ DONE – `scripts/python/request_tier_router.py` ships request → tier + compute_multiplier + rate_tier (+ escalate_to). Phase 2 & 3 next.

---

## How the dots connect (one flow)

```
Request (user / ticket / task)
    │
    ▼
[request_vector: difficulty, request_type, threat, customer_impact]
    │
    ▼
[Match to character_vector: boons/banes, tier]  ← character_cluster_request_tiers.json
    │
    ▼
[tier, compute_multiplier, rate_tier]  ← scalars from request_character_rates
    │
    ├──► [@TRIAGE]  priority_class, escalate_if  ← psychological_profiles_blackbox (triage_hints)
    ├──► [@BAU]     standard_flow, handoff_to    ← psychological_profiles_blackbox (bau_hints)
    └──► [@DOIT]    execute_after, rate_tier     ← psychological_profiles_blackbox (doit_hints)
    │
    ▼
[Route to CA/model]  ← unified_ca_peak_spec (Kilo Code, Cline, Continue, Roo)
    │
    ▼
[Compute balance]  ← compute_tier_balance_by_persona (min/max/optimal % per character)
    │
    ▼
JARVIS (orchestrator / Tier 3)  ← jarvis_lumina_homelab_connection
    │
    ├──► @LUMINA   (framework, CAs, chat, SSOT, QOL)
    └──► @HOMELAB  (EMP-001, digital employees, Iron Legion, NAS)
```

**Single sentence**: Request → vector match (character + difficulty + boons/banes) → tier + compute + rate → TRIAGE/BAU/DOIT hints → route to CA → balance → JARVIS orchestrates in Lumina + Homelab.

---

## JARVIS, what would Tony do?

**Tony** = The Innovative Builder. Rapid dev, code, architect, iteration. He would:

1. **Ship one path first** – Don’t wire everything at once. Implement **one** flow: e.g. **request → character (Tony) → tier + compute_multiplier** from `character_cluster_request_tiers.json`. Prove it in code.
2. **Use the configs as contract** – Read `character_cluster_request_tiers.json`, `compute_tier_balance_by_persona.json`, `vectors_and_scalars.json` from a single **router/orchestrator** (script or service). Input = request_vector stub; output = tier, compute_multiplier, rate_tier.
3. **Wire JARVIS chat to the connection** – Ensure the JARVIS chat surface (pinned session or future custom UI) calls the same **JARVIS Lumina/Homelab** contract: `jarvis_lumina_homelab_connection.json` + homelab_ai_ecosystem (EMP-001). One identity, one backend.
4. **TRIAGE/BAU/DOIT as next slice** – After request→tier works, add **triage_hints / bau_hints / doit_hints** from psychological_profiles_blackbox (or from character configs). No raw profile export; only routing outputs.
5. **Unified CA = same config, many UIs** – Kilo Code, Cline, Continue, Roo already share framework (we documented it). Implementation: one **shared config loader** (tiers, endpoints, rules) used by each CA’s adapter or by a small gateway.
6. **Measure, then balance** – Use **compute_tier_balance_by_persona** to log actual usage per character/tier; compare to optimal_pct; adjust routing or capacity (implementation follows doc).

**Tony’s mantra**: *Documentation is started. Implementation to begin. Ship the first path. Then the next. ACTION.*

---

## Implementation action list (begin now)

### Phase 1 – First path (request → tier/rate) [Day 1–2] ✅ IMPLEMENTED

| # | Action | Config / code | Owner | Status |
|---|--------|----------------|-------|--------|
| 1 | **Implement request → character → tier + compute_multiplier** | Read `character_cluster_request_tiers.json` → `request_character_rates[character][difficulty][boon_match\|bane_match\|neutral_match]`. Input: character, difficulty, match_type. Output: tier, compute_multiplier, rate_tier. | Dev | ✅ |
| 2 | **Add a small router script or API** | `scripts/python/request_tier_router.py` – takes (character, difficulty, request_type), maps request_type to boon/bane/neutral via character_boons_banes, returns tier + compute_multiplier + rate_tier + escalate_to. | Dev | ✅ |
| 3 | **Test with Tony** | Example: character=Tony, difficulty=easy, request_type=code_generation → boon_match → tier=2, compute_multiplier=0.7, rate_tier=standard. | Dev/QA | ✅ |

**Usage**:
- `python scripts/python/request_tier_router.py Tony easy code_generation` → tier + compute + rate (+ escalate_to when set).
- **One-shot delegate**: `python scripts/python/request_tier_router.py Tony easy long_form_compliance_docs --delegate` → re-routes as first escalated character (e.g. `run_as=Mace`); one call = single "run as X" result. Use `--one-shot` as alias for `--delegate`.

### Phase 2 – JARVIS chat + Lumina/Homelab [Week 1]

| # | Action | Config / code | Owner |
|---|--------|----------------|-------|
| 4 | **Wire JARVIS chat to JARVIS Lumina/Homelab connection** | Ensure chat (pinned session or API) uses `jarvis_lumina_homelab_connection.json` and homelab EMP-001 as identity. Same backend for IDE, desktop, widget. | Dev |
| 5 | **Apply unified CA shared config** | One loader that reads tiers, endpoints, rules from `unified_ca_peak_spec.json` + `ip_character_cluster_tiers.json` + `ca_pa_ide_framework_alignment.json`; use in Kilo Code / Cline / Continue (and Roo when config exists). | Dev |
| 6 | **Cursor QOL checklist** | Run through `CURSOR_IDE_QOL_INDEX.md` checklist: settings from CURSOR_PEAK_EFFICIENCY_CONFIG, hotkeys (RAlt @DOIT, F23 @JARVIS), extensions, JARVIS pinned session. | User/Dev |

### Phase 3 – TRIAGE / BAU / DOIT and balance [Ongoing]

| # | Action | Config / code | Owner |
|---|--------|----------------|-------|
| 7 | **Add triage_hints / bau_hints / doit_hints to router** | Feed from `psychological_profiles_blackbox_policy.json` (or from character_boons_banes + request_character_rates). Output: priority_class, escalate_to, handoff_to where applicable. No raw profile export. | Dev |
| 8 | **Log usage by character/tier** | Use `compute_tier_balance_by_persona.json` (optimal_pct, min_pct, max_pct). Compare actual vs optimal; alert or adjust. | Dev/Ops |
| 9 | **JARVIS chat UI/UX (Kilo Code–level)** | When ready: dedicated JARVIS chat panel/extension using same contract; see `JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`. | Dev |

---

## Config → implementation map

| Dot (doc/config) | Implementation use |
|------------------|---------------------|
| `character_cluster_request_tiers.json` | Request → tier, compute_multiplier, rate_tier; escalate_to. |
| `compute_tier_balance_by_persona.json` | Capacity planning; usage vs optimal_pct; dashboard. |
| `psychological_profiles_blackbox_policy.json` | triage_hints, bau_hints, doit_hints (no raw export). |
| `vectors_and_scalars.json` | Schema for request_vector, character_vector; scalars = router output. |
| `unified_ca_peak_spec.json` | Shared config loader for all CAs; same tiers, rules, endpoints. |
| `jarvis_lumina_homelab_connection.json` | JARVIS identity and Lumina/Homelab entry points; chat backend. |
| `ip_character_cluster_tiers.json` | Tier 1/2/3, characters, models; source for router and CAs. |
| `cursor_ide_qol_registry.json` | Checklist and refs for Cursor + JARVIS chat. |

---

## One-line summary

**Connect the dots**: Request → (character + difficulty + boons/banes) → tier + compute + rate → TRIAGE/BAU/DOIT → route to CA → JARVIS in Lumina + Homelab. **What would Tony do?** Ship the first path (request→tier), wire JARVIS chat to the connection, then TRIAGE/BAU/DOIT and balance. **Documentation is started. Implementation to begin. ACTION.**
