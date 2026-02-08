# Agent Collaboration System - @COLAB with JARVIS Oversight

## Overview

The Agent Collaboration System enables agents and subagents to collaborate on tasks with JARVIS providing oversight and coordination.

## Features

- ✅ **Agent Registration**: Register agents and subagents with capabilities
- ✅ **Collaboration Sessions**: Start collaboration sessions with multiple agents
- ✅ **Agent Communication**: Agents can communicate with each other
- ✅ **JARVIS Oversight**: JARVIS monitors and supervises all collaborations
- ✅ **Task Completion**: Track task completion and results
- ✅ **Oversight Logging**: Complete audit trail of JARVIS oversight

## Usage

### Register Agents

```python
from src.cfservices.services.jarvis_core.agent_collaboration import (
    AgentCollaborationSystem,
    AgentRole
)

colab = AgentCollaborationSystem()

# Register agents/subagents
colab.register_agent(
    agent_id="r2d2",
    name="R2-D2",
    role=AgentRole.SUBAGENT,
    capabilities=["technical_operations", "diagnostics"]
)
```

### Start Collaboration

```python
# Start collaboration session with JARVIS oversight
session = colab.start_collaboration(
    task_description="Analyze system performance",
    agent_ids=["r2d2", "c3po", "k2so"],
    jarvis_oversight=True,
    oversight_level="standard"
)
```

### Agent Communication

```python
# Agents communicate with each other
colab.agent_communicate(
    session_id=session.session_id,
    from_agent_id="c3po",
    to_agent_id="r2d2",
    message="Please analyze CPU utilization",
    data={"metric": "cpu_utilization"}
)
```

### Complete Collaboration

```python
# Complete collaboration session
colab.complete_collaboration(
    session_id=session.session_id,
    final_result={"status": "success", "recommendations": [...]},
    success=True
)
```

## JARVIS Oversight

JARVIS provides oversight at three levels:

1. **Standard**: Monitors communication and task completion
2. **Strict**: Detailed monitoring with intervention capability
3. **Minimal**: Basic logging only

## Tags

`@COLAB` `#COLLABORATION` `#AGENTS` `#SUBAGENTS` `@JARVIS` `@TEAM`
