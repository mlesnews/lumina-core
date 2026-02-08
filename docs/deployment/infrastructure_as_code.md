# Infrastructure as Code

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

Infrastructure as Code (IaC) definitions for deploying the JARVIS Master Agent system to Azure.

---

## Tools

- **Terraform**: Primary IaC tool
- **Azure Resource Manager (ARM)**: Alternative/backup
- **Azure CLI**: Deployment automation

---

## Infrastructure Components

### Resource Group

```hcl
resource "azurerm_resource_group" "jarvis_lumina" {
  name     = "jarvis-lumina-rg"
  location = "East US 2"
}
```

### Azure Service Bus

```hcl
resource "azurerm_servicebus_namespace" "jarvis_lumina" {
  name                = "jarvis-lumina-bus"
  location            = azurerm_resource_group.jarvis_lumina.location
  resource_group_name = azurerm_resource_group.jarvis_lumina.name
  sku                 = "Standard"
}
```

### Azure Key Vault

```hcl
resource "azurerm_key_vault" "jarvis_lumina" {
  name                = "jarvis-lumina"
  location            = azurerm_resource_group.jarvis_lumina.location
  resource_group_name = azurerm_resource_group.jarvis_lumina.name
  tenant_id           = var.tenant_id
  sku_name            = "standard"
}
```

### App Service Plan

```hcl
resource "azurerm_app_service_plan" "jarvis_api" {
  name                = "jarvis-api-plan"
  location            = azurerm_resource_group.jarvis_lumina.location
  resource_group_name = azurerm_resource_group.jarvis_lumina.name
  kind                = "Linux"
  reserved            = true
  sku {
    tier = "Standard"
    size = "S1"
  }
}
```

### App Service

```hcl
resource "azurerm_app_service" "jarvis_api" {
  name                = "jarvis-api"
  location            = azurerm_resource_group.jarvis_lumina.location
  resource_group_name = azurerm_resource_group.jarvis_lumina.name
  app_service_plan_id = azurerm_app_service_plan.jarvis_api.id

  site_config {
    linux_fx_version = "PYTHON|3.11"
  }

  identity {
    type = "SystemAssigned"
  }
}
```

### PostgreSQL Database

```hcl
resource "azurerm_postgresql_server" "jarvis_db" {
  name                = "jarvis-lumina-db"
  location            = azurerm_resource_group.jarvis_lumina.location
  resource_group_name = azurerm_resource_group.jarvis_lumina.name
  version             = "13"
  sku_name            = "GP_Gen5_2"

  administrator_login          = var.db_admin_login
  administrator_login_password = var.db_admin_password

  ssl_enforcement_enabled = true
}
```

---

## Deployment Process

### 1. Initialize Terraform

```bash
terraform init
```

### 2. Plan Deployment

```bash
terraform plan -out=tfplan
```

### 3. Apply Deployment

```bash
terraform apply tfplan
```

### 4. Verify Deployment

```bash
terraform output
```

---

## State Management

- **Backend**: Azure Storage for Terraform state
- **Locking**: State locking enabled
- **Versioning**: State file versioned

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
