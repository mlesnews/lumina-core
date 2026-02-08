# Triad Password Manager Strategy (+doc)

**Architecture**: The Password Trifecta
**Standard**: enterprise-v6
**Governance**: Change Management (@cm)

---

## 🏗️ The Three Tiers

### 1. Tier 1: Azure Key Vault (Primary Enterprise)
- **Purpose**: Single Source of Truth (SSoT) for all organizational secrets.
- **Access**: Managed via `UnifiedSecretManager` (Azure CLI / Default ID). NAS access uses `NASAzureVaultIntegration` (same vault; optional Triad coordinator fallback).
- **NAS credentials**: Store `nas-username` (e.g. `backupadm`) / `nas-password` in Azure; same can exist in ProtonPass CLI (Tier 2). `NASAzureVaultIntegration` uses Azure → UnifiedSecretManager → ProtonPass CLI (Clawedbot-style). See `config/triad_nas_credentials.json` and `config/azure/key_vault_config.json` → `nas_secrets`.
- **Status**: ✅ **Operational** (58+ secrets).

### 2. Tier 2: ProtonPass CLI (Primary Automation)
- **Purpose**: Zero-knowledge redundancy and local automation backup.
- **Access**: Managed via `pass-cli.exe`.
- **Status**: ⚠️ **Awaiting Baseline Sync**.

### 3. Tier 3: Dashlane (Manual/Human)
- **Purpose**: High-availability human access and emergency browser redundancy.
- **Access**:
    *   **Web Extension**: Sideloaded into **Neo Browser** automation.
    *   **Web App**: Accessible via `https://www.dashlane.com/login`.
- **Status**: ℹ️ **Manual Tier** (Web Only - No Desktop App).

---

## 🔄 Synchronization Strategy
- **Baseline**: Az ➔ Proton ➔ Dashlane (Manual).
- **Quorum Rule**: AI-guided verification via `triad_quorum_engine.py`.
- **Failover**: Automatic redirection if Tier 1 is unreachable due to network congestion.

---

## 🛡️ Risk Mitigation
- **Proxy-cache (NAS) server**: We use a proxy-cache (NAS) server that **only pulls passwords every thirty minutes**. In-memory credential cache TTL in `NASAzureVaultIntegration` is 30 minutes to match this; do not shorten it without aligning proxy-cache refresh.
- **Encrypted Buffer**: To avoid the `Bad file descriptor` and `ECONNRESET` issues observed during the NAS migration, secrets will be cached in a local **Encrypted Buffer** if the NAS Proxy Cache (NPCS) latency exceeds 500ms.
