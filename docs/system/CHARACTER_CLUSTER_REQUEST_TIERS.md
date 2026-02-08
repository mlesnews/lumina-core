# Character cluster and request-tier rates

**Purpose**: Each **character** has many **personas**, **personality variants**, and **shifts-drifts** virtually assigned as a **custom-built cluster** for that character. **Request difficulty** (easy / moderate / specialized / critical) plus **character boons/banes** drive **tier**, **compute**, and **rates**.

**Config**: `config/character_cluster_request_tiers.json`  
**Related**: `config/ip_character_cluster_tiers.json`, `config/compute_tier_balance_by_persona.json`, `config/kilo_code_cluster_profiles.json`  
**Last updated**: 2026-01-31

---

## Character = custom-built virtual cluster

A character (e.g. **Tony Stark**) is not a single model; they are a **virtual cluster** of:

- **Personas**: AI-ML team personas that can “wear” that character (e.g. @gene, @marcus for Tony).
- **Personality variants**: builder, experimenter, architect, rapid_iterator.
- **Shifts**: 1st shift CCM, Cursor primary.
- **Drifts**: when another persona bleeds in (e.g. @samantha review bleed, or escalation to orchestrator).

The **virtual_cluster_id** (e.g. `tony_stark_cluster`) is the logical set of models/profiles that embody that character across those personas and shifts. Routing and capacity use this cluster.

---

## How hard is the request? How much compute?

**Request difficulty** (from config → `request_difficulty_levels`):

| Level        | Default tier | Compute hint | Typical tokens | Rate tier |
|-------------|--------------|--------------|----------------|-----------|
| **Easy**     | 1            | low          | 1k–8k          | standard  |
| **Moderate**| 2            | medium      | 8k–32k         | standard  |
| **Specialized** | 2        | medium_high | 16k–64k        | premium   |
| **Critical**| 3            | high         | 32k–128k       | premium   |

**Character boons/banes** then adjust:

- **Boon match**: request type aligns with character strengths → **same or lower tier**, **lower compute multiplier**.
- **Bane match**: request type aligns with character weaknesses → **same tier but higher compute** or **escalate** to another character / Tier 3.
- **Neutral**: use default tier and compute for that difficulty.

So: **how hard** = request_difficulty; **how much compute** = tier + compute_multiplier from the (character, difficulty, boon|bane|neutral) table.

---

## Tony Stark: boons/banes and rates (full example)

**Boons** (Tony matches well; use Tier 2, often lower compute):

- code_generation, debug, refactor, rapid_prototype, architect_single_domain, experimentation, iteration

**Banes** (Tony matches poorly; escalate or heavier compute):

- long_form_compliance_docs, heavy_process_governance, multi_team_consensus, formal_legal_review, pure_review_only_no_code

**Rates / tiers (Tony):**

| Request difficulty | Boon match | Neutral | Bane match |
|--------------------|------------|---------|------------|
| **Easy**            | Tier 2, 0.7× compute, standard | Tier 2, 1.0×, standard | Tier 2, 1.2×, escalate to Mace/Gandalf |
| **Moderate**       | Tier 2, 1.0×, standard (ideal Tony) | Tier 2, 1.0×, standard | Tier 2, 1.3×, consider Mace/Gandalf |
| **Specialized**    | Tier 2, 1.2×, premium (32B/codellama) | Tier 2, 1.2×, premium | **Tier 3**, 1.5×, escalate to JARVIS/Mace/Gandalf |
| **Critical**       | Tier 3, 1.5×, escalate to JARVIS | Tier 3, 1.5×, JARVIS | Tier 3, 2.0×, do not keep on Tony; JARVIS |

So:

- **Easy request + boon** (e.g. “quick refactor”) → **Tier 2**, **0.7× compute**, **standard rate**.
- **Specialized request + bane** (e.g. “long compliance doc”) → **Tier 3** or hand to **Mace/Gandalf/JARVIS**, **1.5× compute**, **premium rate** if Tony must handle.

---

## Usage

1. **Classify request**: difficulty (easy/moderate/specialized/critical) + request_type (map to boons/banes/neutral).
2. **Pick character**: e.g. Tony for code/architect; Mace for review; Gandalf for planning; Marvin for quick review; JARVIS for critical/orchestration.
3. **Look up (character, difficulty, boon|bane|neutral)** in `request_character_rates` → tier, compute_multiplier, rate_tier, optional escalate_to.
4. **Route**: use that tier and virtual cluster (models from `character_virtual_clusters`); apply compute_multiplier to budget/cost.

---

## References

- **IP character tiers**: `config/ip_character_cluster_tiers.json`
- **Compute balance**: `config/compute_tier_balance_by_persona.json`, `docs/system/COMPUTE_TIER_BALANCE_BY_PERSONA.md`
- **Kilo Code profiles**: `config/kilo_code_cluster_profiles.json`
- **Personas**: `config/ai_ml_team.json`
