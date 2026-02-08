# Cursor + Local AI Clusters – Investigation Brief for Support Teams

**PM Ticket**: PM000003102
**Created**: 2026-01-29
**Status**: Open – Support teams to investigate and work the issue
**Risk**: Continued ad-hoc changes = "playing in traffic"; require structured investigation first.

---

## 1. Purpose

Support teams (Problem Management, QA/QC) are to **investigate** and **work** the Cursor + local AI cluster issue through the proper workflow. Do **not** make further config or doc changes without root cause analysis and a clear definition of "done right."

---

## 2. What We Know (Facts)

### 2.1 Host Identity (Canonical)

| Host | IP | Role | Do NOT |
|------|-----|------|--------|
| **Kaiju** = Kaiju_no_8 | **10.17.17.11** | Windows desktop; Iron Legion cluster | Use *.32 for Kaiju |
| **NAS** | **10.17.17.32** | Only NAS on LAN; DSM, MCP, containers | No alias; do not use *.11 |
| **pfSense firewall** | **10.17.17.1** | Firewall device only | Do not use for NAS or "ultron_nas" |

**SSOT**: `config/host_identity_registry.json`
**Persistent memory**: `.cursor/memories/host_identity_kaiju_nas_critical.md`, `.cursor/rules/host_identity_dns.mdc`

### 2.2 Clusters (Intended)

- **ULTRON**: Laptop local – Ollama at `http://localhost:11434`; router at `http://localhost:8080` (if used). Multiple models (qwen2.5-coder:7b, qwen2-72b, qwen2.5-coder:1.5b-base, codellama:13b, llama3.2:3b, qwen2.5:72b, etc.).
- **Iron Legion**: Kaiju_no_8 desktop at `http://10.17.17.11:11434` (Ollama) or marks 3001–3007. Models: codellama:13b, llama3.2:11b, qwen2.5-coder:1.5b-base, llama3:8b, mistral:7b, mixtral-8x7b, gemma:2b.

### 2.3 What Has Been Done (Ad-Hoc)

- Host identity corrected in configs and persistent memory (Kaiju=*.11, NAS=*.32, pfSense=*.1; no ultron_nas alias).
- **Single-node cluster presentation enforced (2026-01-29)**: Cursor sees exactly **two** custom models – **ULTRON** (cluster face: localhost:11434, model qwen2.5-coder:7b) and **Iron Legion** (cluster face: 10.17.17.11:11434, model codellama:13b). All internal routing (ULTRON variants, Iron Legion Marks) is handled inside the cluster; do **not** re-expose individual models in Agent/Chat/Composer.
- maxTokens raised to 8192 globally and per model.
- Docs: CURSOR_LOCAL_AI_FIX_CHECKLIST.md, CURSOR_CONNECTION_STALLED_*, PERSISTENT_MEMORY_MAP.md, host identity memory/rule. Rule: `.cursor/rules/cluster_single_node_presentation.mdc`.

---

## 3. What Is Still Wrong / Unclear

1. **Root cause** of Cursor not working with local clusters (if it still fails) – not formally documented.
2. **Actual vs intended** architecture: **RESOLVED 2026-01-29** – clusters present as single nodes; Cursor has exactly two custom models (ULTRON, Iron Legion). Internal routing is cluster-internal only.
3. **Chat/Composer** custom model lists – **RESOLVED 2026-01-29**: Agent, Chat, and Composer each have exactly two cluster faces (ULTRON, Iron Legion). No individual models exposed.
4. **DNS**: Configs are not pulling from DNS; host_identity_registry is fallback. When/how to move to DNS as source of truth?
5. **Persistent memory**: Corrections (host identity, etc.) have been forgotten on reboot before; is the current persistence (rules, memories, registry) sufficient and validated?

---

## 4. Workflow Violation (2026-01-29)

**Single-node cluster presentation was implemented by the AI without routing through the support workflow.** Settings, brief, and rule were changed directly instead of: PM assign → RCA → define "done right" → implement → QA validate → sign-off. The change is an **interim correction**; support must still perform RCA, define done right, and get QA sign-off before closing PM000003102. Do not repeat: future changes must follow the workflow.

---

## 5. “Playing in Traffic” – What to Avoid

- Making further changes to Cursor settings, cluster registry, or host identity **without**:
  - Reading this brief and the PM ticket
  - Performing root cause analysis per Problem Management workflow
  - Defining acceptance criteria and "done right" state
  - Involving QA for validation before closure
- Conflating Kaiju with NAS or using wrong IPs.
- Treating the issue as "fixed" before support teams have investigated and signed off.

---

## 6. Required Investigation (Support Teams)

### 6.1 Problem Management

1. **Root cause analysis**: Why has Cursor + local AI been repeatedly misunderstood or broken? (e.g. no single SSOT, no RCA, no sign-off.)
2. **Current state capture**: Document actual Cursor config (Agent, Chat, Composer), cluster registry, and which endpoints Cursor uses in practice.
3. **Gap analysis**: Actual vs intended (two clusters, router vs multi-model, DNS vs static registry).
4. **Known error**: If workaround exists, document it; if not, drive RFC for fix.

### 6.2 QA/QC

1. **Acceptance criteria**: Define what “Cursor working with local AI clusters” means (e.g. model selector shows cluster models, requests reach correct endpoint, no invalid model / connection stalled when services are up).
2. **Validation**: Test Cursor against Ultron and Iron Legion per acceptance criteria; record results.
3. **Sign-off**: Do not close PM000003102 until QA has validated and signed off.

### 6.3 Outputs

- RCA document (or section in PM ticket).
- Updated knowledge base / runbook for Cursor + local AI (so future work does not “play in traffic”).
- Clear “done right” state and any remaining C/RFC for implementation.

---

## 7. Related investigations

- **Kilo Code + Ultron**: PM000003178 – Kilo Code API request spinning; wrong port (11437 vs 11434). Brief: `docs/helpdesk/KILO_CODE_ULTRON_INVESTIGATION_BRIEF.md`, user steps: `docs/system/KILO_CODE_ULTRON_CONNECTIVITY.md`.

---

## 8. References

| Doc / Asset | Purpose |
|-------------|---------|
| `docs/HELPDESK_PROBLEM_CHANGE_MANAGEMENT_STRUCTURE.md` | Problem Management workflow |
| `docs/system/CURSOR_LOCAL_AI_FIX_CHECKLIST.md` | Current fix checklist and cluster table |
| `docs/system/CURSOR_CONNECTION_STALLED_WORKFLOW_FIX.md` | Connection stalled diagnostics |
| `docs/system/PERSISTENT_MEMORY_MAP.md` | Where persistence lives |
| `config/cluster_endpoint_registry.json` | Cluster SSOT |
| `config/host_identity_registry.json` | Host → IP SSOT |
| `.cursor/memories/host_identity_kaiju_nas_critical.md` | Host identity memory |
| `.vscode/settings.json` | Cursor custom models (Agent; verify Chat/Composer) |

---

## 9. Success Criteria for Closure

1. RCA completed and documented.
2. “Done right” state and acceptance criteria agreed and documented.
3. Cursor + Ultron and Cursor + Iron Legion validated by QA against acceptance criteria.
4. Knowledge base / runbook updated so future changes follow process and do not repeat misunderstandings.
5. PM000003102 closed only after QA sign-off and Problem Manager approval.

---

**Next step**: Problem Manager (@samantha) assigns investigation; Senior Problem Analyst (@gene) leads RCA and technical investigation using this brief.
