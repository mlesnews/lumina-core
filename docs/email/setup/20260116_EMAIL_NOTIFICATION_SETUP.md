# Gmail Email Notification Setup - Quick Start

**Status**: ✅ **READY**  
**Date**: 2026-01-12  

---

## Quick Setup

### 1. Configure NAS MailPlus Company Email

The system uses **NAS MailPlus** company email to send to your Gmail.

**Company Email**: `user@company.local` (configure via `NAS_EMAIL_FROM` environment variable)  
**NAS SMTP**: `YOUR_NAS_IP:587` (configure via `NAS_SMTP_SERVER` environment variable)

### 2. Configure

**Option A: Environment Variables** (Recommended)
```bash
export NAS_EMAIL_FROM="user@company.local"
export NAS_EMAIL_TO="your-gmail@gmail.com"
export NAS_EMAIL_PASSWORD="your-nas-mailplus-password"
export NAS_SMTP_SERVER="10.17.17.32"
export NAS_SMTP_PORT="587"
```

**Option B: Config File**
```bash
cp config/nas_email_notifications.json.example config/nas_email_notifications.json
# Edit config/nas_email_notifications.json with your credentials
```

### 3. Test

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

---

## What You'll Receive

When any ticket is created (problem, change, task), you'll get an email with:

✅ **Ticket Type** - Problem 🚨, Change 🔄, Task 📋, or General 📝  
✅ **Area** - What system/area (e.g., "APICLI Endpoints", "Standardization")  
✅ **Team** - Which team is assigned  
✅ **Individual** - Who is assigned  
✅ **Role** - Analyst or Engineer  
✅ **Priority** - Critical, High, Medium, Low  
✅ **Status** - Current ticket status  
✅ **Related Tickets** - Helpdesk, GitLens ticket, PR numbers  
✅ **Tags & Patterns** - All relevant information  

---

## Automatic Notifications

Emails are **automatically sent** when:
- New @ask tickets are created
- Change management tickets are created
- Helpdesk tickets are created

No action needed - it just works! 📧

---

**Tags**: `#EMAIL` `#NOTIFICATION` `#NAS` `#MAILPLUS` `#COMPANY_EMAIL` `#ASK` `#HELPDESK` `@JARVIS` `@LUMINA`
