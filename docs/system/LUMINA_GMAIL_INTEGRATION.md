# LUMINA Gmail Integration System

**Status**: ✅ **COMPLETE**  
**Tags**: `#JARVIS` `#LUMINA` `#GMAIL` `#ADMIN` `#HOLOCRON` `#JEDIARCHIVES`

---

## Overview

Direct LUMINA<>GOOGLE Gmail integration system for search, filtering, and email management. Integrated with Admin SME job slot and Holocron/Jedi Archives for comprehensive email organization.

**Based on**: HVAC Bid Search System template

---

## System Components

### 1. Core Gmail Integration (`lumina_gmail_integration.py`)

**Features**:
- Direct Gmail API integration
- Advanced search and filtering
- Email categorization (auto)
- Priority determination (auto)
- Holocron/Jedi Archives sync
- Send/receive email workflows

**Key Classes**:
- `LUMINAGmailIntegration` - Main integration class
- `EmailCategory` - Email categorization enum
- `EmailPriority` - Priority levels enum
- `EmailMetadata` - Email metadata structure

### 2. Admin SME Job Slot (`config/admin_sme_job_slot.json`)

**Role**: Administrative Subject Matter Expert

**Responsibilities**:
1. **Email Sending**
   - Compose and send emails
   - Attach files
   - Schedule emails
   - Track sent emails

2. **Email Receiving**
   - Process incoming emails
   - Auto-categorize
   - Assign priorities
   - Extract action items

3. **Email Organization**
   - Categorize emails
   - Tag emails
   - Archive emails
   - Organize into folders

4. **Jedi Archives Integration**
   - Sync to Holocron
   - Create archive entries
   - Link emails to references
   - Extract knowledge

### 3. Secretarial Workflows (`admin_sme_secretarial_workflows.py`)

**Incoming Email Workflow**:
1. Receive email
2. Auto-categorize (Admin SME rules)
3. Determine priority
4. Extract tags
5. Check for action items
6. Save to Holocron/Jedi Archives
7. Notify if action required

**Outgoing Email Workflow**:
1. Compose email
2. Validate recipient
3. Attach files if needed
4. Send email
5. Track sent email
6. Set follow-up reminder if needed
7. Archive sent email

**Categorization Workflow**:
- Auto-categorization based on content
- Tag assignment
- Folder organization
- Archive management

---

## Email Categories

- **ADMINISTRATIVE** - General administrative emails
- **FINANCIAL** - Invoices, payments, bills, budgets
- **TECHNICAL** - Code, bugs, system issues
- **PERSONAL** - Personal correspondence
- **PROJECT** - Project-related emails
- **REFERENCE** - Reference documents
- **ARCHIVE** - Archived emails
- **ACTION_REQUIRED** - Emails requiring action
- **FOLLOW_UP** - Emails needing follow-up
- **JEDI_ARCHIVES** - Emails in Jedi Archives/Holocron

---

## Email Priorities

- **CRITICAL** - Urgent, emergency, immediate action
- **HIGH** - Important, priority, attention needed
- **MEDIUM** - Standard priority (default)
- **LOW** - Newsletters, notifications, digests
- **ARCHIVE** - Archived, no action needed

---

## Holocron/Jedi Archives Integration

### Auto-Sync
- Emails automatically synced to Holocron
- Organized by category in `data/holocron/emails/`
- Also saved to Jedi Archives in `data/jedi_archives/emails/`

### Metadata Included
- Email ID and thread ID
- Subject, from, to, date
- Category and priority
- Tags
- Action required status
- Admin notes
- Follow-up dates

### Organization
- By category (default)
- By date (optional)
- By project (optional)
- Search indexing enabled

---

## Search and Filtering

### Advanced Search Features
- Full text search
- Date range filtering
- Category filtering
- Priority filtering
- Tag filtering
- Attachment filtering
- Sender filtering

### Filter Presets

**Action Required**:
```
action_required:true OR priority:critical OR priority:high
```

**Financial**:
```
category:financial
```

**Project Related**:
```
category:project OR tags:#LUMINA OR tags:#JARVIS
```

**Jedi Archives**:
```
category:jedi_archives OR holocron_reference:*
```

---

## Usage Examples

### Process Incoming Emails
```bash
python scripts/python/admin_sme_secretarial_workflows.py --process-incoming
```

### Organize Emails
```bash
python scripts/python/admin_sme_secretarial_workflows.py --organize
```

### Sync to Holocron
```bash
python scripts/python/admin_sme_secretarial_workflows.py --sync-holocron
```

### Search Emails
```bash
python scripts/python/admin_sme_secretarial_workflows.py \
  --search "from:contractor@email.com" \
  --category financial \
  --priority high
```

### Send Email
```python
from lumina_gmail_integration import LUMINAGmailIntegration

integration = LUMINAGmailIntegration(project_root)
result = integration.send_email(
    to="recipient@email.com",
    subject="Subject",
    body="Email body"
)
```

### Search Gmail
```python
emails = integration.search_emails(
    query="from:contractor@email.com subject:bid has:attachment",
    max_results=50
)
```

---

## Configuration

### Admin SME Config
Location: `config/admin_sme_job_slot.json`

### Gmail Integration Config
Location: `data/gmail_integration/admin_sme_config.json`

### Gmail API Credentials
Location: `config/gmail_credentials.json` (OAuth2)
Location: `config/gmail_token.pickle` (auto-generated)

---

## Integration Points

### With JARVIS
- Email automation workflows
- Action item extraction
- Priority management

### With Holocron
- Email archiving
- Knowledge extraction
- Reference linking

### With Jedi Archives
- Long-term storage
- Search indexing
- Project organization

### With n8n
- Workflow automation
- Email triggers
- Scheduled processing

---

## File Structure

```
data/
├── gmail_integration/
│   ├── metadata/          # Email metadata
│   ├── sent_emails/       # Sent email tracking
│   └── follow_up_reminders/  # Follow-up reminders
├── holocron/
│   └── emails/            # Holocron email archive
│       ├── administrative/
│       ├── financial/
│       ├── technical/
│       └── ...
└── jedi_archives/
    └── emails/            # Jedi Archives email storage
        ├── administrative/
        ├── financial/
        └── ...

config/
├── admin_sme_job_slot.json    # Admin SME configuration
└── gmail_credentials.json     # Gmail OAuth2 credentials
```

---

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. **Set Up Gmail OAuth2**:
   - Go to Google Cloud Console
   - Create OAuth2 credentials
   - Download to `config/gmail_credentials.json`
   - Run integration to authenticate (first time)

3. **Configure Admin SME**:
   - Edit `config/admin_sme_job_slot.json`
   - Adjust workflows and permissions as needed

4. **Test Integration**:
   ```bash
   python scripts/python/lumina_gmail_integration.py --search "in:inbox"
   ```

---

## Status

✅ **Core Integration** - Complete  
✅ **Admin SME Job Slot** - Complete  
✅ **Secretarial Workflows** - Complete  
✅ **Holocron Integration** - Complete  
✅ **Jedi Archives Integration** - Complete  
✅ **Search and Filtering** - Complete  

---

**Tags**: `#JARVIS` `#LUMINA` `#GMAIL` `#ADMIN` `#HOLOCRON` `#JEDIARCHIVES` `@LUMINA`
