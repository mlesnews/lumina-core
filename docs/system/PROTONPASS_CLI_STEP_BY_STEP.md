# ProtonPass CLI — Step-by-Step (No Secrets in Docs)

**Policy**: We **never** broadcast or store SECRETS in text files, logs, or documentation. This guide uses placeholders only (e.g. `your-proton-email`, `Your Item Title`). Scripts use secrets only in memory and send them to Azure Key Vault or APIs; they do not write secrets to disk or log their values.

**Tags**: #automation @triad @JARVIS @itsec

---

## Automation first — AI does the heavy lifting

**Regardless of manual steps below, use #automation so AI does the heavy lifting.**

- **One command to sync (optional) + deploy cron to NAS:**

  ```powershell
  python scripts/python/automate_nas_deploy.py
  ```

  Credentials are resolved automatically (Azure → UnifiedSecretManager → ProtonPass). No secrets in logs or files.

- **If credentials are missing**, the scripts show a short line first, e.g. **"No credentials active. Please run: az login"** or **"No credentials active. Please run: pass-cli login --interactive &lt;your-proton-email&gt;"** (see [Proton Pass CLI login](https://protonpass.github.io/pass-cli/commands/login/)), then optional details and "Run 'az login' now? (y/n)". Follow the prompts in the same terminal.

- **If you want to ensure Azure has NAS credentials from ProtonPass before deploy:**

  ```powershell
  python scripts/python/automate_nas_deploy.py --sync-first
  ```

  This syncs from ProtonPass CLI to Azure Key Vault, then runs the deploy.

- Manual steps (Steps 1–6) are for setup and troubleshooting only. Day-to-day: run `automate_nas_deploy.py`.

---

## Running in WSL (personal account)

To run automation in **WSL** as your personal account, ensure **Azure CLI** (`az`) and **Proton Pass CLI** (`pass-cli`) are on your PATH:

1. **One-time per session** (from repo root inside WSL):

   ```bash
   source scripts/wsl/ensure_nas_tools_path.sh
   ```

   Or run it to verify and print PATH additions (exits with an error if `az` or `pass-cli` is missing):

   ```bash
   bash scripts/wsl/ensure_nas_tools_path.sh
   ```

2. **Persist PATH for future WSL sessions** (run once after both tools are installed):

   ```bash
   bash scripts/wsl/ensure_nas_tools_path.sh --persist
   ```

   This verifies `az` and `pass-cli` are on PATH, then appends `/usr/bin`, `/usr/local/bin`, `$HOME/.local/bin`, and `$HOME/bin` to your `~/.bashrc` so new shells have both tools on PATH.

3. **Then run automation** in the same WSL shell:

   ```bash
   python3 scripts/python/automate_nas_deploy.py
   python3 scripts/python/automate_nas_deploy.py --sync-first
   ```

Install locations in WSL: **Azure CLI** — `sudo apt install azure-cli` or [Microsoft install guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux); **Proton Pass CLI** — `npm i -g @proton/pass-cli` (often in `~/.local/bin` or NVM bin) or [Proton Pass CLI installation](https://protonpass.github.io/pass-cli/get-started/installation/).

---

## SECURITY: Never Reveal Secrets

- **Do not** put passwords, API keys, or tokens in this doc, in config files committed to git, or in logs.
- **Do not** `print()` or `logger.info()` secret values. Use masking (e.g. `***REDACTED***` or length-only) when logging that a secret was used.
- **Scripts**: Retrieve secrets from ProtonPass CLI or Azure Vault → use in memory → send to vault/API only. No writing secrets to plain text files.
- See `scripts/python/secret_utils.py` and `docs/security/SECRET_MANAGEMENT_POLICY.md` for masking and audit.

---

## Proton Pass CLI syntax (from Proton website / FAQ)

**Source**: [Proton Pass CLI documentation](https://protonpass.github.io/pass-cli/) (official).

- **Command name**: `pass-cli` (Windows: `pass-cli.exe`). Some installs may expose `protonpass` on PATH; the official binary is `pass-cli`.
- **Login**:
  - **Web login (default)**: `pass-cli login` — opens a URL in your browser to complete auth (required for SSO or hardware key 2FA).
  - **Interactive login** (CLI only): `pass-cli login --interactive <USERNAME>` — e.g. `pass-cli login --interactive user@proton.me`. You are prompted for password, then TOTP (if enabled), then Proton Pass “extra password” if your account has one. The username is a **positional argument** after `--interactive`, not a `--username` flag.
- **Check session**: `pass-cli info` or `pass-cli test`.
- **Logout**: `pass-cli logout` (or `pass-cli logout --force` for troubleshooting).
- **Vaults**: `pass-cli vault list`.
- **Shares**: `pass-cli share list` — lists share IDs (needed for item commands).
- **Items**: `pass-cli item list --share-id "<ShareId>"` — list items in a vault; `pass-cli item view --share-id "<ShareId>" --item-id "<ItemId>"` — view one item. Share IDs come from `pass-cli share list`.
- **Secret URI**: Secrets can be referenced as `pass://vault/item/field` (see official docs).
- **Troubleshooting**: [Proton Pass CLI Troubleshoot](https://protonpass.github.io/pass-cli/help/troubleshoot/) — e.g. keyring errors (`PROTON_PASS_KEY_PROVIDER=fs`), Windows script policy (`Set-ExecutionPolicy RemoteSigned`).

---

## Step 1: Find the Proton Pass CLI

The official binary is **pass-cli** (Windows: `pass-cli.exe`). It may also be on PATH as `pass-cli` or, on some installs, `protonpass`.

1. **Run the finder script** (no secrets involved):

   ```powershell
   cd path\to\.lumina
   python scripts/python/find_protonpass_cli.py
   ```

2. **Typical locations** (paths only; no credentials):
   - `%LOCALAPPDATA%\Programs\ProtonPass\pass-cli.exe`
   - Or `pass-cli` / `protonpass` if on PATH.
3. **Optional**: Set `PROTONPASS_CLI_PATH` to the full path to the executable so scripts use it consistently.
4. **Verify**: `pass-cli --version` (see [Installation](https://protonpass.github.io/pass-cli/get-started/installation/)).

---

## Step 2: Log in (interactive — you type in terminal only)

You must be logged in so the CLI can read items. **Do not** put your Proton account password in a script or a file.

1. **Open a terminal** and run using the **official syntax** (replace with your Proton Pass email only; never put your password in the command or in a file):

   **Web login** (easiest; use if you have SSO or hardware key 2FA):

   ```powershell
   pass-cli login
   ```

   Then open the URL shown in your browser and complete the flow.

   **Interactive login** (password + optional TOTP in the terminal):

   ```powershell
   pass-cli login --interactive your-proton-email@example.com
   ```

   Or with full path on Windows:

   ```powershell
   & "$env:LOCALAPPDATA\Programs\ProtonPass\pass-cli.exe" login --interactive your-proton-email@example.com
   ```

   The username is a **positional argument** after `--interactive` (no `--username` flag per [Proton docs](https://protonpass.github.io/pass-cli/commands/login/)).

2. When prompted, **type your Proton account password in the terminal**. It is not stored in any file; the CLI uses it only for that session.
3. If 2FA (TOTP) is enabled, enter the code when prompted. If your account has a Proton Pass **extra password**, you will be prompted for that too. Again, type in terminal only; never paste codes or passwords into a text file or doc.

---

## Step 3: List items (titles only — no secret values)

To see what the CLI can access (item **titles** only; no passwords in output):

1. **Get share IDs** (required for item commands per [Proton docs](https://protonpass.github.io/pass-cli/objects/share/)):

   ```powershell
   pass-cli share list
   ```

2. **List items in a vault** (use a share ID from the step above):

   ```powershell
   pass-cli item list --share-id "<YourShareId>"
   ```

   Or list vaults first: `pass-cli vault list`. Then use the appropriate share ID with `item list`.

3. **In docs and examples** we refer to items by **placeholder** names, e.g.:
   - `Your Item Title`
   - `NAS`, `Synology NAS`, or similar (for NAS credentials)
   - Never paste real item titles that could be considered sensitive; use generic names in shared docs.

Scripts match NAS credentials by **search terms** (e.g. nas, synology, backupadm) against title/username/URL; see `config/triad_nas_credentials.json` → `protonpass_cli.search_terms`.

---

## Step 4: How Scripts Use ProtonPass (No File, No Log of Value)

- **NASAzureVaultIntegration** (Triad Tier 2): Calls ProtonPass CLI (`item list` then `item read <id>`), gets username/password **in memory only**, uses them for NAS/SSH or passes to Azure Vault client. Does **not** write secrets to files or log their values.
- **UnifiedSecretManager**: Can use ProtonPass as a source; retrieves secret into memory and returns it to the caller. Callers must not log or write that value.
- **sync_nas_credentials_protonpass_to_vault.py**: Reads NAS credentials from ProtonPass CLI → writes them **only** to Azure Key Vault (via SDK). No local text file of the password.

When debugging, log only **presence/length** or **masked** form (e.g. “Retrieved NAS credentials (username set, password length N)” or “Password: ***REDACTED***”), never the actual secret.

---

## Step 5: Sync NAS Credentials to Azure (Optional)

If you want Azure Key Vault to have the same NAS credentials as ProtonPass (e.g. for deploy or Tier 1):

1. **Ensure you are logged in** (Step 2).
2. **Dry run** (fetches from ProtonPass, does **not** write to Azure; no secrets printed):

   ```powershell
   python scripts/python/sync_nas_credentials_protonpass_to_vault.py --dry-run
   ```

   You should see that credentials were retrieved; the script must **not** print the password.
3. **Real run** (writes to Azure only; no local secret file):

   ```powershell
   python scripts/python/sync_nas_credentials_protonpass_to_vault.py
   ```

   Secrets go from ProtonPass CLI → in-memory → Azure Vault API only.

---

## Step 6: Deploy Cron to NAS

After NAS credentials are in Azure (and/or ProtonPass), deploy uses them from memory only:

```powershell
python scripts/python/deploy_all_cron_to_nas.py
```

Credentials are read from Azure or ProtonPass (Triad order), used for SSH/vault, and never written to a text file or broadcast in logs.

---

## Quick reference (no secrets)

<!-- markdownlint-disable MD060 -->
|Action|Command / Script|
|-----|-----|
|Find CLI|`python scripts/python/find_protonpass_cli.py`|
|Login (web)|`pass-cli login` (open URL in browser)|
|Login (interactive)|`pass-cli login --interactive your-proton-email@example.com` (then type password)|
|Check session|`pass-cli info` or `pass-cli test`|
|List shares|`pass-cli share list`|
|List items|`pass-cli item list --share-id "<ShareId>"`|
|Sync NAS → Azure|`python scripts/python/sync_nas_credentials_protonpass_to_vault.py [--dry-run]`|
|Deploy cron to NAS|`python scripts/python/deploy_all_cron_to_nas.py`|
|**Automation (all-in-one)**|`python scripts/python/automate_nas_deploy.py` or `... --sync-first`|
<!-- markdownlint-enable MD060 -->

---

## References

- **Proton Pass CLI (official docs and FAQ)**: <https://protonpass.github.io/pass-cli/>
  - [Overview](https://protonpass.github.io/pass-cli/) · [Login command](https://protonpass.github.io/pass-cli/commands/login/) · [Installation](https://protonpass.github.io/pass-cli/get-started/installation/) · [Troubleshoot](https://protonpass.github.io/pass-cli/help/troubleshoot/) · [Share object](https://protonpass.github.io/pass-cli/objects/share/)
- Triad: `docs/system/TRIAD_PASSWORD_MANAGER_SYSTEM.md`, `TRIAD_VAULT_STRATEGY.md`
- NAS credential config: `config/triad_nas_credentials.json`
- Secret masking: `scripts/python/secret_utils.py`

**Last updated**: 2026-01
**Policy**: No secrets in this doc or in any committed text file. Never broadcast or store secrets in plain text.
