# Proton Bridge Credential Names Reference
## Actual Secret/Entry Names Based on Configuration

**Date**: 2026-01-15  
**Status**: ✅ Configuration Verified

---

## 📋 Actual Credential Names (From Config Files)

Based on `config/proton_bridge_accounts.json` and other config files, here are the **actual** secret/entry names:

### For mlesn Account

**Azure Vault Secret Names**:
- `proton-bridge-mlesn-password` ✅ (from proton_bridge_accounts.json)
- `protonmail-bridge-password` (from proton_family_integration.json)
- `protonmail-password` (from protonbridge_config.json)

**ProtonPassCli Entry Names**:
- `proton-bridge-mlesn-password`
- `proton-bridge-mlesn`
- `protonmail-bridge-password`
- `proton-bridge-password`

**Username**: 
- Bridge username is typically the ProtonMail email: `mlesn@protonmail.com`
- Or stored separately as: `protonmail-username` or `protonmail-email`

### For glesn Account

**Azure Vault Secret Names**:
- `proton-bridge-glesn-password` ✅ (from proton_bridge_accounts.json)
- `protonmail-bridge-password` (shared if using same Bridge instance)

**ProtonPassCli Entry Names**:
- `proton-bridge-glesn-password`
- `proton-bridge-glesn`
- `protonmail-bridge-password`

**Username**:
- Bridge username: `glesn@protonmail.com`
- Or stored as: `protonmail-username` or `protonmail-email`

---

## 🔍 How to Verify What's Actually Stored

### Check ProtonPassCli

```bash
# List all entries
protonpass list

# Search for Bridge entries
protonpass list | grep -i "proton\|bridge\|mail"
```

### Check Azure Vault

Since Azure Vault doesn't support listing all secrets easily, you can:

1. **Check Azure Portal**:
   - Go to: https://portal.azure.com
   - Navigate to: Key Vaults → jarvis-lumina
   - Check Secrets section

2. **Try Common Names**:
   ```python
   from azure_service_bus_integration import AzureKeyVaultClient
   
   vault = AzureKeyVaultClient(vault_url="https://jarvis-lumina.vault.azure.net/")
   
   # Try these names
   names_to_try = [
       "proton-bridge-mlesn-password",
       "proton-bridge-glesn-password",
       "protonmail-bridge-password",
       "protonmail-password",
       "protonmail-username",
       "protonmail-email"
   ]
   
   for name in names_to_try:
       try:
           value = vault.get_secret(name)
           print(f"✅ Found: {name}")
       except:
           print(f"❌ Not found: {name}")
   ```

---

## 🔧 Update Script to Use Correct Names

The credential retrieval script has been updated to try these names in order:

**For Password** (account_name="mlesn"):
1. `proton-bridge-mlesn-password` ✅ (from config)
2. `proton-bridge-mlesn`
3. `protonmail-bridge-password`
4. `proton-bridge-password`
5. `protonmail-password`

**For Username**:
1. `proton-bridge-mlesn-username`
2. `protonmail-username`
3. `protonmail-email`
4. `proton-account-username`

---

## ✅ Configuration Files Reference

### `config/proton_bridge_accounts.json`
```json
{
  "accounts": {
    "mlesn": {
      "bridge_password_secret": "proton-bridge-mlesn-password"  ✅
    },
    "glesn": {
      "bridge_password_secret": "proton-bridge-glesn-password"  ✅
    }
  }
}
```

### `config/proton_family_integration.json`
```json
{
  "protonmail": {
    "credentials": {
      "secrets": [
        "protonmail-username",
        "protonmail-password",
        "protonmail-bridge-password"  ✅
      ]
    }
  }
}
```

### `config/protonbridge_config.json`
```json
{
  "credentials": {
    "username_secret": "protonmail-username or protonmail-email",
    "password_secret": "protonmail-password"  ✅
  }
}
```

---

## 🚀 Usage

### Get Credentials for mlesn Account

```bash
python scripts/python/get_proton_bridge_credentials.py --account-name mlesn
```

### Get Credentials for glesn Account

```bash
python scripts/python/get_proton_bridge_credentials.py --account-name glesn
```

### Get Password Only

```bash
python scripts/python/get_proton_bridge_credentials.py --account-name mlesn --password-only
```

### Get Username Only

```bash
python scripts/python/get_proton_bridge_credentials.py --account-name mlesn --username-only
```

---

## 📝 Notes

1. **Bridge Username**: Typically the ProtonMail email address (e.g., `mlesn@protonmail.com`)
2. **Bridge Password**: Bridge-generated password (NOT your ProtonMail web password)
3. **Multiple Accounts**: If using Proton Family, each account may have separate credentials
4. **ProtonPassCli**: Entry names may differ - check with `protonpass list`

---

**Configuration updated to use actual secret names from your config files!** ✅
