# ElevenLabs API Key - Docker Desktop Setup

**Date**: 2026-01-14  
**Status**: 📋 **SETUP GUIDE**  
**Tags**: `#ELEVENLABS` `#DOCKER` `#API_KEY` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Objective

Get the ElevenLabs API key from Azure Key Vault and add it to Docker Desktop secrets.

---

## ✅ Key Found

**Location**: Azure Key Vault  
**Secret Name**: `elevenlabs-api-key`  
**Status**: ✅ **FOUND** in vault

---

## 📋 Setup Steps

### Step 1: Retrieve Key

**Option A: Automatic (Recommended)**
```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python -c "import sys; sys.path.insert(0, 'scripts/python'); from azure_service_bus_integration import AzureKeyVaultClient; import pyperclip; client = AzureKeyVaultClient(vault_url='https://jarvis-lumina.vault.azure.net/'); key = client.get_secret('elevenlabs-api-key'); pyperclip.copy(key); print('✅ Key copied to clipboard!')"
```

**Option B: PowerShell Script**
```powershell
.\scripts\powershell\get_elevenlabs_key_for_docker.ps1
```

**Option C: Manual**
1. Open Azure Portal
2. Navigate to Key Vault: `jarvis-lumina`
3. Find secret: `elevenlabs-api-key`
4. Copy the value

---

### Step 2: Add to Docker Desktop

1. **Open Docker Desktop**
2. **Go to Settings** (gear icon)
3. **Navigate to**: 
   - **Secrets** tab, OR
   - **Environment** tab, OR
   - **Resources → Advanced** (depending on Docker Desktop version)
4. **Find field**: `ELEVENLABS_API_KEY` (or create it)
5. **Paste the key** (Ctrl+V)
6. **Click Save**

---

### Step 3: Verify

**Check environment variable in Docker container:**
```bash
docker exec <container_name> env | grep ELEVENLABS_API_KEY
```

**Or test in application:**
```python
import os
key = os.getenv('ELEVENLABS_API_KEY')
print('✅ Key found!' if key else '❌ Key not found')
```

---

## 🔧 Troubleshooting

### Key Not in Clipboard

**Solution**: Run retrieval command again or check Azure Key Vault manually.

### Docker Desktop Field Not Found

**Solution**: 
- Check Docker Desktop version
- Look for "Environment Variables" or "Secrets" section
- May need to add as environment variable in docker-compose.yml

### Key Not Working

**Solution**:
- Verify key is correct (check preview)
- Ensure key hasn't expired
- Check ElevenLabs account has credits

---

## 📝 Alternative: Docker Compose

If Docker Desktop doesn't have secrets UI, add to `docker-compose.yml`:

```yaml
services:
  your_service:
    environment:
      - ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}
```

Then set environment variable:
```powershell
$env:ELEVENLABS_API_KEY = "<key-value>"
docker-compose up
```

---

## 🎯 Next Steps

1. ✅ Retrieve key from Azure Key Vault
2. ✅ Copy to clipboard
3. ⏳ Paste into Docker Desktop
4. ⏳ Save and verify
5. ⏳ Test ElevenLabs integration

---

**Status**: 📋 **SETUP GUIDE CREATED**  
**Key Location**: Azure Key Vault → `elevenlabs-api-key`  
**Next Action**: Retrieve key and add to Docker Desktop  
**Tags**: `#ELEVENLABS` `#DOCKER` `#API_KEY` `@LUMINA` `@JARVIS` `#PEAK`
