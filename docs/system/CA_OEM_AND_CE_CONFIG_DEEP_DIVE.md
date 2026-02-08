# CAs, PAs, and IDEs: OEM State (Core) and Custom Configuration (CE) – Deep Dive

**Date**: 2026-01-29  
**Tag**: @JARVIS @CA @PA @IDE @Core @CE

This document consolidates **external research** and Lumina inventory for **CAs (Coding Agents), PAs (Personal Assistants), and IDEs** in the JARVIS set. For each, it defines:

- **OEM state for "Core"**: Out-of-the-box behavior, config locations, schema, and what is generic/public (suitable for `.lumina/` or shared templates).
- **Custom configuration for "CE"**: What belongs in the company fork (cedarbrook-* trees): company-specific API profiles, endpoints, rules, MCPs, and overrides.

**Scope:**

- **CAs**: Continue, Kilocode, Roo Code, Cline (coding assistant extensions).
- **PAs**: Personal Assistant tooling (e.g. JARVIS PA — tasks, voice, calendar; evolution/maturation).
- **IDEs**: Cursor, VSCode, JetBrains, Neovim (editors and their workspace config).

See `docs/system/LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md` for Core vs Premium vs CE and `docs/JARVIS_CA_IDE_CONSOLIDATION_PLAN.md` for the full CA/IDE inventory.

---

## 1. Continue

### 1.1 OEM state (Core)

| Aspect | Details |
|--------|---------|
| **Config file** | `config.yaml` (YAML). Legacy `config.json` is deprecated. |
| **Schema** | Top-level `schema: v1`; `name` and `version` required. |
| **User (global) path** | `~/.continue/config.yaml` (OS user directory). |
| **Workspace path** | `.continue/` in project root. Workspace can use `.continuerc.json` for overrides; hybrid with user config is supported (workspace extends/overrides user). |
| **Lumina usage** | `.lumina/.continue/` holds `config.yaml`, `agents/`, `mcpServers/` in the **public** tree — effectively workspace config for the Lumina repo. |
| **Top-level properties** | `name`, `version`, `schema`, `models`, `context`, `rules`, `prompts`, `docs`, `mcpServers`, `data`. |
| **Models** | Each model: `name`, `provider` (e.g. `openai`, `ollama`, `continue-proxy`), `model`, `apiBase`, `roles` (e.g. `chat`, `edit`, `apply`, `autocomplete`), plus completion/autocomplete options. |
| **Providers** | OpenAI, Anthropic, Azure, Ollama, OpenAI-compatible (custom `apiBase`). Continue Mission Control supports hub configs and local file refs (`file://`, `uses:`). |

**Core-appropriate content**: Generic model definitions (no secrets), shared rules/prompts, MCP server definitions (commands/env only; no API keys), docs list. Templates for Ultron/Ollama endpoints with placeholders for host/port.

### 1.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **API keys / secrets** | Never in repo; use env vars or secret refs (e.g. `${{ secrets.OPENAI_API_KEY }}`). CE docs/scripts can reference *where* keys are stored (e.g. Azure Key Vault), not values. |
| **Company endpoints** | Internal LLM endpoints (e.g. Iron Legion `http://10.17.17.11:11437`, Ultron `http://localhost:31434/v1`) — these can live in CE override config or in a CE `continue-extension/` folder that extends Core. |
| **Company rules/prompts** | Proprietary rules, internal workflow prompts, company-specific system messages. |
| **Company MCP servers** | Internal tools, company-only commands/env. |
| **Data destinations** | If using Continue `data` for internal analytics, company endpoint and schema in CE only. |

**Current Lumina state**: Continue config is in **public** `.lumina/.continue/` (config.yaml with Ultron/Iron Legion models). No dedicated CE `continue-extension/` folder today; see “CA/IDE config: only Roo Code has a dedicated CE folder” in `LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md`. Option: add `cedarbrook-*/continue-extension/` for company overrides (e.g. extra models, company rules, MCP env).

---

## 2. Kilocode

### 2.1 OEM state (Core)

| Aspect | Details |
|--------|---------|
| **Config mechanism** | UI-first: gear icon in Kilocode chat view. Export/Import/Reset. |
| **Export file** | `kilo-code-settings.json` (typically user-chosen path, e.g. `~/Documents`). Contains API Provider Profiles and Global Settings; **API keys are exported in plaintext** — treat as sensitive. |
| **Workspace auto-launch** | `.kilocode/` in project root with `launchConfig.json`: `{"prompt":"...", "profile":"Profile Name (optional)", "mode":"mode-name (optional)"}`. |
| **Providers** | VS Code Language Model API, plus other API providers selectable in settings (Anthropic, OpenAI, etc.). |
| **No single canonical path** | Kilocode does not use a fixed repo path like `.continue/config.yaml`; config is in extension storage + optional exported JSON. |

**Core-appropriate content**: Generic `.kilocode/rules/` (e.g. ticket_number_syntax.md) and Lumina-side agent config in `config/kilo_code_optimized_config.json` (JARVIS @peak behavior, not Kilocode’s native format). Templates for `launchConfig.json` (no secrets).

### 2.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **API profiles** | Company API provider profiles (names, model IDs, endpoints). Keys via env or secret manager only. |
| **Company modes** | Internal mode names and mappings. |
| **LaunchConfig presets** | Company-specific prompt/profile/mode presets for `.kilocode/launchConfig.json`. |
| **Exported kilo-code-settings.json** | If exported for company use, store only in CE and never commit plaintext keys; use for import on company machines only. |

**Current Lumina state**: Kilocode rules live in **public** `.lumina/.kilocode/rules/`; `config/kilo_code_optimized_config.json` is Lumina/JARVIS agent config (public). No CE-only Kilocode folder. Option: add `cedarbrook-*/kilocode-extension/` with company profile presets and launchConfig templates (no secrets).

---

## 3. Roo Code

### 3.1 OEM state (Core)

| Aspect | Details |
|--------|---------|
| **Settings file** | Exported/imported as `roo-code-settings.json`. |
| **Global (extension)** | MCPs: `mcp_settings.json`; Modes: `custom_modes.json` in Roo Code extension global settings directory. |
| **Project-level** | MCPs: `.roo/mcp.json` in project root; Modes: `.roomodes` in project root. |
| **Auto-import** | VS Code setting `roo-cline.autoImportSettingsPath`: absolute path or `~/...` to a `.json` config file; Roo Code can auto-import on startup. |
| **Settings panel** | Gear icon in chat view: Export / Import / Reset. Export contains API keys in plaintext — treat as sensitive. |

**Core-appropriate content**: Generic `.roo/mcp.json` and `.roomodes` templates (no keys). Documented structure for provider profiles and modes. Public Lumina tree could hold *templates* only.

### 3.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **Full roo-code-settings.json** | Company-specific providers (e.g. Anthropic, VS Code LM, Ollama/Iron Legion), mode→profile mapping, MCP config. **Only in CE**; strip or mask keys before any share. |
| **Provider profiles** | e.g. "Iron Legion" (Ollama at company endpoint), "GitHub VSCODE" (VS Code LM), "Anthropic" — company model IDs and base URLs. |
| **Mode→API config** | Which mode (code, architect, ask, debug, orchestrator) uses which profile (e.g. ask → Iron Legion, code → GitHub VSCODE). |
| **Auto-import path** | On company machines, `roo-cline.autoImportSettingsPath` can point to CE path (e.g. `cedarbrook-*/roo-code-extension/roo-code-settings.json`) so company config is applied automatically. |

**Current Lumina state**: **CE only** — `cedarbrook-*/roo-code-extension/` contains `roo-code-settings.json` (and conflicted copy) with company profiles (Anthropic, Iron Legion, GitHub VSCODE). This is the **only** CA with a dedicated CE config folder today. Keep OEM (Core) as templates/docs; keep live company config in CE.

---

## 4. Cline

### 4.1 OEM state (Core)

| Aspect | Details |
|--------|---------|
| **Config access** | UI: `/config` in Cline REPL opens tabbed Settings. No single canonical project config file in official docs. |
| **Scopes** | Managed (system), Project (workspace), User (personal). |
| **MCP** | `cline_mcp_settings.json` (extension/IDE storage); discussion of moving MCP to VS Code `settings.json` for workspace-committable config. |
| **External config** | Feature request for `$XDG_CONFIG_HOME/cline/config.json` (or `~/.config/cline/config.json`) and `CLINE_CONFIG_FILE` / `--config` — not yet standard. |
| **Settings** | Permissions (rule syntax), sandbox, attribution, file suggestions, hooks, system prompt, sensitive file exclusion, plugins, env vars. |

**Core-appropriate content**: Lumina holds `config/cline_mcp_config.json` (Lumina-side MCP config for Cline). Generic Cline rules/docs (e.g. terminal management, MCP troubleshooting) can live in public docs; no Cline-native project config file in repo today.

### 4.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **Company rules** | Permission rules, sandbox policy, internal system prompt snippets. |
| **Company model/provider presets** | When Cline supports external config, CE could hold company provider list and model mappings. |
| **MCP server list** | Company MCP servers (commands, env) — today in Cline UI or `cline_mcp_settings.json`; if workspace config is added, CE could hold a committable MCP fragment. |
| **Docs only (current)** | CE has Cline docs (e.g. cline_terminal_management.md, cline_mcp_troubleshooting.md) but **no** dedicated `cline-extension` config folder yet. |

**Current Lumina state**: Cline config is UI/extension storage; Lumina has `config/cline_mcp_config.json` in the **public** tree. CE has documentation only. Option: add `cedarbrook-*/cline-extension/` for company rules, MCP template, and (when available) external config override.

---

## 5. PAs (Personal Assistants)

### 5.1 OEM state (Core)

| Aspect | Details |
|--------|---------|
| **JARVIS PA** | High-level personal assistant: tasks/reminders, voice (ElevenLabs TTS/STT) or text, placeholder integrations (calendar, email), context across turns. Implemented in repo (e.g. `jarvis` / scripts); not a third-party extension. |
| **Evolution / maturation** | JARVIS Evolution & Maturation Framework tracks AI, Avatar, **Personal Assistant**, and Command & Control evolution; integrated with governance, voice profile (@AIO), AIOS. |
| **Config** | PA behavior and voice/config typically live in Lumina config (e.g. `config/unified_startup_config.json`, voice/TTS configs); no single OEM “PA product” config schema from an external vendor. |

**Core-appropriate content**: Generic PA workflows, non–company-specific task/reminder logic, public voice/TTS config templates (no API keys), docs for PA evolution.

### 5.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **Company tasks/reminders** | Proprietary task lists, internal reminders, company calendar/email integration endpoints (no secrets in repo). |
| **Voice / TTS / STT** | Company ElevenLabs (or other) API refs, voice IDs, company-only endpoints; store key refs in CE docs/scripts, never values. |
| **PA evolution overrides** | Company-specific PA maturity criteria, internal governance rules. |
| **JARVIS panel / company UI** | Company-specific JARVIS panel config or desktop widget config (if any) in CE. |

**Current Lumina state**: PA logic and evolution are in the **public** tree (scripts, config, docs). CE holds company workspace tooling (e.g. JARVIS panel, company data); no dedicated `pa-extension/` or `jarvis-pa/` folder in CE today. Option: add CE folder for company PA overrides (voice refs, task sources, calendar/email endpoints) when those are formalized.

---

## 6. IDEs (Cursor, VSCode, JetBrains, Neovim)

### 6.1 OEM state (Core)

| IDE | Config path(s) | OEM behavior |
|-----|----------------|--------------|
| **Cursor** | `.cursor/settings.json`, `.cursor/mcp_config.json`, `.cursor/rules/`, `.cursor/commands/`, `.cursor/extensions.json` | VS Code–fork; workspace settings, MCP, rules, commands. User data in `%APPDATA%\Cursor` (or OS equivalent). |
| **VSCode** | `.vscode/settings.json`, `.vscode/extensions.json`, `.vscode/launch.json`, `.vscode/tasks.json` | Standard VS Code workspace config; extensions, launch, tasks. |
| **JetBrains** | Project `.idea/` or product-specific config (e.g. `*.iml`); user settings in app data. | IDE-specific; limited MCP/custom agents in Lumina context. |
| **Neovim** | `init.lua`, `~/.config/nvim/`; project via local config. | CLI; config in Lua; no built-in MCP in same way as Cursor. |

**Core-appropriate content**: Generic `.cursor/` and `.vscode/` in `.lumina/` (rules, commands, extensions.json, settings templates, MCP config templates). No secrets; placeholder endpoints only. JetBrains/Neovim: docs and example config snippets in public tree.

### 6.2 Custom configuration (CE)

| What belongs in CE | Notes |
|--------------------|--------|
| **Cursor** | Company-specific rules (`.cursor/rules/`), commands (`.cursor/commands/`), MCP env/endpoints in `mcp_config.json`; company extensions list. CE can hold overrides or full workspace config for company repos. |
| **VSCode** | Company `.vscode/` for internal projects: settings, extensions, launch/tasks pointing at company endpoints. |
| **JetBrains** | Company run configs, code styles, or shared project config in CE if Lumina standardizes JetBrains. |
| **Neovim** | Company `init.lua` or plugin/config overrides in CE if used. |

**Current Lumina state**: **Cursor** and **VSCode** config live in **public** `.lumina/.cursor/` and `.lumina/.vscode/` (settings, extensions, mcp_config, rules, commands). No separate CE-only IDE config folders; company-specific IDE tweaks can live in CE workspace copies of the same repos or in a dedicated `ide-config/` or per-IDE folder in CE when desired.

---

## 7. Summary matrix

| Type | Item | OEM config location / format | Lumina Core (public) today | CE (company) today | CE custom config (recommended) |
|------|------|------------------------------|----------------------------|--------------------|----------------------------------|
| **CA** | Continue | `config.yaml`; `.continue/`, `.continuerc.json` | `.lumina/.continue/` | None | Company endpoints, rules, MCP; optional `continue-extension/` |
| **CA** | Kilocode | UI + `kilo-code-settings.json`; `.kilocode/launchConfig.json` | `.lumina/.kilocode/rules/`, `config/kilo_code_optimized_config.json` | None | Company profiles, modes; optional `kilocode-extension/` |
| **CA** | Roo Code | `roo-code-settings.json`; `.roo/`, `roo-cline.autoImportSettingsPath` | Templates/docs | `cedarbrook-*/roo-code-extension/` | Full company config in CE; auto-import path |
| **CA** | Cline | UI `/config`; `cline_mcp_settings.json` (extension) | `config/cline_mcp_config.json` | Docs only | Company rules, MCP; optional `cline-extension/` |
| **PA** | JARVIS PA / evolution | Scripts, config (e.g. unified_startup_config), voice/TTS configs | Public tree (scripts, config, docs) | Company workspace/panel | Company voice refs, task sources, PA overrides; optional CE folder |
| **IDE** | Cursor | `.cursor/settings.json`, `mcp_config.json`, `rules/`, `commands/` | `.lumina/.cursor/` | None (or CE workspace copy) | Company rules, commands, MCP env; optional CE `cursor-extension/` |
| **IDE** | VSCode | `.vscode/settings.json`, `extensions.json`, `launch.json`, `tasks.json` | `.lumina/.vscode/` | None (or CE workspace copy) | Company settings, extensions, launch/tasks |
| **IDE** | JetBrains | `.idea/`, product config | Docs / examples | — | Company run configs, code styles if standardized |
| **IDE** | Neovim | `init.lua`, `~/.config/nvim/` | Docs / examples | — | Company init/plugin overrides if used |

---

## 8. Optionals (CE folders and config)

All optional CE folders and config choices are listed here for alignment. None are required; add when you want company-specific overrides in a dedicated CE location.

| Type | Item | Optional CE folder / location | Contents (when used) |
|------|------|-------------------------------|----------------------|
| **CA** | Continue | `cedarbrook-*/continue-extension/` | Company overrides: extra models, company rules, MCP env, data destinations. Extends or overrides `.lumina/.continue/`. |
| **CA** | Kilocode | `cedarbrook-*/kilocode-extension/` | Company profile presets, launchConfig templates (no secrets). Exported `kilo-code-settings.json` only if needed for import on company machines; never commit plaintext keys. |
| **CA** | Roo Code | *(already present)* `cedarbrook-*/roo-code-extension/` | Full company config (roo-code-settings.json). Optional Core side: `.lumina/` templates only if you want public Roo templates. |
| **CA** | Cline | `cedarbrook-*/cline-extension/` | Company rules, MCP template, and (when Cline supports it) external config override. |
| **PA** | JARVIS PA / evolution | `cedarbrook-*/pa-extension/` or `cedarbrook-*/jarvis-pa/` | Company PA overrides: voice refs, task sources, calendar/email endpoints when formalized. |
| **IDE** | Cursor | `cedarbrook-*/cursor-extension/` or `cedarbrook-*/ide-config/cursor/` | Company rules, commands, MCP env, extensions list. Overrides or extends `.lumina/.cursor/` for company repos. |
| **IDE** | VSCode | `cedarbrook-*/vscode-extension/` or `cedarbrook-*/ide-config/vscode/` | Company `.vscode/` for internal projects: settings, extensions.json, launch.json, tasks.json. |
| **IDE** | JetBrains | `cedarbrook-*/jetbrains-extension/` or `cedarbrook-*/ide-config/jetbrains/` | Company run configs, code styles, shared project config — when Lumina standardizes JetBrains. |
| **IDE** | Neovim | `cedarbrook-*/neovim-extension/` or `cedarbrook-*/ide-config/neovim/` | Company `init.lua` or plugin/config overrides — when Neovim is used in the stack. |

**Generic optional:** A single `cedarbrook-*/ide-config/` tree with subdirs per IDE (e.g. `cursor/`, `vscode/`, `jetbrains/`, `neovim/`) instead of separate `*-extension/` folders, if you prefer one place for all IDE company config.

---

## 9. Next steps

Recommended order; pick by priority and capacity.

### @peak recommendation (CA/CE alignment choice)

Given #PEAK principles — **nutrient-dense**, **small footprint**, **reusability**, **full context first** (no jump-in fix), **force multiplier** — the recommended choice for step 1 (CA/CE alignment) is:

| Priority | Choice | Rationale |
|----------|--------|-----------|
| **1** | **(B) Document the current split as intentional** | **Small footprint**: one short paragraph, no new folders. **Nutrient-dense**: clarifies intent so the inconsistency is reviewable. **Force multiplier**: one doc change removes ambiguity for everyone. **Full context first**: you already have full context (deep-dive done); documenting is the right next action before adding structure. |
| **2** | **(A) Add parallel CE folders only when needed** | If/when you actually have company overrides for Continue, Kilocode, or Cline, add that CE folder then (e.g. `continue-extension/`). **Demand-driven** keeps footprint small and **maximum utilization** (no empty structure). |
| **3** | **(C) Roo Code templates in Core** | Optional later: add generic Roo templates to `.lumina/` only if you want a single “template + CE overrides” pattern for all CAs; today Roo Code in CE already works, so this is not required for #PEAK. |

**Summary:** Do **step 1 = (B)** first (document the split in `LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md`). Add optional CE folders **(A)** only when you have concrete company config to put there. Defer **(C)** unless you standardize on “Core templates + CE overrides” for every CA.

| # | Step | Why |
|---|------|-----|
| **1** | **Decide CA/CE alignment** | Resolve the “only Roo Code has a CE folder” inconsistency. Choose: **(A)** Add parallel CE folders for Continue, Kilocode, Cline (see §8 Optionals); **(B)** Document the current split as intentional; or **(C)** Add Roo Code templates to `.lumina/` and keep CE overrides only. See `LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md` § CA/IDE config. |
| **2** | **Create CE folders (if 1 = A)** | In `cedarbrook-*/`, add only the optional CE folders you need (e.g. `continue-extension/`, `kilocode-extension/`, `cline-extension/`). Populate with company overrides (no secrets in repo). |
| **3** | **Add Core templates for Roo Code (if 1 = C)** | In `.lumina/`, add generic Roo Code templates (e.g. `.roo/` or a `roo-templates/` doc) so CE holds only overrides, not the only copy of full config. |
| **4** | **Formalize PA/IDE optionals** | If company PA overrides or IDE-specific CE config are needed, create `pa-extension/` or `ide-config/` (or per-IDE folders) in CE and document in this doc. |
| **5** | **JARVIS consolidation Phase 2** | Restructure: create directory structure from `JARVIS_CA_IDE_CONSOLIDATION_PLAN.md` §4, move agents to subdirs, preserve author credits. |
| **6** | **JARVIS consolidation Phase 3–4** | Integration (routing, tests, author display) and automation (auto-update script, monitoring). See same plan §8 Migration Plan. |
| **7** | **Review and refresh** | Periodically re-run external research for CAs/PAs/IDEs (config paths, new OEM options) and update this deep-dive and §8 Optionals. |

**Quick win:** If you do nothing else, **document the current split** (step 1 = B): one short paragraph in `LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md` stating that Continue/Kilocode are public-only, Cline has CE docs only, and Roo Code alone has a CE config folder by design (and why). That makes the inconsistency intentional and reviewable.

**Completion note (2026-01-29):** Steps 1–6 were executed: (B) documented in `LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md`; optional CE folders created in `cedarbrook-*/` (continue-extension, kilocode-extension, cline-extension, pa-extension, ide-config with cursor/vscode/jetbrains/neovim); Core Roo templates in `.lumina/roo-templates/`; JARVIS skeleton in `.lumina/jarvis/`; `config/auto_update.yaml` and `docs/system/JARVIS_PHASE_3_4_NEXT_STEPS.md` added. Populate CE folders and implement Phase 3–4 script when ready.

---

## 10. References

- Continue config reference: https://docs.continue.dev/reference/config  
- Continue understanding configs (hub vs local): https://docs.continue.dev/guides/understanding-configs  
- Kilocode settings / VS Code LM: https://kilocode.ai/docs/providers/vscode-lm , https://kilo.ai/docs/getting-started/settings  
- Kilocode auto-launch: https://kilo.ai/docs/features/auto-launch-configuration  
- Roo Code settings management: https://docs.roocode.com/features/settings-management  
- Cline provider/config: https://docs.cline.bot/provider-config/claude-code ; Cline CLI/config discussion: e.g. external config file feature request  
- Lumina: `docs/system/LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md`, `docs/JARVIS_CA_IDE_CONSOLIDATION_PLAN.md` (incl. §8 Migration Plan), `cursoride.ff.inventory.jsonc`

---

**Document version**: 1.2.0  
**Last updated**: 2026-01-29  
**Maintained by**: @JARVIS @LUMINA
