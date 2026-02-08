# Azure Service Bus Retry Policies

**Version**: 1.0.0
**Last Updated**: 2026-01-14
**Status**: 🟢 **ACTIVE**

---

## Overview

This document defines retry policies for Azure Service Bus queues and subscriptions. Retry policies ensure message delivery reliability and handle transient failures.

---

## Default Retry Policy

### Configuration

- **Max Delivery Count**: 10
- **Time To Live (TTL)**: 7 days
- **Lock Duration**: 60 seconds
- **Retry Strategy**: Exponential backoff

### Exponential Backoff Schedule

| Attempt | Delay | Cumulative Time |
|---------|-------|-----------------|
| 1 | Immediate | 0s |
| 2 | 1s | 1s |
| 3 | 2s | 3s |
| 4 | 4s | 7s |
| 5 | 8s | 15s |
| 6 | 16s | 31s |
| 7 | 32s | 63s |
| 8 | 60s (capped) | 123s |
| 9 | 60s | 183s |
| 10 | 60s | 243s |

**After Max Delivery Count**: Message moved to dead-letter queue

---

## Per-Queue Retry Policies

### jarvis-escalation-queue

**Max Delivery Count**: 10
**Lock Duration**: 120 seconds
**TTL**: 7 days

**Rationale**: Escalations are critical, allow more retries. Longer lock duration for complex escalation processing.

---

### workflow-execution-queue

**Max Delivery Count**: 5
**Lock Duration**: 300 seconds (5 minutes)
**TTL**: 7 days

**Rationale**: Workflows can take time to execute. Fewer retries to avoid duplicate executions. Longer lock duration for workflow processing.

---

### r5-ingestion-queue

**Max Delivery Count**: 10
**Lock Duration**: 60 seconds
**TTL**: 7 days

**Rationale**: Knowledge ingestion is important but can be retried. Standard lock duration.

---

### verification-queue

**Max Delivery Count**: 5
**Lock Duration**: 120 seconds
**TTL**: 7 days

**Rationale**: Verifications should be quick. Fewer retries to avoid delays. Moderate lock duration.

---

### droid-assignment-queue

**Max Delivery Count**: 5
**Lock Duration**: 60 seconds
**TTL**: 7 days

**Rationale**: Droid assignments should be quick. Fewer retries. Standard lock duration.

---

## Per-Subscription Retry Policies

### High-Priority Subscriptions

**workflow-processor**: Max Delivery Count 10, Lock Duration 60s
**jarvis-escalation-handler**: Max Delivery Count 10, Lock Duration 120s
**r5-ingestion-processor**: Max Delivery Count 10, Lock Duration 60s

### Standard Subscriptions

**workflow-notifications**: Max Delivery Count 5, Lock Duration 60s
**escalation-notifications**: Max Delivery Count 3, Lock Duration 60s
**response-notifications**: Max Delivery Count 3, Lock Duration 60s

### Audit Subscriptions

**workflow-audit**: Max Delivery Count 1, Lock Duration 60s
**verification-audit**: Max Delivery Count 1, Lock Duration 60s

**Rationale**: Audit messages should not be retried. If processing fails, log error but don't retry.

---

## Retry Strategy Implementation

### Exponential Backoff Algorithm

```python
def calculate_retry_delay(attempt: int, max_delay: int = 60) -> int:
    """
    Calculate retry delay using exponential backoff.

    Args:
        attempt: Retry attempt number (1-based)
        max_delay: Maximum delay in seconds

    Returns:
        Delay in seconds
    """
    if attempt == 1:
        return 0  # Immediate first attempt

    delay = min(2 ** (attempt - 2), max_delay)
    return delay
```

### Retry Decision Logic

```python
def should_retry(error: Exception, attempt: int, max_attempts: int) -> bool:
    """
    Determine if message should be retried.

    Args:
        error: Exception that occurred
        attempt: Current attempt number
        max_attempts: Maximum number of attempts

    Returns:
        True if should retry, False otherwise
    """
    if attempt >= max_attempts:
        return False

    # Retry on transient errors
    transient_errors = [
        "Timeout",
        "ConnectionError",
        "ServiceUnavailable",
        "Throttling"
    ]

    error_str = str(error)
    for transient_error in transient_errors:
        if transient_error in error_str:
            return True

    # Don't retry on permanent errors
    permanent_errors = [
        "ValidationError",
        "AuthenticationError",
        "AuthorizationError",
        "NotFound"
    ]

    for permanent_error in permanent_errors:
        if permanent_error in error_str:
            return False

    # Default: retry on unknown errors
    return True
```

---

## Dead-Letter Queue Handling

### When Messages Go to Dead-Letter

1. **Max Delivery Count Exceeded**: Message retried maximum times
2. **TTL Expired**: Message time-to-live exceeded
3. **Processing Error**: Permanent error during processing

### Dead-Letter Processing

**Monitoring**: Dead-letter queues monitored and alerted

**Recovery**: Dead-letter messages can be:
- Resubmitted to original queue/topic
- Manually reviewed and processed
- Automatically retried after fix (if applicable)

**Retention**: Dead-letter messages retained for 30 days

---

## Best Practices

1. **Appropriate Max Delivery Count**: Balance between reliability and avoiding infinite retries
2. **Lock Duration**: Set based on expected processing time
3. **TTL**: Set based on message importance and freshness requirements
4. **Idempotency**: Ensure message processing is idempotent (safe to retry)
5. **Monitoring**: Monitor retry rates and dead-letter queues
6. **Alerting**: Alert on high dead-letter counts or retry rates

---

## Monitoring Retry Behavior

### Key Metrics

- **Retry Count**: Number of retries per message
- **Dead-Letter Count**: Messages in dead-letter queue
- **Average Processing Time**: Time to successfully process message
- **Retry Rate**: Percentage of messages requiring retries

### Alerts

- **High Dead-Letter Count**: Alert when dead-letter count > 100
- **High Retry Rate**: Alert when retry rate > 10%
- **Processing Failures**: Alert on processing errors

---

**Last Updated**: 2026-01-14
**Next Review**: 2026-01-21
**Status**: 🟢 **ACTIVE**
