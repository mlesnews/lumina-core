# N8N NAS/DSM Email Hub Integration Setup

**Date**: 2025-01-24  
**Status**: ✅ **CONFIGURED**  
**Tag**: @N8N @NAS @DSM @email #email-hub #integration

---

## Overview

@N8N expansion for integration with custom company email hub on NAS/DSM package configuration.

This expansion provides comprehensive email workflow automation for the NAS/DSM Mail Server package, including:
- Email sending via SMTP
- Email receiving via IMAP
- Email hub management operations
- Health monitoring and alerts

---

## Configuration File

**Location**: `config/n8n/nas_dsm_email_hub_expansion.json`

**Status**: ✅ **CREATED**

---

## NAS/DSM Email Hub Configuration

### Mail Server Package

- **Package**: Mail Server (DSM 7.x)
- **NAS IP**: 10.17.17.32
- **Web Portal**: https://10.17.17.32:5001
- **API Endpoint**: https://10.17.17.32:5001/webapi

### SMTP Configuration

- **Server**: 10.17.17.32
- **Port**: 25
- **TLS**: Enabled
- **Authentication**: Login (credentials from Azure Key Vault)
- **From Address**: noreply@company.local

### IMAP Configuration

- **Server**: 10.17.17.32
- **Port**: 143
- **TLS**: Enabled
- **Authentication**: Login (credentials from Azure Key Vault)
- **Check Interval**: Every 5 minutes

---

## N8N Workflows

### 1. Email Hub Send (`email_hub_send`)

**Purpose**: Send emails via NAS/DSM Email Hub SMTP

**Webhook**: `/email/hub/send`

**Workflow**:
1. Receive email request via webhook
2. Validate email format and recipients
3. Get SMTP credentials from Azure Key Vault
4. Send email via NAS/DSM Email Hub SMTP
5. Log email status
6. Notify JARVIS

**Usage**:
```bash
curl -X POST http://10.17.17.32:5678/webhook/email/hub/send \
  -H "Content-Type: application/json" \
  -d '{
    "to": "recipient@example.com",
    "subject": "Test Email",
    "text": "Email body",
    "from": "noreply@company.local"
  }'
```

---

### 2. Email Hub Receive (`email_hub_receive`)

**Purpose**: Receive and process emails from NAS/DSM Email Hub

**Trigger**: Scheduled (every 5 minutes)

**Workflow**:
1. Check for new emails via IMAP
2. Process new emails
3. Extract intelligence via @SYPHON
4. Route to appropriate systems (JARVIS, MARVIN)
5. Save to email archive

**Integration**:
- @SYPHON: Extract actionable intelligence
- JARVIS: Route important emails
- Email Archive: Store on NAS

---

### 3. Email Hub Management (`email_hub_management`)

**Purpose**: Manage email hub operations via DSM API

**Webhook**: `/email/hub/management`

**Operations**:
- Create mailbox
- Delete mailbox
- Update mailbox
- Create alias
- Create distribution list
- Get mailbox list
- Get domain list

**Usage**:
```bash
curl -X POST http://10.17.17.32:5678/webhook/email/hub/management \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "create_mailbox",
    "mailbox": "user@company.local",
    "password": "secure_password"
  }'
```

---

### 4. Email Hub Monitoring (`email_hub_monitoring`)

**Purpose**: Monitor email hub health and status

**Trigger**: Scheduled (every hour)

**Checks**:
- SMTP server status
- IMAP server status
- Mailbox availability
- Disk space
- Queue status

**Alerts**:
- Error rate > 5%
- Queue size > 1000
- Disk space > 80%

---

## Integration Points

### JARVIS Integration

- **Webhook**: `http://localhost:8000/api/jarvis/email`
- **Notifications**: Email received, sent, errors, status changes
- **Purpose**: Route important emails to JARVIS for processing

### @SYPHON Integration

- **Webhook**: `http://localhost:8000/api/syphon/email`
- **Extraction**: Actionable items, tasks, decisions, intelligence
- **Purpose**: Extract actionable intelligence from emails

### MARVIN Integration

- **Webhook**: `http://localhost:8000/api/marvin/verify`
- **Verification**: Email content, security, compliance
- **Purpose**: Verify email content and security

### Azure Key Vault Integration

- **Vault URL**: `https://jarvis-lumina.vault.azure.net/`
- **Secrets**:
  - `nas-email-hub-smtp-username`
  - `nas-email-hub-smtp-password`
  - `nas-email-hub-imap-username`
  - `nas-email-hub-imap-password`
  - `nas-email-hub-api-key`

---

## Security

### Credential Storage

- **All credentials stored in Azure Key Vault**
- **Never hardcoded in workflows**
- **Retrieved dynamically at runtime**

### Access Control

- **API Key Required**: Stored in Azure Key Vault
- **IP Whitelist**: 10.17.17.0/24, 127.0.0.1
- **TLS Required**: All connections use TLS

### Audit Logging

- **All email operations logged**
- **Management operations logged**
- **Health check results logged**

---

## Setup Instructions

### 1. Configure Azure Key Vault Secrets

Store email hub credentials in Azure Key Vault:

```powershell
# SMTP Credentials
az keyvault secret set --vault-name jarvis-lumina --name nas-email-hub-smtp-username --value "smtp_user"
az keyvault secret set --vault-name jarvis-lumina --name nas-email-hub-smtp-password --value "smtp_password"

# IMAP Credentials
az keyvault secret set --vault-name jarvis-lumina --name nas-email-hub-imap-username --value "imap_user"
az keyvault secret set --vault-name jarvis-lumina --name nas-email-hub-imap-password --value "imap_password"

# API Key
az keyvault secret set --vault-name jarvis-lumina --name nas-email-hub-api-key --value "api_key"
```

### 2. Import Workflows to N8N

1. Open N8N at `http://10.17.17.32:5678`
2. Import workflows from `config/n8n/nas_dsm_email_hub_expansion.json`
3. Configure credentials (use Azure Key Vault secrets)
4. Activate workflows

### 3. Configure DSM Mail Server

1. Ensure Mail Server package is installed on NAS
2. Configure SMTP server (port 25, TLS enabled)
3. Configure IMAP server (port 143, TLS enabled)
4. Create mailboxes and domains as needed
5. Test SMTP/IMAP connectivity

### 4. Test Integration

```bash
# Test email send
curl -X POST http://10.17.17.32:5678/webhook/email/hub/send \
  -H "Content-Type: application/json" \
  -d '{"to": "test@company.local", "subject": "Test", "text": "Test email"}'

# Test email receive (check logs)
# Test management (create mailbox)
curl -X POST http://10.17.17.32:5678/webhook/email/hub/management \
  -H "Content-Type: application/json" \
  -d '{"operation": "get_mailbox_list"}'
```

---

## Monitoring

### Health Checks

- **Interval**: Every hour
- **Checks**: SMTP, IMAP, mailboxes, disk space, queue
- **Alerts**: Sent to JARVIS if issues detected

### Metrics

- Emails sent per hour
- Emails received per hour
- Queue size
- Error rate
- Response time

---

## Troubleshooting

### Common Issues

1. **SMTP Connection Failed**
   - Check NAS firewall rules
   - Verify SMTP port (25) is open
   - Check credentials in Azure Key Vault

2. **IMAP Connection Failed**
   - Check NAS firewall rules
   - Verify IMAP port (143) is open
   - Check credentials in Azure Key Vault

3. **Azure Key Vault Access Denied**
   - Verify managed identity or service principal
   - Check Key Vault access policies
   - Verify secret names match configuration

---

## References

- **Expansion Config**: `config/n8n/nas_dsm_email_hub_expansion.json`
- **N8N Config**: `config/n8n/unified_communications_config.json`
- **Workflows**: `config/n8n/workflows.json`
- **NAS Email Config**: `config/nas_email_config.json`
- **Secret Management**: `docs/security/SECRET_MANAGEMENT_POLICY.md`

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **CONFIGURED**  
**Maintained By**: @N8N @JARVIS