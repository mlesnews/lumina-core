# Azure Service Bus Usage Guide

**Version**: 1.0.0  
**Last Updated**: 2026-01-14  
**Status**: 🟢 **ACTIVE**

---

## Overview

This guide explains how to use Azure Service Bus integration in the JARVIS Master Agent system.

---

## Initialization

### Basic Initialization

```python
from azure_service_bus_integration import (
    get_service_bus_client,
    get_key_vault_client
)

# Initialize Key Vault client
kv_client = get_key_vault_client()

# Initialize Service Bus client
sb_client = get_service_bus_client(
    namespace="jarvis-lumina-bus.servicebus.windows.net",
    key_vault_client=kv_client
)
```

---

## Publishing Messages

### Publish to Topic

```python
from azure_service_bus_integration import ServiceBusMessage, MessageType
import uuid
from datetime import datetime

message = ServiceBusMessage(
    message_id=str(uuid.uuid4()),
    message_type=MessageType.ESCALATION,
    timestamp=datetime.now(),
    source="my-service",
    destination="target-service",
    payload={
        "MessageType": "EscalationRequest",
        "Priority": "high",
        "Data": {...}
    }
)

success = sb_client.publish_to_topic(
    topic_name="jarvis.escalations",
    message=message
)
```

### Send to Queue

```python
message = ServiceBusMessage(
    message_id=str(uuid.uuid4()),
    message_type=MessageType.WORKFLOW,
    timestamp=datetime.now(),
    source="workflow-api",
    destination="workflow-execution-queue",
    payload={
        "MessageType": "WorkflowExecutionRequest",
        "WorkflowId": "workflow-uuid",
        "Parameters": {}
    }
)

success = sb_client.send_to_queue(
    queue_name="workflow-execution-queue",
    message=message
)
```

---

## Consuming Messages

### Subscribe to Topic

```python
def handle_message(message_body: Dict[str, Any]):
    """Handle received message"""
    payload = message_body.get("payload", {})
    print(f"Received: {payload}")

sb_client.subscribe_to_topic(
    topic_name="jarvis.workflows",
    subscription_name="workflow-processor",
    handler=handle_message,
    max_wait_time=5
)
```

### Receive from Queue

```python
def handle_queue_message(message_body: Dict[str, Any]):
    """Handle queue message"""
    payload = message_body.get("payload", {})
    print(f"Received: {payload}")

sb_client.receive_from_queue(
    queue_name="workflow-execution-queue",
    handler=handle_queue_message,
    max_wait_time=5
)
```

---

## Workflow Integration

### Using Workflow Helper Functions

```python
from workflow_service_bus_integration import (
    publish_workflow_created,
    publish_workflow_status_update,
    publish_workflow_completed,
    send_workflow_execution_request
)

# Publish workflow created
publish_workflow_created({
    "id": "workflow-uuid",
    "name": "My Workflow",
    "created_by": "user-uuid",
    "priority": 5
})

# Update workflow status
publish_workflow_status_update(
    workflow_id="workflow-uuid",
    status="running",
    progress=50,
    current_step="step-2"
)

# Publish workflow completed
publish_workflow_completed(
    workflow_id="workflow-uuid",
    status="completed",
    execution_time=123.45,
    result={"output": "success"}
)

# Send execution request
send_workflow_execution_request(
    workflow_id="workflow-uuid",
    parameters={"param1": "value1"},
    async_execution=True
)
```

---

## Error Handling

### Retry Logic

Service Bus integration includes automatic retry with exponential backoff:

```python
try:
    success = sb_client.publish_to_topic("jarvis.workflows", message)
    if not success:
        # Handle failure
        logger.error("Failed to publish message")
except Exception as e:
    # Handle exception
    logger.error(f"Error: {e}")
```

---

## Best Practices

1. **Always use Service Bus for async communication**
2. **Use topics for pub/sub, queues for point-to-point**
3. **Include correlation_id for request/response matching**
4. **Handle errors gracefully with fallback**
5. **Use message types consistently**
6. **Monitor dead-letter queues**

---

**Last Updated**: 2026-01-14  
**Next Review**: 2026-01-21  
**Status**: 🟢 **ACTIVE**
