# Continuous Workflow Analysis Setup

**Date:** 2026-01-15
**Status:** ✅ Setup Complete
**Purpose:** Automatically analyze workflows and execute opportunities

---

## 🎯 **OVERVIEW**

The Continuous Workflow Analyzer automatically:
1. Analyzes AI summaries/debriefs for patterns
2. Identifies workflow opportunities
3. Executes opportunities using @DOIT
4. Runs on a schedule (daily by default)

---

## 🚀 **SETUP**

### **Windows (PowerShell)**

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\automation\workflow_analysis\setup_continuous_analysis.ps1
```

This creates a scheduled task that runs daily at 2:00 AM.

### **Linux/NAS (Bash)**

```bash
cd /path/to/.lumina
chmod +x scripts/automation/workflow_analysis/setup_continuous_analysis.sh
./scripts/automation/workflow_analysis/setup_continuous_analysis.sh
```

This creates a cron job that runs daily at 2:00 AM.

---

## 🔧 **MANUAL EXECUTION**

### **Run Once**

```bash
python scripts/python/jarvis_workflow_continuous_analyzer.py --once
```

### **Run Continuously (Background)**

```bash
python scripts/python/jarvis_workflow_continuous_analyzer.py
```

This runs in the foreground, checking every 60 minutes if analysis is needed.

---

## ⚙️ **CONFIGURATION**

### **Analysis Interval**

Default: 24 hours (daily)

Change with `--interval-hours`:
```bash
python jarvis_workflow_continuous_analyzer.py --interval-hours 12 --once
```

### **Check Interval**

Default: 60 minutes (for continuous mode)

Change with `--check-minutes`:
```bash
python jarvis_workflow_continuous_analyzer.py --check-minutes 30
```

### **Auto-Execute**

Default: Enabled (automatically executes opportunities)

Disable with `--no-auto-execute`:
```bash
python jarvis_workflow_continuous_analyzer.py --no-auto-execute --once
```

---

## 📊 **WHAT IT DOES**

### **1. Analysis Phase**
- Loads summaries from `data/jarvis/summaries/`
- Analyzes for patterns:
  - Repetition patterns
  - Time patterns
  - Decision patterns
  - Error patterns
  - Knowledge gaps

### **2. Opportunity Generation**
- Creates opportunities from patterns:
  - Knowledge base entries
  - Automation scripts
  - Optimization guides
  - Error documentation

### **3. Execution Phase** (if auto-execute enabled)
- Creates knowledge base entries
- Generates automation scripts
- Creates optimization guides
- Documents error resolutions

---

## 📁 **OUTPUT LOCATIONS**

- **Analysis Reports**: `data/jarvis/workflow_analysis/workflow_analysis_*.json`
- **Knowledge Base**: `docs/knowledge_base/kb_*.md`
- **Automation Scripts**: `scripts/automation/auto_*.py`
- **Error Docs**: `docs/troubleshooting/error_*.md`
- **Optimization Guides**: `docs/optimization/opt_*.md`

---

## 🔍 **MONITORING**

### **Check Last Analysis**

The system tracks last analysis time in:
```
data/jarvis/workflow_analysis/.last_analysis
```

### **View Scheduled Task (Windows)**

```powershell
Get-ScheduledTask -TaskName "JARVIS-Workflow-Analysis"
```

### **View Cron Job (Linux)**

```bash
crontab -l | grep workflow_analysis
```

### **View Logs**

Windows scheduled task logs are in Event Viewer.

Linux cron logs are in:
```
logs/workflow_analysis_cron.log
```

---

## 🛠️ **TROUBLESHOOTING**

### **Task Not Running**

1. Check if task exists:
   ```powershell
   Get-ScheduledTask -TaskName "JARVIS-Workflow-Analysis"
   ```

2. Check task history:
   ```powershell
   Get-ScheduledTaskInfo -TaskName "JARVIS-Workflow-Analysis"
   ```

3. Run manually to test:
   ```bash
   python scripts/python/jarvis_workflow_continuous_analyzer.py --once
   ```

### **No Opportunities Found**

- Check if summaries exist: `data/jarvis/summaries/`
- Verify analysis ran: Check `workflow_analysis_*.json` files
- Review analysis output for patterns

### **Auto-Execute Not Working**

- Verify `--no-auto-execute` is not set
- Check executor permissions
- Review executor logs

---

## 📈 **METRICS**

The system tracks:
- Summaries analyzed
- Patterns found
- Opportunities generated
- Opportunities executed
- Time saved (estimated)

View in analysis reports: `data/jarvis/workflow_analysis/workflow_analysis_*.json`

---

## ✅ **STATUS**

**Setup:** ✅ Complete
**Scheduled Task:** ✅ Created
**Auto-Execute:** ✅ Enabled
**First Run:** Pending (will run at next scheduled time)

---

**Tags:** `#JARVIS` `#WORKFLOW` `#AUTOMATION` `#DOIT` `@JARVIS` `@LUMINA`
