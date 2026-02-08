# Remote Desktop: Prefer TightVNC Over RDP for MANUS

**Purpose**: Use a lightweight remote desktop (TightVNC) instead of RDP for MANUS-related remote access to Kaiju and DSM configuration.
**Tag**: #MANUS #REMOTE-DESKTOP #TIGHTVNC #QOL

---

## Does MANUS have its own remote desktop?

**No.** MANUS (Manual Automation System) does **not** include a built-in remote desktop viewer or streaming. It provides:

- **Control**: IDE control (Cursor/VS Code), workstation control, homelab automation via MCP (`manus_execute_operation`, `manus_ide_control`, `manus_workstation_control`, etc.).
- **Screenshot capture**: `manus_rdp_screenshot_capture.py` runs on the machine where you are and captures that machine’s screen (no MANUS-built-in viewer).

To **see** a remote machine (e.g. Kaiju), you still need a separate remote desktop transport: **RDP**, **TightVNC**, or similar. MANUS uses that session (you connect with VNC/RDP, then run MANUS-driven tasks there); it does not replace the need for a viewer.

---

## Decision

**Prefer [TightVNC](https://www.tightvnc.com/download.php) over Windows RDP** for that remote desktop transport when using MANUS:

- **Lightweight**: Smaller footprint, fewer dependencies than full RDP stack.
- **Free**: No Windows licensing considerations; works across Windows versions.
- **Cross-platform**: TightVNC has Windows 64/32-bit installers and Unix/Linux/macOS server options.
- **Reliable**: Mature, GPL-licensed; suitable for homelab and automation contexts.

RDP remains **supported** where already in use (e.g. existing scripts, FALC→KAIJU); new setups and MANUS flows should use TightVNC when possible.

---

## Download & Install

- **Windows (64-bit / 32-bit)**: [TightVNC Download](https://www.tightvnc.com/download.php) — Installer for Windows (Version 2.8.85+).
- **Source**: GPL-licensed C++ source available on the same page for custom builds.

Install **TightVNC Server** on the machine to be controlled (e.g. Kaiju); use **TightVNC Viewer** on the machine from which you connect (e.g. FALC, Ultron).

---

## Credentials (two passwords)

TightVNC uses **two different passwords**; both are set during installation and must be kept secure.

| Purpose | Used for | Store in |
|--------|----------|----------|
| **Administration password** | Changing TightVNC Server settings, configuring the service on the host | Azure Key Vault or ProtonPass (e.g. secret name `tightvnc-admin-password` or equivalent). **Never** in docs or committed config. |
| **VNC / view-only password** | Viewer connections: full control vs view-only access. You use the main VNC password for normal control; view-only is a separate password for read-only sessions. | Azure Key Vault or ProtonPass (e.g. `tightvnc-viewer-password`, `tightvnc-view-only-password`). **Never** in docs or committed config. |

- **Policy**: No passwords in documentation, config files committed to git, or logs. See `.cursor/rules/no_secrets_broadcast.mdc` and `docs/security/SECRET_MANAGEMENT_POLICY.md`.
- **Homelab pattern**: Same as NAS/DSM — store in Azure Key Vault (e.g. jarvis-lumina) or ProtonPass; scripts resolve at runtime. Use placeholders in examples only.

---

## Affected MANUS Flows

| Flow | Current | Preferred |
|------|--------|-----------|
| DSM package config (manual/semi-auto) | RDP to Kaiju then configure DSM | TightVNC to Kaiju; same DSM config steps |
| Screenshot / video capture context | `manus_rdp_screenshot_capture.py` (name/context only; capture is local) | No script change required; use TightVNC for the remote session you are capturing |
| FALC → KAIJU remote access | RDP (see `RDP_SETUP_INSTRUCTIONS.md`) | TightVNC as primary; RDP as fallback |

---

## Scripts & Docs to Align

- **`scripts/powershell/configure_all_dsm_packages_via_rdp.ps1`** — Today: checks RDP connectivity to Kaiju, then runs SSH-based config to NAS. **Migration**: Add or prefer TightVNC connectivity check; document "connect via TightVNC" for any manual DSM steps.
- **`scripts/python/manus_rdp_screenshot_capture.py`** — Captures screenshots on the **local** machine (where the script runs). The "RDP" in the name refers to the **context** (e.g. "screenshot while using RDP"). **Recommendation**: When you remote into Kaiju, use TightVNC; the script still works (it captures the machine where it runs). Optional future rename: e.g. `manus_remote_desktop_screenshot_capture.py` if we want to be transport-agnostic.
- **`docs/system/CUSTOM_NAS_DSM_PACKAGES.md`** — Updated to reference this doc and "Remote desktop (prefer TightVNC)".
- **`docs/system/RDP_SETUP_INSTRUCTIONS.md`** — Keep for RDP fallback; add one line that TightVNC is the preferred remote desktop (link to this doc).
- **`docs/system/MANUS_RDP_SCREENSHOT_CAPTURE.md`** — Note that TightVNC is preferred for the remote session; RDP still supported.

---

## Video feed for the agent (@mdv)

So the agent can **"see"** what you're doing (e.g. when #troubleshooting in Cursor):

1. **Use TightVNC** for the session you want the agent to see (connect to Kaiju or the machine you're working on via TightVNC Viewer).
2. **On that machine** (or on the machine whose screen shows the VNC session), run:
   ```powershell
   python scripts/python/manus_rdp_screenshot_capture.py --feed
   ```
   This captures the current screen and writes it to **`data/manus_rdp_captures/mdv_feed_latest.png`** in the Lumina project.
3. The agent can then **read** `data/manus_rdp_captures/mdv_feed_latest.png` when you say "use @mdv" or "see the feed" — no need to attach the image if you've just run `--feed`.

Run `--feed` whenever you want to refresh what the agent sees (e.g. before asking for help with MCP notifications, DSM, or IDE).

## Verify TightVNC configuration

To check that TightVNC Server is installed and running (e.g. on Kaiju):

```powershell
python scripts/python/verify_tightvnc_config.py
```

- **Installed + running**: You can connect with TightVNC Viewer and use `--feed` as above.
- **Installed but not running**: Start the TightVNC Server service or run `tvnserver.exe`.
- **Not installed**: Install from [TightVNC Download](https://www.tightvnc.com/download.php); Server on the machine to be controlled, Viewer on the machine from which you connect.

Credentials (admin + VNC password) stay in Azure Key Vault or ProtonPass; never in docs or config. See "Credentials (two passwords)" above.

## Summary

- **Use TightVNC** for new MANUS remote desktop usage and for DSM/config access to Kaiju.
- **Keep RDP** as a supported fallback; no requirement to remove existing RDP setup.
- **Scripts**: Prefer TightVNC in docs and connectivity checks; screenshot script supports `--feed` for the agent's video feed.
- **Agent video feed**: TightVNC + `manus_rdp_screenshot_capture.py --feed` → agent reads `data/manus_rdp_captures/mdv_feed_latest.png` when you use @mdv.

**Last updated**: 2026-02-04
