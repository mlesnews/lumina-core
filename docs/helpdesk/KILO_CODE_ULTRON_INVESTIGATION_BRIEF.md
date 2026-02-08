# Kilo Code + Ultron Connectivity – Investigation Brief

**PM Ticket**: PM000003178  
**Related**: PM000003102 (Cursor + Local AI Clusters)  
**Created**: 2026-01-30  
**Status**: Open – RCA and validation per support workflow  
**Risk**: Kilo Code API requests spinning = wrong endpoint or service not running; must align configs and define done-right state.

---

## 1. Purpose

Support teams (Problem Management, QA/QC) are to **investigate** and **work** the Kilo Code + Ultron connectivity issue through the proper workflow. Do **not** treat as fixed until root cause is documented, acceptance criteria are met, and QA has validated.

---

## 2. What We Know (Facts)

### 2.1 Endpoint SSOT (Ultron = Laptop Local)

| Cluster / Service | Host | Port | URL | Use |
|-------------------|------|------|-----|-----|
| **Ultron (Ollama)** | localhost | **11434** | http://localhost:11434 | Laptop local Ollama; default for Kilo Code when using "Ultron" |
| **Ultron router** | localhost | 8080 | http://localhost:8080 | Optional; Cursor cluster face |
| **Iron Legion (Kaiju)** | 10.17.17.11 | 11434 or 11437 | http://10.17.17.11:11434 (Ollama) or :11437 (per Kaiju) | Kaiju desktop; not localhost |
| **MCP / WS (local)** | localhost | 11437 | ws://localhost:11437, http://localhost:11437 | MCP toolkit / Iron Legion MCP; **not** Ollama |

**Critical**: On the **laptop**, nothing serves **Ollama** on port **11437**. Ollama is on **11434** only. Kilo Code pointed at `http://localhost:11437` for "Ultron" will hang (API request spins).

**SSOT**: `config/host_identity_registry.json` (ultron.primary = http://localhost:11434), `config/cluster_endpoint_registry.json`, `.cursor/memories/host_identity_kaiju_nas_critical.md`.

### 2.2 Kilo Code Config Mechanism

- **Kilo Code** uses **its own settings** (gear in Kilo Code panel): API provider profiles, base URL, model. Stored in extension storage and/or exported `kilo-code-settings.json`.
- **Repo** `config/kilo_code_optimized_config.json` is **Lumina/JARVIS** agent config (@peak behavior); Kilo Code extension does **not** read it for API URL. It is used for documentation and any tooling that syncs or validates.
- Therefore: **Fixing repo config alone does not fix Kilo Code.** User must set Kilo Code profile base URL to **http://localhost:11434** (or http://localhost:11434/v1) in Kilo Code UI.

### 2.3 What Has Been Done (Interim)

- **config/kilo_code_optimized_config.json**: `primary_llm.base_url` changed from `http://localhost:11437` to **http://localhost:11434** (2026-01-30).
- **docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md**: User-facing steps (Kilo Code gear → set base URL 11434; ensure Ollama running).
- **Diagnostic**: `scripts/python/diagnose_kilo_code_ultron_connectivity.py` added to check Ollama at 11434 and validate repo config alignment.

---

## 3. Root Cause (Documented)

1. **Wrong port for Ultron**: Config(s) and/or Kilo Code profile pointed at **localhost:11437**. On laptop, 11437 is MCP/WS, not Ollama. Ollama is **11434** only → requests hang.
2. **Kilo Code uses its own profile**: Repo config fix is necessary but not sufficient; user must correct the **Kilo Code API profile** (gear) to base URL **http://localhost:11434**.
3. **Ollama not running**: If Ollama is not running, any URL will spin; user must run `ollama serve` and verify `http://localhost:11434/api/tags`.

---

## 4. Acceptance Criteria (QA)

- [ ] **Ollama reachable**: `http://localhost:11434/api/tags` returns 200 and lists models when Ollama is running.
- [ ] **Kilo Code profile**: Kilo Code API profile used for "Ultron" or local Ollama has base URL **http://localhost:11434** (or **http://localhost:11434/v1** if OpenAI-compatible path).
- [ ] **Hello World test**: Kilo Code "Hello World" (or equivalent) request completes without spinning; response received.
- [ ] **Repo config aligned**: `config/kilo_code_optimized_config.json` and any other repo configs that reference "Ultron" or "local Ollama" use **11434** for laptop; 11437 only for MCP/WS or Kaiju where documented.
- [ ] **Diagnostic passes**: `python scripts/python/diagnose_kilo_code_ultron_connectivity.py` exits 0 when Ollama is running and repo config is aligned.

---

## 5. “Done Right” State

1. **Single source of truth**: Ultron (laptop) Ollama = **http://localhost:11434** in host_identity_registry, cluster registry, and all docs/checklists. Port **11437** on laptop = MCP/WS only; never Ollama.
2. **Kilo Code**: User-facing doc (KILO_CODE_ULTRON_CONNECTIVITY.md) and investigation brief state clearly that Kilo Code **UI** must set base URL to 11434; repo config is for tooling/consistency only.
3. **Validation**: Diagnostic script runnable from repo root; runbook includes “run diagnostic before closing ticket.”
4. **No ad-hoc changes**: Future endpoint or port changes follow PM/RCA and update SSOT and brief.

---

## 6. Required Investigation (Support Teams)

### 6.1 Problem Management

1. **RCA**: Confirm root cause (wrong port 11437 vs 11434; Kilo Code profile vs repo config; Ollama not running) and document in ticket.
2. **Gap analysis**: Any other CAs or configs (Continue, Cline, multi_ide_optimal_settings, ollama_model_mapping) that reference localhost:11437 for **Ollama** and should be 11434 for Ultron.
3. **Knowledge base**: Update runbook so “Kilo Code + Ultron” and “Cursor + Ultron” both reference the same SSOT (11434 for laptop Ollama).

### 6.2 QA/QC

1. **Validate** per acceptance criteria above.
2. **Sign-off**: Do not close PM000003178 until QA has validated and signed off.

### 6.3 Outputs

- RCA section in PM ticket or brief.
- Updated KILO_CODE_ULTRON_CONNECTIVITY.md and this brief with any new findings.
- Clear “done right” state and any remaining C/RFC for implementation.

---

## 7. References

| Doc / Asset | Purpose |
|-------------|---------|
| `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md` | User-facing fix steps and checklist |
| `docs/helpdesk/CURSOR_LOCAL_AI_INVESTIGATION_BRIEF.md` | Related Cursor + local AI brief |
| `config/host_identity_registry.json` | Host → IP and ultron.primary (11434) |
| `config/cluster_endpoint_registry.json` | Cluster endpoints |
| `config/kilo_code_optimized_config.json` | Repo Kilo Code / Lumina config (base_url 11434) |
| `scripts/python/diagnose_kilo_code_ultron_connectivity.py` | Diagnostic: Ollama + config alignment |
| `scripts/python/diagnose_cursor_connection.py` | Cursor/Ollama diagnostic (same Ollama 11434) |
| `docs/HELPDESK_PROBLEM_CHANGE_MANAGEMENT_STRUCTURE.md` | PM workflow |

---

## 8. Success Criteria for Closure

1. RCA completed and documented.
2. Acceptance criteria (Section 4) met and validated by QA.
3. “Done right” state (Section 5) documented and configs aligned.
4. Kilo Code Hello World (or equivalent) completes without spinning when Ollama is running and profile uses 11434.
5. PM000003178 closed only after QA sign-off and Problem Manager approval.

---

**Next step**: Problem Manager (@samantha) assigns investigation; Senior Problem Analyst (@gene) leads RCA. User: set Kilo Code profile base URL to **http://localhost:11434** and run diagnostic; see `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md`.
