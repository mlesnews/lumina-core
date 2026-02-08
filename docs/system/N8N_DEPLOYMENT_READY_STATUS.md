# N8N SYPHON Workflows - Deployment Ready Status

**Date**: 2026-01-10  
**Status**: ✅ **WORKFLOWS READY - AWAITING N8N SERVICE**

---

## 📋 Current Status

### ✅ Completed
- **3 Workflow JSON files created** in `data/n8n_syphon_workflows/workflow_json/`
  - `email_syphon.json` - Email intelligence extraction (every 2 hours)
  - `sms_syphon.json` - SMS intelligence extraction (every 3 hours)
  - `education_syphon.json` - White papers & thesis extraction (every 6 hours)
- **Deployment script ready**: `scripts/python/deploy_n8n_with_vault_creds.py`
- **Azure Vault credentials retrieved**:
  - `n8n-password` ✅
  - `n8n-basic-auth-password` ✅
  - `n8n-nas-password` ✅
- **NAS configuration**: `config/nas_config.json` (user: `mlesn`, host: `10.17.17.32`)

### ⏳ Pending
- **N8N service not running** on port 5678
- **N8N not installed** as Synology package
- **Deployment blocked** until N8N is accessible

---

## 🎯 Target Configuration

**N8N URL**: `http://10.17.17.32:5678`  
**Authentication**: Basic Auth (username: `mlesn`, password from Azure Vault)  
**Workflows**: 3 SYPHON workflows ready for deployment

---

## 🚀 Deployment Instructions (When N8N is Available)

### Option 1: Automated Deployment (Recommended)

Once N8N is running and accessible:

```bash
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/deploy_n8n_with_vault_creds.py
```

**What it does**:
1. Retrieves credentials from Azure Vault
2. Finds N8N at `http://10.17.17.32:5678`
3. Authenticates using `mlesn` + password from vault
4. Deploys all 3 workflows via N8N API
5. Reports deployment status

### Option 2: Manual Import

1. **Access N8N**: Open `http://10.17.17.32:5678` in browser
2. **Login**: Use `mlesn` + password from Azure Vault (`n8n-password`)
3. **Import Workflows**:
   - Click "Workflows" → "Import from File"
   - Import each JSON file from `data/n8n_syphon_workflows/workflow_json/`
4. **Configure**:
   - Set IMAP credentials for email workflow
   - Configure any API keys if needed
5. **Activate**: Toggle each workflow to "Active"

---

## 📊 Workflow Details

### Email SYPHON Workflow
- **Schedule**: Every 2 hours
- **Process**: Fetch emails → Format → SYPHON Extract → Save → Queue
- **Webhook**: `http://10.17.17.32:5678/webhook/email/syphon`
- **Storage**: `/data/syphon/email_intelligence/YYYY-MM-DD_email_intelligence.jsonl`

### SMS SYPHON Workflow
- **Schedule**: Every 3 hours
- **Process**: Receive SMS → Format → SYPHON Extract → Save → Queue
- **Webhook**: `http://10.17.17.32:5678/webhook/sms/syphon`
- **Storage**: `/data/syphon/sms_intelligence/YYYY-MM-DD_sms_intelligence.jsonl`

### Education SYPHON Workflow
- **Schedule**: Every 6 hours
- **Sources**: ArXiv, ResearchGate, Web (white papers, thesis)
- **Process**: Fetch → Merge → SYPHON Extract → Save → Queue
- **Webhook**: `http://10.17.17.32:5678/webhook/education/syphon`
- **Storage**: `/data/syphon/education_intelligence/YYYY-MM-DD_education_intelligence.jsonl`

---

## 🔗 Integration Points

### SYPHON API Endpoints
- **Email**: `http://10.17.17.11:8000/api/syphon/email`
- **SMS**: `http://10.17.17.11:8000/api/syphon/sms`
- **Web/Education**: `http://10.17.17.11:8000/api/syphon/web`

### Unified Queue API
- **Add Item**: `http://10.17.17.11:8000/api/unified-queue/add`

---

## 🔍 N8N Installation Options

### Option 1: Synology Container Manager (Docker)
1. Open **Container Manager** in DSM
2. Search for `n8nio/n8n` image
3. Create container with:
   - Port mapping: `5678:5678`
   - Volume: `/volume1/docker/n8n:/home/node/.n8n`
   - Environment: `N8N_BASIC_AUTH_USER=mlesn`, `N8N_BASIC_AUTH_PASSWORD=<from-vault>`

### Option 2: Synology Package Center
1. Check if N8N package is available in Package Center
2. Install and configure

### Option 3: Manual Docker Installation (SSH)
```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v /volume1/docker/n8n:/home/node/.n8n \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=mlesn \
  -e N8N_BASIC_AUTH_PASSWORD=<from-azure-vault> \
  n8nio/n8n:latest
```

---

## ✅ Verification Steps

Once N8N is running:

1. **Test Connection**:
   ```bash
   curl http://10.17.17.32:5678
   ```

2. **Test Authentication**:
   ```bash
   curl -u mlesn:<password> http://10.17.17.32:5678/api/v1/workflows
   ```

3. **Deploy Workflows**:
   ```bash
   python scripts/python/deploy_n8n_with_vault_creds.py
   ```

---

## 📝 Files Ready

- ✅ `data/n8n_syphon_workflows/workflow_json/email_syphon.json`
- ✅ `data/n8n_syphon_workflows/workflow_json/sms_syphon.json`
- ✅ `data/n8n_syphon_workflows/workflow_json/education_syphon.json`
- ✅ `scripts/python/deploy_n8n_with_vault_creds.py`
- ✅ `config/nas_config.json`

---

## 🎯 Next Steps

1. **Install/Start N8N** on NAS at `10.17.17.32:5678`
2. **Verify Access**: Test connection and authentication
3. **Deploy Workflows**: Run deployment script or manual import
4. **Activate**: Enable all workflows in N8N
5. **Monitor**: Check workflow executions in N8N dashboard

---

**Status**: ✅ **READY FOR DEPLOYMENT - AWAITING N8N SERVICE**

**Tags**: @SYPHON @N8N @NAS #EMAIL #SMS #EDUCATION #WHITE_PAPER #THESIS @JARVIS @LUMINA #READY
