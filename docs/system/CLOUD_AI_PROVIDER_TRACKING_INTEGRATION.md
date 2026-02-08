# Cloud AI Provider Tracking & #Decisioning Integration

## Overview

This document describes the Cloud AI Provider Tracking System and its integration with the #decisioning engine and Cursor IDE agent mode's "auto" functionality.

## Components

### 1. Cloud AI Provider Tracker (`cloud_ai_provider_tracker.py`)

A comprehensive system for tracking cloud AI providers (OpenAI, Anthropic, Google, etc.) to identify:

- **Traits**: Capabilities, characteristics (e.g., "Versatility", "Reasoning", "Multi-modal")
- **Specialties**: What they excel at (e.g., "Code Generation", "Code Review")
- **Uniqueness**: What makes them unique (e.g., "Constitutional AI", "Enterprise Integration")
- **@Sparks**: Insights and learnings captured about each provider
- **Job Performance**: Learning system that tracks which provider is best for which job type

### 2. Integration with #Decisioning Engine

The `auto_mode_decision_tree.py` now integrates with:

- **LuminaDecisioningEngine**: Uses #decisioning for decision-making workflows
- **CloudAIProviderTracker**: Uses learned provider performance for model selection

### 3. Integration with Auto Mode Model Selector

The `auto_mode_model_selector.py` now:

- Uses Cloud AI Provider Tracker to get best provider for job type
- Learns from job performance to improve selection over time
- Falls back to heuristics if no learned data available

## How It Works

### Provider Tracking

```python
from cloud_ai_provider_tracker import (
    CloudAIProviderTracker,
    ProviderType,
    TaskCategory,
    get_provider_tracker
)

tracker = get_provider_tracker()

# Capture a @spark about a provider
tracker.capture_provider_spark(
    ProviderType.ANTHROPIC,
    "Claude excels at code review tasks with detailed explanations",
    source="user_observation",
    context={"task": "code_review", "quality": "high"}
)

# Record job performance
tracker.record_job_performance(
    ProviderType.ANTHROPIC,
    TaskCategory.CODE_REVIEW,
    success=True,
    quality_score=0.95,
    time_taken=45.0,
    cost=0.05
)

# Get best provider for a job
best = tracker.get_best_provider_for_job(TaskCategory.CODE_REVIEW)
```

### Auto Mode Integration

When Cursor IDE agent mode's "auto" is used:

1. **Request Analysis**: Analyzes the request (intent, complexity, modality, etc.)
2. **#Decisioning**: Uses LuminaDecisioningEngine for decision-making
3. **Provider Selection**: Uses CloudAIProviderTracker to get best provider for job type
4. **Model Selection**: Selects optimal model based on learned performance
5. **Execution**: Executes with selected model
6. **Learning**: Records performance to improve future selections

## Task Categories

The system tracks performance across these task categories:

- `CODE_GENERATION`: Generating new code
- `CODE_REVIEW`: Reviewing and analyzing code
- `DEBUGGING`: Finding and fixing bugs
- `REFACTORING`: Restructuring code
- `DOCUMENTATION`: Writing documentation
- `ANALYSIS`: Analyzing code/data
- `REASONING`: Complex reasoning tasks
- `CREATIVE`: Creative writing/content
- `MULTI_MODAL`: Tasks requiring multiple modalities
- `CONVERSATION`: Conversational tasks
- `RESEARCH`: Research tasks
- `TRANSLATION`: Translation tasks
- `SUMMARIZATION`: Summarization tasks
- `QUESTION_ANSWERING`: Q&A tasks

## Provider Performance Scoring

The system calculates an overall performance score based on:

- **Success Rate** (40%): Percentage of successful jobs
- **Quality Score** (30%): Average quality rating
- **Speed** (20%): Average time per job (inverse)
- **Cost** (10%): Cost per job (inverse)

## Default Providers

The system initializes with default profiles for:

### Local AI Providers

- **ULTRON**: Hybrid cluster combining local ULTRON and KAIJU Iron Legion
  - Traits: Hybrid Routing, Local-First, Zero Cost
  - Specialties: Advanced Reasoning, Code Generation
  - Uniqueness: Hybrid Cluster Architecture, Default Model Protection
  
- **Iron Legion**: KAIJU Iron Legion Cluster on NAS
  - Traits: Expert Models, NAS-Based, Load Balancing
  - Specialties: Batch Processing, Multi-Model Routing
  - Uniqueness: KAIJU NAS Integration, Self-Healing Cluster

### Cloud AI Providers

- **OpenAI**: Versatile, strong code generation
- **Anthropic**: Strong reasoning, excellent code review
- **Azure OpenAI**: Enterprise integration, stability
- **Google**: Multi-modal strength

## @Sparks Integration

All provider insights are captured as @sparks and integrated with:

- **Insights/Sparks System**: Captures insights for future reference
- **R5 Living Context Matrix**: Aggregates insights into knowledge matrix
- **SYPHON**: Extracts intelligence from insights

## Usage in Cursor IDE Agent Mode

When using Cursor IDE agent mode's "auto":

1. The system automatically uses #decisioning for decision-making
2. **Local-First Approach**: ULTRON and Iron Legion are prioritized for privacy and cost
3. Provider selection is based on learned performance (local vs cloud)
4. Performance is recorded after each job
5. The system learns and improves over time

### Local vs Cloud Selection

- **Local Providers (ULTRON, Iron Legion)**: Used by default for privacy, zero cost, and local-first workflows
- **Cloud Providers**: Used when complexity is high, or when learned performance indicates cloud is better
- **Hybrid Mode**: Combines local for simple tasks, cloud for complex tasks

## Configuration

Provider data is stored in:
- `data/cloud_ai_providers/providers.json`

Insights/sparks are stored in:
- `data/insights_sparks/sparks/`

## Future Enhancements

- Real-time provider performance monitoring
- Automatic provider recommendation based on context
- Integration with cost tracking
- Multi-provider comparison dashboards
- Provider-specific optimization strategies

## Tags

`#CLOUD_AI` `#PROVIDER_TRACKING` `#DECISIONING` `#SPARKS` `@JARVIS` `@LUMINA`
