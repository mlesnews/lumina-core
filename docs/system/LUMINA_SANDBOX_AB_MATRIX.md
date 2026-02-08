# LUMINA A/B Sandbox Matrix — Required Workaround for Cursor Network Block

**Date**: 2026-01-29  
**Status**: Required workaround. Cursor Agent–invoked terminals have no network access; LUMINA B-Side runs outside that sandbox and executes network-requiring commands via file handoff.

---

## The Matrix

| Side | Name | Who runs it | Network | Use for |
|------|------|-------------|---------|--------|
| **A** | Cursor Sandbox | Cursor IDE (Agent / Run) | ❌ Blocked | Editing, reading, running commands that don’t need network; **submitting** B-Side requests (file I/O only). |
| **B** | Lumina Sandbox | Our daemon (user or Task Scheduler) | ✅ Allowed | Running scripts that need network: drive mapping, backups, NAS deploy, Key Vault, etc. |

- **A-Side**: Safe zone controlled by Cursor — workspace read/write, no internet. The Agent lives here.
- **B-Side**: Safe zone we control — same machine, full network, allowlisted scripts only. We customize it (e.g. allow network) so Cursor’s hardcoded block doesn’t stop automation.

---

## How It Works (File Handoff)

1. **Agent (A-Side)** needs to run something that requires network (e.g. map drives, run backups).
2. Instead of running that script in the Cursor terminal (where it would be blocked), the Agent **writes a request file** into `data/lumina_sandbox/requests/` with an allowlisted `action_id`. No network is used — only file I/O in the workspace.
3. **B-Side daemon** (running outside Cursor, with network) watches that directory, picks up the request, runs the allowlisted script in a normal subprocess, and writes the result to `data/lumina_sandbox/responses/<request_id>.json`.
4. **Agent** reads the response file and can report stdout/stderr and success/failure to the user.

Protocol: **A → request file → B runs script → response file → A reads**. No network from A; B has full network.

---

## Automation (Required Path for Agent)

When the Agent (or any A-Side context) needs to run a network-requiring command:

1. **Submit and wait** (recommended):  
   `python scripts/python/lumina_sandbox_request.py map_network_drives --wait 120`  
   This writes the request and polls for the response file (up to 120s). B-Side must be running.

2. **Submit only**:  
   `python scripts/python/lumina_sandbox_request.py execute_all_backups --wait 0`  
   Then the user or Agent can read the response from `data/lumina_sandbox/responses/<request_id>.json` when ready.

Allowlisted `action_id` values are in `config/lumina_sandbox.json`. Examples:

- `map_network_drives` — Map-LuminaNetworkDrives.ps1  
- `setup_nas_git_repos` — Setup-NASGitRepos.ps1  
- `execute_all_backups` — execute_all_backups.py  
- `automate_nas_deploy` — automate_nas_deploy.py  
- `automate_nas_deploy_sync_first` — automate_nas_deploy.py --sync-first  
- `nas_azure_vault_test` — nas_azure_vault_integration.py --test  
- `syphon_scheduled_cycle` — syphon_scheduled_daemon_nas_kron.py --cycle  

---

## B-Side Daemon: Run Outside Cursor

The B-Side daemon **must** run in a process that is **not** started by the Cursor Agent (so it isn’t sandboxed). Options:

1. **Manual (one-off)**  
   From a normal terminal (e.g. PowerShell or Cursor’s integrated terminal **opened by you**, not by Agent):  
   `python scripts/python/lumina_sandbox_daemon.py`  
   Leave it running while you use the Agent for network-requiring tasks.

2. **Install at logon (recommended)**  
   Run once from a normal terminal:  
   `python scripts/python/lumina_sandbox_daemon.py --install`  
   This registers a Task Scheduler task that starts the B-Side daemon at logon (with a short delay). It then runs with full network.

3. **Single batch (testing)**  
   `python scripts/python/lumina_sandbox_daemon.py --once`  
   Processes any pending request files once and exits.

---

## Config and Allowlist

- **Config**: `config/lumina_sandbox.json`  
  - `request_dir` / `response_dir`: where A-Side writes requests and B-Side writes responses.  
  - `allowed_actions`: list of `{ "id", "description", "runner", "script", "args" }`. Only these `id`s can be requested.  
  - `poll_interval_seconds`, `default_timeout_seconds`: daemon polling and run timeout.

- **Adding a new allowlisted action**: Add an entry to `allowed_actions` with a unique `id`, then use that `id` in `lumina_sandbox_request.py <action_id>`.

---

## Testing the workaround

1. **Start the B-Side daemon** (from a **normal** terminal — one you opened, not the Agent):
   ```bash
   cd c:\Users\mlesn\Dropbox\my_projects\.lumina
   python scripts/python/lumina_sandbox_daemon.py
   ```
   Leave it running. You should see: `LUMINA B-Side Sandbox Daemon started (full network). Watching: ...`

2. **From the Agent** (or the same normal terminal), submit a request and wait:
   ```bash
   python scripts/python/lumina_sandbox_request.py map_network_drives --wait 90
   ```
   The request script only does file I/O (writes request, polls for response). The daemon runs the real script with network and writes the response.

3. **If you had a pending request** (e.g. from a previous run when the daemon wasn’t running), start the daemon and it will pick up the file. Or run once: `python scripts/python/lumina_sandbox_daemon.py --once` to process pending requests and exit.

---

## References

- **RCA**: [RCA_AGENT_TERMINAL_NETWORK_BLOCK.md](./RCA_AGENT_TERMINAL_NETWORK_BLOCK.md) — why Cursor blocks network and paper trail.
- **Automation**: [AUTOMATION_FIRST.md](./AUTOMATION_FIRST.md) — B-Side is the required path for network-requiring automation when run by the Agent.
- **Scripts**: `scripts/python/lumina_sandbox_daemon.py` (B-Side), `scripts/python/lumina_sandbox_request.py` (A-Side).

**Tags**: #workaround #cursor-sandbox #automation #A/B-matrix #Lumina-Sandbox
