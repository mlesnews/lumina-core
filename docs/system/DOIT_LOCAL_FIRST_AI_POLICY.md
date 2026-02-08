# @DOIT Local-First AI Policy

**Date:** 2026-01-14  
**Status:** ✅ **IMPLEMENTED**

---

## Policy Statement

**Use @local @ai @llm @agent resources over cloud AI providers, unless @bau #decisioning @r5 @matrix &| @lattice approves cloud usage.**

---

## Policy Details

### Default Behavior: Local-First

- **Primary:** @local @ai @llm @agent resources (ULTRON, KAIJU, IRON LEGION, R5)
- **Cloud:** Only used when explicitly approved by decisioning systems

### Approval Required for Cloud

Cloud AI providers (OpenAI, Anthropic, Google, etc.) require approval from:
- **@bau** - Business As Usual decisioning
- **#decisioning** - Universal Decision Tree
- **@r5** - R5 Living Context Matrix
- **@matrix** - Decision Matrix
- **@lattice** - Decision Lattice

**Any one of these systems can approve cloud usage.**

---

## Implementation

### Core System: `doit_local_first_ai_policy.py`

**Key Classes:**
- `DOITLocalFirstAIPolicy` - Policy enforcement system
- `AIDecisionRequest` - Request for AI provider decision
- `AIDecisionResult` - Result of decision

**Key Methods:**
- `decide_ai_provider()` - Main decision method
- `_get_cloud_approval()` - Get approval from decisioning systems
- `_get_r5_recommendation()` - Get @R5 @matrix recommendation
- `_get_matrix_recommendation()` - Get @matrix recommendation
- `_get_lattice_recommendation()` - Get @lattice recommendation

### Integration Points

1. **@DOIT Chain-of-Thought Enhanced**
   - Integrated into workflow step execution
   - Enforces policy when AI is needed
   - Logs decisions and approvals

2. **JARVIS @DOIT Executor**
   - Initializes policy system
   - Enforces policy during execution

3. **Local-First AI Router** (`enforce_local_first_ai_routing.py`)
   - Existing system enhanced with policy
   - Blocks cloud unless approved

---

## Decision Flow

```
Request AI Provider
    │
    ├─ Cloud Requested?
    │   │
    │   ├─ NO → Use Local (ULTRON/KAIJU/IRON_LEGION/R5)
    │   │
    │   └─ YES → Check Approval
    │       │
    │       ├─ @bau #decisioning → Approved?
    │       │   ├─ YES → Use Cloud
    │       │   └─ NO → Continue checking
    │       │
    │       ├─ @r5 @matrix → Approved?
    │       │   ├─ YES → Use Cloud
    │       │   └─ NO → Continue checking
    │       │
    │       ├─ @matrix → Approved?
    │       │   ├─ YES → Use Cloud
    │       │   └─ NO → Continue checking
    │       │
    │       └─ @lattice → Approved?
    │           ├─ YES → Use Cloud
    │           └─ NO → Use Local (default)
```

---

## Examples

### Example 1: Local Request (No Approval Needed)

```
Request: "Use AI to generate code"
Provider: None specified

Decision:
  ✅ Use Local (ULTRON)
  Reason: Local-first policy - no cloud requested
  Source: local_first_policy
```

### Example 2: Cloud Request (Not Approved)

```
Request: "Use GPT-4 to analyze data"
Provider: "gpt-4"

Decision:
  🚫 Cloud NOT approved
  ✅ Use Local (ULTRON) instead
  Reason: Cloud not approved by @bau #decisioning @r5 @matrix/@lattice
  Source: @bau #decisioning @r5 @matrix/@lattice
```

### Example 3: Cloud Request (Approved)

```
Request: "Use Claude for complex reasoning"
Provider: "claude-3-opus"

Decision:
  ✅ Cloud approved by @bau #decisioning
  ✅ Use Cloud (Anthropic)
  Reason: Approved by @bau #decisioning decision tree
  Source: @bau #decisioning
  Approval ID: decisioning_1234567890
```

---

## Benefits

1. **Cost Control** - Minimizes cloud API costs
2. **Privacy** - Keeps data local by default
3. **Performance** - Local models often faster
4. **Reliability** - Not dependent on external services
5. **Flexibility** - Cloud available when decisioning approves

---

## Files Created

1. `scripts/python/doit_local_first_ai_policy.py`
   - Core policy enforcement system
   - Decisioning integration
   - Local-first enforcement

2. `docs/system/DOIT_LOCAL_FIRST_AI_POLICY.md`
   - This documentation

---

## Files Modified

1. `scripts/python/doit_chain_of_thought_enhanced.py`
   - Added AI policy enforcement in step execution
   - Checks AI provider requests
   - Enforces local-first policy

2. `scripts/python/jarvis_doit_executor.py`
   - Added AI policy initialization
   - Policy enforcement during execution

---

## Usage

### Standalone

```python
from doit_local_first_ai_policy import DOITLocalFirstAIPolicy

policy = DOITLocalFirstAIPolicy(project_root)
result = policy.decide_ai_provider(
    task_description="Generate code",
    requested_provider="gpt-4"
)

# Result will enforce local-first unless approved
```

### Integrated with @DOIT

The policy is automatically enforced in:
- @DOIT Chain-of-Thought Enhanced workflows
- JARVIS @DOIT Executor
- All @DOIT operations

---

## Tags

**Tags:** #DOIT #LOCAL_FIRST #BAU #DECISIONING #R5 #MATRIX #LATTICE 
         #AI #LLM #AGENT @JARVIS @LUMINA @DOIT

---

**Status:** ✅ **IMPLEMENTED - POLICY ENFORCED**
