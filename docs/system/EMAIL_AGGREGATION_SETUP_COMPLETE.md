# Email Aggregation Setup - Complete Guide

**Date**: 2026-01-03  
**Status**: ✅ **READY TO DEPLOY**  
**Tag**: @JARVIS @MARVIN @NAS @EMAIL @N8N

---

## Overview

Complete email aggregation system that pulls emails from all your accounts:
- ✅ Google/Gmail
- ✅ Proton Family Suite (via Proton Bridge on host PC)
- ✅ Xfinity
- ✅ Apple/.me (iCloud)
- ✅ Yahoo
- ✅ Outlook/Microsoft 365
- ✅ Others

All emails are:
- Aggregated via n8n workflows
- Processed by SYPHON for intelligence extraction
- Stored in NAS MailPlus
- Accessible through unified interface

---

## Setup Steps

### Step 1: Install MailPlus

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts\python\setup_mailplus_email_hub.py
```

This will:
- ✅ Install MailPlus on NAS (if not already installed)
- ✅ Create email accounts configuration
- ✅ Generate n8n workflows for all providers
- ✅ Configure Proton Bridge integration

### Step 2: Store Email Credentials

**CRITICAL: +++++ MEMORY PRIORITY - All credentials in Azure Key Vault**

```powershell
# Interactive setup (recommended)
python scripts\python\setup_email_credentials_azure_vault.py --interactive

# Or setup specific providers
python scripts\python\setup_email_credentials_azure_vault.py --provider google --email user@gmail.com
python scripts\python\setup_email_credentials_azure_vault.py --provider proton --email user@proton.me
python scripts\python\setup_email_credentials_azure_vault.py --provider xfinity --email user@comcast.net
python scripts\python\setup_email_credentials_azure_vault.py --provider apple --email user@me.com
python scripts\python\setup_email_credentials_azure_vault.py --provider yahoo --email user@yahoo.com
python scripts\python\setup_email_credentials_azure_vault.py --provider outlook --email user@outlook.com
```

### Step 3: Install & Configure Proton Bridge

**Proton Bridge must run on host PC:**

1. Download Proton Bridge: https://proton.me/mail/bridge
2. Install and sign in with Proton Family account
3. Enable IMAP/SMTP in Bridge settings
4. Note ports:
   - IMAP: 1143 (default)
   - SMTP: 1025 (default)
5. Keep Bridge running (it must be active for n8n to connect)

### Step 4: Import n8n Workflows

1. Open n8n interface
2. Import workflows from: `config/n8n/email_aggregation_workflows.json`
3. Configure credentials for each workflow:
   - Google: OAuth2 or App Password
   - Proton: Bridge credentials (from Azure Vault)
   - Xfinity: Email/password (from Azure Vault)
   - Apple: App-Specific Password (from Azure Vault)
   - Yahoo: OAuth2 or App Password (from Azure Vault)
   - Outlook: OAuth2 or App Password (from Azure Vault)

### Step 5: Activate Workflows

Enable all email aggregation workflows in n8n:
- ✅ Email Aggregation - Google/Gmail
- ✅ Email Aggregation - ProtonMail (Bridge)
- ✅ Email Aggregation - Xfinity
- ✅ Email Aggregation - Apple/iCloud
- ✅ Email Aggregation - Yahoo
- ✅ Email Aggregation - Outlook/Microsoft 365
- ✅ Email Aggregation - Unified Processing

---

## Email Provider Configuration

### Google/Gmail

**Method 1: OAuth2 (Recommended)**
1. Create OAuth2 credentials in Google Cloud Console
2. Store OAuth token in Azure Key Vault
3. n8n workflow uses OAuth token

**Method 2: App Password**
1. Enable 2FA on Google account
2. Generate App Password: myaccount.google.com → Security → App passwords
3. Store App Password in Azure Key Vault
4. n8n workflow uses App Password

**IMAP Settings:**
- Server: `imap.gmail.com`
- Port: `993`
- SSL: Yes
- Auth: OAuth2 or App Password

**SMTP Settings:**
- Server: `smtp.gmail.com`
- Port: `587`
- SSL: Yes
- Auth: OAuth2 or App Password

### ProtonMail (via Bridge)

**Setup:**
1. Install Proton Bridge on host PC
2. Sign in with Proton Family account
3. Enable IMAP/SMTP in Bridge
4. Store Bridge credentials in Azure Key Vault

**IMAP Settings:**
- Server: `127.0.0.1` (localhost - Bridge on host PC)
- Port: `1143` (default)
- SSL: No (Bridge handles encryption)
- Auth: Bridge password

**SMTP Settings:**
- Server: `127.0.0.1` (localhost - Bridge on host PC)
- Port: `1025` (default)
- SSL: No (Bridge handles encryption)
- Auth: Bridge password

**Note:** n8n must run on host PC or have network access to host PC

### Xfinity

**IMAP Settings:**
- Server: `imap.comcast.net`
- Port: `993`
- SSL: Yes
- Auth: Email/password

**SMTP Settings:**
- Server: `smtp.comcast.net`
- Port: `587`
- SSL: Yes
- Auth: Email/password

### Apple/iCloud

**IMAP Settings:**
- Server: `imap.mail.me.com`
- Port: `993`
- SSL: Yes
- Auth: **App-Specific Password** (required)

**SMTP Settings:**
- Server: `smtp.mail.me.com`
- Port: `587`
- SSL: Yes
- Auth: **App-Specific Password** (required)

**App-Specific Password:**
1. Go to appleid.apple.com
2. Sign in with Apple ID
3. Generate App-Specific Password
4. Use that password (NOT your Apple ID password)

### Yahoo

**Method 1: OAuth2 (Recommended)**
- Requires OAuth2 setup
- Store OAuth token in Azure Key Vault

**Method 2: App Password**
1. Enable 2FA on Yahoo account
2. Generate App Password
3. Store App Password in Azure Key Vault

**IMAP Settings:**
- Server: `imap.mail.yahoo.com`
- Port: `993`
- SSL: Yes
- Auth: OAuth2 or App Password

**SMTP Settings:**
- Server: `smtp.mail.yahoo.com`
- Port: `587`
- SSL: Yes
- Auth: OAuth2 or App Password

### Outlook/Microsoft 365

**Method 1: OAuth2 (Recommended)**
- Requires OAuth2 setup in Azure AD
- Store OAuth token in Azure Key Vault

**Method 2: App Password**
1. Enable 2FA on Microsoft account
2. Generate App Password
3. Store App Password in Azure Key Vault

**IMAP Settings:**
- Server: `outlook.office365.com`
- Port: `993`
- SSL: Yes
- Auth: OAuth2 or App Password

**SMTP Settings:**
- Server: `smtp.office365.com`
- Port: `587`
- SSL: Yes
- Auth: OAuth2 or App Password

---

## n8n Workflow Architecture

### Individual Provider Workflows

Each email provider has its own workflow:
- Runs every 5 minutes
- Fetches new emails via IMAP
- Sends to SYPHON for intelligence extraction
- Stores in NAS MailPlus archive

### Unified Processing Workflow

Master workflow that:
- Aggregates all email sources
- Processes through SYPHON
- Stores in unified archive
- Notifies JARVIS of important emails

---

## SYPHON Integration

All emails are automatically processed by SYPHON:
- ✅ Actionable items extraction
- ✅ Task identification
- ✅ Decision points
- ✅ Intelligence gathering
- ✅ Cross-platform correlation

SYPHON webhook: `http://localhost:8000/api/syphon/email`

---

## Security & Credentials

**CRITICAL: +++++ MEMORY PRIORITY**

All credentials stored in:
- ✅ **Azure Key Vault** (primary)
- ✅ **ProtonPass** (synced from Azure Vault)
- ❌ **NEVER** in plain text files
- ❌ **NEVER** in code/config files

**Credential Storage:**
- `google-email`, `google-email-password`, `google-oauth-token`
- `proton-bridge-username`, `proton-bridge-password`
- `xfinity-email`, `xfinity-email-password`
- `apple-email`, `apple-email-password`
- `yahoo-email`, `yahoo-email-password`, `yahoo-oauth-token`
- `outlook-email`, `outlook-email-password`, `outlook-oauth-token`

---

## Testing

### Test Individual Workflows

1. Open n8n
2. Select workflow (e.g., "Email Aggregation - Google/Gmail")
3. Click "Execute Workflow"
4. Check logs for errors
5. Verify emails are fetched
6. Check SYPHON extraction

### Test Unified Workflow

1. Trigger unified workflow: `POST /email/aggregate/all`
2. Check all providers are processed
3. Verify SYPHON extraction
4. Check NAS MailPlus archive

### Verify Credentials

```powershell
# Check if credentials are stored
python scripts\python\unified_secret_manager.py --list

# Test credential retrieval
python scripts\python\unified_secret_manager.py --get google-email
```

---

## Troubleshooting

### Proton Bridge Not Connecting

**Issue:** n8n can't connect to Proton Bridge

**Solutions:**
1. Verify Bridge is running on host PC
2. Check Bridge ports (default: IMAP 1143, SMTP 1025)
3. Ensure n8n has network access to host PC
4. Check Bridge credentials in Azure Vault

### OAuth2 Not Working

**Issue:** Google/Yahoo/Outlook OAuth2 fails

**Solutions:**
1. Verify OAuth2 credentials are correct
2. Check token expiration (refresh if needed)
3. Use App Password as fallback
4. Verify OAuth scopes are correct

### Apple App-Specific Password

**Issue:** Apple/iCloud authentication fails

**Solutions:**
1. Must use App-Specific Password (NOT Apple ID password)
2. Generate new App-Specific Password at appleid.apple.com
3. Store in Azure Key Vault
4. Update n8n workflow credentials

### Emails Not Being Fetched

**Issue:** Workflows run but no emails fetched

**Solutions:**
1. Check IMAP credentials in Azure Vault
2. Verify IMAP server/port settings
3. Check firewall/network access
4. Review n8n workflow logs
5. Test IMAP connection manually

---

## Summary

✅ **Complete Email Aggregation System**
- All email providers configured
- n8n workflows ready
- SYPHON integration active
- Azure Key Vault for credentials
- NAS MailPlus for storage

**Next Steps:**
1. Run setup script: `python scripts\python\setup_mailplus_email_hub.py`
2. Store credentials: `python scripts\python\setup_email_credentials_azure_vault.py --interactive`
3. Install Proton Bridge on host PC
4. Import n8n workflows
5. Activate workflows
6. Test email aggregation

---

**Last Updated**: 2026-01-03  
**Maintained By**: @JARVIS @MARVIN
