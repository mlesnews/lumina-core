# Email Credentials Setup Guide

## Overview

This guide helps you set up email credentials for Gmail and ProtonMail to enable email searching.

## Quick Setup

### Option 1: Interactive Setup (Recommended)

```bash
python scripts/python/setup_email_credentials_azure_vault.py --interactive
```

Follow the prompts to:
1. Select email provider (Gmail, ProtonMail, etc.)
2. Enter email address
3. Enter password or OAuth token
4. Credentials stored in Azure Key Vault

### Option 2: Command Line Setup

```bash
# Gmail with OAuth2
python scripts/python/setup_email_credentials_azure_vault.py \
  --provider google \
  --email your.email@gmail.com \
  --oauth-token <token>

# Gmail with App Password
python scripts/python/setup_email_credentials_azure_vault.py \
  --provider google \
  --email your.email@gmail.com \
  --password <app-password>

# ProtonMail Bridge
python scripts/python/setup_email_credentials_azure_vault.py \
  --provider proton \
  --email your.email@proton.me \
  --password <bridge-password>
```

## Gmail Setup

### Option A: OAuth2 (Recommended)

1. **Get OAuth2 credentials**:
   - Go to https://console.cloud.google.com/
   - Create OAuth 2.0 credentials
   - Download JSON file

2. **Store credentials**:
   ```bash
   python scripts/python/unified_secrets_manager.py --set gmail-oauth2-credentials "$(cat credentials.json)"
   ```

### Option B: App Password

1. **Enable 2FA** on your Google account
2. **Generate App Password**:
   - Go to https://myaccount.google.com/security
   - App passwords → Generate
3. **Store password**:
   ```bash
   python scripts/python/setup_email_credentials_azure_vault.py \
     --provider google \
     --email your.email@gmail.com \
     --password <app-password>
   ```

## ProtonMail Setup

### Using Proton Bridge

1. **Install Proton Bridge** (if not installed)
2. **Get Bridge Password**:
   - Open Proton Bridge
   - Settings → Advanced → Bridge password
3. **Store credentials**:
   ```bash
   python scripts/python/setup_email_credentials_azure_vault.py \
     --provider proton \
     --email your.email@proton.me \
     --password <bridge-password>
   ```

## Verify Setup

```bash
# Test email search
python scripts/python/search_emails_for_credentials.py --stripe
python scripts/python/search_emails_for_credentials.py --plaid
```

## Secret Names in Azure Key Vault

- **Gmail OAuth2**: `gmail-oauth2-credentials`
- **Gmail Password**: `google-email-password`
- **Gmail Email**: `google-email`
- **ProtonMail Password**: `proton-bridge-password`
- **ProtonMail Email**: `proton-bridge-username`

## Troubleshooting

### "Gmail credentials not found"
- Check Azure Key Vault for `gmail-oauth2-credentials` or `google-email-password`
- Re-run setup if missing

### "ProtonMail credentials not found"
- Check Azure Key Vault for `proton-bridge-password`
- Verify Proton Bridge is running

### "OAuth token expired"
- Re-authenticate and update token in Azure Key Vault

## Security Notes

- ✅ All credentials stored in Azure Key Vault
- ✅ Never stored in plain text
- ✅ OAuth2 preferred over passwords
- ✅ App passwords required for 2FA accounts
