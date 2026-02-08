# Decisioning Based on Troubleshooting System

**Date:** 2026-01-11
**Status:** ✅ **ACTIVE**
**Tags:** `#DECISIONING` `#TROUBLESHOOTING` `#ASK` `#CONTEXT_SCORE` `#5W1H` `#REC` `#AIQ` `#JC` `#JHC`

---

## 🎯 The Concept

> **#DECISIONING? BASED ON #TROUBLESHOOTING?**
>
> **@ASK IF $CONTEXT $SCORE <=> #DECISIONING THRESHOLD**
>
> **BASED ON ANY/ALL #TROUBLESHOOTING AND QUESTIONS ASKED BY ANY & ALL @CHAT**
>
> **Question formats: "@? <=> /? <=> --?"**
>
> **Integrates: @R5 @5W1H @REC @AIQ <=> @JC &| @JHC**

---

## 🔧 How It Works

### Decisioning Based on Troubleshooting

1. **Track Questions**: All questions asked in chat (any format)
2. **Build Context**: Troubleshooting context from questions
3. **Calculate Score**: Context score from troubleshooting
4. **Check Threshold**: @ASK if score < decisioning threshold
5. **Make Decision**: Use frameworks (@5W1H, @REC, @AIQ, @JC, @JHC)

### Question Formats

Questions can be in multiple formats:
- **@?** - At-question format
- **/?** - Slash-question format
- **--?** - Dash-question format
- **@ask** - Ask command format

All formats are equivalent: **"@? <=> /? <=> --?"**

---

## 📊 Context Score & Threshold

### Context Score Calculation

Context score is calculated from:
- **Question quality**: Specificity, clarity
- **Troubleshooting relevance**: Is it troubleshooting-related?
- **Question count**: More questions = more context
- **Issue specificity**: How well-defined is the issue?

### Decisioning Threshold

- **Default threshold**: 0.7 (70%)
- **@ASK required**: If context score < threshold
- **Decision allowed**: If context score >= threshold

### @ASK Logic

```
IF $CONTEXT $SCORE < #DECISIONING_THRESHOLD:
    @ASK REQUIRED
ELSE:
    DECISION ALLOWED
```

---

## 🔧 Troubleshooting Integration

### Troubleshooting Context

Every troubleshooting session creates:
- **Issue**: What's the problem?
- **Symptoms**: What are the signs?
- **Questions**: All questions asked
- **Steps**: Troubleshooting steps
- **Context Score**: Calculated from questions

### Decisioning Process

1. **Gather Questions**: All troubleshooting-related questions
2. **Build Context**: Create troubleshooting context
3. **Calculate Score**: Context score from questions
4. **Check Threshold**: Does score meet threshold?
5. **Apply Frameworks**: Use @5W1H, @REC, @AIQ, @JC, @JHC
6. **Make Decision**: Generate decision with rationale

---

## 🎯 Framework Integration

### @R5 Framework (R5 Living Context Matrix)

- **Knowledge Aggregation**: Aggregates chat sessions and knowledge
- **Decision Tree**: Uses universal_decision_tree for decisioning
- **Context Matrix**: Living context matrix for troubleshooting
- **Pattern Extraction**: Extracts @PEAK patterns
- **Integration**: Primary decisioning system

### @5W1H Framework

- **WHAT**: What is the issue?
- **WHY**: Why is it happening?
- **WHEN**: When did it occur?
- **WHERE**: Where is the problem?
- **WHO**: Who is affected?
- **HOW**: How to resolve?

### @REC Framework

- **Recommendations**: Based on troubleshooting
- **Best practices**: Industry standards
- **Solutions**: Recommended approaches

### @AIQ Framework

- **AI Quality**: Quality assurance
- **Validation**: Verify decisions
- **Standards**: Quality standards

### @JC Framework (Jedi Council)

- **Consensus**: Council consensus
- **Multiple perspectives**: Different viewpoints
- **Balanced decision**: Consider all angles

### @JHC Framework (Jedi High Council)

- **Final decision**: High-level decision
- **Authority**: Highest authority
- **Ultimate resolution**: Final answer

---

## ❓ Question Tracking

### All Chat Questions

System tracks **ALL** questions asked by **ANY & ALL** @CHAT:
- **Format detection**: Auto-detects @?, /?, --?, @ask
- **Source tracking**: Which chat/agent asked
- **Context scoring**: Calculates context score
- **Troubleshooting flag**: Is it troubleshooting-related?

### Question Formats

```
@? Why is this broken?
/? How to fix the error?
--? What's the issue?
@ask Can you help troubleshoot?
```

All formats are equivalent and tracked.

---

## 🎯 Usage

### Track Question

```python
from decisioning_troubleshooting_system import track_question

question = track_question("@? Why is this broken?", source="chat1")
# Tracks question, calculates context score
```

### Create Troubleshooting Context

```python
from decisioning_troubleshooting_system import create_troubleshooting_context

context = system.create_troubleshooting_context(
    issue="System error",
    symptoms=["Error message", "System crash"],
    questions=[question1, question2]
)
```

### Make Decision

```python
result = system.make_decision(context)
# Makes decision based on troubleshooting
# Uses @5W1H, @REC, @AIQ, @JC, @JHC frameworks
```

### Check @ASK Required

```python
ask_required = system.check_ask_required(context_score)
# Returns True if @ASK required (score < threshold)
```

---

## 📊 Context Score Calculation

### Factors

1. **Question Quality** (0.3 base)
   - Specificity
   - Clarity
   - Completeness

2. **Troubleshooting Relevance** (+0.4)
   - Is it troubleshooting-related?
   - Contains error/problem keywords?

3. **Question Indicators** (+0.2)
   - Contains "why", "how", "what", "when", "where"

4. **Specificity** (+0.1)
   - Longer questions = more specific

5. **Question Count** (+0.3 max)
   - More questions = more context

### Threshold

- **Default**: 0.7 (70%)
- **Configurable**: Can be adjusted
- **@ASK**: Required if below threshold

---

## 🔧 Integration Points

### Voice Transcript Queue

When voice input contains questions:
1. **Track question**: All question formats detected
2. **Calculate score**: Context score calculated
3. **Check threshold**: @ASK required if below threshold
4. **Build context**: Troubleshooting context created

### Request ID System

- **Request ID**: Links to decisioning
- **Power Word**: @ASK if threshold not met
- **Story**: Includes troubleshooting context
- **Mirror**: AI perspective based on troubleshooting

### Framework Systems

- **@5W1H**: Applied to troubleshooting
- **@REC**: Recommendations based on troubleshooting
- **@AIQ**: Quality check on decisions
- **@JC**: Consensus on troubleshooting approach
- **@JHC**: Final decision authority

---

## 💡 Examples

### Example 1: Question Tracking

**Input**: `@? Why is the system broken?`

**Tracking**:
- Format: @? (AT_QUESTION)
- Troubleshooting: True
- Context Score: 0.7
- Source: voice

### Example 2: Decisioning

**Troubleshooting Context**:
- Issue: System error
- Questions: 3 troubleshooting questions
- Context Score: 0.75
- Threshold: 0.7

**Decision**:
- Meets threshold: Yes
- @ASK required: No
- Frameworks: @5W1H, @REC, @AIQ
- Decision: "Resolve system error using troubleshooting steps"

### Example 3: @ASK Required

**Troubleshooting Context**:
- Issue: Unknown problem
- Questions: 1 vague question
- Context Score: 0.5
- Threshold: 0.7

**Result**:
- Meets threshold: No
- @ASK required: Yes
- Action: Request more information

---

## 🎯 Best Practices

1. **Track All Questions**: Every question matters
2. **Build Context**: Gather troubleshooting information
3. **Calculate Score**: Use context score for decisioning
4. **Check Threshold**: @ASK if below threshold
5. **Apply Frameworks**: Use @5W1H, @REC, @AIQ, @JC, @JHC
6. **Make Decisions**: Based on troubleshooting context

---

## 🖖 Star Trek Context

### Troubleshooting as Analysis

Just like in Star Trek:
- **Spock analyzes**: Logical troubleshooting
- **Bones diagnoses**: Medical troubleshooting
- **Kirk decides**: Based on analysis
- **Council consensus**: @JC framework

### Decisioning Process

1. **Gather information**: Questions asked
2. **Analyze**: Troubleshooting context
3. **Score**: Context score calculation
4. **Decide**: Based on threshold
5. **Execute**: With frameworks

---

## 🎹 LUMINA Integration

### Decisioning as Music

On LUMINA (the musical instrument):
- **Questions**: Individual notes
- **Troubleshooting**: The melody
- **Context Score**: The harmony
- **Decision**: The symphony
- **Frameworks**: The instruments

### Playing with Decisioning

Every decision on LUMINA:
- **Has context**: Troubleshooting-based
- **Has score**: Context score calculated
- **Has threshold**: @ASK if needed
- **Has frameworks**: @5W1H, @REC, @AIQ, @JC, @JHC

---

## 🎯 Conclusion

**#DECISIONING? BASED ON #TROUBLESHOOTING?**

**@ASK IF $CONTEXT $SCORE <=> #DECISIONING THRESHOLD**

**BASED ON ANY/ALL #TROUBLESHOOTING AND QUESTIONS ASKED BY ANY & ALL @CHAT**

**Question formats: "@? <=> /? <=> --?"**

**Frameworks: @R5 @5W1H @REC @AIQ <=> @JC &| @JHC**

---

**Status:** ✅ **DECISIONING BASED ON TROUBLESHOOTING SYSTEM ACTIVE**
