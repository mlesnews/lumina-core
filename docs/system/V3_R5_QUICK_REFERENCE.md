# V3 & R5 Quick Reference - pfSense, NAS, N8N

**Quick reference for @v3 & @r5 infrastructure setup**

---

## 🎯 Infrastructure at a Glance

| Component | Address | Status | Purpose |
|-----------|---------|--------|---------|
| **pfSense** | 10.17.17.1 | ✅ | Firewall, network security |
| **NAS** | 10.17.17.32:5001 | ✅ | Storage, package server |
| **N8N** | http://10.17.17.32:5678 | ✅ | Workflow automation |
| **V3** | Via N8N webhook | ✅ | Vector verification |
| **R5** | Via N8N webhook | ✅ | Reasoning engine |

---

## 🚀 Quick Commands

### **Setup Everything:**
```powershell
.\scripts\setup-v3-r5-n8n-nas.ps1
```

### **Check Status:**
```python
from pathlib import Path
from scripts.python.v3_r5_n8n_orchestrator import V3R5N8NOrchestrator

orchestrator = V3R5N8NOrchestrator(project_root=Path("."))
status = orchestrator.get_system_status()
print(status)
```

### **Send Email:**
```python
orchestrator.send_email_via_n8n(
    to="user@example.com",
    subject="Test",
    body="Hello!"
)
```

### **Send SMS:**
```python
orchestrator.send_sms_via_n8n(
    to="+1234567890",
    message="Hello!"
)
```

### **Trigger V3:**
```python
result = orchestrator.trigger_v3_verification()
```

### **Trigger R5:**
```python
result = orchestrator.trigger_r5_reasoning(context={"task": "analyze"})
```

---

## 📋 N8N Webhook Endpoints

```
POST http://10.17.17.32:5678/webhook/v3_verification
POST http://10.17.17.32:5678/webhook/r5_reasoning
POST http://10.17.17.32:5678/webhook/email_send
POST http://10.17.17.32:5678/webhook/sms_send
POST http://10.17.17.32:5678/webhook/mobile_app
POST http://10.17.17.32:5678/webhook/desktop_widgets_*
```

---

## 📁 Key Files

- **Orchestrator:** `scripts/python/v3_r5_n8n_orchestrator.py`
- **Integration:** `scripts/python/v3_r5_n8n_nas_integration.py`
- **Config:** `config/v3_r5_n8n/integration_config.json`
- **Full Docs:** `docs/system/V3_R5_PFSENSE_NAS_N8N_COMPLETE_SETUP_HISTORY.md`

---

## ✅ Status Check

```python
status = orchestrator.get_system_status()
# Check:
# - status['integration']['v3_connected']
# - status['integration']['r5_connected']
# - status['integration']['n8n_connected']
# - status['integration']['nas_connected']
# - status['integration']['services_enabled']
```

---

**For complete documentation, see:** `V3_R5_PFSENSE_NAS_N8N_COMPLETE_SETUP_HISTORY.md`

