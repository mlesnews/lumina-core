# MailStation Configuration - Verified and Updated

**Date**: 2026-01-15  
**Status**: ✅ Configuration Verified and Updated

---

## 📊 Actual Configuration Verified

### Mail Server Package
- **Package**: MailStation (not MailPlus)
- **Status**: Installed and Running
- **NAS IP**: 10.17.17.32
- **Web Portal**: https://10.17.17.32:5001

### Port Configuration

#### SMTP (Outgoing Mail)
- **Server**: 10.17.17.32
- **Port**: 25
- **Encryption**: STARTTLS
- **Secure**: No (upgrades to TLS)
- **Note**: Port 587 and 465 are closed - using standard port 25

#### IMAP (Incoming Mail)
- **Server**: 10.17.17.32
- **Port**: 993
- **Encryption**: SSL/TLS
- **Secure**: Yes
- **Note**: Port 143 is closed - using secure port 993

### Domain Configuration
- **Primary Domain**: homelab.lesnewski.local
- **Accounts**:
  - mlesn@homelab.lesnewski.local
  - glesn@homelab.lesnewski.local

---

## ✅ Configuration Files Updated

### 1. Email Accounts Configuration
**File**: `config/email_accounts_aggregation.json`

**Updates**:
- Added `mailstation` section with verified configuration
- Updated `company` section to reference MailStation
- Confirmed domain: `homelab.lesnewski.local`
- Updated SMTP port: 25 (was 587)
- Confirmed IMAP port: 993

### 2. Outlook Configuration
**File**: `config/outlook/mailstation_outlook_config.json`

**Updates**:
- Created MailStation-specific Outlook configuration
- Updated SMTP settings: Port 25 (STARTTLS)
- Confirmed IMAP settings: Port 993 (SSL/TLS)
- Added step-by-step setup instructions

### 3. N8N Configuration
**File**: `config/n8n/nas_dsm_email_hub_expansion.json`

**Updates**:
- Changed package reference from "Mail Server" to "MailStation"
- Updated SMTP port: 25 (was 25, but config was generic)
- Updated IMAP port: 993 (was 143, now secure)
- Updated domain references

---

## 📋 Outlook Setup Instructions (Updated)

### Outlook Desktop Configuration

**Account Settings**:
```
Account Type: IMAP
Email Address: mlesn@homelab.lesnewski.local
Display Name: Company Email (MailStation)

Incoming Mail Server (IMAP):
  Server: 10.17.17.32
  Port: 993
  Encryption: SSL/TLS
  Username: mlesn@homelab.lesnewski.local

Outgoing Mail Server (SMTP):
  Server: 10.17.17.32
  Port: 25
  Encryption: STARTTLS
  Username: mlesn@homelab.lesnewski.local
  Requires Authentication: Yes
```

**Steps**:
1. Open Outlook Desktop
2. File → Account Settings → Account Settings
3. New → Manual setup → POP or IMAP
4. Enter email: `mlesn@homelab.lesnewski.local`
5. Account Type: IMAP
6. Incoming: `10.17.17.32`, Port `993`, SSL/TLS
7. Outgoing: `10.17.17.32`, Port `25`, STARTTLS
8. More Settings → Outgoing Server: Require authentication
9. Test connection

### Outlook Mobile Configuration

**Account Settings**:
```
Email: mlesn@homelab.lesnewski.local
IMAP Server: 10.17.17.32
IMAP Port: 993 (SSL/TLS)
SMTP Server: 10.17.17.32
SMTP Port: 25 (STARTTLS)
```

**Steps**:
1. Open Outlook Mobile App
2. Add Account → Advanced Setup → IMAP
3. Enter email and password
4. IMAP: `10.17.17.32:993` (SSL/TLS)
5. SMTP: `10.17.17.32:25` (STARTTLS)
6. Configure sync settings

---

## 🔍 Port Status Summary

| Port | Service | Status | Encryption |
|------|---------|--------|------------|
| 25 | SMTP | ✅ Open | STARTTLS |
| 587 | SMTP (Alt) | ❌ Closed | - |
| 465 | SMTP (SSL) | ❌ Closed | - |
| 993 | IMAP (SSL) | ✅ Open | SSL/TLS |
| 143 | IMAP (Standard) | ❌ Closed | - |
| 110 | POP3 | ❌ Closed | - |
| 995 | POP3 (SSL) | ❌ Closed | - |

**Note**: MailStation is configured with:
- SMTP on port 25 (standard, with STARTTLS)
- IMAP on port 993 (secure SSL/TLS)

---

## ⚠️ Important Notes

### SMTP Port 25
- **Standard port** for SMTP
- Uses **STARTTLS** for encryption (upgrades connection)
- Some ISPs block port 25 - if sending fails, may need to:
  - Use ISP's SMTP relay
  - Configure port forwarding
  - Use alternative port (if MailStation supports it)

### IMAP Port 993
- **Secure port** for IMAP
- Uses **SSL/TLS** encryption
- Recommended for all email clients

### MailStation vs MailPlus
- **MailStation**: Basic mail server (currently installed)
- **MailPlus**: Advanced features (webmail, calendar, mobile apps)
- Current setup uses MailStation
- If upgrading to MailPlus, ports may change

---

## 🔄 Next Steps

### For Gmail Integration
1. **Check if External Mail is configured** in MailStation
2. **Add Gmail account** via External Mail settings (if available)
3. **Use OAuth2** for Gmail authentication
4. **Alternative**: Configure Gmail to forward to MailStation

### For ProtonMail Integration
1. **Proton Bridge** must be running on host PC
2. **N8N can bridge** connection (see N8N config)
3. **Alternative**: Install Bridge on NAS (if supported)

### For Outlook Configuration
1. **Use updated settings** from `config/outlook/mailstation_outlook_config.json`
2. **Test connection** with verified ports
3. **Verify sending/receiving** works correctly

---

## 📄 Reference Files

- **Email Accounts**: `config/email_accounts_aggregation.json`
- **Outlook Config**: `config/outlook/mailstation_outlook_config.json`
- **N8N Config**: `config/n8n/nas_dsm_email_hub_expansion.json`
- **Verification Results**: `data/mailstation_config_verification.json`

---

## ✅ Verification Complete

All configuration files have been updated to match the actual MailStation setup:
- ✅ Ports verified (25/993)
- ✅ Domain confirmed (homelab.lesnewski.local)
- ✅ Accounts listed (mlesn, glesn)
- ✅ Outlook configs updated
- ✅ N8N configs updated

**Configuration is now accurate and ready for use!** 🚀
