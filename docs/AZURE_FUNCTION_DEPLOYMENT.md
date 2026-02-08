# Azure Function Deployment Guide

## Current Status

✅ **Azure is available and logged in**  
❌ **Azure Function not yet deployed**  
✅ **Function code ready in `azure_functions/RenderIronLegion/`**

## Deployment Options

### Option 1: Azure Portal (Easiest)

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Function App: `jarvis-lumina-functions`
3. Go to **Functions** → **Create**
4. Choose **HTTP trigger**
5. Name it: `RenderIronLegion`
6. Copy code from `azure_functions/RenderIronLegion/__init__.py`
7. Save and test

### Option 2: Azure Functions Core Tools

```bash
# Install (if not installed)
npm install -g azure-functions-core-tools@4

# Login
func azure login

# Deploy
cd azure_functions
func azure functionapp publish jarvis-lumina-functions
```

### Option 3: Azure CLI

```bash
# Install Azure CLI first
# https://aka.ms/installazurecliwindows

# Login
az login

# Deploy
cd azure_functions
func azure functionapp publish jarvis-lumina-functions
```

### Option 4: VS Code Extension

1. Install "Azure Functions" extension in VS Code
2. Open `azure_functions` folder
3. Right-click → **Deploy to Function App**
4. Select `jarvis-lumina-functions`

## What Happens Now

**Current behavior**: The system gracefully falls back to local rendering since the remote endpoint doesn't exist yet. This is working as designed - no errors, just local CPU usage.

**After deployment**: Once the function is deployed, the system will automatically start using remote rendering, offloading compute to Azure.

## Testing After Deployment

```bash
python scripts/python/test_azure_function.py
```

This will verify the endpoint is accessible and responding.

## Function Requirements

The function needs:
- Python 3.9+ runtime
- Pillow library (included in requirements.txt)
- HTTP trigger with POST method

All of this is configured in the function template.
