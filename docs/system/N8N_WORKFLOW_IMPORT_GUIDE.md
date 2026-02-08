# N8N Workflow Import Guide - Quick Reference

**Status**: ✅ **N8N RUNNING - READY FOR IMPORT**

---

## 🚀 Quick Import (2 minutes)

### Step 1: Access N8N
Open in browser: **http://10.17.17.32:5678**

### Step 2: Login
- **Username**: `mlesn`
- **Password**: From Azure Vault (`n8n-password`)

### Step 3: Import Workflows

1. Click **"Workflows"** in left sidebar
2. Click **"+"** button (top right) → **"Import from File"**
3. Select each file from:
   ```
   C:\Users\mlesn\Dropbox\my_projects\.lumina\data\n8n_syphon_workflows\workflow_json\
   ```
   - `email_syphon.json`
   - `sms_syphon.json`
   - `education_syphon.json`
4. Click **"Import"** for each
5. **Activate**: Toggle switch on each workflow to "Active"

---

## 📋 What Each Workflow Does

### Email SYPHON
- Runs every **2 hours**
- Fetches emails from all accounts
- Extracts intelligence via SYPHON
- Saves to NAS storage
- Adds to unified queue

### SMS SYPHON
- Runs every **3 hours**
- Receives SMS from all sources
- Extracts intelligence via SYPHON
- Saves to NAS storage
- Adds to unified queue

### Education SYPHON
- Runs every **6 hours**
- Fetches from ArXiv, ResearchGate, Web
- Extracts intelligence from white papers & thesis
- Saves to NAS storage
- Adds to unified queue

---

## ✅ After Import

1. **Verify** workflows appear in N8N dashboard
2. **Configure** any credentials needed (IMAP, etc.)
3. **Activate** all workflows (toggle switches)
4. **Monitor** executions in N8N dashboard

---

## 🔄 For Future Automated Deployment

Generate API key in N8N:
1. Settings → API → Create API Key
2. Add to Azure Vault: `n8n-api-token`
3. Then run: `python scripts/python/deploy_n8n_with_vault_creds.py`

---

**Current Status**: ✅ **READY - AWAITING MANUAL IMPORT**
