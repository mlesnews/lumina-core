# MailPlus Auto-Start Configuration Guide

## Overview

This guide ensures that MailPlus IMAP and SMTP services start automatically when the NAS boots, so Outlook can always connect.

---

## Quick Configuration Steps

### 1. Log into DSM
- URL: `https://10.17.17.32:5001`
- Use your NAS admin credentials

### 2. Open MailPlus Server
- **Package Center** → **Installed** → **MailPlus Server**
- Or: **Main Menu** → **MailPlus Server**

### 3. Configure IMAP Service Auto-Start

1. Go to **IMAP/POP3** tab
2. Enable **IMAP service**
3. Set configuration:
   - **Port**: `993`
   - **Encryption**: `SSL/TLS`
   - **Enable**: ✅ Checked
4. **Auto-Start Settings**:
   - Look for **"Start automatically"** or **"Auto-start"** checkbox
   - ✅ Enable it
5. Click **Apply**

### 4. Configure SMTP Service Auto-Start

1. Go to **SMTP** tab
2. Enable **SMTP service**
3. Set configuration:
   - **Port**: `587`
   - **Encryption**: `STARTTLS`
   - **Enable**: ✅ Checked
4. **Auto-Start Settings**:
   - Look for **"Start automatically"** or **"Auto-start"** checkbox
   - ✅ Enable it
5. Click **Apply**

### 5. Verify Services

1. Go to **Status** or **Overview** tab
2. Verify:
   - ✅ IMAP: **Running** on port 993
   - ✅ SMTP: **Running** on port 587
3. Both should show **"Auto-start: Enabled"** or similar

### 6. Test Auto-Start (Optional)

1. Restart NAS (or just MailPlus package)
2. After reboot, verify services start automatically
3. Check status - both IMAP and SMTP should be running

---

## Using the Automation Script

Run the auto-configuration script:

```bash
python scripts/python/ensure_mailplus_autostart.py
```

This will:
- Check current service status
- Provide configuration instructions
- Verify services are accessible

### Script Options

```bash
# Check status only
python scripts/python/ensure_mailplus_autostart.py --check

# Configure auto-start
python scripts/python/ensure_mailplus_autostart.py --configure

# Verify services are running
python scripts/python/ensure_mailplus_autostart.py --verify
```

---

## Verification

After configuration, verify services are accessible:

```powershell
# Run the status check script
powershell -File scripts/powershell/check_nas_mail_hub_status.ps1
```

Expected output:
- ✅ IMAP service (993): Accessible
- ✅ SMTP service (587): Accessible

---

## Troubleshooting

### Services Don't Start Automatically

**Problem**: Services don't start after NAS reboot

**Solutions**:
1. Check MailPlus package auto-start:
   - **Package Center** → **MailPlus Server** → **Settings**
   - Ensure **"Start automatically"** is enabled
2. Check service-level auto-start:
   - In MailPlus Server, verify IMAP/SMTP auto-start checkboxes
3. Check NAS boot sequence:
   - Some NAS models have boot order settings
   - Ensure MailPlus starts early in boot sequence

### Services Start But Stop

**Problem**: Services start but then stop

**Solutions**:
1. Check logs:
   - **MailPlus Server** → **Logs**
   - Look for errors or warnings
2. Check resources:
   - Ensure NAS has enough RAM/CPU
3. Check configuration:
   - Verify port conflicts (993, 587 not used by other services)
   - Check firewall rules

### Can't Access Services

**Problem**: Services are running but Outlook can't connect

**Solutions**:
1. Verify network:
   - Ensure you're on `10.17.17.x` network
   - Test connectivity: `ping 10.17.17.32`
2. Check firewall:
   - NAS firewall should allow ports 993 and 587
   - Windows firewall should allow Outlook connections
3. Verify credentials:
   - Username: `mlesn@homelab.lesnewski.local`
   - Password: Correct NAS Mail Hub password

---

## Configuration Files

- **Script**: `scripts/python/ensure_mailplus_autostart.py`
- **Status Check**: `scripts/powershell/check_nas_mail_hub_status.ps1`
- **Config**: `config/outlook/hybrid_email_config.json`

---

## Summary

✅ **Package Auto-Start**: Enable in Package Center  
✅ **IMAP Auto-Start**: Enable in MailPlus Server → IMAP/POP3  
✅ **SMTP Auto-Start**: Enable in MailPlus Server → SMTP  
✅ **Verify**: Run status check script after configuration  

Once configured, MailPlus services will start automatically on every NAS boot, ensuring Outlook can always connect.

---

*Last Updated: 2026-01-16*
