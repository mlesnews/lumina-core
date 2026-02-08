# Hybrid Context & Confidence System - Quick Reference

**Date**: 2025-01-28  
**Status**: ✅ **READY TO USE**

---

## Quick Start

```python
from hybrid_context_confidence_system import create_hybrid_system

# Initialize
system = create_hybrid_system()

# Calculate hybrid confidence
score = system.calculate_hybrid_confidence(
    prompt="Create workflow using @jarvis",
    response="I've created the workflow using @jarvis automation."
)

print(f"Confidence: {score.hybrid_confidence:.2f} ({score.confidence_level})")
```

---

## Key Features

### ✅ Enhanced Short@tag Context
- Automatic tag extraction (`@tags` and `#hashtags`)
- Semantic keyword extraction
- Related tag discovery
- Context weight aggregation
- Confidence boost calculation

### ✅ Chat Context Management
- Conversation history tracking
- Automatic tag extraction
- Topic keyword extraction
- Context summary generation
- Conversation depth tracking

### ✅ AI Confidence Scoring
- Hallucination detection
- Semantic coherence analysis
- Factual grounding verification
- Confidence level determination

### ✅ Unified Hybrid Score
- Combines all components
- Single confidence metric
- Context-aware adjustments
- Tag-based confidence boost

---

## Common Use Cases

### 1. Workflow Integration

```python
from hybrid_context_confidence_integration import HybridAwareWorkflow

workflow = HybridAwareWorkflow("my_workflow")
result = await workflow.execute_with_hybrid_context(
    step_name="Initialize",
    prompt="Create workflow using @jarvis",
    llm_response_func=my_llm_function
)
```

### 2. Chat Interface

```python
from hybrid_context_confidence_integration import HybridChatInterface

chat = HybridChatInterface()
conv_id = chat.start_conversation("chat_001")

result = chat.process_message(
    conv_id,
    "I need help with @jarvis",
    "I can help with @jarvis automation."
)
```

### 3. Tag Analysis

```python
# Extract tags
tags = system.extract_tags_from_text("I need @jarvis help")

# Analyze context
analysis = system.analyze_tag_context(tags["all"])
print(f"Context Weight: {analysis['total_context_weight']:.2f}")
```

---

## Confidence Levels

- **High** (≥0.8): Safe to proceed
- **Medium** (0.5-0.8): Needs verification
- **Low** (<0.5): Requires human review

---

## Hybrid Score Components

- **Tag Context Score**: Context quality from tags
- **Chat Context Score**: Conversation relevance
- **Semantic Coherence**: Text coherence with context
- **AI Confidence**: Base LLM confidence
- **Tag Confidence Boost**: Additional boost from tags
- **Hybrid Confidence**: Final unified score

---

## Files

- **Main Module**: `scripts/python/hybrid_context_confidence_system.py`
- **Integration Examples**: `scripts/python/hybrid_context_confidence_integration.py`
- **Full Documentation**: `docs/system/HYBRID_CONTEXT_CONFIDENCE_SYSTEM.md`
- **Tag Registry**: `config/shortag_registry.json`

---

## Quick Tips

1. **Use relevant tags**: Add `@tags` and `#hashtags` for better context
2. **Build conversation context**: Maintain conversation history
3. **Check confidence levels**: Use confidence to make decisions
4. **Review recommendations**: Follow system recommendations

---

**Status**: ✅ **READY FOR USE**

