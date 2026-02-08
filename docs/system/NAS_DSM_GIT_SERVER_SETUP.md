# NAS DSM Git Server – Local Git “Cloud” for LUMINA

**Purpose**: Use the Synology DSM **Git Server** package as the local Git “cloud” so LUMINA’s local enterprise Git (backup, sync, NAS repos) runs on the NAS instead of only on `data/local_backup`.

**Status**: Documented; install Git Server on DSM and map the share to match existing LUMINA config.

---

## Do it all (checklist)

1. **On NAS DSM**: Package Center → install **Git Server**; Control Panel → Shared Folder → create folder **git** (same NAS `10.17.17.32` where you already have backups, home, jupyter, etc.); in Git Server set repository root to that folder.
2. **On PC**: From repo root, run `.\scripts\powershell\Setup-NASGitRepos.ps1`. It maps G: (and Z:, H:) and creates `G:\git\repositories\lumina-local-enterprise` and `lumina-backup` with `git init`. Requires NAS reachable and (if using Key Vault) `az login` in that session.

---

## Why use DSM Git Server

- **Single place for local Git**: Repos live on the NAS (e.g. `G:\git\repositories`), so all machines can use the same “local cloud” instead of each having its own `data/local_backup` with a nested `.git`.
- **No “too many active changes”**: We avoid turning `data/local_backup` into a Git repo; it stays a **fallback** copy only (no `.git` there). Primary versioned backup is on the NAS Git Server.
- **Fits existing config**: `config/repository_structure.json` and `config/git_gitlens_enterprise.json` expect:
  - `G:\git\repositories\lumina-local-enterprise` (or `lumina-enterprise`)
  - `G:\git\repositories\lumina-backup`
  - Fallback path: `data/local_backup` when NAS is unavailable

---

## 1. Install Git Server on DSM

1. **Open DSM**: `https://10.17.17.32:5001` (or `http://10.17.17.32:5000`).
2. **Package Center** → search for **Git Server**.
3. **Install** the Git Server package (Synology add-on).
4. **Launch** Git Server from Package Center or the main menu.

---

## 2. Create shared folder for Git repos

Git Server uses a shared folder for repository storage.

1. **Control Panel** → **Shared Folder** → create a folder, e.g. `git` (or use the default chosen by Git Server during setup).
2. In **Git Server** app:
   - Set the **repository root** to that shared folder (e.g. `git` or `/volume1/git`).
   - Create repositories via the Git Server UI, or create them manually under that share (e.g. `lumina-local-enterprise`, `lumina-backup`).

Ensure the NAS user used for SMB (e.g. the same account used for Z: or other shares) has read/write permission to this folder.

---

## 3. Map the Git share on Windows (G:)

So that `G:\git\repositories` matches LUMINA config:

1. **Option A – Manual mapping**
   - Map the Git shared folder to **G:** (e.g. `\\10.17.17.32\git` → G:).
   - Create `G:\git\repositories` and create or clone repos there (e.g. `lumina-local-enterprise`, `lumina-backup`).

2. **Option B – Add to LUMINA network drives (recommended)**
   - G: is already defined in `config/lumina_network_drives.json` for the Git share; the mapping script maps it at login.
   - Use the same credential source as other NAS drives (e.g. Azure Key Vault / `nas-password`).
   - Run the mapping script (e.g. `scripts/powershell/Map-LuminaNetworkDrives.ps1`) so G: is created at startup.

After mapping, ensure `G:\git\repositories` exists and that LUMINA’s Git/backup scripts use it (see below).

---

## 4. LUMINA config (already set up)

No code changes required; only ensure the NAS share and G: match these paths:

| Config | Path / purpose |
|--------|-----------------|
| `config/repository_structure.json` | `local_enterprise.path`: `G:\git\repositories\lumina-local-enterprise` |
| `config/git_gitlens_enterprise.json` | `local_enterprise.repository_path`: `G:\git\repositories\lumina-enterprise`; `backup_path`: `G:\git\repositories\lumina-backup`; `fallback_path`: `data/local_backup` |

- **Primary**: NAS Git Server at `G:\git\repositories\...` (push/pull, backup scripts).
- **Fallback**: `data/local_backup` when NAS is unavailable; this folder must **not** contain a `.git` directory (see `docs/system` note on local_backup).

---

## 5. Create repos on the NAS (if not using Git Server UI)

From a machine with G: mapped and Git installed:

```powershell
# Create bare or normal repos under G:\git\repositories
mkdir G:\git\repositories\lumina-local-enterprise
cd G:\git\repositories\lumina-local-enterprise
git init

mkdir G:\git\repositories\lumina-backup
cd G:\git\repositories\lumina-backup
git init
```

Then point LUMINA’s backup/sync scripts at these paths (they already use the config above).

---

## 6. One-command setup (Windows)

After the NAS has the **git** share and Git Server is installed, on your PC run:

```powershell
# Map G: (and Z:) and create G:\git\repositories + init repos
.\scripts\powershell\Setup-NASGitRepos.ps1
```

This script: (1) runs `Map-LuminaNetworkDrives.ps1` so G: is mapped (requires `az login` and NAS reachable), (2) creates `G:\git\repositories`, `lumina-local-enterprise`, and `lumina-backup`, (3) runs `git init` in each repo. If G: is not available, it prints the DSM steps above.

To only create repo structure (G: already mapped): `.\scripts\powershell\Setup-NASGitRepos.ps1 -SkipMap`

## 7. Automation (ongoing)

- **Backup/sync**: `config/git_gitlens_enterprise.json` defines NAS cron tasks (e.g. `local_enterprise_backup.py`, `git_gitlens_enterprise_services.py`) that use `repository_path` and `backup_path` on G:.
- **Startup**: `scripts/powershell/Wait-ForNetworkDrives.ps1` (Phase 0) waits for configured drives; G: is in `config/lumina_network_drives.json` so it is waited on at startup.

---

## Related

- **Custom DSM packages**: `docs/system/CUSTOM_NAS_DSM_PACKAGES.md`
- **Local backup fallback**: `data/local_backup` is in `.gitignore`; do **not** put a `.git` inside it.
- **Repository strategy**: `config/repository_structure.json`
- **Git/GitLens enterprise**: `config/git_gitlens_enterprise.json`
- **Synology Git Server**: [Synology Knowledge Center – Git Server](https://kb.synology.com/en-me/DSM/help/Git/git?version=7)

**Tags**: #DSM #NAS #Git #local-cloud #LUMINA
