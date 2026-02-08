# Notification Credentials Investigation - Azure Vault Integration

**Date**: 2026-01-12  
**Investigation**: Deep dive into credential storage for Multi-Channel Notification System  
**Breadcrumb**: @triad (Triad Password Manager System)

## Executive Summary

The Multi-Channel Notification System was designed to use **Azure Key Vault** (via Triad system) as the primary credential source, but the required secrets are **NOT YET STORED** in Azure Vault.

## Current State

### ✅ What's Working

1. **UnifiedSecretsManager Integration**: The notification system correctly initializes `UnifiedSecretsManager` with Azure Key Vault as primary source
2. **Triad System Available**: Azure Key Vault and ProtonPass CLI are both available
3. **Code Structure**: The credential retrieval logic is in place with proper fallback to environment variables

### ❌ What's Missing

**Required secrets NOT found in Azure Key Vault:**

1. `gmail-test-email` - Gmail test account email address
2. `nas-email-password` - NAS MailPlus account password for sending emails
3. `protonmail-email` - ProtonMail production email address
4. `sms-phone-number` - SMS recipient phone number

### 🔍 Related Secrets Found

From Triad comparison, these related secrets exist but may not be the right ones:
- `login-account-gmail-ceo-gmail-email` - Might be Gmail email (but not specifically "test")
- `login-account-gmail-ceo-gmail-app-password` - Gmail app password (different from NAS email password)
- `twilio-account-sid`, `twilio-auth-token` - Twilio credentials (already used by Twilio service)
- `twilio-phone-number` - Twilio phone number (might be the sender, not recipient)

## Triad System Context

The **@triad** breadcrumb refers to the **Triad Password Manager System**:
- **Azure Key Vault** (Primary) - Company secrets
- **ProtonPass CLI** (Secondary) - Personal/secure passwords
- **Dashlane** (Tertiary) - Manual/extension-only

**Current Status:**
- ✅ Azure Key Vault: Available (62 secrets)
- ✅ ProtonPass CLI: Available
- ⚠️  Dashlane: Web Extension Only (Manual Tier)

**Sync Status:**
- ⚠️  All 62 secrets in Azure Vault have sync gaps (not synced to ProtonPass/Dashlane)
- This is expected - notification credentials should be stored in Azure Vault first

## Required Actions

### 1. Store Notification Credentials in Azure Key Vault

**Gmail (TEST) Channel:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name gmail-test-email --value "your-gmail-test@gmail.com"
az keyvault secret set --vault-name jarvis-lumina --name nas-email-password --value "your-nas-mailplus-password"
```

**ProtonMail (PRODUCTION) Channel:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name protonmail-email --value "your-protonmail@protonmail.com"
```

**SMS (PRODUCTION) Channel:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name sms-phone-number --value "+1234567890"
```

### 2. Verify Credential Retrieval

After storing credentials:
```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

Expected output:
- ✅ Credentials retrieved from Azure Vault
- ✅ All three channels configured
- ✅ Test connections successful

### 3. Optional: Sync to ProtonPass (Triad Baseline)

For redundancy, sync to ProtonPass (excluding gating secrets):
```bash
python scripts/python/triad_baseline_sync.py
```

**Note:** Gating secrets (like `protonpass-extra-password`) are excluded from sync for security.

## Code Status

### ✅ Fixed Issues

1. **Bug Fix**: Removed `self.secrets_manager` calls in `else` block when secrets_manager is None
2. **Azure Vault Integration**: Code correctly uses `UnifiedSecretsManager` to retrieve credentials
3. **Fallback Logic**: Proper fallback to environment variables when Azure Vault unavailable

### 📋 Current Implementation

The notification system:
1. Initializes `UnifiedSecretsManager` with Azure Key Vault as primary source
2. Attempts to retrieve credentials from Azure Vault first
3. Falls back to environment variables if Azure Vault unavailable or secret not found
4. Logs which credentials were found and from which source

## Secret Naming Convention

Following LUMINA patterns:
- **kebab-case**: `gmail-test-email`, `nas-email-password`
- **Descriptive**: `sms-phone-number` not just `phone`
- **Consistent**: Matches existing patterns like `twilio-account-sid`, `protonmail-email`

## Security Notes

- ✅ **Never commit credentials to git**
- ✅ **Always use Azure Key Vault for production**
- ✅ **Environment variables are for local development only**
- ✅ **Config files should only contain non-sensitive settings**
- ✅ **Triad system provides redundancy across three sources**

## Next Steps

1. **Store credentials in Azure Key Vault** using the commands above
2. **Test credential retrieval** with `--test` flag
3. **Verify all three channels** are working
4. **Optional: Run Triad baseline sync** for redundancy

## Related Documentation

- `docs/system/NOTIFICATION_CREDENTIALS_AZURE_VAULT.md` - Credential storage guide
- `scripts/python/unified_secrets_manager.py` - Unified Secrets Manager
- `scripts/python/triad_vault_comparison.py` - Triad system comparison
- `scripts/python/triad_baseline_sync.py` - Triad baseline sync
- `scripts/python/triad_quorum_engine.py` - Quorum-based retrieval

---

**Tags**: `#AZURE_KEY_VAULT` `#CREDENTIALS` `#SECURITY` `#NOTIFICATION` `#TRIAD` `#INVESTIGATION` `@JARVIS` `@LUMINA`
