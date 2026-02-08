# Psychological profiles blackbox – @TRIAGE @BAU @DOIT

**Purpose**: AI keeps **blackboxed psychological profiles** on **everyone and everything**, as applicable by **scope** and **scale**. Profiles are used only for **@TRIAGE**, **@BAU**, and **@DOIT**; never exposed raw.

**Config**: `config/psychological_profiles_blackbox_policy.json`  
**Tags**: `@TRIAGE` `@BAU` `@DOIT`  
**Last updated**: 2026-01-31

---

## Policy

- **Principle**: AI maintains psychological profiles (traits, tendencies, behavioral cues, boons/banes, triage/bau/doit hints) on characters, personas, digital employees, users (anonymized), systems, and tickets/requests — **as applicable by scope and scale**.
- **Blackbox rule**: Profiles are **internal-only**. No raw export to users or external systems. Use only for:
  - **@TRIAGE**: priority sorting and resource allocation
  - **@BAU**: business-as-usual routing and standard change
  - **@DOIT**: post-approval execution (executor choice, tier, rate)

---

## Scope and scale

| Entity type        | Scope                                      | Scale    | Use |
|--------------------|--------------------------------------------|----------|-----|
| **Character**      | JARVIS, Tony, Mace, Gandalf, Marvin        | **Full** | Request routing, tier/rate, boons/banes |
| **Persona**        | @samantha, @gene, @ava, @marcus, @elena    | **Full** | Assignment, triage, BAU |
| **Digital employee** | Droid actors, C3PO, R2-D2, etc.         | Standard | Routing, BAU |
| **User**           | Anonymized/pseudonymized only               | **Minimal** | Triage/BAU hints only; no PII |
| **System**         | Syphon, R5, NAS, services                   | Standard | Triage, DOIT (which system handles) |
| **Ticket/request** | PM/C/T, changes, requests                  | Minimal  | TRIAGE vs BAU, priority_class |

- **Full**: traits, tendencies, behavioral_cues, boons_banes, triage_hints, bau_hints, doit_hints, personality_variants, shifts_drifts.
- **Standard**: traits_summary, tendencies, triage_hints, bau_hints, doit_hints.
- **Minimal**: identifier + triage_hints + bau_hints + doit_hints only.

---

## @TRIAGE

**Purpose**: Prioritization under resource constraints (from `config/shortag_registry.json`).

**Use profiles for**:

1. **Match request/ticket to character or persona** by boons/banes and tendencies (e.g. Tony for code, Mace for review).
2. **Decide TRIAGE vs BAU**: critical/high threat or customer-impact → @TRIAGE (CAB or higher); low/medium → @BAU (Change Manager or self). Profile hints (escalate_if, priority_class) feed this.
3. **Allocate resources**: use triage_hints (priority_class, resource_preference, escalate_if) to assign tier and agent.

**References**: `docs/CHANGE_MANAGEMENT_REVIEW_CA_PA_IDE_JARVIS_CHAT_SEGMENT.md`, `config/character_cluster_request_tiers.json`.

---

## @BAU

**Purpose**: Business as usual; standard change; low/medium threat and customer-impact.

**Use profiles for**:

1. **Route BAU work** to the correct character/persona using bau_hints (standard_flow, self_approve_if, handoff_to).
2. **Avoid over-escalation**: use profile to keep work in BAU when appropriate (e.g. bane_match → consider handoff_to instead of escalating to TRIAGE).

**References**: `docs/system/JARVIS_TRIAGE_BAU_PRIORITIZATION.md`, `docs/CHANGE_MANAGEMENT_REVIEW_CA_PA_IDE_JARVIS_CHAT_SEGMENT.md`.

---

## @DOIT

**Purpose**: Execute action immediately; post-approval execution (from `config/core_definitions/DOIT.json`).

**Use profiles for**:

1. **Apply doit_hints** (execute_after, validate_before, rate_tier) when executing.
2. **Choose executor** (character/model) and compute tier from profile and `config/character_cluster_request_tiers.json` → request_character_rates.

**References**: `config/ip_character_cluster_tiers.json` → r5_decisioning_escalation_chain, `config/character_cluster_request_tiers.json`.

---

## Blackbox enforcement

- **No raw export**: Full psychological profiles must not be returned to users, logs, or external APIs.
- **Allowed outputs**: Routing decisions, tier/rate assignments, priority_class, escalate_to recommendations, aggregate or anonymized stats.
- **Storage**: If a dedicated profile store exists, it must be access-controlled. Referenced configs hold structure and policy only; user-level psychological content stays internal/blackboxed.

---

## References

- **Policy config**: `config/psychological_profiles_blackbox_policy.json`
- **Character tiers / boons-banes**: `config/ip_character_cluster_tiers.json`, `config/character_cluster_request_tiers.json`
- **Personas**: `config/ai_ml_team.json`, `config/compute_tier_balance_by_persona.json`
- **Tags**: `config/shortag_registry.json` (@TRIAGE), `config/core_definitions/DOIT.json` (@DOIT)
- **TRIAGE vs BAU**: `docs/CHANGE_MANAGEMENT_REVIEW_CA_PA_IDE_JARVIS_CHAT_SEGMENT.md`
