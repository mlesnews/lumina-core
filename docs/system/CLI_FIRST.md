# CLI First — Work 100% from CLI

**Goal**: Do all LUMINA workflows from the command line. No GUI dependency for day-to-day operations.

**Tag**: #automation #CLI #headless

---

## Principle

- **Single-entry CLI**: Every workflow is one (or a short chain of) CLI commands.
- **Headless by default**: Startup, daemons, and automation run without visible windows; monitor via logs.
- **GUI only for one-time setup**: IDE settings, credential prompts, or OS dialogs that cannot be driven from CLI are documented as one-time; everything else is CLI.

---

## CLI-only flows (no GUI)

| What | Command |
|------|---------|
| Map network drives | `.\scripts\powershell\Map-LuminaNetworkDrives.ps1` |
| Add drive mapping to startup | `.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -AddToStartup` |
| Verify drives | `.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -VerifyOnly` |
| NAS Git repos (G:, init) | `.\scripts\powershell\Setup-NASGitRepos.ps1` |
| Deploy cron to NAS | `python scripts/python/automate_nas_deploy.py` |
| Sync ProtonPass → Azure then deploy | `python scripts/python/automate_nas_deploy.py --sync-first` |
| Run all backups | `python execute_all_backups.py` |
| B-Side request (when Agent sandbox blocks network) | `python scripts/python/lumina_sandbox_request.py <action_id> --wait 120` |
| Install headless startup daemon | `python scripts/python/lumina_headless_startup_daemon.py --install` |
| Install B-Side daemon at logon | `python scripts/python/lumina_sandbox_daemon.py --install` |
| LUMINA CLI-API (status, help, routing) | `lumina-cli status`, `lumina-cli help` — see [CLI_API_README.md](../../CLI_API_README.md) |

All of the above are invokable from PowerShell, cmd, or WSL (where applicable); no IDE or GUI required.

---

## One-time or rare GUI touchpoints

These are the few places that may still involve a GUI or IDE; set once, then use CLI for everything else.

| Touchpoint | What to do | After that |
|------------|------------|------------|
| **Cursor Auto-Run mode** | If you want Agent-run commands to have network: Settings → Auto-Run Mode → **Run Everything (Unsandboxed)**. | All Agent terminal runs then have network; no B-Side needed for that. |
| **Network drive credentials** | When Windows prompts for NAS login (e.g. after reboot or expiry), enter credentials in the dialog once. | Credentials are cached; mapping script is CLI-only. |
| **Azure login** | `az login` in a terminal (browser may open once). | Subsequent scripts use cached credential. |
| **ProtonPass CLI** | `pass-cli login --interactive <your-proton-email>` once. | Automation uses CLI after that. |

---

## References

- [AUTOMATION_FIRST.md](./AUTOMATION_FIRST.md) — single-entry automation, B-Side when sandboxed.
- [LUMINA_NETWORK_DRIVES.md](./LUMINA_NETWORK_DRIVES.md) — drive mapping CLI.
- [CLI_API_README.md](../../CLI_API_README.md) — 100% CLI to API (lumina-cli).
- [STARTUP_CONSOLIDATION.md](./STARTUP_CONSOLIDATION.md) — headless startup, one terminal goal.

**Last updated**: 2026-01
