# @DOIT @END2END @REPORT: Iron Legion Mixture of Experts (MoE) Configuration

**Date**: 2026-01-09
**Protocol**: @DOIT @BAU @TRIAGE @END2END @AI2AI @AGENT2AGENT @ALWAYS @REPORT
**Status**: ✅ **EXPERT ROUTING SYSTEM CONFIGURED**

---

## Executive Summary

Configured a **Mixture of Experts (MoE)** system for all 7 Iron Legion LLM models with intelligent routing based on task type, keywords, and expert specialization. The system automatically selects the best expert for each request.

## The 7 Iron Legion Experts

| Mark         | Expert Name      | Model              | Port | Status       | Specialization           |
| ------------ | ---------------- | ------------------ | ---- | ------------ | ------------------------ |
| **Mark I**   | Code Expert      | codellama:13b      | 3001 | ✅ Working    | Primary code generation  |
| **Mark II**  | General Purpose  | llama3.2:11b       | 3002 | ⚠️ Restarting | Secondary general tasks  |
| **Mark III** | Quick Response   | qwen2.5-coder:1.5b | 3003 | ⚠️ Restarting | Lightweight quick tasks  |
| **Mark IV**  | Balanced Expert  | llama3:8b          | 3004 | ✅ Working    | General purpose balanced |
| **Mark V**   | Reasoning Expert | mistral:7b         | 3005 | ✅ Working    | Logical reasoning        |
| **Mark VI**  | Complex Expert   | mixtral:8x7b       | 3006 | ⚠️ Restarting | High complexity tasks    |
| **Mark VII** | Fallback Expert  | gemma:2b           | 3007 | ⚠️ Restarting | Lightweight fallback     |

**Current Status**: 3/7 experts operational (42.9%)

## Expert Specializations

### Mark I - Code Expert (codellama:13b)
- **Expertise**: Code generation, debugging, refactoring, software architecture
- **Use Cases**:
  - Write Python/JavaScript/TypeScript code
  - Fix bugs and errors
  - Code review and optimization
  - Generate unit tests
  - Design software architecture
- **Keywords**: `code`, `function`, `class`, `import`, `def`, `bug`, `error`, `fix`, `refactor`, `test`, `algorithm`, `API`

### Mark II - General Purpose Expert (llama3.2:11b)
- **Expertise**: General conversation, question answering, content creation
- **Use Cases**:
  - Answer questions
  - Generate content
  - Summarize text
  - Translate languages
  - Creative writing
- **Keywords**: `what`, `how`, `why`, `explain`, `describe`, `tell me`, `summarize`, `translate`, `write`, `create`

### Mark III - Quick Response Expert (qwen2.5-coder:1.5b)
- **Expertise**: Quick responses, lightweight tasks, fast inference
- **Use Cases**:
  - Quick answers
  - Simple code snippets
  - Fast responses
  - Low-resource tasks
- **Keywords**: `quick`, `fast`, `simple`, `easy`, `basic`, `short`

### Mark IV - Balanced Expert (llama3:8b)
- **Expertise**: Balanced performance, versatile tasks, moderate complexity
- **Use Cases**:
  - General tasks
  - Balanced performance needs
  - Versatile applications
- **Keywords**: `general`, `help`, `assist`, `task`, `work`

### Mark V - Reasoning Expert (mistral:7b)
- **Expertise**: Logical reasoning, problem solving, analysis, decision making
- **Use Cases**:
  - Solve problems
  - Logical reasoning
  - Analysis
  - Decision making
  - Mathematical problems
- **Keywords**: `solve`, `reason`, `analyze`, `decide`, `think`, `logic`, `problem`, `why`, `because`, `therefore`

### Mark VI - Complex Expert (mixtral:8x7b)
- **Expertise**: High complexity, advanced reasoning, multi-step problems
- **Use Cases**:
  - Complex problems
  - Advanced reasoning
  - Multi-step analysis
  - Sophisticated tasks
- **Keywords**: `complex`, `advanced`, `sophisticated`, `deep`, `multi-step`, `comprehensive`, `detailed`, `thorough`

### Mark VII - Fallback Expert (gemma:2b)
- **Expertise**: Fallback, lightweight, basic tasks, resource efficient
- **Use Cases**:
  - Fallback when others unavailable
  - Basic tasks
  - Resource-efficient responses
- **Keywords**: `basic`, `simple`, `fallback`, `backup`

## Intelligent Routing System

### Routing Algorithm

The system uses a **multi-stage routing algorithm**:

1. **Rule-Based Matching**: Checks predefined rules for task types
2. **Keyword Matching**: Analyzes prompt for expert-specific keywords
3. **Fallback Chain**: Uses priority-ordered fallback if no match
4. **Health Check**: Only routes to healthy/available experts

### Routing Rules

```json
{
  "code-related keywords": "Mark I (Code Expert)",
  "complex/advanced keywords": "Mark VI (Complex Expert) → Mark I (fallback)",
  "reasoning keywords": "Mark V (Reasoning Expert)",
  "quick/simple keywords": "Mark III (Quick) → Mark VII (fallback)",
  "general purpose": "Mark IV (Balanced)",
  "default": "Mark II (General Purpose)"
}
```

### Fallback Chain

Priority order when primary expert unavailable:
1. Mark I (Code Expert)
2. Mark IV (Balanced)
3. Mark V (Reasoning)
4. Mark II (General Purpose)
5. Mark III (Quick)
6. Mark VII (Fallback)

## Configuration Files

### 1. Expert Configuration
**File**: `config/iron_legion_experts_config.json`
- Defines all 7 experts
- Specializations and keywords
- Routing rules and fallback chain

### 2. Expert Router
**File**: `scripts/python/iron_legion_expert_router.py`
- Python implementation of routing logic
- Health checking
- Request routing and response handling

### 3. Cursor IDE Models
**File**: `data/cursor_models/cursor_models_config.json`
- Added 3 working experts to Cursor IDE:
  - `kaiju-code` (Mark I)
  - `kaiju-balanced` (Mark IV)
  - `kaiju-reasoning` (Mark V)

## Usage

### Command Line Router

```bash
# Check expert status
python scripts/python/iron_legion_expert_router.py --status

# Route a request
python scripts/python/iron_legion_expert_router.py --prompt "Write a Python function"

# Test routing with sample prompts
python scripts/python/iron_legion_expert_router.py --test
```

### Python API

```python
from scripts.python.iron_legion_expert_router import IronLegionExpertRouter

router = IronLegionExpertRouter()

# Select expert
selection = router.select_expert("Write a Python function to sort a list")
print(f"Selected: {selection.expert_name}")
print(f"Confidence: {selection.confidence}")

# Route request
result = router.route_request("Write a Python function to sort a list")
if result["success"]:
    print(result["response"])
```

### Cursor IDE

Three expert models are now available in Cursor IDE:
- **KAIJU (Iron Legion) - Code Expert**: For code-related tasks
- **KAIJU (Iron Legion) - Balanced Expert**: For general tasks
- **KAIJU (Iron Legion) - Reasoning Expert**: For reasoning tasks

## Test Results

```
✅ Mark I (Code): "Write a Python function..." → Selected (0.90 confidence)
✅ Mark V (Reasoning): "Solve this math problem..." → Selected (0.80 confidence)
⚠️  Mark IV (Balanced): "Create complex neural network..." → Selected (0.20 confidence)
```

## Next Steps

1. ✅ **Expert Routing System**: Complete
2. ⏳ **Fix Restarting Containers**: Mark II, III, VI, VII need investigation
3. ⏳ **Improve Keyword Matching**: Refine keyword detection for better routing
4. ⏳ **Load Balancer Integration**: Integrate with Iron Legion load balancer
5. ⏳ **Monitoring**: Track expert usage and performance metrics

## Troubleshooting Restarting Containers

Containers that are restarting:
- **Mark II** (llama3.2:11b) - Port 3002
- **Mark III** (qwen2.5-coder:1.5b) - Port 3003
- **Mark VI** (mixtral:8x7b) - Port 3006
- **Mark VII** (gemma:2b) - Port 3007

**To investigate**:
```bash
ssh 10.17.17.11 "docker logs iron-legion-mark-ii-llama32-llamacpp --tail 50"
ssh 10.17.17.11 "docker logs iron-legion-mark-iii-qwen-llamacpp --tail 50"
ssh 10.17.17.11 "docker logs iron-legion-mark-vi-mixtral-llamacpp --tail 50"
ssh 10.17.17.11 "docker logs iron-legion-mark-vii-gemma-llamacpp --tail 50"
```

**Common issues**:
- Model files missing
- GPU memory insufficient
- Port conflicts
- Container health check failures

---

**Configuration Status**: ✅ **EXPERT ROUTING CONFIGURED**
**Working Experts**: 3/7 (42.9%)
**Router Status**: ✅ **OPERATIONAL**
**Last Updated**: 2026-01-09 04:00:00

**@REPORT COMPLETE** ✅
