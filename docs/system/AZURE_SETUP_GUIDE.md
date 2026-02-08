# Azure Infrastructure Setup Guide

**Date**: 2025-01-24
**Status**: 📋 **SETUP GUIDE**

---

## Prerequisites

1. **Azure Subscription** - Active Azure subscription
2. **Azure CLI** - Installed and configured
3. **Azure Login** - Logged in to Azure
4. **Permissions** - Contributor or Owner role on subscription

---

## Step 1: Login to Azure

```powershell
az login
```

Verify login:
```powershell
az account show
```

---

## Step 2: Run Infrastructure Setup

```powershell
cd scripts/azure
.\setup_azure_infrastructure.ps1 -ResourceGroupName "jarvis-lumina-rg" -Location "eastus"
```

This will create:
- Resource Group: `jarvis-lumina-rg`
- Key Vault: `jarvis-lumina-vault`
- Service Bus Namespace: `jarvis-lumina-bus`
- All required topics and queues

---

## Step 3: Get Service Bus Connection String

```powershell
az servicebus namespace authorization-rule keys list `
    --name RootManageSharedAccessKey `
    --namespace-name jarvis-lumina-bus `
    --resource-group jarvis-lumina-rg `
    --query primaryConnectionString -o tsv
```

---

## Step 4: Store Connection String in Key Vault

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina-vault `
    --name service-bus-connection-string `
    --value "<connection-string-from-step-3>"
```

---

## Step 5: Migrate Secrets to Key Vault

```powershell
cd scripts/python
python migrate_secrets_to_keyvault.py
```

This will:
1. Scan config files for secrets
2. Scan environment variables for secrets
3. Migrate all found secrets to Key Vault

---

## Step 6: Verify Setup

### Verify Key Vault
```powershell
az keyvault secret list --vault-name jarvis-lumina-vault
```

### Verify Service Bus
```powershell
az servicebus topic list --namespace-name jarvis-lumina-bus --resource-group jarvis-lumina-rg
az servicebus queue list --namespace-name jarvis-lumina-bus --resource-group jarvis-lumina-rg
```

---

## Next Steps

After infrastructure is set up:

1. **Update Components** - Integrate Azure services
2. **Test Integration** - Verify secret retrieval and message flow
3. **Remove Local Secrets** - Clean up config files
4. **Monitor** - Set up monitoring and alerting

---

## Troubleshooting

### "Not logged in to Azure"
```powershell
az login
```

### "Insufficient permissions"
- Ensure you have Contributor or Owner role
- Check subscription access

### "Key Vault name already exists"
- Key Vault names must be globally unique
- Use a different name or delete existing vault

### "Service Bus namespace already exists"
- Namespace names must be globally unique
- Use a different name or delete existing namespace

---

## Manual Setup (Alternative)

If PowerShell script doesn't work, use Azure Portal:

1. **Create Resource Group**
   - Portal → Resource Groups → Create
   - Name: `jarvis-lumina-rg`
   - Region: `East US`

2. **Create Key Vault**
   - Portal → Key Vaults → Create
   - Name: `jarvis-lumina-vault` (must be unique)
   - Resource Group: `jarvis-lumina-rg`
   - Region: `East US`

3. **Create Service Bus Namespace**
   - Portal → Service Bus → Create
   - Name: `jarvis-lumina-bus` (must be unique)
   - Resource Group: `jarvis-lumina-rg`
   - Region: `East US`
   - Pricing Tier: `Standard`

4. **Create Topics and Queues**
   - Use Azure Portal or Azure CLI
   - See `setup_azure_infrastructure.ps1` for list

---

**Last Updated**: 2025-01-24

