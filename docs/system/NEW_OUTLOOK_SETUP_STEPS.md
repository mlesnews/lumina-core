# New Outlook Setup - Remove Gmail, Add NAS Email

**Complete step-by-step instructions**

---

## 🗑️ STEP 1: Remove Gmail Account

1. **Open New Outlook** (ensure it's running)

2. **Open Account Settings**:
   - Press `Ctrl+Shift+A` (Account Settings shortcut)
   - OR: Click **File** → **Account Settings** → **Account Settings**

3. **Remove Gmail**:
   - In the account list, **select** the Gmail account
   - Click **"Remove"** button (usually at bottom or top of dialog)
   - **Confirm** removal when prompted
   - Click **"Close"** to close Account Settings

---

## ➕ STEP 2: Add NAS Company Email

1. **Open Add Account**:
   - In New Outlook: Click **File** → **Add Account**
   - OR: Look for **"Add Account"** button in the UI

2. **Select Advanced Setup**:
   - Click **"Advanced setup"** or **"Manual setup"**
   - (Skip automatic detection)

3. **Choose IMAP**:
   - Select **"IMAP"** account type
   - Click **Next** or **Continue**

4. **Enter Account Information**:
   ```
   Your Name: [Your Display Name]
   Email Address: mlesn@homelab.lesnewski.local
   Password: [From Azure Vault or enter manually]
   ```

5. **Click "Advanced Options"** or **"More Settings"**

6. **Configure Incoming Mail (IMAP)**:
   ```
   Server: 10.17.17.32
   Port: 993
   Encryption: SSL/TLS
   Authentication: Use same as incoming mail server
   ```

7. **Configure Outgoing Mail (SMTP)**:
   ```
   Server: 10.17.17.32
   Port: 587
   Encryption: STARTTLS
   Authentication: Use same as incoming mail server
   ```

8. **Connect**:
   - Click **"Connect"** or **"Finish"**
   - Wait for connection test
   - Click **"Done"** when complete

---

## ✅ Verification

**Check New Outlook:**
- Gmail account should be **removed**
- NAS company email (`mlesn@homelab.lesnewski.local`) should be **added**
- Emails should start syncing from NAS Mail Hub

**Old Outlook:**
- Remains unchanged
- Still has its own configuration
- Both can coexist

---

## 📋 Configuration Summary

**NAS Mail Hub Settings:**
- **IMAP Server**: `10.17.17.32:993` (SSL/TLS)
- **SMTP Server**: `10.17.17.32:587` (STARTTLS)
- **Email**: `mlesn@homelab.lesnewski.local`
- **Password**: From Azure Vault (`n8n-password`)

---

**Status**: ✅ **READY FOR MANUAL CONFIGURATION**

**Note**: New Outlook's UI structure makes full automation difficult. These manual steps are the most reliable method.
