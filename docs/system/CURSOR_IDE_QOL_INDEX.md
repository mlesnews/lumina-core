# Cursor IDE customizations, features & functionality (@QOL)

**🟢 PUBLIC: GitHub Open-Source (v2.0)** — This doc is part of the public (open-source v2.0) documentation set.

**Part of Lumina Core (extension).** This index and the Cursor IDE customizations it describes are **part of Lumina Core** — the Cursor/VS Code extension and its documentation. Config, scripts, and docs referenced here live in the Lumina Core tree (`.lumina/`); the Lumina JARVIS Chat panel is part of the Lumina Core offering (extension: `applications/ide_chat`). Build/install Core: `vscode-extensions/lumina-core/build_and_install.ps1`. See `docs/system/LUMINA_EXTENSIONS_CORE_PREMIUM_NAMING.md`.

**Purpose**: Single **visible index** of all Cursor IDE customizations, additions, features, and functionality. Tagged **@QOL** (Quality of Life). If you're not seeing them, start here.

**Config (SSOT)**: `config/cursor_ide_qol_registry.json`
**Tag**: `@QOL`
**Scope**: PUBLIC (v2.0) | **Last updated**: 2026-01-31

---

## Where everything lives

| Category | What | Where |
|----------|------|--------|
| **Peak efficiency** | Agent behavior, context, model routing, task mapping | `config/CURSOR_PEAK_EFFICIENCY_CONFIG.md` |
| **Multi-IDE Cursor** | Kilo Code, Continue, Cline, config path, extensions | `config/multi_ide_optimal_settings.json` → `cursor` |
| **Model config** | ULTRON / Iron Legion for Cursor | `config/cursor_ultron_model_config.json` |
| **Retry / resilience** | Retry behavior, watchdog | `config/cursor_ide_retry_config.json` |
| **Footer & ticker** | Footer display, ticker content | `config/cursor_footer_config.json`, `config/footer_ticker_config.json` |
| **Recycle** | Warm recycle, session recycle | `config/cursor_recycle_config.json` |
| **UI auto-hide** | Auto-hide UI for more space | `config/cursor_ui_auto_hide_config.json` |
| **Voice & input** | Voice filter, voice input | `config/cursor_voice_filter_config.json` |
| **Hotkeys** | RAlt → @DOIT + Enter; F23 → @JARVIS + Voice | `config/lumina_hotkeys.json` |
| **PTRSCR (Print Screen)** | Left as OEM — no Lumina override; restore if overridden: `restore_ptrscr_to_oem.py` | `config/lumina_hotkeys.json` → `ptrscr_oem`, `scripts/python/restore_ptrscr_to_oem.py` |
| **Keyboard shortcuts** | Shortcuts, accept-all keybindings | `config/cursor_ide_keyboard_shortcuts.json`, `config/cursor_ide_complete_keyboard_shortcuts.json`, `config/cursor_keybindings_accept_all.json` |
| **Agent modes** | Mode definitions, mode tracking | `config/cursor_agent_modes.json` |
| **Pinned files** | Allowlist, cleanup | `config/cursor_ide/pinned_files_allowlist.json` |
| **Workspace** | Workspace settings, extensions, tasks, launch | `.vscode/settings.json`, `.vscode/extensions.json`, `.vscode/tasks.json`, `.vscode/launch.json` |
| **Framework** | CA/PA/IDE alignment, tiers, IP characters | `config/ca_pa_ide_framework_alignment.json` |
| **Unified CA @PEAK** | Cline, Continue, Roo, all CAs mashed into one; shared commonality; @PEAK preserved | `config/unified_ca_peak_spec.json` → `docs/system/UNIFIED_CA_PEAK_SPEC.md` |
| **JARVIS @LUMINA & @HOMELAB** | JARVIS as our personal virtual digital assistant; connected into Lumina and Homelab | `config/jarvis_lumina_homelab_connection.json` → `docs/system/JARVIS_LUMINA_HOMELAB_CONNECTION.md` |
| **JARVIS Master Chat** | Pinned JARVIS chat session, default session, agent coordination | `config/jarvis_master_chat_cursor_config.json` |
| **JARVIS chat widget** | Widget for JARVIS chat | `config/agent_widgets.json` → `jarvis_chat_widget` |
| **AI model layers (routing order)** | Foundational → second → tertiary: local, then free tier, then premium | `config/ai_model_layers.json` |
| **Local AI (foundational layer)** | Ollama (ULTRON), Iron Legion; local-first; trait routing within local | `config/cursor_ultron_model_config.json`, `config/ca_free_models_providers.json` (ollama_local / iron_legion), `cursor_local_first_interceptor.py` |
| **Free-tier virtual cluster (second level)** | Trait-matched model routing, token pool awareness, round-robin similar models | `config/free_tier_virtual_cluster.json`, `scripts/python/free_tier_cluster_router.py`, `data/free_tier_token_pools.json` |
| **Premium-tier virtual cluster (tertiary)** | Same routing for paid models; per-provider token/request limits, monthly reset | `config/premium_tier_virtual_cluster.json`, `config/ca_premium_models_providers.json`, `scripts/python/premium_tier_cluster_router.py`, `data/premium_tier_token_pools.json` |

---

## Features & functionality (@QOL)

- **Agent behavior**: timeout 120s, maxIterations 10, autoContinue, parallelToolCalls, retryOnFailure, maxRetries 3
- **Context**: maxFiles 50, maxTokens 128K, priorityFiles, excludePatterns, autoInclude, smartInclude, dependencyAnalysis
- **Model routing**: taskMapping (edit/chat/generate/refactor/debug/explain/test/document/security/optimize); ULTRON, ULTRON Coder, Iron Legion
- **Hotkeys**: RAlt → @DOIT + Enter; F23 → @JARVIS + Enter + Voice Input
- **Footer & ticker**: footer customization, ticker content
- **Retry & resilience**: retry on failure, retry watchdog
- **Recycle**: warm recycle, intelligent warm recycle
- **UI auto-hide**: auto-hide UI elements for more screen space
- **Voice & input**: voice filter, voice input integration
- **Keyboard shortcuts**: full shortcut reference, accept-all keybindings
- **Pinned files**: allowlist, cleanup
- **Kilo Code**: enabled, use_peak_patterns, use_r5_context, prefer_local_llm
- **Bones (Lumina doctor)**: single command to check config, bindings, keybindings, JARVIS connectivity; themed after Star Trek TOS Bones. See `bones.py`, `docs/system/OPENCLAW_UNIQUE_FEATURES_AND_LUMINA_FIT.md`.
- **Lumina onboard**: one CLI wizard for new user or new machine (Bones → keybindings → JARVIS pin → router test → optional MCP). See `lumina_onboard.py`.
- **AI model layers (routing order)**: **Foundational** = local AI (Ollama/ULTRON, Iron Legion); **second level** = free-tier virtual cluster; **tertiary** = premium-tier virtual cluster. Route local first, then free, then premium. See `config/ai_model_layers.json`.
- **Local AI (foundational)**: ULTRON, Iron Legion; local-first; trait routing within local endpoints.
- **Free-tier virtual cluster (second)**: request-type → model traits, token pool remaining, round-robin among similar models to preserve pool reserves (`free_tier_cluster_router.py --request-type <edit|chat|...>`).
- **Premium-tier virtual cluster (tertiary)**: same trait-matched routing for paid models (OpenAI, Anthropic, OpenRouter, Azure); per-provider token/request limits, monthly reset; API keys from env (see `ca_premium_models_providers.json` key_source). (`premium_tier_cluster_router.py --request-type <edit|chat|...>`).

---

## Scripts (automation & extensions)

Scripts live under `scripts/python/`. Key ones:

| Feature | Script(s) |
|--------|-----------|
| Footer | `cursor_ide_footer_customization.py` |
| Retry watchdog | `cursor_ide_retry_watchdog.py` |
| Warm recycle | `cursor_intelligent_warm_recycle.py` |
| UI auto-hide | `cursor_ui_auto_hide_extension.py` |
| Voice filter | `cursor_voice_filter_integration.py` |
| Shortcuts restorer / Dyno | `cursor_keyboard_shortcuts_restorer.py`, `cursor_keyboard_shortcuts_dyno_explorer.py` |
| Layout | `cursor_jarvis_layout_manager.py` |
| Todo display | `cursor_ide_todo_status_display.py`, `cursor_ide_master_todo_display.py` |
| Mode tracker | `cursor_ide_mode_tracker.py` |
| Settings optimizer | `cursor_ide_settings_optimizer.py` |
| Add new rule | `cursor_add_new_rule_integration.py` |
| Workspace sync / mode | `cursor_workspace_sync_cron.py`, `cursor_workspace_mode_manager.py` |
| Pinned files | `cursor_pinned_file_manager.py`, `cursor_cleanup_pinned_files.py` |
| Chat / agent | `cursor_chat_manager.py`, `cursor_agent_chat_renamer.py`, `cursor_agent_history_processor.py`, etc. |
| Free-tier cluster router | `free_tier_cluster_router.py` — trait match + token pool + round-robin (`--request-type edit|chat|generate|...`) |
| Premium-tier cluster router | `premium_tier_cluster_router.py` — same for paid models; per-provider pools, monthly reset; keys from env |
| Notifications | `cursor_notification_handler.py`, `cursor_notification_queue_manager.py` |
| Connection | `cursor_connection_health_monitor.py`, `cursor_connection_resilience.py` |
| Local first | `cursor_local_first_interceptor.py` |
| Error / performance | `cursor_ide_error_monitor.py`, `cursor_ide_performance_fix.py` |
| Auto-accept / feature track | `cursor_ide_auto_accept.py`, `cursor_ide_feature_utilization_tracker.py` |
| R2-D2 sounds | `cursor_ide_r2d2_sounds.py` |
| **Bones (Lumina doctor)** | `bones.py` — health check: config, bindings, keybindings, JARVIS connectivity. Star Trek TOS Bones; `--persona` for alternate Trek doctors. |
| **Lumina onboard** | `lumina_onboard.py` — one CLI wizard: Bones → keybindings → JARVIS pin → router test → optional MCP. |
| **Session tools** | `session_tools.py` — list, history, send (sessions_list, sessions_history, sessions_send); reply-back. |
| **Skills registry** | `lumina_skills_registry.py` + `config/lumina_skills_registry.json` — discover/list/check skills (.cursor/skills). |
| **Per-session tool allowlists** | `config/per_session_tool_allowlists.json` — per-character allowlist/denylist. |
| **Trigger contract** | `docs/system/TRIGGER_CONTRACT.md` — cron, webhook, pub/sub. |

Full list: **`config/cursor_ide_qol_registry.json`** → `scripts`.

---

## Full utilization (IDE / CA / frameworks)

- **Master audit**: **`docs/system/IDE_CA_FRAMEWORK_FULL_UTILIZATION.md`** — Cursor feature-by-feature utilization, other IDEs (VS Code, JetBrains, Neovim), all CAs (Kilo Code, Continue, Cline, Roo), and #frameworks (rules, skills, MCP, request workflow, helpdesk, etc.). Use it to confirm every feature/functionality is customized and used to the fullest.

---

## Docs (setup, workflow, troubleshooting)

- **Peak efficiency**: `config/CURSOR_PEAK_EFFICIENCY_CONFIG.md`
- **Kilo Code setup**: `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **Workflow**: `docs/workflow/CURSOR_WORKFLOW_SOLUTIONS.md`, `docs/workflow/CURSOR_IDE_WORKFLOW_PAIN_POINTS.md`
- **Keyboard shortcuts**: `docs/workflow/CURSOR_KEYBOARD_SHORTCUTS.md`
- **Local AI / connection / errors**: `docs/helpdesk/CURSOR_LOCAL_AI_INVESTIGATION_BRIEF.md`, `docs/system/CURSOR_CONNECTION_STALLED_QUICK_FIX.md`, `docs/system/CURSOR_INTERNAL_ERROR_WORKAROUND.md`, `docs/system/CURSOR_LOCAL_AI_FIX_CHECKLIST.md`
- **Custom models**: `docs/CURSOR_CUSTOM_MODELS_AND_LOCAL_AI.md`
- **Pinned files / todo**: `docs/system/CURSOR_PINNED_FILES_CLEANUP_SUMMARY.md`, `docs/CURSOR_IDE_TODO_PIN_LIMITATION.md`
- **Control plane contract**: `docs/system/CONTROL_PLANE_CONTRACT.md` — route request, list/send sessions, run tool; JARVIS + CAs.
- **Trigger contract**: `docs/system/TRIGGER_CONTRACT.md` — cron, webhook, pub/sub; run on schedule / run on event.

Full list: **`config/cursor_ide_qol_registry.json`** → `docs`.

---

## Why aren't all Lumina features available? (Notably a chat interface like Kilo Code)

Lumina is delivered in **three layers**; only the first is a single extension you install:

| Layer | What | Why you might not see it |
|-------|------|---------------------------|
| **1. Lumina Core (one extension)** | Activity Bar icon, Lumina sidebar (webview, Cline-style; opens JARVIS Chat), File Cleanup Stack under Explorer, many commands. | You must **build and install** the VSIX: `.\vscode-extensions\lumina-core\build_and_install.ps1`. It’s not on the marketplace. |
| **2. Config + scripts** | Hotkeys, footer, retry, recycle, voice, shortcuts, pinned files, chat session pinning. | These are **config files and Python scripts** applied to Cursor/settings or run separately; they’re not inside the extension. |
| **3. Lumina JARVIS Chat (second extension)** | **Custom chat panel** — dedicated JARVIS UI, branding, local ULTRON, like Kilo Code’s tailored experience. | This is a **separate extension** (`applications/ide_chat`). It is **not** bundled with Lumina Core. You must build and install it: see **“Lumina JARVIS Chat (custom panel)”** below. |

So: **“All Lumina features”** = Lumina Core (sidebar + Lumina welcome; File Cleanup Stack under Explorer + commands) **plus** applied config/scripts **plus** the **JARVIS Chat extension** if you want a chat interface like Kilo Code. To get the **custom chat interface** (JARVIS panel like Kilo Code), install **both** Lumina Core and Lumina JARVIS Chat; see the JARVIS chat section and the build/install steps for `applications/ide_chat`.

---

## Where is JARVIS chat?

**Two different things:**

| What you see | What it is |
|--------------|------------|
| **Cursor default IDE AI chat** | OEM Cursor chat — built-in interface. Same UI for every session. |
| **Lumina JARVIS AI chat** | **Custom** JARVIS chat interface — dedicated panel, JARVIS branding, queue, workflow, R5. Like Kilo Code but for JARVIS. |

**Lumina JARVIS custom chat (built):** A **dedicated JARVIS chat panel** with JARVIS branding and local ULTRON is available via the **Lumina JARVIS Chat** extension — **part of Lumina Core** (companion extension in the Core set).

- **Lumina JARVIS Chat (custom panel)**: **Dedicated panel** — not the OEM Cursor chat. **Separate extension**: **`applications/ide_chat`** (display name: **Lumina JARVIS Chat**, id: `cedarbrook-financial-services.jarvis-ide-chat`). **How to use:** (1) **Build and install**: from repo root run `.\applications\ide_chat\build_and_install.ps1` (or open `applications/ide_chat`, run **Tasks: Run Task** → **Compile**, then **Developer: Install Extension from Location...** and choose `applications/ide_chat`). (2) Run command **Lumina: Open JARVIS Chat** (Command Palette or Lumina sidebar) or bind a key to `jarvis.chat.open`. (3) Ensure Ollama (ULTRON) is running on `localhost:11434`. Config: **`jarvis.chat.apiBaseUrl`** (default `http://localhost:11434/v1`), **`jarvis.chat.model`** (default `ULTRON`). Spec/expectation: **`docs/system/JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`**.
- **In Cursor (OEM workaround)**: JARVIS Master Chat as a **pinned session** inside Cursor’s OEM chat. Open Chat (Ctrl+L / Ctrl+Alt+L); use the session dropdown to select “JARVIS Master Chat - All Agents” if needed. Config: **`config/jarvis_master_chat_cursor_config.json`**. To re-apply: `python scripts/python/apply_jarvis_pinned_to_cursor_settings.py`, then restart Cursor.
- **Fallback when JARVIS doesn’t work**: Use the **default Cursor chat** as fallback (chat session dropdown → new chat or default). Run `python scripts/python/check_jarvis_chat_backends.py` to see which backend is up.
- **Local JARVIS chat (separate window)**: WoW-style server + UI. **`docs/JARVIS_LOCAL_CHAT_GUIDE.md`**. Server: `python scripts/python/jarvis_local_chat_system.py --server --host 0.0.0.0 --port 8888`. UI: `python scripts/python/jarvis_chat_ui.py --host localhost --port 8888`.
- **Architecture / summary**: **`docs/system/JARVIS_CHAT_INTERFACE_SUMMARY.md`**, **`docs/system/JARVIS_IDE_CHAT_INTERFACE_ARCHITECTURE.md`**, **`docs/JARVIS_AI_CHAT_PEAK_SPEC.md`**.
- **Widget**: **`config/agent_widgets.json`** → `jarvis_chat_widget`.

### After reboot (post-reboot readiness)

JARVIS chat **surface** (pinned session, keybinding) is persisted in Cursor config and works once Cursor is open. The **AI** (replies from a model) works only if at least one backend is running: **Ollama (ULTRON)** on `localhost:11434` and/or **Iron Legion (Kaiju)** on `10.17.17.11:11437`.

**Checklist after reboot:**

1. **Start Cursor** (Cursor does not auto-start).
2. **Start Ollama** if it’s not set to start at Windows login — otherwise Chat has no local backend and messages may hang.
3. **Optional**: Run AutoHotkey (or your hotkey host) if you use **RAlt** / **F23** for @DOIT / @JARVIS.
4. **Open Chat**: **Ctrl+Alt+L** or **Ctrl+L** → Chat opens with JARVIS pinned session.
5. **If Chat doesn’t respond**: Use the **default Cursor chat** as fallback (chat session dropdown → new chat or default). Run `python scripts/python/check_jarvis_chat_backends.py` to see which backend is up (ULTRON, Iron Legion, or none). Ensure Ollama is running or Iron Legion (Kaiju) is on when you want to use JARVIS again.

**Optional**: Add Cursor and/or Ollama to Windows Startup (e.g. Task Scheduler or shell:startup) so after reboot you only need to wait for them to start. See **`docs/system/JARVIS_CHAT_AFTER_REBOOT_5W1H_AND_GAPS.md`** for full 5W1H reasoning and gap-closing actions.

### JARVIS Chat UI/UX expectation (Kilo Code as example)

**Our expectation**: A **customized chat UI/UX** as the **JARVIS-to-human interface** — not just default IDE chat with a pinned session. The **Kilo Code extension** is the **example**: it provides a distinct, tailored CA experience (modes, profiles, panel, rules, MCP, R5). We want the same level of customization for JARVIS: a dedicated JARVIS chat panel/sidebar, JARVIS branding, queue, workflow status, R5/@helpdesk shortcuts — ideally via a **JARVIS Chat extension** (or equivalent) in Cursor/VS Code.

**Spec**: **`docs/system/JARVIS_CHAT_UI_UX_EXPECTATION_KILO_CODE_EXAMPLE.md`**

---

## Troubleshooting

### “Command 'Lumina: Open Lumina AI Chat' resulted in an error” / `lumina.openLuminaAIChat` not found

**Cause**: The command `lumina.openLuminaAIChat` is **not registered** — a Lumina/JARVIS Chat extension that would provide it does not exist yet (see JARVIS Chat UI/UX expectation below).

**Workaround**:

1. **Apply all steps (one-shot)**: `python scripts/python/apply_lumina_chat_workaround_all.py` — runs: keybinding fix, JARVIS consolidate+pin, and JARVIS pinned config into Cursor user settings. Restart Cursor after.
2. **Open Cursor Chat**: **Ctrl+L** (Windows/Linux) or **Cmd+L** (macOS), or **Ctrl+Alt+L** (Lumina fallback). Command: `workbench.action.openChat`.
3. **Individual steps**: `fix_lumina_open_chat_keybinding.py` (remap + Ctrl+Alt+L); `jarvis_master_chat_session.py --consolidate --pin`; `apply_jarvis_pinned_to_cursor_settings.py` (merge JARVIS pinned into Cursor settings).
4. **Rebind manually**: Keyboard Shortcuts → search “Lumina” or “Open Chat” → set the key to **Cursor: Open Chat** (`workbench.action.openChat`).

---

### "Lumina Core" not in Output dropdown / extension reported a message

- In **Extensions** (Ctrl+Shift+X), if Lumina Core shows **"This extension has reported 1 message"**, click that line (or the red X) to open the message. That message often explains why the extension failed to activate or why the **Lumina Core** output channel was never created.
- Then try **Ctrl+Shift+P** → **"Lumina: Show Lumina Core Output"**. That command creates and shows the Lumina Core log channel if the extension activates.
- If the extension still doesn’t create the channel, check **Help → Toggle Developer Tools → Console** for errors mentioning `lumina-core` or `extension host`; those can show load/activation failures.

### Lumina stalled / green horizontal progress bar stuck

**Symptom**: Lumina shows only a green horizontal progress bar that scrolls and never finishes.

**Cause**: The LUMINA progress display reads `data/progress_status.json`. If that file has an old "Starting" or in-progress state and nothing updates it to "Ready", the status bar and progress panel show the bar indefinitely.

**Fix** (use any one):

1. **Manual reset (works immediately, no rebuild)**: Create or overwrite **`data/progress_status.json`** in your **workspace root** (the first folder in your workspace) with:

   ```json
   {"agent":"JARVIS","status":"Ready","progress":100,"message":"","timestamp":"2026-01-29T00:00:00.000Z"}
   ```

   The extension reads this every few seconds; the bar should switch to "Ready" shortly.
2. **Command (after rebuild)**: **Ctrl+Shift+P** → run **"Reset LUMINA Progress Display (unstall green bar)"** (under Lumina). This command exists only in a **rebuilt** Lumina Core extension. If you don't see it, use the manual reset above or rebuild (step 3).
3. **Auto-stale**: The extension treats progress as **stale** after 90 seconds and shows "Ready". Wait ~90s and the status bar may update.
4. **Rebuild and install** (to get the command): From repo root run `.\vscode-extensions\lumina-core\build_and_install.ps1`, then **Developer: Reload Window**. Or install the built VSIX manually: **Extensions** → **...** → **Install from VSIX...** → choose `vscode-extensions\lumina-core\lumina-core-2.0.9.vsix` → Reload Window.

---

## Lumina in Extensions list and Sidebar (like Kilo Code, Continue, GitLens)

**Lumina Core** is not on the marketplace; you install it from the local VSIX. Until it’s installed, **Lumina won’t appear** in the Extensions list or as a sidebar (Activity Bar) icon.

**To see Lumina in Extensions and as a sidebar icon:**

1. **Build and install** (from repo root):
   `.\vscode-extensions\lumina-core\build_and_install.ps1`
   This compiles the extension, packages the VSIX, and installs it into Cursor.
2. **Reload Cursor** (Developer: Reload Window or restart Cursor).
3. **Extensions**: You should see **“Lumina Core - Open Source Lumina Ecosystem”** (publisher: lumina) in the Extensions list.
4. **Sidebar**: You should see a **Lumina** icon (sparkle) in the Activity Bar (left sidebar) next to Explorer, Kilo Code, Continue, GitLens, etc. Click it to open the Lumina sidebar (webview, like Cline/Kilo Code; opens JARVIS Chat). **File Cleanup Stack** is under the **Explorer** sidebar. Skeleton pattern: `docs/system/LUMINA_SIDEBAR_SKELETON_CLINE_PATTERN.md`.

The workspace **recommends** Lumina Core (`.vscode/extensions.json`). If Cursor prompts “This workspace recommends extensions,” accept **Lumina Core**; you still need to install from the VSIX (step 1) because it’s not published to the marketplace.

---

## Quick checklist: “I’m not seeing Cursor customizations”

1. **Lumina in Extensions/sidebar**: Install Lumina Core from VSIX: `.\vscode-extensions\lumina-core\build_and_install.ps1`, then reload Cursor. **To see what might be wrong:** Open **View → Output**, then in the Output panel’s **dropdown** (top-right of the Output pane) select **"Lumina Core"** (not "Lumina" — the channel name is "Lumina Core"). The channel is created and shown automatically when the extension activates; the last line in that log shows where activation reached or where it stalled. You can also run **Lumina: Show Lumina Core Output** (Ctrl+Shift+P) to open the channel. If "Lumina Core" does not appear in the dropdown, the extension may not have activated yet — ensure Lumina Core is installed and reload the window; the extension activates on startup (`onStartupFinished`). See `docs/system/LUMINA_SIDEBAR_SKELETON_CLINE_PATTERN.md`.
2. **Chat interface like Kilo Code (JARVIS custom panel)**: Install Lumina JARVIS Chat: `.\applications\ide_chat\build_and_install.ps1`, then reload. Use **Lumina: Open JARVIS Chat** (Command Palette or Lumina).
3. **Settings**: Merge or apply `config/CURSOR_PEAK_EFFICIENCY_CONFIG.md` into Cursor settings (or `~/.cursor/settings.json`).
4. **Multi-IDE**: Ensure `config/multi_ide_optimal_settings.json` → `cursor` settings and recommended extensions are applied.
5. **Hotkeys**: Ensure `config/lumina_hotkeys.json` is active (e.g. AutoHotkey or equivalent) for RAlt → @DOIT, F23 → @JARVIS.
6. **Extensions**: Check `.vscode/extensions.json` and install recommended (Lumina Core, Lumina JARVIS Chat, Kilo Code, Continue, GitLens, etc.).
7. **Registry**: Open **`config/cursor_ide_qol_registry.json`** for the full list of configs, features, scripts, and docs.

---

## Reboot: fully automatic (no manual steps)

- **One command**: `.\scripts\powershell\lumina_reboot_auto.ps1 -Restart` — closes Cursor, stops Ollama/Docker, restarts PC. No prompts. Post-reboot verify runs automatically at logon (install task once with `-Install` or by running `-Restart` once).
- **Shutdown (power off)**: `.\scripts\powershell\lumina_reboot_auto.ps1 -Shutdown`
- **Full flow & monitoring**: **`docs/system/REBOOT_MONITOR_SHUTDOWN_STARTUP.md`**

---

## References

- **CA activation comparison**: `docs/system/LUMINA_CA_ACTIVATION_COMPARISON.md` — Lumina vs Cline and other CAs (setup, startup, activation events); Lumina Core now uses `onStartupFinished` like the other CAs so all commands and status bars are available from the start.
- **SSOT registry**: `config/cursor_ide_qol_registry.json`
- **Kilo Code / tiers**: `config/ip_character_cluster_tiers.json`, `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`
- **CA/PA/IDE framework**: `config/ca_pa_ide_framework_alignment.json`
- **Lumina SSOT**: `config/lumina_ssot_registry.json` (Cursor IDE, extensions, settings refs)
- **AI model layers**: `config/ai_model_layers.json` — foundational (local) → second (free tier) → tertiary (premium).
- **Local AI (foundational)**: `config/cursor_ultron_model_config.json`, `config/local_first_ai_enforcement.json`
- **Free-tier cluster**: `config/free_tier_virtual_cluster.json`, `config/ca_free_models_providers.json`
- **Premium-tier cluster**: `config/premium_tier_virtual_cluster.json`, `config/ca_premium_models_providers.json` (no secrets; keys from env)
