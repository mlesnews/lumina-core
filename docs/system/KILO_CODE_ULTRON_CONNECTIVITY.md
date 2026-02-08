# Kilo Code + Ultron Connectivity

<!-- cspell:ignore Ultron Ollama helpdesk kilocode Kilocode SSOT api_conversation_history -->

**Purpose**: Fix Kilo Code "API request keeps spinning" when using Ultron (local Ollama).  
**Last updated**: 2026-01-30  
**PM Ticket**: PM000003178  
**Investigation brief**: `docs/helpdesk/KILO_CODE_ULTRON_INVESTIGATION_BRIEF.md`

---

## Cause

Kilo Code was pointing at **<http://localhost:11437>**. On the laptop, **Ultron (Ollama)** runs on the default port **11434**. Nothing listens on 11437, so requests hang.

---

## 1. Fix in Kilo Code (required)

Kilo Code uses **its own settings** (gear icon in Kilo Code chat view), not `config/kilo_code_optimized_config.json`. Our repo config is for JARVIS/@peak behavior only.

1. **Open Kilo Code settings** (gear in Kilo Code panel).
2. Find the **API provider profile** used for your test (e.g. Ollama or "Ultron").
3. Set **base URL** to:
   - **<http://localhost:11434>** (Ollama default), or  
   - **<http://localhost:11434/v1>** if the profile expects an OpenAI-compatible base path.
4. Save and try your Hello World again.

---

## 2. Ensure Ollama is running (Ultron)

```powershell
# Is Ollama up?
Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing

# If it fails, start Ollama:
ollama serve

# Models available?
ollama list
# If needed: ollama pull qwen2.5-coder:7b  (or the model your Kilo Code profile uses)
```

---

## 3. Repo config (already updated)

In `config/kilo_code_optimized_config.json`, `primary_llm.base_url` was changed from `http://localhost:11437` to **<http://localhost:11434>**, so any tooling that reads this file uses Ultron correctly. Kilo Code’s UI/storage still overrides this; fix the profile in Kilo Code as in section 1.

---

## 4. If it still spins

- **Restart Cursor** after changing Kilo Code settings.
- Confirm the **model name** in the Kilo Code profile matches a model you have (`ollama list`), e.g. `qwen2.5-coder:7b`, `llama3.2:3b`.
- See `docs/system/CURSOR_LOCAL_AI_FIX_CHECKLIST.md` and `docs/system/CURSOR_CONNECTION_STALLED_QUICK_FIX.md` for Ollama and Cursor checks.

---

## 4a. "Task file not found" (Kilo Code panel)

Kilo Code may show **"Task file not found for task ID: … (file … api_conversation_history.json)"**. That means the extension is looking for a task’s conversation file under Cursor’s `globalStorage\\kilocode.kilo-code\\tasks\\<taskId>\\` and the file is missing (stale task, failed write, or corrupted state).

**What to do:**

1. **Use a new task/chat** – Start a **new** Kilo Code chat/task (e.g. new "Hello World"), so it creates a new task and new `api_conversation_history.json`. Don’t reopen the old task IDs that already show the error.
2. **Set API profile first** – In Kilo Code settings (gear), set base URL to **<http://localhost:11434>** (or **<http://localhost:11434/v1>**), then run the new test. Spinning + missing file often go together when the profile was wrong.
3. **Optional – clear Kilo Code task storage** – If "Task file not found" keeps appearing for old task IDs, run the script, so Kilo Code starts with a clean task set:
   - **Ctrl+Shift+P** → **Tasks: Run Task** → **Kilo Code: Clear task storage (fix Task file not found)**  
   - Or: `.\scripts\powershell\clear_kilo_code_task_storage.ps1` from repo root.  
   The script renames `%APPDATA%\Cursor\User\globalStorage\kilocode.kilo-code\tasks` to a backup folder. Then **Reload Cursor** and set the API profile to <http://localhost:11434>. Finally, start a **new** Kilo Code chat.
4. **Ignore old errors** – The pop-up for an old task ID (e.g. 019c1238-…) can be dismissed; it doesn’t block new tasks once the profile is correct and you use a new chat.

---

## 4c. "Prompt is too long" (context window)

Kilo Code may report: **"Prompt is too long (estimated tokens: N, max tokens: 4096). Increase the Context Window Size in Settings."** The prompt includes your message plus injected context (open tabs, `.kilocode` rules, workspace file list), which can exceed 16k tokens even for a short "hello world" in a large repo.

**Fix:**

1. **Increase Context Window Size** – In Kilo Code settings (gear) → your Ollama/Ultron profile, find **Context Window Size (num_ctx)** and set it to **16384** or **32768** (Kilo Code recommends at least 32k for local models).
2. **Save** and start a **new** chat; retry your request.
3. **Optional** – Reduce injected context: close unneeded tabs and/or trim `.kilocode/rules` so fewer rules are included in each request.

---

## 4b. Request still spinning after changing profile

If you set the base URL to **<http://localhost:11434>** but the Kilo Code request still spins:

1. **Cancel the current request** – In the Kilo Code panel, click **Cancel** so the stuck request stops.
2. **Confirm Ollama** – In a terminal: `Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing`. If it fails, run `ollama serve`.
3. **Reload Cursor** – **Ctrl+Shift+P** → **Developer: Reload Window**. Kilo Code must reload to use the new API profile.
4. **New chat only** – After reload, open Kilo Code and start a **new** chat (don’t reopen “hello world”). Run a simple “Hello World” again.
5. **Profile name** – In Kilo Code settings (gear), ensure the profile you’re using for this chat is the one with base URL **<http://localhost:11434>** (or **<http://localhost:11434/v1>**). If you have several API profiles, pick the correct one in the chat/task.
6. **VS Code Language Model** – If Kilo Code is set to use “VS Code Language Model API”, it uses Cursor’s models instead of a direct URL. Then ensure Cursor’s model selector is set to **ULTRON** (localhost:11434), and that Cursor chat works; Kilo Code will use that.

---

## 5. Acceptance criteria (QA)

- [ ] Ollama reachable: `http://localhost:11434/api/tags` returns 200 when Ollama is running.
- [ ] Kilo Code profile base URL set to **<http://localhost:11434>** (or **<http://localhost:11434/v1>**).
- [ ] Kilo Code **Context Window Size** set to **16384** or **32768** (not 4096) so injected context (rules, tabs, workspace) fits.
- [ ] Kilo Code Hello World (or equivalent) completes without spinning or "Prompt is too long".
- [ ] Diagnostic passes: `python scripts/python/diagnose_kilo_code_ultron_connectivity.py` exits 0.

---

## 6. Done-right state

- **SSOT**: Ultron (laptop) Ollama = **<http://localhost:11434>** in `config/host_identity_registry.json` and all docs. Port **11437** on laptop = MCP/WS only; never Ollama.
- **Kilo Code**: User sets base URL to 11434 in Kilo Code UI (gear); repo config (`config/kilo_code_optimized_config.json`) aligned to 11434 for tooling.
- **Validation**: Run diagnostic before closing PM000003178; see investigation brief for full criteria.
- **Secrets**: Kilo Code must never suggest code that prints or logs API keys, passwords, or tokens. See `.kilocode/rules/no_secrets_broadcast.md` and `.kilocode/rules/secrets.md`. **Lumina Core** users can run **Lumina: Apply Kilo Code Setup** (Ctrl+Shift+P) to copy these rules into the workspace if missing.

---

## 7. Diagnostic

```powershell
# From repo root
python scripts/python/diagnose_kilo_code_ultron_connectivity.py
```

Exit 0 = Ollama reachable and repo config aligned; exit 1 = fix recommendations printed.

---

## 8. Automated prepare (run this first)

**One-click (Cursor)**: **Ctrl+Shift+P** → **Tasks: Run Task** → **Kilo Code + Ultron: Prepare**.

**Or from repo root (PowerShell)**:

```powershell
.\scripts\powershell\prepare_kilo_code_ultron.ps1
```

This script:

1. Checks if Ollama is reachable at <http://localhost:11434>; if not, starts `ollama serve` in the background.
2. Runs the Kilo Code + Ultron diagnostic.
3. Prints the next manual steps (reload Cursor, set Kilo Code profile base URL, start a new chat).

Kilo Code’s API profile (base URL) must still be set in the Kilo Code UI (gear); the script cannot change that.

---

## 9. Using Kilo Code as a cluster (multiple LLMs)

For **per-model profiles**, **context windows above 32K** (64K/128K where supported), and config-driven setup, see **`docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md`** and **`config/kilo_code_cluster_profiles.json`**.

To use **multiple LLMs** (not a single Ollama instance), you have two patterns.

### Option A: Multiple Kilo Code profiles (cluster-by-choice)

Create **separate API profiles** in Kilo Code (gear → Providers → Add/Edit), one per backend. Pick the profile **per chat or per task**.

| Profile name   | Base URL (Ollama)              | When to use |
|----------------|--------------------------------|-------------|
| **ULTRON**     | `http://localhost:11434` or `/v1` | Laptop local; fast, offline. |
| **Iron Legion** | `http://10.17.17.11:11434` or `http://10.17.17.11:3000/v1` (if Kaiju runs a router) | Desktop Kaiju; heavier models. |
| **Cloud** (optional) | Your OpenAI/Anthropic base URL | When you want cloud and approve usage. |

- Endpoints come from **`config/host_identity_registry.json`** → `cluster_endpoints_derived` (e.g. `ultron.primary`, `iron_legion_kaiju.ollama` or `expert_router`).
- Each profile has its own **Context Window Size** (e.g. 32768) and **model** (e.g. `qwen2.5:7b`, `codellama:13b`).
- You switch “cluster” by **choosing the profile** in the Kilo Code chat/task; no automatic routing.

### Option B: Single gateway (cluster-by-routing)

If you run a **single router/gateway** that forwards to multiple backends (e.g. by model or load), point **one** Kilo Code profile at that gateway.

- **Ultron (laptop)**: `cluster_endpoints_derived.ultron.router` = `http://localhost:8080` (if you run a router there).
- **Kaiju**: `cluster_endpoints_derived.iron_legion_kaiju.expert_router` = `http://10.17.17.11:3000/expert` (if Kaiju exposes an expert router).

Set the profile **Base URL** to that gateway; the gateway decides which LLM handles the request. Kilo Code stays on one profile; the cluster is behind the gateway.

**There is no “router LLM” you select in Kilo Code.** You must set a **Model ID** in Kilo Code (it cannot be blank). The “router” here is an **HTTP gateway** (a service at a URL like `http://localhost:8080`), not a model. In Kilo Code you only set **Base URL** to that gateway; the **Model ID** should be whatever the gateway expects (e.g. `auto`, or a specific model name the gateway maps to a backend). If your gateway uses a small LLM internally to decide which backend to call, that “router LLM” is configured in the gateway itself, not in Kilo Code.

**Which Model ID to choose:** Use a **concrete model name** your cluster provides and the gateway understands – e.g. `qwen2.5:7b`, `llama3.2:3b`, or `qwen2.5-coder:7b`. That value is the **target model** for the request (what the gateway should use or route to), not a “router” model. Pick the model you want this chat/task to use (e.g. `qwen2.5:7b` for general use, `llama3.2:3b` for lighter load). That satisfies Kilo Code’s “valid model ID” requirement and tells the gateway which model to use. If your gateway documents a special value (e.g. `auto`), use that instead.

**Modes and model choice:** Kilo Code has **Modes** (e.g. Code, Architect, Ask, Debug, Orchestrator, Review) under **Agent Behaviour → Modes**. Align **Model ID** with the mode when it makes sense: for **Code** mode use a coding-focused model (e.g. `qwen2.5-coder:7b`); for Ask, Review, or Architect you might use a general or larger model. You can create **custom modes** as needed; each mode can have its own **Agent Behaviour** (Modes, MCP Servers, Rules, Workflows, Skills) and thus its own model choice per profile. So: one profile (e.g. gateway at 8080) can still serve all modes; pick the Model ID that fits the mode you’re using for that chat/task, or configure mode-specific behaviour in Kilo Code where supported.

### Multiple models on one Ollama (not “cluster”)

On a **single** Ollama (e.g. Ultron at 11434), you still pick the **model** in Kilo Code (e.g. `qwen2.5:7b`, `llama3.2:3b`, `qwen2-72b:latest`). That is multiple models on one server, not multiple servers. For true multi-LLM (different machines or routing), use Option A or B above.

---

**Reference**: `config/host_identity_registry.json` (Ultron = <http://localhost:11434>), `config/host_identity_registry.json` → `cluster_endpoints_derived`, `docs/system/ENDPOINT_SSOT_ULTRON_KILO_CODE.md`, `docs/system/KILO_CODE_CLUSTER_PER_MODEL_SETUP.md` (per-model profiles, >32K context), `config/kilo_code_cluster_profiles.json`, `docs/system/CA_OEM_AND_CE_CONFIG_DEEP_DIVE.md` (Kilocode config mechanism), `docs/helpdesk/KILO_CODE_ULTRON_INVESTIGATION_BRIEF.md`.
