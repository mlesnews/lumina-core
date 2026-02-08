# JARVIS Courage Evaluation System

**Date:** 2026-01-17  
**Status:** ✅ **ACTIVE**  
**Tags:** `#DECISIONING_SYSTEM` `#JARVIS` `#COURAGE` `#DEBRIEF` `#EVALUATION`

---

## 🎯 Purpose

The JARVIS Courage Evaluation System evaluates everything in @lumina with **courage** in contextual problems. It allows JARVIS to ask questions during debrief/summary, recognizing that questions are for **clarification**, not hesitation.

---

## 🛡️ Key Principles

### 1. Slash Commands = Directives

**Slash commands ("/command") are directives that say "HERE DO THIS!"**

- `/command` format = Direct execution instruction
- `@doit` / `@DOIT` = Full power of @manus/@magneto
- Explicit directives = Clear "do this" instructions
- Implied directives = Context suggests action needed

**JARVIS recognizes these as directives and executes with courage.**

### 2. Courage = Proactive Decision-Making

**Courage is NOT recklessness. Courage is:**

- ✅ **Proactive**: Making decisions when context is clear
- ✅ **Bold**: Taking action on high-risk problems when appropriate
- ✅ **Balanced**: Asking questions for clarification, not hesitation
- ❌ **NOT Excessive Caution**: Avoiding decisions due to uncertainty
- ❌ **NOT Reckless**: Ignoring risks entirely

### 3. Questions During Debrief = Clarification

**Questions are for clarification, not hesitation:**

- ✅ **Clarification**: "Should we use llama3.2:latest or llama3.2:11b?"
- ✅ **Risk Assessment**: "Are there edge cases for high-risk scenarios?"
- ✅ **Optimization**: "Could we have been more decisive?"
- ❌ **NOT Hesitation**: "I'm not sure if I should do this..."

### 4. Contextual Problems = Real-World Judgment

**Contextual problems require real-world judgment:**

- Model deployment uncertainty
- File location uncertainty
- Risk assessment in ambiguous scenarios
- Decision-making with incomplete information

---

## 🔍 Evaluation Process

### 1. Identify Contextual Problems

The system identifies contextual problems in @lumina:

```python
problems = [
    ContextualProblem(
        problem_id="model_deployment_uncertainty",
        context="Iron Legion model deployment - model name format unclear",
        question="Should we use llama3.2:latest or llama3.2:11b?",
        requires_courage=True,
        risk_level="medium",
        directive_type=DirectiveType.DOIT_COMMAND
    )
]
```

### 2. Generate Debrief Questions

Questions are generated based on problems:

```python
questions = [
    DebriefQuestion(
        question_id="q_model_deployment_uncertainty",
        question="Should we use llama3.2:latest or llama3.2:11b?",
        context="Iron Legion model deployment",
        priority="high",
        category="clarification"
    )
]
```

### 3. Evaluate Courage Level

Courage level is evaluated based on:
- Decision-making ratio
- High-risk problem handling
- Question appropriateness
- Action taken vs. hesitation

**Courage Levels:**
- **EXCESSIVE_CAUTION**: Too hesitant, asks too many questions
- **BALANCED**: Appropriate questions, decisive action
- **COURAGEOUS**: Bold decisions with appropriate risk assessment
- **RECKLESS**: Too bold, insufficient consideration

### 4. Generate Recommendations

Recommendations are generated based on evaluation:
- Increase decisiveness if excessive caution
- Add risk assessment if reckless
- Review high-risk problems
- Address unanswered questions

---

## 📋 Usage

### Basic Evaluation

```bash
python scripts/python/jarvis_courage_evaluation_system.py --scope full
```

### Answer Questions

```bash
python scripts/python/jarvis_courage_evaluation_system.py \
    --question-id q_model_deployment_uncertainty \
    --answer "Use llama3.2:latest with mapping to expected name"
```

### Configuration

Edit `config/jarvis_courage_eval_config.json`:

```json
{
    "courage_threshold": "balanced",
    "allow_questions": true,
    "question_priority_threshold": "medium",
    "evaluation_scope": "full",
    "directive_recognition": {
        "slash_commands": true,
        "doit_commands": true,
        "explicit_directives": true,
        "implied_directives": true
    }
}
```

---

## 🎯 Integration with @DOIT

The system recognizes `@DOIT` commands as directives:

```python
directive = system.recognize_directive("@DOIT deploy models to KAIJU")
# Returns: DirectiveType.DOIT_COMMAND
```

When a directive is recognized:
1. **Execute with courage** - Don't hesitate
2. **Ask clarifying questions** - But don't wait for answers if context is clear
3. **Make decisions** - Take action based on best available information
4. **Document questions** - For debrief/summary discussion

---

## 💡 Examples

### Example 1: Model Deployment

**Problem**: Model name format unclear
**Question**: "Should we use llama3.2:latest or llama3.2:11b?"
**Courageous Decision**: Use `llama3.2:latest` (actual Ollama name) with mapping
**Result**: ✅ Deployed successfully

### Example 2: File Location

**Problem**: Downloaded files location unclear
**Question**: "Where did the files move to?"
**Courageous Decision**: Search comprehensively, then move if found
**Result**: ✅ Found and moved to correct location

---

## 📊 Evaluation Metrics

- **Problems Identified**: Number of contextual problems
- **Decisions Made**: Number of decisions taken
- **Questions Asked**: Number of debrief questions
- **Courage Level**: Overall courage assessment
- **Recommendations**: Actionable recommendations

---

## 🔗 Related Systems

- `lumina_decisioning_engine.py` - Core decisioning engine
- `jarvis_decision_matrix_analysis.py` - Decision matrix analysis
- `@DOIT` command system - Directive execution

---

## 🎯 Best Practices

1. **Recognize Directives**: Slash commands = "HERE DO THIS!"
2. **Be Courageous**: Make decisions when context is clear
3. **Ask Questions**: But don't wait if action is needed
4. **Document Everything**: For debrief/summary discussion
5. **Balance Risk**: Bold but not reckless

---

**Status:** ✅ **JARVIS COURAGE EVALUATION SYSTEM ACTIVE**

**Power Recognition:** JARVIS evaluates with courage, asks questions for clarification, and recognizes directives as execution commands.
