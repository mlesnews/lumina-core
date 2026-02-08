# WSL Backup to NAS / Backups Drive

Back up all WSL distributions so project and personal data are preserved before reinstalling or overwriting WSL.

**Default:** Backups go to **B:\WSL-backups** (B: is the backups drive). The **subdir is created if it doesn't exist** so everything doesn't end up in the root of B:\.
**Two places:** If **`mirror_to_nas_unc`** is set in config (e.g. `\\10.17.17.32\backups\WSL-backups`), the script also copies to the NAS so you have the same backup on disk and on the NAS.

## Automation — PowerShell (default: B:\WSL-backups)

From **PowerShell on Windows** (not inside WSL), from the repo root:

```powershell
.\scripts\powershell\backup_wsl_to_nas.ps1
```

- Reads destination from **`config/wsl_backup_config.json`** (default: **`B:\WSL-backups`**)
- Creates **B:\WSL-backups** if it doesn't exist
- Exports every WSL distro to **`B:\WSL-backups\<distro>-<date>.tar`**
- Optionally creates a home-directory archive: `home-<distro>-<date>.tar.gz` in the same folder

## Automation — Python (when using NAS UNC and vault credentials)

If you set **`nas_backup_unc`** in config to a NAS path (e.g. `\\10.17.17.32\backups\WSL-backups`), use the Python entry point so the share is mapped with homelab credentials:

```powershell
python scripts/python/backup_wsl_to_nas.py
```

- **Credential order**: Azure Key Vault (nas-username, nas-password) → ProtonPass CLI → NAS-DSM config
- Maps **`\\10.17.17.32\backups`** via `net use` then runs the same PowerShell script (exports go to the configured path)
- Options: `--no-map` (share already accessible), `--skip-home` (no home archive)

When destination is a **local path** (e.g. **B:\WSL-backups**), the Python script skips mapping and just runs the backup; no vault credentials needed.

## Config

- **`config/wsl_backup_config.json`**: **`nas_backup_unc`** — backup root (default **`B:\WSL-backups`**). Subdir is created if missing. **`mirror_to_nas_unc`** — optional; if set (e.g. `\\10.17.17.32\backups\WSL-backups`), script also copies to NAS so backups exist in two places.
- To use NAS directly, set `nas_backup_unc` to `\\10.17.17.32\backups\WSL-backups` and run the Python script for credential mapping.

## Restore after reinstall

From **PowerShell on Windows**:

```powershell
# List existing backups (e.g. B:\WSL-backups or \\10.17.17.32\backups\WSL-backups)
# Then import a specific backup:
wsl --import Kali-Restored "C:\WSL\Kali-Restored" "B:\WSL-backups\kali-linux-20260129-120000.tar"
```

Replace the distro name, import path, and `.tar` filename with your backup.

## Manual options

- **Export one distro**: `wsl --export <DistroName> B:\WSL-backups\<name>.tar`
- **Copy only important data from inside WSL**: copy or `tar` from `~` to a Windows path then copy that folder to B:\WSL-backups (or your configured path)

## Requirements

- **B: drive**: Ensure B:\ is available (e.g. backups drive or mapped NAS share). The script creates **B:\WSL-backups** if it doesn't exist.
- Run backup from **Windows PowerShell**, not from inside WSL.

If you use a NAS UNC and get "Access is denied":
1. Open **File Explorer** and go to `\\10.17.17.32\backups` (log in if prompted), or map: `net use B: \\10.17.17.32\backups`
2. Re-run `.\scripts\powershell\backup_wsl_to_nas.ps1` from the repo root.

## Login / account issues (homelab)

When using `python scripts/python/backup_wsl_to_nas.py`:

1. **Azure**: Run `az login` so the script can read Key Vault (jarvis-lumina).
2. **NAS secrets in vault**: Ensure **nas-username** and **nas-password** (or **nas-username-10-17-17-32** / **nas-password-10-17-17-32**) exist in the vault. If they are only in ProtonPass, sync first:
   ```powershell
   python scripts/python/sync_nas_credentials_protonpass_to_vault.py
   ```
   then run:
   ```powershell
   python scripts/python/backup_wsl_to_nas.py
   ```
3. **Share already mapped**: If the NAS share is already accessible (e.g. you logged in via Explorer), run with `--no-map` so the script skips `net use` and only runs the backup:
   ```powershell
   python scripts/python/backup_wsl_to_nas.py --no-map
   ```
