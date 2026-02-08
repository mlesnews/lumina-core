# Email SYPHON Setup Instructions - NAS Mail Hub

**Quick Setup Guide for N8N Email SYPHON Workflow**

---

## ✅ Current Status

- **Workflow Deployed**: ✅ Email SYPHON (ID: `CvU8gDibd1VYpxWf`)
- **NAS Mail Hub**: `10.17.17.32:993` (MailStation/MailPlus)
- **Company Email**: `mlesn@homelab.lesnewski.local`
- **Outlook Clients**: Already configured to use NAS Mail Hub

---

## 🔧 Configuration Steps

### Step 1: Access N8N Workflow

1. Open: `http://10.17.17.32:5678/home/workflows`
2. Find: **"SYPHON Email Intelligence Extraction"**
3. Click to open the workflow

### Step 2: Configure IMAP Credentials

1. Click on the **"Fetch All Emails"** node
2. In the node settings, find **"Credentials"** section
3. Click **"Create New Credential"** or edit existing **"NAS Email Account"**

### Step 3: Enter IMAP Settings

**IMAP Configuration:**
```
Type: IMAP
Host: 10.17.17.32
Port: 993
User: mlesn@homelab.lesnewski.local
Password: [Your company email password]
Secure: Yes (SSL/TLS)
Allow Unauthorized Certificates: Yes (if using self-signed cert)
```

**Or use Azure Vault password:**
- Password can be retrieved from Azure Vault: `nas-email-password` or `company-email-password`

### Step 4: Test Connection

1. Click **"Test"** or **"Execute Node"** on the "Fetch All Emails" node
2. Verify emails are fetched successfully
3. Check that email data appears in the node output

### Step 5: Activate Workflow

1. Toggle the workflow switch to **"Active"**
2. Workflow will run automatically every 2 hours
3. Monitor executions in N8N dashboard

---

## 📊 How It Works

### Email Flow

1. **Email Arrives**
   - Email sent to your company email
   - Stored on NAS Mail Hub (`10.17.17.32`)
   - Available via IMAP

2. **Outlook Clients Access**
   - Desktop Outlook: Connects to `10.17.17.32:993` → Sees email
   - Mobile Outlook: Connects to `10.17.17.32:993` → Sees email
   - **No changes needed** - Outlook already configured

3. **N8N SYPHON Extracts**
   - Every 2 hours: N8N connects to `10.17.17.32:993`
   - Fetches new emails via IMAP
   - Extracts intelligence via SYPHON API
   - Saves to NAS: `/data/syphon/email_intelligence/`
   - Adds to unified queue

---

## 🔍 Verification

**Check if it's working:**
1. Go to N8N: `http://10.17.17.32:5678/home/executions`
2. Look for "SYPHON Email Intelligence Extraction" executions
3. Check execution logs for:
   - ✅ Emails fetched
   - ✅ SYPHON extraction successful
   - ✅ Intelligence saved

**Check NAS storage:**
- Location: `/data/syphon/email_intelligence/YYYY-MM-DD_email_intelligence.jsonl`
- Files should appear after first successful run

---

## ⚠️ Important Notes

1. **No Impact on Outlook**: SYPHON only reads emails, never modifies or deletes
2. **Same Source**: All clients (Outlook desktop, mobile, N8N) read from same NAS Mail Hub
3. **Deduplication**: SYPHON tracks processed emails to avoid duplicates
4. **Privacy**: All processing happens on NAS, stored locally

---

## 🎯 Expected Results

Once configured and active:
- ✅ Emails extracted every 2 hours
- ✅ Intelligence saved to NAS
- ✅ Added to unified queue
- ✅ No interference with Outlook usage

---

**Status**: ✅ **WORKFLOW DEPLOYED - AWAITING IMAP CREDENTIAL CONFIGURATION**
