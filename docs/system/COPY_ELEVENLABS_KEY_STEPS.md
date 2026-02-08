# How to Copy ElevenLabs API Key

## Steps to Get Your CURSOR-IDE-APIKEY

1. **In ElevenLabs webui**, find the entry showing:
   ```
   Basic Authentication • CURSOR • Unused
   ```

2. **Click on it** to reveal the actual API key value

3. **Copy the key string** (it will look like a long alphanumeric string, possibly starting with `sk-` or similar)

4. **Paste it** - I'll store it immediately

---

## After You Copy It

Once the key is in your clipboard, tell me and I'll run:
```powershell
.\scripts\powershell\store_elevenlabs_key.ps1
```

This will store it securely in Azure Key Vault under multiple names:
- `Cursor - Cursor API Key`
- `elevenlabs-api-key`
- `cursor-api-key`
- `cursor-cursor-api-key`

---

**Ready when you are!** Just copy the actual key value and let me know. 🔐
