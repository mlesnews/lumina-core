# Azure Key Vault Access Policies

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines access policies for Azure Key Vault. All secrets are accessed using Managed Identity authentication. Access is granted based on service roles and least-privilege principles.

---

## Access Policy Principles

1. **Managed Identity**: All services use Managed Identity (no connection strings in code)
2. **Least Privilege**: Services only have access to secrets they need
3. **Role-Based**: Access granted based on service roles
4. **Audit Logging**: All secret access is logged
5. **Rotation Support**: Access policies support secret rotation

---

## Service Roles

### api-services

**Description**: API services that need to read secrets for normal operation

**Services**:
- JARVIS Master Agent API
- Lumina API services
- R5 API server
- Helpdesk API

**Permissions**:
- `Get`: Read secret values
- `List`: List secrets (for discovery)

**Secrets Accessible**:
- All authentication_secrets
- All integration_secrets
- All database_secrets
- All service_secrets
- azure-storage-account-key (platform_secrets)
- encryption-key (platform_secrets)

---

### admin-services

**Description**: Administrative services that need full secret management

**Services**:
- Secret rotation services
- Administrative tools
- Deployment services

**Permissions**:
- `Get`: Read secret values
- `List`: List secrets
- `Set`: Create/update secrets
- `Delete`: Delete secrets (with restrictions)
- `Recover`: Recover deleted secrets
- `Backup`: Backup secrets
- `Restore`: Restore secrets

**Secrets Accessible**:
- All secrets (full access)

**Restrictions**:
- Delete operations require approval
- Audit logging for all operations

---

### rotation-services

**Description**: Services that perform automatic secret rotation

**Services**:
- Secret rotation automation
- Rotation monitoring

**Permissions**:
- `Get`: Read current secret values
- `Set`: Create new secret versions
- `List`: List secrets

**Secrets Accessible**:
- Secrets with auto_rotation enabled

**Restrictions**:
- Cannot delete secrets
- Cannot access secrets without rotation schedules

---

## Access Policy Definitions

### Policy: api-services-policy

**Assigned To**: Managed Identities for API services

**Permissions**:
```json
{
  "keys": [],
  "secrets": ["Get", "List"],
  "certificates": []
}
```

**Secret Filters**:
- All secrets except admin-only secrets

---

### Policy: admin-services-policy

**Assigned To**: Managed Identities for admin services

**Permissions**:
```json
{
  "keys": ["Get", "List", "Create", "Update", "Delete", "Recover", "Backup", "Restore"],
  "secrets": ["Get", "List", "Set", "Delete", "Recover", "Backup", "Restore"],
  "certificates": ["Get", "List", "Create", "Update", "Delete", "Recover", "Backup", "Restore"]
}
```

**Secret Filters**:
- All secrets (no restrictions)

---

### Policy: rotation-services-policy

**Assigned To**: Managed Identities for rotation services

**Permissions**:
```json
{
  "keys": ["Get", "List", "Create", "Update"],
  "secrets": ["Get", "List", "Set"],
  "certificates": ["Get", "List", "Create", "Update"]
}
```

**Secret Filters**:
- Only secrets with auto_rotation enabled

---

## Managed Identity Assignments

### API Services

**JARVIS Master Agent API**:
- Managed Identity: `jarvis-api-identity`
- Policy: `api-services-policy`
- Access: Read secrets for API operation

**Lumina API Services**:
- Managed Identity: `lumina-api-identity`
- Policy: `api-services-policy`
- Access: Read secrets for Lumina services

**R5 API Server**:
- Managed Identity: `r5-api-identity`
- Policy: `api-services-policy`
- Access: Read R5-specific secrets

**Helpdesk API**:
- Managed Identity: `helpdesk-api-identity`
- Policy: `api-services-policy`
- Access: Read helpdesk-specific secrets

---

### Admin Services

**Secret Rotation Service**:
- Managed Identity: `secret-rotation-identity`
- Policy: `rotation-services-policy`
- Access: Rotate secrets with auto_rotation

**Deployment Service**:
- Managed Identity: `deployment-identity`
- Policy: `admin-services-policy`
- Access: Full secret management for deployment

---

## Secret Access Patterns

### Reading Secrets

**Pattern**: Services read secrets at startup and cache in memory

**Example**:
```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
client = SecretClient(
    vault_url="https://jarvis-lumina.vault.azure.net/",
    credential=credential
)

# Read secret
secret = client.get_secret("jwt-secret-key")
jwt_secret = secret.value
```

**Caching**: Secrets cached in memory, refreshed on rotation notification

---

### Secret Rotation

**Pattern**: New secret version created, services notified, old version deprecated

**Process**:
1. Rotation service creates new secret version
2. Services notified of new version
3. Services update cached secret
4. Old version marked as deprecated
5. Old version deleted after grace period

---

## Network Access

### Firewall Rules

**Allowed IP Ranges**:
- Azure service IP ranges
- Internal network ranges (if applicable)

**Virtual Network**: Key Vault accessible from configured virtual networks

**Private Endpoint**: Private endpoint for internal access (recommended)

---

## Audit Logging

### Logged Operations

- All Get operations (secret reads)
- All Set operations (secret updates)
- All Delete operations
- All List operations
- All rotation operations

### Log Retention

- **Retention Period**: 90 days
- **Storage**: Azure Monitor Logs
- **Alerting**: Alerts on suspicious access patterns

---

## Security Best Practices

1. **Managed Identity**: Always use Managed Identity (never connection strings)
2. **Least Privilege**: Grant minimum necessary permissions
3. **Rotation**: Rotate secrets regularly
4. **Monitoring**: Monitor all secret access
5. **Audit**: Review audit logs regularly
6. **Network Security**: Use private endpoints and firewall rules
7. **Versioning**: Use secret versions for rotation
8. **Backup**: Backup secrets regularly (admin services only)

---

## Secret Naming Conventions

### Format

`{category}-{purpose}-{identifier}`

### Examples

- `auth-jwt-secret-key`
- `integration-openai-api-key`
- `database-postgres-connection-string`
- `service-r5-api-key`
- `platform-azure-storage-account-key`

### Categories

- `auth`: Authentication secrets
- `integration`: Third-party integration secrets
- `database`: Database connection secrets
- `service`: Internal service secrets
- `platform`: Platform and infrastructure secrets

---

## Compliance

### Requirements

- **No Secrets in Code**: All secrets in Key Vault
- **No Secrets in Config**: All secrets retrieved from Key Vault
- **Encryption**: All secrets encrypted at rest
- **Access Control**: Role-based access control
- **Audit Trail**: Complete audit logging
- **Rotation**: Regular secret rotation

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
