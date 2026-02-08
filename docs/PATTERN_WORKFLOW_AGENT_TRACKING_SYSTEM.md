# Pattern → Workflow → Agent Tracking System

**Date**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

---

## Overview

**Complete flow tracking system:**
1. ✅ Pattern discovery/update → Key-value pairs
2. ✅ Key-values → Workflow matching
3. ✅ Workflows → AI agents (one per workflow)
4. ✅ All agents in same sub-agent chat session
5. ✅ Full hook and trace tracking
6. ✅ Analytics, metrics, performance tracking
7. ✅ Flow rate per second improvement

---

## Key Principle

**When patterns are discovered or updated:**
- Create key-value pairs matching the pattern
- Map pattern to one or more workflows
- Each workflow gets its own AI agent
- All agents can be in the same sub-agent chat session
- Hook and trace track everything
- Maintain proper flow
- Evaluate for analytics/metrics
- Track performance over time
- Improve flow rate per second

---

## System Flow

```
Pattern Discovered/Updated
    ↓
Create Key-Value Pairs (matching pattern)
    ↓
Map Pattern → Workflows (one or more)
    ↓
Create AI Agent for Each Workflow
    ↓
All Agents in Same Sub-Agent Chat Session
    ↓
Hook & Trace Track Everything
    ↓
Analytics & Performance Metrics
    ↓
Improve Flow Rate Per Second
```

---

## Components

### 1. Pattern Discovery/Update

**When patterns are discovered or updated:**

```python
from pattern_workflow_agent_mapper import PatternWorkflowAgentMapper, PatternType

mapper = PatternWorkflowAgentMapper()

# Discover new pattern
mapper.discover_or_update_pattern(
    pattern_id="pattern_123",
    pattern_data={"name": "Test Pattern", "description": "..."},
    pattern_type=PatternType.NEW
)

# Update existing pattern
mapper.discover_or_update_pattern(
    pattern_id="pattern_123",
    pattern_data={"name": "Updated Pattern", "improvements": "..."},
    pattern_type=PatternType.UPDATED
)

# Improve pattern
mapper.discover_or_update_pattern(
    pattern_id="pattern_123",
    pattern_data={"name": "Improved Pattern", "optimizations": "..."},
    pattern_type=PatternType.IMPROVED
)
```

---

### 2. Key-Value Pairs

**Each pattern must have key-value pairs that match it:**

```python
# Add key-value pairs to pattern
mapper.add_pattern_key_value(
    pattern_id="pattern_123",
    key="workflow_type",
    value="automation",
    confidence=0.95
)

mapper.add_pattern_key_value(
    pattern_id="pattern_123",
    key="complexity",
    value="medium",
    confidence=0.85
)
```

**Purpose**: Key-value pairs ensure patterns can be matched to workflows.

---

### 3. Pattern → Workflow Mapping

**Map patterns to workflows (one pattern can match multiple workflows):**

```python
# Map pattern to workflow
mapper.map_pattern_to_workflow(
    pattern_id="pattern_123",
    workflow_id="workflow_456",
    workflow_name="Automation Workflow",
    confidence=0.9
)

# Pattern can match multiple workflows
mapper.map_pattern_to_workflow(
    pattern_id="pattern_123",
    workflow_id="workflow_789",
    workflow_name="Another Workflow",
    confidence=0.8
)
```

---

### 4. Workflow → Agent Creation

**Each workflow gets its own AI agent:**

```python
# Create agent for workflow
agent = mapper.create_agent_for_workflow(
    workflow_id="workflow_456",
    workflow_name="Automation Workflow",
    agent_name="Automation Agent"
)

# All agents can be in same chat session
agent2 = mapper.create_agent_for_workflow(
    workflow_id="workflow_789",
    workflow_name="Another Workflow",
    agent_name="Another Agent",
    chat_session_id=agent.chat_session_id  # Reuse same chat session
)
```

**Key Features**:
- Each workflow gets its own agent
- All agents can share the same sub-agent chat session
- Agents are tracked individually

---

### 5. Hook & Trace Tracking

**Everything is traced for flow tracking:**

```python
# Automatic tracing happens for:
# - Pattern discovery/update
# - Key-value addition
# - Workflow mapping
# - Agent creation
# - Agent start
# - Agent completion
# - Performance metrics

# Get traces
traces = mapper.flow_traces
for trace in traces:
    print(f"{trace.event_type}: {trace.timestamp}")
    print(f"  Flow Rate: {trace.flow_rate} per second")
```

**Trace Events**:
- `pattern_discovered` - New pattern found
- `pattern_updated` - Pattern updated
- `pattern_key_value_added` - Key-value added
- `pattern_workflow_mapped` - Pattern mapped to workflow
- `agent_created` - Agent created
- `agent_started` - Agent started
- `agent_completed` - Agent completed
- `agent_failed` - Agent failed
- `pattern_to_agents_complete` - Complete flow finished

---

### 6. Analytics & Performance Metrics

**Track performance over time:**

```python
# Get performance analytics
analytics = mapper.get_performance_analytics(
    pattern_id="pattern_123",
    workflow_id="workflow_456",
    time_range_hours=24
)

print(f"Current Flow Rate: {analytics['current_flow_rate_per_second']} per second")
print(f"Average Flow Rate: {analytics['average_flow_rate_per_second']} per second")
print(f"Peak Flow Rate: {analytics['peak_flow_rate_per_second']} per second")
print(f"Success Rate: {analytics['success_rate']}")
```

**Metrics Tracked**:
- Flow rate per second (current, average, peak)
- Total flow time
- Agent count
- Workflow count
- Pattern count
- Success rate
- Performance over time

---

### 7. Flow Rate Per Second Improvement

**System automatically tracks and improves flow rate:**

```python
# Get current flow rate
flow_rate = mapper.get_flow_rate_per_second()
print(f"Current Flow Rate: {flow_rate} per second")

# Flow rate is calculated from:
# - Number of traces in last 60 seconds
# - Agent completion times
# - Workflow execution times
# - Pattern processing times

# System automatically:
# - Tracks flow rate history
# - Identifies bottlenecks
# - Suggests improvements
# - Optimizes agent allocation
```

---

## Complete Flow Example

```python
from pattern_workflow_agent_mapper import PatternWorkflowAgentMapper, PatternType

mapper = PatternWorkflowAgentMapper()

# Complete flow: Pattern → Key-Values → Workflows → Agents
result = mapper.process_pattern_to_agents(
    pattern_id="pattern_automation_123",
    pattern_data={
        "name": "Automation Pattern",
        "description": "Pattern for automation workflows",
        "category": "automation"
    },
    pattern_type=PatternType.NEW,
    key_values=[
        ("workflow_type", "automation"),
        ("complexity", "medium"),
        ("priority", "high"),
        ("confidence", 0.95)
    ]
)

# Result contains:
# - Pattern ID
# - Workflows mapped
# - Agents created
# - Chat session ID (all agents in same session)
# - Flow rate

print(f"Pattern: {result['pattern_id']}")
print(f"Workflows: {len(result['workflows'])}")
print(f"Agents: {len(result['agents'])}")
print(f"Chat Session: {result['chat_session_id']}")
print(f"Flow Rate: {result['flow_rate']} per second")

# Start agents
for agent_data in result['agents']:
    mapper.start_agent(agent_data['agent_id'])

# Complete agents
for agent_data in result['agents']:
    mapper.complete_agent(agent_data['agent_id'], success=True)

# Get analytics
analytics = mapper.get_performance_analytics()
print(f"Improved Flow Rate: {analytics['current_flow_rate_per_second']} per second")
```

---

## Integration with WOPR

**Automatically integrated with WOPR Workflow Pattern Mapper:**

When WOPR maps workflows to patterns:
1. ✅ Pattern automatically discovered/updated
2. ✅ Key-values automatically created
3. ✅ Workflows automatically mapped
4. ✅ Agents automatically created
5. ✅ Everything automatically tracked

**No manual intervention needed** - happens automatically during WOPR processing.

---

## Data Storage

**Files:**
- `data/pattern_workflow_agent/patterns.json` - All patterns
- `data/pattern_workflow_agent/pattern_key_values.json` - Pattern key-values
- `data/pattern_workflow_agent/workflow_mappings.json` - Pattern→Workflow mappings
- `data/pattern_workflow_agent/agents.json` - All agents
- `data/pattern_workflow_agent/traces.jsonl` - Flow traces (append-only)
- `data/pattern_workflow_agent/analytics/metrics_YYYYMMDD.json` - Daily metrics

---

## Flow Rate Improvement

**System tracks and improves flow rate:**

1. **Track Current Flow Rate**
   - Calculated from traces in last 60 seconds
   - Updated in real-time
   - Stored in history

2. **Identify Bottlenecks**
   - Slow agents
   - Slow workflows
   - Pattern processing delays

3. **Optimize**
   - Agent allocation
   - Workflow execution
   - Pattern matching

4. **Improve Over Time**
   - Historical analysis
   - Trend identification
   - Performance optimization

---

## Best Practices

1. **Always create key-values for patterns** - Ensures proper matching
2. **Map patterns to workflows** - Links patterns to execution
3. **Create agents for each workflow** - Individual tracking
4. **Use same chat session for related agents** - Better coordination
5. **Track everything** - Full observability
6. **Monitor flow rate** - Continuous improvement
7. **Analyze performance** - Identify improvements

---

## Files Created

- ✅ `scripts/python/pattern_workflow_agent_mapper.py` - Core mapper
- ✅ `docs/PATTERN_WORKFLOW_AGENT_TRACKING_SYSTEM.md` - This documentation

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

