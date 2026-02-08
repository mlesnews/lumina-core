# Notification System Credentials - Azure Key Vault Storage

## Overview

The Multi-Channel Notification System retrieves credentials from **Azure Key Vault** as the primary source, with environment variables as fallback.

**ACCOUNT INFORMATION SECRETS REMINDER: LOCATION AZURE VAULT / PROTONPASSCLI / DASHLANE.**

## Required Secrets in Azure Key Vault

### Gmail (TEST) Channel

**Secret Names** (tried in order):
1. `gmail-test-email` - Gmail test account email address
2. `gmail-email` - Fallback Gmail email
3. `nas-email-password` - NAS MailPlus account password
4. `nas-mailplus-password` - Alternative NAS password secret name

**Example:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name gmail-test-email --value "your-gmail-test@gmail.com"
az keyvault secret set --vault-name jarvis-lumina --name nas-email-password --value "your-nas-password"
```

### ProtonMail (PRODUCTION) Channel

**Secret Names** (tried in order):
1. `protonmail-email` - ProtonMail email address
2. `protonmail-username` - Fallback ProtonMail username

**Example:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name protonmail-email --value "your-protonmail@protonmail.com"
```

### SMS (PRODUCTION) Channel

**Secret Names** (tried in order):
1. `sms-phone-number` - SMS recipient phone number
2. `twilio-phone-number` - Fallback Twilio phone number

**Note:** Twilio credentials (`twilio-account-sid`, `twilio-auth-token`) are already stored separately by `LuminaTwilioSMSService`.

**Example:**
```bash
az keyvault secret set --vault-name jarvis-lumina --name sms-phone-number --value "+1234567890"
```

## Credential Retrieval Priority

The system uses `UnifiedSecretsManager` with the following priority:

1. **Azure Key Vault** (Primary) - Company secrets
2. **Environment Variables** (Fallback) - For local development
3. **Config File** (Last Resort) - `config/ticket_notifications.json`

## Verification

After storing credentials in Azure Key Vault, verify they're accessible:

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

The system will:
- ✅ Show which credentials were found in Azure Vault
- ⚠️  Warn about missing credentials
- 💡 Provide instructions for storing missing secrets

## Secret Naming Convention

Following LUMINA patterns:
- Use kebab-case: `gmail-test-email`, `nas-email-password`
- Be descriptive: `sms-phone-number` not just `phone`
- Match existing patterns: `twilio-account-sid`, `protonmail-email`

## Security Notes

- **Never commit credentials to git**
- **Always use Azure Key Vault for production**
- **Environment variables are for local development only**
- **Config files should only contain non-sensitive settings**

## Related Systems

- **UnifiedSecretsManager**: `scripts/python/unified_secrets_manager.py`
- **Azure Key Vault**: `https://jarvis-lumina.vault.azure.net/`
- **Twilio Service**: Already uses Azure Vault for `twilio-account-sid`, `twilio-auth-token`
- **ProtonBridge**: Uses UnifiedSecretsManager for ProtonMail credentials

## Troubleshooting

### Credentials Not Found

1. **Check Azure Vault access:**
   ```bash
   az keyvault secret show --vault-name jarvis-lumina --name gmail-test-email
   ```

2. **Verify secret names match exactly** (case-sensitive)

3. **Check UnifiedSecretsManager logs** for retrieval attempts

4. **Use environment variables as temporary fallback** while fixing Vault access

### Credentials Found But Not Working

1. **Verify secret values are correct** (no extra spaces, correct format)
2. **Check credential permissions** in Azure Vault
3. **Test individual channels** with `--test` flag

---

**Tags**: `#AZURE_KEY_VAULT` `#CREDENTIALS` `#SECURITY` `#NOTIFICATION` `#UNIFIED_SECRETS_MANAGER` `@JARVIS` `@LUMINA`
