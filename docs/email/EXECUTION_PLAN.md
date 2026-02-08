# MailPlus Setup Execution Plan
## Based on Current Status Review

**Date**: 2026-01-11  
**Status**: Partially Complete - Ready for Execution

---

## 📊 Current Status Assessment

### ✅ Completed
1. **Email Accounts Configuration** - `config/email_accounts_aggregation.json` created
2. **n8n Workflows** - Email aggregation workflows configured
3. **Proton Bridge Configuration** - Bridge config files created
4. **Outlook Templates** - Configuration templates generated
5. **SMTP/IMAP** - Basic mail server running (MailStation)
6. **SYPHON Integration** - Configured and active

### ❌ Missing/Incomplete
1. **MailPlus Not Installed** - Currently using MailStation (basic features only)
2. **Gmail OAuth2** - Not configured in MailPlus External Mail
3. **ProtonMail Bridge** - Not integrated with MailPlus
4. **Outlook Desktop** - Not connected to MailPlus
5. **Outlook Mobile** - Not connected to MailPlus
6. **N8N Proton Bridge** - Not fully configured for localhost access

---

## 🎯 Execution Plan

### Phase 1: MailPlus Installation & Upgrade

**Current**: MailStation is running (basic mail server)  
**Target**: MailPlus (advanced features: webmail, calendar, mobile apps, OAuth2 support)

#### Steps:
1. **Check MailPlus License Availability**
   - MailPlus requires a license (free for limited users or paid)
   - Verify license status in DSM Package Center

2. **Install/Upgrade to MailPlus**
   ```bash
   # Via DSM Package Center or SSH
   synopkg install MailPlus
   synopkg start MailPlus
   ```

3. **Verify MailPlus Installation**
   - Check MailPlus Server is running
   - Verify webmail accessible at `https://10.17.17.32:5001/mailplus`
   - Test IMAP (993) and SMTP (587) ports

**Script**: `scripts/python/setup_mailplus_email_hub.py --install-mailplus`

---

### Phase 2: Gmail Configuration in MailPlus

**Goal**: Add Gmail account to MailPlus External Mail using OAuth2

#### Steps:
1. **Access MailPlus External Mail Settings**
   - DSM → MailPlus Server → Settings → External Mail
   - Or MailPlus Web Client → Settings → External Mail

2. **Add Gmail Account**
   - Click "Add Account" or "+"
   - Select "Gmail" provider
   - Complete OAuth2 flow:
     - Redirected to Google OAuth consent
     - Sign in with Gmail account
     - Grant permissions: "Read, compose, send, and permanently delete all your email from Gmail"
     - Return to MailPlus

3. **Configure Sync Settings**
   - Sync frequency: Every 15 minutes (or as needed)
   - Folders to sync: All folders or selected
   - Sync direction: Bidirectional

4. **Verify Gmail Connection**
   - Check status shows "Connected" or "Active"
   - Test sync manually
   - Verify emails appearing in MailPlus

**Manual Steps Required**: OAuth2 flow must be completed in browser

---

### Phase 3: ProtonMail Configuration in MailPlus

**Challenge**: Proton Bridge runs on localhost (127.0.0.1), MailPlus on NAS (10.17.17.32)

#### Option A: Bridge on NAS (Recommended)
1. **Install Proton Bridge on NAS**
   - If NAS supports Docker: Run Bridge in container
   - Or install Bridge directly if supported
   - Configure Bridge to listen on NAS IP instead of localhost

2. **Add ProtonMail to MailPlus External Mail**
   - External Mail → Add Account → Other
   - Server: `[NAS IP]` (where Bridge is running)
   - IMAP Port: 1143
   - SMTP Port: 1025
   - Username: Bridge-generated username
   - Password: Bridge-generated password

#### Option B: Bridge on Host PC + MailPlus Forwarding
1. **Keep Bridge on localhost** (current setup)
2. **Configure MailPlus to forward** ProtonMail emails
3. **Or use N8N** to bridge the connection (see Phase 5)

**Current Configuration**: Bridge on host PC (127.0.0.1:1143/1025)  
**Decision Needed**: Install Bridge on NAS or use N8N bridge?

**Script**: Update `config/email_accounts_aggregation.json` with chosen approach

---

### Phase 4: Outlook Desktop Configuration

**Goal**: Connect Outlook Desktop to MailPlus (not directly to Gmail/ProtonMail)

#### Steps:
1. **Get MailPlus IMAP/SMTP Settings**
   - IMAP Server: `10.17.17.32`
   - IMAP Port: `993` (SSL/TLS)
   - SMTP Server: `10.17.17.32`
   - SMTP Port: `587` (STARTTLS)
   - Username: `mlesn@homelab.lesnewski.local` (or your MailPlus email)
   - Password: MailPlus account password

2. **Add Account to Outlook Desktop**
   - File → Account Settings → Account Settings
   - New → Manual setup → POP or IMAP
   - Enter MailPlus settings (see above)
   - More Settings → Outgoing Server: Require authentication
   - Advanced: IMAP 993 (SSL), SMTP 587 (STARTTLS)
   - Test connection

3. **Verify External Mail Sync**
   - Gmail emails should appear (synced via MailPlus)
   - ProtonMail emails should appear (if configured)

**Script**: `scripts/python/configure_new_outlook_nas_email.py` (already exists)

---

### Phase 5: Outlook Mobile Configuration

**Goal**: Connect Outlook Mobile app to MailPlus

#### Steps:
1. **Open Outlook Mobile App**
2. **Add Account**
   - Get Started → Add Account
   - Advanced Setup → IMAP

3. **Enter MailPlus Settings**
   - Email: `mlesn@homelab.lesnewski.local`
   - Password: MailPlus password
   - IMAP Server: `10.17.17.32`
   - Port: `993` (SSL/TLS)
   - SMTP Server: `10.17.17.32`
   - Port: `587` (STARTTLS)

4. **Configure Sync**
   - Sync frequency: Automatic
   - Days to sync: 30 days or All
   - Enable notifications

**Manual Steps Required**: Mobile app configuration

---

### Phase 6: N8N@NAS Integration with Proton Bridge

**Goal**: Configure N8N workflows to access ProtonMail via Bridge

#### Current Setup:
- N8N running on NAS
- Proton Bridge on host PC (localhost:1143/1025)

#### Challenge:
- N8N in Docker cannot access `127.0.0.1` on host PC
- Need network path from NAS to host PC

#### Solutions:

**Option A: Use host.docker.internal (if N8N in Docker)**
```json
{
  "host": "host.docker.internal",
  "imap_port": 1143,
  "smtp_port": 1025
}
```

**Option B: Use Host PC IP Address**
```json
{
  "host": "[HOST_PC_IP]",
  "imap_port": 1143,
  "smtp_port": 1025
}
```
*Requires: Bridge configured to listen on network IP, not just localhost*

**Option C: Install Bridge on NAS**
- Run Bridge in Docker on NAS
- N8N connects to `127.0.0.1` or `localhost` (same container/host)

#### Steps:
1. **Determine N8N Deployment**
   - Check if N8N is in Docker or native
   - Get host PC IP address if needed

2. **Configure Proton Bridge Network Access** (if Option B)
   - Bridge Settings → Advanced
   - Configure to listen on network IP (not just localhost)
   - Update firewall rules

3. **Update N8N Workflow Configuration**
   - Update `config/n8n/email_aggregation_workflows.json`
   - Set correct host for Proton Bridge connection
   - Test IMAP/SMTP connections

4. **Test N8N Workflows**
   - Email Trigger (IMAP) node
   - Send Email (SMTP) node
   - Verify emails are processed

**Script**: Update `scripts/python/setup_mailplus_email_hub.py` with N8N config

---

### Phase 7: Testing & Verification

**Goal**: Verify all components working together

#### Test Checklist:
- [ ] MailPlus Server running and accessible
- [ ] Gmail OAuth2 connection active in MailPlus
- [ ] Gmail emails syncing to MailPlus
- [ ] ProtonMail Bridge accessible (from NAS or N8N)
- [ ] ProtonMail emails syncing (if configured)
- [ ] Outlook Desktop connected to MailPlus
- [ ] Outlook Desktop receiving Gmail emails
- [ ] Outlook Desktop receiving ProtonMail emails (if configured)
- [ ] Outlook Mobile connected to MailPlus
- [ ] Outlook Mobile receiving emails
- [ ] N8N workflows accessing Proton Bridge
- [ ] N8N processing emails correctly
- [ ] Email sending working from all clients

**Script**: `scripts/python/verify_email_hub_nas.py` (already exists)

---

## 🚀 Quick Start Commands

### 1. Check Current Status
```bash
python scripts/python/check_nas_email_hub_status.py
```

### 2. Install/Upgrade to MailPlus
```bash
python scripts/python/setup_mailplus_email_hub.py --install-mailplus
```

### 3. Generate Outlook Configuration
```bash
python scripts/python/setup_outlook_gmail_protonmail.py --check
```

### 4. Verify Setup
```bash
python scripts/python/verify_email_hub_nas.py
```

---

## 📋 Decision Points

### 1. MailPlus vs MailStation
- **Current**: MailStation (basic)
- **Target**: MailPlus (advanced)
- **Action**: Install MailPlus (requires license check)

### 2. Proton Bridge Location
- **Option A**: Bridge on NAS (recommended for MailPlus integration)
- **Option B**: Bridge on host PC + N8N bridge
- **Decision Needed**: Which approach?

### 3. N8N Access to Bridge
- **If Bridge on NAS**: Use `127.0.0.1` or `localhost`
- **If Bridge on Host PC**: Use `host.docker.internal` or host IP
- **Decision Needed**: N8N deployment method?

---

## 📝 Next Steps

1. **Review this plan** and confirm approach for Proton Bridge
2. **Install MailPlus** (if license available)
3. **Configure Gmail OAuth2** in MailPlus (manual OAuth flow)
4. **Configure ProtonMail** (based on Bridge location decision)
5. **Configure Outlook Desktop** (using MailPlus settings)
6. **Configure Outlook Mobile** (using MailPlus settings)
7. **Set up N8N integration** (based on Bridge location)
8. **Test and verify** all connections

---

## 🔗 Reference Documents

- **Complete Setup Guide**: `docs/email/MAILPLUS_COMPLETE_SETUP.md`
- **Quick Reference**: `docs/email/MAILPLUS_QUICK_REFERENCE.md`
- **Configuration Files**: `config/email_accounts_aggregation.json`
- **Outlook Config**: `config/outlook/outlook_accounts.json`

---

**Ready to execute!** 🚀
