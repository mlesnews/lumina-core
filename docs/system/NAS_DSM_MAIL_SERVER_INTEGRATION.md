# NAS DSM Mail Server Integration with SYPHON

**Date**: 2025-12-28  
**Status**: Operational  
**Location**: `scripts/python/syphon_nas_dsm_mail_integration.py`

## Overview

The NAS DSM Mail Server acts as our custom email aggregation system for corporate email accounts. We have complete control over all email accounts and how we choose to handle them, including:

- **Secure email**: ProtonMail with Proton Bridge
- **Unsecure email providers**: Google, Apple, etc.

All emails are aggregated through the NAS DSM mail server, providing centralized management and integration with SYPHON for intelligence extraction.

## Architecture

### Email Infrastructure

```
┌─────────────────────────────────────────────────────────┐
│              NAS DSM Mail Server                        │
│              (10.17.17.32)                              │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Email Aggregation Layer                         │  │
│  │  - IMAP Server (Port 993)                        │  │
│  │  - SMTP Server (Port 587)                        │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Secure      │  │  Unsecure    │  │  Corporate   │ │
│  │  Accounts    │  │  Accounts    │  │  Accounts    │ │
│  │              │  │              │  │              │ │
│  │  ProtonMail  │  │  Google      │  │  Company     │ │
│  │  (Bridge)    │  │  Apple       │  │  Domains     │ │
│  │              │  │  etc.        │  │              │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────┘
                        │
                        │ IMAP/SMTP
                        ▼
┌─────────────────────────────────────────────────────────┐
│           SYPHON Email Extraction                       │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  EmailExtractor                                  │  │
│  │  - Actionable items extraction                   │  │
│  │  - Task extraction                               │  │
│  │  - Decision extraction                           │  │
│  │  - Intelligence extraction                       │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Account Types

#### Secure Accounts
- **ProtonMail with Proton Bridge**
- End-to-end encryption
- Aggregated through NAS DSM
- Complete privacy and security

#### Unsecure Accounts
- **Google (Gmail)**
- **Apple (iCloud)**
- Other standard email providers
- Aggregated through NAS DSM for centralized management

## Features

### Complete Control
- All email accounts managed through NAS DSM
- Centralized configuration
- Unified IMAP/SMTP access
- Complete control over email handling

### SYPHON Integration
- Automated email extraction
- Intelligence extraction from all email sources
- Task and decision identification
- Actionable items extraction

### Account Management
- Register secure and unsecure accounts
- Enable/disable accounts
- Account-specific configuration
- Statistics and reporting

## Usage

### Register Email Account

```python
from syphon_nas_dsm_mail_integration import NASDSMMailServerIntegration

integration = NASDSMMailServerIntegration(project_root)

# Register secure account (ProtonMail via Bridge)
integration.register_account(
    account_id="protonmail_main",
    account_name="ProtonMail Main Account",
    email_address="user@protonmail.com",
    account_type="secure",
    nas_dsm_aggregated=True
)

# Register unsecure account (Google)
integration.register_account(
    account_id="gmail_personal",
    account_name="Gmail Personal",
    email_address="user@gmail.com",
    account_type="unsecure",
    nas_dsm_aggregated=True
)
```

### Syphon Emails

```python
# Syphon emails from all accounts
results = integration.syphon_emails(limit=50)

# Syphon emails from specific account
results = integration.syphon_emails(account_id="protonmail_main", limit=100)
```

### Command Line

```bash
# Register account
python scripts/python/syphon_nas_dsm_mail_integration.py \
    --register-account protonmail_main "ProtonMail Main" user@protonmail.com secure 10.17.17.32

# Syphon emails
python scripts/python/syphon_nas_dsm_mail_integration.py --syphon --limit 50

# Show infrastructure summary
python scripts/python/syphon_nas_dsm_mail_integration.py --summary
```

## Configuration

Configuration is stored in:
- `data/syphon/nas_dsm_mail/nas_dsm_mail_config.json`

### Configuration Structure

```json
{
  "nas_host": "10.17.17.32",
  "nas_dsm_port": 5000,
  "mail_server_port": 993,
  "mail_smtp_port": 587,
  "aggregation_enabled": true,
  "accounts": [
    {
      "account_id": "protonmail_main",
      "account_name": "ProtonMail Main Account",
      "email_address": "user@protonmail.com",
      "account_type": "secure",
      "imap_server": "10.17.17.32",
      "imap_port": 993,
      "imap_ssl": true,
      "smtp_server": "10.17.17.32",
      "smtp_port": 587,
      "smtp_ssl": true,
      "nas_dsm_aggregated": true,
      "enabled": true
    }
  ]
}
```

## Statistics

Statistics are tracked and stored in:
- `data/syphon/nas_dsm_mail/stats.json`

### Stats Tracked

- Total emails processed
- Secure emails count
- Unsecure emails count
- Actionable items extracted
- Tasks extracted
- Decisions extracted
- Last sync timestamp

## Security Considerations

### Secure Accounts (ProtonMail)
- End-to-end encryption via Proton Bridge
- Private keys remain on client
- No server-side decryption capability
- Full privacy protection

### Unsecure Accounts
- Standard IMAP/SMTP encryption (TLS/SSL)
- Server-side access possible
- Standard email security practices

### NAS DSM Aggregation
- All accounts aggregated through NAS DSM
- Centralized management
- Unified access control
- Complete control over email handling

## Integration Points

### SYPHON System
- Email extraction via `EmailExtractor`
- Intelligence extraction
- Task and decision identification

### NAS Infrastructure
- NAS DSM mail server
- IMAP/SMTP services
- Account aggregation

### Lumina Systems
- R5 Living Context Matrix (knowledge aggregation)
- Helpdesk (task routing)
- JARVIS (automation)

## Files

- **Integration Script**: `scripts/python/syphon_nas_dsm_mail_integration.py`
- **Configuration**: `data/syphon/nas_dsm_mail/nas_dsm_mail_config.json`
- **Statistics**: `data/syphon/nas_dsm_mail/stats.json`
- **Results**: `data/syphon/nas_dsm_mail/syphon_results_*.json`
- **Documentation**: `docs/system/NAS_DSM_MAIL_SERVER_INTEGRATION.md`

## Related Systems

- SYPHON System (`scripts/python/syphon/`)
- NAS Infrastructure (`scripts/python/nas_*.py`)
- Email Extraction (`scripts/python/syphon/extractors.py`)

