# @ask Ticket Email Notifications

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#ASK` `#HELPDESK` `#EMAIL` `#NOTIFICATION` `#GMAIL` `@JARVIS` `@LUMINA`

---

## Overview

The @ask Ticket Email Notification system sends Gmail notifications to your personal Gmail account whenever tickets are created in the @ask ticket system. You'll receive detailed information about:

- **Ticket Type**: Problem, Change, Task, or General
- **Area**: What area/system the ticket is for
- **Team Assignment**: Which team is assigned
- **Individual Assignment**: Who is assigned (Analyst or Engineer)
- **Priority & Status**: Ticket priority and current status
- **Related Tickets**: Helpdesk ticket, GitLens ticket, PR numbers
- **Tags & Patterns**: All relevant tags and @SYPHON patterns

---

## Setup

### Step 1: Create Configuration File

Create `config/ticket_notifications.json`:

```json
{
  "gmail": {
    "enabled": true,
    "from_email": "user@company.local",
    "to_email": "your-gmail-test@gmail.com",
    "password": "your-nas-mailplus-password",
    "smtp_server": "10.17.17.32",
    "smtp_port": 587
  },
  "protonmail": {
    "enabled": true,
    "to_email": "your-protonmail@protonmail.com",
    "account_name": "default"
  },
  "sms": {
    "enabled": true,
    "phone_number": "+1234567890"
  }
}
```

### Step 2: Environment Variables (Alternative)

**Gmail (TEST):**
```bash
export GMAIL_TEST_EMAIL="your-gmail-test@gmail.com"
export NAS_EMAIL_PASSWORD="your-nas-mailplus-password"
export NAS_SMTP_SERVER="10.17.17.32"
export NAS_SMTP_PORT="587"
```

**ProtonMail (PRODUCTION):**
```bash
export PROTONMAIL_EMAIL="your-protonmail@protonmail.com"
export PROTONMAIL_ACCOUNT="default"
```

**SMS (PRODUCTION):**
```bash
export SMS_PHONE_NUMBER="+1234567890"
```

### Step 3: Prerequisites

- **NAS MailPlus**: Company email system configured
- **ProtonBridge**: Desktop app running with ProtonMail account configured
- **Twilio**: Account configured with credentials in Azure Key Vault

### Step 3: Test Configuration

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

---

## Email Content

### Ticket Information

- **Request ID**: Unique ticket identifier
- **Type**: Problem 🚨, Change 🔄, Task 📋, or General 📝
- **Status**: Pending, Assigned, In Progress, Resolved, Closed
- **Priority**: Critical, High, Medium, Low (color-coded)

### Assignment Details

- **Area**: System/area the ticket is for (e.g., "APICLI Endpoints", "Standardization")
- **Team**: Assigned team (e.g., "JARVIS_TEAM")
- **Individual**: Assigned person
- **Role**: Analyst or Engineer (auto-detected)

### Ticket Details

- **@ask Text**: Original @ask directive
- **Description**: Expanded description
- **Related Tickets**: Helpdesk, GitLens ticket, PR numbers
- **Tags**: All @tags and #tags
- **@SYPHON Patterns**: Extracted patterns

---

## Integration

### Automatic Notifications

Email notifications are **automatically sent** when:
- New @ask tickets are created via `collate_ask()`
- Tickets are created through the helpdesk system
- Change management tickets are created

### Integration Points

- **@ask Ticket Collation System**: Sends email on ticket creation
- **Helpdesk System**: Integrated with ticket workflow
- **Change Management**: Notifies on change tickets

---

## Ticket Type Detection

### Problem Tickets 🚨

Detected by keywords: error, bug, fix, issue, problem, broken, fail

### Change Tickets 🔄

Detected by keywords: change, update, modify, implement, create, add

### Task Tickets 📋

Detected by keywords: task, todo, work, do

### General Tickets 📝

Default for other tickets

---

## Area Detection

Areas are determined from tags and team assignments:

- **APICLI** → "APICLI Endpoints"
- **Standardization** → "Standardization & Modularization"
- **Ask Ticket** → "Ask Ticket System"
- **V3** → "V3 Verification"
- **Health Check** → "Health & Welfare"
- And more...

---

## Role Detection

### Engineer

- Keywords: engineer, dev, developer, programmer
- Problem/Change tickets default to Engineer

### Analyst

- Keywords: analyst, business
- Task/General tickets default to Analyst

---

## Usage

### Test Email Configuration

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

### Manual Notification

```python
from ask_ticket_collation_system import AskTicketCollationSystem
from ask_ticket_email_notifier import AskTicketEmailNotifier

# Create ticket
collation = AskTicketCollationSystem()
ticket = collation.collate_ask(
    ask_id="...",
    ask_text="@ask @jarvis fix API endpoint"
)

# Email is automatically sent, or manually:
notifier = AskTicketEmailNotifier()
notifier.send_ticket_notification(ticket)
```

---

## Email Format

### HTML Email

- Professional HTML formatting
- Color-coded priority badges
- Status indicators
- Responsive design
- Mobile-friendly

### Subject Line

Format: `[EMOJI] New [TYPE] Ticket: [AREA] - [ID]`

Examples:
- `🚨 New Problem Ticket: APICLI Endpoints - a8139a79`
- `🔄 New Change Ticket: Standardization - 018b80ba`
- `📋 New Task Ticket: Health & Welfare - 03520f08`

---

## Security

### Channel Security

- **Gmail (TEST)**: Company email via NAS MailPlus - internal network only
- **ProtonMail (PRODUCTION)**: End-to-end encrypted via ProtonBridge - maximum security
- **SMS (PRODUCTION)**: Twilio secure messaging - production alerts

### Configuration Security

- Store credentials in `config/ticket_notifications.json` (not in git)
- Use environment variables for sensitive data
- Keep all passwords and API keys secure
- ProtonMail credentials managed via ProtonBridge (local)
- Twilio credentials stored in Azure Key Vault

---

## Troubleshooting

### Notifications Not Sending

**Gmail (TEST):**
1. Check NAS MailPlus credentials
2. Verify NAS (10.17.17.32) is accessible
3. Check SMTP port 587 is open

**ProtonMail (PRODUCTION):**
1. Ensure ProtonBridge desktop app is running
2. Verify ProtonMail account is configured in ProtonBridge
3. Check ProtonBridge IMAP/SMTP ports (1143/1025)

**SMS (PRODUCTION):**
1. Verify Twilio credentials in Azure Key Vault
2. Check Twilio account is active
3. Verify phone number format (+1234567890)

### Testing

Run test command:
```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

This tests all three channels and reports results.

### Common Issues

- **"Authentication failed"**: Wrong credentials
- **"Connection refused"**: Service not running or firewall blocking
- **"ProtonBridge not available"**: ProtonBridge desktop app not running
- **"Twilio not available"**: Twilio credentials not in Azure Key Vault

---

## Status

✅ **ACTIVE** - Email notification system operational

**Features**:
1. ✅ Automatic email notifications on ticket creation
2. ✅ Detailed ticket information
3. ✅ Area, team, individual assignment details
4. ✅ Ticket type detection
5. ✅ Role detection (Analyst/Engineer)
6. ✅ HTML email formatting
7. ✅ Gmail integration

---

**Tags**: `#ASK` `#HELPDESK` `#EMAIL` `#NOTIFICATION` `#NAS` `#MAILPLUS` `#COMPANY_EMAIL` `@JARVIS` `@LUMINA` `#PEAK`
