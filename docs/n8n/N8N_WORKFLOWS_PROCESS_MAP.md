# N8N Workflows Process Map

**Total Workflows**: 14

## Integrations

### 11Labs
- 11labs_phone_11labs_incoming
- 11labs_phone_11labs_outgoing
- 11labs_sms_11labs_incoming

### SYPHON
- 11labs_phone_11labs_incoming
- 11labs_sms_11labs_incoming
- hvac_syphon_monitor_workflow
- proton_bridge_workflow
- sms_syphon_workflow

### Twilio
- 11labs_phone_11labs_outgoing

### Gmail
- hvac_bid_gmail_search_workflow
- hvac_syphon_monitor_workflow
- lumina_gmail_integration_workflow

### Holocron
- lumina_gmail_integration_workflow
- sms_syphon_workflow

### ProtonMail
- proton_bridge_workflow

## Webhooks

- **Twilio Webhook**: `phone/11labs` (POST)
- **Webhook**: `sms/11labs` (POST)
- **Webhook - Search Request**: `hvac-bid-search` (POST)
- **Respond to Webhook**: `` (POST)
- **Webhook**: `syphon/sms` (POST)

## Workflow Details

### Incoming Call → 11Labs Voice AI
**File**: `11labs_phone_11labs_incoming.json`

**Nodes**: 4
**Integrations**: 11Labs, SYPHON

**Triggers**:
- Twilio Webhook (n8n-nodes-base.webhook)

### Outgoing Call → 11Labs Voice
**File**: `11labs_phone_11labs_outgoing.json`

**Nodes**: 3
**Integrations**: Twilio, 11Labs

### SMS → 11Labs Voice → Notification
**File**: `11labs_sms_11labs_incoming.json`

**Nodes**: 5
**Integrations**: 11Labs, SYPHON

**Triggers**:
- Webhook (n8n-nodes-base.webhook)

### email_aggregation_workflows
**File**: `email_aggregation_workflows.json`

**Nodes**: 0
**Integrations**: None

### HVAC Bid Gmail Search
**File**: `hvac_bid_gmail_search_workflow.json`

**Nodes**: 6
**Integrations**: Gmail

**Triggers**:
- Webhook - Search Request (n8n-nodes-base.webhook)
- Respond to Webhook (n8n-nodes-base.respondToWebhook)

**Process Flow**:
  START: Webhook - Search Request
  → Gmail - Search Messages
    → Gmail - Get Message
      → Gmail - Download Attachment
        → Write Binary File
          → Respond to Webhook
  START: Respond to Webhook

### HVAC @SYPHON Monitor - Other Contractors
**File**: `hvac_syphon_monitor_workflow.json`

**Nodes**: 7
**Integrations**: Gmail, SYPHON

**Process Flow**:
  START: Schedule - Every 15 Minutes
  → Gmail - Search Other Contractors
    → Gmail - Get Message Details
      → @SYPHON Extract Intelligence
        → Extract Bid Information
          → Update Bid Comparison
            → Archive to JEDIARCHIVES

### LUMINA-Gmail Integration Workflow
**File**: `lumina_gmail_integration_workflow.json`

**Nodes**: 9
**Integrations**: Gmail, Holocron

**Process Flow**:
  START: Schedule - Check Every 5 Minutes
  → Gmail - Get Unread with Attachments
    → Gmail - Get Message Details
      → Process with LUMINA-Gmail System
        → Create Admin SME Job
          → Archive to JEDIARCHIVES
            → Index in HOLOCRON Library
              → Process with @F4 Capabilities
                → Check SLA Compliance

### messages
**File**: `messages.json`

**Nodes**: 0
**Integrations**: None

### nas_dsm_email_hub_expansion
**File**: `nas_dsm_email_hub_expansion.json`

**Nodes**: 0
**Integrations**: None

### proton_bridge_n8n_config
**File**: `proton_bridge_n8n_config.json`

**Nodes**: 0
**Integrations**: None

### ProtonMail Bridge to MailStation Integration
**File**: `proton_bridge_workflow.json`

**Nodes**: 7
**Integrations**: SYPHON, ProtonMail

**Triggers**:
- Schedule Trigger (n8n-nodes-base.scheduleTrigger)

**Process Flow**:
  START: Schedule Trigger
  → Get Proton Bridge Credentials
    → Fetch ProtonMail via Bridge
      → Process Emails
        → Send to MailStation
          → SYPHON Intelligence Extraction
            → Log Success

### SMS → SYPHON → Holocron
**File**: `sms_syphon_workflow.json`

**Nodes**: 4
**Integrations**: Holocron, SYPHON

**Triggers**:
- Webhook (n8n-nodes-base.webhook)

### unified_communications_config
**File**: `unified_communications_config.json`

**Nodes**: 0
**Integrations**: None

### workflows
**File**: `workflows.json`

**Nodes**: 0
**Integrations**: None
