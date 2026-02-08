# JARVIS Chat UI/UX expectation – Kilo Code as example

**Purpose**: State our **expectation**: a **customized chat UI/UX** as the **JARVIS-to-human interface**, using the **Kilo Code extension** as the reference example.

**Status**: Expectation / spec  
**Last updated**: 2026-01-31  
**Related**: [JARVIS_IDE_CHAT_INTERFACE_ARCHITECTURE.md](JARVIS_IDE_CHAT_INTERFACE_ARCHITECTURE.md), [JARVIS_AI_CHAT_PEAK_SPEC.md](../JARVIS_AI_CHAT_PEAK_SPEC.md), [KILO_CODE_CLUSTER_PER_MODEL_SETUP.md](KILO_CODE_CLUSTER_PER_MODEL_SETUP.md), [CURSOR_IDE_QOL_INDEX.md](CURSOR_IDE_QOL_INDEX.md)

---

## Expectation

We expect a **customized chat UI/UX** — a dedicated **JARVIS-to-human interface** — not just the default IDE chat with a pinned “JARVIS” session. The **Kilo Code extension** is the **example** of the level of customization we want: its own panel, modes, profiles, rules, MCP, and R5 integration form a distinct, tailored experience. JARVIS chat should be the same: a **first-class, recognizable JARVIS interface** for human ↔ JARVIS conversation.

---

## Kilo Code extension as example

Kilo Code provides a **customized CA experience** in the IDE:

| Aspect | Kilo Code (example) | JARVIS chat (expectation) |
|--------|----------------------|----------------------------|
| **Surface** | Extension with its own config, modes, profiles | Dedicated JARVIS chat surface (panel/sidebar or equivalent) |
| **Identity** | Kilo Code brand, per-model profiles, agent behaviour | JARVIS brand, JARVIS Master Agent, CTO/Superagent identity |
| **Modes** | Code, debug, architect, ask, review, orchestrator | Chat modes aligned with JARVIS (orchestration, workflow, helpdesk, R5 query) |
| **Context** | priorityFiles, excludePatterns, R5 integration | R5 Living Context, workspace, conversation history, workflow context |
| **Rules** | .kilocode/rules, no-secrets, ticket syntax | Same Lumina rules + JARVIS-specific (no secrets, verification, escalation) |
| **Config** | kilo_code_cluster_profiles, kilo_code_optimized_config | JARVIS chat config (model routing, UI preferences, queue, workflow panel) |
| **Integration** | Cursor, VS Code, JetBrains, Neovim; config path per IDE | Same IDEs; JARVIS chat as primary human interface |

So: **Kilo Code = customized CA UI/UX**. **JARVIS chat = customized JARVIS-to-human UI/UX** at that same level — recognizable, branded, and feature-rich.

---

## What “customized chat UI/UX” means for JARVIS

- **Dedicated JARVIS chat panel/sidebar** (or equivalent in each IDE), not just a generic chat tab renamed “JARVIS”.
- **JARVIS-specific layout and controls**: e.g. queue (voice + text), workflow status, @helpdesk / R5 / escalation shortcuts, optional airport-signboard style progress.
- **Consistent identity**: JARVIS Master Agent, CTO/Superagent; same API and behaviour across IDE, desktop app, and widgets.
- **@PEAK-aligned behaviour**: full context first, pattern-aware responses, task-optimized model routing, streaming, local-first, no secrets, verification where needed (see [JARVIS_AI_CHAT_PEAK_SPEC.md](../JARVIS_AI_CHAT_PEAK_SPEC.md)).
- **Extension or equivalent**: Ideally a **JARVIS Chat extension** (or equivalent) that provides this UI/UX in Cursor/VS Code, analogous to how the Kilo Code extension provides its customized CA experience.

---

## Current state vs target

| | Current state | Target (expectation) |
|---|----------------|----------------------|
| **In Cursor** | Pinned “JARVIS Master Chat” session + Cursor default chat UI | **Customized JARVIS chat UI/UX** (dedicated panel, JARVIS branding, queue, workflow, R5) — e.g. JARVIS Chat extension |
| **Standalone** | WoW-style local chat server + `jarvis_chat_ui.py` | Same JARVIS identity and API; desktop/widget can share the same backend and UX principles |
| **Config** | `jarvis_master_chat_cursor_config.json`, Cursor settings | JARVIS chat–specific config (like Kilo Code has); referenced from framework and QOL registry |

So: **current** = pinned session + scripts + local chat. **Target** = **customized JARVIS-to-human interface** at Kilo Code–level (extension or equivalent, dedicated UI/UX, config, and behaviour).

---

## References

- **Kilo Code (example)**: `config/kilo_code_cluster_profiles.json`, `config/kilo_code_optimized_config.json`, `config/coding_assistants_registry.json` (kilo_code), `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **JARVIS IDE Chat**: `docs/system/JARVIS_IDE_CHAT_INTERFACE_ARCHITECTURE.md`, `docs/system/JARVIS_CHAT_INTERFACE_SUMMARY.md`
- **JARVIS Chat vision**: `docs/JARVIS_AI_CHAT_PEAK_SPEC.md`
- **Current JARVIS chat config**: `config/jarvis_master_chat_cursor_config.json`
- **Cursor IDE QOL**: `config/cursor_ide_qol_registry.json`, `docs/system/CURSOR_IDE_QOL_INDEX.md`
