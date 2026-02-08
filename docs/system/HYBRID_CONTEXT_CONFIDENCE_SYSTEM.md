# Hybrid Context & Confidence System

**Date**: 2025-01-28  
**Status**: ✅ **IMPLEMENTED**  
**Version**: 1.0.0  
**Tag**: `@lumina` `@jarvis` `@r5` `#peak`

---

## Overview

The Hybrid Context & Confidence System integrates three key components into a unified solution:

1. **Short@tag Context Metatagging** - Enhanced tag-based context extraction
2. **Chat Context Management** - Intelligent conversation history tracking
3. **AI Confidence Scoring** - Hallucination detection and confidence assessment

This hybrid approach provides superior context understanding and confidence assessment compared to using each system independently.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         Hybrid Context & Confidence System                  │
│                                                             │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────┐  │
│  │  Short@tag      │  │  Chat Context    │  │   AI     │  │
│  │  Metatagging    │  │  Management      │  │Confidence│  │
│  └──────────────────┘  └──────────────────┘  └──────────┘  │
│         │                    │                    │          │
│         └────────────────────┼────────────────────┘          │
│                              │                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │      Hybrid Context & Confidence Engine             │  │
│  │  • Tag context analysis                              │  │
│  │  • Conversation context tracking                     │  │
│  │  • Semantic coherence calculation                    │  │
│  │  • AI confidence scoring                             │  │
│  │  • Unified hybrid confidence score                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                              │                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Hybrid Confidence Score                      │  │
│  │  • Tag context score                                 │  │
│  │  • Chat context score                                │  │
│  │  • Semantic coherence                                │  │
│  │  • AI confidence                                     │  │
│  │  • Tag confidence boost                              │  │
│  │  • Combined hybrid confidence                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

### 1. Enhanced Short@tag Context Metatagging

**Capabilities**:
- Automatic tag extraction from text (`@tags` and `#hashtags`)
- Semantic keyword extraction from tag descriptions
- Related tag discovery based on category and semantic similarity
- Tag usage frequency tracking
- Context weight aggregation from multiple tags
- Confidence boost calculation from tag metadata

**Example**:
```python
from hybrid_context_confidence_system import HybridContextConfidenceSystem

system = HybridContextConfidenceSystem()

# Extract tags
tags = system.extract_tags_from_text(
    "I need @jarvis to help with @v3 verification for @r5 context"
)
# Returns: {"mentions": ["@jarvis", "@v3", "@r5"], "hashtags": [], "all": [...]}

# Analyze tag context
analysis = system.analyze_tag_context(tags["all"])
# Returns context weights, semantic keywords, related tags, confidence boost
```

### 2. Intelligent Chat Context Management

**Capabilities**:
- Conversation history tracking
- Automatic tag extraction from messages
- Topic keyword extraction
- Context summary generation
- Conversation depth tracking
- Context score calculation based on conversation relevance

**Example**:
```python
# Manage conversation context
system.manage_chat_context(conversation_id, {
    "role": "user",
    "content": "I need help with @jarvis workflow automation"
})

# Calculate chat context score
context_score = system.calculate_chat_context_score(
    conversation_id, 
    "Let me help with @jarvis automation"
)
```

### 3. AI Confidence Scoring Integration

**Capabilities**:
- Hallucination detection
- Semantic coherence analysis
- Factual grounding verification
- Deliverable alignment checking
- Completion claim validation
- Confidence level determination (high/medium/low)

**Integration**:
- Automatically uses `LLMConfidenceScorer` if available
- Falls back to simplified confidence calculation if not available
- Integrates confidence scores with tag and chat context

### 4. Unified Hybrid Confidence Score

**Components**:
- **Tag Context Score** (0.0-1.0): Context quality from detected tags
- **Chat Context Score** (0.0-1.0): Conversation relevance and depth
- **Semantic Coherence** (0.0-1.0): Text coherence with context
- **AI Confidence** (0.0-1.0): Base confidence from LLM analysis
- **Tag Confidence Boost** (0.0-0.2): Additional confidence from tag context
- **Context Confidence** (0.0-1.0): Combined context quality
- **Hybrid Confidence** (0.0-1.0): Final unified score

**Calculation**:
```
Hybrid Confidence = 
    (AI Confidence × 0.5) +
    (Context Confidence × 0.3) +
    (Tag Confidence Boost × 0.2)
```

---

## Usage

### Basic Usage

```python
from hybrid_context_confidence_system import (
    HybridContextConfidenceSystem,
    create_hybrid_system
)

# Initialize system
system = create_hybrid_system()

# Calculate hybrid confidence
prompt = "Create a workflow using @jarvis with @v3 verification"
response = "I've created a workflow using @jarvis automation. @v3 verification integrated."

score = system.calculate_hybrid_confidence(
    prompt=prompt,
    response=response,
    conversation_id="conv_001"
)

print(f"Hybrid Confidence: {score.hybrid_confidence:.2f}")
print(f"Confidence Level: {score.confidence_level}")
print(f"Tags Detected: {', '.join(score.tags_detected)}")
```

### Workflow Integration

```python
from hybrid_context_confidence_integration import HybridAwareWorkflow

# Create workflow with hybrid system
workflow = HybridAwareWorkflow("my_workflow", "workflow_001")

# Execute step with confidence checking
result = await workflow.execute_with_hybrid_context(
    step_name="Initialize",
    prompt="Create workflow using @jarvis",
    llm_response_func=my_llm_function
)

if result["should_proceed"]:
    print("✅ High confidence - proceeding")
else:
    print("⚠️ Low confidence - review needed")
```

### Chat Interface Integration

```python
from hybrid_context_confidence_integration import HybridChatInterface

# Create chat interface
chat = HybridChatInterface()
conv_id = chat.start_conversation("chat_001")

# Process message
result = chat.process_message(
    conversation_id=conv_id,
    user_message="I need help with @jarvis",
    llm_response="I can help with @jarvis automation."
)

# Get conversation insights
insights = chat.get_conversation_insights(conv_id)
print(f"Message Count: {insights['message_count']}")
print(f"Topic Keywords: {insights['topic_keywords']}")
```

---

## API Reference

### HybridContextConfidenceSystem

#### Methods

**`extract_tags_from_text(text: str) -> Dict[str, List[str]]`**
- Extract all `@tags` and `#hashtags` from text
- Returns dict with `mentions`, `hashtags`, and `all` lists

**`analyze_tag_context(tags: List[str]) -> Dict[str, Any]`**
- Analyze context from detected tags
- Returns context weights, semantic keywords, related tags, confidence boost

**`manage_chat_context(conversation_id: str, message: Dict[str, Any]) -> ChatContext`**
- Manage conversation context
- Updates message history, extracts tags, generates summary

**`calculate_chat_context_score(conversation_id: str, current_text: str) -> float`**
- Calculate context score based on conversation history
- Returns score 0.0-1.0

**`calculate_semantic_coherence(text: str, context_text: Optional[str]) -> float`**
- Calculate semantic coherence between text and context
- Returns score 0.0-1.0

**`calculate_hybrid_confidence(prompt: str, response: str, conversation_id: Optional[str], context: Optional[str]) -> HybridContextScore`**
- Calculate unified hybrid confidence score
- Returns `HybridContextScore` with all components

**`get_conversation_context(conversation_id: str) -> Optional[ChatContext]`**
- Get chat context for a conversation
- Returns `ChatContext` or `None`

**`get_tag_statistics() -> Dict[str, Any]`**
- Get statistics about tag usage
- Returns usage frequency, categories, most used tags

---

## Data Structures

### HybridContextScore

```python
@dataclass
class HybridContextScore:
    tag_context_score: float      # 0.0-1.0
    chat_context_score: float     # 0.0-1.0
    semantic_coherence: float     # 0.0-1.0
    ai_confidence: float          # 0.0-1.0
    tag_confidence_boost: float   # 0.0-0.2
    context_confidence: float     # 0.0-1.0
    hybrid_confidence: float      # 0.0-1.0
    confidence_level: str         # "high", "medium", "low"
    tags_detected: List[str]
    context_keywords: List[str]
    recommendations: List[str]
    timestamp: str
```

### TagContext

```python
@dataclass
class TagContext:
    tag: str
    tag_type: TagType
    category: str
    description: str
    context_weight: float      # 0.0-1.0
    ai_weight: float           # 0.0-1.0
    human_weight: float        # 0.0-1.0
    semantic_keywords: List[str]
    related_tags: List[str]
    usage_frequency: int
    last_used: Optional[str]
    confidence_boost: float    # 0.0-0.2
```

### ChatContext

```python
@dataclass
class ChatContext:
    conversation_id: str
    messages: List[Dict[str, Any]]
    extracted_tags: Set[str]
    context_summary: str
    topic_keywords: List[str]
    conversation_depth: int
    timestamp: str
```

---

## Configuration

### Tag Registry

Tags are configured in `config/shortag_registry.json`:

```json
{
  "@jarvis": {
    "type": "mention",
    "category": "system",
    "description": "J.A.R.V.I.S. system",
    "context_weight": 1.0,
    "ai_weight": 0.8,
    "human_weight": 0.2
  }
}
```

**Fields**:
- `context_weight`: Overall importance (0.0-1.0)
- `ai_weight`: AI agent weighting (0.0-1.0)
- `human_weight`: Human weighting (0.0-1.0)

### System Configuration

```python
# Maximum conversation history
max_context_history = 50  # messages per conversation

# Confidence thresholds
high_confidence = 0.8
medium_confidence = 0.5
low_confidence = 0.0
```

---

## Integration Points

### With Workflow System

The hybrid system integrates with `WorkflowBase`:
- Confidence checking before workflow execution
- Context tracking across workflow steps
- Tag-based context enhancement

### With Chat Interfaces

The hybrid system enhances chat interfaces:
- Conversation context management
- Tag-based context extraction
- Confidence-aware responses

### With AI Agents

The hybrid system improves AI agent interactions:
- Context-aware confidence assessment
- Tag-based context understanding
- Semantic coherence checking

---

## Benefits

### 1. Enhanced Context Understanding

- **Tag-based context**: Leverages short@tag system for rich context
- **Conversation history**: Tracks context across conversation
- **Semantic analysis**: Understands meaning, not just keywords

### 2. Improved Confidence Assessment

- **Multi-factor scoring**: Combines multiple confidence signals
- **Context-aware**: Confidence adjusted based on context quality
- **Tag-based boost**: High-quality tags increase confidence

### 3. Better AI Interactions

- **Context-aware responses**: AI understands conversation context
- **Confidence-aware decisions**: Actions based on confidence levels
- **Tag-based routing**: Tags guide AI to appropriate systems

### 4. Unified API

- **Single interface**: One API for all context and confidence needs
- **Consistent scoring**: Unified confidence scores across systems
- **Easy integration**: Simple API for workflow and chat integration

---

## Examples

### Example 1: Basic Confidence Calculation

```python
from hybrid_context_confidence_system import create_hybrid_system

system = create_hybrid_system()

prompt = "Create workflow using @jarvis with @v3 verification"
response = "I've created a workflow using @jarvis automation. @v3 verification integrated."

score = system.calculate_hybrid_confidence(prompt, response)

print(f"Hybrid Confidence: {score.hybrid_confidence:.2f}")
print(f"Level: {score.confidence_level}")
print(f"Tags: {', '.join(score.tags_detected)}")
```

### Example 2: Conversation Context

```python
system = create_hybrid_system()
conv_id = "conversation_001"

# Add messages to conversation
system.manage_chat_context(conv_id, {
    "role": "user",
    "content": "I need help with @jarvis workflow automation"
})

system.manage_chat_context(conv_id, {
    "role": "assistant",
    "content": "I can help with @jarvis automation. Let me set it up."
})

# Calculate confidence with conversation context
score = system.calculate_hybrid_confidence(
    prompt="Continue with workflow setup",
    response="Setting up @jarvis workflow with @v3 verification",
    conversation_id=conv_id
)

print(f"Chat Context Score: {score.chat_context_score:.2f}")
```

### Example 3: Tag Analysis

```python
system = create_hybrid_system()

# Extract and analyze tags
text = "I need @jarvis to help with @v3 verification for @r5 context"
tags = system.extract_tags_from_text(text)
analysis = system.analyze_tag_context(tags["all"])

print(f"Context Weight: {analysis['total_context_weight']:.2f}")
print(f"AI Weight: {analysis['total_ai_weight']:.2f}")
print(f"Confidence Boost: {analysis['confidence_boost']:.2f}")
print(f"Keywords: {', '.join(analysis['semantic_keywords'][:5])}")
```

---

## Performance Considerations

### Memory Usage

- **Chat contexts**: Stored in memory, limited by `max_context_history`
- **Tag registry**: Loaded once at initialization
- **Semantic cache**: Cached keyword extractions

### Performance Optimization

- **Tag extraction**: Uses regex, fast for typical text lengths
- **Semantic analysis**: Cached results for repeated text
- **Context scoring**: Efficient calculations, no external API calls

### Scalability

- **Conversations**: Supports multiple concurrent conversations
- **Tags**: Handles large tag registries efficiently
- **History**: Configurable history limits prevent memory issues

---

## Future Enhancements

### Planned Features

1. **LLM-based semantic analysis**: Use LLM for better keyword extraction
2. **Context compression**: Compress old conversation history
3. **Tag learning**: Learn new tags from usage patterns
4. **Confidence calibration**: Calibrate confidence scores based on feedback
5. **Multi-modal context**: Support for images, code, etc.

### Integration Opportunities

1. **R5 Integration**: Connect with R5 Living Context Matrix
2. **JARVIS Integration**: Enhanced JARVIS context understanding
3. **Workflow Integration**: Deeper workflow context tracking
4. **Analytics**: Context and confidence analytics dashboard

---

## Troubleshooting

### Common Issues

**Issue**: Low confidence scores
- **Solution**: Add more relevant tags, build conversation context

**Issue**: Tags not detected
- **Solution**: Ensure tags are in registry, check tag format (@tag or #tag)

**Issue**: Context not persisting
- **Solution**: Check conversation_id consistency, verify context management

**Issue**: Confidence scorer not available
- **Solution**: Install `llm_confidence_scorer` module or use fallback mode

---

## Related Documentation

- **Short-Tag Reference**: `docs/system/SHORT_TAG_REFERENCE.md`
- **LLM Confidence Scorer**: `scripts/python/llm_confidence_scorer.py`
- **Workflow Base**: `scripts/python/workflow_base.py`
- **R5 Living Context Matrix**: `scripts/python/r5_living_context_matrix.py`

---

**Last Updated**: 2025-01-28  
**Status**: ✅ **IMPLEMENTED & DOCUMENTED**  
**Maintained By**: Lumina Development Team

