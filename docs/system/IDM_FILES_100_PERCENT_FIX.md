# IDM Files Stuck at 100% - Resolution

## Issue
Files show "100.00%" and "0 sec" in IDM but aren't in expected location.

## Possible Causes
1. **IDM Queue Folder**: Files may be in IDM's internal queue/temp folder
2. **Not Finalized**: IDM may need to "finalize" the download
3. **Wrong Destination**: Files downloaded to different location than expected

## Solutions

### 1. Check IDM's Actual File Location
In IDM:
- Right-click the completed file
- Select "Properties" or "Open Folder"
- This shows the actual file location

### 2. Manually Move Files
If files are found in a different location:
```powershell
# Move SAD
Move-Item "C:\path\to\model_ckpt_steps_80000.ckpt" "C:\Users\mlesn\Dropbox\my_projects\.lumina\models\singing_synthesis\TCSinger\checkpoints\SAD\"

# Move SDLM  
Move-Item "C:\path\to\model_ckpt_steps_120000.ckpt" "C:\Users\mlesn\Dropbox\my_projects\.lumina\models\singing_synthesis\TCSinger\checkpoints\SDLM\"
```

### 3. Re-download with Correct Path
If files are missing, re-queue in IDM with correct destination:
```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\python
python download_tcsinger_models.py
```

## NAS Storage Configuration

**Updated**: Download script now prioritizes NAS storage:
- Primary: `\\10.17.17.32\backups\MATT_Backups\models\singing_synthesis\TCSinger`
- Fallback: Local project directory

When NAS is accessible, all future downloads will go to NAS automatically.

## Verification

After moving files, verify:
```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\python
python verify_tcsinger_models.py
```
