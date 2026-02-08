# Azure Key Vault Credentials for backupadm Account

**Date**: 2026-01-02  
**Status**: ✅ ACTIVE  
**Priority**: +++++ (CRITICAL)

## Account Information

**NAS Account**: `backupadm` (+++++ CRITICAL)  
**Azure Key Vault**: `jarvis-lumina`  
**NAS IP**: `10.17.17.32`

## Required Azure Key Vault Secrets

The following secrets MUST exist in Azure Key Vault with `backupadm` credentials:

1. **Secret Name**: `nas-username`
   - **Value**: `backupadm`
   - **Purpose**: NAS username for authentication

2. **Secret Name**: `nas-password`
   - **Value**: `[backupadm password]`
   - **Purpose**: NAS password for authentication

## Alternative Secret Names (Supported)

The system also supports IP-specific secret names (fallback patterns):
- `nas-username-10-17-17-32` (if different credentials per NAS)
- `nas-password-10-17-17-32` (if different credentials per NAS)

However, the primary secrets should be `nas-username` and `nas-password` containing `backupadm` credentials.

## Verification

To verify credentials are correctly stored:

```bash
# Test credential retrieval
python scripts/python/nas_azure_vault_integration.py --ssh-test

# Or via setup script
python scripts/python/nas_push_migration_setup.py
```

## Error: "The user name or password is incorrect"

If you see this error:
1. ✅ Verify Azure Key Vault secrets `nas-username` and `nas-password` exist
2. ✅ Verify `nas-username` secret value is exactly `backupadm`
3. ✅ Verify `nas-password` secret value matches the NAS password for `backupadm`
4. ✅ Check credential cache (credentials are cached for 30 minutes)
5. ✅ Clear cache if needed: Call `NASAzureVaultIntegration.clear_credential_cache()`

## Usage in Scripts

All scripts should retrieve credentials via:

```python
from nas_azure_vault_integration import NASAzureVaultIntegration

vault_integration = NASAzureVaultIntegration()
credentials = vault_integration.get_nas_credentials()

username = credentials.get("username")  # Should be "backupadm"
password = credentials.get("password")   # Should match NAS password
```

## Security Notes (+++++)

- ✅ ALWAYS use Azure Key Vault for credentials (+++++)
- ❌ NEVER hardcode credentials
- ❌ NEVER store credentials in code or config files
- ✅ Credentials are cached in-memory for 30 minutes (matches NAS proxy-cache retention)
- ✅ Credentials are NOT logged (password length only)

---

**Tag**: @AZURE @VAULT @CREDENTIALS @SECURITY @BACKUPADM
