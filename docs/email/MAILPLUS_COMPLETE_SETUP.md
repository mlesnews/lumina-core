# MailPlus Complete Setup Guide
## Gmail + ProtonMail → MailPlus → Outlook Desktop/Mobile → N8N@NAS

---

## 📋 Overview

This guide configures:
1. **Synology MailPlus** as the central email hub
2. **Gmail** integration via OAuth2
3. **ProtonMail** integration via Proton Email Bridge
4. **Outlook Desktop** connection to MailPlus
5. **Outlook Mobile** connection to MailPlus
6. **N8N@NAS** integration with Proton Bridge for automation

---

## 🎯 Architecture

```
┌─────────────┐
│   Gmail     │──OAuth2──>┌──────────────┐
└─────────────┘           │              │
                          │  MailPlus    │<──IMAP/SMTP──┐
┌─────────────┐           │  Server      │              │
│ ProtonMail  │──Bridge──>│  (NAS)       │              │
│   Bridge    │           │              │              │
│ (localhost) │           └──────────────┘              │
└─────────────┘                  │                      │
                                 │                      │
                    ┌────────────┴────────────┐        │
                    │                         │        │
            ┌───────▼───────┐        ┌───────▼───────┐ │
            │ Outlook       │        │ Outlook       │ │
            │ Desktop       │        │ Mobile        │ │
            └───────────────┘        └───────────────┘ │
                                                       │
                                                       │
            ┌──────────────────────────────────────────┘
            │
    ┌───────▼───────┐
    │   N8N@NAS    │
    │  (Workflows)  │
    └───────────────┘
```

---

## 📧 Part 1: MailPlus Gmail Setup

### Step 1: Access MailPlus Server

1. **Log into DSM** (Synology DiskStation Manager)
2. **Open MailPlus Server** application
3. **Navigate to**: `Mail Server` → `External Mail` (or `Settings` → `External Mail`)

### Step 2: Add Gmail Account via OAuth2

1. **Click**: `Add Account` or `+` button
2. **Select**: `Gmail` from the provider list
3. **OAuth Flow**:
   - You'll be redirected to Google's OAuth consent page
   - Sign in with your Gmail account
   - **Grant permissions**: "Read, compose, send, and permanently delete all your email from Gmail"
   - Click `Allow` or `Continue`
   - You'll be redirected back to MailPlus

4. **MailPlus Configuration** (if manual entry needed):
   ```
   Account Type: Gmail
   Incoming Server: imap.gmail.com
   Port: 993
   Encryption: SSL/TLS
   Authentication: OAuth 2.0
   
   Outgoing Server: smtp.gmail.com
   Port: 587 (STARTTLS) or 465 (SSL)
   Encryption: STARTTLS or SSL
   Authentication: OAuth 2.0
   ```

5. **Sync Settings**:
   - **Sync Frequency**: Every 15 minutes (or as needed)
   - **Folders to Sync**: All folders or selected folders
   - **Sync Direction**: Both ways (bidirectional)

6. **Save Configuration**

### Step 3: Verify Gmail Connection

1. **Check Status**: External Mail account should show "Connected" or "Active"
2. **Test Sync**: Click "Sync Now" to test connection
3. **Check Logs**: Review MailPlus logs for any errors

---

## 🔐 Part 2: MailPlus ProtonMail Setup (via Bridge)

### Step 1: Install Proton Email Bridge

1. **Download Proton Bridge**:
   - Visit: https://proton.me/mail/bridge
   - Download for your OS (Windows/Mac/Linux)
   - Install the application

2. **Launch Proton Bridge**:
   - Sign in with your ProtonMail credentials
   - Add your ProtonMail account to Bridge
   - Bridge will generate local IMAP/SMTP credentials

### Step 2: Configure Proton Bridge

1. **Open Bridge Settings**:
   - Click on your account in Bridge
   - Go to `Settings` → `Advanced Settings`

2. **Note Bridge Credentials**:
   ```
   IMAP Server: 127.0.0.1 (localhost)
   IMAP Port: 1143 (default, change if needed)
   SMTP Server: 127.0.0.1 (localhost)
   SMTP Port: 1025 (default, change if needed)
   
   Username: [Bridge-generated username]
   Password: [Bridge-generated password]
   ```

3. **Connection Mode**:
   - **Recommended**: STARTTLS
   - Alternative: SSL (if needed)

4. **Port Configuration** (if conflicts):
   - Change ports in Bridge if 1143/1025 are in use
   - Update MailPlus configuration accordingly

### Step 3: Add ProtonMail to MailPlus

**Important**: Since Bridge runs on localhost, MailPlus on NAS cannot directly connect to it. You have two options:

#### Option A: Bridge on NAS (Recommended)

1. **Install Bridge on NAS**:
   - If NAS supports Docker: Run Bridge in container
   - Or install Bridge directly on NAS if supported
   - Configure Bridge to listen on NAS IP instead of localhost

2. **Bridge Network Configuration**:
   ```
   IMAP Server: [NAS IP Address] (e.g., 192.168.1.100)
   IMAP Port: 1143
   SMTP Server: [NAS IP Address]
   SMTP Port: 1025
   ```

3. **Add to MailPlus**:
   - In MailPlus External Mail settings
   - Add account manually:
     ```
     Account Type: Other
     Incoming Server: [NAS IP Address]
     Port: 1143
     Encryption: STARTTLS (or SSL)
     Username: [Bridge-generated username]
     Password: [Bridge-generated password]
     
     Outgoing Server: [NAS IP Address]
     Port: 1025
     Encryption: STARTTLS (or SSL)
     Username: [Bridge-generated username]
     Password: [Bridge-generated password]
     ```

#### Option B: Bridge on Local Machine + MailPlus Forwarding

1. **Keep Bridge on localhost** (your desktop)
2. **Configure MailPlus to forward**:
   - Set up email forwarding rules
   - Or use N8N to bridge the connection (see Part 6)

---

## 💻 Part 3: Outlook Desktop Configuration

### Step 1: Get MailPlus IMAP/SMTP Settings

1. **Access MailPlus Web Client**:
   - Open MailPlus web interface
   - Go to `Settings` → `Account` → `IMAP/POP3`

2. **Note Your MailPlus Credentials**:
   ```
   IMAP Server: [NAS IP] or [mail.yourdomain.local]
   Port: 993 (IMAPS) or 143 (IMAP)
   Encryption: SSL/TLS
   Username: [Your MailPlus email address]
   Password: [Your MailPlus password]
   
   SMTP Server: [NAS IP] or [mail.yourdomain.local]
   Port: 587 (STARTTLS) or 465 (SSL)
   Encryption: STARTTLS or SSL
   Username: [Your MailPlus email address]
   Password: [Your MailPlus password]
   ```

### Step 2: Add Account to Outlook Desktop

1. **Open Outlook**
2. **Add Account**:
   - `File` → `Account Settings` → `Account Settings`
   - Click `New...`
   - Select `Manual setup or additional server types`
   - Choose `POP or IMAP`

3. **Enter Account Information**:
   ```
   Your Name: [Your Display Name]
   Email Address: [Your MailPlus email address]
   Account Type: IMAP
   
   Incoming mail server: [NAS IP or mail server address]
   Outgoing mail server (SMTP): [NAS IP or mail server address]
   
   User Name: [Your MailPlus email address]
   Password: [Your MailPlus password]
   ```

4. **More Settings**:
   - Click `More Settings...`
   - **Outgoing Server Tab**:
     - ✅ Check "My outgoing server (SMTP) requires authentication"
     - Select "Use same settings as my incoming mail server"
   
   - **Advanced Tab**:
     ```
     Incoming server (IMAP): 993
     Use the following type of encrypted connection: SSL/TLS
     
     Outgoing server (SMTP): 587
     Use the following type of encrypted connection: STARTTLS
     ```

5. **Test Account Settings**:
   - Click `Test Account Settings...`
   - Verify both incoming and outgoing tests pass
   - Click `Next` → `Finish`

### Step 3: Configure Folders

1. **Sync Settings**:
   - Right-click on account → `Properties`
   - Go to `Synchronization` tab
   - Select folders to sync
   - Set sync frequency

2. **Verify External Mail Sync**:
   - Gmail and ProtonMail emails should appear in Outlook
   - Check that folders are syncing correctly

---

## 📱 Part 4: Outlook Mobile Configuration

### Step 1: Add Account

1. **Open Outlook Mobile App**
2. **Add Account**:
   - Tap `Get Started` or `Add Account`
   - Select `Add Account`
   - Choose `Advanced Setup` or `IMAP`

3. **Enter Account Details**:
   ```
   Email Address: [Your MailPlus email address]
   Password: [Your MailPlus password]
   ```

4. **Manual Configuration** (if auto-detect fails):
   ```
   Account Type: IMAP
   
   Incoming Mail Server: [NAS IP or mail server address]
   Port: 993
   Security: SSL/TLS
   Username: [Your MailPlus email address]
   Password: [Your MailPlus password]
   
   Outgoing Mail Server: [NAS IP or mail server address]
   Port: 587
   Security: STARTTLS
   Username: [Your MailPlus email address]
   Password: [Your MailPlus password]
   ```

5. **Save and Verify**:
   - Tap `Sign In` or `Save`
   - Wait for account verification
   - Emails should start syncing

### Step 2: Configure Sync Settings

1. **Open Account Settings**:
   - Tap account name → `Settings`
   - Select your MailPlus account

2. **Sync Options**:
   - **Sync Frequency**: Automatic or Manual
   - **Days to Sync**: 30 days, 3 months, or All
   - **Sync Folders**: Select folders to sync
   - **Notifications**: Enable/disable as needed

---

## ⚙️ Part 5: N8N@NAS Integration with Proton Bridge

### Step 1: Configure Proton Bridge for N8N

1. **Ensure Bridge is Running**:
   - Bridge must be running on the host where N8N can access it
   - If N8N is in Docker, Bridge must be accessible from container

2. **Bridge Network Configuration**:
   - If N8N is on NAS and Bridge is on localhost:
     - Use `host.docker.internal` (Docker Desktop)
     - Or use NAS IP if Bridge is installed on NAS
     - Or use host networking mode

### Step 2: N8N IMAP Configuration (Receive Emails)

1. **Create New Workflow** in N8N
2. **Add Email Trigger (IMAP) Node**:
   - Node: `Email Trigger (IMAP)`
   - **Credentials**:
     ```
     Host: 127.0.0.1 (if Bridge on same host)
            OR
     Host: host.docker.internal (if N8N in Docker, Bridge on host)
            OR
     Host: [NAS IP] (if Bridge on NAS)
     
     Port: 1143 (or custom port from Bridge)
     Username: [Bridge-generated username]
     Password: [Bridge-generated password]
     SSL/TLS: OFF (if Bridge in STARTTLS mode)
              ON (if Bridge in SSL mode)
     Allow Self-Signed Certificates: ON
     ```
   - **Mailbox**: `INBOX` (or specific folder)
   - **Options**:
     - **Process All Unread**: Yes
     - **Download Attachments**: Yes (if needed)

3. **Test Connection**:
   - Click `Execute Node`
   - Verify emails are retrieved

### Step 3: N8N SMTP Configuration (Send Emails)

1. **Add Send Email Node**:
   - Node: `Send Email`
   - **Credentials**:
     ```
     Host: 127.0.0.1 (or host.docker.internal or NAS IP)
     Port: 1025 (or custom port from Bridge)
     Username: [Bridge-generated username]
     Password: [Bridge-generated password]
     SSL/TLS: OFF (if Bridge in STARTTLS mode)
              ON (if Bridge in SSL mode)
     Disable STARTTLS: OFF (if using STARTTLS)
     Allow Self-Signed Certificates: ON
     ```
   - **Email Configuration**:
     ```
     From Email: [Your ProtonMail address]
     To Email: [Recipient]
     Subject: [Email subject]
     Email Type: HTML or Text
     Message: [Email body]
     ```

2. **Test Sending**:
   - Execute node with test data
   - Verify email is sent via ProtonMail

### Step 4: N8N Workflow Examples

#### Example 1: Email Processing Workflow
```json
{
  "nodes": [
    {
      "name": "ProtonMail Trigger",
      "type": "n8n-nodes-base.emailImap",
      "parameters": {
        "host": "host.docker.internal",
        "port": 1143,
        "mailbox": "INBOX",
        "options": {
          "allowUnauthorizedCerts": true
        }
      }
    },
    {
      "name": "Process Email",
      "type": "n8n-nodes-base.function",
      "parameters": {
        "functionCode": "// Process email content\nreturn items;"
      }
    },
    {
      "name": "Store in NAS",
      "type": "n8n-nodes-base.writeBinaryFile",
      "parameters": {
        "fileName": "emails/{{ $now.format('YYYY-MM-DD') }}/{{ $json.messageId }}.eml"
      }
    }
  ]
}
```

#### Example 2: Email Automation Workflow
```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "parameters": {
        "cronExpression": "0 */15 * * * *"
      }
    },
    {
      "name": "Check ProtonMail",
      "type": "n8n-nodes-base.emailImap",
      "parameters": {
        "host": "host.docker.internal",
        "port": 1143,
        "mailbox": "INBOX"
      }
    },
    {
      "name": "Filter Important",
      "type": "n8n-nodes-base.filter",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.subject }}",
              "operation": "contains",
              "value2": "URGENT"
            }
          ]
        }
      }
    },
    {
      "name": "Send Notification",
      "type": "n8n-nodes-base.sendEmail",
      "parameters": {
        "host": "host.docker.internal",
        "port": 1025,
        "fromEmail": "your@protonmail.com",
        "toEmail": "notification@example.com",
        "subject": "URGENT: {{ $json.subject }}",
        "message": "{{ $json.text }}"
      }
    }
  ]
}
```

---

## 🔧 Part 6: Troubleshooting

### Gmail OAuth Issues

1. **Permission Denied**:
   - Go to [Google Account Permissions](https://myaccount.google.com/permissions)
   - Remove "Synology" or "MailPlus" entries
   - Re-add account in MailPlus

2. **Token Expired**:
   - Re-authenticate in MailPlus External Mail settings
   - Complete OAuth flow again

3. **IMAP Not Enabled**:
   - Gmail IMAP is always on with OAuth
   - No manual toggle needed

### Proton Bridge Issues

1. **Port Conflicts**:
   - Change Bridge ports in Settings → Advanced
   - Update MailPlus and N8N configurations

2. **Certificate Errors**:
   - Enable "Allow Self-Signed Certificates" in clients
   - Or export Bridge certificate and install it

3. **Connection from NAS to Bridge**:
   - If Bridge on localhost, NAS cannot reach it
   - Solution: Install Bridge on NAS or use Docker with host networking

### Outlook Connection Issues

1. **Cannot Connect to MailPlus**:
   - Verify NAS IP address is correct
   - Check firewall allows IMAP (993) and SMTP (587)
   - Test connection: `telnet [NAS IP] 993`

2. **Authentication Failed**:
   - Verify MailPlus username/password
   - Check account is activated in MailPlus Server
   - Ensure IMAP/POP3 is enabled for user

3. **SSL/TLS Errors**:
   - Verify MailPlus SSL certificate
   - Accept certificate in Outlook
   - Or use self-signed certificate settings

### N8N Integration Issues

1. **Cannot Reach Bridge**:
   - If N8N in Docker: Use `host.docker.internal`
   - If on Linux: Use host IP or host networking
   - Verify Bridge is running and ports are open

2. **Authentication Failed**:
   - Use Bridge-generated credentials (not ProtonMail password)
   - Verify Bridge is running and account is added

3. **Certificate Errors**:
   - Enable "Allow Self-Signed Certificates" in N8N
   - Or use STARTTLS mode with SSL/TLS OFF

---

## ✅ Verification Checklist

### MailPlus Setup
- [ ] Gmail account added via OAuth2
- [ ] Gmail sync working (emails appearing)
- [ ] ProtonMail Bridge configured
- [ ] ProtonMail account added to MailPlus (if Bridge on NAS)
- [ ] External mail accounts showing "Connected" status

### Outlook Desktop
- [ ] Account added successfully
- [ ] Incoming emails syncing
- [ ] Outgoing emails sending
- [ ] Gmail emails visible
- [ ] ProtonMail emails visible (if configured)

### Outlook Mobile
- [ ] Account added successfully
- [ ] Push notifications working
- [ ] Emails syncing correctly
- [ ] Send/receive working

### N8N Integration
- [ ] Proton Bridge accessible from N8N
- [ ] IMAP trigger working (receiving emails)
- [ ] SMTP send working (sending emails)
- [ ] Workflows executing successfully

---

## 📚 Additional Resources

- **Synology MailPlus Documentation**: https://kb.synology.com/en-us/DSM/help/MailPlus/mailplus
- **Proton Bridge Guide**: https://proton.me/support/imap-smtp-and-pop3-setup
- **N8N Email Nodes**: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap/
- **Gmail OAuth Setup**: https://developers.google.com/gmail/imap/xoauth2-protocol

---

## 🎯 Next Steps

1. **Test Email Flow**: Send test emails through each account
2. **Monitor Sync**: Check MailPlus logs for sync status
3. **Create N8N Workflows**: Build automation workflows
4. **Set Up Rules**: Configure MailPlus email rules for organization
5. **Backup Configuration**: Document all settings for future reference

---

**Setup Complete!** Your email infrastructure is now centralized through MailPlus with Outlook clients and N8N automation integrated. 🚀
