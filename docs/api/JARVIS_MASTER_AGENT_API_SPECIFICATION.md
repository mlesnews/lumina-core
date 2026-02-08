# JARVIS Master Agent API Specification

**Version**: 1.0.0  
**Status**: 🟢 **ACTIVE**  
**Base URL**: `https://api.jarvis.local`  
**Last Updated**: 2026-01-14  
**Maintained By**: Cedarbrook Financial Services LLC

---

## Overview

The JARVIS Master Agent API is the unified API interface for all JARVIS multi-platform applications. All platforms (Windows 11 Widgets, Desktop Applications, Mobile Applications, IDE Chat Interface) use this unified API to interact with JARVIS systems.

### Architecture Principles

- **Unified Interface**: Single API for all platforms
- **RESTful Design**: Standard HTTP methods and status codes
- **WebSocket Support**: Real-time updates via WebSocket connections
- **Azure Service Bus**: All async communication via Azure Service Bus
- **Azure Key Vault**: All secrets retrieved from Azure Key Vault
- **Authentication**: Token-based authentication with refresh tokens
- **Versioning**: API versioning via URL path (`/v1/`, `/v2/`)

---

## Table of Contents

1. [Authentication](#authentication)
2. [Workflows](#workflows)
3. [Chat](#chat)
4. [R5 Knowledge](#r5-knowledge)
5. [Helpdesk](#helpdesk)
6. [JARVIS Intelligence](#jarvis-intelligence)
7. [System Status](#system-status)
8. [Error Handling](#error-handling)
9. [Rate Limiting](#rate-limiting)
10. [WebSocket API](#websocket-api)

---

## Authentication

### Base Path
`/api/v1/auth`

### Endpoints

#### POST `/api/v1/auth/login`

Authenticate user and receive access token.

**Request Body**:
```json
{
  "username": "string",
  "password": "string",
  "device_id": "string (optional)",
  "device_name": "string (optional)"
}
```

**Response** (200 OK):
```json
{
  "access_token": "string (JWT)",
  "refresh_token": "string",
  "token_type": "Bearer",
  "expires_in": 3600,
  "user": {
    "id": "string",
    "username": "string",
    "email": "string",
    "permissions": ["string"]
  }
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid credentials
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

**Rate Limit**: 5 requests per minute per IP

---

#### POST `/api/v1/auth/refresh`

Refresh access token using refresh token.

**Request Body**:
```json
{
  "refresh_token": "string"
}
```

**Response** (200 OK):
```json
{
  "access_token": "string (JWT)",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or expired refresh token
- `429 Too Many Requests`: Rate limit exceeded

**Rate Limit**: 10 requests per minute per IP

---

#### POST `/api/v1/auth/logout`

Invalidate access token and refresh token.

**Headers**:
- `Authorization: Bearer {access_token}` (required)

**Response** (200 OK):
```json
{
  "message": "Logged out successfully"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing token
- `500 Internal Server Error`: Server error

---

#### GET `/api/v1/auth/me`

Get current authenticated user information.

**Headers**:
- `Authorization: Bearer {access_token}` (required)

**Response** (200 OK):
```json
{
  "user": {
    "id": "string",
    "username": "string",
    "email": "string",
    "permissions": ["string"],
    "preferences": {
      "theme": "string",
      "notifications": true
    }
  }
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing token

---

## Workflows

### Base Path
`/api/v1/workflows`

All workflow endpoints require authentication.

### Endpoints

#### GET `/api/v1/workflows`

List all workflows with optional filtering.

**Query Parameters**:
- `status` (optional): Filter by status (`pending`, `running`, `completed`, `failed`)
- `limit` (optional): Number of results (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)
- `sort` (optional): Sort field (`created_at`, `updated_at`, `priority`) (default: `created_at`)
- `order` (optional): Sort order (`asc`, `desc`) (default: `desc`)

**Response** (200 OK):
```json
{
  "workflows": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "status": "pending|running|completed|failed",
      "priority": 1,
      "created_at": "2026-01-14T00:00:00Z",
      "updated_at": "2026-01-14T00:00:00Z",
      "created_by": "string",
      "execution_time": 123.45,
      "droid_assigned": "string"
    }
  ],
  "total": 100,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### GET `/api/v1/workflows/{workflow_id}`

Get specific workflow details.

**Path Parameters**:
- `workflow_id` (required): Workflow UUID

**Response** (200 OK):
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "status": "pending|running|completed|failed",
  "priority": 1,
  "created_at": "2026-01-14T00:00:00Z",
  "updated_at": "2026-01-14T00:00:00Z",
  "created_by": "string",
  "execution_time": 123.45,
  "droid_assigned": "string",
  "steps": [
    {
      "step_id": "string",
      "name": "string",
      "status": "pending|running|completed|failed",
      "started_at": "2026-01-14T00:00:00Z",
      "completed_at": "2026-01-14T00:00:00Z",
      "error": "string (if failed)"
    }
  ],
  "logs": [
    {
      "timestamp": "2026-01-14T00:00:00Z",
      "level": "info|warning|error",
      "message": "string"
    }
  ]
}
```

**Error Responses**:
- `404 Not Found`: Workflow not found
- `403 Forbidden`: Insufficient permissions

---

#### POST `/api/v1/workflows`

Create a new workflow.

**Request Body**:
```json
{
  "name": "string (required)",
  "description": "string (optional)",
  "priority": 5,
  "steps": [
    {
      "step_id": "string",
      "name": "string",
      "action": "string",
      "parameters": {}
    }
  ],
  "droid_preference": "string (optional)"
}
```

**Response** (201 Created):
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "status": "pending",
  "priority": 5,
  "created_at": "2026-01-14T00:00:00Z",
  "created_by": "string",
  "droid_assigned": "string"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid workflow data
- `403 Forbidden`: Insufficient permissions

**Rate Limit**: 30 requests per minute

---

#### PUT `/api/v1/workflows/{workflow_id}`

Update an existing workflow (only if status is `pending`).

**Path Parameters**:
- `workflow_id` (required): Workflow UUID

**Request Body**:
```json
{
  "name": "string (optional)",
  "description": "string (optional)",
  "priority": 5,
  "steps": [
    {
      "step_id": "string",
      "name": "string",
      "action": "string",
      "parameters": {}
    }
  ]
}
```

**Response** (200 OK):
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "status": "pending",
  "priority": 5,
  "updated_at": "2026-01-14T00:00:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid workflow data or workflow not in pending status
- `404 Not Found`: Workflow not found
- `403 Forbidden`: Insufficient permissions

---

#### DELETE `/api/v1/workflows/{workflow_id}`

Delete a workflow (only if status is `pending` or `failed`).

**Path Parameters**:
- `workflow_id` (required): Workflow UUID

**Response** (200 OK):
```json
{
  "message": "Workflow deleted successfully"
}
```

**Error Responses**:
- `400 Bad Request`: Workflow cannot be deleted (status is running or completed)
- `404 Not Found`: Workflow not found
- `403 Forbidden`: Insufficient permissions

---

#### POST `/api/v1/workflows/{workflow_id}/execute`

Execute a workflow.

**Path Parameters**:
- `workflow_id` (required): Workflow UUID

**Request Body**:
```json
{
  "parameters": {},
  "async": true
}
```

**Response** (202 Accepted - if async):
```json
{
  "workflow_id": "string",
  "status": "running",
  "execution_id": "string",
  "message": "Workflow execution started"
}
```

**Response** (200 OK - if sync):
```json
{
  "workflow_id": "string",
  "status": "completed",
  "execution_id": "string",
  "result": {},
  "execution_time": 123.45
}
```

**Error Responses**:
- `400 Bad Request`: Workflow cannot be executed
- `404 Not Found`: Workflow not found
- `403 Forbidden`: Insufficient permissions

**Rate Limit**: 20 requests per minute

---

#### GET `/api/v1/workflows/{workflow_id}/status`

Get real-time workflow execution status.

**Path Parameters**:
- `workflow_id` (required): Workflow UUID

**Response** (200 OK):
```json
{
  "workflow_id": "string",
  "status": "pending|running|completed|failed",
  "progress": 75,
  "current_step": "string",
  "started_at": "2026-01-14T00:00:00Z",
  "estimated_completion": "2026-01-14T00:00:00Z",
  "steps_completed": 3,
  "total_steps": 4
}
```

**Error Responses**:
- `404 Not Found`: Workflow not found

---

## Chat

### Base Path
`/api/v1/chat`

All chat endpoints require authentication.

### Endpoints

#### POST `/api/v1/chat/message`

Send a message to JARVIS.

**Request Body**:
```json
{
  "message": "string (required)",
  "context": {
    "conversation_id": "string (optional)",
    "file_references": ["string"],
    "code_context": "string"
  },
  "stream": false
}
```

**Response** (200 OK - if stream=false):
```json
{
  "message_id": "string",
  "conversation_id": "string",
  "response": "string",
  "timestamp": "2026-01-14T00:00:00Z",
  "suggestions": ["string"],
  "code_blocks": [
    {
      "language": "python",
      "code": "string"
    }
  ]
}
```

**Response** (200 OK - if stream=true):
Streaming response via Server-Sent Events (SSE) or WebSocket

**Error Responses**:
- `400 Bad Request`: Invalid message data
- `429 Too Many Requests`: Rate limit exceeded

**Rate Limit**: 60 requests per minute

---

#### GET `/api/v1/chat/history`

Get chat conversation history.

**Query Parameters**:
- `conversation_id` (optional): Specific conversation ID
- `limit` (optional): Number of messages (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)
- `since` (optional): Get messages since timestamp (ISO 8601)

**Response** (200 OK):
```json
{
  "conversations": [
    {
      "conversation_id": "string",
      "title": "string",
      "created_at": "2026-01-14T00:00:00Z",
      "updated_at": "2026-01-14T00:00:00Z",
      "message_count": 10,
      "last_message": "string"
    }
  ],
  "messages": [
    {
      "message_id": "string",
      "conversation_id": "string",
      "role": "user|assistant",
      "content": "string",
      "timestamp": "2026-01-14T00:00:00Z",
      "metadata": {}
    }
  ],
  "total": 100,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### DELETE `/api/v1/chat/conversations/{conversation_id}`

Delete a conversation.

**Path Parameters**:
- `conversation_id` (required): Conversation UUID

**Response** (200 OK):
```json
{
  "message": "Conversation deleted successfully"
}
```

**Error Responses**:
- `404 Not Found`: Conversation not found
- `403 Forbidden`: Insufficient permissions

---

#### GET `/api/v1/chat/stream`

Establish WebSocket connection for streaming chat.

**WebSocket URL**: `wss://api.jarvis.local/api/v1/chat/stream?token={access_token}`

**Message Format** (Client → Server):
```json
{
  "type": "message",
  "message": "string",
  "conversation_id": "string (optional)",
  "context": {}
}
```

**Message Format** (Server → Client):
```json
{
  "type": "chunk|complete|error",
  "message_id": "string",
  "conversation_id": "string",
  "content": "string",
  "done": false,
  "timestamp": "2026-01-14T00:00:00Z"
}
```

---

## R5 Knowledge

### Base Path
`/api/v1/r5`

All R5 endpoints require authentication.

### Endpoints

#### GET `/api/v1/r5/matrix`

Get R5 Living Context Matrix data.

**Query Parameters**:
- `session_id` (optional): Specific session ID
- `limit` (optional): Number of entries (default: 100, max: 500)
- `offset` (optional): Pagination offset (default: 0)
- `filter` (optional): Filter by category or tag

**Response** (200 OK):
```json
{
  "matrix": {
    "session_id": "string",
    "created_at": "2026-01-14T00:00:00Z",
    "updated_at": "2026-01-14T00:00:00Z",
    "entries": [
      {
        "entry_id": "string",
        "category": "string",
        "content": "string",
        "tags": ["string"],
        "patterns": ["string"],
        "timestamp": "2026-01-14T00:00:00Z",
        "metadata": {}
      }
    ],
    "patterns": [
      {
        "pattern_id": "string",
        "name": "string",
        "frequency": 10,
        "last_seen": "2026-01-14T00:00:00Z",
        "related_patterns": ["string"]
      }
    ]
  },
  "total_entries": 1000,
  "total_patterns": 50
}
```

**Rate Limit**: 60 requests per minute

---

#### POST `/api/v1/r5/search`

Search R5 knowledge base.

**Request Body**:
```json
{
  "query": "string (required)",
  "filters": {
    "category": "string",
    "tags": ["string"],
    "date_range": {
      "start": "2026-01-14T00:00:00Z",
      "end": "2026-01-14T00:00:00Z"
    }
  },
  "limit": 50,
  "offset": 0
}
```

**Response** (200 OK):
```json
{
  "results": [
    {
      "entry_id": "string",
      "category": "string",
      "content": "string",
      "tags": ["string"],
      "relevance_score": 0.95,
      "timestamp": "2026-01-14T00:00:00Z",
      "matches": {
        "query_terms": ["string"],
        "matched_sections": ["string"]
      }
    }
  ],
  "total": 25,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### GET `/api/v1/r5/patterns`

Get extracted patterns from R5.

**Query Parameters**:
- `limit` (optional): Number of patterns (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)
- `sort` (optional): Sort by (`frequency`, `last_seen`, `name`) (default: `frequency`)
- `order` (optional): Sort order (`asc`, `desc`) (default: `desc`)

**Response** (200 OK):
```json
{
  "patterns": [
    {
      "pattern_id": "string",
      "name": "string",
      "description": "string",
      "frequency": 10,
      "first_seen": "2026-01-14T00:00:00Z",
      "last_seen": "2026-01-14T00:00:00Z",
      "related_patterns": ["string"],
      "categories": ["string"],
      "metadata": {}
    }
  ],
  "total": 100,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### GET `/api/v1/r5/patterns/{pattern_id}`

Get specific pattern details.

**Path Parameters**:
- `pattern_id` (required): Pattern UUID

**Response** (200 OK):
```json
{
  "pattern_id": "string",
  "name": "string",
  "description": "string",
  "frequency": 10,
  "first_seen": "2026-01-14T00:00:00Z",
  "last_seen": "2026-01-14T00:00:00Z",
  "related_patterns": [
    {
      "pattern_id": "string",
      "name": "string",
      "relationship": "similar|related|opposite"
    }
  ],
  "occurrences": [
    {
      "entry_id": "string",
      "timestamp": "2026-01-14T00:00:00Z",
      "context": "string"
    }
  ],
  "categories": ["string"],
  "metadata": {}
}
```

**Error Responses**:
- `404 Not Found`: Pattern not found

---

## Helpdesk

### Base Path
`/api/v1/helpdesk`

All helpdesk endpoints require authentication.

### Endpoints

#### GET `/api/v1/helpdesk/status`

Get helpdesk system status.

**Response** (200 OK):
```json
{
  "status": "operational|degraded|down",
  "coordinator": "C-3PO",
  "droids": {
    "total": 8,
    "available": 7,
    "busy": 1,
    "offline": 0,
    "list": [
      {
        "droid_id": "string",
        "name": "string",
        "status": "available|busy|offline",
        "current_workflows": 1,
        "queue_length": 0
      }
    ]
  },
  "queue": {
    "pending": 5,
    "processing": 2,
    "completed_today": 50
  }
}
```

**Rate Limit**: 30 requests per minute

---

#### GET `/api/v1/helpdesk/droids`

Get list of all droids with detailed status.

**Query Parameters**:
- `status` (optional): Filter by status (`available`, `busy`, `offline`)

**Response** (200 OK):
```json
{
  "droids": [
    {
      "droid_id": "string",
      "name": "string",
      "type": "C-3PO|R2-D2|K-2SO|2-1B|IG-88|Mouse Droid|R5-D4|Marvin",
      "status": "available|busy|offline",
      "current_workflows": 1,
      "queue_length": 0,
      "total_workflows_processed": 100,
      "success_rate": 0.98,
      "average_processing_time": 45.5,
      "last_active": "2026-01-14T00:00:00Z"
    }
  ],
  "total": 8
}
```

**Rate Limit**: 30 requests per minute

---

#### POST `/api/v1/helpdesk/escalate`

Escalate an issue to JARVIS.

**Request Body**:
```json
{
  "workflow_id": "string (optional)",
  "ticket_id": "string (optional)",
  "priority": "low|medium|high|critical",
  "reason": "string (required)",
  "context": {}
}
```

**Response** (202 Accepted):
```json
{
  "escalation_id": "string",
  "status": "pending",
  "message": "Escalation submitted to JARVIS",
  "estimated_response_time": "5 minutes"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid escalation data
- `429 Too Many Requests`: Rate limit exceeded

**Rate Limit**: 10 requests per minute

---

#### GET `/api/v1/helpdesk/tickets`

Get helpdesk tickets.

**Query Parameters**:
- `status` (optional): Filter by status (`open`, `in_progress`, `resolved`, `closed`)
- `priority` (optional): Filter by priority (`low`, `medium`, `high`, `critical`)
- `limit` (optional): Number of results (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)

**Response** (200 OK):
```json
{
  "tickets": [
    {
      "ticket_id": "string",
      "title": "string",
      "status": "open|in_progress|resolved|closed",
      "priority": "low|medium|high|critical",
      "created_at": "2026-01-14T00:00:00Z",
      "updated_at": "2026-01-14T00:00:00Z",
      "created_by": "string",
      "assigned_to": "string",
      "droid_assigned": "string"
    }
  ],
  "total": 100,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

## JARVIS Intelligence

### Base Path
`/api/v1/intelligence`

All intelligence endpoints require authentication.

### Endpoints

#### GET `/api/v1/intelligence/feed`

Get JARVIS intelligence feed.

**Query Parameters**:
- `limit` (optional): Number of items (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)
- `type` (optional): Filter by type (`escalation`, `alert`, `insight`, `recommendation`)
- `priority` (optional): Filter by priority (`low`, `medium`, `high`, `critical`)

**Response** (200 OK):
```json
{
  "feed": [
    {
      "id": "string",
      "type": "escalation|alert|insight|recommendation",
      "priority": "low|medium|high|critical",
      "title": "string",
      "message": "string",
      "timestamp": "2026-01-14T00:00:00Z",
      "source": "string",
      "action_required": true,
      "metadata": {}
    }
  ],
  "total": 100,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### GET `/api/v1/intelligence/escalations`

Get JARVIS escalations.

**Query Parameters**:
- `status` (optional): Filter by status (`pending`, `acknowledged`, `resolved`)
- `limit` (optional): Number of results (default: 50, max: 100)
- `offset` (optional): Pagination offset (default: 0)

**Response** (200 OK):
```json
{
  "escalations": [
    {
      "escalation_id": "string",
      "title": "string",
      "message": "string",
      "status": "pending|acknowledged|resolved",
      "priority": "low|medium|high|critical",
      "created_at": "2026-01-14T00:00:00Z",
      "acknowledged_at": "2026-01-14T00:00:00Z",
      "resolved_at": "2026-01-14T00:00:00Z",
      "source": "string",
      "context": {}
    }
  ],
  "total": 25,
  "limit": 50,
  "offset": 0
}
```

**Rate Limit**: 60 requests per minute

---

#### POST `/api/v1/intelligence/escalations/{escalation_id}/acknowledge`

Acknowledge an escalation.

**Path Parameters**:
- `escalation_id` (required): Escalation UUID

**Response** (200 OK):
```json
{
  "escalation_id": "string",
  "status": "acknowledged",
  "acknowledged_at": "2026-01-14T00:00:00Z"
}
```

**Error Responses**:
- `404 Not Found`: Escalation not found
- `400 Bad Request`: Escalation cannot be acknowledged

---

## System Status

### Base Path
`/api/v1/system`

All system endpoints require authentication.

### Endpoints

#### GET `/api/v1/system/status`

Get overall system status.

**Response** (200 OK):
```json
{
  "status": "operational|degraded|down",
  "version": "6.0.0",
  "uptime": 86400,
  "components": {
    "master_feedback_loop": {
      "status": "operational",
      "version": "6.0.0",
      "last_updated": "2026-01-14T00:00:00Z"
    },
    "r5_matrix": {
      "status": "operational",
      "api_server": "http://localhost:8000",
      "last_updated": "2026-01-14T00:00:00Z"
    },
    "helpdesk": {
      "status": "operational",
      "coordinator": "C-3PO",
      "droids_available": 7,
      "last_updated": "2026-01-14T00:00:00Z"
    },
    "azure_service_bus": {
      "status": "operational",
      "namespace": "jarvis-lumina-bus",
      "last_updated": "2026-01-14T00:00:00Z"
    },
    "azure_key_vault": {
      "status": "operational",
      "vault_name": "jarvis-lumina",
      "last_updated": "2026-01-14T00:00:00Z"
    }
  },
  "timestamp": "2026-01-14T00:00:00Z"
}
```

**Rate Limit**: 30 requests per minute

---

#### GET `/api/v1/system/health`

Health check endpoint (no authentication required for monitoring).

**Response** (200 OK):
```json
{
  "status": "healthy|unhealthy",
  "timestamp": "2026-01-14T00:00:00Z",
  "checks": {
    "database": "healthy",
    "azure_service_bus": "healthy",
    "azure_key_vault": "healthy",
    "r5_api": "healthy"
  }
}
```

**Response** (503 Service Unavailable):
```json
{
  "status": "unhealthy",
  "timestamp": "2026-01-14T00:00:00Z",
  "checks": {
    "database": "healthy",
    "azure_service_bus": "unhealthy",
    "azure_key_vault": "healthy",
    "r5_api": "healthy"
  },
  "errors": [
    "Azure Service Bus connection failed"
  ]
}
```

---

## Error Handling

### Standard Error Response Format

All error responses follow this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {},
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "string"
  }
}
```

### HTTP Status Codes

- `200 OK`: Request successful
- `201 Created`: Resource created successfully
- `202 Accepted`: Request accepted for async processing
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required or invalid
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `409 Conflict`: Resource conflict (e.g., duplicate)
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error
- `503 Service Unavailable`: Service temporarily unavailable

### Error Codes

- `AUTH_REQUIRED`: Authentication required
- `AUTH_INVALID`: Invalid authentication credentials
- `AUTH_EXPIRED`: Authentication token expired
- `PERMISSION_DENIED`: Insufficient permissions
- `RESOURCE_NOT_FOUND`: Resource not found
- `VALIDATION_ERROR`: Request validation failed
- `RATE_LIMIT_EXCEEDED`: Rate limit exceeded
- `SERVICE_UNAVAILABLE`: Service temporarily unavailable
- `INTERNAL_ERROR`: Internal server error

---

## Rate Limiting

### Rate Limit Headers

All responses include rate limit headers:

- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Timestamp when rate limit resets

### Rate Limit Response

When rate limit is exceeded (429):

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later.",
    "retry_after": 60,
    "timestamp": "2026-01-14T00:00:00Z"
  }
}
```

### Default Rate Limits

- **Authentication endpoints**: 5-10 requests per minute
- **Workflow endpoints**: 20-60 requests per minute
- **Chat endpoints**: 60 requests per minute
- **R5 Knowledge endpoints**: 60 requests per minute
- **Helpdesk endpoints**: 30-60 requests per minute
- **Intelligence endpoints**: 60 requests per minute
- **System Status endpoints**: 30 requests per minute

---

## WebSocket API

### Connection

**WebSocket URL**: `wss://api.jarvis.local/api/v1/ws?token={access_token}`

### Message Types

#### Client → Server

**Subscribe to Updates**:
```json
{
  "type": "subscribe",
  "channels": ["workflows", "intelligence", "helpdesk"]
}
```

**Unsubscribe from Updates**:
```json
{
  "type": "unsubscribe",
  "channels": ["workflows"]
}
```

**Ping**:
```json
{
  "type": "ping"
}
```

#### Server → Client

**Update Notification**:
```json
{
  "type": "update",
  "channel": "workflows",
  "data": {
    "workflow_id": "string",
    "status": "running",
    "progress": 50
  },
  "timestamp": "2026-01-14T00:00:00Z"
}
```

**Pong**:
```json
{
  "type": "pong",
  "timestamp": "2026-01-14T00:00:00Z"
}
```

**Error**:
```json
{
  "type": "error",
  "code": "ERROR_CODE",
  "message": "Error message"
}
```

### Available Channels

- `workflows`: Workflow status updates
- `intelligence`: Intelligence feed updates
- `helpdesk`: Helpdesk status updates
- `r5`: R5 knowledge updates
- `system`: System status updates

---

## Versioning

### API Versioning Strategy

- **URL Path Versioning**: `/api/v1/`, `/api/v2/`
- **Default Version**: If no version specified, defaults to latest stable version
- **Version Deprecation**: Deprecated versions supported for 6 months after deprecation announcement

### Version Headers

- `API-Version`: Requested API version
- `Supported-Versions`: List of supported versions

---

## Security

### Authentication

- **Token-based**: JWT access tokens
- **Refresh Tokens**: Long-lived refresh tokens for token renewal
- **Token Expiration**: Access tokens expire in 1 hour
- **Token Storage**: Tokens stored securely, never in localStorage for web apps

### Authorization

- **Role-based Access Control (RBAC)**: Permissions based on user roles
- **Resource-level Permissions**: Fine-grained permissions per resource
- **API Keys**: For service-to-service communication

### Data Protection

- **HTTPS Required**: All API communication over HTTPS
- **TLS 1.3**: Minimum TLS version
- **Secrets Management**: All secrets in Azure Key Vault
- **Data Encryption**: Sensitive data encrypted at rest and in transit

---

## Changelog

### Version 1.0.0 (2026-01-14)

- Initial API specification
- All core endpoints defined
- Authentication system
- Workflow management
- Chat interface
- R5 Knowledge integration
- Helpdesk integration
- JARVIS Intelligence feed
- System status endpoints
- WebSocket support
- Error handling
- Rate limiting

---

**Last Updated**: 2026-01-14  
**Next Review**: 2026-01-21  
**Status**: 🟢 **ACTIVE**
