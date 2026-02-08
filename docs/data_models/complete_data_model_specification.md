# Complete Data Model Specification

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**
**Maintained By**: Cedarbrook Financial Services LLC

---

## Overview

This document defines the complete data models for all JARVIS Master Agent API systems. All data models follow consistent patterns and include validation rules, relationships, and database schemas.

---

## Table of Contents

1. [User & Authentication Models](#user--authentication-models)
2. [Workflow Models](#workflow-models)
3. [Chat Models](#chat-models)
4. [R5 Knowledge Models](#r5-knowledge-models)
5. [Helpdesk Models](#helpdesk-models)
6. [Intelligence Models](#intelligence-models)
7. [System Models](#system-models)
8. [Common Types](#common-types)
9. [Database Schemas](#database-schemas)
10. [Validation Rules](#validation-rules)

---

## User & Authentication Models

### User

**Description**: User account information

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "username": "string (unique, required)",
  "email": "string (unique, required, email format)",
  "password_hash": "string (required, never exposed in API)",
  "permissions": ["string"] (array of permission strings),
  "preferences": {
    "theme": "string (enum: light, dark, auto)",
    "notifications": "boolean",
    "language": "string (ISO 639-1, default: en)"
  },
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "last_login": "datetime",
  "is_active": "boolean (default: true)",
  "devices": ["Device"] (relationship)
}
```

**Validation Rules**:
- `username`: 3-50 characters, alphanumeric + underscore/hyphen
- `email`: Valid email format, max 255 characters
- `password_hash`: BCrypt hash, never returned in API responses
- `permissions`: Array of strings matching pattern `resource:action`

**Database Table**: `users`

---

### Device

**Description**: User device for multi-device support

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "user_id": "uuid (foreign key -> users.id, required)",
  "device_id": "string (unique, required)",
  "device_name": "string (required)",
  "device_type": "string (enum: desktop, mobile, widget, ide)",
  "platform": "string (enum: windows, macos, linux, ios, android)",
  "last_seen": "datetime",
  "created_at": "datetime (required)",
  "is_active": "boolean (default: true)"
}
```

**Validation Rules**:
- `device_id`: UUID format, unique per user
- `device_name`: 1-100 characters
- `device_type`: Must be one of enum values
- `platform`: Must be one of enum values

**Database Table**: `devices`

**Relationships**:
- Belongs to: `User` (many-to-one)

---

### AccessToken

**Description**: JWT access token metadata

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "user_id": "uuid (foreign key -> users.id, required)",
  "device_id": "uuid (foreign key -> devices.id, optional)",
  "token_jti": "string (JWT ID, unique, required)",
  "expires_at": "datetime (required)",
  "created_at": "datetime (required)",
  "revoked_at": "datetime",
  "is_revoked": "boolean (default: false)"
}
```

**Validation Rules**:
- `token_jti`: UUID format, unique
- `expires_at`: Must be in future when created
- `is_revoked`: Cannot be true if `revoked_at` is null

**Database Table**: `access_tokens`

**Relationships**:
- Belongs to: `User` (many-to-one)
- Belongs to: `Device` (many-to-one, optional)

---

### RefreshToken

**Description**: Refresh token for token renewal

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "user_id": "uuid (foreign key -> users.id, required)",
  "device_id": "uuid (foreign key -> devices.id, optional)",
  "token_hash": "string (bcrypt hash, required)",
  "expires_at": "datetime (required)",
  "created_at": "datetime (required)",
  "revoked_at": "datetime",
  "is_revoked": "boolean (default: false)",
  "rotated_from": "uuid (foreign key -> refresh_tokens.id, optional)"
}
```

**Validation Rules**:
- `token_hash`: BCrypt hash, never exposed in API
- `expires_at`: Must be in future when created (typically 30 days)
- `is_revoked`: Cannot be true if `revoked_at` is null

**Database Table**: `refresh_tokens`

**Relationships**:
- Belongs to: `User` (many-to-one)
- Belongs to: `Device` (many-to-one, optional)
- Self-referential: `rotated_from` (for token rotation tracking)

---

## Workflow Models

### Workflow

**Description**: Workflow definition and execution

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "name": "string (required, 3-100 characters)",
  "description": "string (optional, max 1000 characters)",
  "status": "string (enum: pending, running, completed, failed, cancelled, required)",
  "priority": "integer (1-10, default: 5)",
  "created_by": "uuid (foreign key -> users.id, required)",
  "droid_assigned": "string (optional, droid identifier)",
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "started_at": "datetime",
  "completed_at": "datetime",
  "execution_time": "float (seconds, optional)",
  "steps": ["WorkflowStep"] (relationship),
  "logs": ["WorkflowLog"] (relationship),
  "parameters": "object (optional, JSON)",
  "result": "object (optional, JSON)",
  "error": "string (optional, error message if failed)"
}
```

**Validation Rules**:
- `name`: 3-100 characters, required
- `description`: Max 1000 characters, optional
- `status`: Must be one of enum values
- `priority`: 1-10, default 5
- `execution_time`: Must be positive if set

**Database Table**: `workflows`

**Relationships**:
- Belongs to: `User` (many-to-one, via `created_by`)
- Has many: `WorkflowStep` (one-to-many)
- Has many: `WorkflowLog` (one-to-many)

**Status Transitions**:
- `pending` → `running` (on execution start)
- `running` → `completed` (on success)
- `running` → `failed` (on error)
- `pending` → `cancelled` (on cancellation)
- `running` → `cancelled` (on cancellation)

---

### WorkflowStep

**Description**: Individual step in a workflow

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "workflow_id": "uuid (foreign key -> workflows.id, required)",
  "step_id": "string (required, unique within workflow)",
  "name": "string (required, 1-100 characters)",
  "action": "string (required, action identifier)",
  "status": "string (enum: pending, running, completed, failed, skipped, required)",
  "order": "integer (required, sequence order)",
  "parameters": "object (required, JSON, action-specific)",
  "started_at": "datetime",
  "completed_at": "datetime",
  "execution_time": "float (seconds, optional)",
  "error": "string (optional, error message if failed)",
  "result": "object (optional, JSON, step result)"
}
```

**Validation Rules**:
- `step_id`: Unique within workflow, 1-50 characters
- `name`: 1-100 characters, required
- `action`: Valid action identifier, required
- `order`: Positive integer, unique within workflow
- `parameters`: Valid JSON, required

**Database Table**: `workflow_steps`

**Relationships**:
- Belongs to: `Workflow` (many-to-one)

---

### WorkflowLog

**Description**: Log entry for workflow execution

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "workflow_id": "uuid (foreign key -> workflows.id, required)",
  "step_id": "uuid (foreign key -> workflow_steps.id, optional)",
  "level": "string (enum: info, warning, error, debug, required)",
  "message": "string (required, max 5000 characters)",
  "timestamp": "datetime (required)",
  "metadata": "object (optional, JSON, additional context)"
}
```

**Validation Rules**:
- `level`: Must be one of enum values
- `message`: Max 5000 characters, required
- `timestamp`: Required, typically current time

**Database Table**: `workflow_logs`

**Relationships**:
- Belongs to: `Workflow` (many-to-one)
- Belongs to: `WorkflowStep` (many-to-one, optional)

---

## Chat Models

### Conversation

**Description**: Chat conversation thread

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "user_id": "uuid (foreign key -> users.id, required)",
  "title": "string (optional, max 200 characters, auto-generated)",
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "last_message_at": "datetime",
  "message_count": "integer (default: 0)",
  "is_archived": "boolean (default: false)",
  "messages": ["ChatMessage"] (relationship)
}
```

**Validation Rules**:
- `title`: Max 200 characters, optional
- `message_count`: Non-negative integer, default 0

**Database Table**: `conversations`

**Relationships**:
- Belongs to: `User` (many-to-one)
- Has many: `ChatMessage` (one-to-many)

---

### ChatMessage

**Description**: Individual message in a conversation

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "conversation_id": "uuid (foreign key -> conversations.id, required)",
  "role": "string (enum: user, assistant, system, required)",
  "content": "string (required, max 100000 characters)",
  "timestamp": "datetime (required)",
  "metadata": {
    "file_references": ["string"] (array of file IDs),
    "code_context": "string (optional)",
    "suggestions": ["string"] (array of suggestion strings),
    "code_blocks": [{
      "language": "string",
      "code": "string"
    }]
  },
  "parent_message_id": "uuid (foreign key -> chat_messages.id, optional)",
  "is_edited": "boolean (default: false)",
  "edited_at": "datetime"
}
```

**Validation Rules**:
- `role`: Must be one of enum values
- `content`: Max 100000 characters, required
- `file_references`: Array of valid UUIDs
- `code_blocks`: Valid array of code block objects

**Database Table**: `chat_messages`

**Relationships**:
- Belongs to: `Conversation` (many-to-one)
- Self-referential: `parent_message_id` (for message threading)

---

## R5 Knowledge Models

### R5Session

**Description**: R5 Living Context Matrix session

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "session_id": "string (unique, required)",
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "entries": ["R5Entry"] (relationship),
  "patterns": ["R5Pattern"] (relationship)
}
```

**Validation Rules**:
- `session_id`: Unique identifier, required

**Database Table**: `r5_sessions`

**Relationships**:
- Has many: `R5Entry` (one-to-many)
- Has many: `R5Pattern` (one-to-many)

---

### R5Entry

**Description**: Knowledge entry in R5 matrix

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "session_id": "uuid (foreign key -> r5_sessions.id, optional)",
  "entry_id": "string (unique, required)",
  "category": "string (required, max 100 characters)",
  "content": "string (required, max 100000 characters)",
  "tags": ["string"] (array of tag strings),
  "patterns": ["string"] (array of pattern IDs),
  "timestamp": "datetime (required)",
  "metadata": "object (optional, JSON, additional context)",
  "source": "string (optional, source identifier)",
  "relevance_score": "float (0.0-1.0, optional)"
}
```

**Validation Rules**:
- `entry_id`: Unique identifier, required
- `category`: Max 100 characters, required
- `content`: Max 100000 characters, required
- `tags`: Array of strings, max 50 tags
- `relevance_score`: 0.0-1.0 if set

**Database Table**: `r5_entries`

**Relationships**:
- Belongs to: `R5Session` (many-to-one, optional)
- Many-to-many: `R5Pattern` (via join table)

---

### R5Pattern

**Description**: Extracted pattern from R5 knowledge

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "pattern_id": "string (unique, required)",
  "name": "string (required, max 200 characters)",
  "description": "string (optional, max 1000 characters)",
  "frequency": "integer (default: 0, non-negative)",
  "first_seen": "datetime (required)",
  "last_seen": "datetime (required)",
  "categories": ["string"] (array of category strings),
  "related_patterns": ["string"] (array of pattern IDs),
  "occurrences": ["R5PatternOccurrence"] (relationship),
  "metadata": "object (optional, JSON)"
}
```

**Validation Rules**:
- `pattern_id`: Unique identifier, required
- `name`: Max 200 characters, required
- `description`: Max 1000 characters, optional
- `frequency`: Non-negative integer, default 0
- `last_seen`: Must be >= `first_seen`

**Database Table**: `r5_patterns`

**Relationships**:
- Has many: `R5PatternOccurrence` (one-to-many)
- Many-to-many: `R5Entry` (via join table)
- Self-referential: `related_patterns` (pattern relationships)

---

### R5PatternOccurrence

**Description**: Occurrence of a pattern in an entry

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "pattern_id": "uuid (foreign key -> r5_patterns.id, required)",
  "entry_id": "uuid (foreign key -> r5_entries.id, required)",
  "context": "string (optional, surrounding context)",
  "timestamp": "datetime (required)",
  "confidence": "float (0.0-1.0, optional)"
}
```

**Validation Rules**:
- `confidence`: 0.0-1.0 if set
- `timestamp`: Required

**Database Table**: `r5_pattern_occurrences`

**Relationships**:
- Belongs to: `R5Pattern` (many-to-one)
- Belongs to: `R5Entry` (many-to-one)

---

## Helpdesk Models

### HelpdeskTicket

**Description**: Helpdesk ticket/issue

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "ticket_id": "string (unique, required, format: T + 9 digits)",
  "title": "string (required, max 200 characters)",
  "description": "string (required, max 5000 characters)",
  "status": "string (enum: open, in_progress, resolved, closed, required)",
  "priority": "string (enum: low, medium, high, critical, default: medium)",
  "created_by": "uuid (foreign key -> users.id, required)",
  "assigned_to": "uuid (foreign key -> users.id, optional)",
  "droid_assigned": "string (optional, droid identifier)",
  "workflow_id": "uuid (foreign key -> workflows.id, optional)",
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "resolved_at": "datetime",
  "closed_at": "datetime",
  "tags": ["string"] (array of tag strings),
  "comments": ["HelpdeskComment"] (relationship)
}
```

**Validation Rules**:
- `ticket_id`: Format `T` + 9 digits, unique, required
- `title`: Max 200 characters, required
- `description`: Max 5000 characters, required
- `status`: Must be one of enum values
- `priority`: Must be one of enum values

**Database Table**: `helpdesk_tickets`

**Relationships**:
- Belongs to: `User` (many-to-one, via `created_by`)
- Belongs to: `User` (many-to-one, via `assigned_to`, optional)
- Belongs to: `Workflow` (many-to-one, optional)
- Has many: `HelpdeskComment` (one-to-many)

---

### HelpdeskComment

**Description**: Comment on a helpdesk ticket

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "ticket_id": "uuid (foreign key -> helpdesk_tickets.id, required)",
  "user_id": "uuid (foreign key -> users.id, required)",
  "content": "string (required, max 5000 characters)",
  "created_at": "datetime (required)",
  "updated_at": "datetime (required)",
  "is_internal": "boolean (default: false)",
  "attachments": ["string"] (array of attachment IDs)
}
```

**Validation Rules**:
- `content`: Max 5000 characters, required

**Database Table**: `helpdesk_comments`

**Relationships**:
- Belongs to: `HelpdeskTicket` (many-to-one)
- Belongs to: `User` (many-to-one)

---

### Droid

**Description**: Droid actor in helpdesk system

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "droid_id": "string (unique, required)",
  "name": "string (required, max 100 characters)",
  "type": "string (enum: C-3PO, R2-D2, K-2SO, 2-1B, IG-88, Mouse Droid, R5-D4, Marvin, required)",
  "status": "string (enum: available, busy, offline, required)",
  "current_workflows": "integer (default: 0, non-negative)",
  "queue_length": "integer (default: 0, non-negative)",
  "total_workflows_processed": "integer (default: 0, non-negative)",
  "success_rate": "float (0.0-1.0, default: 1.0)",
  "average_processing_time": "float (seconds, default: 0)",
  "last_active": "datetime",
  "capabilities": ["string"] (array of capability strings),
  "metadata": "object (optional, JSON)"
}
```

**Validation Rules**:
- `droid_id`: Unique identifier, required
- `name`: Max 100 characters, required
- `type`: Must be one of enum values
- `status`: Must be one of enum values
- `success_rate`: 0.0-1.0, default 1.0

**Database Table**: `droids`

---

## Intelligence Models

### IntelligenceItem

**Description**: Item in JARVIS intelligence feed

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "type": "string (enum: escalation, alert, insight, recommendation, required)",
  "priority": "string (enum: low, medium, high, critical, default: medium)",
  "title": "string (required, max 200 characters)",
  "message": "string (required, max 5000 characters)",
  "source": "string (required, source identifier)",
  "action_required": "boolean (default: false)",
  "created_at": "datetime (required)",
  "acknowledged_at": "datetime",
  "resolved_at": "datetime",
  "acknowledged_by": "uuid (foreign key -> users.id, optional)",
  "metadata": "object (optional, JSON, additional context)",
  "related_workflow_id": "uuid (foreign key -> workflows.id, optional)",
  "related_ticket_id": "uuid (foreign key -> helpdesk_tickets.id, optional)"
}
```

**Validation Rules**:
- `type`: Must be one of enum values
- `priority`: Must be one of enum values
- `title`: Max 200 characters, required
- `message`: Max 5000 characters, required
- `source`: Required, source identifier

**Database Table**: `intelligence_items`

**Relationships**:
- Belongs to: `User` (many-to-one, via `acknowledged_by`, optional)
- Belongs to: `Workflow` (many-to-one, optional)
- Belongs to: `HelpdeskTicket` (many-to-one, optional)

---

### Escalation

**Description**: Escalation to JARVIS

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "escalation_id": "string (unique, required)",
  "title": "string (required, max 200 characters)",
  "message": "string (required, max 5000 characters)",
  "status": "string (enum: pending, acknowledged, resolved, required)",
  "priority": "string (enum: low, medium, high, critical, default: medium)",
  "source": "string (required, source identifier)",
  "created_at": "datetime (required)",
  "acknowledged_at": "datetime",
  "resolved_at": "datetime",
  "acknowledged_by": "uuid (foreign key -> users.id, optional)",
  "context": "object (optional, JSON, escalation context)",
  "workflow_id": "uuid (foreign key -> workflows.id, optional)",
  "ticket_id": "uuid (foreign key -> helpdesk_tickets.id, optional)"
}
```

**Validation Rules**:
- `escalation_id`: Unique identifier, required
- `status`: Must be one of enum values
- `priority`: Must be one of enum values

**Database Table**: `escalations`

**Relationships**:
- Belongs to: `User` (many-to-one, via `acknowledged_by`, optional)
- Belongs to: `Workflow` (many-to-one, optional)
- Belongs to: `HelpdeskTicket` (many-to-one, optional)

---

## System Models

### SystemComponent

**Description**: System component status

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "component_name": "string (unique, required)",
  "status": "string (enum: operational, degraded, down, required)",
  "version": "string (optional)",
  "last_updated": "datetime (required)",
  "health_check_url": "string (optional)",
  "metadata": "object (optional, JSON, component-specific data)"
}
```

**Validation Rules**:
- `component_name`: Unique identifier, required
- `status`: Must be one of enum values

**Database Table**: `system_components`

---

### HealthCheck

**Description**: Health check result

**Schema**:
```json
{
  "id": "uuid (primary key)",
  "check_name": "string (required)",
  "status": "string (enum: healthy, unhealthy, required)",
  "timestamp": "datetime (required)",
  "response_time": "float (milliseconds, optional)",
  "error": "string (optional, error message if unhealthy)",
  "metadata": "object (optional, JSON)"
}
```

**Validation Rules**:
- `check_name`: Required
- `status`: Must be one of enum values
- `response_time`: Positive if set

**Database Table**: `health_checks`

---

## Common Types

### Timestamp

**Type**: `datetime`
**Format**: ISO 8601 (e.g., `2026-01-14T00:00:00Z`)
**Timezone**: UTC
**Storage**: Database datetime type

---

### UUID

**Type**: `uuid`
**Format**: RFC 4122 UUID v4
**Example**: `550e8400-e29b-41d4-a716-446655440000`
**Storage**: Database UUID type or string(36)

---

### JSON Object

**Type**: `object`
**Format**: Valid JSON
**Storage**: Database JSON type or TEXT with JSON validation
**Validation**: Must be valid JSON, schema validation per use case

---

### Enum

**Type**: `string`
**Format**: One of predefined values
**Storage**: Database ENUM type or string with constraint
**Validation**: Must match one of enum values

---

## Database Schemas

### PostgreSQL Schema

See `database_schemas.json` for complete PostgreSQL DDL statements.

### Key Constraints

- **Primary Keys**: All tables have UUID primary keys
- **Foreign Keys**: All relationships enforced with foreign key constraints
- **Unique Constraints**:
  - `users.username`
  - `users.email`
  - `devices.device_id`
  - `workflows.id`
  - `tickets.ticket_id`
  - `r5_entries.entry_id`
  - `r5_patterns.pattern_id`
- **Indexes**:
  - Foreign key columns
  - Frequently queried columns (status, created_at, user_id)
  - Search columns (full-text search indexes)

---

## Validation Rules

### String Lengths

- **Short strings**: 1-100 characters (names, identifiers)
- **Medium strings**: 1-200 characters (titles, descriptions)
- **Long strings**: 1-1000 characters (descriptions)
- **Very long strings**: 1-100000 characters (content, messages)

### Number Ranges

- **Priority**: 1-10 (integers)
- **Scores**: 0.0-1.0 (floats)
- **Counts**: 0+ (non-negative integers)
- **Times**: 0+ (non-negative floats, seconds)

### Date/Time

- **Created/Updated**: Always required, auto-set
- **Timestamps**: ISO 8601 format, UTC timezone
- **Date ranges**: Start <= End

### Enums

All enum values are case-sensitive and must match exactly.

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
