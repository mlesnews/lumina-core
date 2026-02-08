# VA Chat Session Coordinator - @COOR @COLAB

## Overview

The VA Chat Coordinator assists and coordinates Virtual Assistant (VA) agents in chat sessions with JARVIS providing oversight and coordination.

## Features

- ✅ **VA Agent Registration**: Automatically registers IMVA, ACVA, and JARVIS VA
- ✅ **Chat Session Management**: Start and manage chat sessions between VAs
- ✅ **Message Distribution**: Distribute user messages to all participating agents
- ✅ **Agent Communication**: Agents can communicate with each other
- ✅ **JARVIS Assistance**: JARVIS provides coordination and assistance
- ✅ **Oversight Logging**: Complete audit trail of all interactions

## Usage

### Basic Chat Session

```python
from scripts.python.jarvis_va_chat_coordinator import VAChatCoordinator

coordinator = VAChatCoordinator()

# Start chat session
session = coordinator.coordinate_chat_session(
    chat_topic="System Performance Discussion",
    participant_agents=["imva", "acva", "jarvis_va"],
    user_message="How is the system performing?"
)
```

### Agent Responses

```python
# Agent provides response
coordinator.agent_response(
    session_id=session["session_id"],
    agent_id="imva",
    response="System performance is optimal.",
    data={"cpu": 45, "status": "healthy"}
)
```

### JARVIS Assistance

```python
# JARVIS assists agents
assistance = coordinator.assist_agents(
    session_id=session["session_id"],
    assistance_type="coordination"  # general, coordination, decision, technical
)
```

### Get Chat Log

```python
# Get full chat log
chat_log = coordinator.get_chat_log(session["session_id"])
for entry in chat_log:
    print(f"{entry['from']} → {entry['to']}: {entry['message']}")
```

### Complete Session

```python
# Complete chat session
coordinator.complete_chat_session(
    session_id=session["session_id"],
    summary="Discussion completed successfully",
    success=True
)
```

## Registered VA Agents

1. **IMVA (Iron Man VA)**
   - Capabilities: desktop_companion, combat, system_monitoring, voice_acting
   - Role: Subagent

2. **ACVA (Armoury Crate VA)**
   - Capabilities: system_control, lighting, hardware_management
   - Role: Subagent

3. **JARVIS VA**
   - Capabilities: orchestration, coordination, intelligence, decision_making
   - Role: Primary

## JARVIS Assistance Types

- **general**: General assistance and coordination
- **coordination**: Coordinate agent communication and task distribution
- **decision**: Provide decision-making assistance based on agent inputs
- **technical**: Provide technical guidance and expertise

## JARVIS Oversight

JARVIS monitors all chat sessions and provides:
- Communication logging
- Task completion tracking
- Assistance when needed
- Oversight reports

## Tags

`@COOR` `@COLAB` `@VA` `#COLLABORATION` `#AGENTS` `#CHAT` `@JARVIS` `@TEAM`
