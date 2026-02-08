# Compute tier balance by persona (@BALANCE)

**Purpose**: Define **min / max / optimal** compute share (percentage of ecosystem budget) per **tier** and per **character**, driven by **persona, skills, skillsets, and education**. Project/ecosystem-wide **@BALANCE**.

**Config**: `config/compute_tier_balance_by_persona.json`  
**Related**: `config/ip_character_cluster_tiers.json`, `config/ai_ml_team.json`, `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`  
**Last updated**: 2026-01-31

---

## @BALANCE principle

- **Ecosystem-wide**: Compute (time, token, or cost budget) is allocated so no tier or character is over- or under-provisioned relative to **role, skills, and workload**.
- **Scope**: Project-wide; applies across Lumina/Kilo Code cluster, JEDI Council, and persona-driven sessions.
- **Units**: Percent of total budget. Sum of character-level **optimal** percentages = **100**.

---

## Tier-level bands (capacity planning)

| Tier | Label              | Min % | Max % | Optimal % | Rationale                                      |
|------|--------------------|-------|-------|-----------|------------------------------------------------|
| **1** | Smallest (worker)  | 5     | 20    | **10**   | Lightweight, quick; small models, low share.   |
| **2** | Middle (CCMs)      | 50    | 80    | **65**   | Day-to-day work; bulk of compute.              |
| **3** | Orchestrator       | 10    | 40    | **25**   | Fewer, heavier calls; quality over volume.     |

Use these for **cluster sizing** and **tier caps**; character-level bands (below) drive **per-entity** targets.

---

## Character-level bands (per-persona / skills / education)

Driven by **persona**, **skillsets**, and **education/role** from `config/ip_character_cluster_tiers.json` and `config/ai_ml_team.json`.

| Character | Tier | Min % | Max % | Optimal % | Role / skillsets (summary)                          |
|-----------|------|-------|-------|-----------|-----------------------------------------------------|
| **Marvin**  | 1 | 5  | 20 | **10** | Reality check, review, ask; small models, high volume. |
| **Tony**    | 2 | 15 | 35 | **22** | Builder; code, debug, architect; primary Tier-2 share.   |
| **Mace**    | 2 | 12 | 30 | **21** | Validator; review, quality, strategic execution.         |
| **Gandalf** | 2 | 12 | 30 | **22** | Wisdom; architect, long-term planning, infrastructure.  |
| **JARVIS**  | 3 | 10 | 40 | **25** | Orchestrator; critical decisions, premium/72B.            |

**Sum optimal** = 10 + 22 + 21 + 22 + 25 = **100**.

---

## Persona → tier/character (AI-ML team)

When a **persona** is active (e.g. @samantha, @gene), their compute band is derived from the **preferred character(s)** for that persona:

| Persona    | Preferred tier | Preferred characters | Notes                          |
|------------|----------------|----------------------|--------------------------------|
| @samantha  | 2              | Mace, Gandalf        | Strategy, coordination, review |
| @gene      | 2              | Tony, Mace            | ML engineering, code           |
| @ava       | 2              | Mace, Gandalf         | Behavior analyst, review      |
| @marcus    | 2              | Tony                  | ML ops, code, debug            |
| @elena     | 1              | Marvin                | Training data, lighter models |

See `config/compute_tier_balance_by_persona.json` → `persona_to_tier_character`.

---

## Usage

- **Schedulers / routers**: Use **optimal_pct** as target and **min_pct** / **max_pct** as hard bounds when allocating budget per character or tier.
- **Dashboards**: Report actual vs optimal share per character/tier; flag when outside min/max.
- **Capacity**: Tier-level bands inform how much capacity to provision for Tier 1 vs 2 vs 3 (e.g. node mix, model availability).

---

## References

- **IP character tiers**: `config/ip_character_cluster_tiers.json`
- **Personas (AI-ML)**: `config/ai_ml_team.json`
- **Kilo Code per-model setup**: `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **Ecosystem classification**: `config/homelab_ai_ecosystem.json`
