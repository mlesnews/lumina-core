# IDE, CA & Framework Full Utilization Audit

**Purpose:** Ensure Cursor IDE, every other IDE/CA, and Lumina #frameworks are customized and used to their fullest extent. Single reference for "are we using it all?"

**SSOT:** This doc. **Last audit:** 2026-02-04.

**Related:** `config/cursor_ide_qol_registry.json`, `config/ca_pa_ide_framework_alignment.json`, `config/coding_assistants_registry.json`, `config/multi_ide_optimal_settings.json`, `docs/system/CURSOR_IDE_QOL_INDEX.md`.

---

## 1. Cursor IDE – Feature-by-Feature Utilization

| Feature / functionality | Status | Customization / config | Notes |
|-------------------------|--------|------------------------|--------|
| **Chat** | ✅ Utilized | `.cursor/settings.json`, `.vscode/settings.json`: `cursor.chat.customModels`, `cursor.chat.defaultModel`, `cursor.chat.pinnedSessions`, `cursor.chat.defaultSession`, `cursor.chat.alwaysOpenPinned` | JARVIS Master Chat pinned; ULTRON / Iron Legion models. |
| **Composer** | ✅ Utilized | Same: `cursor.composer.customModels`, `cursor.composer.defaultModel`. Keybindings: `Ctrl+K Ctrl+C` open, `Ctrl+Enter` accept all, `Ctrl+Shift+Enter` keep all, `Ctrl+K Ctrl+F` accept all files | |
| **Agent (Background / Auto)** | ✅ Utilized | Same: `cursor.agent.customModels`, `cursor.agent.defaultModel`; `cursor.agent.retryAttempts`, `retryDelay`, `connectionTimeout`, `streamTimeout`. Keybindings: `Ctrl+K Ctrl+A` start | |
| **Tab completion / autocomplete** | ✅ Utilized | `cursor.ai.autoComplete`, `cursor.ai.suggestions`, `cursor.ai.showInlineSuggestions`, `cursor.ai.inlineSuggestionDelay` | |
| **Refactor** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+R` | |
| **Test generation** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+T` | |
| **Codebase index** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+I` | |
| **Summarize** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+S` | |
| **Debug explain** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+D` | |
| **Inline edit** | ✅ Utilized | Keybinding: `Ctrl+K Ctrl+E` | |
| **Accept All (suggestions)** | ✅ Utilized | `Ctrl+Shift+A` in editor; `Ctrl+Enter` / `Ctrl+K Ctrl+F` in Composer; `Ctrl+Enter` / `Ctrl+K Ctrl+K` in Agent | See `config/cursor_keybindings_accept_all.json`, `docs/workflow/CURSOR_WORKFLOW_SOLUTIONS.md` (accept changes). |
| **Custom models (Chat / Composer / Agent)** | ✅ Utilized | ULTRON (local :8080 or :11434), Iron Legion (10.17.17.11:11437); many named models (Qwen, Llama, Codellama, etc.) in `.vscode/settings.json` | `.cursor/settings.json` uses :8080 for ULTRON; .vscode uses :11434. Align if one gateway. |
| **MCP** | ✅ Utilized | `.cursor/mcp.json`: single `MCP_DOCKER` gateway (`docker mcp gateway run`). All MCP servers via Docker Desktop MCP Toolkit | Per-machine: run `scripts/setup_mcp_ultron.ps1` (laptop); enable MCP_DOCKER in Cursor Settings. |
| **Rules** | ✅ Utilized | `.cursor/rules/*.mdc` – always-applied and agent-requestable rules | See `.cursor/rules/`. |
| **Skills** | ✅ Utilized | `.cursor/skills/` – `--request-workflow`, `--helpdesk-pm`, `--mdv-troubleshoot`, `--automation-first`, `--nas-dsm`, `--local-resources-first`, `--ai-integration`, `--warm` | Index: `docs/system/LUMINA_CURSOR_SKILLS.md`, `.cursor/docs/LUMINA_SKILLS_INDEX.md`. |
| **Keybindings** | ✅ Utilized | `.cursor/keybindings.json` – Chat, Composer, Agent, Refactor, Test, Index, Summarize, Debug, Inline edit, Accept/Keep all, MANUS screenshots, Print/Shift+Print, Git stage/discard | RAlt @DOIT / F23 @JARVIS: `config/lumina_hotkeys.json` (external: PowerToys/AutoHotkey). |
| **Tasks** | ✅ Utilized | `.cursor/tasks.json` – JARVIS (health, optimize, monitor IDE notifications, MCP check), MANUS (MDV feed, TightVNC, screenshots), LDAP, SSO | "JARVIS: Monitor IDE Notifications" runs on folder open. |
| **Workspace settings** | ✅ Utilized | `.vscode/settings.json` – editor, cursor.ai, cursor.agent, cursor.chat, cursor.composer, git, workbench, Python, cSpell, LTeX | Shared with VS Code. |
| **Extensions** | ✅ Utilized | `.vscode/extensions.json`, `.cursor/extensions.json` – recommendations | Install Kilo Code, Continue, Cline per `multi_ide_optimal_settings.json`. |
| **Peak Efficiency (agent behavior)** | ⚠️ Partial | `config/CURSOR_PEAK_EFFICIENCY_CONFIG.md` defines timeout, maxIterations, autoContinue, parallelToolCalls, context maxFiles/maxTokens, etc. | Not all keys may be exposed by Cursor Settings; apply what exists in Cursor Settings UI. See "Recommended actions" below. |
| **Voice input** | ✅ Utilized | Lumina Core Voice Request Queue; F23 → @JARVIS + Voice (lumina_hotkeys) | `docs/workflow/CURSOR_WORKFLOW_SOLUTIONS.md`, `config/cursor_voice_filter_config.json`. |
| **Footer / ticker** | ✅ Utilized | `config/cursor_footer_config.json`, `config/footer_ticker_config.json`; script: `cursor_ide_footer_customization.py` | |
| **JARVIS IDE problems contract** | ✅ Utilized | Monitor: `jarvis_ide_notification_monitor.py` (run on folder open); contract: `docs/system/JARVIS_IDE_PROBLEMS_CONTRACT.md` | JARVIS addresses every detected problem; delegates to #frameworks. |

---

## 2. Other IDEs – Utilization Summary

| IDE | Status | Config / doc | Customization level |
|-----|--------|--------------|---------------------|
| **VS Code** | ✅ Aligned | `config/multi_ide_optimal_settings.json` → `vscode`, `.vscode/settings.json`, `extensions.json`, `tasks.json`, `launch.json` | Same workspace settings as Cursor; Kilo Code, Continue, Cline; same CA priorities. |
| **JetBrains** | ✅ Defined | `multi_ide_optimal_settings.json` → `jetbrains`; `coding_assistants_registry.json` → `ide_priorities.jetbrains` | Kilo Code primary; config path `.idea/kilo_code.xml`. |
| **Neovim** | ✅ Defined | `multi_ide_optimal_settings.json` → `neovim`; `coding_assistants_registry.json` → `ide_priorities.neovim` | kilocode.nvim; config `~/.config/nvim/lua/plugins/kilocode.lua`. |

**Framework alignment:** All IDEs use the same CA/PA/IDE framework: `config/ca_pa_ide_framework_alignment.json` (tiers, IP characters, decisioning chain, context guidance). See `config/unified_ca_peak_spec.json`, `docs/system/UNIFIED_CA_PEAK_SPEC.md`.

---

## 3. Coding Assistants (CA) – Utilization Summary

| CA | Status | IDE support | Config | Notes |
|----|--------|------------|--------|--------|
| **Kilo Code** | ✅ Primary | Cursor, VS Code, JetBrains, Neovim | `config/kilo_code_optimized_config.json`, `multi_ide_optimal_settings.json` (cursor/vscode/jetbrains/neovim) | use_peak_patterns, use_r5_context, prefer_local_llm. |
| **Continue** | ✅ Secondary | Cursor, VS Code | `config/continue_config.json`, `.continue/config.yaml` | |
| **Cline** | ✅ Tertiary | Cursor, VS Code | `config/cline_config.json`, `config/cline_mcp_config.json` | |
| **Roo** | ⏳ To add | Planned | `config/roo_config.json` (when available) | Align to unified_ca_peak_spec when added. |
| **GitHub Copilot** | Standby | Cursor, VS Code | requires_approval; cloud; never for PII/security-critical | |
| **AWS CodeWhisperer** | Standby | Cursor, VS Code | requires_approval; cloud | |

**Verification:** `scripts/python/verify_coding_assistants_setup.py` (referenced in `coding_assistants_registry.json`).

---

## 4. Frameworks (#frameworks) – Utilization Summary

| Framework | Status | Where | Notes |
|-----------|--------|--------|--------|
| **Cursor rules** | ✅ Utilized | `.cursor/rules/*.mdc` | Always-applied + requestable; troubleshooting, one_shot_no_mess, no_secrets, git_workflow, context_intent_baseline, etc. |
| **Skills** | ✅ Utilized | `.cursor/skills/*/SKILL.md` | Request workflow, helpdesk-PM, mdv-troubleshoot, automation-first, nas-dsm, local-resources-first, ai-integration, warm. |
| **MCP** | ✅ Utilized | `.cursor/mcp.json` (MCP_DOCKER gateway) | Docker Desktop MCP Toolkit; per-machine setup scripts. |
| **Request workflow (snapshots)** | ✅ Utilized | `docs/workflow/REQUEST_WORKFLOW.md`, `--request-workflow` skill, git milestone snapshots | Step 0 snapshot before, Step 2 commit after. |
| **Troubleshooting & decisioning** | ✅ Utilized | `.cursor/rules/troubleshooting_decisioning_workflow.mdc`, context_intent_baseline; PM tickets, investigation briefs | Full context first; no jump-in fix. |
| **Helpdesk / PM** | ✅ Utilized | `--helpdesk-pm` skill, `data/helpdesk/tickets/`, `docs/HELPDESK_PROBLEM_CHANGE_MANAGEMENT_STRUCTURE.md` | |
| **Automation first** | ✅ Utilized | `.cursor/rules/automation_first.mdc`, `--automation-first` skill, `docs/system/AUTOMATION_FIRST.md` | Single-entry scripts; B-Side for network. |
| **Local resources first** | ✅ Utilized | `.cursor/rules/check_local_resources_first.mdc`, `--local-resources-first` skill | Search before creating; integrate before creating. |
| **Host identity / DNS** | ✅ Utilized | `.cursor/rules/host_identity_dns.mdc`, `config/host_identity_registry.json` | Kaiju = .11, NAS = .32. |
| **One-shot no mess** | ✅ Utilized | `.cursor/rules/one_shot_no_mess.mdc` | Accept changes; verify; snapshot after. |
| **Fix underlying problem** | ✅ Utilized | `.cursor/rules/fix_underlying_problem.mdc` | No suppressors without fixing root cause. |
| **No commit --no-verify** | ✅ Utilized | `.cursor/rules/no_commit_no_verify.mdc` | Batch commits so pre-commit runs. |
| **JARVIS IDE problems** | ✅ Utilized | `JARVIS_IDE_PROBLEMS_CONTRACT.md`, IDE notification monitor (folder open), MCP check task | Every problem → JARVIS; delegate to subagents/#frameworks. |
| **Homelab inventory–driven automation** | ✅ Utilized | `docs/system/HOMELAB_INVENTORY_AUTOMATION_CONTRACT.md`, `config/homelab_inventory_registry.json`, `.cursor/rules/homelab_inventory_automation.mdc` | Automation/autonomy driven by hw/sw homelab inventory—every device, feature, function, application, service. |

---

## 5. Recommended Actions (Gaps & Hardening)

1. **Peak Efficiency settings**
   Apply any settings from `config/CURSOR_PEAK_EFFICIENCY_CONFIG.md` that exist in Cursor’s Settings UI (Cursor → Settings → Cursor Settings). If a key is not visible, treat it as aspirational and do not add to `settings.json` to avoid noise. Prefer documenting "verify in UI" in this doc.

2. **ULTRON base URL**
   Align ULTRON `apiBase` between `.cursor/settings.json` (e.g. `http://localhost:8080`) and `.vscode/settings.json` (e.g. `http://localhost:11434/v1`) if you use a single local gateway; otherwise document why they differ (e.g. 8080 = proxy, 11434 = Ollama).

3. **RAlt @DOIT / F23 @JARVIS**
   Ensure `config/lumina_hotkeys.json` is applied via PowerToys or AutoHotkey so global hotkeys work in Cursor.

4. **Other IDEs (JetBrains, Neovim)**
   When using them, run through `multi_ide_optimal_settings.json` setup_instructions and verify Kilo Code (and Continue/Cline where applicable) are configured per framework.

5. **Roo**
   When adding Roo, add config and extension/plugin IDs to `coding_assistants_registry.json` and align to `unified_ca_peak_spec.json`.

6. **Verify CAs**
   Run `scripts/python/verify_coding_assistants_setup.py` periodically and set `last_verified` in `config/coding_assistants_registry.json`.

---

## 6. Quick Reference – Where to Change What

| Goal | Primary location |
|------|-------------------|
| Cursor models (Chat/Composer/Agent) | `.vscode/settings.json` (cursor.chat/composer/agent.customModels, defaultModel) |
| Cursor keybindings | `.cursor/keybindings.json` |
| Cursor tasks | `.cursor/tasks.json` |
| Cursor MCP | `.cursor/mcp.json` (project); user-level `~/.cursor/mcp.json` empty mcpServers |
| Cursor rules | `.cursor/rules/*.mdc` |
| Cursor skills | `.cursor/skills/*/SKILL.md` |
| All IDEs + CAs alignment | `config/ca_pa_ide_framework_alignment.json`, `config/multi_ide_optimal_settings.json` |
| CA registry | `config/coding_assistants_registry.json` |
| Cursor QOL index | `config/cursor_ide_qol_registry.json`, `docs/system/CURSOR_IDE_QOL_INDEX.md` |

---

**Maintained by:** @JARVIS @LUMINA
**Next audit:** When adding a new IDE, CA, or major Cursor feature.
