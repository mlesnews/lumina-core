# Intelligent Routing + Golden Cross LLM Integration

## 🎯 System Overview

**Intelligent Routing** + **Golden Cross Convergence** = Optimal model selection with single active model alignment

### How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│                   USER REQUEST                              │
│  Task: code_generation, priority=5                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            INTELLIGENT ROUTER (SELECTION)                   │
│  • Evaluates all available models                           │
│  • Uses routing strategy (round-robin, adaptive, etc.)      │
│  • SELECTS optimal model: codellama:13b                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         GOLDEN CROSS CONVERGENCE (ACTIVATION)               │
│  • Checks if codellama:13b is already active                │
│  • If not: Deactivate current, Activate codellama:13b       │
│  • Maintains SINGLE active model state                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              SINGLE ACTIVE MODEL                            │
│  codellama:13b (ACTIVE)                                     │
│  • All inferences use this model                            │
│  • Batch processing uses this model                         │
│  • Parallel tasks use this model                            │
│  • Quantum inference alignment maintained                   │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Parallel Processing with Golden Cross

### How Parallel Processing Works

**Key Point**: Tasks run in parallel, but ALL use the SAME active model.

```python
# Example: 5 tasks in parallel
tasks = [task1, task2, task3, task4, task5]

# ALL tasks use same active model (golden cross maintained)
async def process_parallel():
    # Router selects: codellama:13b
    # Golden Cross activates: codellama:13b
    
    results = await asyncio.gather(
        process_task(task1),  # Uses codellama:13b
        process_task(task2),  # Uses codellama:13b  
        process_task(task3),  # Uses codellama:13b
        process_task(task4),  # Uses codellama:13b
        process_task(task5)   # Uses codellama:13b
    )
    # All 5 tasks processed by SINGLE model
```

### Batch Processing

```python
# Batch of 10 tasks
batch = [task1, task2, ..., task10]

# Router selects optimal model for batch
# Golden Cross activates that model
# ALL 10 tasks use SAME model
results = await golden_cross.batch_inference(batch, use_same_model=True)
```

## 🎛️ Routing Strategies

### 1. Round-Robin
```python
# Cycles through models
Task 1 → Model A (activated)
Task 2 → Model B (switched from A)
Task 3 → Model C (switched from B)
Task 4 → Model A (switched from C)
```

### 2. Adaptive (Recommended)
```python
# Learns and adapts
Task 1: code_generation → codellama:13b (activated)
Task 2: code_generation → codellama:13b (reused, no switch)
Task 3: reasoning → llama3.2:11b (switched)
Task 4: code_generation → codellama:13b (switched back)
```

### 3. Performance-Based
```python
# Always selects best performer
Task 1 → Best model (activated)
Task 2 → Same best model (reused)
Task 3 → Same best model (reused)
```

## 🔧 Usage Examples

### Basic Usage
```python
from peak_ai_orchestrator import PEAK_AI_Orchestrator

orchestrator = PEAK_AI_Orchestrator()

# Submit task - automatically uses golden cross
task_id = await orchestrator.submit_task(
    content="Generate Python function",
    task_type="code_generation",
    priority=5
)

# Task automatically:
# 1. Router selects: codellama:13b
# 2. Golden Cross activates: codellama:13b
# 3. Inference uses: codellama:13b (SINGLE active model)
```

### Parallel Processing
```python
# Submit batch - all use same model
batch_tasks = [
    {"content": "Task 1", "task_type": "code_generation"},
    {"content": "Task 2", "task_type": "code_generation"},
    {"content": "Task 3", "task_type": "code_generation"},
]

job_id = await orchestrator.submit_batch_job(batch_tasks, batch_mode="parallel")

# All tasks use SAME active model (golden cross maintained)
```

### Change Routing Strategy
```python
# Set routing strategy
orchestrator.set_routing_strategy("round_robin")
# OR
orchestrator.set_routing_strategy("adaptive")

# Router uses new strategy for SELECTION
# Golden Cross still maintains SINGLE active model
```

## 📊 Status Monitoring

### Check Status
```python
status = orchestrator.get_status()

# Shows:
# - Routing strategy
# - Active model (golden cross)
# - Model metrics
# - Convergence score
```

### CLI Status
```bash
python scripts/python/peak_ai_orchestrator.py status

# Output:
# Routing Strategy: adaptive
# ✨ GOLDEN CROSS CONVERGENCE:
#    Active Model: codellama:13b
#    State: active
#    Inference Count: 42
#    Convergence Score: 1.00
```

## ✅ Benefits

### 1. Intelligent Selection
- Router chooses optimal model based on strategy
- Considers performance, load, capabilities

### 2. Single Active Model
- Only one model loaded (memory efficient)
- Unified inference state (quantum alignment)
- Predictable behavior

### 3. Parallel Processing
- Tasks can run in parallel
- All use same model (alignment maintained)
- Efficient batch processing

### 4. Flexible Routing
- Multiple strategies available
- Easy to switch strategies
- Adaptive learning

## 🎯 Best Practices

### ✅ Do:
- Use adaptive routing for best results
- Let golden cross manage model switching
- Use batch processing for efficiency
- Monitor convergence status

### ❌ Don't:
- Manually switch models (let system handle it)
- Load multiple models simultaneously
- Mix different models in same batch

---

## ✨ Summary

**Intelligent Routing** selects the optimal model.  
**Golden Cross Convergence** ensures only ONE model is active.  
**Result**: Optimal selection with quantum inference alignment! 🎯✨
