# Azure Key Vault Security Configuration

## NO SECRETS IN THE CLEAR! 🔐

All API keys and secrets are stored securely in Azure Key Vault.

## Vault Details

| Property | Value |
|----------|-------|
| **Vault Name** | `jarvis-lumina` |
| **Vault URL** | `https://jarvis-lumina.vault.azure.net/` |
| **Total Secrets** | 57+ |
| **Authentication** | Azure Default Credential |

## Startup Configuration

At every Windows login, the LUMINA Secure Startup script:
1. Connects to Azure Key Vault
2. Retrieves all configured API keys
3. Sets environment variables for each secret
4. Apps use env vars (no plaintext secrets)

### Startup Files

| File | Purpose |
|------|---------|
| `scripts/startup/lumina_secure_startup.ps1` | Main startup script |
| `scripts/startup/install_startup.ps1` | Installer |
| `scripts/python/get_vault_secret.py` | Python retrieval utility |
| `scripts/python/add_secret_to_vault.py` | Add new secrets |
| `scripts/python/set_wakatime_env.py` | WakaTime-specific retrieval |

### Installation Location

```
C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
├── LUMINA-Secure-Startup.lnk
└── LUMINA-Secure-Startup.bat
```

## Current Secrets in Vault

### AI Provider API Keys
| Secret Name | Environment Variable | Status |
|-------------|---------------------|--------|
| `wakatime-api-key` | `WAKATIME_API_KEY` | ✅ Configured |
| `openai-api-key` | `OPENAI_API_KEY` | ⚠️ Add when needed |
| `anthropic-api-key` | `ANTHROPIC_API_KEY` | ⚠️ Add when needed |
| `azure-openai-api-key` | `AZURE_OPENAI_API_KEY` | ⚠️ Add when needed |
| `google-ai-api-key` | `GOOGLE_AI_API_KEY` | ⚠️ Add when needed |
| `elevenlabs-api-key` | `ELEVENLABS_API_KEY` | ⚠️ Add when needed |
| `deepseek-api-key` | `DEEPSEEK_API_KEY` | ⚠️ Add when needed |
| `mistral-api-key` | `MISTRAL_API_KEY` | ⚠️ Add when needed |
| `groq-api-key` | `GROQ_API_KEY` | ⚠️ Add when needed |
| `xai-api-key` | `XAI_API_KEY` | ⚠️ Add when needed |
| `openrouter-api-key` | `OPENROUTER_API_KEY` | ⚠️ Add when needed |

### Infrastructure Secrets (Already Configured)
- `azure-speech-key` / `azure-speech-region`
- `huggingface-token`
- `youtube-api-key`
- `nas-username` / `nas-password`
- `pfsense-username` / `pfsense-password`
- `mariadb-root-password`
- `n8n-*` credentials
- `cursor-session-token-*`
- And 40+ more...

## Adding New Secrets

### Method 1: Python Script (Recommended)
```bash
# Add with value prompt (secure)
python scripts/python/add_secret_to_vault.py --name openai-api-key

# Add with value directly
python scripts/python/add_secret_to_vault.py --name openai-api-key --value sk-xxx

# List all secrets
python scripts/python/add_secret_to_vault.py --list
```

### Method 2: Azure CLI
```bash
az keyvault secret set --vault-name jarvis-lumina --name openai-api-key --value "sk-xxx"
```

### Method 3: Azure Portal
1. Go to https://portal.azure.com
2. Navigate to Key Vaults → jarvis-lumina
3. Click Secrets → Generate/Import
4. Enter name and value

## Security Audit

Run the secrets audit to check for any plaintext secrets:
```bash
python scripts/python/audit_secrets_in_clear.py
```

## Configuration Files

### Secure WakaTime Config
`config/wakatime_secure_config.json`
```json
{
  "security": {
    "storage": "azure_key_vault",
    "vault_url": "https://jarvis-lumina.vault.azure.net/",
    "secret_name": "wakatime-api-key",
    "plaintext_allowed": false
  }
}
```

### .wakatime.cfg (Key Removed)
```ini
[settings]
# API key retrieved securely from Azure Key Vault
# DO NOT store API keys in this file!
api_key_vault = jarvis-lumina
api_key_secret = wakatime-api-key
```

## Testing

### Verify Startup Script
```powershell
powershell -ExecutionPolicy Bypass -File "scripts\startup\lumina_secure_startup.ps1"
```

### Check Environment Variables
```powershell
[System.Environment]::GetEnvironmentVariable("WAKATIME_API_KEY", "User")
```

### Verify Vault Access
```bash
python scripts/python/add_secret_to_vault.py --list
```

## Troubleshooting

### "Could not connect to vault"
1. Ensure Azure CLI is logged in: `az login`
2. Or ensure Azure identity is configured
3. Check network connectivity to Azure

### "Secret not found"
1. Add the secret: `python scripts/python/add_secret_to_vault.py --name <name>`
2. Verify it exists: `--list`

### "Environment variable not set"
1. Run startup script manually
2. Check logs in `logs/startup_*.log`
3. Restart terminal/IDE to pick up new env vars

---

**Remember: NO SECRETS IN THE CLEAR!** 🔐

All sensitive data flows through Azure Key Vault.
