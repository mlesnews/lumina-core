# Critical Fixes Applied - 2026-01-06

## 🚨 Issue 1: Azure Key Vault Authentication Loop
**Status**: ✅ **FIXED**

**Problem**: Python SDK authentication kept timing out/401ing despite `az login`

**Solution**: Created PowerShell script using Azure CLI directly (bypasses Python SDK)

**Usage**:
```powershell
# Get key from clipboard and store
Get-Clipboard | ForEach-Object { .\scripts\powershell\store_elevenlabs_key.ps1 -ApiKey $_ }
```

**OR manually**:
```powershell
.\scripts\powershell\store_elevenlabs_key.ps1 -ApiKey "YOUR_KEY_HERE"
```

---

## 🚨 Issue 2: Bedrock Model Error
**Status**: 🔧 **IN PROGRESS**

**Error**: `Selected model is not supported by bedrock, please use a different model`

**Problem**: ULTRON model is selected but Bedrock doesn't support it

**Root Cause**: Cursor settings have `ULTRON` as default model, but Bedrock backend is enabled

**Fix Required**: 
1. Either disable Bedrock and use local ULTRON
2. Or change default model to a Bedrock-supported model (e.g., `claude-3-sonnet`)

---

## Quick Fixes

### Fix 1: Store ElevenLabs Key (WORKING NOW)
```powershell
# Copy key to clipboard, then:
Get-Clipboard | ForEach-Object { .\scripts\powershell\store_elevenlabs_key.ps1 -ApiKey $_ }
```

### Fix 2: Bedrock Model Issue
Need to check Cursor settings and either:
- Change default model to Bedrock-supported one
- Or ensure local-first routing bypasses Bedrock for ULTRON

---

**Last Updated**: 2026-01-06
