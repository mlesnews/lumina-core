# NAS Company Email Hub Setup - 2 Employees

**Date**: 2026-01-03  
**Status**: ✅ **READY TO SETUP**  
**Tag**: @JARVIS @MARVIN @NAS @EMAIL

---

## Perfect Fit: MailPlus with Free Licenses

**Your Situation:**
- ✅ 2 human employees
- ✅ 5 free MailPlus licenses included with Synology NAS
- ✅ **Cost: $0** (well within free license limit)
- ✅ 3 licenses remaining for future growth

**Recommendation: MailPlus** - Full enterprise features at zero cost!

---

## MailPlus vs MailStation Comparison

### MailPlus (Recommended) ✅
- **Cost**: $0 (5 free licenses)
- **Webmail**: ✅ Yes
- **Mobile Apps**: ✅ iOS & Android
- **Calendar**: ✅ Yes
- **Contacts**: ✅ Yes
- **Advanced Filtering**: ✅ Yes
- **Anti-spam/Anti-virus**: ✅ Yes
- **Email Archiving**: ✅ Yes
- **Backup**: ✅ Yes

### MailStation (Alternative)
- **Cost**: $0
- **Webmail**: ❌ No
- **Mobile Apps**: ❌ No
- **Calendar**: ❌ No
- **Contacts**: ❌ No
- **Advanced Filtering**: ❌ Basic only
- **Anti-spam/Anti-virus**: ❌ No
- **Email Archiving**: ❌ No
- **Backup**: ❌ No

---

## Setup Steps

### 1. Install MailPlus

```bash
# Via SSH to NAS
ssh admin@10.17.17.32

# Install MailPlus
synopkg install MailPlus
synopkg start MailPlus
```

Or via DSM Package Center:
1. Open DSM → Package Center
2. Search "MailPlus"
3. Install MailPlus Server
4. Start the package

### 2. Configure Email Domain

1. Open MailPlus Server in DSM
2. Configure your email domain (e.g., `company.local` or your actual domain)
3. Set up SMTP/IMAP ports
4. Configure DNS records if using external domain

### 3. Create Email Accounts

Create 2 email accounts (one for each employee):
- `employee1@company.local`
- `employee2@company.local`

You have 3 more licenses available for:
- Shared mailboxes
- Distribution lists
- Future employees
- Service accounts

### 4. Configure n8n Integration

The n8n workflows are already configured in:
- `config/n8n/nas_dsm_email_hub_expansion.json`

Workflows ready:
- ✅ Email send (SMTP)
- ✅ Email receive (IMAP)
- ✅ Email management
- ✅ Email monitoring

### 5. Configure SYPHON Integration

SYPHON integration is ready:
- `scripts/python/syphon_nas_dsm_mail_integration.py`

This will extract intelligence from all emails automatically.

---

## Quick Setup Script

Run the automated setup:

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python nas_dsm_mail_server_setup.py
```

This will:
1. ✅ Check for MailPlus installation
2. ✅ Install MailPlus if needed
3. ✅ Configure email server
4. ✅ Set up email accounts
5. ✅ Configure n8n workflows
6. ✅ Set up SYPHON integration

---

## Cost Breakdown

### Current Setup (2 Employees)
- **MailPlus Licenses**: 5 free (included with NAS)
- **Accounts Used**: 2
- **Accounts Remaining**: 3
- **Additional Cost**: $0

### Future Growth Scenarios

**If you grow to 6-10 employees:**
- Need: 5 more licenses
- Cost: ~$250 (one-time, perpetual)
- Total Cost: $250

**If you grow to 11-25 employees:**
- Need: 20 more licenses
- Cost: ~$1,070 (one-time, perpetual)
- Total Cost: $1,070

**Note**: Licenses are perpetual - buy once, use forever (even if you upgrade NAS)

---

## Features You Get (Free!)

### Webmail Interface
- Access email from any browser
- Modern, responsive design
- Works on desktop, tablet, mobile browsers

### Mobile Apps
- **iOS App**: Available on App Store
- **Android App**: Available on Google Play
- Push notifications
- Offline access
- Full calendar and contacts sync

### Calendar Integration
- Shared calendars
- Meeting scheduling
- Calendar sync to mobile devices
- Integration with email

### Contact Management
- Shared address book
- Contact sync across devices
- Integration with email and calendar

### Advanced Features
- Email filtering rules
- Auto-forwarding
- Email aliases
- Distribution lists
- Anti-spam protection
- Anti-virus scanning
- Email archiving
- Email backup

---

## Integration Points

### Already Configured ✅

1. **n8n Workflows**
   - Email send/receive automation
   - Email processing workflows
   - Integration with JARVIS/SYPHON

2. **SYPHON Intelligence Extraction**
   - Automatic email intelligence extraction
   - Actionable items, tasks, decisions
   - Cross-platform correlation

3. **Azure Key Vault**
   - Secure credential storage
   - SMTP/IMAP credentials
   - API keys

4. **JARVIS Integration**
   - Email notifications
   - Email processing coordination
   - Automated responses

---

## Next Steps

1. **Install MailPlus** (if not already installed)
   ```bash
   python scripts/python/check_nas_email_hub_status.py
   ```

2. **Run Setup Script**
   ```bash
   python nas_dsm_mail_server_setup.py
   ```

3. **Verify Setup**
   ```bash
   python scripts/python/check_nas_email_hub_status.py
   ```

4. **Create Email Accounts**
   - Via DSM MailPlus interface
   - Or via API/script

5. **Test Email Hub**
   - Send test email
   - Receive test email
   - Verify SYPHON extraction
   - Check n8n workflows

---

## Summary

✅ **Perfect Setup for 2 Employees**
- MailPlus: $0 (5 free licenses)
- Full enterprise features
- Room to grow (3 more accounts)
- All integrations ready
- Zero additional cost

**Recommendation**: Install MailPlus and enjoy full-featured email hub at no cost!

---

**Last Updated**: 2026-01-03  
**Maintained By**: @JARVIS @MARVIN
