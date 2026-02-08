# Azure Service Bus Routing Rules

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines routing rules for Azure Service Bus topics and subscriptions. Routing determines which messages are delivered to which subscriptions based on message properties and filters.

---

## Filter Types

### TrueFilter

**Description**: Matches all messages

**Usage**: Audit subscriptions, catch-all subscriptions

**Example**:
```json
{
  "type": "TrueFilter"
}
```

---

### SqlFilter

**Description**: SQL-like filter expressions on message properties

**Usage**: Most subscriptions use SqlFilter for selective message routing

**Syntax**: SQL WHERE clause syntax

**Example**:
```json
{
  "type": "SqlFilter",
  "expression": "MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'"
}
```

---

## Topic Routing Rules

### jarvis.workflows

#### workflow-processor Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'`

**Purpose**: Route workflow creation and execution requests to processor

**Messages Routed**:
- WorkflowCreated
- WorkflowExecutionRequest

---

#### workflow-notifications Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'WorkflowStatusUpdate' OR MessageType = 'WorkflowCompleted'`

**Purpose**: Route workflow status updates to notification system

**Messages Routed**:
- WorkflowStatusUpdate
- WorkflowCompleted

---

#### workflow-audit Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Capture all workflow messages for audit logging

**Messages Routed**: All messages on topic

---

### jarvis.escalations

#### jarvis-escalation-handler Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'EscalationRequest'`

**Purpose**: Route escalation requests to JARVIS escalation handler

**Messages Routed**:
- EscalationRequest

---

#### escalation-notifications Subscription

**Filter**: SqlFilter
**Expression**: `Priority = 'high' OR Priority = 'critical'`

**Purpose**: Route high-priority escalations to notification system

**Messages Routed**:
- EscalationRequest (high/critical priority)
- EscalationAcknowledged (high/critical priority)

---

### jarvis.intelligence

#### intelligence-processor Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Process all intelligence items

**Messages Routed**: All messages on topic

---

#### intelligence-feed Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Distribute intelligence feed to subscribers

**Messages Routed**: All messages on topic

---

#### intelligence-analytics Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Route intelligence items to analytics processing

**Messages Routed**: All messages on topic

---

### jarvis.responses

#### response-handler Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Process JARVIS response messages

**Messages Routed**: All messages on topic

---

#### response-notifications Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Route responses to notification system

**Messages Routed**: All messages on topic

---

### lumina.workflows

#### lumina-workflow-processor Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'`

**Purpose**: Route workflow creation and execution requests to Lumina processor

**Messages Routed**:
- WorkflowCreated
- WorkflowExecutionRequest

---

#### workflow-verification Subscription

**Filter**: SqlFilter
**Expression**: `RequiresVerification = true`

**Purpose**: Route workflows requiring verification to @v3 system

**Messages Routed**:
- WorkflowCreated (if RequiresVerification = true)
- WorkflowExecutionRequest (if RequiresVerification = true)

---

#### workflow-r5-sync Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'WorkflowCompleted'`

**Purpose**: Route completed workflows to R5 knowledge sync

**Messages Routed**:
- WorkflowCompleted

---

### lumina.verification

#### v3-verification-processor Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Process all verification messages

**Messages Routed**: All messages on topic

---

#### verification-audit Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Capture all verification messages for audit logging

**Messages Routed**: All messages on topic

---

### r5.knowledge

#### r5-ingestion-processor Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'KnowledgeEntry' OR MessageType = 'BatchIngestion'`

**Purpose**: Route knowledge entries to ingestion processor

**Messages Routed**:
- KnowledgeEntry
- BatchIngestion

---

#### r5-pattern-extractor Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'KnowledgeEntry' AND ExtractPatterns = true`

**Purpose**: Route knowledge entries requiring pattern extraction

**Messages Routed**:
- KnowledgeEntry (if ExtractPatterns = true)

---

#### r5-search-processor Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'SearchRequest'`

**Purpose**: Route search requests to search processor

**Messages Routed**:
- SearchRequest

---

### helpdesk.coordination

#### helpdesk-coordinator Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Route all helpdesk coordination messages to coordinator

**Messages Routed**: All messages on topic

---

#### droid-assignment Subscription

**Filter**: SqlFilter
**Expression**: `MessageType = 'DroidAssignmentRequest'`

**Purpose**: Route droid assignment requests to assignment processor

**Messages Routed**:
- DroidAssignmentRequest

---

#### helpdesk-notifications Subscription

**Filter**: TrueFilter
**Expression**: (all messages)

**Purpose**: Route helpdesk messages to notification system

**Messages Routed**: All messages on topic

---

## Queue Routing

Queues use point-to-point messaging. Messages are routed to queues based on explicit send operations, not filters.

### Queue Selection Logic

**jarvis-escalation-queue**: Explicitly sent escalation requests

**workflow-execution-queue**: Explicitly sent workflow execution requests

**r5-ingestion-queue**: Explicitly sent knowledge ingestion tasks

**verification-queue**: Explicitly sent verification requests

**droid-assignment-queue**: Explicitly sent droid assignment requests

---

## Message Property Routing

Messages can be routed based on custom properties:

### Priority-Based Routing

**High/Critical Priority**: Routed to priority processing subscriptions

**Example**:
```json
{
  "Priority": "critical",
  "MessageType": "EscalationRequest"
}
```

Routes to:
- jarvis-escalation-handler (all escalations)
- escalation-notifications (high/critical priority filter)

---

### Type-Based Routing

**MessageType Property**: Primary routing property

**Example**:
```json
{
  "MessageType": "WorkflowCreated",
  "RequiresVerification": true
}
```

Routes to:
- workflow-processor (MessageType filter)
- workflow-verification (RequiresVerification filter)

---

## Complex Routing Scenarios

### Multi-Subscription Routing

Messages can match multiple subscriptions:

**Example**: WorkflowCompleted message
- Routes to: workflow-notifications (status update)
- Routes to: workflow-r5-sync (completed workflow)
- Routes to: workflow-audit (all messages)

---

### Conditional Routing

**Example**: KnowledgeEntry with ExtractPatterns = true
- Routes to: r5-ingestion-processor (all entries)
- Routes to: r5-pattern-extractor (ExtractPatterns = true)

---

## Routing Best Practices

1. **Use Specific Filters**: Prefer specific SqlFilter expressions over TrueFilter
2. **Minimize Overlap**: Avoid unnecessary message duplication
3. **Performance**: Simple filters perform better than complex ones
4. **Maintainability**: Use clear, documented filter expressions
5. **Testing**: Test routing rules with sample messages

---

## Filter Expression Examples

### Simple Equality
```
MessageType = 'WorkflowCreated'
```

### Multiple Conditions (OR)
```
MessageType = 'WorkflowCreated' OR MessageType = 'WorkflowExecutionRequest'
```

### Multiple Conditions (AND)
```
MessageType = 'KnowledgeEntry' AND ExtractPatterns = true
```

### Priority Filtering
```
Priority = 'high' OR Priority = 'critical'
```

### Property Existence
```
RequiresVerification = true
```

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
