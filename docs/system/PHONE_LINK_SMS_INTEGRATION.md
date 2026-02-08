# Windows Phone Link SMS Integration

**Integrating Phone Link with N8N SMS SYPHON Workflow**

---

## ⚠️ Limitation

**Windows Phone Link app does NOT have a public API** for programmatic access to SMS.

Microsoft has confirmed this limitation - there is no official API for Phone Link.

---

## 💡 Workaround Solutions

### 1. UI Automation (Primary Method)

**Status**: ⚠️ **EXPERIMENTAL**

Use UI automation (`pywinauto`/`pyautogui`) to:
- Monitor Phone Link window
- Detect new messages in UI
- Extract message content
- Send to N8N webhook

**Challenges**:
- Phone Link UI structure may change
- Requires Phone Link window to be open
- Fragile - breaks if UI changes

**Implementation**: `scripts/python/phone_link_sms_integration.py`

---

### 2. Database Monitoring (Alternative)

**Status**: 🔍 **INVESTIGATION NEEDED**

Phone Link may store messages in local database:
- Location: `AppData\Local\Packages\Microsoft.YourPhone_*\LocalState`
- Format: SQLite database files
- Access: Direct database queries

**Challenges**:
- Database structure unknown
- May be encrypted
- Location may vary

---

### 3. Alternative SMS Services

**Recommended**: Use services with proper APIs

#### Option A: SMS Mobile API
- Install app on phone
- Python API available
- Direct SMS gateway

#### Option B: Twilio
- Cloud SMS service
- Full API support
- Reliable and scalable

#### Option C: Azure Communication Services
- Microsoft's SMS platform
- Full API support
- Integrates with Azure ecosystem

---

## 🔧 Current N8N SMS Workflow

**Workflow**: `data/n8n_syphon_workflows/workflow_json/sms_syphon.json`

**Flow**:
1. **Webhook Receiver**: Receives SMS data via POST
2. **Format SMS Data**: Processes and formats message
3. **SYPHON Extract**: Sends to SYPHON API for intelligence extraction
4. **Save Intelligence**: Saves to `data/syphon/sms_intelligence/`
5. **Unified Queue**: Adds to unified processing queue

**Webhook URL**: `http://10.17.17.32:5678/webhook/sms/syphon`

---

## 📋 Integration Options

### Option 1: Bridge Service (Recommended)

Create a bridge service that:
1. Monitors Phone Link (UI automation or database)
2. Detects new SMS messages
3. Sends to N8N webhook in correct format

**File**: `scripts/python/phone_link_sms_integration.py`

### Option 2: Direct API Service

Use a proper SMS API service (Twilio, Azure, etc.) that:
1. Receives SMS via API
2. Sends directly to N8N webhook
3. More reliable than Phone Link workaround

---

## 🚀 Next Steps

1. **Test UI Automation**: 
   - Analyze Phone Link UI structure
   - Implement message detection
   - Test with real messages

2. **Investigate Database**:
   - Find Phone Link database location
   - Analyze database structure
   - Implement database monitoring

3. **Consider Alternatives**:
   - Evaluate SMS Mobile API
   - Consider Twilio integration
   - Evaluate Azure Communication Services

---

## 📊 Status

- ✅ N8N SMS workflow configured
- ⚠️ Phone Link API: Not available
- 🔧 UI Automation: Experimental
- 🔍 Database Monitoring: Investigation needed
- 💡 Alternative Services: Available

---

**Tags**: `#PHONE_LINK #SMS #SYPHON #N8N #UI_AUTOMATION @JARVIS @LUMINA`
