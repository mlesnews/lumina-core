# Store ElevenLabs API Key in Azure Key Vault
**Quick Guide**

---

## Quick Start

### Step 1: Authenticate Azure (if needed)
```powershell
az login
```

### Step 2: Store the Key

**Option A: Clipboard (Easiest)**
1. Copy your ElevenLabs API key to clipboard
2. Run:
```powershell
python scripts/python/jarvis_store_elevenlabs_key.py --clipboard --all-variations
```

**Option B: Interactive (Most Secure)**
```powershell
python scripts/python/jarvis_store_elevenlabs_key.py --interactive --all-variations
```

---

## What `--all-variations` Does

Stores the key under multiple names so JARVIS can find it:
- `Cursor - Cursor API Key` (exact ElevenLabs webui name)
- `elevenlabs-api-key`
- `cursor-api-key`
- `cursor-cursor-api-key`

---

## Troubleshooting

### Timeout Issues
If the script times out:
1. Run `az login` first
2. Check Azure Key Vault permissions
3. Verify vault URL: `https://jarvis-lumina.vault.azure.net/`

### Authentication Required
```
❌ Azure Key Vault operation timed out
💡 Run: az login
```

---

## After Storing

Test that it works:
```powershell
python scripts/python/jarvis_ralt_hybrid_macro.py --test --context work_shift
```

You should see TTS audio working now!

---

**Last Updated**: 2026-01-06
