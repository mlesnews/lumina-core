# Azure Key Vault Integration Points

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines all integration points where Azure Key Vault is used to retrieve secrets. All secrets must be retrieved from Key Vault - no secrets in code or config files.

---

## Integration Points

### 1. JARVIS Master Agent API

**Secrets Used**:
- jwt-secret-key
- refresh-token-secret
- database-password
- azure-service-bus-connection-string
- openai-api-key
- anthropic-api-key

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/jarvis_master_agent_api.py`

---

### 2. Lumina API Services

**Secrets Used**:
- database-password
- azure-service-bus-connection-string
- r5-api-key
- helpdesk-api-key

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/lumina_api_services.py`

---

### 3. R5 API Server

**Secrets Used**:
- r5-api-key
- database-password
- azure-service-bus-connection-string

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/r5_api_server.py`

---

### 4. Helpdesk API

**Secrets Used**:
- helpdesk-api-key
- database-password
- azure-service-bus-connection-string

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/helpdesk_api.py`

---

### 5. Master Feedback Loop

**Secrets Used**:
- master-feedback-loop-secret
- database-password
- azure-service-bus-connection-string

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/master_feedback_loop_enhancer.py`

---

### 6. Workflow Processor

**Secrets Used**:
- database-password
- azure-service-bus-connection-string
- openai-api-key (for AI workflows)

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/workflow_processor.py`

---

### 7. SYPHON Intelligence Extraction

**Secrets Used**:
- database-password
- azure-service-bus-connection-string
- openai-api-key

**Integration**:
- Read secrets at startup
- Cache secrets in memory
- Refresh on rotation notification
- Use Managed Identity authentication

**Code Location**: `scripts/python/syphon/`

---

### 8. Secret Rotation Service

**Secrets Used**:
- All secrets (for rotation)

**Integration**:
- Read current secret versions
- Create new secret versions
- Update secret metadata
- Use Managed Identity authentication

**Code Location**: `scripts/python/secret_rotation_service.py`

---

## Integration Pattern

### Standard Pattern

All services follow this pattern:

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class ServiceWithKeyVault:
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.secret_client = SecretClient(
            vault_url="https://jarvis-lumina.vault.azure.net/",
            credential=self.credential
        )
        self.secrets = {}
        self.load_secrets()

    def load_secrets(self):
        """Load secrets from Key Vault"""
        secret_names = [
            "jwt-secret-key",
            "database-password",
            # ... other secrets
        ]

        for secret_name in secret_names:
            try:
                secret = self.secret_client.get_secret(secret_name)
                self.secrets[secret_name] = secret.value
            except Exception as e:
                logger.error(f"Failed to load secret {secret_name}: {e}")
                raise

    def get_secret(self, secret_name: str) -> str:
        """Get secret from cache"""
        return self.secrets.get(secret_name)

    def refresh_secret(self, secret_name: str):
        """Refresh secret from Key Vault"""
        secret = self.secret_client.get_secret(secret_name)
        self.secrets[secret_name] = secret.value
```

---

## Secret Caching

### Cache Strategy

**In-Memory Cache**: Secrets cached in memory after first read

**Refresh Triggers**:
- Rotation notification received
- Secret access fails (stale secret)
- Manual refresh request
- Startup (always refresh)

**Cache Invalidation**: Cache invalidated on rotation notification

---

## Error Handling

### Secret Access Failures

**Scenarios**:
- Key Vault unavailable
- Secret not found
- Access denied
- Network error

**Handling**:
- Retry with exponential backoff
- Fallback to cached secret (if available)
- Alert on persistent failures
- Fail gracefully (don't crash service)

---

## Migration from Config Files

### Current State

**Secrets in Config Files**: Must be migrated to Key Vault

**Migration Process**:
1. Identify all secrets in code/config
2. Create secrets in Key Vault
3. Update code to read from Key Vault
4. Remove secrets from code/config
5. Verify functionality
6. Delete old config files

### Files to Migrate

- `config/*.json` (encrypted config files)
- Environment variables
- Hardcoded secrets in code

---

## Testing

### Test Scenarios

1. **Secret Retrieval**: Test reading secrets from Key Vault
2. **Secret Rotation**: Test handling secret rotation
3. **Access Denied**: Test handling access denied
4. **Key Vault Unavailable**: Test handling Key Vault unavailability
5. **Invalid Secret**: Test handling invalid secret values

---

## Monitoring

### Metrics

- **Secret Access Count**: Number of secret reads
- **Secret Access Latency**: Time to read secret
- **Secret Access Failures**: Number of failed secret reads
- **Rotation Notifications**: Number of rotation notifications received

### Alerts

- **Key Vault Unavailable**: Alert if Key Vault is unreachable
- **Access Denied**: Alert on access denied errors
- **Secret Not Found**: Alert if required secret is missing
- **High Access Latency**: Alert if secret access is slow

---

## Security

### Best Practices

1. **Managed Identity**: Always use Managed Identity
2. **No Secrets in Code**: Never hardcode secrets
3. **No Secrets in Config**: Never store secrets in config files
4. **Least Privilege**: Grant minimum necessary permissions
5. **Audit Logging**: Log all secret access
6. **Rotation**: Rotate secrets regularly
7. **Encryption**: Secrets encrypted at rest and in transit

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
