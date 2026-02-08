# AWS Bedrock Setup & Configuration for Cursor IDE

**Date**: 2025-01-24  
**Status**: ✅ **CONFIGURATION CREATED** | ⚠️ **SETUP REQUIRED**

---

## Overview

AWS Bedrock provides access to Claude and other foundation models through AWS. This guide helps you configure AWS Bedrock for use with Cursor IDE.

---

## Prerequisites

1. **AWS Account** with Bedrock access enabled
2. **AWS Credentials** (Access Key ID and Secret Access Key)
3. **Bedrock Model Access** (models must be enabled in your AWS account)

---

## Step 1: Enable Bedrock in AWS Console

1. Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Navigate to **Model access** in the left sidebar
3. **Request access** to the models you want to use:
   - **Claude 3.5 Sonnet** (recommended)
   - **Claude 3.5 Haiku**
   - **Claude 3 Opus/Sonnet/Haiku**
   - **Llama 3.1** models (if desired)
4. Wait for approval (usually instant for most models)

---

## Step 2: Get AWS Credentials

You have two options:

### Option A: AWS Access Keys (Recommended for Cursor)

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Navigate to **Users** → Select your user (or create one)
3. Go to **Security credentials** tab
4. Click **Create access key**
5. Choose **Application running outside AWS**
6. Copy the **Access Key ID** and **Secret Access Key**
   - ⚠️ **Important**: Save the Secret Access Key immediately - you won't see it again!

### Option B: AWS Credentials File

If you have AWS CLI configured, credentials are in `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
region = us-east-1
```

---

## Step 3: Determine Your Region

AWS Bedrock is available in multiple regions. Common regions:
- `us-east-1` (N. Virginia) - **Recommended**, most models available
- `us-west-2` (Oregon)
- `eu-west-1` (Ireland)
- `ap-southeast-1` (Singapore)

**Check which region has your desired models**: [AWS Bedrock Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html#regions)

---

## Step 4: Configure Cursor IDE Settings

### In Cursor Settings (JSON):

Add AWS Bedrock configuration:

```json
{
  "cursor.ai.providers": {
    "aws-bedrock": {
      "enabled": true,
      "region": "us-east-1",
      "modelId": "anthropic.claude-3-5-sonnet-20241022-v2:0",
      "credentials": {
        "accessKeyId": "YOUR_ACCESS_KEY_ID",
        "secretAccessKey": "YOUR_SECRET_ACCESS_KEY"
      }
    }
  }
}
```

### OR Use Environment Variables (More Secure):

Set environment variables (Cursor will use these automatically):

**Windows PowerShell:**
```powershell
$env:AWS_ACCESS_KEY_ID = "YOUR_ACCESS_KEY_ID"
$env:AWS_SECRET_ACCESS_KEY = "YOUR_SECRET_ACCESS_KEY"
$env:AWS_REGION = "us-east-1"
```

**Linux/Mac:**
```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
export AWS_REGION="us-east-1"
```

---

## Step 5: Store Credentials Securely (Optional but Recommended)

### Option A: Azure Key Vault (If using Azure integration)

Store AWS credentials in Azure Key Vault:

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name aws-bedrock-access-key-id `
    --value "YOUR_ACCESS_KEY_ID"

az keyvault secret set `
    --vault-name jarvis-lumina `
    --name aws-bedrock-secret-access-key `
    --value "YOUR_SECRET_ACCESS_KEY"

az keyvault secret set `
    --vault-name jarvis-lumina `
    --name aws-bedrock-region `
    --value "us-east-1"
```

### Option B: AWS Credentials File (Recommended)

Create/update `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
region = us-east-1
```

Then reference the profile in Cursor settings (if supported).

---

## Step 6: Test Configuration

### Test AWS CLI (if installed):

```bash
aws bedrock list-foundation-models --region us-east-1
```

Should return a list of available models.

### Test in Cursor:

1. Open Cursor Settings
2. Enable AWS Bedrock provider
3. Try using Chat or Composer
4. Check for errors in Cursor logs

---

## Configuration Values for Cursor

### Base URL
**Format**: `https://bedrock-runtime.{region}.amazonaws.com`

**Examples**:
- `https://bedrock-runtime.us-east-1.amazonaws.com`
- `https://bedrock-runtime.us-west-2.amazonaws.com`
- `https://bedrock-runtime.eu-west-1.amazonaws.com`

### Deployment/Model ID
Use the model ID from the models list:

**Recommended Models**:
- **Claude 3.5 Sonnet**: `anthropic.claude-3-5-sonnet-20241022-v2:0`
- **Claude 3.5 Haiku**: `anthropic.claude-3-5-haiku-20241022-v2:0`
- **Claude 3 Opus**: `anthropic.claude-3-opus-20240229-v1:0`
- **Claude 3 Sonnet**: `anthropic.claude-3-sonnet-20240229-v1:0`
- **Claude 3 Haiku**: `anthropic.claude-3-haiku-20240307-v1:0`

**Llama Models**:
- **Llama 3.1 405B**: `meta.llama3-1-405b-instruct-v1:0`
- **Llama 3.1 70B**: `meta.llama3-1-70b-instruct-v1:0`
- **Llama 3.1 8B**: `meta.llama3-1-8b-instruct-v1:0`

### API Key / Access Key ID
Your AWS Access Key ID (not a traditional API key)

### Secret Key / Secret Access Key
Your AWS Secret Access Key

### Region
AWS region where Bedrock is enabled (e.g., `us-east-1`)

---

## Cursor Settings Format

Depending on how Cursor implements AWS Bedrock, you may need:

### Format 1: Direct Configuration
```json
{
  "cursor.ai.providers.awsBedrock.enabled": true,
  "cursor.ai.providers.awsBedrock.region": "us-east-1",
  "cursor.ai.providers.awsBedrock.modelId": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "cursor.ai.providers.awsBedrock.accessKeyId": "YOUR_ACCESS_KEY_ID",
  "cursor.ai.providers.awsBedrock.secretAccessKey": "YOUR_SECRET_ACCESS_KEY"
}
```

### Format 2: Endpoint-Based (if Cursor uses endpoint)
```json
{
  "cursor.ai.providers.awsBedrock.enabled": true,
  "cursor.ai.providers.awsBedrock.endpoint": "https://bedrock-runtime.us-east-1.amazonaws.com",
  "cursor.ai.providers.awsBedrock.modelId": "anthropic.claude-3-5-sonnet-20241022-v2:0",
  "cursor.ai.providers.awsBedrock.accessKeyId": "YOUR_ACCESS_KEY_ID",
  "cursor.ai.providers.awsBedrock.secretAccessKey": "YOUR_SECRET_ACCESS_KEY"
}
```

### Format 3: Environment Variables (Most Secure)
Cursor may automatically use AWS environment variables:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_SESSION_TOKEN` (if using temporary credentials)

Then you only need to set:
```json
{
  "cursor.ai.providers.awsBedrock.enabled": true,
  "cursor.ai.providers.awsBedrock.region": "us-east-1",
  "cursor.ai.providers.awsBedrock.modelId": "anthropic.claude-3-5-sonnet-20241022-v2:0"
}
```

---

## Security Best Practices

1. **Never commit credentials** to version control
2. **Use IAM user with minimal permissions** (Bedrock read-only)
3. **Rotate access keys regularly**
4. **Use environment variables** instead of hardcoding in settings
5. **Consider using AWS IAM roles** if running on AWS infrastructure
6. **Enable CloudTrail** for audit logging (optional)

### IAM Policy (Minimal Permissions):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## Troubleshooting

### Issue: "Access Denied" or "Model not found"

**Solutions**:
1. Verify model access is enabled in AWS Bedrock Console
2. Check you're using the correct region
3. Verify IAM permissions include Bedrock invoke permissions
4. Check the model ID is correct (full ID, not just name)

### Issue: "Invalid credentials"

**Solutions**:
1. Verify Access Key ID and Secret Access Key are correct
2. Check credentials haven't expired or been rotated
3. Verify AWS credentials file format is correct
4. Test credentials with AWS CLI: `aws sts get-caller-identity`

### Issue: "Region not supported"

**Solutions**:
1. Use `us-east-1` (most models available)
2. Check [AWS Bedrock Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html#regions)
3. Verify the model is available in your selected region

### Issue: "Model access not granted"

**Solutions**:
1. Go to AWS Bedrock Console → Model access
2. Request access to the model you want to use
3. Wait for approval (usually instant)
4. Verify in the console that access is granted

---

## Cost Considerations

- **Claude 3.5 Sonnet**: ~$3-15 per 1M input tokens, ~$15-75 per 1M output tokens
- **Claude 3.5 Haiku**: ~$0.80-3 per 1M input tokens, ~$4-15 per 1M output tokens
- **Claude 3 Opus**: ~$15-75 per 1M input tokens, ~$75-375 per 1M output tokens
- Pricing varies by region

**Monitor costs** in AWS Cost Explorer or set up billing alerts.

---

## References

- **AWS Bedrock Console**: https://console.aws.amazon.com/bedrock/
- **AWS Bedrock Docs**: https://docs.aws.amazon.com/bedrock/
- **Model IDs List**: https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html
- **Cursor Docs**: https://cursor.com/docs
- **Configuration File**: `config/aws_bedrock_config.json`

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN