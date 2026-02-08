# JARVIS Governance & Evolution - Quick Reference

**Core Values: Adapt, Improvise, Overcome**

---

## 🚀 Quick Start

### Initialize Systems

```python
from jarvis_governance_system import JARVISGovernanceSystem
from jarvis_command_control_center import JARVISCommandControlCenter
from jarvis_evolution_maturation import JARVISEvolutionMaturation

# Initialize all systems
governance = JARVISGovernanceSystem()
command_control = JARVISCommandControlCenter()
evolution = JARVISEvolutionMaturation()
```

---

## 📋 Governance

### Propose Decision

```python
from jarvis_governance_system import GovernanceBranch, DecisionType, GovernanceScale

decision = governance.propose_decision(
    branch=GovernanceBranch.EXECUTIVE,
    decision_type=DecisionType.STRATEGIC,
    title="Operation Title",
    description="Description",
    scale=GovernanceScale.PLANETARY,
    proposer="JARVIS"
)
```

### Vote on Decision

```python
governance.vote_on_decision(decision.decision_id, "voter_id", "approve")
```

### Execute Decision

```python
result = governance.execute_decision(decision.decision_id, "executor")
```

---

## ⚡ Command & Control

### Create Operation

```python
operation = command_control.create_operation(
    name="Operation Name",
    scale="planetary",
    priority=8
)
```

### Declare Crisis

```python
crisis = command_control.declare_crisis(
    level="critical",
    description="Crisis description",
    affected_scale="global"
)
```

---

## 🧬 Evolution

### Record Interaction

```python
evolution.record_interaction(
    component_id="ai",
    interaction_type="decision_making",
    success=True
)
```

### Unlock Capability

```python
evolution.unlock_capability("ai", "enhanced_reasoning")
```

---

## 📊 Scales

- **Local**: Single system/user
- **Regional**: Multiple systems
- **Global**: Earth-wide
- **Planetary**: Multi-planetary
- **Solar System**: System-wide
- **Beyond**: Interstellar

---

## 🎯 Evolution Stages

- **Embryonic** (0.0-0.2)
- **Infant** (0.2-0.4)
- **Child** (0.4-0.6)
- **Adolescent** (0.6-0.8)
- **Adult** (0.8-0.95)
- **Mature** (0.95-1.0)
- **Transcendent** (>1.0)

---

## 🔗 Integration

- **Governance** ↔ **Command & Control** (Executive Branch)
- **Command & Control** ↔ **AIOS** (Orchestration)
- **Command & Control** ↔ **Voice Profile (@AIO)** (Voice filtering)
- **Evolution** ↔ **All Components** (Maturation)

---

**Tags:** #JARVIS #GOVERNANCE #QUICK_REFERENCE #EVOLUTION #ADAPT #IMPROVISE #OVERCOME
