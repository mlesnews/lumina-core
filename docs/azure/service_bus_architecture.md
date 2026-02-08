# Azure Service Bus Architecture

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**
**Maintained By**: Cedarbrook Financial Services LLC

---

## Overview

Azure Service Bus is the central messaging infrastructure for all asynchronous communication in the JARVIS Master Agent system. All moving pieces must work asynchronously using Azure Service Bus.

### Architecture Principles

- **Async-First**: All inter-system communication via Service Bus
- **Topic-Based**: Pub/sub pattern for broadcast messages
- **Queue-Based**: Point-to-point pattern for work distribution
- **Reliability**: Guaranteed delivery, retry policies, dead-letter handling
- **Scalability**: Auto-scaling, load distribution
- **Security**: Managed Identity authentication, encryption in transit

---

## Service Bus Namespace

**Namespace**: `jarvis-lumina-bus`
**Resource Group**: `jarvis-lumina-rg`
**SKU**: Standard (supports topics and queues)
**Location**: East US 2 (or configured region)

---

## Topics

Topics support pub/sub messaging where multiple subscribers can receive messages.

### 1. jarvis.workflows

**Purpose**: Workflow-related messages for JARVIS system

**Message Types**:
- Workflow created
- Workflow status updates
- Workflow execution requests
- Workflow completion notifications

**Subscriptions**:
- `workflow-processor` - Main workflow processing
- `workflow-notifications` - Notification system
- `workflow-audit` - Audit logging

**Message Schema**: See `message_schemas.json`

---

### 2. jarvis.escalations

**Purpose**: Escalation messages to JARVIS

**Message Types**:
- Escalation requests
- Escalation acknowledgments
- Escalation resolutions

**Subscriptions**:
- `jarvis-escalation-handler` - Main escalation processing
- `escalation-notifications` - Notification system

**Message Schema**: See `message_schemas.json`

---

### 3. jarvis.intelligence

**Purpose**: JARVIS intelligence feed messages

**Message Types**:
- Intelligence items
- Alerts
- Insights
- Recommendations

**Subscriptions**:
- `intelligence-processor` - Intelligence processing
- `intelligence-feed` - Feed distribution
- `intelligence-analytics` - Analytics processing

**Message Schema**: See `message_schemas.json`

---

### 4. jarvis.responses

**Purpose**: JARVIS response messages

**Message Types**:
- Response messages
- Response acknowledgments
- Response status updates

**Subscriptions**:
- `response-handler` - Response processing
- `response-notifications` - Notification system

**Message Schema**: See `message_schemas.json`

---

### 5. lumina.workflows

**Purpose**: Workflow-related messages for Lumina system

**Message Types**:
- Workflow creation
- Workflow execution
- Workflow status updates
- Workflow completion

**Subscriptions**:
- `lumina-workflow-processor` - Lumina workflow processing
- `workflow-verification` - Verification system
- `workflow-r5-sync` - R5 knowledge sync

**Message Schema**: See `message_schemas.json`

---

### 6. lumina.verification

**Purpose**: Verification messages for @v3 system

**Message Types**:
- Verification requests
- Verification results
- Verification status updates

**Subscriptions**:
- `v3-verification-processor` - Verification processing
- `verification-audit` - Audit logging

**Message Schema**: See `message_schemas.json`

---

### 7. r5.knowledge

**Purpose**: R5 knowledge ingestion and updates

**Message Types**:
- Knowledge entries
- Pattern updates
- Matrix updates
- Search requests

**Subscriptions**:
- `r5-ingestion-processor` - Knowledge ingestion
- `r5-pattern-extractor` - Pattern extraction
- `r5-search-processor` - Search processing

**Message Schema**: See `message_schemas.json`

---

### 8. helpdesk.coordination

**Purpose**: Helpdesk coordination and droid assignment

**Message Types**:
- Ticket assignments
- Droid status updates
- Coordination messages
- C-3PO messages

**Subscriptions**:
- `helpdesk-coordinator` - Main coordination
- `droid-assignment` - Droid assignment
- `helpdesk-notifications` - Notifications

**Message Schema**: See `message_schemas.json`

---

## Queues

Queues support point-to-point messaging for work distribution.

### 1. jarvis-escalation-queue

**Purpose**: Queue for JARVIS escalation processing

**Message Types**:
- Escalation requests
- Escalation processing tasks

**Processing**:
- Single consumer (JARVIS escalation handler)
- FIFO ordering
- Dead-letter after 10 failed attempts

**Message Schema**: See `message_schemas.json`

---

### 2. workflow-execution-queue

**Purpose**: Queue for workflow execution tasks

**Message Types**:
- Workflow execution requests
- Workflow step execution tasks

**Processing**:
- Multiple consumers (workflow processors)
- Load balancing across consumers
- Dead-letter after 5 failed attempts

**Message Schema**: See `message_schemas.json`

---

### 3. r5-ingestion-queue

**Purpose**: Queue for R5 knowledge ingestion

**Message Types**:
- Knowledge entry ingestion tasks
- Batch ingestion tasks

**Processing**:
- Multiple consumers (R5 ingestion processors)
- Batch processing support
- Dead-letter after 10 failed attempts

**Message Schema**: See `message_schemas.json`

---

### 4. verification-queue

**Purpose**: Queue for @v3 verification tasks

**Message Types**:
- Verification requests
- Verification processing tasks

**Processing**:
- Multiple consumers (verification processors)
- Priority processing for critical verifications
- Dead-letter after 5 failed attempts

**Message Schema**: See `message_schemas.json`

---

### 5. droid-assignment-queue

**Purpose**: Queue for droid assignment tasks

**Message Types**:
- Droid assignment requests
- Droid coordination tasks

**Processing**:
- Single consumer (C-3PO coordinator)
- FIFO ordering
- Dead-letter after 5 failed attempts

**Message Schema**: See `message_schemas.json`

---

## Routing Rules

### Topic Subscription Filters

#### jarvis.workflows Subscriptions

**workflow-processor**:
- Filter: `MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'`
- Action: None

**workflow-notifications**:
- Filter: `MessageType = 'WorkflowStatusUpdate' OR MessageType = 'WorkflowCompleted'`
- Action: None

**workflow-audit**:
- Filter: `MessageType = '*'` (All messages)
- Action: None

#### jarvis.escalations Subscriptions

**jarvis-escalation-handler**:
- Filter: `MessageType = 'EscalationRequest'`
- Action: None

**escalation-notifications**:
- Filter: `Priority = 'high' OR Priority = 'critical'`
- Action: None

#### lumina.workflows Subscriptions

**lumina-workflow-processor**:
- Filter: `MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'`
- Action: None

**workflow-verification**:
- Filter: `RequiresVerification = true`
- Action: None

**workflow-r5-sync**:
- Filter: `MessageType = 'WorkflowCompleted'`
- Action: None

#### r5.knowledge Subscriptions

**r5-ingestion-processor**:
- Filter: `MessageType = 'KnowledgeEntry' OR MessageType = 'BatchIngestion'`
- Action: None

**r5-pattern-extractor**:
- Filter: `MessageType = 'KnowledgeEntry' AND ExtractPatterns = true`
- Action: None

**r5-search-processor**:
- Filter: `MessageType = 'SearchRequest'`
- Action: None

---

## Message Schemas

See `message_schemas.json` for complete message schema definitions.

### Common Message Properties

All messages include:
- `MessageId`: Unique message identifier (UUID)
- `MessageType`: Type of message (string)
- `Timestamp`: Message timestamp (ISO 8601)
- `Source`: Source system identifier (string)
- `CorrelationId`: Correlation identifier for request/response (UUID, optional)
- `Priority`: Message priority (low, medium, high, critical)

---

## Retry Policies

### Default Retry Policy

**Max Delivery Count**: 10
**Time To Live**: 7 days
**Lock Duration**: 60 seconds

### Retry Strategy

**Exponential Backoff**:
- Initial delay: 1 second
- Maximum delay: 60 seconds
- Backoff multiplier: 2.0

**Retry Attempts**:
- Attempt 1: Immediate
- Attempt 2: 1 second delay
- Attempt 3: 2 seconds delay
- Attempt 4: 4 seconds delay
- Attempt 5: 8 seconds delay
- Attempt 6: 16 seconds delay
- Attempt 7: 32 seconds delay
- Attempt 8+: 60 seconds delay (capped)

### Per-Queue Retry Policies

**jarvis-escalation-queue**:
- Max Delivery Count: 10
- Lock Duration: 120 seconds (longer for complex escalations)

**workflow-execution-queue**:
- Max Delivery Count: 5
- Lock Duration: 300 seconds (workflows can take time)

**r5-ingestion-queue**:
- Max Delivery Count: 10
- Lock Duration: 60 seconds

**verification-queue**:
- Max Delivery Count: 5
- Lock Duration: 120 seconds

**droid-assignment-queue**:
- Max Delivery Count: 5
- Lock Duration: 60 seconds

---

## Dead-Letter Handling

### Dead-Letter Queue Configuration

All queues and subscriptions have dead-letter queues enabled.

**Dead-Letter Conditions**:
- Max delivery count exceeded
- Message expired (TTL exceeded)
- Message cannot be processed

### Dead-Letter Processing

**Monitoring**:
- Dead-letter messages monitored and alerted
- Dead-letter count tracked per queue/subscription

**Recovery**:
- Dead-letter messages can be resubmitted
- Manual review and processing
- Automatic retry after fix (if applicable)

**Retention**:
- Dead-letter messages retained for 30 days
- After 30 days, messages are purged

---

## Security

### Authentication

**Managed Identity**: All services use Managed Identity for authentication

**Connection String**: Stored in Azure Key Vault (not in code/config)

**SAS Tokens**: Not used (Managed Identity preferred)

### Authorization

**Access Policies**:
- Send: Services that publish messages
- Listen: Services that consume messages
- Manage: Administrative operations only

**Role-Based Access Control (RBAC)**:
- Azure Service Bus Data Owner
- Azure Service Bus Data Sender
- Azure Service Bus Data Receiver

### Encryption

**In Transit**: TLS 1.2+ (enforced)

**At Rest**: Service Bus managed encryption

---

## Monitoring & Metrics

### Key Metrics

- **Message Count**: Messages in queue/topic
- **Active Message Count**: Messages being processed
- **Dead-Letter Count**: Messages in dead-letter queue
- **Incoming Messages**: Messages per second
- **Outgoing Messages**: Messages per second
- **Server Errors**: 5xx errors
- **User Errors**: 4xx errors

### Alerts

- **High Dead-Letter Count**: Alert when dead-letter count > 100
- **Queue Depth**: Alert when queue depth > 10,000
- **Processing Errors**: Alert on processing failures
- **Service Unavailable**: Alert on Service Bus unavailability

---

## Performance & Scaling

### Throughput

**Standard Tier**:
- 1,000 messages/second per queue/topic
- 2,000 operations/second per namespace

**Premium Tier** (if upgraded):
- Higher throughput
- Lower latency
- Dedicated resources

### Scaling

**Auto-Scaling**: Not available (Standard tier)

**Manual Scaling**: Upgrade to Premium tier for higher throughput

**Partitioning**: Topics can be partitioned for higher throughput

---

## Disaster Recovery

### Geo-Disaster Recovery

**Primary Region**: East US 2
**Secondary Region**: West US 2 (paired region)

**Failover**: Manual failover process

**RTO**: 4 hours (Recovery Time Objective)
**RPO**: 1 hour (Recovery Point Objective)

### Backup

**Configuration Backup**: Infrastructure as Code (IaC) templates

**Message Backup**: Not applicable (messages are transient)

---

## Migration Status

**Current Status**: Pending

**Migration Plan**:
1. Create Service Bus namespace and resources
2. Implement Service Bus integration module
3. Migrate JARVIS communication
4. Migrate Lumina communication
5. Deprecate file-based communication
6. Validate and monitor

**Target Completion**: Phase 2 (see Master Plan)

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
