# New Outlook Setup - Remove Gmail, Add NAS Company Email

**Complete step-by-step instructions**

---

## 🗑️ STEP 1: Remove Gmail Account

1. **Open New Outlook** (ensure it's running)
2. **Go to**: File → Account Settings → Account Settings
   - Or press `Ctrl+Shift+A` (Account Settings shortcut)
3. **Select** the Gmail account in the list
4. **Click** "Remove" or "Delete" button
5. **Confirm** removal when prompted
6. **Click** "Close"

---

## ➕ STEP 2: Add NAS Company Email

1. **In New Outlook**: File → Add Account
   - Or click "Add Account" button if visible

2. **Select**: "Advanced setup" or "Manual setup"

3. **Choose**: "IMAP" account type

4. **Enter Account Information**:
   ```
   Your Name: [Your Display Name]
   Email Address: mlesn@homelab.lesnewski.local
   Password: [From Azure Vault or enter manually]
   ```

5. **Click**: "Advanced Options" or "More Settings"

6. **Incoming Mail Server (IMAP)**:
   ```
   Server: 10.17.17.32
   Port: 993
   Encryption: SSL/TLS
   Authentication: Use same as incoming mail server
   ```

7. **Outgoing Mail Server (SMTP)**:
   ```
   Server: 10.17.17.32
   Port: 587
   Encryption: STARTTLS
   Authentication: Use same as incoming mail server
   ```

8. **Click**: "Connect" or "Finish"

9. **Wait** for connection test to complete

10. **Click**: "Done" or "Close"

---

## ✅ Verification

**Check if it's working:**
- New Outlook should show only the NAS company email account
- Emails should start syncing from NAS Mail Hub
- You can send/receive emails normally

---

## 📋 Summary

- ✅ **Gmail removed**: No longer in New Outlook
- ✅ **NAS email added**: `mlesn@homelab.lesnewski.local` configured
- ✅ **Old Outlook**: Remains unchanged (still has its own configuration)

---

**Status**: ✅ **READY FOR MANUAL CONFIGURATION**

**Note**: New Outlook requires manual UI interaction - automation is limited due to UI complexity.
