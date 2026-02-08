# JARVIS Body Check with Triage
## Comprehensive Self-Assessment and Priority Determination

**Date**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0

---

## Overview

JARVIS performs a complete "body check" of all systems, components, and capabilities, identifying what needs the most work with triage-based prioritization (P0/P1/P2/P3).

---

## Quick Start

### Run Body Check

```bash
python scripts/python/jarvis_body_check_triage.py --check
```

### Get Priority Action Plan

```bash
python scripts/python/jarvis_body_check_triage.py --check --actions
```

### Get Top Priorities

```python
from jarvis_body_check_triage import JARVISBodyCheckTriage

body_check = JARVISBodyCheckTriage()
top_priorities = body_check.get_top_priorities(limit=10)

for action in top_priorities:
    print(f"{action['priority']}: {action['action']}")
```

---

## Triage Priority Levels

### P0 - CRITICAL (Do Immediately)
- **Timeline**: Immediate action required
- **Examples**: 
  - Voice conversation system not configured
  - IDE integration failing
  - Agent registry missing
  - Critical dependencies unavailable

### P1 - HIGH (Within 30 Days)
- **Timeline**: Urgent attention needed
- **Examples**:
  - Voice system degraded
  - IDE integration partially working
  - Missing key agents
  - JARVIS not running

### P2 - MEDIUM (Within 60-90 Days)
- **Timeline**: Plan and implement
- **Examples**:
  - Learning systems need more data
  - Feature-agent mappings incomplete
  - Integration systems degraded

### P3 - LOW (Ongoing)
- **Timeline**: Standard maintenance
- **Examples**:
  - Systems operational but could be optimized
  - Minor improvements needed
  - Standard security practices

---

## Components Checked

### 1. Voice Conversation System
- Async voice conversation
- Always-listening capability
- Azure Speech SDK configuration
- TTS system availability

### 2. Cursor IDE Integration
- Keyboard controller
- Command mappings
- Interaction learner
- Feature-agent mapper

### 3. MANUS Agent System
- Agent registry
- JARVIS full-time super agent
- Droid actor system
- Agent communication

### 4. Learning Systems
- Interaction learner
- Feature-agent mapper
- Pattern recognition
- Learning data accumulation

### 5. Communication Systems
- JARVIS communication bridge
- Inter-agent communication
- Message routing

### 6. Storage Systems
- Data directories
- File permissions
- Storage availability

### 7. Security Systems
- Azure Key Vault access
- Credential management
- Access control

### 8. Monitoring Systems
- Health monitoring
- Diagnostic systems
- Alerting

### 9. Workflow Systems
- Workflow engines
- n8n integration
- Task orchestration

### 10. Data Systems
- R5 system
- Data processing
- Analysis systems

### 11. Integration Systems
- ULTRON cluster
- LLM router
- External integrations

---

## Report Structure

### Overall Health Score
- **0.0 - 0.5**: Critical issues (P0)
- **0.5 - 0.7**: Degraded (P1)
- **0.7 - 0.9**: Good (P2)
- **0.9 - 1.0**: Excellent (P3)

### Component Status
- **HEALTHY**: Fully operational
- **DEGRADED**: Working but with issues
- **FAILING**: Critical problems
- **UNKNOWN**: Cannot determine status
- **NOT_INITIALIZED**: Not set up

### Priority Actions
Grouped by triage priority:
- **P0**: Critical - fix immediately
- **P1**: High - fix within 30 days
- **P2**: Medium - plan and implement
- **P3**: Low - ongoing maintenance

---

## Usage Examples

### Basic Check

```python
from jarvis_body_check_triage import JARVISBodyCheckTriage

body_check = JARVISBodyCheckTriage()
report = body_check.perform_body_check()

print(f"Overall Health: {report.overall_health_score:.1%}")
print(f"Failing Components: {report.failing_components}")
print(f"Summary: {report.summary}")
```

### Get Priority Actions

```python
action_plan = body_check.get_priority_action_plan()

for priority in ["P0", "P1", "P2", "P3"]:
    actions = action_plan.get(priority, [])
    if actions:
        print(f"\n{priority} Actions ({len(actions)}):")
        for action in actions[:5]:
            print(f"  • {action['action']}")
```

### Top Priorities

```python
top_priorities = body_check.get_top_priorities(limit=10)

print("Top 10 Priorities:")
for i, action in enumerate(top_priorities, 1):
    print(f"{i}. [{action['priority']}] {action['action']}")
    print(f"   Component: {action['component']}")
    print(f"   Health: {action['health_score']:.1%}")
```

---

## Report Output

### Console Output

```
🔍 Starting JARVIS body check...
   Assessing all systems, components, and capabilities
   Checking voice systems...
   Checking IDE integration...
   Checking agent systems...
   ...

✅ Body check complete
   Overall Health Score: 75.0%
   Priority Actions: P0=2, P1=3, P2=4, P3=5

======================================================================
🔍 JARVIS Body Check Report
======================================================================

Overall Health Score: 75.0%
Total Components: 11
  ✅ Healthy: 5
  ⚠️  Degraded: 4
  ❌ Failing: 2

Summary: Overall health: 75.0%. 2 critical component(s) failing (P0). 4 component(s) degraded. 5 component(s) healthy. Priority actions: 2 P0, 3 P1.

Priority Actions
======================================================================

P0 (2 components):
  • Voice Conversation System (failing)
    - Issue: Azure Speech SDK not configured - voice conversation unavailable
    - Configure Azure Speech SDK credentials in Key Vault
    - Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION environment variables

  • Cursor IDE Integration (failing)
    - Issue: Keyboard controller not available - pynput/pygetwindow missing
    - Install dependencies: pip install pynput pygetwindow
```

### JSON Report

Reports are saved to: `data/jarvis_body_checks/body_check_YYYYMMDD_HHMMSS.json`

```json
{
  "timestamp": "2025-01-24T12:00:00",
  "overall_health_score": 0.75,
  "total_components": 11,
  "healthy_components": 5,
  "degraded_components": 4,
  "failing_components": 2,
  "components": [...],
  "priority_actions": {
    "P0": [...],
    "P1": [...],
    "P2": [...],
    "P3": [...]
  },
  "summary": "..."
}
```

---

## Integration

### With Voice Commands

```python
# JARVIS can perform body check via voice
# "JARVIS, perform body check"
# "JARVIS, what needs the most work?"
# "JARVIS, show me priority actions"
```

### With IDE Integration

```python
# Can be triggered from Cursor IDE
# Command: "jarvis body check"
# Shows results in IDE output panel
```

### Scheduled Checks

```python
# Run body check periodically
import schedule

schedule.every().day.at("09:00").do(
    lambda: JARVISBodyCheckTriage().perform_body_check()
)
```

---

## Best Practices

1. **Run Regularly**: Perform body check daily or weekly
2. **Address P0 First**: Fix critical issues immediately
3. **Track Progress**: Compare reports over time
4. **Prioritize**: Focus on P0 and P1 before P2/P3
5. **Document Fixes**: Note what was fixed and when

---

## Troubleshooting

### "Module not found" errors
- Install missing dependencies
- Check Python path configuration
- Verify module imports

### "Component status unknown"
- Component may not be initialized
- Check component configuration
- Verify component dependencies

### "Health score inconsistent"
- Multiple issues may affect score
- Check all issues and recommendations
- Address root causes, not symptoms

---

## Related Documentation

- [JARVIS Full-Time Super Agent Guide](./JARVIS_REAL_TIME_CONVERSATION_GUIDE.md)
- [JARVIS-Cursor Keyboard Integration](./JARVIS_CURSOR_KEYBOARD_CONTROL_GUIDE.md)
- [IDE Interaction Learning System](./JARVIS_IDE_INTERACTION_LEARNING_SYSTEM.md)
- [SYPHON Health Monitoring](../scripts/python/syphon/health.py)

---

**Status**: ✅ **OPERATIONAL**

JARVIS can now perform comprehensive self-assessment and prioritize issues using triage system!
