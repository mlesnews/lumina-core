# Service-Level Accounts — Best Way to Run Them

**Policy**: Service-level accounts (e.g. backupadm, ldapadm, dbadmin) are used by **automation and scripts**, not for interactive human login. Credentials live only in Azure Key Vault (Triad Tier 1) or ProtonPass (Tier 2); scripts fetch and use them in memory.

**Tags**: @triad @JARVIS @itsec

---

## Best way to run service-level accounts

1. **Store credentials in the Triad**  
   - **Azure Key Vault** (primary): Create secrets for each service account (username and password).  
   - **ProtonPass** (optional Tier 2): Same credentials can exist for CLI/backup; sync via `sync_nas_credentials_protonpass_to_vault.py` if needed.

2. **Run via automation, not interactive login**  
   - **You** run `az login` (or ProtonPass login) once in your terminal.  
   - **Scripts and cron** use Triad to fetch service-account credentials and run tasks (NAS deploy, LDAP, DB, etc.).  
   - Do **not** log in interactively as backupadm, ldapadm, or dbadmin for day-to-day use; use automation that pulls from the vault.

3. **One account per purpose**  
   - **backupadm** — NAS (backup, SSH, cron deploy).  
   - **ldapadm** — LDAP / DSM join (see `docs/system/CREATE_LDAP_SERVICE_ACCOUNT.md`).  
   - **dbadmin** — MariaDB / DB admin (see `dbadmin-username`, `dbadmin-password` in vault).

4. **If credentials are missing**  
   - Scripts show: **"No credentials active. Please run: az login"** (or ProtonPass).  
   - After you log in, re-run the automation; it will pull service-account creds from the vault.

---

## Registry: service account → Key Vault secrets

| Service account | Purpose           | Key Vault secret names (jarvis-lumina)     | How it’s run |
|-----------------|-------------------|---------------------------------------------|--------------|
| **backupadm**     | NAS (SSH, cron)   | `nas-username`, `nas-password` (or `nas-username-10-17-17-32`, `nas-password-10-17-17-32`) | `automate_nas_deploy.py`, NAS Kron, network drives |
| **ldapadm**     | LDAP / DSM        | Store in vault per `CREATE_LDAP_SERVICE_ACCOUNT.md` | LDAP auth, DSM join |
| **dbadmin**     | MariaDB           | `dbadmin-username`, `dbadmin-password`     | DB scripts, sync tools |

---

## Do not

- Log in interactively as a service account for normal use.  
- Put service-account passwords in config files committed to git or in plain text.  
- Share service-account credentials; use vault + automation only.

---

## Config reference

- **`config/service_level_accounts.json`** — Lists service accounts, Key Vault secret names, and which scripts use them. Use this when adding a new service account or wiring automation.
- **`config/azure/key_vault_config.json`** — Key Vault URL and secret categories (e.g. `nas_secrets`).

---

## References

- Triad: `docs/system/TRIAD_PASSWORD_MANAGER_SYSTEM.md`, `TRIAD_VAULT_STRATEGY.md`  
- NAS / deploy: `docs/system/PROTONPASS_CLI_STEP_BY_STEP.md`, `config/triad_nas_credentials.json`  
- Key Vault categories: `config/azure/key_vault_config.json` (e.g. `nas_secrets`)  
- LDAP service account: `docs/system/CREATE_LDAP_SERVICE_ACCOUNT.md`

**Last updated**: 2026-01
