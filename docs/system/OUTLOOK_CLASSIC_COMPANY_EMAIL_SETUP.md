# Outlook Classic Company Email Setup

## Overview

Complete setup guide for configuring Outlook Classic with the company email account (`mlesn@homelab.lesnewski.local`).

## Account Configuration

- **Email**: `mlesn@homelab.lesnewski.local`
- **Display Name**: `mlesn`
- **IMAP Server**: `10.17.17.32`
- **IMAP Port**: `993` (SSL/TLS)
- **SMTP Server**: `10.17.17.32`
- **SMTP Port**: `587` (STARTTLS)
- **Username**: `mlesn@homelab.lesnewski.local`
- **Password**: [NAS Mail Hub password]

## Setup Script

The automated setup script is located at:
```
scripts/python/setup_outlook_classic_company_email.py
```

### Usage

```bash
# Automatic setup (will prompt for password if not in Azure Vault)
python scripts/python/setup_outlook_classic_company_email.py

# With password provided
python scripts/python/setup_outlook_classic_company_email.py --password "your-password"
```

## Prerequisites

1. **IMAP Port 993**: Must be enabled on MailStation
   - Access DSM → MailStation → Settings → Mail Service
   - Enable IMAP service
   - Set IMAP port to 993 (SSL/TLS)
   - Ensure firewall allows port 993

2. **SMTP Port 587**: Should already be open (verified)

3. **Credentials**: Password should be stored in Azure Key Vault as one of:
   - `nas-email-password`
   - `mailplus-mlesn-password`
   - `company-email-password`
   - `email-password`
   - `nas-mailplus-password`

## Setup Process

The script automates the following steps:

1. **Start Outlook Classic** (if not running)
2. **Navigate to Account Settings**
   - File → Account Settings → Account Settings
3. **Add New Account**
   - Click "New..." button
   - Select "Manual setup or additional server types"
   - Select "POP or IMAP"
4. **Enter Account Details**
   - Your Name: `mlesn`
   - Email Address: `mlesn@homelab.lesnewski.local`
   - Account Type: `IMAP`
   - Incoming mail server: `10.17.17.32`
   - Outgoing mail server: `10.17.17.32`
   - User Name: `mlesn@homelab.lesnewski.local`
   - Password: [Enter manually if not in vault]
5. **Configure More Settings**
   - **Outgoing Server Tab**:
     - ✅ Check "My outgoing server (SMTP) requires authentication"
     - ✅ Select "Use same settings as my incoming mail server"
   - **Advanced Tab**:
     - IMAP Port: `993`
     - IMAP Encryption: `SSL/TLS`
     - SMTP Port: `587`
     - SMTP Encryption: `STARTTLS`
6. **Test Connection**
   - Click "Next" to test connection
   - Verify connection test passes
7. **Finish Setup**
   - Click "Close" after successful test
   - Click "Finish" to complete

## Verification

After setup, verify the account:

```bash
python scripts/python/outlook_account_verifier.py
```

The account should appear in the list with:
- Display Name: `mlesn`
- SMTP Address: `mlesn@homelab.lesnewski.local`

## Troubleshooting

### Account Not Appearing

1. **Check IMAP Port 993**:
   ```bash
   python -c "import socket; sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.settimeout(3); result = sock.connect_ex(('10.17.17.32', 993)); sock.close(); print('OPEN' if result == 0 else 'CLOSED')"
   ```

2. **Enable IMAP on MailStation**:
   - Access DSM → MailStation → Settings → Mail Service
   - Enable IMAP service
   - Set port to 993 (SSL/TLS)

3. **Check Connection Test**:
   - If connection test failed, verify:
     - IMAP port 993 is open
     - Password is correct
     - Server address is correct (10.17.17.32)

4. **Restart Outlook**:
   - Close and reopen Outlook Classic
   - Check Account Settings again

### Connection Test Failed

- **IMAP Port Closed**: Enable IMAP port 993 on MailStation
- **Wrong Password**: Verify password in Azure Vault or re-enter
- **Server Unreachable**: Verify network connectivity to 10.17.17.32

### Password Not in Vault

Store the password in Azure Key Vault:

```bash
# Using Azure CLI (if available)
az keyvault secret set --vault-name jarvis-lumina --name nas-email-password --value "your-password"
```

Or use the credential management scripts to store it securely.

## Manual Setup Alternative

If automated setup fails, manually configure:

1. Open Outlook Classic
2. File → Account Settings → Account Settings
3. Click "New..."
4. Follow the account configuration above
5. Enter all details manually
6. Configure More Settings as specified
7. Test connection and finish

## Related Files

- `scripts/python/setup_outlook_classic_company_email.py` - Automated setup script
- `scripts/python/outlook_account_verifier.py` - Account verification
- `scripts/python/manus_outlook_account_setup.py` - General Outlook automation
- `config/outlook/mailstation_outlook_config.json` - Configuration file

## Tags

`#OUTLOOK` `#CLASSIC` `#COMPANY_EMAIL` `#MAILSTATION` `#AUTOMATION` `@JARVIS` `@LUMINA` `@MANUS`
