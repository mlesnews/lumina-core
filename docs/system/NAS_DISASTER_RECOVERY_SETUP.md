# NAS Disaster Recovery & Bare-Metal Preparedness

**Status:** ✅ **VERIFIED & ACTIVE**
**Date:** 2025-04-14
**Priority:** 🔴 **CRITICAL - Disaster Recovery**

---

## 🎯 Overview

This document details the "Disaster Preparedness" backup policy implementation using Synology NAS. We utilize a **Hybrid Backup Strategy** to ensure both bare-metal recovery for endpoints and secure off-site backup for NAS data.

**Components:**

1. **Active Backup for Business (ABB):** Provides bare-metal recovery for PCs, Servers, and Virtual Machines.
2. **Hyper Backup:** Backs up the NAS configuration, applications, and data to external targets (Azure/C2).
3. **R5 Integration:** Automated monitoring and status reporting via SSH/API.

---

## ⚙️ Configuration

The Single Source of Truth (SSoT) for this configuration is:
`config/lumina_nas_ssh_config.json`

### **1. Active Backup for Business (Bare-Metal Recovery)**

- **Purpose:** Protects endpoints (PCs) and Servers.
- **Recovery Type:** Bare-metal (Full system restoration).
- **Service Name:** `ActiveBackupBusiness` (Process: `synoabb`)
- **Monitoring:** Process detection via SSH.
- **Target Devices:** Endpoints, Servers.

### **2. Hyper Backup (NAS Data Protection)**

- **Purpose:** Protects the NAS itself (Config, Apps, Data).
- **Recovery Type:** Data & Configuration restoration.
- **Service Name:** `HyperBackup` (Process: `synoimgbkptool`)
- **Monitoring:** Process detection via SSH.
- **Destination:** Azure / C2 / External Storage.

---

## 🛠️ Automation & Monitoring

### **Robust Verification Script**

A dedicated Python script has been created to verify the status of these critical services via SSH. It performs a deep check including:

1. **Connectivity:** Verifies SSH access via Azure Key Vault credentials.
2. **System Time:** Checks NAS clock synchronization.
3. **Process Verification:** Uses `ps aux` to confirm services are actually running (more reliable than `synopkg`).
4. **Activity Check:** Attempts to find recent backup files (where permissions allow).

**Script Location:** `scripts/python/nas_disaster_recovery_verify.py`

**Usage:**

```bash
python scripts/python/nas_disaster_recovery_verify.py
```

**Output Example (Verified 2025-04-14):**

```text
🛡️  Starting Robust Disaster Recovery Verification...
🔌 Connecting to NAS (10.17.17.32)...
✅ SSH Connection Established.
🕒 NAS System Time: Wed Dec 10 08:38:20 AST 2025

🔍 Verifying Active Backup for Business (Bare-Metal)...
   ✅ Service Process: DETECTED (Running)
   ✅ Data Directory Found: /volume1/ActiveBackupforBusiness

🔍 Verifying Hyper Backup (NAS Data)...
   ✅ Service Process: DETECTED (Running)
```

### **R5 Integration**

The `nas_azure_vault_integration.py` library is configured to publish SSH command results to the Lumina/R5 API (`nas_ssh_command` event). This allows the Living Context Matrix to be aware of the backup status.

---

## 📋 Recovery Procedure (Summary)

1. **Endpoint Failure (PC/Server):**
   - Boot from Synology Active Backup Recovery Media (USB).
   - Connect to NAS (10.17.17.32).
   - Select restore point.
   - Perform bare-metal restore.

2. **NAS Failure:**
   - Reinstall DSM.
   - Install Hyper Backup.
   - Connect to Backup Destination (Azure/C2).
   - Restore System Configuration & Data.

---

## ✅ Verification Checklist

- [x] `lumina_nas_ssh_config.json` updated with DR settings.
- [x] `nas_disaster_recovery_verify.py` created and tested.
- [x] Dependencies (`azure-keyvault-secrets`, `paramiko`) installed.
- [x] **Live Verification:** Confirmed services are running via SSH.
