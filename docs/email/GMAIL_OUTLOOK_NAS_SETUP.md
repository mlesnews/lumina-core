# Gmail to Outlook Setup via NAS Email Hub

## Problem Summary
- **Issue**: OAuth authentication errors when setting up Gmail in old Outlook
- **Requirement**: All email traffic must route through company NAS email hub
- **Error**: Google OAuth consent page errors during authentication

## Solution Overview

Since you want everything to go through your NAS email hub, we have two approaches:

### Option 1: NAS as Email Relay/Proxy (Recommended)
Configure your NAS DSM Mail Server to:
1. Connect to Gmail using OAuth2 (which the NAS supports)
2. Act as an IMAP/SMTP server for Outlook
3. Route all Gmail traffic through the NAS

### Option 2: Direct Gmail with App Password (Fallback)
If NAS relay isn't feasible, use Google App Passwords for old Outlook versions that don't support OAuth.

---

## Option 1: NAS Email Hub Configuration (Recommended)

### Step 1: Configure NAS DSM Mail Server for Gmail OAuth

1. **Access NAS DSM Mail Server**
   - Log into your NAS DSM interface
   - Navigate to Mail Server application
   - Go to Mail Server Settings

2. **Enable Gmail OAuth2 Integration**
   - In Mail Server settings, find "External Mail Accounts" or "Mail Relay"
   - Add Gmail account using OAuth2 authentication
   - Complete the OAuth flow in the NAS interface (this will work where Outlook fails)
   - Grant permissions: "Read, compose, send, and permanently delete all your email from Gmail"

3. **Configure IMAP/SMTP Relay**
   - Set NAS to act as IMAP/SMTP relay for Gmail
   - NAS will maintain the OAuth connection
   - Outlook will connect to NAS using standard IMAP/SMTP (no OAuth needed)

### Step 2: Configure Outlook to Connect to NAS

Instead of connecting Outlook directly to Gmail, connect it to your NAS:

**IMAP Settings for Outlook:**
```
Incoming Mail Server: [NAS IP Address] or [mail.yourcompany.local]
Port: 143 (IMAP) or 993 (IMAPS)
Encryption: SSL/TLS
Username: [Your NAS email account or Gmail address]
Password: [NAS email password or App Password]
```

**SMTP Settings for Outlook:**
```
Outgoing Mail Server: [NAS IP Address] or [mail.yourcompany.local]
Port: 587 (STARTTLS) or 465 (SSL)
Encryption: SSL/TLS
Username: [Your NAS email account or Gmail address]
Password: [NAS email password or App Password]
```

### Step 3: NAS Email Hub Benefits

✅ **OAuth handled by NAS**: NAS maintains Gmail OAuth connection
✅ **Centralized routing**: All email traffic goes through NAS
✅ **Old Outlook compatible**: Outlook uses standard IMAP/SMTP (no OAuth)
✅ **Unified management**: All email accounts managed through NAS
✅ **Security**: NAS acts as secure gateway

---

## Option 2: Direct Gmail with App Password (If NAS Relay Not Available)

If your NAS doesn't support Gmail OAuth relay, use Google App Passwords:

### Step 1: Enable 2-Step Verification

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification** (required for App Passwords)
3. Complete the setup process

### Step 2: Generate App Password

1. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
2. Select "Mail" and "Other (Custom name)"
3. Enter name: "Outlook [Your Computer Name]"
4. Click "Generate"
5. **Copy the 16-character password** (you'll use this in Outlook)

### Step 3: Configure Outlook with App Password

**IMAP Settings:**
```
Incoming Mail Server: imap.gmail.com
Port: 993
Encryption: SSL/TLS
Username: your.email@gmail.com
Password: [16-character App Password from Step 2]
```

**SMTP Settings:**
```
Outgoing Mail Server: smtp.gmail.com
Port: 587
Encryption: STARTTLS
Username: your.email@gmail.com
Password: [16-character App Password from Step 2]
```

**Note**: This bypasses OAuth but still routes through Gmail directly (not through NAS).

---

## Troubleshooting OAuth Errors

### Common OAuth Error Causes

1. **Outlook Version Incompatibility**
   - Outlook 2013/2010/2007: Don't support OAuth → Use App Password
   - Outlook 2016 MSI: Limited OAuth → Use App Password
   - Outlook 2016 Click-to-Run/2019/365: Support OAuth → Should work

2. **Permission Denied Previously**
   - Go to [Google Account Permissions](https://myaccount.google.com/permissions)
   - Remove "Microsoft" or "Outlook" entries
   - Try adding account again in Outlook

3. **Windows Credential Manager Issues**
   - Open Windows Credential Manager
   - Remove any Gmail/Google entries
   - Restart Outlook and try again

### Fix OAuth Consent Errors

If you see the OAuth consent page error:

1. **Clear Browser Cache**: Clear cookies for accounts.google.com
2. **Remove Existing Permissions**: 
   - Visit [Google Account Permissions](https://myaccount.google.com/permissions)
   - Remove "Microsoft" or "Outlook" entries
3. **Reset in Outlook**:
   - Remove Gmail account from Outlook
   - Close Outlook completely
   - Reopen and add account again
4. **Ensure Correct Permissions**: When OAuth prompt appears, ensure you check:
   - ✅ "Read, compose, send, and permanently delete all your email from Gmail"

---

## NAS Email Hub Integration (Advanced)

### If NAS Supports Gmail OAuth Relay

Your NAS DSM Mail Server should have these capabilities:

1. **External Mail Account Configuration**
   - Add Gmail account via OAuth2
   - Configure sync frequency
   - Set up folder mapping

2. **IMAP/SMTP Relay Service**
   - Enable IMAP service on NAS
   - Enable SMTP relay service
   - Configure authentication (local accounts or pass-through)

3. **Email Routing Rules**
   - Configure rules to route Gmail through NAS
   - Set up forwarding if needed
   - Configure spam filtering

### NAS Configuration Checklist

- [ ] NAS Mail Server application installed and running
- [ ] Gmail OAuth2 account added to NAS
- [ ] IMAP service enabled on NAS (port 143/993)
- [ ] SMTP relay service enabled on NAS (port 587/465)
- [ ] Firewall rules allow IMAP/SMTP from Outlook clients
- [ ] DNS configured for mail server (optional but recommended)
- [ ] SSL certificates configured for secure connections

---

## Recommended Approach

**For your use case (everything through NAS email hub):**

1. **Primary**: Configure NAS as email relay with Gmail OAuth
   - NAS handles OAuth complexity
   - Outlook connects to NAS with simple IMAP/SMTP
   - All traffic routes through NAS

2. **Fallback**: If NAS doesn't support Gmail OAuth relay:
   - Use App Password method
   - Configure Outlook to use Gmail directly
   - Set up NAS to forward/copy emails if needed

---

## Next Steps

1. **Check NAS Capabilities**: Verify if your NAS DSM Mail Server supports Gmail OAuth2 relay
2. **Choose Approach**: Based on NAS capabilities, choose Option 1 or Option 2
3. **Configure**: Follow the appropriate setup steps above
4. **Test**: Send test emails to verify routing through NAS

---

## References

- [Google Workspace OAuth Requirements](https://workspaceupdates.googleblog.com/2023/09/winding-down-google-sync-and-less-secure-apps-support.html)
- [Microsoft Outlook Gmail Setup](https://support.microsoft.com/en-gb/office/unable-to-add-a-gmail-account-to-classic-outlook-4d9530c5-3f40-4e6d-9b45-4477f160828f)
- [Google App Passwords Guide](https://support.google.com/accounts/answer/185833)
- [Gmail IMAP/SMTP Settings](https://support.google.com/mail/answer/78892)

---

## Support

If you need help with:
- NAS Mail Server configuration details
- Specific Outlook version compatibility
- Network/firewall configuration for NAS email hub
- Email routing rules setup

Please provide:
- NAS model and DSM version
- Outlook version (Help → About Outlook)
- Current error messages or screenshots
- Network configuration details
