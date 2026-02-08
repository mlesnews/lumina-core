# Vectors and scalars

**Purpose**: Define **vectors** (multi-dimensional) and **scalars** (single values) used for triage, routing, compute balance, and DOIT across the ecosystem.

**Config**: `config/vectors_and_scalars.json`  
**Last updated**: 2026-01-31

---

## Vectors (multi-dimensional)

| Vector | Dimensions | Use |
|--------|------------|-----|
| **request_vector** | difficulty, request_type, threat, customer_impact, context_size | Match to character; drive tier and compute. |
| **character_vector** | tier, boons_match, banes_match, persona_ids, orchestration_rank | Compare with request for routing and request_character_rates. |
| **profile_vector** | traits_summary, tendencies, triage_hints, bau_hints, doit_hints | @TRIAGE @BAU @DOIT (blackboxed). |
| **triage_vector** | priority_class, resource_preference, escalate_if, triage_vs_bau | Triage output; feeds BAU and DOIT. |
| **compute_budget_vector** | min_pct, max_pct, optimal_pct, current_usage_pct | Balance and capacity; components are scalars. |

---

## Scalars (single values)

| Scalar | Type | Range/values | Use |
|--------|------|--------------|-----|
| **tier** | integer | 1–3 | Model/compute tier. |
| **optimal_pct** | number | percent; sum = 100 over characters | Target compute share. |
| **min_pct** | number | percent | Floor for compute share. |
| **max_pct** | number | percent | Cap for compute share. |
| **compute_multiplier** | number | e.g. 0.7, 1.0, 1.5 | Per-request compute scaling. |
| **rate_tier** | string | standard \| premium | Cost/billing tier. |
| **priority_class** | string | critical \| important \| can_wait \| skip | Triage priority. |
| **scale** | string | minimal \| standard \| full | Profile depth. |

---

## Usage

- **Routing**: Match **request_vector** to **character_vector** (boons/banes, tier); output **tier**, **compute_multiplier**, **rate_tier** (scalars).
- **Balance**: Use **optimal_pct**, **min_pct**, **max_pct** per character; aggregate as **compute_budget_vector** for dashboards.
- **Triage**: Input **request_vector** + **profile_vector** → output **triage_vector**; scalars **priority_class** and **triage_vs_bau** drive @TRIAGE vs @BAU.
- **DOIT**: Scalars **tier**, **compute_multiplier**, **rate_tier** from request_character_rates; **doit_hints** from profile_vector.

---

## References

- **Compute balance**: `config/compute_tier_balance_by_persona.json`
- **Request tiers / boons-banes**: `config/character_cluster_request_tiers.json`
- **Psychological profiles**: `config/psychological_profiles_blackbox_policy.json`
- **IP character tiers**: `config/ip_character_cluster_tiers.json`
