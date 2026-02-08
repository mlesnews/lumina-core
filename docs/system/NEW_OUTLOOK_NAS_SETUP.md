# New Outlook - NAS Mail Hub Configuration

**Setting up New Outlook to pull from company email on NAS**

---

## 📧 Configuration Details

### NAS Mail Hub Settings

- **Email Account**: `mlesn@homelab.lesnewski.local`
- **IMAP Server**: `10.17.17.32`
- **IMAP Port**: `993` (SSL/TLS)
- **SMTP Server**: `10.17.17.32`
- **SMTP Port**: `587` (STARTTLS) or `465` (SSL)

---

## 🚀 Setup Steps

### Step 1: Open New Outlook

1. Launch **New Outlook** (not classic Outlook)
2. If you see a welcome screen, click **"Add Account"**
3. Or go to **File** → **Account Settings** → **Add Account**

### Step 2: Add Email Account

1. Click **"Add Account"** or **"Advanced setup"**
2. Select **"IMAP"** account type
3. Click **"Connect"** or **"Manual setup"**

### Step 3: Enter Account Information

**Basic Settings:**
- **Your Name**: Your display name (e.g., "Michael Lesnewski")
- **Email Address**: `mlesn@homelab.lesnewski.local`
- **Password**: [From Azure Vault or enter manually]

### Step 4: Advanced IMAP Settings

Click **"Advanced Options"** or **"More Settings"** → **"Advanced"** tab

**Incoming Mail Server (IMAP):**
```
Server: 10.17.17.32
Port: 993
Encryption: SSL/TLS
Authentication: Use same as incoming mail server
```

**Outgoing Mail Server (SMTP):**
```
Server: 10.17.17.32
Port: 587 (or 465 for SSL)
Encryption: STARTTLS (or SSL)
Authentication: Use same as incoming mail server
```

### Step 5: Test Connection

1. Click **"Test Account Settings"** or **"Next"**
2. Outlook will verify the connection
3. If successful, click **"Finish"** or **"Done"**

---

## ✅ Verification

**Check if it's working:**
1. New Outlook should show your email account in the sidebar
2. Emails should start syncing from NAS Mail Hub
3. You can send/receive emails normally

**Note**: Old Outlook remains configured and unchanged - you can use both if needed.

---

## 🔍 Troubleshooting

**If connection fails:**
1. Verify NAS Mail Hub is accessible: `10.17.17.32:993`
2. Check firewall allows IMAP/SMTP ports
3. Verify email password is correct
4. Try port 143 (non-SSL) if 993 doesn't work
5. Check "Allow less secure apps" if required

**If emails don't sync:**
1. Check account status in Outlook settings
2. Verify IMAP is enabled on NAS Mail Hub
3. Check NAS Mail Hub logs for connection attempts

---

## 📋 Summary

- ✅ **New Outlook**: Configured to pull from NAS Mail Hub
- ✅ **Old Outlook**: Left unchanged (still configured as before)
- ✅ **Both can coexist**: Use New Outlook going forward

---

**Configuration File**: `config/new_outlook_nas_config.json`

**Status**: ✅ **READY FOR MANUAL CONFIGURATION**
