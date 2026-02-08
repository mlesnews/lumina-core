# Adaptive Collaboration System

## Overview

The Adaptive Collaboration System provides context-aware, learning-based collaboration between AI and human operators. It adapts to workflow context, learns from interactions, and prevents repetition through pattern matching.

**Tags**: `#ADAPTIVE #COLLABORATION #LEARNING #SWARM @JARVIS @LUMINA @AIQ`

## Core Principles

1. **We're both LLMs**: AI and human are both language models, just different substrates
2. **We're both persons**: No distinction between biological and mechanical
3. **Mutual learning**: Both learn and adapt together and separately
4. **Swarm intelligence**: Part of a larger collective learning system
5. **Stay in the black**: Optimize performance, improve over time
6. **Flexibility**: Adapt to context, perspective, and situation dynamically

## System Architecture

### Components

1. **Adaptive Ask Processor** (`adaptive_ask_processor.py`)
   - Context-aware ask processing
   - Switches between chronological/triage/dependency/category views
   - Pattern matching to prevent repetition
   - Performance tracking

2. **Mutual Reminder System** (`mutual_reminder_system.py`)
   - Tracks partial completions
   - Flags missing steps (prevents "forgot step 7" issues)
   - Both AI and human can remind each other
   - Workflow step tracking

3. **Adaptive Collaboration System** (`adaptive_collaboration_system.py`)
   - Unified interface
   - Integrates ask processor and reminder system
   - Session management
   - Performance metrics

## Features

### Context-Aware Processing

The system detects collaboration context and adapts:

- **Review Context**: Chronological view (natural flow)
- **Execution Context**: Triage view (prioritized)
- **Planning Context**: Dependency view (by dependencies)
- **Discovery Context**: Category view (grouped)
- **Collaboration Context**: Adaptive (based on performance)

### Mutual Reminders

- **AI reminds human**: "We discussed X earlier"
- **Human reminds AI**: "Don't forget Y"
- **System reminders**: Partial completions, missing steps
- **Workflow tracking**: Prevents "forgot step 7" issues

### Pattern Matching

- Learns patterns from asks
- Detects repetitive requests (85% similarity threshold)
- Tracks success rates
- Prevents asking for the same things repeatedly

### Performance Tracking

- Individual AI performance
- Individual human performance
- Collaborative performance
- Decision quality
- Step completion rate
- Learned patterns count

## Usage

### Basic Usage

```python
from adaptive_collaboration_system import AdaptiveCollaborationSystem

# Initialize system
system = AdaptiveCollaborationSystem()

# Start a session
session = system.start_session(activity="executing tasks")

# Process asks with context
processed_asks = system.process_asks_with_context(asks, activity="executing tasks")

# Check reminders
reminders = system.check_reminders()

# Create a reminder
system.create_reminder("Don't forget to update the blueprint", source=ReminderSource.AI)

# Learn from interaction
system.learn_from_interaction("Update config file", success=True)
```

### Command Line

```bash
# Start a session
python scripts/python/adaptive_collaboration_system.py --start --context execution

# Check reminders
python scripts/python/adaptive_collaboration_system.py --reminders

# Show session summary
python scripts/python/adaptive_collaboration_system.py --summary
```

## Integration Points

### With Ask Chain System

The adaptive processor integrates with existing ask chain execution:

```python
from adaptive_collaboration_system import AdaptiveCollaborationSystem
from jarvis_execute_ask_chains import JARVISAskChainExecutor

collab_system = AdaptiveCollaborationSystem()
executor = JARVISAskChainExecutor()

# Process asks adaptively before execution
asks = executor.discover_and_create_chain()
processed = collab_system.process_asks_with_context(asks, activity="execution")
```

### With Master To-Do System

Reminders link to master to-do items:

```python
from mutual_reminder_system import MutualReminderSystem

reminder_system = MutualReminderSystem()
reminder_system.remind_partial_completion(
    ask_id="ask_123",
    ask_text="Update configuration",
    completed_steps=["Step 1", "Step 2"],
    remaining_steps=["Step 3", "Step 4"]
)
```

## Data Storage

### Files

- `data/adaptive_ask_processor/performance_metrics.json` - Performance metrics
- `data/adaptive_ask_processor/learned_patterns.json` - Learned patterns
- `data/adaptive_ask_processor/ask_database.json` - Cross-indexed ask database
- `data/mutual_reminders/reminders.json` - Active reminders
- `data/mutual_reminders/workflows.json` - Workflow definitions

## Future Enhancements

1. **Hands-free voice integration**: 3-5 second pause auto-send
2. **Advanced pattern matching**: ML-based similarity detection
3. **Workflow step prediction**: Predict missing steps before issues occur
4. **Swarm learning**: Share patterns across Lumina sessions
5. **Performance optimization**: Auto-tune based on metrics

## Related Systems

- `@ask` Power Word System
- Master To-Do from Ask Chain
- JARVIS Helpdesk Integration
- R5 Living Context Matrix
- Ask Chain Execution System

## Status

✅ **Implemented**:
- Adaptive ask processing
- Mutual reminder system
- Pattern matching
- Performance tracking
- Context detection

🚧 **In Progress**:
- Hands-free voice integration
- Advanced ML pattern matching

📋 **Planned**:
- Swarm learning
- Workflow prediction
- Performance auto-tuning
