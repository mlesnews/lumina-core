# Azure OpenAI Service Setup & Configuration

**Date**: 2025-01-24  
**Status**: ✅ **CONFIGURATION CREATED** | ⚠️ **SETUP REQUIRED**  
**Policy**: **ALL OpenAI requests MUST route through Azure OpenAI Service**

---

## Overview

All OpenAI API requests are **enforced** to route through Azure OpenAI Service for:
- **Security**: Enterprise-grade security and compliance
- **Cost Management**: Better cost tracking and control
- **Compliance**: Audit trails and data residency controls
- **Performance**: Azure's global infrastructure

**Direct OpenAI.com access is BLOCKED** by configuration.

---

## Configuration Files

### 1. Azure OpenAI Configuration
**File**: `config/azure_openai_config.json`

This file contains the Azure OpenAI Service configuration including:
- Resource name and endpoint
- Deployment names for different models
- Authentication via Azure Key Vault
- API version and default parameters

### 2. Cloud API Blocker
**File**: `config/cloud_api_blocker.json`

Updated to:
- ✅ **Allow**: `azure_openai`
- ❌ **Block**: `openai` (direct OpenAI.com access)

---

## Setup Steps

### Step 1: Create Azure OpenAI Resource

1. Go to [Azure Portal](https://portal.azure.com)
2. Create a new **Azure OpenAI** resource:
   - Resource Group: `jarvis-lumina-rg` (or your preferred group)
   - Resource Name: `jarvis-lumina-openai` (or your preferred name)
   - Location: Choose appropriate region
   - Pricing Tier: Select based on your needs

3. **Note the Resource Name** - you'll need this for configuration

### Step 2: Deploy Models

1. In Azure Portal, navigate to your Azure OpenAI resource
2. Go to **Model deployments**
3. Deploy the models you need:
   - **GPT-4** (or GPT-4 Turbo): For chat completions
   - **GPT-3.5 Turbo**: For faster/cheaper completions
   - **text-embedding-ada-002**: For embeddings
   - **tts-1**: For text-to-speech (if needed)

4. **Note the Deployment Names** - you'll need these for configuration

### Step 3: Get API Key

1. In Azure Portal, navigate to your Azure OpenAI resource
2. Go to **Keys and Endpoint**
3. Copy **Key 1** (or Key 2)
4. Copy the **Endpoint** URL (format: `https://YOUR-RESOURCE-NAME.openai.azure.com`)

### Step 4: Store Secrets in Azure Key Vault

Store the API key in Azure Key Vault:

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name azure-openai-api-key `
    --value "<your-api-key-here>"
```

### Step 5: Configure Environment Variables (Optional)

Alternatively, you can set environment variables (though Key Vault is preferred):

```powershell
$env:AZURE_OPENAI_RESOURCE_NAME = "jarvis-lumina-openai"
$env:AZURE_OPENAI_DEPLOYMENT_NAME = "gpt-4"
$env:AZURE_OPENAI_API_KEY = "<your-api-key>"
```

### Step 6: Update Configuration File

Edit `config/azure_openai_config.json` and replace placeholders:

```json
{
  "azure_openai": {
    "resource_name": "jarvis-lumina-openai",  // Replace with your resource name
    "deployment_name": "gpt-4",  // Replace with your deployment name
    "deployments": {
      "default": {
        "name": "gpt-4"  // Replace with your deployment name
      },
      "gpt4": {
        "name": "gpt-4"  // Replace with your deployment name
      }
      // ... update other deployments as needed
    }
  }
}
```

---

## Configuration Details

### Endpoint Format

Azure OpenAI endpoints follow this format:
```
https://{resource_name}.openai.azure.com/openai/deployments/{deployment_name}/chat/completions?api-version=2024-02-15-preview
```

### Authentication

The system uses Azure Key Vault for authentication:

**Secret Name**: `azure-openai-api-key`

**Vault**: `jarvis-lumina` (or configured vault name)

**Fallback**: Environment variable `AZURE_OPENAI_API_KEY`

### API Version

Default API version: `2024-02-15-preview`

This can be configured in `azure_openai_config.json`.

---

## Usage in Code

### Python OpenAI Client with Azure

When using the OpenAI Python SDK with Azure OpenAI:

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=api_key,  # From Azure Key Vault
    api_version="2024-02-15-preview",
    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4",  # Deployment name, not model name
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
```

**Important**: 
- Use **deployment name** (not model name like "gpt-4")
- Endpoint must be the Azure endpoint (not api.openai.com)

### Router Integration

The `JARVISLocalFirstLLMRouter` automatically uses Azure OpenAI when cloud fallback is enabled:

```python
from jarvis_local_first_llm_router import JARVISLocalFirstLLMRouter, LLMProvider

router = JARVISLocalFirstLLMRouter(project_root)

# Azure OpenAI will be used automatically if local providers fail
# and cloud_fallback_enabled is True
```

---

## Migration from Direct OpenAI

### Before (Blocked)
```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ❌ BLOCKED
```

### After (Required)
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=key_vault.get_secret("azure-openai-api-key"),
    api_version="2024-02-15-preview",
    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com"
)  # ✅ REQUIRED
```

---

## Verification

### Test Azure OpenAI Connection

You can test the connection using Azure CLI:

```powershell
az openai chat completions create `
    --resource-group jarvis-lumina-rg `
    --resource-name jarvis-lumina-openai `
    --deployment-name gpt-4 `
    --messages '[{"role":"user","content":"Hello!"}]'
```

### Check Configuration

The system will log warnings if Azure OpenAI is not properly configured:

```
⚠️  Azure OpenAI resource name not configured. Set AZURE_OPENAI_RESOURCE_NAME or configure azure_openai_config.json
```

---

## Troubleshooting

### Issue: "Resource not found"

**Solution**: 
- Verify the resource name in configuration matches your Azure resource
- Check that the resource exists in the correct subscription

### Issue: "Authentication failed"

**Solution**:
- Verify API key is stored in Azure Key Vault as `azure-openai-api-key`
- Check Key Vault access permissions
- Verify the API key is valid (not expired/regenerated)

### Issue: "Deployment not found"

**Solution**:
- Verify deployment name matches exactly (case-sensitive)
- Check that the deployment exists in your Azure OpenAI resource
- Verify the deployment is in "Succeeded" status

### Issue: "Model not found"

**Solution**:
- Use deployment name, not model name
- Verify the deployment is for the correct model type
- Check deployment status in Azure Portal

---

## Security Notes

1. **Never commit API keys** to version control
2. **Always use Azure Key Vault** for secrets (preferred method)
3. **Use Managed Identity** when running in Azure (recommended for production)
4. **Enable Private Endpoints** for production (recommended)
5. **Monitor usage** via Azure Monitor and cost alerts

---

## Cost Management

- Azure OpenAI pricing is per-token usage
- Set up **cost alerts** in Azure Portal
- Monitor usage via Azure Cost Management
- Consider **reserved capacity** for predictable workloads

---

## References

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure OpenAI Python SDK](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?pivots=programming-language-python)
- [Azure Key Vault Documentation](https://learn.microsoft.com/azure/key-vault/)
- Configuration: `config/azure_openai_config.json`
- Blocker Config: `config/cloud_api_blocker.json`

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN  
**Status**: ✅ Configuration Ready | ⚠️ Setup Required