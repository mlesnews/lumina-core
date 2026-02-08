# Notification Credentials - Triad System Resolution

**Date**: 2026-01-12  
**Resolution**: Credentials stored in ProtonPass CLI (Triad system)  
**Breadcrumb**: @triad

## Summary

The notification system credentials are stored in **ProtonPass CLI** as part of the Triad Password Manager System. The `UnifiedSecretsManager` automatically retrieves credentials from:

1. **Azure Key Vault** (Primary) - Company secrets
2. **ProtonPass CLI** (Secondary) - Personal/secure passwords ← **Credentials are here**
3. **Environment Variables** (Fallback) - Local development

## Triad System Integration

The notification system uses `UnifiedSecretsManager` which implements the Triad pattern:

```
Azure Key Vault → ProtonPass CLI → Environment Variables
     (Primary)         (Secondary)        (Fallback)
```

### Current Status

✅ **UnifiedSecretsManager**: Properly configured with Triad fallback  
✅ **ProtonPass CLI**: Available and accessible  
✅ **Auto-Retrieval**: System automatically tries Azure Vault first, then ProtonPass

### Credential Retrieval

The system retrieves credentials in this order:

1. **Azure Key Vault** - Tries first (company secrets)
2. **ProtonPass CLI** - Falls back automatically if not in Azure Vault
3. **Environment Variables** - Final fallback

**Secret Names Expected:**
- `gmail-test-email` - Gmail test account
- `nas-email-password` - NAS MailPlus password
- `protonmail-email` - ProtonMail email address
- `sms-phone-number` - SMS recipient phone number

## ProtonPass CLI Integration

### Updated Retrieval Method

The `UnifiedSecretsManager` has been updated to use correct ProtonPass CLI commands:

```python
# Uses: pass-cli.exe item view --item-title <name> --field password --output json
```

### Authentication

ProtonPass CLI requires authentication. The system will:
- Use existing ProtonPass session if available
- Prompt for extra password if needed (for protected items)

## Verification

To verify credentials are being retrieved from ProtonPass:

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

The system will:
- ✅ Try Azure Key Vault first
- ✅ Automatically fallback to ProtonPass CLI
- ✅ Show which source provided each credential
- ✅ Use environment variables as final fallback

## Next Steps

1. **Verify ProtonPass Authentication**: Ensure ProtonPass CLI is logged in
2. **Test Credential Retrieval**: Run `--test` to verify credentials are found
3. **Optional: Sync to Azure Vault**: For redundancy, sync credentials from ProtonPass to Azure Vault using `triad_baseline_sync.py`

## Related Systems

- **Triad System**: `scripts/python/triad_vault_comparison.py`
- **Triad Sync**: `scripts/python/triad_baseline_sync.py`
- **Unified Secrets Manager**: `scripts/python/unified_secrets_manager.py`

---

**Tags**: `#TRIAD` `#PROTONPASS` `#CREDENTIALS` `#NOTIFICATION` `#UNIFIED_SECRETS_MANAGER` `@JARVIS` `@LUMINA`
