# Cursor Cloud Agents Configuration

**Date**: 2025-01-24  
**Issues**: 
1. Base Environment Default showing "Ubuntu" instead of "Kali-Linux"
2. Secrets management - Azure Key Vault integration

---

## Issue 1: Base Environment Default (Kali-Linux vs Ubuntu)

### Problem
Cursor Cloud Agents shows "Ubuntu" as Base Environment Default, but you want "Kali-Linux".

### Solution

#### Option A: Change in Cursor Settings UI

1. Open **Cursor Settings** (File → Preferences → Settings, or `Ctrl+,`)
2. Navigate to **Personal Configuration** → **Cloud Agents** (or **Base Environment**)
3. Find **Base Environment Default** setting
4. Change from **Ubuntu** to **Kali-Linux**
5. Save settings

#### Option B: Edit Settings JSON Directly

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Preferences: Open User Settings (JSON)"
3. Add or update the setting:

```json
{
  "cursor.cloudAgents.baseEnvironment": "kali-linux",
  "cursor.cloudAgents.defaultEnvironment": "kali-linux"
}
```

Or if the setting name is different:

```json
{
  "cursor.baseEnvironment": "kali-linux",
  "cursor.defaultEnvironment": "kali-linux"
}
```

#### Option C: Check Cursor Settings File Location

The setting might be in:
- User settings: `%APPDATA%\Cursor\User\settings.json`
- Workspace settings: `.cursor/settings.json`

Search for "ubuntu" or "environment" and update to "kali-linux".

---

## Issue 2: Secrets Management with Azure Key Vault

### Problem
Cursor Cloud Agents needs secrets (API keys, tokens), but you want to use Azure Key Vault to store all secrets.

### Solution: Azure Key Vault Integration

Cursor doesn't have direct Azure Key Vault integration, but you can:

#### Step 1: Store Secrets in Azure Key Vault

All secrets should be stored in Azure Key Vault (`jarvis-lumina`):

```powershell
# GitHub Token
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name github-personal-access-token `
    --value "ghp_YOUR_TOKEN"

# Azure OpenAI API Key
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name azure-openai-api-key `
    --value "YOUR_API_KEY"

# AWS Bedrock Access Key ID
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name aws-bedrock-access-key-id `
    --value "YOUR_ACCESS_KEY_ID"

# AWS Bedrock Secret Access Key
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name aws-bedrock-secret-access-key `
    --value "YOUR_SECRET_ACCESS_KEY"

# Any other secrets...
```

#### Step 2: Retrieve Secrets for Cursor Configuration

Since Cursor needs the secrets directly (not from Key Vault), you have two approaches:

**Approach A: Manual Retrieval (One-time setup)**

1. Retrieve secrets from Key Vault
2. Paste into Cursor Settings
3. Update when secrets rotate

```powershell
# Get GitHub token
az keyvault secret show `
    --vault-name jarvis-lumina `
    --name github-personal-access-token `
    --query "value" -o tsv

# Get Azure OpenAI key
az keyvault secret show `
    --vault-name jarvis-lumina `
    --name azure-openai-api-key `
    --query "value" -o tsv

# Get AWS credentials
az keyvault secret show `
    --vault-name jarvis-lumina `
    --name aws-bedrock-access-key-id `
    --query "value" -o tsv
```

**Approach B: Helper Script (Automated)**

Create a script to retrieve secrets and update Cursor settings (if Cursor supports programmatic configuration).

#### Step 3: Configure Secrets in Cursor

In Cursor Settings → **Personal Configuration** → **Secrets** (or **Cloud Agents** → **Secrets**):

1. **GitHub Token**: Paste GitHub Personal Access Token
2. **Azure OpenAI API Key**: Paste Azure OpenAI API key
3. **AWS Bedrock Credentials**: Paste AWS Access Key ID and Secret Access Key
4. **Other secrets**: Add as needed

---

## Recommended Secret Names in Azure Key Vault

For consistency, use these secret names in Azure Key Vault:

### GitHub
- `github-personal-access-token` - GitHub PAT for repository access

### Azure OpenAI
- `azure-openai-api-key` - Azure OpenAI API key
- `azure-openai-resource-name` - Resource name (optional)
- `azure-openai-deployment-name` - Deployment name (optional)

### AWS Bedrock
- `aws-bedrock-access-key-id` - AWS Access Key ID
- `aws-bedrock-secret-access-key` - AWS Secret Access Key
- `aws-bedrock-region` - AWS Region (optional)

### Other Common Secrets
- `anthropic-api-key` - Anthropic API key
- `openai-api-key` - Direct OpenAI API key (if needed, though Azure OpenAI preferred)
- Any other API keys or tokens

---

## Helper Script: Retrieve Secrets for Cursor

Create a PowerShell script to retrieve secrets:

```powershell
# scripts/retrieve_cursor_secrets.ps1
$vaultName = "jarvis-lumina"

Write-Host "Retrieving secrets from Azure Key Vault..." -ForegroundColor Cyan

# GitHub Token
$githubToken = az keyvault secret show `
    --vault-name $vaultName `
    --name github-personal-access-token `
    --query "value" -o tsv 2>$null

if ($githubToken) {
    Write-Host "`nGitHub Personal Access Token:" -ForegroundColor Green
    Write-Host $githubToken
    Write-Host "`nCopy this token to Cursor Settings → Personal Configuration → GitHub Access"
}

# Azure OpenAI API Key
$azureOpenAIKey = az keyvault secret show `
    --vault-name $vaultName `
    --name azure-openai-api-key `
    --query "value" -o tsv 2>$null

if ($azureOpenAIKey) {
    Write-Host "`nAzure OpenAI API Key:" -ForegroundColor Green
    Write-Host $azureOpenAIKey
    Write-Host "`nCopy this key to Cursor Settings → Azure OpenAI → API Key"
}

# AWS Bedrock Access Key ID
$awsAccessKey = az keyvault secret show `
    --vault-name $vaultName `
    --name aws-bedrock-access-key-id `
    --query "value" -o tsv 2>$null

if ($awsAccessKey) {
    Write-Host "`nAWS Bedrock Access Key ID:" -ForegroundColor Green
    Write-Host $awsAccessKey
}

# AWS Bedrock Secret Access Key
$awsSecretKey = az keyvault secret show `
    --vault-name $vaultName `
    --name aws-bedrock-secret-access-key `
    --query "value" -o tsv 2>$null

if ($awsSecretKey) {
    Write-Host "`nAWS Bedrock Secret Access Key:" -ForegroundColor Green
    Write-Host $awsSecretKey
    Write-Host "`nCopy these to Cursor Settings → AWS Bedrock → Credentials"
}

Write-Host "`n✅ Secrets retrieved. Copy values to Cursor Settings manually." -ForegroundColor Yellow
Write-Host "⚠️  Note: Cursor does not have direct Azure Key Vault integration." -ForegroundColor Yellow
Write-Host "   You must copy secrets from Key Vault to Cursor Settings." -ForegroundColor Yellow
```

---

## Security Best Practices

1. **Never Commit Secrets**:
   - Secrets in Cursor Settings are stored locally
   - Never commit Cursor settings files with secrets to version control
   - Use `.gitignore` to exclude settings files with secrets

2. **Rotate Secrets Regularly**:
   - Update secrets in Azure Key Vault
   - Retrieve new secrets
   - Update Cursor Settings
   - Revoke old secrets

3. **Use Minimum Required Permissions**:
   - GitHub tokens: Only `repo` scope
   - AWS credentials: Only Bedrock permissions
   - Azure keys: Only required permissions

4. **Monitor Secret Usage**:
   - Check Azure Key Vault access logs
   - Review secret access patterns
   - Set up alerts for unusual access

5. **Key Vault Access Control**:
   - Use Managed Identity when possible (for scripts/services)
   - Use Azure RBAC for Key Vault access
   - Limit who can read secrets

---

## Future: Direct Key Vault Integration (If Available)

If Cursor adds Azure Key Vault integration in the future, configuration might look like:

```json
{
  "cursor.secrets.provider": "azure-key-vault",
  "cursor.secrets.vaultName": "jarvis-lumina",
  "cursor.secrets.vaultUrl": "https://jarvis-lumina.vault.azure.net/",
  "cursor.secrets.authentication": "default-azure-credential",
  "cursor.secrets.secretMappings": {
    "github-token": "github-personal-access-token",
    "azure-openai-key": "azure-openai-api-key",
    "aws-bedrock-access-key": "aws-bedrock-access-key-id",
    "aws-bedrock-secret-key": "aws-bedrock-secret-access-key"
  }
}
```

**Note**: This is hypothetical - Cursor doesn't currently support this. Monitor Cursor updates for Key Vault integration.

---

## Troubleshooting

### Issue: Can't find "Base Environment" setting

**Solutions**:
1. Look for "Cloud Agents" section in settings
2. Search settings for "environment" or "ubuntu"
3. Check if setting is in Cloud Agents specific section
4. Update Cursor to latest version

### Issue: Setting doesn't save

**Solutions**:
1. Ensure you have write permissions to settings file
2. Check if setting name is correct
3. Try restarting Cursor after changing setting
4. Check Cursor logs for errors

### Issue: Secrets not working after copying from Key Vault

**Solutions**:
1. Verify secret was copied completely (no truncation)
2. Check for extra spaces or newlines
3. Verify secret hasn't expired
4. Test secret directly (e.g., test GitHub token with `gh auth status`)
5. Check Cursor logs for authentication errors

---

## Quick Reference

### Base Environment Setting
- **Current**: Ubuntu
- **Desired**: Kali-Linux
- **Location**: Cursor Settings → Personal Configuration → Cloud Agents → Base Environment Default

### Secrets Storage
- **Primary**: Azure Key Vault (`jarvis-lumina`)
- **Cursor**: Manual entry in Cursor Settings
- **Workflow**: Retrieve from Key Vault → Copy to Cursor Settings

### Key Vault Secrets
- `github-personal-access-token`
- `azure-openai-api-key`
- `aws-bedrock-access-key-id`
- `aws-bedrock-secret-access-key`

---

## References

- **Azure Key Vault**: https://portal.azure.com (vault: `jarvis-lumina`)
- **Cursor Docs**: https://cursor.com/docs
- **GitHub Token Setup**: `docs/system/CURSOR_GITHUB_ACCESS_SETUP.md`
- **Azure OpenAI Setup**: `docs/system/AZURE_OPENAI_SETUP.md`
- **AWS Bedrock Setup**: `docs/system/AWS_BEDROCK_SETUP.md`

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN