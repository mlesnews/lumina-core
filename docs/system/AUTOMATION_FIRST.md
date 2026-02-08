# Automation First — AI Does the Heavy Lifting

**Tag**: #automation @JARVIS

Regardless of manual options, **use automation so AI does the heavy lifting.** Prefer single-entry scripts over step-by-step manual flows.

**100% CLI goal**: All workflows from the command line. See [CLI_FIRST.md](system/CLI_FIRST.md) for CLI-only flows and the few one-time GUI touchpoints.

---

## Principle

- **Single entry points**: One script that chains sync → deploy (or other workflows) so the human runs one command.
- **Credentials and Triad**: Scripts resolve credentials automatically (Azure → UnifiedSecretManager → ProtonPass). No secrets in logs or files.
- **Day-to-day**: Run automation scripts. Manual steps are for one-time setup and troubleshooting only.

---

## NAS / ProtonPass / Deploy

| Goal | Automation command |
|------|--------------------|
| Deploy cron to NAS (creds from Triad) | `python scripts/python/automate_nas_deploy.py` |
| Sync ProtonPass → Azure then deploy | `python scripts/python/automate_nas_deploy.py --sync-first` |

See `docs/system/PROTONPASS_CLI_STEP_BY_STEP.md` (Automation first section) and `scripts/python/automate_nas_deploy.py`.

---

## For agents and code

- When adding flows (credentials, deploy, sync): provide a **single automation script** that does the full sequence.
- Tag automation entry points with `#automation` in docstrings and docs.
- Prefer invoking automation over documenting long manual steps.

---

## Required: B-Side for network when run by Agent (Cursor sandbox workaround)

Cursor Agent–invoked terminals have **no network access**. For any automation that needs network (drive mapping, backups, NAS deploy, Key Vault), the Agent **must not** run the script directly in the Cursor terminal — it will be blocked.

**Required path**: Use the **LUMINA B-Side (Lumina Sandbox)**. The Agent submits a request by running (file I/O only, no network):

```bash
python scripts/python/lumina_sandbox_request.py <action_id> --wait 120
```

Examples: `map_network_drives`, `execute_all_backups`, `automate_nas_deploy`, `automate_nas_deploy_sync_first`. The B-Side daemon (running outside Cursor, with network) executes the allowlisted script and writes the result; the request script polls for the response.

- **B-Side daemon**: Run `python scripts/python/lumina_sandbox_daemon.py` from a normal terminal, or install at logon: `python scripts/python/lumina_sandbox_daemon.py --install`.
- **Full doc**: [LUMINA_SANDBOX_AB_MATRIX.md](system/LUMINA_SANDBOX_AB_MATRIX.md).

**Last updated**: 2026-01
