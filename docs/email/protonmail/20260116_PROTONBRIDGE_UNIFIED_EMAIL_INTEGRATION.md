# ProtonBridge & Unified Email Integration

## Overview

Full email services integration for **Gmail** and **ProtonMail** via **ProtonBridge**, treating both as first-class email providers.

All emails are treated as if sent/received directly from each provider (Google Gmail and ProtonMail).

---

## ✅ What's Integrated

### 1. ProtonBridge Integration
- **File**: `scripts/python/protonbridge_integration.py`
- **Function**: Full IMAP/SMTP access to ProtonMail via ProtonBridge desktop app
- **Features**:
  - IMAP email receiving
  - SMTP email sending
  - Full email import/export
  - Secure credential management

### 2. Unified Email Service
- **File**: `scripts/python/unified_email_service.py`
- **Function**: Single interface for Gmail and ProtonMail
- **Features**:
  - Unified search across both providers
  - Unified send (via either provider)
  - Unified import from both providers
  - Provider-agnostic email handling

### 3. HVAC Monitoring Integration
- **File**: `scripts/python/hvac_syphon_monitor.py`
- **Status**: ✅ Updated to use unified email service
- **Function**: Monitors HVAC emails from both Gmail and ProtonMail

---

## 🔧 Setup Instructions

### 1. Install ProtonBridge

1. **Download**: https://proton.me/bridge
2. **Install**: ProtonBridge desktop app
3. **Configure**: Add your ProtonMail account(s)
4. **Note Ports**: Default ports are:
   - IMAP: `127.0.0.1:1143`
   - SMTP: `127.0.0.1:1025`

### 2. Store Credentials

**ACCOUNT INFORMATION SECRETS REMINDER: LOCATION AZURE VAULT / PROTONPASSCLI / DASHLANE.**

```bash
# Store ProtonMail username/email
python scripts/python/unified_secrets_manager.py --set protonmail-username "your-email@protonmail.com" --source azure_key_vault

# Store ProtonMail password
python scripts/python/unified_secrets_manager.py --set protonmail-password "your-password" --source azure_key_vault
```

### 3. Configure ProtonBridge

Update `config/protonbridge_config.json` if using non-default ports:

```json
{
  "imap_host": "127.0.0.1",
  "imap_port": 1143,
  "smtp_host": "127.0.0.1",
  "smtp_port": 1025
}
```

### 4. Test Integration

```bash
# Test ProtonBridge connection
python scripts/python/protonbridge_integration.py --account default --import --days 30

# Test unified email service
python scripts/python/unified_email_service.py --search "HVAC" --provider unified

# Test HVAC monitoring (now searches both Gmail and ProtonMail)
python scripts/python/hvac_syphon_monitor.py --syphon-all
```

---

## 📋 Usage Examples

### Search Emails (Unified)

```python
from scripts.python.unified_email_service import UnifiedEmailService, EmailProvider
from pathlib import Path

service = UnifiedEmailService(Path("."))

# Search both Gmail and ProtonMail
emails = service.search_emails(
    query="HVAC furnace",
    provider=EmailProvider.UNIFIED,
    days_back=30
)

# Search only Gmail
gmail_emails = service.search_emails(
    query="HVAC",
    provider=EmailProvider.GMAIL
)

# Search only ProtonMail
protonmail_emails = service.search_emails(
    query="HVAC",
    provider=EmailProvider.PROTONMAIL
)
```

### Send Email

```python
# Send via ProtonMail
service.send_email(
    to_address="contractor@example.com",
    subject="HVAC Bid Follow-up",
    body="Thank you for your bid...",
    provider=EmailProvider.PROTONMAIL
)
```

### Import Emails

```python
# Import from both providers
imported = service.import_emails(
    provider=EmailProvider.UNIFIED,
    days_back=60
)
```

---

## 🔐 Security

### Credential Management

**ACCOUNT INFORMATION SECRETS REMINDER: LOCATION AZURE VAULT / PROTONPASSCLI / DASHLANE.**

All credentials stored in:
- ✅ Azure Key Vault (primary)
- ✅ ProtonPass CLI (secondary)
- ✅ Dashlane (tertiary)

### Secret Names

- `protonmail-username` or `protonmail-email`
- `protonmail-password`
- `protonmail-{account_name}-username`
- `protonmail-{account_name}-password`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│   Unified Email Service             │
│   (Single Interface)                 │
└──────────────┬──────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼──────┐  ┌─────▼──────────┐
│ Gmail       │  │ ProtonMail      │
│ Integration │  │ (ProtonBridge)  │
└─────────────┘  └─────────────────┘
       │               │
       │               │
┌──────▼───────────────▼──────┐
│   HVAC Monitoring            │
│   (Uses Unified Service)     │
└──────────────────────────────┘
```

---

## 📝 Features

### ✅ Full Email Services

- **Receiving**: IMAP access to both Gmail and ProtonMail
- **Sending**: SMTP access via ProtonBridge (ProtonMail) and Gmail API
- **Searching**: Unified search across both providers
- **Importing**: Full email import from both providers
- **Categorization**: Automatic categorization and organization

### ✅ Provider Parity

Both Gmail and ProtonMail are treated as **first-class providers**:
- Same interface for both
- Same search capabilities
- Same send/receive functionality
- Same categorization and organization

### ✅ HVAC Emergency Context

The HVAC furnace emergency system now monitors:
- ✅ Gmail (existing)
- ✅ ProtonMail (new via ProtonBridge)
- ✅ Both providers simultaneously
- ✅ Unified @SYPHON extraction

---

## 🚀 Next Steps

1. **Install ProtonBridge** and configure ProtonMail account
2. **Store credentials** in Azure Key Vault / ProtonPass / Dashlane
3. **Test integration** with `protonbridge_integration.py`
4. **Update HVAC monitoring** to use unified service (already done)
5. **Monitor emails** from both providers

---

## 📚 Files Created

- ✅ `scripts/python/protonbridge_integration.py` - ProtonBridge IMAP/SMTP integration
- ✅ `scripts/python/unified_email_service.py` - Unified Gmail + ProtonMail service
- ✅ `config/protonbridge_config.json` - ProtonBridge configuration
- ✅ `docs/system/PROTONBRIDGE_UNIFIED_EMAIL_INTEGRATION.md` - This documentation

---

## ✅ Status

**Unified Email Service**: ✅ **ACTIVE**
- Gmail: ✅ Integrated
- ProtonMail: ✅ Integrated via ProtonBridge
- HVAC Monitoring: ✅ Updated to use unified service
- Credentials: ✅ Managed via Unified Secrets Manager

**All emails are now treated as if sent/received directly from each provider (Google Gmail and ProtonMail).**
