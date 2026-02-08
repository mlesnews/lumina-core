# N8N SYPHON Workflows - Active Status

**Intelligence Extraction Workflows Status**

---

## ✅ Active Workflows

### 1. SYPHON SMS Intelligence Extraction
- **Status**: ✅ **ACTIVE**
- **ID**: `IUtSGqLvEj05Xmor`
- **Trigger**: Webhook + Schedule (every 3 hours)
- **Webhook**: `http://10.17.17.32:5678/webhook/sms/syphon`
- **Destination**: SYPHON API (`http://10.17.17.11:8000/api/syphon/sms`)

### 2. SYPHON Social-News-Education Intelligence Extraction
- **Status**: ✅ **ACTIVE**
- **ID**: `Kkzv8cGXSLg4JAuk`
- **Trigger**: Schedule (every 6 hours)
- **Source**: Social media, news, education sources
- **Destination**: SYPHON API

---

## ⚠️ Needs Attention

### SYPHON Email Intelligence Extraction
- **Status**: ⚠️ **INACTIVE** (activation issue)
- **ID**: `CvU8gDibd1VYpxWf`
- **Trigger**: Schedule (every 2 hours)
- **Source**: NAS Mail Hub (IMAP)
  - Server: `10.17.17.32:993`
  - Account: `mlesn@homelab.lesnewski.local`
- **Issue**: Activation endpoint not working - may need manual activation in N8N UI

**To Fix**: 
1. Open N8N: `http://10.17.17.32:5678`
2. Navigate to "SYPHON Email Intelligence Extraction" workflow
3. Toggle activation switch manually

---

## 📱 SMS Integration - Phone Link

**Status**: ⚠️ **NO API AVAILABLE**

**Finding**: Windows Phone Link app does NOT have a public API.

**Options**:

1. **UI Automation** (Experimental)
   - Script: `scripts/python/phone_link_sms_integration.py`
   - Status: Experimental - not recommended for production

2. **SMS Mobile API** (Recommended)
   - Install app on phone
   - Python API: `pip install smsmobileapi`
   - Direct SMS gateway

3. **Twilio** (Production)
   - Full API support
   - Reliable and scalable
   - Paid service

4. **Azure Communication Services**
   - Microsoft's SMS platform
   - Full API support
   - Azure integration

---

## 📋 Next Steps

1. **Email Workflow**: Manually activate in N8N UI
2. **SMS Source**: Choose integration method (recommend SMS Mobile API or Twilio)
3. **Test Workflows**: Verify intelligence extraction is working
4. **Monitor**: Check intelligence files in `data/syphon/`

---

## 🚀 Activation Script

**Script**: `scripts/python/activate_n8n_syphon_workflows.py`

**Usage**:
```bash
python scripts/python/activate_n8n_syphon_workflows.py
```

**Status**: 
- ✅ SMS workflow: Activated
- ✅ Education workflow: Activated
- ⚠️ Email workflow: Needs manual activation

---

**Tags**: `#N8N #SYPHON #EMAIL #SMS #WORKFLOWS @JARVIS @LUMINA`
