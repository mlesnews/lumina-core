# RCA: Agent Terminal Network Block When Running Map-LuminaNetworkDrives.ps1

**Date**: 2026-01-29
**Issue**: When the Cursor Agent runs `Map-LuminaNetworkDrives.ps1` (or any script that needs network access), the run reports "Network access: Blocked" and the NAS (10.17.17.32) is not reachable. Previously, the same script could be run successfully from a user-opened terminal.

---

## Root Cause

**Cursor Agent–invoked terminal commands run inside Cursor’s sandbox, which blocks network access by design.**

- The restriction is **not** caused by LUMINA config, scripts, or a recent project change.
- It is imposed by the **Cursor IDE** on any command run by the Agent (e.g. via “Run” or tool execution):
  - The subprocess is sandboxed.
  - Network access is blocked for that subprocess, even when permissions like `network` or `all` are requested for the tool.
- So when the Agent runs `Map-LuminaNetworkDrives.ps1`, the process **cannot** reach 10.17.17.32 or Azure Key Vault, and mapping fails.

## Why It “Didn’t Happen Previously”

- If the script worked before, it was almost certainly run from a **user-opened terminal** (e.g. pwsh in Cursor, or PowerShell outside Cursor), where there is **no** Agent sandbox and network is allowed.
- The “block” has always applied to **Agent-run** terminals; the change in behavior is **who** is running the command (Agent vs. you).

## Mitigation

- **Mapping drives**: Run `.\scripts\powershell\Map-LuminaNetworkDrives.ps1` (and, if used, `Setup-NASGitRepos.ps1`) from a **normal terminal** (e.g. Cursor’s integrated terminal opened by you, or Windows PowerShell). Same for any script that must reach the NAS or the internet.
- **Automation**: Use Task Scheduler or startup scripts to run the mapping at logon; those run outside Cursor’s sandbox and have network access.

## Required workaround: double sandbox (A/B matrix)

Because Agent-run commands cannot use the network, LUMINA uses a **B-Side (Lumina Sandbox)** that runs outside Cursor and executes allowlisted scripts via **file handoff**. The Agent (A-Side) only writes a request file and reads the response file — no network needed.

- **A-Side** = Cursor sandbox (Agent; file I/O only).
- **B-Side** = Lumina Sandbox daemon (user or Task Scheduler; full network).

**When the Agent needs to run a network-requiring command**, use the B-Side request script instead of running the command directly:

```bash
python scripts/python/lumina_sandbox_request.py map_network_drives --wait 120
```

The B-Side daemon must be running (start it from a normal terminal, or install at logon: `python scripts/python/lumina_sandbox_daemon.py --install`).

See **[LUMINA_SANDBOX_AB_MATRIX.md](./LUMINA_SANDBOX_AB_MATRIX.md)** for the full A/B matrix, allowlisted actions, and setup.

## Other output when run by Agent

- **Get-ChildItem : An item with the same key has already been added** – From Cursor's runner script, not Map-LuminaNetworkDrives.ps1. Duplicate env var names. Not fixable in LUMINA.
- **InitializeDefaultDrives operation on the 'FileSystem' provider failed** – PowerShell in restricted context. Harmless.

---

## Paper trail: evidence that network worked previously

This section documents internal and design evidence that the same project and workflows **did** use network from Cursor-attached terminals before the current "Network access: Blocked" behavior. The limitations are **new** (Cursor-side), not a LUMINA regression.

### 1. Cursor project terminal logs (same workspace)

Cursor stores terminal output for this project under
`C:\Users\mlesn\.cursor\projects\c-Users-mlesn-Dropbox-my-projects-lumina\terminals\`.
Those logs show **successful outbound HTTPS** to Azure Key Vault and Azure CLI credential use:

| Terminal file   | Command | Evidence |
|-----------------|--------|----------|
| `273753.txt`    | `python execute_all_backups.py` | Key Vault client created; **Response status: 200** to `https://jarvis-lumina.vault.azure.net/...` (lines 73, 120). Same workspace, 2026-01-29. |
| `80874.txt`     | `python scripts/python/nas_azure_vault_integration.py --test` | Key Vault client created; **Response status: 200** (line 46). Same workspace, 2026-01-29. |
| `226217.txt`    | `python scripts/python/syphon_scheduled_daemon_nas_kron.py --cycle` | "Azure Key Vault client initialized (using Azure CLI credential)". Same workspace, 2026-01-29. |
| Many others     | Various Python/backup/syphon scripts | "Azure Key Vault client initialized" or "Response status: 200" (e.g. 992148, 23614, 139920, 117166, 42103, 246573). |

So terminals **attached to this Cursor project** have previously had full network (HTTPS to Azure, Azure CLI). The same scripts and same workspace now show "Network access: Blocked" when run **by the Agent**; the change is **who** runs the command (Agent vs. user) and/or **when** (post–Cursor 2.0 sandbox), not a change in LUMINA scripts or config.

### 2. "Network access: Blocked" is not in terminal stdout

A search of all terminal log files in that folder for `Network access: Blocked` or `Blocked` (in this context) returns **no matches**. The block message appears in the **Cursor UI** when the Agent runs a command, not in script output. So the restriction is enforced by Cursor's execution environment, not by our code.

### 3. Design intent: automation runnable by AI/Agent

- **`docs/system/AUTOMATION_FIRST.md`**: "Regardless of manual options, use automation so **AI does the heavy lifting**." "**For agents and code**: … provide a single automation script … Tag automation entry points with `#automation`."
- Docs and scripts (e.g. `Map-LuminaNetworkDrives.ps1`, `execute_all_backups.py`, `automate_nas_deploy.py`, `Setup-NASGitRepos.ps1`) are written so that **running one command** (including by Agent) should perform sync/deploy/backup/drive mapping. The design assumes those commands **can** reach the network (NAS, Azure, ProtonPass). There is no LUMINA change that removed that assumption; the environment (Cursor sandbox) now blocks it for Agent-invoked runs.

### 4. No LUMINA allowlist or sandbox config

- There is **no** `allowlist.json` or Cursor allowlist/sandbox config in the repo. The project relied on **default** Cursor behavior. Previously that default allowed network from terminals in this project; after Cursor 2.0, Agent-run commands are sandboxed with no internet by default.

### 5. External timeline (Cursor 2.0)

- **Cursor 2.0** (changelog: "New Coding Model and Agent Interface") introduced sandboxed execution: shell commands run in a sandbox with **read/write to workspace and no internet access by default**; commands not allowlisted get restricted network.
- User reports: e.g. "Cursor AI Agent Cannot Access localhost via curl" — same sandbox behavior (localhost/network blocked).
- So the paper trail aligns with: **same LUMINA workflows, same project, same terminal logs showing past network success; the new restriction is Cursor's sandbox (2.0), not a regression in our scripts or config.**

---

## References

- Cursor docs: Terminal / Agent behavior (sandbox).
- Cursor changelog: [New Coding Model and Agent Interface (2.0)](https://cursor.com/changelog/2-0) — sandbox, no internet by default.
- User reports: e.g. “Cursor AI Agent Cannot Access localhost via curl” (same sandbox behavior).
- LUMINA: `scripts/powershell/Map-LuminaNetworkDrives.ps1`, `config/lumina_network_drives.json`, `docs/system/AUTOMATION_FIRST.md`.
- Paper trail: Cursor project terminals dir `.../terminals/*.txt` (e.g. 273753.txt, 80874.txt, 226217.txt).

**Tags**: #RCA #Cursor #sandbox #network #NAS #paper-trail
