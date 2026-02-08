# Validation Rules Documentation

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines all validation rules for data models in the JARVIS Master Agent API. Validation occurs at multiple levels: API request validation, database constraints, and business logic validation.

---

## Validation Levels

1. **Client-Side Validation**: Initial validation in client applications
2. **API Request Validation**: Validation in API layer before processing
3. **Business Logic Validation**: Domain-specific validation rules
4. **Database Constraints**: Database-level validation and constraints

---

## String Validation

### Length Constraints

| Field Type | Min Length | Max Length | Examples |
|------------|-----------|------------|----------|
| Short String | 1 | 100 | Names, identifiers |
| Medium String | 1 | 200 | Titles, descriptions |
| Long String | 1 | 1000 | Detailed descriptions |
| Very Long String | 1 | 100000 | Content, messages |

### Format Constraints

#### Username
- **Pattern**: `^[a-zA-Z0-9_-]{3,50}$`
- **Rules**:
  - 3-50 characters
  - Alphanumeric, underscore, hyphen only
  - Case-sensitive
  - Must start with letter or number

#### Email
- **Pattern**: `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
- **Rules**:
  - Valid email format
  - Max 255 characters
  - Case-insensitive (normalized to lowercase)

#### UUID
- **Pattern**: `^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`
- **Rules**:
  - RFC 4122 UUID v4 format
  - Lowercase hexadecimal

#### Ticket ID
- **Pattern**: `^T[0-9]{9}$`
- **Rules**:
  - Starts with 'T'
  - Followed by exactly 9 digits
  - Example: `T000001234`

---

## Number Validation

### Integer Ranges

| Field | Min | Max | Default | Description |
|-------|-----|-----|---------|-------------|
| Priority | 1 | 10 | 5 | Workflow priority |
| Order | 1 | - | - | Step order (positive) |
| Count fields | 0 | - | 0 | Non-negative integers |

### Float Ranges

| Field | Min | Max | Default | Description |
|-------|-----|-----|---------|-------------|
| Scores | 0.0 | 1.0 | - | Relevance, confidence, success rate |
| Times | 0.0 | - | 0.0 | Execution time, response time (seconds) |

---

## Enum Validation

### Status Enums

#### Workflow Status
- **Values**: `pending`, `running`, `completed`, `failed`, `cancelled`
- **Transitions**:
  - `pending` → `running` (on execution)
  - `running` → `completed` (on success)
  - `running` → `failed` (on error)
  - `pending` → `cancelled` (on cancellation)
  - `running` → `cancelled` (on cancellation)

#### Workflow Step Status
- **Values**: `pending`, `running`, `completed`, `failed`, `skipped`
- **Transitions**: Similar to workflow status

#### Ticket Status
- **Values**: `open`, `in_progress`, `resolved`, `closed`
- **Transitions**:
  - `open` → `in_progress` (on assignment)
  - `in_progress` → `resolved` (on resolution)
  - `resolved` → `closed` (on closure)

#### Escalation Status
- **Values**: `pending`, `acknowledged`, `resolved`
- **Transitions**:
  - `pending` → `acknowledged` (on acknowledgment)
  - `acknowledged` → `resolved` (on resolution)

#### Component Status
- **Values**: `operational`, `degraded`, `down`
- **Transitions**: Any status can transition to any other status

#### Health Check Status
- **Values**: `healthy`, `unhealthy`
- **Transitions**: Bidirectional

### Priority Enums

#### Priority Levels
- **Values**: `low`, `medium`, `high`, `critical`
- **Order**: `low` < `medium` < `high` < `critical`

### Device Enums

#### Device Type
- **Values**: `desktop`, `mobile`, `widget`, `ide`

#### Platform
- **Values**: `windows`, `macos`, `linux`, `ios`, `android`

#### Droid Type
- **Values**: `C-3PO`, `R2-D2`, `K-2SO`, `2-1B`, `IG-88`, `Mouse Droid`, `R5-D4`, `Marvin`

### Intelligence Type
- **Values**: `escalation`, `alert`, `insight`, `recommendation`

---

## Date/Time Validation

### Timestamp Rules

- **Format**: ISO 8601 (`YYYY-MM-DDTHH:mm:ssZ`)
- **Timezone**: UTC (stored and returned)
- **Required Fields**: `created_at`, `updated_at`
- **Auto-Set**: `created_at` and `updated_at` set automatically

### Date Range Validation

- **Start <= End**: For date ranges, start must be <= end
- **Future Dates**: Expiration dates must be in future when created
- **Past Dates**: Historical dates cannot be in future

### Specific Date Rules

#### Token Expiration
- **Access Token**: Must be in future, typically 1 hour from creation
- **Refresh Token**: Must be in future, typically 30 days from creation

#### Workflow Dates
- **started_at**: Must be >= `created_at`
- **completed_at**: Must be >= `started_at` (if both set)
- **execution_time**: Calculated as `completed_at - started_at`

#### Pattern Dates
- **last_seen**: Must be >= `first_seen`

---

## JSON Validation

### JSON Object Rules

- **Valid JSON**: Must be valid JSON syntax
- **Schema Validation**: JSON objects validated against schemas per use case
- **Size Limits**: JSON fields limited to reasonable sizes (database dependent)

### JSON Schema Examples

#### User Preferences
```json
{
  "type": "object",
  "properties": {
    "theme": {
      "type": "string",
      "enum": ["light", "dark", "auto"]
    },
    "notifications": {
      "type": "boolean"
    },
    "language": {
      "type": "string",
      "pattern": "^[a-z]{2}$"
    }
  },
  "additionalProperties": false
}
```

#### Workflow Parameters
```json
{
  "type": "object",
  "additionalProperties": true
}
```

#### Metadata
```json
{
  "type": "object",
  "additionalProperties": true
}
```

---

## Array Validation

### Array Rules

- **Max Length**: Arrays typically limited to reasonable sizes
- **Element Validation**: Each element validated according to its type
- **Uniqueness**: Some arrays require unique elements

### Specific Array Rules

#### Permissions
- **Format**: `resource:action` (e.g., `workflows:read`, `workflows:write`)
- **Pattern**: `^[a-z_]+:[a-z_]+$`
- **Max Length**: No hard limit, but typically < 100

#### Tags
- **Format**: String array
- **Max Length**: 50 tags per resource
- **Element Length**: 1-50 characters per tag
- **Uniqueness**: Tags should be unique within array (normalized)

#### File References
- **Format**: UUID array
- **Validation**: Each element must be valid UUID
- **Max Length**: Typically < 100

---

## Relationship Validation

### Foreign Key Rules

- **Required Relationships**: Foreign keys marked as NOT NULL must have valid references
- **Cascade Rules**:
  - `ON DELETE CASCADE`: Child records deleted when parent deleted
  - `ON DELETE SET NULL`: Foreign key set to NULL when parent deleted
  - `ON DELETE RESTRICT`: Prevents deletion if child records exist

### Referential Integrity

- **Existence**: Referenced record must exist
- **Type Matching**: Foreign key type must match primary key type
- **Circular References**: Avoided where possible, handled carefully when necessary

---

## Business Logic Validation

### Workflow Validation

1. **Name Uniqueness**: Workflow names should be unique per user (recommended, not enforced)
2. **Step Order**: Step order must be sequential (1, 2, 3, ...)
3. **Step IDs**: Step IDs must be unique within workflow
4. **Execution**: Workflow can only be executed if status is `pending`
5. **Update**: Workflow can only be updated if status is `pending`
6. **Delete**: Workflow can only be deleted if status is `pending` or `failed`

### Chat Validation

1. **Message Length**: Messages limited to 100,000 characters
2. **Conversation Access**: Users can only access their own conversations
3. **Parent Message**: Parent message must exist and be in same conversation

### R5 Validation

1. **Entry ID Uniqueness**: Entry IDs must be globally unique
2. **Pattern ID Uniqueness**: Pattern IDs must be globally unique
3. **Pattern Frequency**: Frequency must be non-negative
4. **Pattern Dates**: `last_seen` must be >= `first_seen`

### Helpdesk Validation

1. **Ticket ID Format**: Must match pattern `T[0-9]{9}`
2. **Ticket ID Uniqueness**: Ticket IDs must be globally unique
3. **Assignment**: Tickets can be assigned to users or droids
4. **Status Transitions**: Must follow valid status transition rules

### Authentication Validation

1. **Password Strength**: Enforced at registration (not stored in API)
2. **Token Expiration**: Tokens validated on every request
3. **Token Revocation**: Revoked tokens cannot be used
4. **Device Limits**: Maximum 10 devices per user (configurable)

---

## Validation Error Messages

### Standard Error Format

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
    }
  }
}
```

### Field-Specific Errors

#### Required Field Missing
- **Code**: `MISSING_REQUIRED_FIELD`
- **Message**: `"{field} is required"`

#### Invalid Format
- **Code**: `INVALID_FORMAT`
- **Message**: `"{field} has invalid format"`

#### Out of Range
- **Code**: `INVALID_VALUE`
- **Message**: `"{field} must be between {min} and {max}"`

#### Invalid Enum Value
- **Code**: `INVALID_VALUE`
- **Message**: `"{field} must be one of: {values}"`

#### Invalid Status Transition
- **Code**: `INVALID_STATUS_TRANSITION`
- **Message**: `"Cannot transition from {current_status} to {new_status}"`

---

## Validation Implementation

### API Layer Validation

Validation should occur in API request handlers before business logic:

```python
def validate_workflow_create(data):
    errors = []

    if 'name' not in data:
        errors.append({'field': 'name', 'error': 'Name is required'})
    elif not (3 <= len(data['name']) <= 100):
        errors.append({'field': 'name', 'error': 'Name must be between 3 and 100 characters'})

    if 'priority' in data:
        if not (1 <= data['priority'] <= 10):
            errors.append({'field': 'priority', 'error': 'Priority must be between 1 and 10'})

    if errors:
        raise ValidationError(errors)

    return True
```

### Database Constraints

Database constraints provide final validation layer:

```sql
ALTER TABLE workflows
ADD CONSTRAINT chk_name_length
CHECK (LENGTH(name) >= 3 AND LENGTH(name) <= 100);

ALTER TABLE workflows
ADD CONSTRAINT chk_priority_range
CHECK (priority >= 1 AND priority <= 10);
```

---

## Testing Validation

### Test Cases

1. **Valid Data**: Test with valid data (should succeed)
2. **Missing Required Fields**: Test with missing required fields
3. **Invalid Formats**: Test with invalid formats (email, UUID, etc.)
4. **Out of Range**: Test with values outside valid ranges
5. **Invalid Enums**: Test with invalid enum values
6. **Invalid Status Transitions**: Test invalid status transitions
7. **Relationship Violations**: Test with invalid foreign keys

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
