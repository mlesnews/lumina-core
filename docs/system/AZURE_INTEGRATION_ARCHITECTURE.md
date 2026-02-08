# Azure Integration Architecture - Lumina | JARVIS Extension

**Date**: 2025-01-24
**Status**: ✅ **REQUIREMENT DEFINED**
**Version**: 1.0.0

---

## Critical Requirements

### 1. Azure Service Bus - Async Communication
**REQUIREMENT**: All moving pieces must work asynchronously using Azure Service Bus

### 2. Azure Key Vault - Secrets Management
**REQUIREMENT**: All company secrets MUST utilize Azure Key Vault

---

## Azure Service Bus Architecture

### Purpose
All inter-component communication must be asynchronous via Azure Service Bus to ensure:
- Decoupled components
- Scalable architecture
- Reliable message delivery
- Event-driven workflows
- Fault tolerance

### Service Bus Topology

```
┌─────────────────────────────────────────────────────────────┐
│              Azure Service Bus Namespace                     │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Topics (Pub/Sub)                             │  │
│  │                                                       │  │
│  │  • jarvis.workflows                                  │  │
│  │  • jarvis.escalations                                │  │
│  │  • jarvis.intelligence                               │  │
│  │  • lumina.workflows                                  │  │
│  │  • lumina.verification                               │  │
│  │  • r5.knowledge                                      │  │
│  │  • helpdesk.coordination                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Queues (Point-to-Point)                      │  │
│  │                                                       │  │
│  │  • jarvis-escalation-queue                           │  │
│  │  • workflow-execution-queue                          │  │
│  │  • r5-ingestion-queue                                │  │
│  │  • verification-queue                                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Message Patterns

#### 1. Workflow Execution (Async)
```
User Request → Service Bus Topic (jarvis.workflows)
  ↓
JARVIS Helpdesk Integration (Subscriber)
  ↓
Droid Actor System (Subscriber)
  ↓
@v3 Verification (Subscriber)
  ↓
Workflow Execution (Queue: workflow-execution-queue)
  ↓
R5 Ingestion (Queue: r5-ingestion-queue)
```

#### 2. Escalation (Async)
```
C-3PO → Service Bus Topic (jarvis.escalations)
  ↓
JARVIS Intelligence (Subscriber)
  ↓
Escalation Handler (Queue: jarvis-escalation-queue)
  ↓
Response Topic (jarvis.responses)
```

#### 3. Knowledge Aggregation (Async)
```
Workflow Results → Service Bus Topic (r5.knowledge)
  ↓
R5 Living Context Matrix (Subscriber)
  ↓
Pattern Extraction (Async)
  ↓
Matrix Update (Async)
```

### Service Bus Configuration

**Namespace**: `jarvis-lumina-bus` (or configured)

**Topics**:
- `jarvis.workflows` - Workflow orchestration messages
- `jarvis.escalations` - Escalation messages
- `jarvis.intelligence` - Intelligence feed messages
- `jarvis.responses` - Response messages
- `lumina.workflows` - Lumina workflow messages
- `lumina.verification` - Verification messages
- `r5.knowledge` - R5 knowledge messages
- `helpdesk.coordination` - Helpdesk coordination messages

**Queues**:
- `jarvis-escalation-queue` - Escalation processing
- `workflow-execution-queue` - Workflow execution
- `r5-ingestion-queue` - R5 session ingestion
- `verification-queue` - Verification processing
- `droid-assignment-queue` - Droid assignment

**Subscriptions**:
- Each component subscribes to relevant topics
- Filters applied for message routing
- Dead-letter queues for failed messages

---

## Azure Key Vault Integration

### Purpose
All company secrets MUST be stored in Azure Key Vault:
- API keys
- Connection strings
- Authentication tokens
- Encryption keys
- Database credentials
- Service Bus connection strings
- Third-party API keys

### Key Vault Structure

**Vault Name**: `jarvis-lumina-vault` (or configured)

**Secret Categories**:

#### 1. Authentication Secrets
- `jarvis-api-key` - JARVIS API authentication
- `lumina-api-key` - Lumina API authentication
- `r5-api-key` - R5 API authentication
- `service-bus-connection-string` - Service Bus connection

#### 2. Integration Secrets
- `anthropic-api-key` - Anthropic API key
- `openai-api-key` - OpenAI API key
- `github-token` - GitHub integration token
- `n8n-webhook-secret` - n8n webhook secret

#### 3. Database Secrets
- `database-connection-string` - Database connection
- `redis-connection-string` - Redis connection

#### 4. Service Secrets
- `r5-encryption-key` - R5 encryption key
- `workflow-signing-key` - Workflow signing key
- `escalation-encryption-key` - Escalation encryption

#### 5. Platform Secrets
- `windows-widget-api-key` - Windows 11 widget API
- `mobile-app-secret` - Mobile app secret
- `desktop-app-secret` - Desktop app secret

### Key Vault Access Pattern

```python
# All secrets accessed via Azure Key Vault
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Initialize Key Vault client
credential = DefaultAzureCredential()
vault_url = "https://jarvis-lumina-vault.vault.azure.net/"
client = SecretClient(vault_url=vault_url, credential=credential)

# Retrieve secret
api_key = client.get_secret("jarvis-api-key").value
```

### Secret Rotation
- Automatic secret rotation supported
- Version tracking for secrets
- Rollback capability
- Audit logging

---

## Updated Architecture with Azure Integration

```
┌─────────────────────────────────────────────────────────────┐
│              Lumina | JARVIS Extension                      │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Components (All Async via Service Bus)       │  │
│  │                                                       │  │
│  │  • JARVIS Helpdesk Integration                       │  │
│  │  • Droid Actor System                                │  │
│  │  • R5 Living Context Matrix                          │  │
│  │  • @v3 Verification                                  │  │
│  │  • @helpdesk (C-3PO)                                 │  │
│  └──────────────────────────────────────────────────────┘  │
│                        │                                     │
│                        ▼                                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Azure Service Bus                            │  │
│  │  • Topics (Pub/Sub)                                  │  │
│  │  • Queues (Point-to-Point)                           │  │
│  │  • Subscriptions                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                        │                                     │
│                        ▼                                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Azure Key Vault                              │  │
│  │  • All secrets stored here                           │  │
│  │  • No secrets in code/config files                   │  │
│  │  • Automatic rotation                                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation Requirements

### 1. Service Bus Integration

**All Components Must**:
- Publish messages to Service Bus topics
- Subscribe to relevant topics
- Use queues for point-to-point communication
- Handle message failures with dead-letter queues
- Implement retry logic
- Support message ordering where needed

**Message Format**:
```json
{
  "message_id": "uuid",
  "message_type": "workflow|escalation|knowledge|verification",
  "timestamp": "ISO timestamp",
  "source": "component_name",
  "destination": "component_name|topic",
  "payload": { /* message data */ },
  "correlation_id": "uuid",
  "reply_to": "topic|queue",
  "metadata": { /* additional metadata */ }
}
```

### 2. Key Vault Integration

**All Components Must**:
- Retrieve secrets from Azure Key Vault
- Never store secrets in code or config files
- Use managed identity or service principal
- Cache secrets appropriately (with TTL)
- Handle secret rotation gracefully
- Log secret access (audit trail)

**Secret Access Pattern**:
```python
# All secrets MUST come from Azure Key Vault
secret = get_secret_from_vault("secret-name")
# Never: secret = "hardcoded-value"
```

---

## Component Updates Required

### JARVIS Helpdesk Integration
- ✅ Publish workflow messages to Service Bus
- ✅ Subscribe to escalation responses
- ✅ Retrieve secrets from Key Vault
- ⚠️ Update to use Service Bus instead of direct calls

### Droid Actor System
- ✅ Publish droid assignment messages
- ✅ Subscribe to workflow topics
- ✅ Retrieve droid configs from Key Vault
- ⚠️ Update to async Service Bus communication

### R5 Living Context Matrix
- ✅ Publish knowledge messages to Service Bus
- ✅ Subscribe to session ingestion queue
- ✅ Store encryption keys in Key Vault
- ⚠️ Update to async Service Bus communication

### @v3 Verification
- ✅ Publish verification results to Service Bus
- ✅ Subscribe to verification requests
- ✅ Retrieve verification keys from Key Vault
- ⚠️ Update to async Service Bus communication

### JARVIS Escalation
- ✅ Publish escalations to Service Bus topic
- ✅ Subscribe to escalation responses
- ✅ Store escalation secrets in Key Vault
- ⚠️ Update to use Service Bus instead of file-based

---

## Migration Plan

### Phase 1: Key Vault Migration
1. Identify all secrets in code/config
2. Create Azure Key Vault
3. Migrate secrets to Key Vault
4. Update code to retrieve from Key Vault
5. Remove secrets from code/config
6. Verify all secrets in Key Vault

### Phase 2: Service Bus Integration
1. Create Azure Service Bus namespace
2. Create topics and queues
3. Update components to publish to Service Bus
4. Update components to subscribe to Service Bus
5. Remove direct component communication
6. Test async message flow

### Phase 3: Full Async Migration
1. Convert all synchronous calls to async
2. Implement message handlers
3. Add retry logic and error handling
4. Implement dead-letter queue handling
5. Add monitoring and alerting
6. Performance testing

---

## Security & Compliance

### Key Vault Security
- ✅ Managed Identity authentication
- ✅ Role-based access control (RBAC)
- ✅ Network isolation (private endpoints)
- ✅ Audit logging enabled
- ✅ Secret versioning
- ✅ Automatic rotation

### Service Bus Security
- ✅ Shared Access Signatures (SAS) or Managed Identity
- ✅ Network isolation (private endpoints)
- ✅ Message encryption in transit
- ✅ Message encryption at rest
- ✅ Access control (RBAC)
- ✅ Audit logging

---

## Monitoring & Observability

### Service Bus Monitoring
- Message throughput
- Queue depth
- Dead-letter queue size
- Message processing time
- Failed message count
- Topic subscription lag

### Key Vault Monitoring
- Secret access frequency
- Failed access attempts
- Secret rotation events
- Access patterns
- Audit log analysis

---

## Status

✅ **REQUIREMENTS DEFINED**

- Azure Service Bus: Required for all async communication
- Azure Key Vault: Required for all secrets
- Migration plan: Defined
- Security: Specified

**Next Steps**: Begin Phase 1 (Key Vault Migration)

---

**Last Updated**: 2025-01-24
**Maintained By**: Cedarbrook Financial Services LLC

