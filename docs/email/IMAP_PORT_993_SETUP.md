# MailStation IMAP Port 993 Configuration

**Date**: 1768546464.313758

```json
{
  "current_status": "port_993_closed",
  "required_action": "enable_imap_service",
  "steps": [
    {
      "step": 1,
      "action": "Access MailStation Settings",
      "details": "DSM \u2192 MailStation \u2192 Settings \u2192 Mail Service"
    },
    {
      "step": 2,
      "action": "Enable IMAP Service",
      "details": "Check 'Enable IMAP service' checkbox"
    },
    {
      "step": 3,
      "action": "Configure IMAP Port",
      "details": "Set IMAP port to 993 (SSL/TLS)"
    },
    {
      "step": 4,
      "action": "Configure SSL/TLS",
      "details": "Enable SSL/TLS encryption for IMAP"
    },
    {
      "step": 5,
      "action": "Firewall Configuration",
      "details": "Ensure port 993 is open in DSM Firewall"
    },
    {
      "step": 6,
      "action": "Verify Port",
      "details": "Run: python scripts/python/verify_complete_email_setup.py"
    }
  ],
  "verification": {
    "script": "scripts/python/verify_complete_email_setup.py",
    "expected_result": "IMAP port 993: \u2705 Open"
  },
  "troubleshooting": {
    "port_still_closed": [
      "Check MailStation service is running",
      "Verify firewall rules allow port 993",
      "Check for port conflicts",
      "Review MailStation logs"
    ]
  }
}
```
