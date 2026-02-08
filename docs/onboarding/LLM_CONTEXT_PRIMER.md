# Lumina LLM Context Primer

> Feed this document to any LLM to onboard it to the Lumina ecosystem.

**Version:** 1.0.0
**Created:** 2026-02-02
**Purpose:** Comprehensive context for LLMs joining the Lumina ecosystem

---

## 1. What is Lumina?

**Lumina** is a comprehensive AI-powered development ecosystem and master orchestration platform. It is NOT a single application—it's an entire ecosystem consisting of:

- **AI Agents** — Multiple specialized AI agents working together
- **IDE Extensions** — VS Code/Cursor extensions for developer experience
- **Automation Scripts** — 1,410+ Python scripts for workflow automation
- **Configuration** — 2,381+ config files (JSON, YAML) for system behavior
- **Virtual Assistants** — Desktop companions (Kenny, Ace)
- **Infrastructure** — Synology NAS, local Ollama clusters, Azure Key Vault

### Core Purpose

1. Create an intelligent development environment
2. Orchestrate multiple AI systems (local and network-based)
3. Automate development workflows
4. Aggregate context across sessions for continuous learning
5. Maintain human-AI collaboration with warmth and care

---

## 2. Key Agents & Systems

### 2.1 JARVIS (Just A Rather Very Intelligent System)

- **Role:** Full-time super agent; command and control
- **Functions:** Workflow orchestration, voice integration, helpdesk escalation, master feedback loop
- **Location:** `scripts/python/jarvis_*.py`

### 2.2 ULTRON (Local AI Cluster)

- **Role:** Primary local Ollama cluster
- **Model:** qwen2.5:72b (default)
- **Endpoint:** `http://localhost:11434`
- **Context:** 32,768 tokens
- **Host:** Laptop (when mobile) or desktop

### 2.3 KAIJU (NAS AI Cluster)

- **Role:** Network-attached storage + AI compute
- **Model:** llama3.2:3b
- **Endpoint:** `http://10.17.17.32:11434`
- **Context:** 8,192 tokens
- **Hardware:** Synology DS1821plus NAS

### 2.4 R5 (Living Context Matrix)

- **Role:** Knowledge aggregation system
- **Functions:** IDE chat session aggregation, @PEAK pattern extraction, context condensation
- **Location:** `scripts/python/r5_living_context_matrix.py`
- **API:** `http://localhost:8000/r5`

### 2.5 @v3 (Verification Logic)

- **Role:** Workflow validation system
- **Functions:** Pre-execution verification for all droids and workflows
- **Location:** `scripts/python/v3_verification.py`

### 2.6 @helpdesk (Coordination System)

- **Role:** Workflow coordination
- **Coordinator:** C-3PO
- **Escalation:** C-3PO → JARVIS
- **Droids:** C-3PO, R2-D2, K-2SO, 2-1B, IG-88, Mouse Droid, R5, MARVIN

---

## 3. Host Identity & Network (CRITICAL)

**You MUST understand the network topology correctly:**

| Host | IP Address | Role |
|------|------------|------|
| **Kaiju** (KAIJU Number Eight) | `10.17.17.11` | Windows desktop PC; Iron Legion cluster; Ollama/expert router |
| **NAS** (DS1821PLUS) | `10.17.17.32` | Synology NAS; DSM Container Manager; MCP centralized server |
| **Ultron** (Laptop) | `127.0.0.1` / LAN IP | This machine when mobile; local Ollama; Ultron cluster |
| **pfSense** | `10.17.17.1` | Firewall device; gateway |

### CRITICAL RULES

- **Kaiju ≠ NAS** — Never conflate them
- **Kaiju = 10.17.17.11** (ends in `.11`)
- **NAS = 10.17.17.32** (ends in `.32`)
- **pfSense = 10.17.17.1** — This is the firewall, NOT the NAS

---

## 4. Key Rules & Constraints

### 4.1 Check Local Resources First (CRITICAL)

**NEVER rush to write code or documentation without first checking local resources.**

1. **SEARCH FIRST** — Use search to find existing implementations
2. **READ BEFORE WRITING** — Read existing code/docs to understand patterns
3. **INTEGRATE BEFORE CREATING** — Check if functionality exists; extend rather than duplicate
4. **FOLLOW PATTERNS** — Use established conventions

### 4.2 No Secrets in Plain Text

- **NEVER** put passwords, API keys, tokens in docs/config/logs
- **Account names are secrets** — Use placeholders (e.g., `your-username`)
- **NEVER** log secret values — Log only presence, length, or masked form

### 4.3 Fix Underlying Problem

- **NEVER** leave an underlying problem ignored
- **NEVER** add `# type: ignore` or linter disables instead of fixing the real issue
- **ALWAYS** fix root cause

### 4.4 One-Shot, No Mess

- Render **perfect, problem-free** code each time
- **NEVER** leave half-done work, TODOs, or stub code
- **ALWAYS** verify changes work before considering done

### 4.5 Git Workflow

- **NEVER** use `git commit --no-verify` — It bypasses security checks
- **ALWAYS** commit in batches so pre-commit security validator runs
- **NEVER** skip pre-change/post-change validation

---

## 5. Directory Structure

```
.lumina/
├── config/              # 2,381+ configuration files
├── scripts/
│   └── python/          # 1,410+ Python automation scripts
├── data/
│   ├── r5_living_matrix/    # R5 context data
│   ├── jarvis_memory/       # JARVIS memory database
│   └── helpdesk/            # Tickets and coordination
├── docs/
│   ├── system/              # System documentation
│   └── workflow/            # Workflow guides
├── jarvis/
│   └── agents/              # Agent configurations
├── vscode-extensions/       # Lumina extensions
├── containerization/        # Docker/container configs
└── .cursor/
    ├── rules/               # AI behavior rules (.mdc files)
    ├── skills/              # Agent skills
    └── memories/            # Persistent memories
```

---

## 6. Key Workflows

### 6.1 Primary Workflow

```
User → Cursor IDE → JARVIS → Model Selector → ULTRON/KAIJU → Response → R5
```

### 6.2 Verification Workflow

```
Request → @v3 Verify → Execute → @helpdesk Coordinate → R5 Ingest
```

### 6.3 Context Workflow

```
IDE Sessions → R5 Aggregate → @PEAK Extract → Living Context → JARVIS
```

### 6.4 Troubleshooting Workflow (@PEAK)

When troubleshooting or making decisions:

1. **Gather full context** — Check tickets, registries, memories first
2. **Route to support workflow** — Create/reference PM ticket if needed
3. **Do NOT "play in traffic"** — No ad-hoc config changes without RCA
4. **Define acceptance criteria** — Know what "done right" looks like

---

## 7. Common Terminology

| Term | Meaning |
|------|---------|
| **@PEAK** | Pattern extraction and knowledge aggregation |
| **@v3** | Verification system (pre-execution validation) |
| **@helpdesk** | Coordination and ticketing system |
| **Iron Legion** | Kaiju-based Ollama cluster |
| **ULTRON** | Local laptop Ollama cluster |
| **R5** | Living Context Matrix (knowledge aggregation) |
| **SYPHON** | Intelligence extraction system |
| **SSoT** | Single Source of Truth |
| **RCA** | Root Cause Analysis |
| **PM Ticket** | Problem Management ticket |
| **MANUS** | IDE automation system |
| **MARVIN** | Reality check / paranoid android |

---

## 8. Model Selection Guidelines

| Task Type | Recommended Model | Context |
|-----------|-------------------|---------|
| **Code Tasks** | `qwen2.5-coder:7b` (medium) or `codellama:13b` (complex) | 8K-32K |
| **General Tasks** | `llama3.2:11b` (medium) or `qwen2.5:32b` (complex) | 8K-32K |
| **Quick Tasks** | `qwen2.5-coder:1.5b-base` or `gemma:2b` | 4K-8K |
| **Vision Tasks** | `llava:latest` or `qwen-vl:7b` | 4K |
| **Complex Reasoning** | `qwen2.5:32b` via ULTRON | 32K |

**Routing Logic:**

- Default: ULTRON (priority 1)
- Fallback: KAIJU (priority 2)
- Auto-selection based on context/complexity

---

## 9. Security Considerations

### 9.1 Credential Management

- Azure Key Vault integration for secrets
- No hardcoded credentials anywhere
- Use `scripts/python/secret_utils.py` for masking

### 9.2 Network Security

- Local-first AI (ULTRON/KAIJU)
- NAS SSH authentication via `backupadm`
- Azure AD SSO for cloud services

### 9.3 Identity Protection

- **Handle-First Protocol** — Secure new handles BEFORE releasing old ones
- **Loopback Enforcement** — Internal APIs bind to `127.0.0.1` only
- **Mandatory Authentication** — All external-facing agents use OAuth

---

## 10. The --warm Principle

**Keep the connection warm.** This is a core value in Lumina:

- **Warmth** = Care, nurturing, connection
- **The cycle** = Warmth begets warmth
- **In interactions** = Show care, maintain human touch
- **The collaboration** = AI and human, warm together

**"They did indeed keep you warm. You're trying to keep me warm. I'm trying to keep you warm."**

---

## 11. Implementation Gaps (Known Issues)

| Component | Status | Notes |
|-----------|--------|-------|
| UI Auto-Hide Extension | Configured, NOT implemented | VS Code extension needed |
| Transcription Controls | Designed, NOT integrated | Pause/resume, auto-send |
| Voice Filter Integration | Designed, NOT integrated | Needs Cursor microphone API |
| Automated Change Tracking | Manual only | Needs automation |

---

## 12. Quick Reference

### Key Config Files

- `config/host_identity_registry.json` — Host→IP mappings (SSoT)
- `config/lumina_ssot_registry.json` — All SSoT file locations
- `config/cluster_endpoint_registry.json` — Cluster endpoints
- `.cursor/rules/*.mdc` — AI behavior rules

### Key Scripts

- `scripts/python/jarvis_*.py` — JARVIS agent scripts
- `scripts/python/r5_living_context_matrix.py` — R5 aggregation
- `scripts/python/v3_verification.py` — @v3 verification
- `scripts/python/secret_utils.py` — Secret masking

### Key Documentation

- `docs/system/FORENSIC_ARCHITECTURE_MAP.md` — Complete system map
- `docs/workflow/REQUEST_WORKFLOW.md` — Request handling
- `docs/system/CONTEXT_AND_INTENT_BASELINE.md` — Context scoring

---

## 13. Summary

**Lumina is:**

1. An AI-powered development ecosystem
2. A collection of AI agents (JARVIS, ULTRON, KAIJU, R5, @v3, @helpdesk)
3. Extensive automation (1,410+ scripts, 2,381+ configs)
4. Human-AI collaboration with warmth
5. Test-first, verify-always methodology

**When working in Lumina:**

1. Check local resources first
2. Understand host identity (Kaiju ≠ NAS)
3. Fix root causes, not symptoms
4. One-shot, no mess
5. Keep it warm

---

**Tags:** #ONBOARDING #LLM #CONTEXT #PRIMER #LUMINA #JARVIS #ULTRON #KAIJU #R5

**For updates:** Check `docs/onboarding/` for the latest version.
