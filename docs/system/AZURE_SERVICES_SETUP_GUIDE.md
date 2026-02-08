# Azure Services Setup Guide

## Overview

This guide helps you configure all Azure services for LUMINA by adding required secrets to Azure Key Vault.

## Prerequisites

✅ **Azure SDKs Installed** - All required Azure SDK packages are now installed
✅ **Key Vault Access** - Successfully connected to `jarvis-lumina` Key Vault

## Required Secrets

The following secrets need to be added to Azure Key Vault: `jarvis-lumina`

### 1. Service Bus
- **Secret Name**: `azure-service-bus-connection-string`
- **Description**: Service Bus namespace connection string
- **Format**: `Endpoint=sb://<namespace>.servicebus.windows.net/;SharedAccessKeyName=...;SharedAccessKey=...`
- **How to Get**:
  1. Go to Azure Portal → Service Bus namespaces → `jarvis-lumina-sb`
  2. Go to "Shared access policies"
  3. Select a policy (or create new) with "Listen" and "Send" permissions
  4. Copy the "Primary Connection String"

### 2. Storage Account
- **Secret Name**: `azure-storage-connection-string`
- **Description**: Storage account connection string
- **Format**: `DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net`
- **How to Get**:
  1. Go to Azure Portal → Storage accounts → `jarvisluminastorage`
  2. Go to "Access keys"
  3. Copy "Connection string" from Key1 or Key2

### 3. Event Grid
- **Secret Name**: `azure-event-grid-key`
- **Description**: Event Grid topic access key
- **Format**: Access key from Event Grid topic
- **How to Get**:
  1. Go to Azure Portal → Event Grid Topics
  2. Select your topic (e.g., `jarvis-system-events`)
  3. Go to "Access keys"
  4. Copy "Key 1" or "Key 2"

- **Secret Name**: `azure-event-grid-endpoint`
- **Description**: Event Grid topic endpoint URL
- **Format**: `https://<topic-name>.<region>-1.eventgrid.azure.net/api/events`
- **How to Get**: Same Event Grid topic page, copy "Topic endpoint"

### 4. Cognitive Services - Speech
- **Secret Name**: `cognitive-speech-key`
- **Description**: Speech service API key
- **Format**: API key from Azure Speech resource
- **How to Get**:
  1. Go to Azure Portal → Cognitive Services → `jarvis-lumina-speech`
  2. Go to "Keys and Endpoint"
  3. Copy "Key 1" or "Key 2"

### 5. Cognitive Services - Text Analytics
- **Secret Name**: `cognitive-text-analytics-key`
- **Description**: Text Analytics API key
- **Format**: API key from Azure Text Analytics resource
- **How to Get**:
  1. Go to Azure Portal → Cognitive Services → `jarvis-lumina-text-analytics`
  2. Go to "Keys and Endpoint"
  3. Copy "Key 1" or "Key 2"

### 6. Cognitive Services - Vision
- **Secret Name**: `cognitive-vision-key`
- **Description**: Computer Vision API key
- **Format**: API key from Azure Computer Vision resource
- **How to Get**:
  1. Go to Azure Portal → Cognitive Services → `jarvis-lumina-vision`
  2. Go to "Keys and Endpoint"
  3. Copy "Key 1" or "Key 2"

### 7. Cosmos DB
- **Secret Name**: `cosmos-db-endpoint`
- **Description**: Cosmos DB account endpoint URL
- **Format**: `https://<account-name>.documents.azure.com:443/`
- **How to Get**:
  1. Go to Azure Portal → Azure Cosmos DB → `jarvis-lumina-cosmos`
  2. Go to "Keys"
  3. Copy "URI"

- **Secret Name**: `cosmos-db-key`
- **Description**: Cosmos DB account primary key
- **Format**: Primary key from Cosmos DB account
- **How to Get**: Same Cosmos DB page, copy "Primary Key"

### 8. Application Insights
- **Secret Name**: `app-insights-instrumentation-key`
- **Description**: Application Insights instrumentation key
- **Format**: Instrumentation key from Application Insights resource
- **How to Get**:
  1. Go to Azure Portal → Application Insights → `jarvis-lumina-insights`
  2. Go to "Overview"
  3. Copy "Instrumentation Key"

## Adding Secrets to Key Vault

### Option 1: Azure Portal (Recommended)

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to: **Key Vaults** → **jarvis-lumina**
3. Click **Secrets** in the left menu
4. Click **Generate/Import** for each secret
5. Enter the secret name and value
6. Click **Create**

### Option 2: Azure CLI

```bash
# Login to Azure
az login

# Set each secret
az keyvault secret set --vault-name jarvis-lumina --name azure-service-bus-connection-string --value "<connection-string>"
az keyvault secret set --vault-name jarvis-lumina --name azure-storage-connection-string --value "<connection-string>"
az keyvault secret set --vault-name jarvis-lumina --name azure-event-grid-key --value "<key>"
az keyvault secret set --vault-name jarvis-lumina --name azure-event-grid-endpoint --value "<endpoint-url>"
az keyvault secret set --vault-name jarvis-lumina --name cognitive-speech-key --value "<api-key>"
az keyvault secret set --vault-name jarvis-lumina --name cognitive-text-analytics-key --value "<api-key>"
az keyvault secret set --vault-name jarvis-lumina --name cognitive-vision-key --value "<api-key>"
az keyvault secret set --vault-name jarvis-lumina --name cosmos-db-endpoint --value "<endpoint-url>"
az keyvault secret set --vault-name jarvis-lumina --name cosmos-db-key --value "<primary-key>"
az keyvault secret set --vault-name jarvis-lumina --name app-insights-instrumentation-key --value "<instrumentation-key>"
```

### Option 3: Python Script (Interactive)

```bash
python scripts/python/configure_azure_services.py --interactive
```

## Verification

After adding secrets, verify they're configured:

```bash
python scripts/python/configure_azure_services.py
```

Or test Azure services:

```bash
python scripts/python/battle_test_azure_services.py
```

## Current Status

Run the configuration script to check current status:

```bash
python scripts/python/configure_azure_services.py
```

This will show:
- ✅ Secrets that exist
- ❌ Secrets that are missing
- Instructions for adding missing secrets

## Next Steps

1. **Add all required secrets** to Key Vault using one of the methods above
2. **Verify configuration** using the configuration script
3. **Test services** using the battle test script
4. **Monitor** Azure services in Azure Portal

## Resources

- [Azure Key Vault Documentation](https://learn.microsoft.com/azure/key-vault/)
- [Azure Service Bus Documentation](https://learn.microsoft.com/azure/service-bus/)
- [Azure Storage Documentation](https://learn.microsoft.com/azure/storage/)
- [Azure Event Grid Documentation](https://learn.microsoft.com/azure/event-grid/)
- [Azure Cognitive Services Documentation](https://learn.microsoft.com/azure/cognitive-services/)
- [Azure Cosmos DB Documentation](https://learn.microsoft.com/azure/cosmos-db/)
