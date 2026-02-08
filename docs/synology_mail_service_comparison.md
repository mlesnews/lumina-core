# Synology Mail Service Comparison

## The Two Options

### 1. Mail Station / Synology Mail Server (Legacy)
- **Status**: End-of-life April 8, 2026
- **Support**: No new updates after EOL
- **Cost**: Free (included)
- **Features**: Basic IMAP/SMTP, simple webmail
- **Security**: Basic SSL/TLS, minimal anti-spam

### 2. MailPlus / MailPlus Server (Current) ✅
- **Status**: Actively supported, future-proof
- **Support**: Regular updates, DSM 7.3+ compatible
- **Cost**: 5 free licenses, then paid packs
- **Features**: Advanced security, modern UI, mobile apps
- **Security**: Rspamd anti-spam, ClamAV, DKIM/SPF/DMARC

---

## Recommendation: **MailPlus Server** ✅

**Why MailPlus Server is better for your setup:**

### ✅ **Future-Proof**
- Mail Station ends support in April 2026
- MailPlus is actively developed
- Compatible with current and future DSM versions

### ✅ **Better Security**
- Advanced anti-spam (Rspamd with auto-learning)
- ClamAV + optional McAfee antivirus
- Full DKIM/SPF/DMARC/DANE support
- Better for company email

### ✅ **Better Features**
- Modern web interface
- Mobile apps (iOS/Android)
- Calendar and contacts integration
- Shared mailboxes
- AI-assisted features
- Better for Outlook integration

### ✅ **Your Current Setup**
- **Already configured**: Your config shows MailPlus Server
- **Webmail URL**: `https://10.17.17.32:5001/mailplus` (MailPlus)
- **Watchdog monitoring**: Already set up for MailPlus
- **Auto-start scripts**: Configured for MailPlus

---

## Current Configuration

**You're using**: **MailPlus Server** ✅

**Evidence:**
- Webmail: `https://10.17.17.32:5001/mailplus`
- Scripts reference: `synopkg status MailPlus`
- Configuration: MailPlus Server settings
- Watchdog: Monitoring MailPlus services

---

## Migration (If Needed)

If you were using Mail Station, you'd need to migrate. But since you're already on MailPlus Server, you're all set!

---

## Summary

**Use MailPlus Server** - It's what you have, it's what's supported, and it's the better option for:
- ✅ Company email reliability
- ✅ Security and anti-spam
- ✅ Outlook integration
- ✅ Future updates
- ✅ Modern features

**Don't use Mail Station** - It's being phased out and lacks modern features.

---

*You're already on the right choice: MailPlus Server!* ✅
