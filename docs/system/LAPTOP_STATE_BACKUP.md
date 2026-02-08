# Laptop State Backup — Restore Anywhere

Back up this laptop's current state (WSL + LUMINA repo) so you can restore it on any machine.

---

## Automation

From the repo root in **PowerShell (Windows)**:

```powershell
.\scripts\powershell\backup_laptop_state.ps1
```

- Creates **one snapshot** under **`B:\LaptopState\<date>`** (e.g. `B:\LaptopState\20260129-120000`).
- **WSL**: Exports every distro to `B:\LaptopState\<date>\WSL-backups\<distro>-<date>.tar`.
- **Data**: Copies paths from config (default: `.lumina` repo) into `B:\LaptopState\<date>\data\`.
- **Manifest**: Writes `manifest.txt` in the snapshot folder.
- **Two places:** If **`mirror_to_nas_unc`** is set in config (e.g. `\\10.17.17.32\backups\LaptopState`), the script also copies the snapshot to the NAS so you have the same backup on disk and on the NAS.

Subdirs are created if missing. B: is the backups drive.

---

## Config

**`config/laptop_backup_config.json`**:

- **`backup_root`** — Base path (default `B:\LaptopState`).
- **`mirror_to_nas_unc`** — Optional. If set (e.g. `\\10.17.17.32\backups\LaptopState`), snapshot is also copied to NAS (two places).
- **`include_wsl`** — Include WSL exports (default true).
- **`include_paths`** — Paths to copy into snapshot (default: `.lumina` repo path). Add more if needed.

---

## Restore Anywhere

1. **Copy the snapshot folder** (e.g. `B:\LaptopState\20260129-120000`) to the new machine (USB, NAS, cloud, or same B:).
2. **Restore WSL** (from Windows PowerShell on the new machine):
   ```powershell
   wsl --import Kali-Restored "C:\WSL\Kali-Restored" "X:\path\to\snapshot\WSL-backups\kali-linux-20260129-120000.tar"
   ```
   Use the actual snapshot path and `.tar` filename.
3. **Restore project/data**: Copy `snapshot\data\.lumina` (or other contents) to your desired location on the new machine.

---

## Related

- **WSL-only backup**: [WSL_BACKUP_TO_NAS.md](WSL_BACKUP_TO_NAS.md) — `backup_wsl_to_nas.ps1` (writes to `B:\WSL-backups`).
- Laptop state = one snapshot with WSL + repo so you can restore anywhere.

---

**Tags:** #automation #backup #restore-anywhere @JARVIS @LUMINA
