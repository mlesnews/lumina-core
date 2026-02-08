# JARVIS IDE Problems Contract

**Expectation:** @Jarvis works on **every problem detected** in the IDE (Cursor), delegating to subagents and #frameworks as needed.

**Tags:** #JARVIS #IDE #NOTIFICATIONS #CONTRACT #AUTOMATION

---

## Contract

1. **Every problem detected** (Problems panel, MCP configuration errors, terminal errors, lint/Diagnostics) is in scope for JARVIS.
2. **JARVIS** either resolves the problem directly or **delegates** to subagents and **#frameworks** (e.g. #troubleshooting, #BAU, helpdesk PM, fix_underlying_problem) as needed.
3. **IDE notification code** (e.g. `jarvis_ide_notification_monitor.py`) is **used**, not left dormant: it runs on folder open and can be run manually; it drives MCP config checks, Git handling, and recommendations.

---

## How it’s wired today

| Mechanism | What it does |
|-----------|----------------|
| **Task: JARVIS: Monitor IDE Notifications** | Runs `jarvis_ide_notification_monitor.py --monitor` (Git + MCP config + Docker gateway). **Run on:** folder open (`runOptions.runOn: folderOpen`) and manually. |
| **Task: JARVIS: MCP Check** | Runs `--mcp-check` (MCP config + gateway only). |
| **MCP config error** | Monitor includes pattern for "must have command or url" / "cursor-browser-extension" / "MCP configuration errors"; suggests running `fix_mcp_notifications_laptop.ps1`. |
| **Fix scripts** | `fix_mcp_notifications_laptop.ps1` and `setup_mcp_ultron.ps1` write user `mcp.json` with **empty mcpServers** so the project’s MCP_DOCKER is the only MCP entry and Cursor stops showing the cursor-browser-extension error. |

---

## Enabling “every problem” automation

- **On folder open:** The monitor task is set to `runOn: folderOpen` so it runs when you open the Lumina workspace.
- **On problem change:** Cursor does not expose a “run task when diagnostics change” in tasks.json. To have JARVIS run on **every** new problem as it appears you would need one of:
  - A **Cursor Hook** (if available) that fires on diagnostics change and invokes the monitor or an agent.
  - An **extension** that subscribes to `vscode.languages.onDidChangeDiagnostics` and triggers the monitor or opens a JARVIS task.
  - **Manual or periodic:** Run **JARVIS: Monitor IDE Notifications** (or **JARVIS: MCP Check** for MCP-only) when you want JARVIS to react; or run the monitor on a schedule (e.g. via a cron or background script).

---

## What to do when you see the MCP config error

1. Run `scripts/fix_mcp_notifications_laptop.ps1` (or set user `~/.cursor/mcp.json` to `{"mcpServers":{}}`).
2. Restart Cursor.
3. In **Settings → Tools & MCP**, turn **MCP_DOCKER** **On** if it is disabled.
4. Run **JARVIS: MCP Check** to confirm config and gateway.

---

## References

- `scripts/python/jarvis_ide_notification_monitor.py` – Git, MCP, and notification patterns
- `scripts/fix_mcp_notifications_laptop.ps1` – Clears user mcpServers to fix the cursor-browser-extension error
- `.cursor/tasks.json` – JARVIS: Monitor IDE Notifications (runOn: folderOpen)
- `docs/system/MCP_MULTI_MACHINE_SETUP.md` – MCP troubleshooting
