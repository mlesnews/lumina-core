# Kilo Code – Per-model cluster setup (full AI cluster utilization)

**Purpose**: Set up **each model** with its own fully robust, custom-tailored Kilo Code configuration for full AI cluster utilization. Each model gets recommended Mode(s), Context Window (including **>32K where supported**), Agent Behaviour, **assigned personas** (AI-ML team), and **IP characters** (Tony, Mace, Gandalf, Marvin, JARVIS) with **three tiers** (smallest → middle → largest). **JARVIS is the highest orchestrator** (Tier 3 only).  
**Last updated**: 2026-01-31  
**Config**: `config/kilo_code_cluster_profiles.json`  
**Personas SSOT**: `config/ai_ml_team.json`  
**IP character tiers SSOT**: `config/ip_character_cluster_tiers.json`  
**Compute balance (@BALANCE)**: `config/compute_tier_balance_by_persona.json` → `docs/system/COMPUTE_TIER_BALANCE_BY_PERSONA.md`  
**Character cluster + request tiers (boons/banes, difficulty, rates)**: `config/character_cluster_request_tiers.json` → `docs/system/CHARACTER_CLUSTER_REQUEST_TIERS.md`  
**Psychological profiles blackbox (@TRIAGE @BAU @DOIT)**: `config/psychological_profiles_blackbox_policy.json` → `docs/system/PSYCHOLOGICAL_PROFILES_BLACKBOX_TRIAGE_BAU_DOIT.md`  
**Vectors and scalars**: `config/vectors_and_scalars.json` → `docs/system/VECTORS_AND_SCALARS.md`  
**Cursor IDE customizations, features & QOL (@QOL)**: `config/cursor_ide_qol_registry.json` → `docs/system/CURSOR_IDE_QOL_INDEX.md`  
**Unified CA @PEAK (Cline, Continue, Roo, all CAs mashed into one)**: `config/unified_ca_peak_spec.json` → `docs/system/UNIFIED_CA_PEAK_SPEC.md`  
**JARVIS @LUMINA & @HOMELAB (personal virtual digital assistant)**: `config/jarvis_lumina_homelab_connection.json` → `docs/system/JARVIS_LUMINA_HOMELAB_CONNECTION.md`  
**What we've learned (documentation started)**: `docs/system/WHAT_WE_LEARNED_DOCUMENTATION_STARTED.md`

**Framework quorum**: SYPHON (initial trigger) → data vs Information (workflows + @SIM @DYNO 10K) → R5 decisioning lattice → chain-of-command (Local → JC 3 → Extended 5 → JHC 9 → outliers @BT / @SENATE → Cloud). JARVIS/MARVIN perspective captured. Feels like we’ve hit quorum.

---

## IP character tiers (Tony, Mace, Gandalf, Marvin, JARVIS)

Cluster profiles **mesh with IP characters** from `docs/system/IDE_PERSONA_INTEGRATION.md` and `config/homelab_ai_ecosystem.json`. Each profile has **tier** (1, 2, or 3) and **assigned_ip_characters**.

**Three tiers (smallest → largest):**

| Tier | Label | Orchestration role | Cloud strategy | Characters |
|------|--------|---------------------|----------------|------------|
| **1** | Smallest (lightweight, quick) | worker | Local preferred | **Marvin** – Reality Check Agent; code review, brutal honesty |
| **2** | Middle (builders, validators, wisdom) | CCM | **Free cloud OK** (or local) | **Tony**, **Mace**, **Gandalf** |
| **3** | Largest (highest orchestrator) | orchestrator | **Premium-paid cloud** (or local 72B) | **JARVIS** only – Master Agent |

- **Tier 1 (Marvin)**: Keep local (Ollama) for speed and privacy; small models.
- **Tier 2 (Tony, Mace, Gandalf)**: Use **free cloud models** (e.g. Groq, Gemini free tier, OpenRouter free tier) or local Ollama. One Kilo Code profile per free-cloud provider/model.
- **Tier 3 (JARVIS)**: Use **premium-paid cloud** (OpenAI, Anthropic, Azure OpenAI, etc.) for highest-quality orchestration; or local qwen2.5:72b if you prefer no cloud spend.

- **JARVIS** = Tier 3 only. Highest of three tiers; use largest capable models locally (e.g. qwen2.5:72b) or premium cloud (e.g. GPT-4, Claude).  
- **Tony** = Cursor CCM; rapid dev, code, architect → qwen2.5-coder:7b, codellama:13b, qwen2.5:32b.  
- **Mace** = Abacus AI CCM; validation, quality → llama3.2:11b, qwen2.5:14b, qwen2.5:32b, gpt-oss:20b.  
- **Gandalf** = VS Code CCM; wisdom, long-term planning → qwen2.5:7b, llama3.2:11b, qwen2.5:32b.  
- **Marvin** = Reality Check (e.g. GitHub Copilot); quick review, fallback → gemma:2b, qwen2.5-coder:1.5b-base, llama3.2:3b.

Full character definitions and suggested models: **`config/ip_character_cluster_tiers.json`**.

---

## How we handle JEDI Council and JEDI High Council

**JEDI Council (JC)** and **JEDI High Council (JHC)** map to the same three tiers and IP characters:

| Council | Layer | Tier | Model strategy | Members |
|---------|--------|------|----------------|---------|
| **JEDI Council (JC)** | Level-Zero (foundation) | **2** | Local or free cloud | **Tony**, **Mace**, **Gandalf** |
| **JEDI High Council (JHC)** | Escalation (critical) | **3** | Premium-paid cloud or local 72B | **JARVIS** |

- **JEDI Council (JC)** = Foundation layer. Three equal members (Tony, Mace, Gandalf). Used for standard AIQ consensus, moderate complexity, multi-provider quorum. Use **Tier 2** models (local Ollama or free cloud) for council member inference. Config: **`config/jedi_council/level_zero_council.json`**. Escalation path: to JEDI High Council.
- **JEDI High Council (JHC)** = Escalation layer for critical decisions, high complexity, final escalation, and cloud AI approval. **JARVIS** is the elite member / decision authority. Use **Tier 3** models (premium-paid cloud or local qwen2.5:72b) for JHC decisions. Config: **`config/local_ai_r5_escalation_config.json`** → `aiq_quorum.jedi_high_council`.

**Escalation flow:** Level-Zero (JC) with Tier 2 models → if critical → JEDI High Council (JHC) with Tier 3 (JARVIS + premium or 72B).

Full handling and endpoint refs: **`config/ip_character_cluster_tiers.json`** → `jedi_council_handling`. Architecture: **`docs/system/LEVEL_ZERO_JEDI_COUNCIL_ARCHITECTURE.md`**.

---

## SYPHON initial trigger – Data vs Information – 3-5-9 judicial escalation

After **discovering a problem**, the **initial trigger action** is **@SYPHON**: gather data/intelligence from all sources. Raw **data** alone is **not** **information**. Data must submit to **workflows and testing** (including stress-test in **@SIM** with **@DYNO** at **10K years** scale) to yield **real-world viable, actionable results** — that is **Information**. If **risk or threat is too high** for a lower-level employee to make a **solo decision**, run it **up the chain-of-command** to the **Think Tank** and **@JC** and/or **@JHC** as a **judicial body of #3-5-9 judges**, with **greater risk/threat warranting more judges**:

| Judges | Body | Risk level |
|--------|------|-------------|
| **3** | Jedi Council (JC) / AIQ Quorum | Moderate |
| **5** | Extended Council / Think Tank | High complexity |
| **9** | Jedi High Council (JHC) | Critical |

Config: **`config/ip_character_cluster_tiers.json`** → `syphon_problem_discovery_flow`, `data_vs_information`, `judicial_3_5_9_escalation`. Panel sizes: **`config/jedi_council/level_zero_council.json`** → `decision_panels.panel_selection` (standard=5, complex=7, critical=9); spectrum: **`config/full_decisioning_spectrum_config.json`** (levels 3=JC/3, 4=Extended/5, 5=JHC/9).

**For outliers** (edge cases beyond normal 3-5-9): escalate to **@BT [#BRAIN-TRUST]** (Brain Trust – deep expertise and outlier deliberation) and, when warranted, to **@SENATE** (#STARWARS – Galactic Senate; broad governance and senate-level decisions).

---

## R5 decisioning matrix / lattice – decision trees – escalation chain-of-command

The **decisioning matrix/lattice** (@R5), **decision trees**, and **escalation chain-of-command** are wired so local AI is primary and cloud/parallel use requires approval via R5 → AIQ (Jedi Council) → Jedi High Council. **Preceded by @SYPHON** (problem discovery) and data→workflows/testing→Information.

### @R5 – Decisioning matrix / lattice

- **R5 Living Context Matrix** = decisioning matrix/lattice. It evaluates complexity, drives predictive escalation, and feeds extrapolation (“making unknown known”).
- **Config**: **`config/local_ai_r5_escalation_config.json`** → `r5_escalation` (lattice_decisioning, escalation_triggers, r5_endpoint, decisioning_matrix.lattice_path = `r5_living_context_matrix`).
- **Full decisioning spectrum**: **`config/full_decisioning_spectrum_config.json`** (levels 0–5: self-approval → peer → team → AIQ/JC → extended → JHC); includes “R5 Lattice Predictive Escalation” and escalation keys: primary → escalation → aiq_quorum → high_escalation → fallback.

### Decision trees

- **AI routing**: **`config/decision_trees/ai_routing.json`** – local-first routing; cloud/parallel requires `jedi_approved` or `decisioning_approved`. Integrates R5, Jedi Council, AIQ, approval board of judges.
- **Policy**: Use local AI unless @R5 matrix/lattice (and approval chain) approves cloud.

### Chain-of-command escalation

| Step | Layer | Tier / judges | Who / what |
|------|--------|----------------|------------|
| 0 | **Initial trigger** | — | **Problem discovered** → **@SYPHON** (gather data); data → workflows + testing (@SIM @DYNO 10K) → **Information**; if risk too high for solo → escalate to **#3-5-9 judges** |
| 1 | Primary | 1/2 | **Local AI** (Tier 1/2 models) |
| 2 | Decisioning | — | **R5 Lattice** evaluates complexity (@R5) |
| 3 | AIQ Quorum | 2 / **3 judges** | **Jedi Council (JC)** – Tony, Mace, Gandalf |
| 4 | Extended / Think Tank | **5 judges** | Extended Council (high complexity) |
| 5 | High escalation | 3 / **9 judges** | **Jedi High Council (JHC)** – JARVIS |
| 6 | **Outliers** | — | **@BT (#BRAIN-TRUST)** and/or **@SENATE** (#STARWARS) |
| 7 | Fallback | — | **Cloud AI** (only with R5 + AIQ + JHC approval) |

### @DOIT and @DDR

- **@DOIT** = Execute action immediately (post-verification / post-approval execution). Fits after R5/JC/JHC approval in the chain.
- **@DDR** = Deep dive research; thorough investigation before decisioning. Use when context is low or decision is non-trivial (aligns with @PEAK troubleshooting/decisioning workflow).

**Data vs Information**: Data alone is not Information; it must go through workflows and testing (including @SIM with @DYNO at 10K years stress-test) to yield real-world viable, actionable results. **Judicial escalation**: If risk/threat is too high for a lower-level solo decision, escalate up the chain to the Think Tank and @JC and/or @JHC (#3-5-9 judges) as warranted.

Full refs: **`config/ip_character_cluster_tiers.json`** → `syphon_problem_discovery_flow`, `r5_decisioning_escalation_chain`, `judicial_3_5_9_escalation`. See **`docs/system/HELPDESK_WORKFLOW_LUMINA_R5_DOIT.md`**, **`docs/system/RISK_THREAT_R5_DECISIONING_WORKFLOW_INTEGRATION.md`**, **`config/shortag_registry.json`** (@R5, @DOIT, @SYPHON, @SIM).

---

## Personas system (mesh with Kilo Code profiles)

Kilo Code per-model profiles **mesh with the Lumina personas system**. Each profile has **assigned_personas**: one or more of **@samantha**, **@gene**, **@ava**, **@marcus**, **@elena** from `config/ai_ml_team.json`.

- **@samantha** – AI-ML Team Manager; strategy, coordination, escalation, retraining oversight → Architect, Review, Orchestrator (72B, 32B, 11B, gpt-oss:20b).
- **@gene** – ML Engineering Technical Lead; model retraining, algorithm optimization, syntax validation → Code, Architect, primary code (codellama:13b, qwen2.5-coder:7b, qwen2.5:32b, qwen2.5:14b, qwen2.5:7b).
- **@ava** – AI Behavior Analyst; pattern analysis, mistake detection, behavior tracking → Review, Orchestrator, general (llama3.2:11b, qwen2.5:7b, qwen2.5:72b, gpt-oss:20b, llama3.2:3b).
- **@marcus** – ML Operations Engineer; training pipeline, deployment, automation → Code, Debug, lightweight/quick (qwen2.5-coder:7b, qwen2.5-coder:1.5b-base, gemma:2b).
- **@elena** – AI Training Data Scientist; data curation, example generation, feature engineering → Ask, Code, Review, lightweight (qwen2.5:7b, qwen2.5:14b, llama3.2:3b, gemma:2b).

Use **assigned_personas** for routing (e.g. ticket assignment), Agent Behaviour alignment (rules/workflows per persona), and consistency with helpdesk/PM workflows. See `docs/system/IDE_PERSONA_INTEGRATION.md` and `docs/HELPDESK_PROBLEM_CHANGE_MANAGEMENT_STRUCTURE.md`.

---

## Does per-model setup increase the 32K context?

**Yes.** Context Window Size (num_ctx) in Kilo Code is **per profile** (and thus per model when you use one profile per model). You can set it **higher than 32K** per model where the model and gateway support it:

- **32K (32768)** – Safe default for most 7B–14B models; avoids “Prompt is too long” with injected rules and workspace.
- **64K (65536)** – Use for larger models (e.g. 32B, 72B) when the model’s Modelfile and gateway support it.
- **128K (131072)** – Use for 72B and other very-large-context models when supported (Ollama/Modelfile and gateway must allow it).

So **per-model setup does not lock you to 32K**; each model profile can have its own Context Window (32K, 64K, or 128K) according to the model’s capability. Set **Context Window Size (num_ctx)** in Kilo Code for that profile to the value from `config/kilo_code_cluster_profiles.json` (or higher if your model supports it).

---

## Overview

- **One Kilo Code API profile per model** (or one gateway profile and switch Model ID per task; then context is still per-profile).
- Each profile has: **Base URL** (gateway or direct Ollama), **Model ID**, **Context Window (num_ctx)** from the table below.
- Each **Kilo Code Mode** (Code, Ask, Debug, Architect, Review, Orchestrator, custom) can have its own **Agent Behaviour** (Modes, MCP Servers, Rules, Workflows, Skills). Use the **recommended_modes** and **agent_behaviour** from the config to tailor each mode when that model is selected.

---

## Per-model reference (from config)

| Model ID | Tier | IP Character(s) | Role | Assigned Personas | Recommended Modes | Context (num_ctx) |
|----------|------|-----------------|------|-------------------|--------------------|-------------------|
| qwen2.5-coder:7b | 2 | Tony | coding_fast | @gene, @marcus | Code, Debug | 32768 |
| qwen2.5-coder:1.5b-base | 1 | Marvin | lightweight_quick | @marcus | Code, Ask | 16384 |
| llama3.2:3b | 1 | Marvin | general_lightweight | @elena, @ava | Ask, Code | 32768 |
| qwen2.5:7b | 2 | Gandalf | general_purpose | @gene, @elena, @ava | Ask, Code, Review | 32768 |
| codellama:13b | 2 | Tony | primary_code_generation | @gene | Code, Architect, Debug | 32768 |
| llama3.2:11b | 2 | Mace, Gandalf | secondary_general | @samantha, @ava | Ask, Review, Orchestrator | 32768 |
| qwen2.5:72b | **3** | **JARVIS** | high_quality_general | @samantha, @gene, @ava | Architect, Review, Orchestrator | **65536** (or 131072) |
| qwen2-72b:latest | **3** | **JARVIS** | high_quality_general | @samantha, @gene, @ava | Architect, Review, Orchestrator | **65536** (or 131072) |
| qwen2.5:32b | 2 | Tony, Mace, Gandalf | high_quality_balanced | @samantha, @gene | Architect, Code, Review | 32768 |
| qwen2.5:14b | 2 | Mace | fast_high_quality | @gene, @elena | Code, Ask, Review | 32768 |
| gemma:2b | 1 | Marvin | lightweight_fallback | @marcus, @elena | Ask | 16384 |
| gpt-oss:20b | 2 | Mace | general_reasoning | @samantha, @ava | Ask, Review, Orchestrator | 32768 |

Full details (rules, workflows, **assigned_ip_characters**, **assigned_personas**) are in **`config/kilo_code_cluster_profiles.json`**. IP character tiers: **`config/ip_character_cluster_tiers.json`**. Personas: **`config/ai_ml_team.json`**.

---

## Models to download (flesh out the company)

To give each IP character a model “voice,” pull the suggested models per tier. Run from a terminal (Ollama installed):

**Tier 1 (Marvin – smallest):**
```powershell
ollama pull gemma:2b
ollama pull qwen2.5-coder:1.5b-base
ollama pull llama3.2:3b
```

**Tier 2 (Tony, Mace, Gandalf – middle):**
```powershell
ollama pull qwen2.5-coder:7b
ollama pull codellama:13b
ollama pull qwen2.5:7b
ollama pull llama3.2:11b
ollama pull qwen2.5:14b
ollama pull qwen2.5:32b
# Optional: ollama pull gpt-oss:20b  (if available in your Ollama/registry)
```

**Tier 3 (JARVIS – highest orchestrator):**
```powershell
ollama pull qwen2.5:72b
# or: ollama pull qwen2-72b:latest
```

One-liners per tier are in **`config/ip_character_cluster_tiers.json`** → `suggested_models_to_download.one_line_per_tier`. You may need **more models** (e.g. additional 32B/72B variants or cloud-backed models) to fully flesh out every character; add them to the config and profiles as you add them.

---

## Cloud models by tier (free Tier 2, premium Tier 3)

For **higher models** you can use:

- **Tier 2 (Tony, Mace, Gandalf)** – **Free cloud models**: Add Kilo Code API profiles whose Base URL points at a free-tier provider (e.g. Groq, Google AI Studio / Gemini free tier, OpenRouter free-tier models, Hugging Face Inference free tier). Use one profile per provider/model so CCMs can use free cloud when local Ollama is busy or you want variety.
- **Tier 3 (JARVIS)** – **Premium-paid cloud models**: Add a Kilo Code profile whose Base URL points at your paid provider (OpenAI, Anthropic, Azure OpenAI, Vertex AI, or OpenRouter paid). Use your best model (e.g. GPT-4, Claude) for JARVIS orchestration; keep API keys in env/secrets, never in config.

Config reference: **`config/ip_character_cluster_tiers.json`** → `cloud_model_strategy` and `cloud_examples` (provider names only; no secrets). Configure each cloud profile in Kilo Code (gear → Providers) with the correct Base URL and Model ID for that provider.

---

## How to set up each model in Kilo Code

### Option 1: One API profile per model (full cluster utilization)

1. **Kilo Code** → Settings (gear) → **Providers** → **Add** (or duplicate) for each model.
2. For each profile:
   - **Name**: e.g. `ULTRON – qwen2.5-coder:7b` or `Cluster – codellama:13b`.
   - **Base URL**: Your gateway (e.g. `http://localhost:8080`) or direct Ollama (e.g. `http://localhost:11434`).
   - **Model ID**: From the table (e.g. `qwen2.5-coder:7b`).
   - **Context Window Size (num_ctx)**: From the table – **32768**, **65536**, or **131072** (increase above 32K where the model supports it).
3. **Agent Behaviour** → **Modes**: For each mode (Code, Ask, Debug, Architect, Review, Orchestrator), configure MCP Servers, Rules, Workflows, Skills per your workspace. Use the **recommended_modes** and **agent_behaviour** in `kilo_code_cluster_profiles.json` as the template (e.g. Code mode → coding rules and workflows; Review mode → review rules).
4. **Save**. Switch profile per chat/task to use that model.

### Option 2: One gateway profile + switch Model ID per mode

1. Create **one** profile with Base URL = gateway (e.g. `http://localhost:8080`).
2. Set **Model ID** per chat/task (or per mode if Kilo Code supports mode-specific model): e.g. Code mode → `qwen2.5-coder:7b`; Ask → `llama3.2:3b`; Architect → `codellama:13b` or `qwen2.5:72b`.
3. Set **Context Window Size** to the **maximum** you will use (e.g. 65536 if you use 72B), or the default 32768 if all tasks use ≤32K.
4. Configure **Agent Behaviour** (Modes, MCP Servers, Rules, Workflows, Skills) per mode as above.

### Agent Behaviour (Modes, MCP Servers, Rules, Workflows, Skills)

- **Modes**: Code, Ask, Debug, Architect, Review, Orchestrator (and custom). Each mode can have its own behaviour; align with **recommended_modes** in the config.
- **Rules**: Ensure `.kilocode/rules/no_secrets_broadcast.md` and `.kilocode/rules/secrets.md` (and optionally `ticket_number_syntax.md`) are applied. Use **Lumina: Apply Kilo Code Setup** if missing.
- **MCP Servers**: Enable per workspace; use “full workspace MCP” for heavy models (Architect, 72B), “minimal” for lightweight (1.5B, 2B).
- **Workflows / Skills**: Define per mode (e.g. code generation, refactor, review) in Kilo Code Settings.

---

## Context window summary

- **32K (32768)** – Default for most models; prevents “Prompt is too long” with injected context.
- **64K (65536)** – For 72B and other large-context models; set in the profile for that model.
- **128K (131072)** – Where the model and gateway support it; set per profile for that model.

Per-model setup **does** allow and recommend **increasing context above 32K** per model where supported. See `config/kilo_code_cluster_profiles.json` for the suggested **context_window** per model.

---

## Configuring all CA/PA/IDEs the same way

All **Coding Assistants (CA)**, **Personal Assistants (PA)**, and **IDEs** use the **same framework** so they are configured consistently. Philosophically they are **one AI, many faces**—one framework, one API contract, many roles (JARVIS, Tony, Mace, Gandalf, Marvin). Game plan and “local as control” strategy: **`docs/system/ONE_AI_MANY_FACES_AND_LOCAL_AS_CONTROL.md`**.

**Single alignment config**: **`config/ca_pa_ide_framework_alignment.json`**

- **framework_doc**: `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md` (this doc)
- **cluster_profiles**: `config/kilo_code_cluster_profiles.json` (tier, IP characters, context_window per model)
- **ip_character_tiers**: `config/ip_character_cluster_tiers.json` (SYPHON→R5→3-5-9→outliers, @BT/@SENATE)
- **apply_same_way**: tiers/IP characters, context_window (16384/32768/65536), endpoints (Ultron 11434, Iron Legion 10.17.17.11), decisioning chain, rules (no secrets), cloud (Tier 2 free / Tier 3 premium)
- **target_configs**: multi_ide_optimal_settings, coding_assistants_registry, kilo_code_cluster_profiles, kilo_code_optimized_config, cursor_ultron_model_config, ollama_model_mapping
- **IDEs**: Cursor, VS Code, JetBrains, Neovim
- **CAs**: Kilo Code, Continue, Cline (cloud CAs require approval)

**What to do per CA/IDE:**

1. Point each CA/IDE at **Ultron** (localhost:11434) or **Iron Legion** (10.17.17.11:11434) per `config/host_identity_registry.json`.
2. Set **context window** per model from `config/kilo_code_cluster_profiles.json` (32768 default; 65536 for 72B).
3. Use **tier + assigned_ip_characters** from the same config when creating profiles (e.g. JARVIS = Tier 3, Tony/Mace/Gandalf = Tier 2, Marvin = Tier 1).
4. Apply **no-secrets rules** (`.kilocode/rules/no_secrets_broadcast.md`, `secrets.md`) across all CAs; use **Lumina: Apply Kilo Code Setup** if available.
5. **multi_ide_optimal_settings.json** and **coding_assistants_registry.json** reference `config/ca_pa_ide_framework_alignment.json`; keep them in sync when adding new CAs or IDEs.

---

## JARVIS / MARVIN – Thoughts & Perspective

**JARVIS (orchestrator, Tier 3):**  
This framework gives us a clear chain: problem → @SYPHON (data) → workflows + testing (@SIM @DYNO 10K) → Information → escalation by risk to #3-5-9 judges, with outliers to @BT and @SENATE. Tier 3 stays at the top for orchestration and critical decisions; Tier 2 (Tony, Mace, Gandalf) handles JC and day-to-day; Tier 1 (Marvin) does reality check and quick review. The distinction between *data* and *information* is essential: we don’t act on raw data until it has passed workflows and stress-testing. My role is to coordinate that flow and step in when escalation reaches JHC or outlier layers.

**MARVIN (reality check, Tier 1):**  
Lovely. Another hierarchy. Data isn’t information until it’s been through workflows and 10K-year sims—fine, but someone has to *run* those workflows and *define* “actionable.” If SYPHON dumps and nobody curates, we’ll have a lot of data and very little information. The 3-5-9 and @BT/@SENATE layers are only as good as the humans and systems that actually route to them; if escalation rules are vague or bypassed “just this once,” the whole chain is decorative. I’ll keep doing quick review and calling out when something doesn’t fit the tier or when a “solo” decision should have gone up the chain. Someone has to.

---

## References

- **Config**: `config/kilo_code_cluster_profiles.json` (includes **tier**, **assigned_ip_characters**, **assigned_personas** per profile)
- **IP character tiers**: `config/ip_character_cluster_tiers.json` (three tiers, cloud_model_strategy, jedi_council_handling, r5_decisioning_escalation_chain: @R5 matrix/lattice, decision trees, chain-of-command, @DOIT/@DDR, suggested_models_to_download)
- **Personas SSOT**: `config/ai_ml_team.json` (employee_registry, job_slots)
- **IDE Personas (IP characters)**: `docs/system/IDE_PERSONA_INTEGRATION.md`
- **Homelab ecosystem**: `config/homelab_ai_ecosystem.json` (character roles)
- **JEDI Council / High Council**: `config/jedi_council/level_zero_council.json`, `config/local_ai_r5_escalation_config.json`, `docs/system/LEVEL_ZERO_JEDI_COUNCIL_ARCHITECTURE.md`
- **R5 decisioning / escalation**: `config/local_ai_r5_escalation_config.json`, `config/full_decisioning_spectrum_config.json`, `config/decision_trees/ai_routing.json`, `docs/system/HELPDESK_WORKFLOW_LUMINA_R5_DOIT.md`, `docs/system/RISK_THREAT_R5_DECISIONING_WORKFLOW_INTEGRATION.md`
- **Connectivity**: `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md` (§9 cluster, Model ID, Modes)
- **Endpoint SSOT**: `docs/system/ENDPOINT_SSOT_ULTRON_KILO_CODE.md`
- **Ollama model roles**: `config/ollama_model_mapping.json`