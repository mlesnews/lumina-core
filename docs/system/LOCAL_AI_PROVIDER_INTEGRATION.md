# Local AI Provider Integration (ULTRON & Iron Legion)

## Overview

ULTRON and Iron Legion are now fully integrated into the Cloud AI Provider Tracker system, allowing the system to learn which provider (local or cloud) is best for each job type.

## ULTRON - Hybrid Cluster

### Architecture

ULTRON is a hybrid cluster that combines:
- **Local ULTRON** (localhost:11434): Laptop-based models
- **KAIJU Iron Legion** (10.17.17.32:11434): NAS-based models

This provides intelligent routing, load balancing, and automatic failover.

### Traits

- **Hybrid Routing**: Intelligent routing between local and NAS nodes
- **Local-First**: Privacy-first, no data leaves local network
- **Zero Cost**: No API costs, runs on local infrastructure

### Specialties

- **Advanced Reasoning**: Excellent for complex reasoning and multi-step tasks
- **Code Generation**: Strong code generation with local models

### Uniqueness

- **Hybrid Cluster Architecture**: Combines laptop and NAS into single virtual cluster
- **Default Model Protection**: Protected as default model in Cursor IDE

### Models

- qwen2.5:72b
- llama3.2:11b
- codellama:13b
- llama3
- codellama:13b

## Iron Legion - KAIJU Cluster

### Architecture

Iron Legion is a cluster of expert models running on KAIJU NAS (10.17.17.32) for centralized resource management.

### Traits

- **Expert Models**: Specialized models for different task types
- **NAS-Based**: Runs on KAIJU NAS for centralized management
- **Load Balancing**: Intelligent load balancing across multiple models

### Specialties

- **Batch Processing**: Excellent for parallel batch processing tasks
- **Multi-Model Routing**: Routes to best model for each task type

### Uniqueness

- **KAIJU NAS Integration**: Deeply integrated with KAIJU NAS infrastructure
- **Self-Healing Cluster**: Automatic monitoring and self-healing capabilities

### Models

- llama3
- codellama:13b
- qwen2.5:72b

## Integration with Provider Tracker

Both ULTRON and Iron Legion are tracked alongside cloud providers:

```python
from cloud_ai_provider_tracker import (
    CloudAIProviderTracker,
    ProviderType,
    TaskCategory,
    get_provider_tracker
)

tracker = get_provider_tracker()

# Record performance for ULTRON
tracker.record_job_performance(
    ProviderType.ULTRON,
    TaskCategory.CODE_GENERATION,
    success=True,
    quality_score=0.90,
    time_taken=30.0,
    cost=0.0  # Zero cost for local
)

# Record performance for Iron Legion
tracker.record_job_performance(
    ProviderType.IRON_LEGION,
    TaskCategory.BATCH_PROCESSING,
    success=True,
    quality_score=0.85,
    time_taken=45.0,
    cost=0.0  # Zero cost for local
)

# Get best provider (local or cloud)
best = tracker.get_best_provider_for_job(TaskCategory.CODE_GENERATION)
# Could return ULTRON, Iron Legion, or a cloud provider based on learned performance
```

## Auto Mode Selection

When Cursor IDE agent mode's "auto" is used:

1. **Local-First**: ULTRON and Iron Legion are prioritized by default
2. **Learned Selection**: System uses learned performance to choose best provider
3. **Hybrid Mode**: Can combine local for simple tasks, cloud for complex tasks
4. **Performance Tracking**: All jobs are tracked to improve future selections

### Selection Priority

For local-only mode:
1. ULTRON (hybrid cluster)
2. Iron Legion (KAIJU cluster)
3. Iron Legion Router
4. Load Balancer
5. Local Cluster
6. Docker Ollama

For hybrid mode:
- Simple tasks → Local (ULTRON/Iron Legion)
- Complex tasks → Cloud (Anthropic/OpenAI/Azure)

## Benefits

1. **Privacy**: Local providers keep data on-premises
2. **Cost**: Zero API costs for local providers
3. **Performance**: Can be faster than cloud for local tasks
4. **Learning**: System learns which provider is best for each job type
5. **Flexibility**: Can use local or cloud based on requirements

## Tags

`#ULTRON` `#IRON_LEGION` `#LOCAL_AI` `#PROVIDER_TRACKING` `#DECISIONING` `@JARVIS` `@LUMINA`
