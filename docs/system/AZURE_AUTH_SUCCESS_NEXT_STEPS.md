# Azure Authentication Complete - Next Steps

✅ **Azure login successful!**

Now you can store your ElevenLabs API key in Azure Key Vault.

---

## Store Your API Key

### Option 1: Clipboard (Easiest)
1. Copy your ElevenLabs API key to clipboard
2. Run:
```powershell
python scripts/python/jarvis_store_elevenlabs_key.py --clipboard --all-variations
```

### Option 2: Interactive (Most Secure)
```powershell
python scripts/python/jarvis_store_elevenlabs_key.py --interactive --all-variations
```

The `--all-variations` flag stores it under multiple names:
- `Cursor - Cursor API Key` (exact ElevenLabs webui name)
- `elevenlabs-api-key`
- `cursor-api-key`
- `cursor-cursor-api-key`

This ensures JARVIS can find it no matter which name it checks first.

---

## After Storing

Test that TTS works:
```powershell
python scripts/python/jarvis_ralt_hybrid_macro.py --test --context work_shift
```

You should now hear JARVIS speak the greeting!

---

**Ready to proceed?**
