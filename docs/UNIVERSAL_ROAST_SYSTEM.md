# Universal Roast System - Flow State Enhancer

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

---

## Overview

Universal roasting system where **ALL agents** can perform roasts (critical analysis) and anti-roasts (constructive criticism). Character-specific roasting styles based on personality.

**Purpose**: Enhance workflow performance by providing multiple perspectives through character-specific roasts.

---

## Key Features

### 1. Universal Roasting

- ✅ **All agents can roast** - Not just MARVIN, but all agents
- ✅ **Character-specific styles** - Each agent has unique roasting style
- ✅ **Roast & Anti-Roast** - Both critical and constructive feedback
- ✅ **Flow state enhancement** - Identifies flow state blockers

### 2. Roast Types

- **ROAST** - Critical, negative analysis (MARVIN, K-2SO, Upper Management)
- **ANTI-ROAST** - Constructive criticism, wisdom-based (Gandalf)
- **BOTH** - Both roast and anti-roast (Jedi Council, JARVIS)

### 3. Character Personalities

#### MARVIN
- **Style**: Depressive, pessimistic
- **Type**: ROAST only
- **Quote**: "I have a brain the size of a planet, and they ask me to roast this."
- **Anti-Roast**: Not capable

#### Gandalf
- **Style**: Wisdom, constructive
- **Type**: ANTI-ROAST (can do both)
- **Quote**: "Fool of a Took! This is no time for carelessness."
- **Anti-Roast Quote**: "You must learn to think before you act."
- **Example**: Chews out Pippin for knocking bucket down well (constructive criticism)

#### Jedi Council
- **Style**: Strategic, wise
- **Type**: BOTH
- **Quote**: "The path forward requires careful consideration."
- **Anti-Roast**: Yes

#### JARVIS
- **Style**: Analytical, helpful
- **Type**: BOTH
- **Quote**: "Analysis complete. Several optimization opportunities identified."
- **Anti-Roast**: Yes

#### Upper Management
- **Style**: Executive, business-focused
- **Type**: ROAST (can do anti-roast)
- **Quote**: "This doesn't align with our strategic objectives."
- **Anti-Roast**: Yes

#### K-2SO
- **Style**: Sarcastic, direct
- **Type**: ROAST only
- **Quote**: "I'll be honest with you - this is terrible."
- **Anti-Roast**: Not capable

#### C-3PO
- **Style**: Protocol, polite
- **Type**: ROAST (can do anti-roast)
- **Quote**: "Oh my! This is most irregular."
- **Anti-Roast**: Yes

#### R2-D2
- **Style**: Technical, beep-based
- **Type**: ROAST (can do anti-roast)
- **Quote**: "*beep boop* (Translation: This needs technical review.)"
- **Anti-Roast**: Yes

---

## Usage

### Automatic Operation

The system automatically roasts all asks with multiple agents:

```python
from master_workflow_orchestrator import MasterWorkflowOrchestrator

orchestrator = MasterWorkflowOrchestrator()

# When user makes ask, multiple agents automatically roast:
# - MARVIN (depressive roast)
# - Gandalf (constructive anti-roast)
# - Jedi Council (strategic roast + anti-roast)
# - JARVIS (analytical roast + anti-roast)
# - Upper Management (executive roast)

ask_id = orchestrator.receive_user_ask(
    "Our workflows performance is being hampered by lack of flow state enhancers"
)
```

### Manual Operation

```python
from universal_roast_system import UniversalRoastSystem, RoastType

roaster = UniversalRoastSystem()

# MARVIN roasts (depressive)
marvin_roast = roaster.roast_ask(
    "marvin", "ask_id", "ask text",
    roast_type=RoastType.ROAST
)

# Gandalf anti-roasts (constructive)
gandalf_roast = roaster.roast_ask(
    "gandalf", "ask_id", "ask text",
    roast_type=RoastType.ANTI_ROAST
)

# Jedi Council does both
jedi_roast = roaster.roast_ask(
    "jedi_council", "ask_id", "ask text",
    roast_type=RoastType.BOTH
)
```

---

## Flow State Enhancement

### Flow State Issues Identified

The system identifies flow state blockers:

- **Performance issues** - Slow workflows
- **Blockers** - Stuck processes
- **Missing enhancers** - Lack of flow state tools
- **Bottlenecks** - Workflow bottlenecks

### Recommendations

- Implement flow state enhancers
- Remove blockers
- Optimize workflow performance
- Add flow state monitoring

---

## Roast Categories

1. **Gaps** - Missing implementations
2. **Bloat** - Duplicate/unused code
3. **Missing Integrations** - Missing connections
4. **Incomplete Workflows** - Broken workflows
5. **Unused Code** - Dead code
6. **Flow State Issues** - Performance blockers

---

## Examples

### MARVIN Roast

```
🔥 MARVIN (ROAST): 1 flow state issue(s). Severity: 5.0

I have a brain the size of a planet, and they ask me to roast this.

Found 1 issues: 0 gaps, 0 bloat, 1 flow state issues.
```

### Gandalf Anti-Roast

```
🔥 Gandalf (ANTI-ROAST): 1 flow state issue(s). Severity: 2.0

You must learn to think before you act.

Identified 1 opportunities for improvement. Consider these enhancements.
```

### Jedi Council Roast + Anti-Roast

```
🔥 Jedi Council (ROAST + ANTI-ROAST): 2 flow state issue(s). Severity: 7.0

The path forward requires careful consideration.

Found 2 issues: 0 gaps, 0 bloat, 2 flow state issues.
Identified 2 opportunities for improvement. Consider these enhancements.
```

---

## Integration

### Master Workflow Orchestrator

- Automatically roasts all asks with multiple agents
- Provides multiple perspectives
- Enhances flow state identification

### JARVIS Gap Closer

- Uses roasts to close gaps
- Reduces bloat
- Completes missing integrations

### Workflow System

- Feeds roasts into workflow loop
- Enhances workflow performance
- Identifies flow state blockers

---

## Configuration

### Agent Personalities

Configured in `universal_roast_system.py`:

```python
agent_configs = {
    "marvin": {
        "style": RoastStyle.DEPRESSIVE,
        "roast_type": RoastType.ROAST,
        "anti_roast_capable": False
    },
    "gandalf": {
        "style": RoastStyle.WISDOM,
        "roast_type": RoastType.ANTI_ROAST,
        "anti_roast_capable": True
    },
    # ... more agents
}
```

### Roast Types

- `RoastType.ROAST` - Critical analysis
- `RoastType.ANTI_ROAST` - Constructive criticism
- `RoastType.BOTH` - Both types

---

## Best Practices

1. **Use multiple agents** - Get different perspectives
2. **Balance roasts** - Use both critical and constructive feedback
3. **Flow state focus** - Identify and fix flow state blockers
4. **Character authenticity** - Maintain character personalities
5. **Action on roasts** - Use roasts to improve workflows

---

## Status

✅ **Universal Roast System** - Operational  
✅ **All Agents Can Roast** - Operational  
✅ **Gandalf Anti-Roast** - Operational  
✅ **Flow State Enhancement** - Operational  
✅ **Master Orchestrator Integration** - Operational  

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

