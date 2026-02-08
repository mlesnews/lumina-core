# Error Handling Documentation

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

All JARVIS Master Agent API endpoints follow a consistent error response format. This document describes the error handling strategy, error codes, HTTP status codes, and best practices for error handling.

---

## Standard Error Response Format

All error responses follow this consistent format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "Additional error details",
      "validation_errors": []
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "request-uuid-1234"
  }
}
```

### Error Response Fields

- **code**: Machine-readable error code (string)
- **message**: Human-readable error message (string)
- **details**: Additional error information (object, optional)
- **timestamp**: ISO 8601 timestamp of error (string)
- **request_id**: Unique request identifier for debugging (string)

---

## HTTP Status Codes

### 200 OK
**Usage**: Successful request
**Error Code**: None (success)

### 201 Created
**Usage**: Resource created successfully
**Error Code**: None (success)

### 202 Accepted
**Usage**: Request accepted for async processing
**Error Code**: None (success)

### 400 Bad Request
**Usage**: Invalid request data or parameters
**Error Codes**:
- `VALIDATION_ERROR`
- `INVALID_REQUEST`
- `MISSING_REQUIRED_FIELD`
- `INVALID_FORMAT`

**Example**:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": {
      "field": "name",
      "validation_errors": [
        "Name is required",
        "Name must be between 3 and 100 characters"
      ]
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### 401 Unauthorized
**Usage**: Authentication required or invalid
**Error Codes**:
- `AUTH_REQUIRED`
- `AUTH_INVALID`
- `AUTH_EXPIRED`
- `AUTH_REVOKED`

**Example**:
```json
{
  "error": {
    "code": "AUTH_EXPIRED",
    "message": "Authentication token expired",
    "details": {
      "expired_at": "2026-01-14T00:00:00Z"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### 403 Forbidden
**Usage**: Insufficient permissions
**Error Codes**:
- `PERMISSION_DENIED`
- `RESOURCE_ACCESS_DENIED`
- `OPERATION_NOT_ALLOWED`

**Example**:
```json
{
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "Insufficient permissions to access this resource",
    "details": {
      "required_permission": "workflows:write",
      "user_permissions": ["workflows:read"]
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### 404 Not Found
**Usage**: Resource not found
**Error Codes**:
- `RESOURCE_NOT_FOUND`
- `ENDPOINT_NOT_FOUND`

**Example**:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Workflow not found",
    "details": {
      "resource_type": "workflow",
      "resource_id": "workflow-uuid-1234"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### 409 Conflict
**Usage**: Resource conflict
**Error Codes**:
- `RESOURCE_CONFLICT`
- `DUPLICATE_RESOURCE`
- `CONCURRENT_MODIFICATION`

**Example**:
```json
{
  "error": {
    "code": "RESOURCE_CONFLICT",
    "message": "Workflow cannot be modified while running",
    "details": {
      "resource_id": "workflow-uuid-1234",
      "current_status": "running"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### 429 Too Many Requests
**Usage**: Rate limit exceeded
**Error Codes**:
- `RATE_LIMIT_EXCEEDED`

**Example**:
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later.",
    "details": {
      "retry_after": 60,
      "limit": 60,
      "window": "1 minute"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

**Headers**:
- `Retry-After`: Seconds to wait before retrying
- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Timestamp when limit resets

### 500 Internal Server Error
**Usage**: Server error
**Error Codes**:
- `INTERNAL_ERROR`
- `SERVICE_ERROR`

**Example**:
```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An internal server error occurred",
    "details": {
      "error_id": "err-uuid-1234"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

**Note**: Internal errors should not expose sensitive information. Error IDs are logged server-side for debugging.

### 503 Service Unavailable
**Usage**: Service temporarily unavailable
**Error Codes**:
- `SERVICE_UNAVAILABLE`
- `MAINTENANCE_MODE`
- `DEPENDENCY_UNAVAILABLE`

**Example**:
```json
{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service temporarily unavailable",
    "details": {
      "retry_after": 300,
      "reason": "Database connection failed"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

---

## Error Code Reference

### Authentication Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `AUTH_REQUIRED` | 401 | Authentication required |
| `AUTH_INVALID` | 401 | Invalid authentication credentials |
| `AUTH_EXPIRED` | 401 | Authentication token expired |
| `AUTH_REVOKED` | 401 | Authentication token revoked |

### Authorization Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `PERMISSION_DENIED` | 403 | Insufficient permissions |
| `RESOURCE_ACCESS_DENIED` | 403 | Access to resource denied |
| `OPERATION_NOT_ALLOWED` | 403 | Operation not allowed |

### Validation Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `VALIDATION_ERROR` | 400 | Request validation failed |
| `INVALID_REQUEST` | 400 | Invalid request format |
| `MISSING_REQUIRED_FIELD` | 400 | Required field missing |
| `INVALID_FORMAT` | 400 | Invalid data format |
| `INVALID_VALUE` | 400 | Invalid field value |

### Resource Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `RESOURCE_NOT_FOUND` | 404 | Resource not found |
| `RESOURCE_CONFLICT` | 409 | Resource conflict |
| `DUPLICATE_RESOURCE` | 409 | Duplicate resource |
| `CONCURRENT_MODIFICATION` | 409 | Concurrent modification detected |

### Rate Limiting

| Code | HTTP Status | Description |
|------|------------|-------------|
| `RATE_LIMIT_EXCEEDED` | 429 | Rate limit exceeded |

### System Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `INTERNAL_ERROR` | 500 | Internal server error |
| `SERVICE_ERROR` | 500 | Service error |
| `SERVICE_UNAVAILABLE` | 503 | Service temporarily unavailable |
| `MAINTENANCE_MODE` | 503 | Service in maintenance mode |
| `DEPENDENCY_UNAVAILABLE` | 503 | External dependency unavailable |

### Workflow Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `WORKFLOW_NOT_EXECUTABLE` | 400 | Workflow cannot be executed |
| `WORKFLOW_ALREADY_RUNNING` | 409 | Workflow is already running |
| `WORKFLOW_STEP_FAILED` | 500 | Workflow step execution failed |

### Chat Errors

| Code | HTTP Status | Description |
|------|------------|-------------|
| `MESSAGE_TOO_LONG` | 400 | Message exceeds maximum length |
| `INVALID_CONVERSATION` | 404 | Conversation not found |
| `CHAT_SERVICE_UNAVAILABLE` | 503 | Chat service unavailable |

---

## Error Handling Best Practices

### Client-Side

1. **Always Check Status Codes**
   ```typescript
   if (!response.ok) {
     const error = await response.json();
     // Handle error based on error.code
   }
   ```

2. **Handle Specific Error Codes**
   ```typescript
   switch (error.code) {
     case 'AUTH_EXPIRED':
       // Refresh token and retry
       break;
     case 'RATE_LIMIT_EXCEEDED':
       // Wait and retry
       break;
     case 'RESOURCE_NOT_FOUND':
       // Show not found message
       break;
   }
   ```

3. **Retry Logic**
   - Retry on 5xx errors (with exponential backoff)
   - Retry on 429 errors (respect Retry-After header)
   - Don't retry on 4xx errors (except 401 with token refresh)

4. **User-Friendly Messages**
   - Map error codes to user-friendly messages
   - Show validation errors inline
   - Provide actionable error messages

5. **Logging**
   - Log all errors with request_id
   - Include error details for debugging
   - Don't expose sensitive information to users

### Server-Side

1. **Consistent Error Format**
   - Always use standard error response format
   - Include request_id for traceability
   - Provide helpful error messages

2. **Error Logging**
   - Log all errors with full context
   - Include request_id in logs
   - Log stack traces for 5xx errors
   - Don't log sensitive data (passwords, tokens)

3. **Error Sanitization**
   - Don't expose internal implementation details
   - Sanitize error messages for production
   - Use error IDs for internal tracking

4. **Validation**
   - Validate all input data
   - Return specific validation errors
   - Use consistent validation error format

5. **Rate Limiting**
   - Return 429 with Retry-After header
   - Include rate limit information in headers
   - Log rate limit violations

---

## Error Response Examples

### Validation Error

**Request**:
```http
POST /api/v1/workflows HTTP/1.1
Content-Type: application/json

{
  "name": "ab"
}
```

**Response** (400 Bad Request):
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": {
      "field": "name",
      "validation_errors": [
        "Name must be at least 3 characters"
      ]
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### Authentication Error

**Request**:
```http
GET /api/v1/workflows HTTP/1.1
Authorization: Bearer expired_token
```

**Response** (401 Unauthorized):
```json
{
  "error": {
    "code": "AUTH_EXPIRED",
    "message": "Authentication token expired",
    "details": {
      "expired_at": "2026-01-14T00:00:00Z"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### Permission Error

**Request**:
```http
DELETE /api/v1/workflows/workflow-uuid HTTP/1.1
Authorization: Bearer token_with_read_only_permissions
```

**Response** (403 Forbidden):
```json
{
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "Insufficient permissions to delete workflows",
    "details": {
      "required_permission": "workflows:delete",
      "user_permissions": ["workflows:read"]
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### Rate Limit Error

**Request**:
```http
POST /api/v1/chat/message HTTP/1.1
Authorization: Bearer token
```

**Response** (429 Too Many Requests):
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 2026-01-14T00:01:00Z

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later.",
    "details": {
      "retry_after": 60,
      "limit": 60,
      "window": "1 minute"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

### Internal Error

**Request**:
```http
POST /api/v1/workflows/workflow-uuid/execute HTTP/1.1
Authorization: Bearer token
```

**Response** (500 Internal Server Error):
```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An internal server error occurred",
    "details": {
      "error_id": "err-uuid-1234"
    },
    "timestamp": "2026-01-14T00:00:00Z",
    "request_id": "req-123"
  }
}
```

**Note**: Error ID is logged server-side with full stack trace. Client should report error_id to support.

---

## Error Handling Implementation

### JavaScript/TypeScript

```typescript
class APIError extends Error {
  constructor(
    public code: string,
    public message: string,
    public details?: any,
    public requestId?: string,
    public statusCode?: number
  ) {
    super(message);
    this.name = 'APIError';
  }
}

async function handleResponse(response: Response) {
  if (!response.ok) {
    const errorData = await response.json();
    throw new APIError(
      errorData.error.code,
      errorData.error.message,
      errorData.error.details,
      errorData.error.request_id,
      response.status
    );
  }
  return response.json();
}

// Usage
try {
  const data = await fetch('/api/v1/workflows')
    .then(handleResponse);
} catch (error) {
  if (error instanceof APIError) {
    switch (error.code) {
      case 'AUTH_EXPIRED':
        // Refresh token
        break;
      case 'RATE_LIMIT_EXCEEDED':
        // Wait and retry
        break;
      default:
        // Show error message
        showError(error.message);
    }
  }
}
```

### Python

```python
class APIError(Exception):
    def __init__(self, code: str, message: str, details: dict = None,
                 request_id: str = None, status_code: int = None):
        self.code = code
        self.message = message
        self.details = details or {}
        self.request_id = request_id
        self.status_code = status_code
        super().__init__(self.message)

def handle_response(response: requests.Response):
    if not response.ok:
        error_data = response.json()
        error = error_data.get('error', {})
        raise APIError(
            code=error.get('code'),
            message=error.get('message'),
            details=error.get('details'),
            request_id=error.get('request_id'),
            status_code=response.status_code
        )
    return response.json()

# Usage
try:
    response = requests.get('/api/v1/workflows')
    data = handle_response(response)
except APIError as error:
    if error.code == 'AUTH_EXPIRED':
        # Refresh token
        pass
    elif error.code == 'RATE_LIMIT_EXCEEDED':
        # Wait and retry
        pass
    else:
        # Handle error
        print(f"Error: {error.message}")
```

---

## Debugging

### Request ID

Every error response includes a `request_id` that can be used for debugging:

1. **Client**: Log request_id with error
2. **Support**: Use request_id to find server logs
3. **Server**: Log request_id with all requests and errors

### Error Logging

Server-side error logging should include:
- Request ID
- Error code
- Error message
- Stack trace (for 5xx errors)
- Request details (method, path, headers)
- User context (if authenticated)
- Timestamp

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
