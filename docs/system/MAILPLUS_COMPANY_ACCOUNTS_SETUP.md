# MailPlus Company Email Accounts Setup

**Date**: 2026-01-03  
**Status**: ✅ **CONFIGURED** (Ready for MailPlus installation)  
**Tag**: @JARVIS @MARVIN @NAS @EMAIL

---

## Company Email Accounts

**Domain**: `homelab.lesnewski.local`

### Accounts to Create

1. **mlesn@homelab.lesnewski.local**
   - Username: `mlesn`
   - Windows Account: `mlesn`
   - Full Name: `mlesn`
   - Quota: 5GB
   - Type: Primary company email account

2. **glesn@homelab.lesnewski.local**
   - Username: `glesn`
   - Windows Account: `glesn`
   - Full Name: `glesn`
   - Quota: 5GB
   - Type: Company email account

---

## Setup Steps

### Step 1: Install MailPlus (via DSM)

1. Open DSM: `https://10.17.17.32:5001`
2. Go to **Package Center**
3. Search for **"MailPlus Server"**
4. Click **Install**
5. Wait for installation to complete
6. Click **Open** to launch MailPlus Server

### Step 2: Configure Domain

1. Open **MailPlus Server** in DSM
2. Go to **Domain** → **Add Domain**
3. Enter domain: `homelab.lesnewski.local`
4. Configure DNS records (if using external domain)
5. Save domain configuration

### Step 3: Create Email Accounts

**Option A: Via DSM MailPlus Interface (Recommended)**

1. Open **MailPlus Server** → **Domain** → `homelab.lesnewski.local`
2. Click **Add Mailbox**
3. Create account for **mlesn**:
   - Email: `mlesn@homelab.lesnewski.local`
   - Username: `mlesn`
   - Full Name: `mlesn`
   - Password: (store in Azure Key Vault first)
   - Quota: 5000 MB
4. Create account for **glesn**:
   - Email: `glesn@homelab.lesnewski.local`
   - Username: `glesn`
   - Full Name: `glesn`
   - Password: (store in Azure Key Vault first)
   - Quota: 5000 MB

**Option B: Store Passwords First, Then Create**

```powershell
# Store passwords in Azure Key Vault
python scripts\python\create_mailplus_accounts.py --store-passwords

# Then create accounts via DSM MailPlus interface
# Use passwords from Azure Key Vault
```

### Step 4: Store Account Passwords

**CRITICAL: +++++ MEMORY PRIORITY - Store in Azure Key Vault**

```powershell
python scripts\python\create_mailplus_accounts.py --store-passwords
```

This will prompt you to enter passwords for:
- `mlesn@homelab.lesnewski.local`
- `glesn@homelab.lesnewski.local`

Passwords will be stored in Azure Key Vault as:
- `mailplus-mlesn-password`
- `mailplus-glesn-password`

---

## Email Account Configuration

### MailPlus Server Settings

- **Domain**: `homelab.lesnewski.local`
- **Server**: `10.17.17.32`
- **Webmail**: `https://10.17.17.32:5001/mailplus`
- **IMAP**: `10.17.17.32:993` (SSL)
- **SMTP**: `10.17.17.32:587` (TLS)

### Account Access

**Webmail:**
- URL: `https://10.17.17.32:5001/mailplus`
- Login with: `mlesn@homelab.lesnewski.local` or `glesn@homelab.lesnewski.local`

**Email Clients (Outlook, Thunderbird, etc.):**
- IMAP Server: `10.17.17.32`
- IMAP Port: `993`
- IMAP Security: SSL/TLS
- SMTP Server: `10.17.17.32`
- SMTP Port: `587`
- SMTP Security: STARTTLS
- Username: Full email address (e.g., `mlesn@homelab.lesnewski.local`)
- Password: (from Azure Key Vault)

**Mobile Apps:**
- Use MailPlus mobile apps (iOS/Android)
- Or configure IMAP in native mail apps
- Server: `10.17.17.32`
- Ports: IMAP 993, SMTP 587

---

## Integration with Email Aggregation

Your company email accounts will be included in the email aggregation system:

1. **n8n Workflows** will check MailPlus IMAP for new emails
2. **SYPHON** will extract intelligence from company emails
3. **All emails** from external providers (Google, Proton, etc.) can be forwarded to company accounts
4. **Unified email hub** for all communications

---

## Account Management

### Password Management

**CRITICAL: +++++ MEMORY PRIORITY**

All passwords stored in:
- ✅ **Azure Key Vault** (primary)
- ✅ **ProtonPass** (synced from Azure Vault)
- ❌ **NEVER** in plain text

**Retrieve passwords:**
```powershell
python scripts\python\unified_secret_manager.py --get mailplus-mlesn-password
python scripts\python\unified_secret_manager.py --get mailplus-glesn-password
```

### Account Quotas

- **Default**: 5GB per account
- **Total Available**: 5 free MailPlus licenses (using 2, 3 remaining)
- **Can increase** quota if needed (limited by NAS storage)

### Account Features

With MailPlus, each account gets:
- ✅ Webmail interface
- ✅ Mobile apps (iOS/Android)
- ✅ Calendar integration
- ✅ Contact management
- ✅ Email filtering
- ✅ Anti-spam/Anti-virus
- ✅ Email archiving

---

## Next Steps

1. ✅ **Install MailPlus** via DSM Package Center
2. ✅ **Configure domain** `homelab.lesnewski.local`
3. ✅ **Store passwords** in Azure Key Vault
4. ✅ **Create accounts** `mlesn` and `glesn` in MailPlus
5. ✅ **Test email** send/receive
6. ✅ **Configure email clients** (Outlook, mobile apps)
7. ✅ **Integrate with n8n** workflows for aggregation

---

## Configuration Files

- **Email Accounts Config**: `config/email_accounts_aggregation.json`
- **MailPlus Accounts**: `config/mailplus_accounts.json` (created after account creation)
- **Account Creation Results**: `data/mailplus_accounts_creation_results.json`

---

## Summary

✅ **Company Email Accounts Configured**
- Domain: `homelab.lesnewski.local`
- Accounts: `mlesn`, `glesn`
- Windows Accounts: `mlesn`, `glesn`
- Quota: 5GB each
- Free Licenses: 2 used, 3 remaining

**Ready for MailPlus installation and account creation!**

---

**Last Updated**: 2026-01-03  
**Maintained By**: @JARVIS @MARVIN
