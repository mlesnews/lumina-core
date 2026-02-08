# Proton Bridge Credential Storage Instructions
## Store Credentials in ProtonPassCli and Azure Vault

**Date**: 2026-01-15  
**Status**: ✅ Configuration Updated - Ready for Credential Storage

---

## ✅ What Was Updated

### Configuration Files Updated
1. **`config/proton_bridge_config.json`**
   - Updated to reference ProtonPassCli (primary) and Azure Vault (redundancy)
   - Added entry names and secret names

2. **`config/n8n/proton_bridge_workflow.json`**
   - Updated credential retrieval to use script
   - Falls back to environment variables if needed

3. **`config/n8n/proton_bridge_n8n_config.json`**
   - Updated to reference credential storage locations
   - Added credential source information

### Scripts Created
1. **`scripts/python/get_proton_bridge_credentials.py`**
   - Retrieves credentials from ProtonPassCli (primary)
   - Falls back to Azure Vault if ProtonPassCli unavailable
   - Can store credentials in both systems

---

## 📝 How to Store Credentials

### Step 1: Get Bridge Credentials

1. **Open Proton Bridge** on your host PC
2. **Click on your ProtonMail account** in Bridge
3. **Note the credentials**:
   - **Username**: Bridge-generated username (shown in Bridge UI)
   - **Password**: Bridge-generated password (shown in Bridge UI)
   - **Note**: These are NOT your ProtonMail web password!

### Step 2: Store in ProtonPassCli (Primary)

#### Option A: Using ProtonPassCli Directly

```bash
# Store Bridge credentials
protonpass create \
  --name "proton-bridge-password" \
  --username "[Bridge-generated username]" \
  --password "[Bridge-generated password]" \
  --url "protonmail://bridge" \
  --note "Proton Bridge credentials for email integration"
```

#### Option B: Using Python Script

```bash
python scripts/python/get_proton_bridge_credentials.py --store \
  --username "[Bridge-generated username]" \
  --password "[Bridge-generated password]" \
  --account-name "proton-bridge"
```

**This will store in BOTH ProtonPassCli and Azure Vault automatically!**

### Step 3: Store in Azure Vault (Redundancy)

If you want to store manually in Azure Vault:

```python
from azure_service_bus_integration import AzureKeyVaultClient

vault = AzureKeyVaultClient(vault_url="https://jarvis-lumina.vault.azure.net/")

# Store username
vault.set_secret("proton-bridge-username", "[Bridge-generated username]")

# Store password
vault.set_secret("proton-bridge-password", "[Bridge-generated password]")
```

**Or use the Python script** (stores in both automatically):
```bash
python scripts/python/get_proton_bridge_credentials.py --store \
  --username "[Bridge username]" \
  --password "[Bridge password]"
```

---

## 🔍 Verify Storage

### Check ProtonPassCli

```bash
# List entries
protonpass list

# Get specific entry
protonpass get --name "proton-bridge-password" --show-details
```

### Check Azure Vault

```python
from azure_service_bus_integration import AzureKeyVaultClient

vault = AzureKeyVaultClient(vault_url="https://jarvis-lumina.vault.azure.net/")
username = vault.get_secret("proton-bridge-username")
password = vault.get_secret("proton-bridge-password")
```

### Test Retrieval Script

```bash
# Test credential retrieval
python scripts/python/get_proton_bridge_credentials.py

# Expected output:
# ✅ Retrieved password from ProtonPassCli: proton-bridge-password
# ✅ Retrieved username from ProtonPassCli: proton-bridge-password
# Username: ✅ Found
# Password: ✅ Found
# Source: protonpasscli
```

---

## 📋 Entry Names (ProtonPassCli)

The script will try these entry names in order:

1. `proton-bridge-password`
2. `proton-bridge`
3. `protonmail-bridge`
4. `proton-bridge-mlesn`
5. `proton-bridge-glesn`

**Recommendation**: Use `proton-bridge-password` for consistency.

---

## 📋 Secret Names (Azure Vault)

The script will try these secret names in order:

**For Username**:
- `proton-bridge-username`
- `proton-bridge-proton-bridge-username`
- `proton-bridge`

**For Password**:
- `proton-bridge-password`
- `proton-bridge-username-password`
- `proton-bridge-proton-bridge-password`
- `proton-bridge`

**Recommendation**: Use `proton-bridge-username` and `proton-bridge-password` for consistency.

---

## 🔧 N8N Integration

### Automatic Retrieval

N8N workflows will automatically retrieve credentials using the script:

1. **Workflow executes**: `python3 scripts/python/get_proton_bridge_credentials.py`
2. **Script tries**: ProtonPassCli first, then Azure Vault
3. **Returns**: JSON with username and password
4. **Workflow uses**: Credentials for IMAP/SMTP connection

### Manual Configuration (If Needed)

If automatic retrieval fails, you can set environment variables in N8N:

```bash
PROTON_BRIDGE_HOST=host.docker.internal
PROTON_BRIDGE_IMAP_PORT=1143
PROTON_BRIDGE_SMTP_PORT=1025
PROTON_BRIDGE_USERNAME=[Bridge username]
PROTON_BRIDGE_PASSWORD=[Bridge password]
```

---

## ✅ Current Status

### ✅ Completed
- Configuration files updated to reference ProtonPassCli and Azure Vault
- Credential retrieval script created
- N8N workflows updated to use script
- Documentation created

### ⏳ Pending
- **Store credentials** in ProtonPassCli (when Bridge is set up)
- **Store credentials** in Azure Vault (for redundancy)
- **Test credential retrieval** after storage

---

## 🚀 Next Steps

1. **Set up Proton Bridge** (if not already done)
   - Install Bridge from: https://proton.me/mail/bridge
   - Add your ProtonMail account
   - Note the Bridge-generated credentials

2. **Store Credentials**:
   ```bash
   python scripts/python/get_proton_bridge_credentials.py --store \
     --username "[Bridge username]" \
     --password "[Bridge password]"
   ```

3. **Verify Storage**:
   ```bash
   python scripts/python/get_proton_bridge_credentials.py
   ```

4. **Test N8N Integration**:
   - Import workflow: `config/n8n/proton_bridge_workflow.json`
   - Execute "Get Proton Bridge Credentials" node
   - Verify credentials are retrieved

---

## 📄 Files Reference

- **Credential Script**: `scripts/python/get_proton_bridge_credentials.py`
- **Bridge Config**: `config/proton_bridge_config.json`
- **N8N Workflow**: `config/n8n/proton_bridge_workflow.json`
- **N8N Config**: `config/n8n/proton_bridge_n8n_config.json`
- **Documentation**: `docs/email/PROTON_BRIDGE_CREDENTIALS.md`

---

**Configuration complete!** Once you store the credentials in ProtonPassCli and/or Azure Vault, the system will automatically retrieve them. 🚀
