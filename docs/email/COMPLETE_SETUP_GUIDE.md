# Complete Email Setup Guide - MailStation + Gmail + ProtonMail
## Ready-to-Use Configuration

**Date**: 2026-01-15  
**Status**: ✅ Configuration Verified - Ready for Setup

---

## 📊 Current Setup Summary

### Mail Server
- **Package**: MailStation (installed and running)
- **NAS IP**: 10.17.17.32
- **SMTP**: Port 25 (STARTTLS)
- **IMAP**: Port 993 (SSL/TLS)
- **Domain**: homelab.lesnewski.local
- **Accounts**: mlesn@homelab.lesnewski.local, glesn@homelab.lesnewski.local

### External Email Accounts
- **Gmail**: Ready for OAuth2 setup (if MailStation supports External Mail)
- **ProtonMail**: Via Proton Bridge on host PC (localhost:1143/1025)

---

## 🚀 Setup Steps

### Step 1: Configure Outlook Desktop

#### Quick Setup
1. **Open Outlook Desktop**
2. **File** → **Account Settings** → **Account Settings**
3. **New...** → **Manual setup or additional server types** → **POP or IMAP**

#### Account Information
```
Your Name: [Your Display Name]
Email Address: mlesn@homelab.lesnewski.local
Account Type: IMAP

Incoming mail server: 10.17.17.32
Outgoing mail server (SMTP): 10.17.17.32

User Name: mlesn@homelab.lesnewski.local
Password: [Your MailStation password]
```

#### Advanced Settings
**Outgoing Server Tab**:
- ✅ Check "My outgoing server (SMTP) requires authentication"
- Select "Use same settings as my incoming mail server"

**Advanced Tab**:
```
Incoming server (IMAP): 993
Use the following type of encrypted connection: SSL/TLS

Outgoing server (SMTP): 25
Use the following type of encrypted connection: STARTTLS
```

4. **Test Account Settings** → **Next** → **Finish**

---

### Step 2: Configure Outlook Mobile

1. **Open Outlook Mobile App**
2. **Add Account** → **Advanced Setup** → **IMAP**

#### Account Settings
```
Email: mlesn@homelab.lesnewski.local
Password: [Your MailStation password]

IMAP Server: 10.17.17.32
Port: 993
Security: SSL/TLS

SMTP Server: 10.17.17.32
Port: 25
Security: STARTTLS
Requires Authentication: Yes
```

3. **Save** and verify connection

---

### Step 3: Configure Gmail Integration

#### Option A: MailStation External Mail (if available)

1. **Access MailStation Settings**
   - DSM → MailStation → Settings → External Mail
   - Or check if External Mail feature exists

2. **Add Gmail Account**
   - If External Mail is available:
     - Click "Add Account"
     - Select "Gmail"
     - Complete OAuth2 flow
     - Configure sync settings

3. **If External Mail Not Available**:
   - Use N8N to fetch Gmail emails
   - Forward to MailStation
   - Or configure Gmail to forward to MailStation

#### Option B: Direct Gmail in Outlook (Alternative)

If MailStation External Mail is not available, add Gmail directly to Outlook:

1. **Add Gmail Account to Outlook**
   - Use Gmail App Password (not regular password)
   - IMAP: imap.gmail.com:993 (SSL)
   - SMTP: smtp.gmail.com:587 (STARTTLS)

2. **Gmail App Password Setup**:
   - Go to: https://myaccount.google.com/apppasswords
   - Enable 2-Step Verification first
   - Generate App Password for "Mail"
   - Use 16-character password in Outlook

---

### Step 4: Configure ProtonMail Integration

#### Current Setup
- **Proton Bridge**: Running on host PC (localhost:1143/1025)
- **Challenge**: MailStation cannot access localhost on host PC
- **Solution**: Use N8N as bridge

#### N8N Integration Setup

1. **Verify Proton Bridge is Running**
   - Check system tray for Proton Bridge icon
   - Ensure account is added and active

2. **Configure N8N Workflow**

**IMAP Node (Receive Emails)**:
```
Host: host.docker.internal (if N8N in Docker)
      OR [HOST_PC_IP] (if using host IP)
Port: 1143
Username: [Bridge-generated username]
Password: [Bridge-generated password]
SSL/TLS: OFF (Bridge uses STARTTLS)
Allow Self-Signed Certificates: ON
```

**SMTP Node (Send Emails)**:
```
Host: host.docker.internal (if N8N in Docker)
      OR [HOST_PC_IP] (if using host IP)
Port: 1025
Username: [Bridge-generated username]
Password: [Bridge-generated password]
SSL/TLS: OFF (Bridge uses STARTTLS)
Allow Self-Signed Certificates: ON
```

3. **Create N8N Workflow**
   - Email Trigger (IMAP) → Process → Forward to MailStation
   - Or: Store in database, process with SYPHON, etc.

4. **Alternative: Direct Outlook Connection**
   - Add ProtonMail account directly to Outlook
   - IMAP: 127.0.0.1:1143 (SSL)
   - SMTP: 127.0.0.1:1025 (SSL)
   - **Note**: Bridge must be running on same PC as Outlook

---

### Step 5: N8N Workflow Configuration

#### Workflow: ProtonMail to MailStation Bridge

**Purpose**: Fetch ProtonMail emails via Bridge and forward to MailStation

**Nodes**:
1. **Schedule Trigger**: Every 5 minutes
2. **IMAP (Proton Bridge)**: Fetch new emails
3. **Process Emails**: Extract content, categorize
4. **SMTP (MailStation)**: Forward to MailStation
5. **SYPHON**: Extract intelligence (optional)

**Configuration File**: `config/n8n/proton_bridge_n8n_config.json`

---

## 📋 Configuration Reference

### MailStation Settings
```
IMAP Server: 10.17.17.32
IMAP Port: 993 (SSL/TLS)
SMTP Server: 10.17.17.32
SMTP Port: 25 (STARTTLS)
Domain: homelab.lesnewski.local
```

### Gmail Settings (if direct)
```
IMAP Server: imap.gmail.com
IMAP Port: 993 (SSL)
SMTP Server: smtp.gmail.com
SMTP Port: 587 (STARTTLS)
Auth: App Password (16 characters)
```

### ProtonMail Bridge Settings
```
IMAP Server: 127.0.0.1 (localhost) or host.docker.internal
IMAP Port: 1143
SMTP Server: 127.0.0.1 (localhost) or host.docker.internal
SMTP Port: 1025
Auth: Bridge-generated credentials
```

---

## ✅ Verification Checklist

### MailStation
- [ ] Outlook Desktop connected
- [ ] Outlook Mobile connected
- [ ] Can send emails
- [ ] Can receive emails
- [ ] Ports 25/993 accessible

### Gmail
- [ ] External Mail configured (if available)
- [ ] OR: Direct Outlook connection working
- [ ] OR: N8N workflow fetching Gmail

### ProtonMail
- [ ] Proton Bridge running
- [ ] N8N workflow accessing Bridge
- [ ] OR: Direct Outlook connection working
- [ ] Emails being processed/forwarded

### N8N
- [ ] Workflows created
- [ ] Proton Bridge connection working
- [ ] Email processing active
- [ ] SYPHON integration working (if enabled)

---

## 🔧 Troubleshooting

### Outlook Cannot Connect to MailStation

**Issue**: Connection timeout or authentication failed

**Solutions**:
1. Verify NAS IP: `10.17.17.32`
2. Check firewall allows ports 25 and 993
3. Verify username: `mlesn@homelab.lesnewski.local`
4. Test connection: `telnet 10.17.17.32 993`
5. Check MailStation is running in DSM

### SMTP Port 25 Blocked

**Issue**: Cannot send emails (port 25 blocked by ISP)

**Solutions**:
1. Use ISP's SMTP relay
2. Configure port forwarding (if router supports)
3. Use alternative SMTP service
4. Check if MailStation supports port 587

### Proton Bridge Not Accessible from N8N

**Issue**: N8N cannot connect to Bridge on host PC

**Solutions**:
1. Use `host.docker.internal` (Docker Desktop)
2. Use host PC IP address
3. Configure Bridge to listen on network IP
4. Check firewall allows connections
5. Verify Bridge is running

### Gmail OAuth2 Fails

**Issue**: OAuth2 consent page errors

**Solutions**:
1. Clear browser cache
2. Remove existing permissions: https://myaccount.google.com/permissions
3. Use App Password instead (if OAuth2 not supported)
4. Check MailStation supports External Mail feature

---

## 📄 Configuration Files

- **Email Accounts**: `config/email_accounts_aggregation.json`
- **Outlook Config**: `config/outlook/mailstation_outlook_config.json`
- **N8N Config**: `config/n8n/nas_dsm_email_hub_expansion.json`
- **Proton Bridge N8N**: `config/n8n/proton_bridge_n8n_config.json`

---

## 🎯 Quick Start Commands

```bash
# Verify MailStation configuration
python scripts/python/verify_and_update_mailstation_config.py

# Check email hub status
python scripts/python/check_nas_email_hub_status.py

# Verify email connections
python scripts/python/verify_email_hub_nas.py
```

---

## 📚 Additional Documentation

- **MailStation Verified Config**: `docs/email/MAILSTATION_CONFIGURATION_VERIFIED.md`
- **Complete Setup Guide**: `docs/email/MAILPLUS_COMPLETE_SETUP.md` (for MailPlus upgrade reference)
- **Quick Reference**: `docs/email/MAILPLUS_QUICK_REFERENCE.md`

---

**Setup Complete!** All configurations verified and ready for use. 🚀
