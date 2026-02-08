# N8N Workflow Import Instructions

## ✅ WORKFLOWS READY FOR IMPORT

All SYPHON workflows have been created and are ready to import into N8N.

## 📁 Workflow Files Location

**Directory**: `data/n8n_syphon_workflows/workflow_json/`

**Files**:
- `email_syphon.json` - Email intelligence extraction workflow
- `sms_syphon.json` - SMS intelligence extraction workflow  
- `education_syphon.json` - Social-news-education (white papers, thesis) workflow

## 🚀 How to Import

### Method 1: N8N Web Interface (Recommended)

1. **Access N8N**: Open N8N in your browser
   - If on NAS: Check NAS package manager or Docker containers
   - Common ports: 5678, 8080, 3000
   - Common URLs: `http://10.17.17.32:5678` or `http://nas.lesnewski.local:5678`

2. **Import Workflow**:
   - Click "Workflows" in the left sidebar
   - Click the "+" button or "Import from File"
   - Select one of the JSON files from `data/n8n_syphon_workflows/workflow_json/`
   - Click "Import"

3. **Repeat** for all three workflows

4. **Configure**:
   - Set up IMAP credentials for email workflow
   - Configure any API keys needed
   - Adjust schedules if needed

5. **Activate**: Toggle each workflow to "Active"

### Method 2: N8N CLI (If Available)

```bash
# If N8N CLI is installed
n8n import:workflow --input=data/n8n_syphon_workflows/workflow_json/email_syphon.json
n8n import:workflow --input=data/n8n_syphon_workflows/workflow_json/sms_syphon.json
n8n import:workflow --input=data/n8n_syphon_workflows/workflow_json/education_syphon.json
```

### Method 3: N8N API (If Authenticated)

```bash
# Get API token from N8N settings first
export N8N_API_TOKEN="your_token_here"
export N8N_URL="http://10.17.17.32:5678"

# Import workflows
curl -X POST "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d @data/n8n_syphon_workflows/workflow_json/email_syphon.json
```

## 📋 Workflow Details

### Email SYPHON Workflow
- **Schedule**: Every 2 hours
- **Function**: Fetches emails → Extracts intelligence → Saves to NAS → Adds to queue
- **Credentials Needed**: IMAP email account credentials

### SMS SYPHON Workflow  
- **Schedule**: Every 3 hours (also accepts webhooks)
- **Function**: Receives SMS → Extracts intelligence → Saves to NAS → Adds to queue
- **Credentials Needed**: SMS service API credentials (if applicable)

### Education SYPHON Workflow
- **Schedule**: Every 6 hours
- **Sources**: ArXiv, ResearchGate, Web (white papers, thesis)
- **Function**: Fetches education sources → Extracts intelligence → Saves to NAS → Adds to queue
- **Credentials Needed**: None (public APIs)

## ✅ After Import

1. **Verify** workflows appear in N8N
2. **Configure** credentials and settings
3. **Test** each workflow manually
4. **Activate** all workflows
5. **Monitor** executions in N8N dashboard

## 🎯 Expected Results

Once active:
- ✅ Email intelligence extracted every 2 hours
- ✅ SMS intelligence extracted every 3 hours  
- ✅ Education intelligence (white papers, thesis) extracted every 6 hours
- ✅ All intelligence saved to NAS storage
- ✅ All intelligence added to unified queue

---

**Status**: ✅ **WORKFLOWS READY - AWAITING MANUAL IMPORT**

**Files Created**: 3 workflow JSON files ready for import
