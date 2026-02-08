# Kali Linux WSL: Upgrade Minimal to Full

Upgrade a **minimal** Kali Linux WSL install to a **full** install (metapackages). Preserve a peak success-point by backing up WSL first.

---

## Automation (recommended)

From the repo root in **PowerShell (Windows)**:

```powershell
.\scripts\powershell\upgrade_kali_wsl_to_full.ps1
```

- Runs inside `kali-linux` WSL: `apt update` then installs the chosen metapackage.
- Default metapackage: **kali-linux-large**. Use `-FullSet` for **kali-linux-everything** (larger).
- Optionally hides the “You are using a minimal installation” message.

**Back up WSL first (peak success-point):**

```powershell
python scripts/python/backup_wsl_to_nas.py
.\scripts\powershell\upgrade_kali_wsl_to_full.ps1
```

---

## Manual (inside WSL)

If you prefer to run inside Kali WSL:

```bash
sudo apt update
sudo apt install -y kali-linux-large
# Or full set:
# sudo apt install -y kali-linux-everything
```

Optional: hide the minimal-install message:

```bash
sudo touch /etc/kali-minimal
```

---

## Metapackages

| Metapackage             | Use case                          |
|-------------------------|------------------------------------|
| **kali-linux-large**    | Default; large tool set, smaller than everything |
| **kali-linux-everything** | Full Kali (all packages)         |

---

## Prerequisites

- **kali-linux** WSL distribution present and initialized.
- Run upgrade from **Windows** (PowerShell) so WSL is driven from the host; or open a Kali WSL shell and run the manual steps above.

---

## Related

- **WSL backup (before upgrade):** [WSL_BACKUP_TO_NAS.md](WSL_BACKUP_TO_NAS.md) — `python scripts/python/backup_wsl_to_nas.py`
- **Kali WSL init + Perl:** [WSL_KALI_SETUP_SUMMARY.md](WSL_KALI_SETUP_SUMMARY.md) — `.\scripts\setup\initialize_kali_wsl.ps1`
- **Hardened Kali Docker image:** [HARDENED_KALI_LINUX_BUILD.md](../security/HARDENED_KALI_LINUX_BUILD.md) — different from WSL upgrade

---

**Tags:** #WSL #KALI_LINUX #automation @JARVIS @LUMINA
