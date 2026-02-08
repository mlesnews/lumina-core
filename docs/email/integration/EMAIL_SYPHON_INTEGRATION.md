# Email Syphoning Integration
## NAS Company Mail Hub Integration

## Overview

Email syphoning has been integrated into the daily work cycle system. All emails from all accounts are syphoned via NAS Company Mail Hub.

## What Was Integrated

### ✅ Email Source Added to Daily Work Cycle

**Configuration:**
- **Enabled**: Yes
- **Scan Interval**: 60 minutes
- **Estimated Duration**: 30-120 seconds (depends on email volume)
- **Method**: NAS Company Mail Hub (MailPlus/DSM)

### ✅ Integration Points

1. **Daily Work Cycle** - Email syphoning runs as part of daily cycle
2. **NAS Mail Hub** - Uses NAS Company Mail Hub (10.17.17.32)
3. **All Accounts** - Syphons all configured email accounts
4. **Learning Extraction** - Extracts learnings from emails
5. **Storage** - Saves to Holocron and R5

## How It Works

### Connection Methods (in order of preference)

1. **IMAP via NAS Mail Hub** (Primary)
   - Connects to NAS Mail Hub via IMAP (port 993)
   - Fetches emails from last 30 days
   - Processes up to 100 emails per account (for performance)

2. **MailPlus API** (Fallback)
   - Uses NAS MailPlus API if available
   - Requires API credentials

3. **Existing Email Syphon System** (Fallback)
   - Falls back to existing email syphon scripts
   - Uses `syphon_all_emails_to_holocron_youtube`

### Email Processing

For each email:
1. **Parse** - Extract subject, from, to, body, date
2. **Extract Learnings** - Analyze content for insights
3. **Store** - Save to `data/email_syphon/`
4. **Update Holocron** - Add to knowledge base
5. **Update R5** - Add to living context matrix

## Performance Estimates

### Daily Work Cycle Duration

**Without Email**:
- Current: ~12-15 seconds
- With optimizations: ~10-12 seconds

**With Email Syphoning**:
- **Small volume** (10-50 emails/day): +30-60 seconds = **~45-75 seconds total**
- **Medium volume** (50-200 emails/day): +60-90 seconds = **~75-105 seconds total**
- **Large volume** (200+ emails/day): +90-120 seconds = **~105-135 seconds total**

### Per Account Estimates

**Small Account** (10-20 emails/day):
- Connection: 2-3 seconds
- Fetch: 3-5 seconds
- Process: 5-10 seconds
- **Total**: ~10-18 seconds per account

**Medium Account** (50-100 emails/day):
- Connection: 2-3 seconds
- Fetch: 10-15 seconds
- Process: 15-30 seconds
- **Total**: ~27-48 seconds per account

**Large Account** (200+ emails/day):
- Connection: 2-3 seconds
- Fetch: 20-30 seconds
- Process: 30-60 seconds
- **Total**: ~52-93 seconds per account

### Multiple Accounts

- **3 Accounts**: ~30-90 seconds
- **5 Accounts**: ~60-150 seconds
- **10 Accounts**: ~120-300 seconds (2-5 minutes)

## Configuration

### Email Accounts

Accounts are loaded from:
1. `config/email_accounts.json` (if exists)
2. Azure Key Vault (if available)
3. NAS Mail Hub default (fallback)

### NAS Mail Hub Settings

- **IP**: 10.17.17.32
- **Port**: 993 (IMAP SSL) or 143 (IMAP)
- **Web Interface**: http://10.17.17.32:5001
- **Type**: MailPlus/DSM Mail Server

## Usage

### Automatic (Daily Work Cycle)

Email syphoning runs automatically as part of daily work cycle:

```powershell
python scripts/python/daily_work_cycle_complete.py --run-cycle
```

### Manual Email Syphon Only

```powershell
python scripts/python/jarvis_syphon_all_emails_nas_hub.py
```

## What Gets Syphoned

### Email Data Extracted

- Subject
- From/To addresses
- Date/Time
- Body content
- Attachments (metadata)
- Headers

### Learnings Extracted

- Key topics/themes
- Important information
- Action items
- Insights
- Patterns

### Storage Locations

- `data/email_syphon/` - Raw email data
- `data/holocron/` - Knowledge base entries
- `data/r5_living_matrix/` - Living context entries

## Integration with Daily Cycle

### Report Includes

- Total emails syphoned
- Accounts processed
- Learnings extracted
- Duration per account
- Errors (if any)

### Example Report Entry

```json
{
  "source_name": "email",
  "source_type": "email",
  "items_found": 150,
  "items_processed": 150,
  "items_new": 150,
  "learnings": [
    "Syphoned 150 emails from 3 accounts",
    "Extracted 25 learnings from emails",
    "Duration: 45.3 seconds"
  ],
  "metadata": {
    "accounts_processed": 3,
    "total_learnings": 25,
    "duration_seconds": 45.3,
    "accounts": [
      {
        "account": "Gmail",
        "emails": 75,
        "learnings": 12
      },
      {
        "account": "Outlook",
        "emails": 50,
        "learnings": 8
      },
      {
        "account": "ProtonMail",
        "emails": 25,
        "learnings": 5
      }
    ]
  }
}
```

## Performance Optimization

### Current Optimizations

- Limits to last 100 emails per account (for performance)
- Processes in batches
- Caches connection
- Parallel processing (future)

### Future Optimizations

- Incremental sync (only new emails)
- Async processing
- Background processing
- Smart caching

## Troubleshooting

### No Emails Found

1. Check NAS Mail Hub connection:
   ```powershell
   python scripts/python/check_nas_email_hub_status.py
   ```

2. Verify credentials in Azure Key Vault or config

3. Check IMAP port (993 for SSL, 143 for non-SSL)

### Slow Performance

1. Reduce email limit (currently 100 per account)
2. Reduce days (currently 30, try 7)
3. Process in background
4. Use incremental sync

## Tags

#EMAIL #SYPHON #NAS #MAIL_HUB #DAILY_CYCLE #INTEGRATION @JARVIS @LUMINA
