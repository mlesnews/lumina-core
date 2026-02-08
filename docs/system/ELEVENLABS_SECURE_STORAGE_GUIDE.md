# ElevenLabs API Key - Secure Storage Guide

## Most Secure Method: Azure Key Vault via Azure CLI

### Security Ranking (Most to Least Secure):

1. ✅ **Azure Key Vault via Azure CLI** (RECOMMENDED - MOST SECURE)
   - Uses Azure AD authentication (already logged in)
   - Encrypted at rest in Azure Key Vault
   - Access controlled via Azure RBAC
   - Audit logging enabled
   - No plain text exposure
   - **Use**: `.\scripts\powershell\store_elevenlabs_key.ps1`

2. ⚠️ **Azure Key Vault via Python SDK** (Less Secure)
   - Has authentication issues/timeouts
   - Still secure but unreliable
   - **Avoid**: Use PowerShell method instead

3. ❌ **Environment Variables** (Least Secure)
   - Visible in process list
   - Can leak in logs
   - **Never use for production**

4. ❌ **Plain Text Files** (NEVER)
   - Can be committed to git
   - No encryption
   - **Absolutely forbidden**

---

## ElevenLabs Authentication Type

**ElevenLabs uses**: **Simple API Key** (not OAuth2)

- Just a single token string (looks like: `sk-...` or long alphanumeric)
- No OAuth2 Client Credentials needed
- No Basic Auth setup required
- Just copy the API key string from ElevenLabs webui

---

## Secure Storage Steps

### Step 1: Get Your ElevenLabs API Key
1. Go to ElevenLabs webui
2. Navigate to API Keys section
3. Find the key labeled "Cursor - Cursor API Key" (or create one)
4. Copy the key (just the key string, nothing else)

### Step 2: Store Securely
```powershell
# Copy key to clipboard, then:
.\scripts\powershell\store_elevenlabs_key.ps1
```

**What this does:**
- ✅ Reads from clipboard (no terminal history)
- ✅ Stores in Azure Key Vault (encrypted)
- ✅ Stores under multiple names for compatibility
- ✅ No plain text files created
- ✅ Azure AD authenticated (already logged in)

---

## Why Azure Key Vault is Most Secure

1. **Encryption**: AES-256 encryption at rest
2. **Access Control**: Azure RBAC - only authorized users/services can access
3. **Audit Logging**: All access attempts logged
4. **Rotation**: Easy to rotate keys without code changes
5. **No Exposure**: Never stored in plain text or git

---

## After Storage

JARVIS will automatically retrieve the key from Azure Key Vault when needed for TTS.

**No code changes needed** - the system already checks Azure Key Vault first!

---

**RECOMMENDATION**: Use Azure Key Vault via PowerShell script (Method #1) ✅
