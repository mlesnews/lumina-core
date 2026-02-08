# Cursor AWS Bedrock Quick Setup Guide

**Date**: 2025-01-24  
**Status**: ⚠️ **SETUP REQUIRED**  
**Tag**: @JARVIS @MARVIN @TRIAD

---

## The Problem

You're seeing this error:
```
Selected model is not supported by bedrock, please use a different model
```

This means **Bedrock is enabled in Cursor but not configured with AWS credentials**.

---

## Solution Options

### Option 1: Configure Bedrock with AWS Credentials (Recommended if you want Bedrock)

If you want to use AWS Bedrock models (Claude, Llama, etc.), you need to configure AWS credentials.

#### Step 1: Get Your AWS Credentials

You need these from your **@PASSWD @TRIAD** password manager or AWS account:

1. **AWS Access Key ID** (starts with `AKIA...`)
2. **AWS Secret Access Key** (long secret string)
3. **AWS Region** (e.g., `us-east-1`, `us-west-2`)

**Where to find them:**
- **TRIAD Password Manager**: Look for "AWS Bedrock" or "AWS Credentials"
- **AWS Console**: IAM → Users → Your User → Security credentials → Access keys
- **ProtonPass/Dashlane**: Search for "AWS" or "Bedrock"

#### Step 2: Store Credentials in Azure Key Vault (Recommended)

**All secrets MUST be stored in Azure Key Vault** per LUMINA security policy.

```powershell
# Run the helper script
.\scripts\store_aws_bedrock_credentials.ps1
```

This script will:
- Prompt for your AWS credentials
- Store them securely in Azure Key Vault (`jarvis-lumina`)
- Use secret names: `aws-bedrock-access-key-id`, `aws-bedrock-secret-access-key`, `aws-bedrock-region`

#### Step 3: Retrieve Credentials for Cursor

```powershell
# Run the retrieval script
.\scripts\retrieve_cursor_secrets.ps1
```

This will display your credentials. **Copy them** - you'll need to paste them into Cursor.

#### Step 4: Configure Cursor Settings

**Method A: Via Cursor UI (Recommended)**

1. Open **Cursor Settings** (`Ctrl+,` or File → Preferences → Settings)
2. Navigate to **Personal Configuration** → **AWS Bedrock** (or search for "Bedrock")
3. Enter the credentials:
   - **Access Key ID**: Paste your AWS Access Key ID
   - **Secret Access Key**: Paste your AWS Secret Access Key
   - **Region**: Enter your AWS region (e.g., `us-east-1`)
4. **Save** settings
5. **Restart Cursor**

**Method B: Via Settings JSON (Advanced)**

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Preferences: Open User Settings (JSON)"
3. Add Bedrock configuration (format depends on Cursor version):

```json
{
  "cursor.ai.providers.awsBedrock.enabled": true,
  "cursor.ai.providers.awsBedrock.region": "us-east-1",
  "cursor.ai.providers.awsBedrock.accessKeyId": "YOUR_ACCESS_KEY_ID",
  "cursor.ai.providers.awsBedrock.secretAccessKey": "YOUR_SECRET_ACCESS_KEY",
  "cursor.ai.providers.awsBedrock.modelId": "anthropic.claude-3-5-sonnet-20241022-v2:0"
}
```

**Note**: The exact setting names may vary by Cursor version. Check Cursor's documentation or use the UI method.

#### Step 5: Enable Model Access in AWS

1. Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Navigate to **Model access**
3. **Request access** to models you want:
   - Claude 3.5 Sonnet (recommended)
   - Claude 3.5 Haiku
   - Llama 3.1 models
4. Wait for approval (usually instant)

#### Step 6: Test Configuration

1. In Cursor, open the **model selector** (top-right)
2. Look for **Bedrock** or **Claude** models
3. Select a Bedrock model
4. Try using Chat or Composer
5. If it works, you're done! ✅

---

### Option 2: Disable Bedrock (Use Ollama Only)

If you **don't want to use Bedrock** and prefer to stick with your local Ollama models (ULTRON, KAIJU), you can disable Bedrock:

#### Step 1: Disable Bedrock in Cursor UI

1. Open **Cursor Settings** (`Ctrl+,`)
2. Navigate to **Personal Configuration** → **AWS Bedrock**
3. **Disable** or **Remove** Bedrock configuration
4. **Save** settings

#### Step 2: Ensure Ollama Models Are Selected

1. Open the **model selector** in Cursor (top-right)
2. Select an **Ollama model**:
   - **ULTRON** (recommended - qwen2.5:72b)
   - **KAIJU** (llama3)
   - **ULTRON Router** (smart routing)
3. Verify Ollama is running:
   ```powershell
   curl http://localhost:11434/api/tags
   ```

#### Step 3: Verify Settings

Your workspace settings (`.cursor/settings.json`) already have Ollama configured correctly. Just make sure Cursor's model selector is using an Ollama model, not Bedrock.

---

## Troubleshooting

### Issue: "Selected model is not supported by bedrock"

**Cause**: Bedrock is enabled but not configured with credentials.

**Solutions**:
1. **Configure Bedrock** (Option 1 above), OR
2. **Disable Bedrock** and use Ollama (Option 2 above)

### Issue: "Invalid credentials" or "Access denied"

**Solutions**:
1. Verify credentials are correct (no extra spaces)
2. Check AWS IAM permissions include Bedrock access
3. Verify region is correct
4. Test credentials with AWS CLI:
   ```powershell
   aws sts get-caller-identity
   ```

### Issue: "Model access not granted"

**Solutions**:
1. Go to AWS Bedrock Console → Model access
2. Request access to the model
3. Wait for approval

### Issue: Can't find Bedrock settings in Cursor

**Solutions**:
1. Update Cursor to latest version
2. Look in "Personal Configuration" → "Cloud Providers" → "AWS Bedrock"
3. Search settings for "bedrock" or "aws"
4. Check if Bedrock is available in your Cursor plan

---

## Quick Reference

### Credential Storage
- **Primary**: Azure Key Vault (`jarvis-lumina`)
- **Secret Names**:
  - `aws-bedrock-access-key-id`
  - `aws-bedrock-secret-access-key`
  - `aws-bedrock-region`

### Scripts
- **Store credentials**: `.\scripts\store_aws_bedrock_credentials.ps1`
- **Retrieve credentials**: `.\scripts\retrieve_cursor_secrets.ps1`

### Documentation
- **AWS Bedrock Setup**: `docs/system/AWS_BEDROCK_SETUP.md`
- **Cloud Agents Config**: `docs/system/CURSOR_CLOUD_AGENTS_CONFIG.md`
- **TRIAD Password Manager**: `docs/system/TRIAD_PASSWORD_MANAGER_SYSTEM.md`

### Recommended Models
- **Claude 3.5 Sonnet**: `anthropic.claude-3-5-sonnet-20241022-v2:0` (best quality)
- **Claude 3.5 Haiku**: `anthropic.claude-3-5-haiku-20241022-v2:0` (faster, cheaper)
- **Llama 3.1 70B**: `meta.llama3-1-70b-instruct-v1:0` (open source alternative)

---

## Security Notes

⚠️ **IMPORTANT**:
1. **Never commit credentials** to version control
2. **Store all secrets in Azure Key Vault** (per LUMINA policy)
3. **Use IAM user with minimal permissions** (Bedrock read-only)
4. **Rotate credentials regularly**
5. **Monitor AWS costs** (Bedrock charges per token)

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN
