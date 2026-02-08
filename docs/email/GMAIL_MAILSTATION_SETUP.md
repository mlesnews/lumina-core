# Gmail + MailStation External Mail Setup

**Date**: 1768546464.313758

```json
{
  "method": "mailstation_external_mail",
  "status": "manual_configuration_required",
  "steps": [
    {
      "step": 1,
      "action": "Access MailStation on NAS",
      "details": "Navigate to DSM \u2192 MailStation \u2192 External Mail"
    },
    {
      "step": 2,
      "action": "Add Gmail Account",
      "details": "Click 'Add External Mail Account' \u2192 Select 'Gmail'"
    },
    {
      "step": 3,
      "action": "OAuth2 Authentication",
      "details": "Click 'Authenticate with Google' \u2192 Complete OAuth2 flow"
    },
    {
      "step": 4,
      "action": "Configure Sync Settings",
      "details": "Set sync frequency, folders to sync, and retention policy"
    },
    {
      "step": 5,
      "action": "Verify Connection",
      "details": "Test connection and verify emails are syncing"
    }
  ],
  "alternative_method": {
    "description": "If MailStation doesn't support External Mail OAuth2",
    "method": "n8n_gmail_workflow",
    "steps": [
      "Use N8N Gmail OAuth2 node",
      "Create workflow to fetch Gmail emails",
      "Forward to MailStation via SMTP",
      "Store credentials in Azure Vault"
    ]
  },
  "credentials_storage": {
    "location": "Azure Vault",
    "secrets": [
      "gmail-oauth2-access-token",
      "gmail-oauth2-refresh-token",
      "gmail-oauth2-client-id",
      "gmail-oauth2-client-secret"
    ]
  }
}
```
