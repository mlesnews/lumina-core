# EWTN Weekly Automation Setup

## Overview

Automated weekly system for EWTN engagement tracking:
- **Status Query**: Check current engagement status
- **Report Generation**: Generate weekly status reports
- **AI/JARVIS Validation**: Request validation and reevaluation

## Quick Start

### Manual Run

```bash
# Complete weekly check
python scripts/python/ewtn_weekly_automation.py

# With JARVIS integration
python scripts/python/ewtn_weekly_automation.py --send-to-jarvis
```

### Individual Commands

```bash
# Check status
python scripts/python/ewtn_engagement_tracker.py --status

# Generate report
python scripts/python/ewtn_engagement_tracker.py --report

# Generate validation questions
python scripts/python/ewtn_engagement_tracker.py --validate

# Complete weekly check
python scripts/python/ewtn_engagement_tracker.py --weekly-check
```

## Scheduled Automation

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Name: "EWTN Weekly Engagement Check"
4. Trigger: Weekly (every Monday at 9:00 AM)
5. Action: Start a program
6. Program: `python`
7. Arguments: `scripts/python/ewtn_weekly_automation.py --send-to-jarvis`
8. Start in: `[project_root]`

### Linux/Mac Cron

Add to crontab (`crontab -e`):

```bash
# EWTN Weekly Engagement Check - Every Monday at 9:00 AM
0 9 * * 1 cd /path/to/project && python scripts/python/ewtn_weekly_automation.py --send-to-jarvis >> logs/ewtn_weekly.log 2>&1
```

### PowerShell Scheduled Task (Windows)

```powershell
$action = New-ScheduledTaskAction -Execute "python" -Argument "scripts/python/ewtn_weekly_automation.py --send-to-jarvis" -WorkingDirectory "C:\path\to\project"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 9am
Register-ScheduledTask -TaskName "EWTN Weekly Check" -Action $action -Trigger $trigger
```

## What It Does

### 1. Status Query
- Checks current engagement phase
- Calculates days since last contact
- Determines if follow-up is needed
- Reviews recent activity

### 2. Report Generation
- Generates comprehensive weekly report
- Saves to `data/ewtn_engagement/reports/weekly_report_YYYYMMDD.md`
- Includes:
  - Current status
  - Timeline information
  - Recent activity
  - Next steps recommendations

### 3. AI/JARVIS Validation
- Generates validation questions:
  - **Status Review**: Is our approach appropriate?
  - **Next Steps Validation**: Are recommended steps correct?
  - **Strategy Validation**: Is our overall strategy sound?
- Saves questions to JSON file
- Optionally sends to JARVIS for validation

## Status Tracking

### Phases
- `initial_contact` - Initial outreach
- `proposal_sent` - Proposal submitted
- `awaiting_response` - Waiting for EWTN response
- `meeting_scheduled` - Meeting arranged
- `partnership_discussion` - Discussing partnership
- `agreement_negotiation` - Negotiating terms
- `partnership_active` - Partnership active
- `on_hold` - Temporarily paused
- `declined` - Partnership declined

### Updating Status

```bash
# Update phase
python scripts/python/ewtn_engagement_tracker.py --update-phase "proposal_sent"

# Add note
python scripts/python/ewtn_engagement_tracker.py --add-note "Sent proposal via email"

# Record action
python scripts/python/ewtn_engagement_tracker.py --add-action "Followed up with phone call"

# Mark response received
python scripts/python/ewtn_engagement_tracker.py --response-received

# Mark meeting scheduled
python scripts/python/ewtn_engagement_tracker.py --meeting-scheduled
```

## Validation Questions

The system automatically generates three types of validation questions:

### 1. Status Review
- Reviews current engagement status
- Validates approach appropriateness
- Suggests strategy adjustments

### 2. Next Steps Validation
- Validates recommended next steps
- Provides additional recommendations
- Ensures actions are appropriate

### 3. Strategy Validation
- Reviews overall engagement strategy
- Validates three-part offer
- Suggests adjustments if needed

## Reports Location

All reports are saved to:
```
data/ewtn_engagement/
  ├── engagement_status.json      # Current status
  ├── validation_requests.json    # Validation requests
  └── reports/
      ├── weekly_report_YYYYMMDD.md
      └── validation_questions_YYYYMMDD.json
```

## Integration with JARVIS

To enable JARVIS integration:

1. Ensure JARVIS system is available
2. Use `--send-to-jarvis` flag
3. Validation questions will be sent to JARVIS
4. Responses will be logged

## Example Output

```
=== EWTN Engagement Weekly Status Report ===
Generated: January 28, 2025 at 09:00 AM

CURRENT STATUS:
  Phase: Proposal Sent
  Partnership Status: Pending
  Contact Count: 1
  Response Received: No
  Meeting Scheduled: No

TIMELINE:
  Last Contact: 2025-01-21T10:00:00
  Days Since Last Contact: 7
  Last Response: None
  Next Follow-up: 2025-01-28T10:00:00
  Days Until Follow-up: 0

NEXT STEPS:
  1. Send follow-up email (1 week since proposal)
  2. Consider phone follow-up
```

## Troubleshooting

### Reports Not Generating
- Check data directory permissions
- Verify project root path
- Check logs for errors

### JARVIS Integration Not Working
- Verify JARVIS system is available
- Check import paths
- Review JARVIS integration code

### Status Not Updating
- Check file permissions
- Verify JSON file format
- Review error logs

## Next Steps

1. Set up scheduled automation
2. Run initial weekly check
3. Review generated reports
4. Send validation questions to JARVIS
5. Update status as engagement progresses

---

**Automation ensures consistent follow-up and validation for EWTN engagement.**
