# Business Logic Documentation

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines the business logic rules and workflows for the JARVIS Master Agent system. Business logic implements domain rules and orchestrates system behavior.

---

## Table of Contents

1. [Workflow Business Logic](#workflow-business-logic)
2. [Authentication Business Logic](#authentication-business-logic)
3. [Helpdesk Business Logic](#helpdesk-business-logic)
4. [R5 Knowledge Business Logic](#r5-knowledge-business-logic)
5. [Escalation Business Logic](#escalation-business-logic)
6. [Verification Business Logic](#verification-business-logic)

---

## Workflow Business Logic

### Workflow Creation Rules

1. **Name Validation**: Workflow name must be 3-100 characters, unique per user (recommended)
2. **Step Validation**: Workflow must have at least one step
3. **Step Order**: Steps must have sequential order (1, 2, 3, ...)
4. **Step ID Uniqueness**: Step IDs must be unique within workflow
5. **Priority Default**: Default priority is 5 if not specified
6. **Status Initialization**: New workflows start with status 'pending'

### Workflow Execution Rules

1. **Execution Eligibility**: Only workflows with status 'pending' can be executed
2. **Concurrent Execution**: Workflows cannot be executed concurrently (status check)
3. **Step Execution**: Steps executed sequentially in order
4. **Failure Handling**: If any step fails, workflow status set to 'failed', remaining steps not executed
5. **Completion**: Workflow marked 'completed' only when all steps complete successfully
6. **Execution Time**: Execution time calculated as (completed_at - started_at)

### Workflow Update Rules

1. **Update Eligibility**: Only workflows with status 'pending' can be updated
2. **Running Workflows**: Running workflows cannot be updated (status check)
3. **Step Modification**: Steps can be added, modified, or removed if workflow is 'pending'
4. **Order Recalculation**: Step order recalculated if steps removed

### Workflow Deletion Rules

1. **Deletion Eligibility**: Only workflows with status 'pending' or 'failed' can be deleted
2. **Running Workflows**: Running workflows cannot be deleted
3. **Completed Workflows**: Completed workflows cannot be deleted (archive instead)
4. **Cascade Deletion**: Deleting workflow deletes all associated steps and logs

---

## Authentication Business Logic

### Login Rules

1. **Credential Validation**: Username and password must be provided
2. **User Existence**: User must exist and be active
3. **Password Verification**: Password verified against hash in database
4. **Device Tracking**: Device ID and name tracked for multi-device support
5. **Token Generation**: Access token (1 hour) and refresh token (30 days) generated
6. **Last Login Update**: User's last_login timestamp updated

### Token Refresh Rules

1. **Refresh Token Validation**: Refresh token must be valid and not expired
2. **Token Revocation Check**: Refresh token must not be revoked
3. **New Token Generation**: New access token generated (1 hour expiration)
4. **Token Rotation**: New refresh token generated, old one revoked (optional, security best practice)
5. **Device Validation**: Refresh token must match device (if device tracking enabled)

### Logout Rules

1. **Token Revocation**: Access token and refresh token revoked
2. **Session Cleanup**: Session data cleared
3. **Device Tracking**: Device marked as logged out (optional)

### Permission Rules

1. **Permission Check**: User permissions checked on every protected endpoint
2. **Resource-Level Permissions**: Permissions checked at resource level (e.g., workflows:read, workflows:write)
3. **Permission Inheritance**: User permissions inherited from roles
4. **Permission Caching**: Permissions cached in JWT token for performance

---

## Helpdesk Business Logic

### Ticket Creation Rules

1. **Ticket ID Generation**: Ticket ID generated as 'T' + 9 digits (e.g., T000001234)
2. **Ticket ID Uniqueness**: Ticket IDs must be globally unique
3. **Status Initialization**: New tickets start with status 'open'
4. **Priority Default**: Default priority is 'medium' if not specified
5. **Creator Assignment**: Created_by set to current user
6. **Timestamp Initialization**: created_at and updated_at set to current time

### Ticket Assignment Rules

1. **Assignment Eligibility**: Only tickets with status 'open' or 'in_progress' can be assigned
2. **User Assignment**: Tickets can be assigned to users or droids
3. **Droid Assignment**: Droid assignment uses droid assignment algorithm
4. **Status Update**: Ticket status updated to 'in_progress' on assignment
5. **Assignment Notification**: Assignment notification sent to assignee

### Ticket Resolution Rules

1. **Resolution Eligibility**: Only tickets with status 'in_progress' can be resolved
2. **Status Transition**: Status changed to 'resolved' on resolution
3. **Resolution Timestamp**: resolved_at timestamp set
4. **Closure**: Tickets can be closed after resolution (status 'closed')
5. **Closure Timestamp**: closed_at timestamp set on closure

### Droid Assignment Rules

1. **Availability Check**: Only available or busy droids with capacity considered
2. **Capability Matching**: Droids must have required capabilities
3. **Workload Consideration**: Droid workload considered in assignment
4. **Priority Handling**: Critical workflows prefer specialized droids (IG-88)
5. **Status Update**: Droid status updated to 'busy' if current_workflows > 0

---

## R5 Knowledge Business Logic

### Knowledge Entry Rules

1. **Entry ID Generation**: Entry IDs must be globally unique
2. **Content Validation**: Content must be non-empty, max 100,000 characters
3. **Category Required**: Category must be provided
4. **Timestamp**: Timestamp set to current time if not provided
5. **Pattern Extraction**: Patterns extracted automatically if ExtractPatterns = true
6. **Tag Normalization**: Tags normalized (lowercase, trimmed, deduplicated)

### Pattern Extraction Rules

1. **Automatic Extraction**: Patterns extracted from knowledge entries automatically
2. **Frequency Tracking**: Pattern frequency incremented on each occurrence
3. **Last Seen Update**: Pattern last_seen timestamp updated on occurrence
4. **Relationship Detection**: Relationships detected between patterns
5. **Pattern Naming**: Pattern names derived from n-grams

### Search Rules

1. **Query Tokenization**: Search query tokenized into terms
2. **Relevance Scoring**: Results scored by relevance (0.0-1.0)
3. **Filtering**: Results filtered by category, tags, date range
4. **Pagination**: Results paginated (default 50, max 100)
5. **Sorting**: Results sorted by relevance score (descending)

---

## Escalation Business Logic

### Escalation Creation Rules

1. **Escalation ID Generation**: Escalation IDs must be globally unique
2. **Status Initialization**: New escalations start with status 'pending'
3. **Priority Required**: Priority must be specified
4. **Source Required**: Source system must be specified
5. **Context Optional**: Context object optional but recommended
6. **Related Resources**: Can reference workflow_id or ticket_id

### Escalation Acknowledgment Rules

1. **Acknowledgment Eligibility**: Only escalations with status 'pending' can be acknowledged
2. **Acknowledger Assignment**: acknowledged_by set to current user
3. **Status Update**: Status changed to 'acknowledged'
4. **Timestamp**: acknowledged_at timestamp set
5. **Notification**: Acknowledgment notification sent

### Escalation Resolution Rules

1. **Resolution Eligibility**: Only escalations with status 'acknowledged' can be resolved
2. **Status Update**: Status changed to 'resolved'
3. **Timestamp**: resolved_at timestamp set
4. **Resolution Context**: Resolution context can be added

---

## Verification Business Logic

### Verification Request Rules

1. **Verification ID Generation**: Verification IDs must be globally unique
2. **Workflow Reference**: Verification must reference workflow_id
3. **Verification Type**: Type must be specified (pre_execution, data_integrity, etc.)
4. **Data Required**: Data object required for verification
5. **Status Initialization**: New verifications start with status 'pending'

### Verification Execution Rules

1. **Type-Specific Logic**: Verification logic depends on verification type
2. **Pre-Execution Verification**: Validates workflow before execution
3. **Data Integrity Verification**: Validates data integrity
4. **Aggregation Verification**: Validates aggregation results
5. **Pattern Extraction Verification**: Validates pattern extraction

### Verification Result Rules

1. **Status Determination**: Status set to 'verified', 'failed', or 'warning'
2. **Result Storage**: Verification results stored
3. **Error Collection**: Errors collected if verification fails
4. **Workflow Impact**: Failed verifications can block workflow execution
5. **Notification**: Verification results notified to relevant systems

---

## Business Rule Enforcement

### Validation Layer

All business rules enforced at API layer before database operations:

1. **Request Validation**: Validate request data against business rules
2. **State Validation**: Validate current state allows requested operation
3. **Permission Validation**: Validate user has required permissions
4. **Resource Validation**: Validate referenced resources exist

### State Machine Enforcement

State transitions enforced by business logic:

1. **Valid Transitions**: Only valid state transitions allowed
2. **Transition Validation**: Validate transition is allowed from current state
3. **State Update**: Update state atomically with operation
4. **Audit Logging**: Log all state transitions

---

## Business Logic Implementation

### Rule Engine

Business rules implemented as:

1. **Validation Functions**: Separate validation functions for each rule
2. **State Machine**: State machine for workflow/ticket status transitions
3. **Business Service Layer**: Business logic in service layer, not controller layer
4. **Rule Configuration**: Configurable rules where appropriate

### Error Handling

Business rule violations return appropriate errors:

1. **Validation Errors**: Return 400 Bad Request with validation details
2. **State Errors**: Return 409 Conflict for invalid state transitions
3. **Permission Errors**: Return 403 Forbidden for permission violations
4. **Resource Errors**: Return 404 Not Found for missing resources

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
