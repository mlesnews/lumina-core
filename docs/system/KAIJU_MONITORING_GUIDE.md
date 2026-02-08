# KAIJU Iron Legion Cluster Monitoring Guide

**Purpose**: Monitor and verify KAIJU Ollama cluster rebuild progress  
**Tag**: #KAIJU #MONITORING #IRON-LEGION

---

## 📋 Available Scripts

### 1. Quick Check (`quick_check_kaiju_models.ps1`)

**One-time status check** - Shows current model count and list.

```powershell
# From .lumina project root
.\scripts\powershell\quick_check_kaiju_models.ps1
```

**Output**:
- ✅ Shows available models (X/7)
- Lists all current models
- Indicates if rebuild is complete

---

### 2. Continuous Monitor (`monitor_kaiju_cluster_rebuild.ps1`)

**Continuous monitoring** - Checks every 30 seconds and alerts when all 7 models are ready.

```powershell
# From .lumina project root
.\scripts\powershell\monitor_kaiju_cluster_rebuild.ps1
```

**Options**:
```powershell
# Custom check interval (default: 30 seconds)
.\monitor_kaiju_cluster_rebuild.ps1 -CheckInterval 60

# Quiet mode (minimal output)
.\monitor_kaiju_cluster_rebuild.ps1 -Quiet

# Custom KAIJU IP
.\monitor_kaiju_cluster_rebuild.ps1 -KAIJU_IP "10.17.17.32"
```

**Features**:
- ✅ Progress bar showing X/7 models
- ✅ Real-time model list updates
- ✅ Audio alert when complete (beep)
- ✅ Shows elapsed time and check count
- ✅ Press Ctrl+C to stop

---

## 🎯 Usage Examples

### Quick Status Check

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\powershell\quick_check_kaiju_models.ps1
```

### Monitor Until Complete

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
.\scripts\powershell\monitor_kaiju_cluster_rebuild.ps1
```

### Monitor in Background (PowerShell Job)

```powershell
# Start monitoring job
$job = Start-Job -ScriptBlock {
    cd C:\Users\mlesn\Dropbox\my_projects\.lumina
    .\scripts\powershell\monitor_kaiju_cluster_rebuild.ps1 -Quiet
}

# Check job status
Get-Job

# View output
Receive-Job -Job $job

# Stop job
Stop-Job -Job $job
Remove-Job -Job $job
```

---

## 📊 Expected Output

### Quick Check (1/7 models)
```
========================================
KAIJU Iron Legion - Quick Model Check
========================================

Checking Ollama API on 10.17.17.32...

✅ KAIJU Ollama is accessible

Available models: 1/7

Models:
  - llama3.2:3b

⚠️  Cluster rebuild in progress: 1/7 models
   Run monitor script: .\monitor_kaiju_cluster_rebuild.ps1
```

### Monitor (Complete)
```
========================================
🎉 CLUSTER REBUILD COMPLETE!
========================================

All 7 models are now available!
Total time: 00:15:32
Total checks: 32

Available models:
  ✅ llama3.2:3b
  ✅ [model 2]
  ✅ [model 3]
  ✅ [model 4]
  ✅ [model 5]
  ✅ [model 6]
  ✅ [model 7]
```

---

## 🔧 Troubleshooting

### Script Cannot Reach KAIJU

**Error**: `Cannot reach KAIJU Ollama`

**Possible causes**:
1. Cluster rebuild in progress (Ollama may be restarting)
2. Network connectivity issue
3. Ollama service not running

**Solution**:
- Wait a few minutes and try again
- Check network: `Test-NetConnection -ComputerName 10.17.17.32 -Port 11434`
- Verify Ollama is running on KAIJU

### Models Not Appearing

**Issue**: Models count not increasing

**Possible causes**:
1. Models still downloading/importing
2. `OLLAMA_MODELS` environment variable not set
3. Models directory not accessible

**Solution**:
- Check on KAIJU: `ollama list`
- Verify environment: `$env:OLLAMA_MODELS`
- Check directory: `Test-Path "D:\Ollama\models"`

---

## 📝 Post-Rebuild Checklist

Once monitor shows all 7 models:

- [ ] Verify in Cursor: Check model selector
- [ ] Test model access: Try generating a response
- [ ] Update Cursor config: Add individual model entries if needed
- [ ] Document model names: Update KAIJU_CLUSTER_REBUILD_STATUS.md

---

## 🚀 Quick Start

**Just want to check status?**
```powershell
.\scripts\powershell\quick_check_kaiju_models.ps1
```

**Want to monitor until complete?**
```powershell
.\scripts\powershell\monitor_kaiju_cluster_rebuild.ps1
```

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS
