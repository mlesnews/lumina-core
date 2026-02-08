# Custom NAS DSM Packages

Catalog of custom NAS DSM packages built for the homelab. These are either **Container Manager projects** (docker-compose) or **DSM package configurations** managed via SSH/API.

---

## @PEAK for this project

**@PEAK** here means **optimal configuration** and **best-of-breed** choice (see `config/jarvis_homelab_control_config.json`: `peak_strategy: "optimal_configuration"`).

For **custom NAS DSM packages**, the @PEAK pick is:

| What | @PEAK choice |
|------|----------------|
| **Primary custom package** | **LUMINA Homelab MCP Central** (`lumina-homelab-mcp-central`) — the single canonical Container Manager project (MCP stack, n8n, MANUS, AWS MCPs, etc.). |
| **Deployment** | `python scripts/python/deploy_mcp_servers_to_nas.py deploy --all` or SSH + `docker-compose up -d --build` from `containerization/services/nas-mcp-servers/`. |
| **Credentials** | Homelab chain: Azure Key Vault → ProtonPass → NAS-DSM config (`nas_user`). Same as @MANUS and WSL backup. |
| **DSM native packages** | `scripts/python/configure_all_dsm_packages_full_auto.py` — full-auto via SSH/synopkg; LDAP join / first-time Container Manager project via DSM UI when required. |

Use the **LUMINA Homelab MCP Central** descriptor and the automation above as the default (@PEAK) unless you need a different stack or flow.

---

## 1. LUMINA Homelab MCP Central

**Type**: Container Manager project (custom “package” descriptor)
**Package name**: `lumina-homelab-mcp-central`
**Display name**: LUMINA Homelab MCP Central

### Definition

- **Descriptor**: `containerization/services/nas-mcp-servers/dsm-container-package.json`
  (mirror: `deploy_to_nas/nas-mcp-servers/dsm-container-package.json`)
- **Deployment**: DSM Container Manager → Create Project from `docker-compose.yml` in that directory
- **Service name**: `lumina-mcp-central`
- **Version**: 1.0.0 | **Firmware**: DSM 7.0+ | **Arch**: x86_64

### Contents

- **Core**: n8n (5678), MANUS MCP (8085), ElevenLabs MCP (8086)
- **AWS MCPs**: Diagram, Documentation, CDK, Terraform, Lambda, Cost Analysis, Bedrock KB, Nova Canvas (8087–8094)
- **Synology**: Synology Download MCP (8095), SynoLink MCP (8096)
- **Data**: MariaDB/SQLite MCP (8097–8098), Filesystem, Git, Brave Search, Puppeteer, GitHub, Slack (8099–8104)
- **Models**: KUBE at `http://10.17.17.32:8000`, volumes at `/volume1/models` (M: on Windows)

### Deploy

```powershell
# From project root
python scripts/python/deploy_mcp_servers_to_nas.py deploy --all
```

Or via SSH (see `containerization/services/nas-mcp-servers/DSM_DEPLOYMENT.md`):

```bash
scp -r containerization/services/nas-mcp-servers <user>@10.17.17.32:/volume1/docker/
ssh <user>@10.17.17.32
cd /volume1/docker/nas-mcp-servers && docker-compose -f docker-compose.yml up -d --build
```

### Docs

- **Deployment**: `containerization/services/nas-mcp-servers/DSM_DEPLOYMENT.md`
- **Activation**: `containerization/services/nas-mcp-servers/ACTIVATE_SERVICES.md`
- **Hybrid**: `containerization/services/nas-mcp-servers/HOMELAB_HYBRID_SETUP.md`
- **Deploy script**: `containerization/services/nas-mcp-servers/deploy-to-dsm.ps1`

---

## 2. DSM Package Full-Auto Configuration

**Type**: DSM native packages configured via SSH / `synopkg`
**Automation**: No browser; SSH + API only where possible.

### Script

- **Script**: `scripts/python/configure_all_dsm_packages_full_auto.py`
- **Docs**: `docs/system/DSM_PACKAGES_FULL_AUTO_CONFIGURATION.md`

### Packages configured

- **LDAP / Azure AD**: Config prepared via script; join still via DSM UI (security).
- **Container Manager (Docker)**: Proxy-cache and other compose stacks; first-time project create via DSM UI if required.
- **Cloud Sync**: Package configured and started; cloud provider setup is manual.
- **Git Server**: Local Git “cloud” for LUMINA – install from Package Center, create shared folder for repos, map as G: so `G:\git\repositories` matches `config/repository_structure.json` and `config/git_gitlens_enterprise.json`. See **`docs/system/NAS_DSM_GIT_SERVER_SETUP.md`**.
- **Others**: LDAPServer, DomainController, Docker, ActiveBackupBusiness, HyperBackup (status/start checks via SSH).

### Credentials

- NAS access: Azure Key Vault / ProtonPass + `config/nas_dsm_jupyter_config.json` (`nas_user`), same as @MANUS and WSL backup.

---

## 3. Related automation

| Area              | Script / config |
|-------------------|------------------|
| DSM LDAP          | `scripts/python/configure_dsm_ldap_azure_ad.py`, `automate_dsm_ldap_join.py` |
| DSM SSO / SAML    | `scripts/python/setup_dsm_saml_sso.py`, `manus_dsm_sso_automation.py` |
| Package Center UI | `scripts/python/jarvis_open_dsm_package_center.py` |
| MANUS DSM tasks   | `scripts/python/manus_dsm_task_scheduler_automation.py`, `manus_complete_all_dsm_tasks.py` |
| Remote desktop (prefer TightVNC) | `scripts/powershell/configure_all_dsm_packages_via_rdp.ps1`; see `docs/system/REMOTE_DESKTOP_TIGHTVNC.md` |

---

## 4. DSM Git Server (local Git “cloud”)

**Type**: DSM native package from Package Center
**Purpose**: Host Git repos on the NAS so LUMINA uses it as the local enterprise Git “cloud” instead of only `data/local_backup`.

- **Install**: Package Center → **Git Server** → Install & launch.
- **Share**: Create a shared folder for repos (e.g. `git`), set it as the Git Server repository root.
- **Windows**: Map that share as **G:** so `G:\git\repositories` exists; LUMINA config and `config/lumina_network_drives.json` use G: (`config/repository_structure.json`, `config/git_gitlens_enterprise.json`).
- **Doc**: **`docs/system/NAS_DSM_GIT_SERVER_SETUP.md`** – full setup, G: mapping, fallback to `data/local_backup`.

---

## Summary

| Custom package              | Kind              | Descriptor / entry point |
|----------------------------|-------------------|---------------------------|
| LUMINA Homelab MCP Central | Container Manager | `dsm-container-package.json` + `docker-compose.yml` in `nas-mcp-servers` |
| DSM packages (LDAP, Cloud, etc.) | synopkg / SSH   | `configure_all_dsm_packages_full_auto.py` |
| DSM Git Server (local Git cloud) | Package Center   | `docs/system/NAS_DSM_GIT_SERVER_SETUP.md` |

**Tags**: #DSM #NAS #MANUS #LUMINA #custom-packages #git
