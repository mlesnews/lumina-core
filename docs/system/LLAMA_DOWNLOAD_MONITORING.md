# Llama Model Download Monitoring

**Date**: 2026-01-10  
**Status**: ⏳ **DOWNLOAD IN PROGRESS**

## Overview

Downloading Llama model (5.55 GB) from FALC (laptop) to KAIJU Docker volume:
- **Source**: M drive on FALC (10.17.17.191)
- **Destination**: Docker volume on KAIJU (10.17.17.11)
- **Volume Path**: `/var/lib/docker/volumes/iron-legion-llamacpp_iron-legion-models/_data`
- **Container Mount**: `/models` inside container

## Monitoring from Laptop

### Quick Status Check
Run this from the laptop to check current progress:
```powershell
.\scripts\startup\CHECK_LLAMA_DOWNLOAD.ps1
```

### Continuous Monitoring
For real-time progress updates:
```powershell
.\scripts\startup\MONITOR_LLAMA_DOWNLOAD.ps1
```

This will:
- Check progress every 30 seconds
- Show progress bar and percentage
- Display file size and last update time
- Alert when download completes

## Download Status

**Current Status**: Download in progress (background job)

**Expected Size**: 5.55 GB  
**Current Size**: Checking...  
**Progress**: Monitoring...

## Background Process

The download is running as a background job on KAIJU via SSH. You can monitor it from the laptop using the scripts above.

## After Download Completes

1. **Verify file size**: Should be ~5.55 GB
2. **Restart Mark II container**:
   ```powershell
   ssh 10.17.17.11 "docker restart iron-legion-mark-ii-llama32-llamacpp"
   ```
3. **Check container logs**:
   ```powershell
   ssh 10.17.17.11 "docker logs iron-legion-mark-ii-llama32-llamacpp --tail 20"
   ```
4. **Test endpoint**:
   ```powershell
   Invoke-WebRequest -Uri "http://10.17.17.11:3002/v1/models" -UseBasicParsing
   ```

## Troubleshooting

If download appears stuck:
1. Check HTTP server on FALC: `http://10.17.17.191:8888/`
2. Verify model file exists: `M:\Llama-3.2-11B-Vision-Instruct.Q4_K_M.gguf`
3. Restart HTTP server if needed
4. Re-run download command

---

**Last Updated**: 2026-01-10  
**Monitoring**: Active from laptop (FALC)
