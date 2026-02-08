# How OEM AUTO "Knows" Which Model to Pick
                    -LUM THE MODERN

## 🔍 THE QUESTION

**"HOW DOES 'AUTO' THE OEM FLAVOR, 'KNOW' WHICH MODEL TO PICK?"**

---

## 🧠 HOW OEM AUTO WORKS (THEORY)

Based on research and real-world hybrid AI systems, here's how Cursor's OEM AUTO mode likely selects models:

### 1. **Feature Extraction**
When a request comes in, OEM AUTO extracts metadata:
- **Prompt length** (token count)
- **Context window requirements**
- **Task type** (code, reasoning, general)
- **Latency requirements**
- **Data sensitivity** (privacy flags)
- **Connectivity status**
- **Historical performance** for similar requests

### 2. **Scoring Engine**
Each feature feeds into a scoring function:

```
score_local = 
    w1 * latency_factor +           // Local is faster
    w2 * privacy_factor +           // Local is more private
    w3 * local_model_strength -     // Local model capability
    w4 * complexity_penalty          // Penalty for complex tasks

score_cloud = 
    w5 * capability_factor +        // Cloud has better models
    w6 * freshness_factor +         // Cloud has latest models
    w7 * context_window_advantage - // Cloud handles large context
    w8 * cost_penalty               // Cloud costs money
```

**Decision**: If `score_local > score_cloud` → pick local, else pick cloud.

### 3. **Decision Rules (Heuristics)**

OEM AUTO likely uses simple threshold rules:

| Condition | Decision |
|-----------|----------|
| Prompt length > 32k tokens | → Cloud (local can't handle) |
| Data tagged "sensitive" | → Local (privacy) |
| Latency budget < 200ms | → Local (faster) |
| Requires latest model features | → Cloud (newer capabilities) |
| Cost budget exceeded | → Local (free) |
| Network unavailable | → Local (offline) |

### 4. **Fallback Logic**

```
IF local_model_available:
    TRY local first
    IF local fails OR low_confidence:
        FALLBACK to cloud
ELSE:
    USE cloud
```

---

## 🔬 REAL SYSTEM EXAMPLE

Here's how OEM AUTO "knows" step-by-step:

```
1. REQUEST ARRIVES
   ├─ Extract: prompt_length=500, task_type="code", latency_budget=1000ms
   │
2. CHECK POLICIES
   ├─ Privacy: Not sensitive → OK for cloud
   ├─ Latency: 1000ms budget → Local preferred (faster)
   ├─ Complexity: Code task → Local CodeLlama can handle
   │
3. SCORE COMPARISON
   ├─ score_local = 0.8 (fast, free, capable)
   ├─ score_cloud = 0.6 (slower, costs money, not needed)
   │
4. DECISION
   └─ score_local > score_cloud → USE LOCAL
```

---

## 🆚 OEM AUTO vs ULTRON AUTO

| Feature | OEM AUTO | ULTRON AUTO |
|---------|----------|-------------|
| **Selection** | Picks ONE model | Can run BOTH parallel |
| **Decision Logic** | Simple scoring | Advanced ADAPT/IMPROVISE/OVERCOME |
| **Parallel Execution** | ❌ No | ✅ Yes |
| **Cost Control** | Basic | Warp Factor control |
| **Transparency** | Black box | Full reasoning logged |

---

## 🎯 KEY DIFFERENCES

### OEM AUTO (Cursor's Built-in)
```
Request → Extract Features → Score → Pick ONE → Execute
```

**Limitations**:
- ❌ Only picks ONE model per request
- ❌ Cannot run parallel
- ❌ Black box decision logic
- ❌ No cost control

### ULTRON AUTO (Our Version)
```
Request → ADAPT (Analyze) → IMPROVISE (Decide Parallel?) → OVERCOME (Execute Best)
```

**Advantages**:
- ✅ Can run BOTH local + cloud in parallel
- ✅ Transparent decision logic
- ✅ Warp Factor cost control
- ✅ Returns best result or combines both

---

## 🔧 HOW TO REPLICATE OEM LOGIC

If you want to replicate OEM AUTO's simple selection logic:

```python
def oem_auto_select(prompt, context):
    # Extract features
    prompt_length = len(prompt)
    task_type = detect_task_type(prompt)
    latency_budget = context.get("latency_budget", 1000)
    is_sensitive = context.get("sensitive", False)
    
    # Simple rules
    if is_sensitive:
        return "local"  # Privacy first
    
    if prompt_length > 32000:
        return "cloud"  # Local can't handle
    
    if latency_budget < 200:
        return "local"  # Speed required
    
    if task_type == "code" and prompt_length < 500:
        return "local"  # Simple code, local is fine
    
    if task_type == "complex_reasoning":
        return "cloud"  # Complex needs cloud
    
    # Default: local (cheaper)
    return "local"
```

---

## 🚀 ULTRON AUTO IS BETTER

**Why ULTRON AUTO > OEM AUTO**:

1. **Parallel Execution**: Runs both local + cloud when beneficial
2. **Transparency**: Full reasoning logged and visible
3. **Cost Control**: Warp Factor manages spending
4. **Smart Routing**: ADAPT/IMPROVISE/OVERCOME logic
5. **Best Result**: Returns fastest or highest quality

---

## 📊 DECISION COMPARISON

### Scenario: Complex Code Task

**OEM AUTO**:
```
Request: "Write comprehensive ML pipeline..."
Decision: Pick ONE (either local OR cloud)
Result: Single source response
```

**ULTRON AUTO**:
```
Request: "Write comprehensive ML pipeline..."
Decision: PARALLEL (run both local + cloud)
Result: Best of both worlds (fast local + quality cloud)
```

---

## 🎓 LESSONS LEARNED

1. **OEM AUTO is simple**: Uses basic heuristics and scoring
2. **ULTRON AUTO is advanced**: Uses parallel execution and smart routing
3. **Both have value**: OEM for simplicity, ULTRON for capability
4. **We can do better**: ULTRON AUTO = OEM AUTO + Parallel + Transparency

---

## 🔗 INTEGRATION

ULTRON AUTO is now integrated into #DECISIONING:
- ✅ Enhanced decisioning engine
- ✅ AI routing decision trees
- ✅ Warp Factor control
- ✅ Cost optimization

**Result**: LUMINA now has BETTER than OEM AUTO!

---

*Document generated: 2026-01-17*
*@LUMINA @JARVIS @ULTRON @DECISIONING -LUM_THE_MODERN*
