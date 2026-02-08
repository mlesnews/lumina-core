# Health Checks

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

Health check endpoints and procedures for system health monitoring.

---

## Health Check Endpoint

### GET /api/v1/system/health

**Purpose**: Overall system health check

**Response**:
```json
{
  "status": "healthy|unhealthy",
  "timestamp": "2026-01-14T00:00:00Z",
  "checks": {
    "database": "healthy|unhealthy",
    "azure_service_bus": "healthy|unhealthy",
    "azure_key_vault": "healthy|unhealthy",
    "r5_api": "healthy|unhealthy"
  },
  "errors": []
}
```

---

## Component Health Checks

### Database Health Check

- Connection test
- Query execution test
- Response time check

### Service Bus Health Check

- Connection test
- Topic/queue availability
- Message publish test

### Key Vault Health Check

- Connection test
- Secret read test
- Access validation

### R5 API Health Check

- API endpoint test
- Response time check
- Functionality test

---

## Health Check Frequency

- **Liveness Probe**: Every 30 seconds
- **Readiness Probe**: Every 10 seconds
- **Startup Probe**: Every 5 seconds (initial)

---

## Health Check Failure Handling

### Unhealthy Status

- Mark service as unhealthy
- Stop accepting new requests
- Alert operations team
- Trigger auto-recovery if configured

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
