# Azure Key Vault - YouTube API Key Integration

**Status**: ✅ **INTEGRATED**  
**Vault**: `jarvis-lumina`  
**URL**: `https://jarvis-lumina.vault.azure.net/`

---

## 🎯 Purpose

All secrets are stored in Azure Key Vault. The deep research system now checks Azure Key Vault for YouTube/Google API keys.

---

## 🔑 Secret Names Checked

The system tries these secret names (in order):

1. `youtube-api-key`
2. `google-api-key`
3. `google-youtube-api-key`
4. `youtube-google-api-key`

---

## ✅ Integration Status

- ✅ Azure Key Vault client integration added
- ✅ Vault URL configured: `https://jarvis-lumina.vault.azure.net/`
- ✅ Multiple secret name variations supported
- ✅ Graceful fallback if Key Vault unavailable

---

## 📋 To Add YouTube API Key to Key Vault

### Option 1: Azure CLI

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name youtube-api-key `
    --value "YOUR_API_KEY_HERE"
```

### Option 2: Azure Portal

1. Go to Azure Portal
2. Navigate to Key Vault: `jarvis-lumina`
3. Go to "Secrets"
4. Click "Generate/Import"
5. Name: `youtube-api-key`
6. Value: Your API key
7. Save

---

## 🔍 How It Works

The deep research system checks for API keys in this order:

1. **Environment Variables**: `GOOGLE_API_KEY`, `YOUTUBE_API_KEY`
2. **YouTube Channel Config**: `data/lumina_youtube_channel/channel.json`
3. **Config/Secrets Directory**: `config/secrets/google_api_key.json`
4. **Azure Key Vault** ⭐ (ALL secrets stored here)
   - Vault: `jarvis-lumina`
   - Tries multiple secret name variations
5. **n8n Integration**: (if available)

---

## 📊 Current Status

- **Azure Key Vault**: ✅ Integrated
- **Secret Names**: Multiple variations checked
- **Error Handling**: Graceful fallback
- **Next Step**: Add API key to Key Vault with one of the supported names

---

## 💡 Recommendation

Use secret name: **`youtube-api-key`** (first in the list, clearest name)

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name youtube-api-key `
    --value "YOUR_API_KEY_HERE"
```

---

**Status**: Ready to use. Just add the API key to Azure Key Vault!

