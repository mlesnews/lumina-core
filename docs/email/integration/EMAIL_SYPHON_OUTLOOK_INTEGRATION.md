# Email SYPHON - Outlook & Company Email Server Integration

**How Email SYPHON Works with Outlook (Desktop/Mobile) and Company Email Server**

---

## 📧 Email Architecture

### Current Setup

```
┌─────────────────────────────────────────────────────────────┐
│                    NAS Mail Hub                              │
│         (MailStation/MailPlus on 10.17.17.32)                │
│                                                              │
│  • Company Email Server (on NAS)                             │
│  • Aggregates ALL emails from ALL providers:                  │
│    - Gmail, Apple Mail, ProtonMail, Outlook, etc.            │
│  • Company email accounts:                                    │
│    - mlesn@homelab.lesnewski.local                           │
│    - glesn@homelab.lesnewski.local                           │
│  • IMAP port: 993 (secure)                                   │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         │                    │                    │
    ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
    │ Desktop │         │ Mobile  │         │   NAS   │
    │ Outlook │         │ Outlook │         │  N8N    │
    │         │         │         │         │ SYPHON  │
    │ Connects│         │ Connects│         │ Connects│
    │ to NAS  │         │ to NAS  │         │ to NAS  │
    └─────────┘         └─────────┘         └─────────┘
```

---

## 🔄 How It Works

### 1. **Outlook Clients (Desktop & Mobile)**
- **Connect to**: NAS Mail Hub (10.17.17.32)
- **Protocol**: IMAP/Exchange (via NAS MailStation/MailPlus)
- **Function**: Read, send, manage emails
- **Access**: Real-time, immediate
- **User Experience**: Normal Outlook usage - configured to use NAS email server
- **Email Accounts**: 
  - `mlesn@homelab.lesnewski.local`
  - `glesn@homelab.lesnewski.local`
  - (All aggregated emails from Gmail, Outlook, ProtonMail, etc.)

### 2. **N8N SYPHON Workflow (on NAS)**
- **Connects to**: Same NAS Mail Hub (10.17.17.32:993)
- **Protocol**: IMAP
- **Function**: Extract intelligence from emails
- **Schedule**: Every 2 hours
- **Access**: Read-only (doesn't interfere with Outlook)
- **Email Accounts**: Same company email accounts on NAS

---

## 🔐 Email Flow

### Step-by-Step Process

1. **Email Arrives at Company Server**
   - Email sent to your company email address
   - Stored on company email server
   - Available via IMAP/Exchange

2. **Outlook Clients Access Email**
   - Desktop Outlook connects → sees email immediately
   - Mobile Outlook connects → sees email immediately
   - Both read from same server, same mailbox
   - **No interference** - normal email access

3. **N8N SYPHON Workflow (Every 2 Hours)**
   - N8N on NAS connects to company email server via IMAP
   - Fetches new emails since last check
   - Extracts intelligence via SYPHON API
   - Saves to NAS storage
   - Adds to unified queue

---

## ⚙️ Configuration Required

### N8N Workflow Needs IMAP Credentials

The workflow references: **"NAS Email Account"** credential

**Required Configuration in N8N:**
1. Go to N8N: `http://10.17.17.32:5678`
2. Open "SYPHON Email Intelligence Extraction" workflow
3. Click on "Fetch All Emails" node
4. Configure IMAP credentials for "NAS Email Account":
   - **IMAP Server**: `10.17.17.32` (NAS Mail Hub)
   - **Port**: `993` (IMAPS - secure)
   - **Username**: `mlesn@homelab.lesnewski.local` (or your company email)
   - **Password**: Company email password (stored in Azure Vault)
   - **SSL/TLS**: Enabled (required for port 993)
   - **Allow Unauthorized Certs**: Enabled (if using self-signed cert)

---

## 📋 NAS Mail Hub Configuration

**Already Configured:**
- **IMAP Server**: `10.17.17.32` (NAS Mail Hub)
- **IMAP Port**: `993` (IMAPS - secure)
- **Mail System**: MailStation/MailPlus on NAS
- **Company Domain**: `homelab.lesnewski.local`

**Email Accounts on NAS:**
- `mlesn@homelab.lesnewski.local` - Primary company email
- `glesn@homelab.lesnewski.local` - Secondary company email

**What's Needed:**
1. **IMAP Credentials in N8N**
   - Username: `mlesn@homelab.lesnewski.local`
   - Password: (from Azure Vault or company email password)

2. **Verify Outlook Configuration**
   - Desktop Outlook: Should be configured to connect to NAS Mail Hub
   - Mobile Outlook: Should be configured to connect to NAS Mail Hub
   - Both use same IMAP server: `10.17.17.32:993`

---

## 🔍 How Outlook and SYPHON Coexist

### ✅ No Conflicts

- **Outlook**: Reads emails for user interaction
- **SYPHON**: Reads emails for intelligence extraction
- **Both**: Access same mailbox, same emails
- **Result**: No interference, no duplicates, no issues

### 📊 Email Access Pattern

```
Timeline:
─────────────────────────────────────────────────────────
00:00  Email arrives at NAS Mail Hub (10.17.17.32)
       (Aggregated from Gmail, Outlook, ProtonMail, etc.)
00:01  Desktop Outlook syncs → User sees email immediately
00:02  Mobile Outlook syncs → User sees email immediately
02:00  N8N SYPHON runs → Connects to NAS Mail Hub via IMAP
       → Extracts intelligence from new emails
04:00  N8N SYPHON runs → Extracts intelligence
06:00  N8N SYPHON runs → Extracts intelligence
...
```

**Key Point**: All three (Desktop Outlook, Mobile Outlook, N8N SYPHON) connect to the **same NAS Mail Hub** and read from the **same email accounts**. No conflicts, no interference.

---

## 🎯 What Gets Extracted

For each email, SYPHON extracts:
- **Subject**: Email subject line
- **Body**: Email content (text/HTML)
- **From/To**: Sender and recipient
- **Date**: Timestamp
- **Attachments**: Metadata about attachments
- **Intelligence**: Processed insights via SYPHON API

**Stored on NAS**: `/data/syphon/email_intelligence/YYYY-MM-DD_email_intelligence.jsonl`

---

## ⚠️ Important Notes

1. **Read-Only Access**: SYPHON only reads emails, never deletes or modifies
2. **No Impact on Outlook**: Your Outlook experience is unchanged
3. **Deduplication**: SYPHON tracks processed emails to avoid duplicates
4. **Privacy**: All processing happens on NAS, intelligence stored locally

---

## 🔧 Next Steps

1. **Configure IMAP Credentials in N8N**
   - Access workflow in N8N
   - Set up "NAS Email Account" credential
   - Use company email server IMAP details

2. **Test Connection**
   - Run workflow manually in N8N
   - Verify emails are fetched
   - Check SYPHON extraction works

3. **Activate Workflow**
   - Toggle workflow to "Active"
   - Runs automatically every 2 hours

---

**Status**: ✅ **WORKFLOW DEPLOYED - AWAITING IMAP CONFIGURATION**

**Workflow ID**: `CvU8gDibd1VYpxWf`

**Access**: `http://10.17.17.32:5678/home/workflows`
