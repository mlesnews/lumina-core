# N8N Workflow Import - Step-by-Step Instructions

**URL**: http://10.17.17.32:5678/home/workflows

---

## 🚀 Quick Import Steps

### Step 1: Login (if not already logged in)
1. Navigate to: `http://10.17.17.32:5678`
2. Username: `mlesn`
3. Password: From Azure Vault (`n8n-password`)

### Step 2: Go to Workflows Page
- Navigate to: `http://10.17.17.32:5678/home/workflows`
- Or click "Workflows" in the left sidebar

### Step 3: Import Workflows

**Method A: Via UI (Recommended)**
1. Click the **"+"** button (top right, next to search)
2. Select **"Import from File"**
3. Browse to: `C:\Users\mlesn\Dropbox\my_projects\.lumina\data\n8n_syphon_workflows\workflow_json\`
4. Import each file:
   - `email_syphon.json`
   - `sms_syphon.json`
   - `education_syphon.json`
5. Click **"Import"** for each

**Method B: Via Browser Console (Alternative)**
1. Open browser console (F12)
2. Copy workflow JSON from files
3. Use the import helper script (see `scripts/python/import_workflows_browser_helper.js`)

### Step 4: Activate Workflows
1. After import, each workflow will appear in the list
2. Toggle the switch on each workflow to **"Active"**

---

## 📋 Workflow Files Location

```
C:\Users\mlesn\Dropbox\my_projects\.lumina\data\n8n_syphon_workflows\workflow_json\
├── email_syphon.json (7,098 bytes)
├── sms_syphon.json (5,014 bytes)
└── education_syphon.json (8,755 bytes)
```

---

## ✅ Verification

After import, verify:
1. All 3 workflows appear in the workflows list
2. Each workflow shows "Active" status
3. Workflows can be opened and edited
4. Schedules are configured correctly:
   - Email: Every 2 hours
   - SMS: Every 3 hours
   - Education: Every 6 hours

---

## 🔧 Troubleshooting

**If import button not visible:**
- Make sure you're logged in
- Check that you have permissions
- Try refreshing the page

**If workflows don't activate:**
- Check for missing credentials (IMAP, etc.)
- Verify all nodes are properly configured
- Check N8N logs for errors

---

**Status**: ✅ **READY FOR IMPORT**
