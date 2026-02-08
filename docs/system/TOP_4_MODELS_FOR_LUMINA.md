# Top 4 Models for Lumina - Recommendations

## Overview

Based on your current setup and Lumina's requirements, here are the **top 4 models** that work best with Lumina, plus how **Auto Selection** works.

---

## 🏆 Top 4 Models for Lumina

### 1. **qwen2.5:72b** (ULTRON) ⭐ **PRIMARY RECOMMENDATION**

**Location**: Local laptop (`localhost:11434`)  
**Size**: 72B parameters  
**Context**: 32,768 tokens  
**Status**: ✅ Currently available and configured

**Why it's #1**:
- ✅ **Best code generation quality** - Excellent for complex code tasks
- ✅ **Large context window** - Can handle entire codebases
- ✅ **Fast local inference** - No cloud latency
- ✅ **Already configured** - ULTRON cluster is set up
- ✅ **Hybrid cluster** - Automatically uses KAIJU as backup

**Best for**:
- Complex code generation
- Large file refactoring
- Architecture decisions
- Multi-file operations
- Agent tasks requiring deep reasoning

**Use when**: Default choice for most tasks

---

### 2. **codellama:13b** (KAIJU Iron Legion - Mark I) ⭐ **CODE SPECIALIST**

**Location**: KAIJU NAS (`10.17.17.32:11434`)  
**Size**: 13B parameters  
**Context**: 8,192 tokens  
**Status**: ⚠️ Needs to be pulled on KAIJU

**Why it's #2**:
- ✅ **Code-optimized** - Specifically trained for code generation
- ✅ **Excellent for Python** - Great Python code quality
- ✅ **Balanced performance** - Good speed/quality ratio
- ✅ **Part of Iron Legion** - 7-model cluster available

**Best for**:
- Python code generation
- Code completion
- Bug fixes
- Code explanations
- Syntax-specific tasks

**Use when**: Working primarily with code, especially Python

---

### 3. **llama3.2:11b** (KAIJU Iron Legion - Mark II) ⭐ **GENERAL PURPOSE**

**Location**: KAIJU NAS (`10.17.17.32:11434`)  
**Size**: 11B parameters  
**Context**: 8,192 tokens  
**Status**: ✅ Currently available on KAIJU

**Why it's #3**:
- ✅ **General purpose** - Good for mixed tasks
- ✅ **Fast inference** - Quick responses
- ✅ **Balanced** - Good for both code and reasoning
- ✅ **Already available** - No setup needed

**Best for**:
- General coding tasks
- Documentation generation
- Code review
- Quick questions
- Mixed code/text tasks

**Use when**: Need balanced performance for general tasks

---

### 4. **qwen2.5-coder:1.5b-base** (KAIJU Iron Legion - Mark III) ⭐ **LIGHTWEIGHT SPEED**

**Location**: KAIJU NAS (`10.17.17.32:11434`)  
**Size**: 1.5B parameters  
**Context**: 4,096 tokens  
**Status**: ⚠️ Needs to be pulled on KAIJU

**Why it's #4**:
- ✅ **Ultra-fast** - Lightning quick responses
- ✅ **Code-focused** - Optimized for code tasks
- ✅ **Low resource** - Minimal RAM/CPU usage
- ✅ **Great for autocomplete** - Perfect for inline suggestions

**Best for**:
- Inline code completion
- Quick suggestions
- Simple code tasks
- When speed is critical
- Low-resource scenarios

**Use when**: Need instant responses for simple tasks

---

## 🤖 Auto Model Selection - How It Works

### What is "Auto" Selection?

**YES** - When you set model selection to "Auto", Lumina will **automatically pick the best model** for each situation based on:

1. **Task Complexity**
   - **Low complexity** → `qwen2.5-coder:1.5b-base` (fast, lightweight)
   - **Medium complexity** → `llama3.2:11b` (balanced)
   - **High complexity** → `qwen2.5:72b` or `codellama:13b` (powerful)

2. **Context Size**
   - **Small context** (< 4K tokens) → Lightweight models
   - **Medium context** (4K-8K tokens) → Balanced models
   - **Large context** (> 8K tokens) → `qwen2.5:72b` (32K context)

3. **Task Type**
   - **Code generation** → `codellama:13b` or `qwen2.5-coder:1.5b-base`
   - **Code review** → `llama3.2:11b` or `qwen2.5:72b`
   - **Documentation** → `llama3.2:11b`
   - **Architecture** → `qwen2.5:72b`
   - **Quick autocomplete** → `qwen2.5-coder:1.5b-base`

4. **Resource Availability**
   - **Local available** → Use ULTRON (`qwen2.5:72b`)
   - **KAIJU available** → Use KAIJU models
   - **Both available** → Load-balanced hybrid cluster

5. **Performance Requirements**
   - **Speed critical** → Lightweight models
   - **Quality critical** → Larger models
   - **Balanced** → Medium models

### Auto Selection Strategy

The system uses an **adaptive routing strategy**:

```
Task Request
    ↓
Analyze: Complexity + Context + Type + Resources
    ↓
Select Best Model
    ↓
Execute
    ↓
If fails → Escalate to larger model
    ↓
If succeeds → Cache result for similar tasks
```

### Current Auto Configuration

From `config/kilo_code_optimized_config.json`:

```json
{
  "model_selection": {
    "strategy": "adaptive",
    "criteria": {
      "complexity": {
        "low": "qwen2.5-coder:1.5b-base",
        "medium": "llama3.2:11b",
        "high": "codellama:13b"
      },
      "context_size": {
        "small": "qwen2.5-coder:1.5b-base",
        "medium": "llama3.2:11b",
        "large": "qwen2.5:72b"
      }
    }
  }
}
```

---

## 📊 Model Comparison Matrix

| Model | Size | Speed | Quality | Context | Best For |
|-------|------|-------|---------|---------|----------|
| **qwen2.5:72b** | 72B | ⭐⭐ | ⭐⭐⭐⭐⭐ | 32K | Complex tasks, large files |
| **codellama:13b** | 13B | ⭐⭐⭐ | ⭐⭐⭐⭐ | 8K | Code generation, Python |
| **llama3.2:11b** | 11B | ⭐⭐⭐ | ⭐⭐⭐⭐ | 8K | General purpose, balanced |
| **qwen2.5-coder:1.5b** | 1.5B | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 4K | Quick tasks, autocomplete |

---

## 🎯 Recommended Setup

### Option 1: Auto Selection (Recommended) ✅

**Best for**: Most users - Let Lumina choose automatically

**Configuration**:
- Set default model to **"ULTRON"** (which uses auto-routing)
- Enable adaptive model selection
- System will automatically pick the best model for each task

**Benefits**:
- ✅ Optimal performance for each task
- ✅ No manual selection needed
- ✅ Automatic fallback if model unavailable
- ✅ Load balancing across ULTRON + KAIJU

### Option 2: Manual Selection

**Best for**: Power users who want control

**Configuration**:
- Manually select model based on task
- Use **qwen2.5:72b** for complex tasks
- Use **codellama:13b** for code tasks
- Use **llama3.2:11b** for general tasks
- Use **qwen2.5-coder:1.5b** for quick tasks

---

## 🚀 Quick Setup Guide

### 1. Ensure Models Are Available

**ULTRON Local** (already configured):
```bash
# Verify qwen2.5:72b is available
curl http://localhost:11434/api/tags
```

**KAIJU** (check available models):
```bash
# Check what's available on KAIJU
curl http://10.17.17.32:11434/api/tags
```

### 2. Pull Missing Models (if needed)

**On KAIJU**:
```bash
# Pull recommended models
ollama pull codellama:13b
ollama pull llama3.2:11b
ollama pull qwen2.5-coder:1.5b-base
```

### 3. Enable Auto Selection

The configuration is already set up! Just:
1. Use **ULTRON** as your default model
2. The system will automatically route to the best model
3. ULTRON cluster handles load balancing

---

## 💡 Pro Tips

1. **Start with Auto** - Let the system learn your patterns
2. **Monitor performance** - Check which models work best for your tasks
3. **Adjust if needed** - Fine-tune based on your specific use cases
4. **Use ULTRON cluster** - It automatically uses both local and KAIJU

---

## 📝 Summary

**Top 4 Models**:
1. **qwen2.5:72b** (ULTRON) - Best overall, large context
2. **codellama:13b** (KAIJU) - Best for code generation
3. **llama3.2:11b** (KAIJU) - Best general purpose
4. **qwen2.5-coder:1.5b** (KAIJU) - Best for speed

**Auto Selection**: ✅ **YES** - When set to "Auto", Lumina automatically picks the best model for each situation based on complexity, context, task type, and available resources.

**Recommendation**: Use **ULTRON with Auto Selection** - It's already configured and will automatically use the best model for each task!

---

## Tags

@ULTRON @KAIJU @IRON_LEGION #MODEL_SELECTION #AUTO_ROUTING #LUMINA_CONFIG
