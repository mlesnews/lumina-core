# Proton Bridge Credentials Management
## Storage in ProtonPassCli and Azure Key Vault

**Date**: 2026-01-15  
**Status**: ✅ Configuration Updated

---

## 🔐 Credential Storage Strategy

### Dual Storage Architecture

Proton Bridge credentials are stored in **both** ProtonPassCli and Azure Key Vault for:
- **Redundancy**: If one source fails, fallback to the other
- **Security**: Dual-layer protection
- **Compliance**: Enterprise-grade security with Azure Vault

### Priority Order

1. **ProtonPassCli** (Primary Source)
   - Zero-knowledge encryption
   - Local CLI access
   - Privacy-focused

2. **Azure Key Vault** (Fallback/Redundancy)
   - Enterprise security
   - High availability
   - Audit logging

3. **Environment Variables** (Last Resort)
   - Only if both above fail
   - Not recommended for production

---

## 📋 Storage Locations

### ProtonPassCli Entries

**Entry Names** (tried in order):
- `proton-bridge-password`
- `proton-bridge`
- `protonmail-bridge`
- `proton-bridge-mlesn`
- `proton-bridge-glesn`

**How to Store**:
```bash
# Using ProtonPassCli
protonpass create \
  --name "proton-bridge-password" \
  --username "[Bridge-generated username]" \
  --password "[Bridge-generated password]" \
  --url "protonmail://bridge" \
  --note "Proton Bridge credentials"
```

**Or using Python script**:
```python
from scripts.python.get_proton_bridge_credentials import ProtonBridgeCredentialManager

manager = ProtonBridgeCredentialManager()
manager.store_bridge_credentials(
    username="[Bridge username]",
    password="[Bridge password]",
    account_name="proton-bridge"
)
```

### Azure Key Vault Secrets

**Secret Names**:
- `proton-bridge-username`
- `proton-bridge-password`
- `proton-bridge-mlesn-username`
- `proton-bridge-mlesn-password`
- `proton-bridge-glesn-username`
- `proton-bridge-glesn-password`

**Vault URL**: `https://jarvis-lumina.vault.azure.net/`

**How to Store**:
```python
from azure_service_bus_integration import AzureKeyVaultClient

vault = AzureKeyVaultClient(vault_url="https://jarvis-lumina.vault.azure.net/")
vault.set_secret("proton-bridge-username", "[Bridge username]")
vault.set_secret("proton-bridge-password", "[Bridge password]")
```

---

## 🔧 Retrieval Methods

### Method 1: Python Script (Recommended)

```bash
# Get complete credentials
python scripts/python/get_proton_bridge_credentials.py

# Get username only
python scripts/python/get_proton_bridge_credentials.py --username-only

# Get password only
python scripts/python/get_proton_bridge_credentials.py --password-only

# Get for specific account
python scripts/python/get_proton_bridge_credentials.py --account-name proton-bridge-mlesn
```

**Output** (JSON):
```json
{
  "username": "[Bridge username]",
  "password": "[Bridge password]",
  "source": "protonpasscli",
  "timestamp": "2026-01-15T...",
  "account_name": "proton-bridge"
}
```

### Method 2: Direct ProtonPassCli

```bash
# Get password
protonpass get --name "proton-bridge-password" --password-only

# Get full entry
protonpass get --name "proton-bridge-password" --show-details
```

### Method 3: Azure Key Vault

```python
from azure_service_bus_integration import AzureKeyVaultClient

vault = AzureKeyVaultClient(vault_url="https://jarvis-lumina.vault.azure.net/")
username = vault.get_secret("proton-bridge-username")
password = vault.get_secret("proton-bridge-password")
```

---

## ⚙️ N8N Integration

### Workflow Configuration

N8N workflows automatically retrieve credentials using the retrieval script:

**Workflow Node**: "Get Proton Bridge Credentials"
- Executes: `python3 scripts/python/get_proton_bridge_credentials.py`
- Parses JSON output
- Falls back to environment variables if script fails

**Configuration File**: `config/n8n/proton_bridge_workflow.json`

### Environment Variables (Fallback)

If ProtonPassCli and Azure Vault are unavailable, N8N can use:
```bash
PROTON_BRIDGE_HOST=host.docker.internal
PROTON_BRIDGE_IMAP_PORT=1143
PROTON_BRIDGE_SMTP_PORT=1025
PROTON_BRIDGE_USERNAME=[Bridge username]
PROTON_BRIDGE_PASSWORD=[Bridge password]
```

---

## 📝 Storing New Credentials

### Initial Setup

1. **Get Bridge Credentials from Bridge UI**:
   - Open Proton Bridge
   - Click on your account
   - Note the IMAP/SMTP username and password
   - These are Bridge-generated, NOT your ProtonMail password

2. **Store in ProtonPassCli**:
   ```bash
   python scripts/python/get_proton_bridge_credentials.py --store \
     --username "[Bridge username]" \
     --password "[Bridge password]" \
     --account-name "proton-bridge"
   ```

3. **Verify Storage**:
   ```bash
   # Check ProtonPassCli
   protonpass get --name "proton-bridge-password"
   
   # Check Azure Vault (via script)
   python scripts/python/get_proton_bridge_credentials.py
   ```

### Updating Credentials

If Bridge password changes:

```bash
python scripts/python/get_proton_bridge_credentials.py --store \
  --username "[New Bridge username]" \
  --password "[New Bridge password]" \
  --account-name "proton-bridge"
```

---

## 🔍 Verification

### Check Credential Availability

```bash
# Test retrieval
python scripts/python/get_proton_bridge_credentials.py

# Expected output:
# ✅ Retrieved password from ProtonPassCli: proton-bridge-password
# ✅ Retrieved username from ProtonPassCli: proton-bridge-password
# Username: ✅ Found
# Password: ✅ Found
# Source: protonpasscli
```

### Test N8N Integration

1. Import workflow: `config/n8n/proton_bridge_workflow.json`
2. Execute "Get Proton Bridge Credentials" node
3. Verify credentials are retrieved
4. Test IMAP/SMTP connection

---

## 🔒 Security Notes

### ProtonPassCli
- **Zero-knowledge encryption**: Proton cannot see your passwords
- **Local CLI**: No cloud transmission
- **Open source**: Auditable

### Azure Key Vault
- **Enterprise security**: SOC 2, PCI DSS, ISO 27001
- **Access control**: Azure RBAC
- **Audit logging**: Complete access tracking
- **High availability**: 99.99% SLA

### Best Practices
- ✅ Store in both systems for redundancy
- ✅ Use retrieval script (handles fallback automatically)
- ✅ Never hardcode credentials in code
- ✅ Rotate credentials periodically
- ✅ Use different credentials for different accounts (mlesn, glesn)

---

## 📄 Configuration Files

- **Credential Config**: `config/proton_bridge_config.json`
- **N8N Workflow**: `config/n8n/proton_bridge_workflow.json`
- **N8N Config**: `config/n8n/proton_bridge_n8n_config.json`
- **Retrieval Script**: `scripts/python/get_proton_bridge_credentials.py`

---

## ✅ Status

**Configuration Updated**: ✅  
**ProtonPassCli Integration**: ✅  
**Azure Vault Integration**: ✅  
**N8N Workflow Updated**: ✅  
**Documentation**: ✅  

**Ready to use!** Credentials will be retrieved from ProtonPassCli (primary) or Azure Vault (fallback) automatically. 🚀
