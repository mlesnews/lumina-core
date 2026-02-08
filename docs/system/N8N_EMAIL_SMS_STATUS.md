# N8N Email & SMS SYPHON - Current Status

**Intelligence Extraction Workflows**

---

## 📧 Email SYPHON Workflow

**Status**: ✅ **DEPLOYED**

**Workflow**: `data/n8n_syphon_workflows/workflow_json/email_syphon.json`

### Configuration

- **Trigger**: Scheduled every 2 hours
- **Source**: NAS Mail Hub (IMAP)
  - Server: `10.17.17.32:993`
  - Account: `mlesn@homelab.lesnewski.local`
  - Credentials: Stored in N8N (IMAP credential type)
- **Destination**: SYPHON API
  - URL: `http://10.17.17.11:8000/api/syphon/email`
- **Storage**: `data/syphon/email_intelligence/`

### Flow

1. **Schedule Trigger** → Runs every 2 hours
2. **Fetch All Emails** → IMAP connection to NAS Mail Hub
3. **Format Email Data** → Process email structure
4. **SYPHON Extract** → Send to SYPHON API for intelligence extraction
5. **Save Intelligence** → Save to JSONL file
6. **Unified Queue** → Add to processing queue

### Current Status

- ✅ Workflow deployed to N8N
- ✅ IMAP credentials configured
- ✅ SYPHON API endpoint configured
- ⚠️ **Needs verification**: Check if workflow is active and processing emails

---

## 📱 SMS SYPHON Workflow

**Status**: ⚠️ **NEEDS INTEGRATION**

**Workflow**: `data/n8n_syphon_workflows/workflow_json/sms_syphon.json`

### Configuration

- **Trigger**: Webhook receiver + Schedule (every 3 hours)
- **Webhook URL**: `http://10.17.17.32:5678/webhook/sms/syphon`
- **Destination**: SYPHON API
  - URL: `http://10.17.17.11:8000/api/syphon/sms`
- **Storage**: `data/syphon/sms_intelligence/`

### Flow

1. **Webhook Receiver** → Receives SMS data via POST
2. **Format SMS Data** → Process SMS structure
3. **SYPHON Extract** → Send to SYPHON API
4. **Save Intelligence** → Save to JSONL file
5. **Unified Queue** → Add to processing queue

### Integration Challenge

**Problem**: No direct SMS source configured

**Options**:

1. **Windows Phone Link** (Requested)
   - ⚠️ **No API available** - Microsoft confirmed limitation
   - 💡 **Workaround**: UI automation (experimental)
   - 📁 **Script**: `scripts/python/phone_link_sms_integration.py`

2. **SMS Mobile API** (Recommended)
   - Install app on phone
   - Python API available
   - Direct integration possible

3. **Twilio** (Cloud Service)
   - Full API support
   - Reliable and scalable
   - Requires paid service

4. **Azure Communication Services**
   - Microsoft's SMS platform
   - Full API support
   - Integrates with Azure

---

## 🔧 Next Steps

### Email Workflow

1. **Verify Active**: Check if N8N workflow is running
2. **Test Connection**: Verify IMAP connection to NAS Mail Hub
3. **Check Processing**: Verify emails are being processed
4. **Review Intelligence**: Check extracted intelligence files

### SMS Workflow

1. **Choose Integration Method**:
   - Option A: Phone Link UI automation (experimental)
   - Option B: SMS Mobile API (recommended)
   - Option C: Twilio/Azure (cloud service)

2. **Implement Bridge**:
   - Create service to monitor SMS source
   - Send to N8N webhook in correct format
   - Handle errors and retries

3. **Test Integration**:
   - Send test SMS
   - Verify webhook receives data
   - Verify SYPHON processing

---

## 📊 Summary

| Workflow | Status | Source | Integration |
|----------|--------|--------|-------------|
| **Email** | ✅ Deployed | NAS Mail Hub (IMAP) | ✅ Configured |
| **SMS** | ⚠️ Needs Source | Phone Link (no API) | 🔧 Workaround needed |

---

## 🚀 Recommendations

1. **Email**: Verify workflow is active and processing
2. **SMS**: 
   - **Short-term**: Try Phone Link UI automation
   - **Long-term**: Consider SMS Mobile API or Twilio for reliability

---

**Tags**: `#N8N #EMAIL #SMS #SYPHON #PHONE_LINK @JARVIS @LUMINA`
