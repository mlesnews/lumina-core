# AIQ Escalation & Decision Tree System - Syphon Documentation

**Date**: 2025-12-31  
**Status**: ✅ ACTIVE  
**Purpose**: Smart escalation/decision-tree with AI Quorum, troubleshooting matrices, and Jedi Council integration

---

## Overview

Our system uses **intelligent escalation lattices and decision matrices** that leverage:

1. **AIQ (AI Quorum)** - Multi-agent consensus for critical decisions
2. **Universal Decision Trees** - Reusable decision logic across all systems
3. **Troubleshooting Matrices** - Systematic problem-solving frameworks
4. **Jedi Council** - Upper management approval board (#jedi-council #jedi-high-council)
5. **WOPR Integration** - Strategic planning and operational execution

**ULTRON is beneficent** - Our two-node cluster operates with benevolent intent, always prioritizing human benefit.

---

## Architecture

### Decision-Making Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│              Human Request / System Event                    │
└─────────────────────────────────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │  Universal Decision Tree      │
        │  (First-Level Decision)       │
        └───────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Simple Task  │ │ Complex Task │ │ Critical     │
│ (Auto)       │ │ (AIQ)        │ │ (Jedi)       │
└──────────────┘ └──────────────┘ └──────────────┘
                        │               │
                        ▼               ▼
                ┌──────────────┐ ┌──────────────┐
                │ AI Quorum    │ │ Jedi Council  │
                │ (Consensus)  │ │ (Approval)   │
                └──────────────┘ └──────────────┘
                        │               │
                        ▼               ▼
                ┌───────────────────────────┐
                │   Troubleshooting Matrix │
                │   (Systematic Resolution) │
                └───────────────────────────┘
                        │
                        ▼
                ┌───────────────────────────┐
                │   WOPR Integration        │
                │   (Strategic Execution)   │
                └───────────────────────────┘
```

---

## Components

### 1. Universal Decision Tree

**Location**: `scripts/python/universal_decision_tree.py`

**Purpose**: First-level decision making for all system operations

**Decision Trees Available**:
- `ai_fallback` - AI model selection (local → GROK → cloud)
- `cache_tier_selection` - Cache tier selection (L1 → L2 → L3)
- `nas_connection` - NAS connection strategy
- `error_handling` - Error handling and escalation

**Usage**:
```python
from universal_decision_tree import decide, DecisionContext, DecisionOutcome

context = DecisionContext(
    complexity="high",
    urgency="medium",
    local_ai_available=True,
    local_ai_quality=0.8
)

result = decide('ai_fallback', context)
# Returns: DecisionResult with outcome, reasoning, confidence
```

### 2. AI Quorum (AIQ)

**Purpose**: Multi-agent consensus for complex decisions

**How It Works**:
1. Question/problem presented to multiple AI agents
2. Each agent provides analysis and recommendation
3. System aggregates responses
4. Consensus reached through voting/weighting
5. Decision made based on quorum

**Agents in Quorum**:
- **JARVIS**: Optimizer, corrects/confirms
- **MARVIN**: Reality checker, proves wrong/confirms
- **TONY**: Executor, implementation perspective
- **MACE**: Coordinator, integration perspective
- **GANDALF**: Advisor, strategic perspective

**Quorum Rules**:
- **Simple Majority**: 3/5 agents agree → proceed
- **Unanimous**: 5/5 agents agree → high confidence
- **Split Decision**: Escalate to Jedi Council

### 3. Troubleshooting Matrices

**Purpose**: Systematic problem-solving frameworks

**Matrix Structure**:
```
Problem Category → Symptom → Root Cause → Solution → Verification
```

**Example Matrix**:
```
Iron Legion Invalid Model Error
├─ Symptom: "Invalid model" error
├─ Possible Causes:
│   ├─ Wrong endpoint (checking laptop instead of KAIJU)
│   ├─ Model not available on endpoint
│   ├─ Network connectivity issue
│   └─ Configuration mismatch
├─ Solutions:
│   ├─ Verify endpoint (prioritize KAIJU endpoints)
│   ├─ Check model availability
│   ├─ Test network connectivity
│   └─ Validate configuration
└─ Verification: Run validator script
```

**Integration**: Troubleshooting matrices are embedded in decision trees and escalate automatically.

### 4. Jedi Council (#jedi-council #jedi-high-council)

**Location**: `scripts/python/jedi_council.py`

**Purpose**: Upper management approval board for critical decisions

**Council Members**:
- **@MARVIN**: Reality Checker - Proves wrong/confirms
- **@JARVIS**: Optimizer - Corrects/confirms
- **Deep Thought (Matrix)**: Primary Reality - Single Answer
- **Deep Thought Two (Animatrix)**: Multiple Perspectives - Multiple Truths
- **Infinite Feedback Loop**: Continuous Refinement
- **Cloud AI Evaluation**: Production Readiness Assessment

**Approval Process**:
1. Request submitted to Jedi Council
2. Each member analyzes independently
3. Members vote: APPROVED, REJECTED, CONDITIONAL
4. Unanimous approval required for critical operations
5. Conditional approval requires addressing concerns

**Escalation Triggers**:
- High-risk operations
- Production deployments
- Cost-sensitive decisions (>$X threshold)
- Security-critical changes
- System architecture changes

### 5. WOPR Integration

**Purpose**: Strategic planning and operational execution

**WOPR Responsibilities**:
- Strategic planning
- Operational execution
- Threat response coordination
- Defense architecture deployment

**Integration Points**:
- Decision trees can escalate to WOPR for strategic planning
- Troubleshooting matrices feed into WOPR operational plans
- Jedi Council approvals trigger WOPR execution

---

## Escalation Flow

### Standard Escalation Path

```
1. Universal Decision Tree
   │
   ├─► Simple → Auto-execute
   │
   ├─► Complex → AI Quorum
   │   │
   │   ├─► Consensus → Execute
   │   │
   │   └─► No Consensus → Jedi Council
   │
   └─► Critical → Jedi Council
       │
       ├─► Approved → WOPR Execution
       │
       └─► Rejected → Address Concerns → Resubmit
```

### Troubleshooting Escalation

```
1. Problem Detected
   │
   ├─► Troubleshooting Matrix Lookup
   │
   ├─► Apply Standard Solutions
   │
   ├─► If Unresolved → AI Quorum Analysis
   │
   ├─► If Still Unresolved → Jedi Council Review
   │
   └─► Final Solution → WOPR Implementation
```

---

## ULTRON Integration

**ULTRON is beneficent** - Our two-node cluster integrates with decision trees:

### Model Selection Decision Tree

```
Request for AI Model
    │
    ├─► Check ULTRON Cluster Status
    │   │
    │   ├─► Primary (KAIJU) Available?
    │   │   ├─► Yes → Select best model from KAIJU (7 models)
    │   │   │   └─► Use decision tree for model selection:
    │   │   │       • Code generation → codellama:13b
    │   │   │       • General → llama3.2:11b
    │   │   │       • Quick → qwen2.5-coder:1.5b
    │   │   │       • Complex → mixtral-8x7b
    │   │   │
    │   │   └─► No → Auto-Failover to Fallback
    │   │
    │   └─► Fallback (Laptop) Available?
    │       └─► Yes → Use qwen2.5:72b
    │
    └─► If Both Down → Escalate to AI Quorum
        └─► Consider cloud fallback (with approval)
```

---

## Real-Time Human-AI Conversations

### JARVIS Full-Time Super Agent

**Location**: `scripts/python/jarvis_fulltime_super_agent.py`

**Status**: ✅ **ACTIVE** - Always listening, always ready

**Features**:
- Direct voice conversations (no IDE clicking)
- Multi-agent discussions
- Real-time responses
- Full project context awareness

### Starting a Conversation

#### Option 1: Voice Conversation
```bash
python scripts/python/jarvis_fulltime_super_agent.py --start-voice
```

#### Option 2: Text Conversation
```python
from jarvis_fulltime_super_agent import get_jarvis_fulltime

jarvis = get_jarvis_fulltime()
conv_id = jarvis.start_voice_conversation()
jarvis.speak(conv_id, "Hello JARVIS, what's the status?")
```

#### Option 3: Multi-Agent Discussion
```bash
python scripts/python/jarvis_fulltime_super_agent.py --multi-agent "How should we optimize ULTRON cluster?"
```

### Current Status

**JARVIS Full-Time Super Agent**:
- ✅ Running: True
- ✅ Voice Interface: Active
- ✅ Voice Listening: Active
- ✅ Total Agents: 5 (JARVIS, MARVIN, TONY, MACE, GANDALF)
- ✅ Active Agents: 5
- ✅ Always Available: Yes

---

## Decision Tree Examples

### Example 1: AI Model Selection

```python
from universal_decision_tree import decide, DecisionContext

context = DecisionContext(
    complexity="high",
    urgency="medium",
    local_ai_available=True,
    local_ai_quality=0.9,
    cost_sensitive=True
)

result = decide('ai_fallback', context)

# Result might be:
# - USE_LOCAL (if quality sufficient)
# - USE_GROK (if local quality low)
# - ESCALATE (if critical and uncertain)
```

### Example 2: Troubleshooting Matrix

```
Problem: Iron Legion Invalid Model Error
    │
    ├─► Check: Endpoint Configuration
    │   └─► Fix: Prioritize KAIJU endpoints
    │
    ├─► Check: Model Availability
    │   └─► Fix: Run validator script
    │
    └─► If Unresolved → AI Quorum Analysis
        └─► Escalate to Jedi Council if needed
```

---

## Integration with ULTRON

### ULTRON Decision Integration

ULTRON cluster uses decision trees for:
1. **Node Selection**: Primary vs Fallback
2. **Model Selection**: Which model on which node
3. **Failover Decisions**: When to failover
4. **Recovery Decisions**: When to switch back

**Example**:
```python
# ULTRON uses decision tree for model selection
from intelligent_llm_router import IntelligentLLMRouter

router = IntelligentLLMRouter()
router.configure_ultron_cluster()

# Router uses decision tree internally:
# - Check node health (decision tree)
# - Select model based on task (decision tree)
# - Handle failover (decision tree)
```

---

## Benefits

1. **Intelligent Escalation**: Automatic escalation based on complexity/risk
2. **Multi-Agent Consensus**: AI Quorum ensures well-considered decisions
3. **Systematic Troubleshooting**: Matrices provide structured problem-solving
4. **Approval Governance**: Jedi Council ensures critical decisions are reviewed
5. **Strategic Execution**: WOPR handles operational planning
6. **Real-Time Conversations**: Direct access to JARVIS without IDE barriers

---

## Usage Examples

### Start Real-Time Conversation

```bash
# Start voice conversation
python scripts/python/jarvis_fulltime_super_agent.py --start-voice

# Check status
python scripts/python/jarvis_fulltime_super_agent.py --status

# Multi-agent discussion
python scripts/python/jarvis_fulltime_super_agent.py --multi-agent "How do we optimize ULTRON?"
```

### Use Decision Tree

```python
from universal_decision_tree import decide, DecisionContext

# Make decision
result = decide('ai_fallback', DecisionContext(
    complexity="high",
    local_ai_available=True
))

print(f"Decision: {result.outcome}")
print(f"Reasoning: {result.reasoning}")
print(f"Confidence: {result.confidence}")
```

### Escalate to Jedi Council

```python
from jedi_council import JediCouncil

council = JediCouncil()
request = council.submit_request(
    description="Deploy new ULTRON configuration",
    urgency="high",
    risk_level="medium"
)

approval = council.get_approval(request.request_id)
print(f"Status: {approval.status}")
```

---

## Related Documentation

- `docs/system/ULTRON_AUTO_AGENT_SELECTION_SYPHON.md` - ULTRON cluster details
- `scripts/python/universal_decision_tree.py` - Decision tree implementation
- `scripts/python/jedi_council.py` - Jedi Council implementation
- `scripts/python/jarvis_fulltime_super_agent.py` - Full-time assistant
- `scripts/python/wopr_*.py` - WOPR integration files

---

**@SYPHON**: This document extracts the escalation/decision-tree system with AI Quorum, troubleshooting matrices, and Jedi Council integration.

**Note**: ULTRON is beneficent - all decisions prioritize human benefit and system reliability.
