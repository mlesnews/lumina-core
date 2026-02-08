# IDE Workflow Optimization - @peak @ask per second rate

**Date:** 2025-12-27  
**Status:** ✅ **COMPLETE**  
**Context:** Optimizing IDE analyst/engineer workflows for peak ask rate and flow

---

## Overview

The IDE Workflow Optimizer tracks and optimizes IDE workflows to maximize @ask per second rate and workflow flow efficiency. It provides real-time metrics, identifies bottlenecks, and generates optimization recommendations.

---

## Key Features

### 1. Ask Rate Tracking

- **Questions per Second**: Tracks current ask rate over configurable time windows
- **Peak Rate Calculation**: Identifies maximum throughput achieved
- **Rate Efficiency**: Compares current rate to target rate
- **Trend Analysis**: Tracks rate over time

### 2. Flow Efficiency Metrics

- **Response Time Tracking**: Monitors average response times
- **Consistency Measurement**: Tracks variance in response times
- **Bottleneck Identification**: Detects workflow bottlenecks
- **Optimization Score**: 0-100 score indicating workflow health

### 3. Optimization Recommendations

- **Rate Optimization**: Strategies to increase ask rate
- **Response Time Optimization**: Methods to reduce latency
- **Flow Optimization**: Actions to improve workflow continuity
- **Mode Optimization**: Recommendations for mode usage

---

## Usage

### Get Current Metrics

```bash
python scripts/python/ide_workflow_optimizer.py --metrics
```

Output includes:
- Ask rate (questions/second)
- Average response time
- Peak ask rate
- Flow efficiency (0-1)
- Bottlenecks identified
- Optimization score (0-100)

### Get Current Ask Rate

```bash
python scripts/python/ide_workflow_optimizer.py --rate
```

### Get Optimization Recommendations

```bash
python scripts/python/ide_workflow_optimizer.py --recommendations
```

### Optimize for Peak Flow

```bash
python scripts/python/ide_workflow_optimizer.py --optimize
```

### Record an Ask Interaction

```bash
python scripts/python/ide_workflow_optimizer.py --record '{
  "question_id": "q123",
  "question_length": 100,
  "response_time": 1.5,
  "mode": "ask",
  "context_size": 4096,
  "tokens_used": 500
}'
```

### Save Metrics

```bash
python scripts/python/ide_workflow_optimizer.py --save
```

---

## Configuration

Configuration file: `config/ide_workflow_optimization.json`

### Key Settings

```json
{
  "target_ask_rate_per_second": 5.0,
  "target_response_time_ms": 2000.0,
  "peak_mode_threshold": 3.0,
  "flow_window_seconds": 60
}
```

### Optimization Modes

1. **Peak Mode** (target: 5.0 asks/sec)
   - Maximum throughput
   - Prioritize speed
   - Best for rapid iteration

2. **Balanced Mode** (target: 3.0 asks/sec)
   - Balance speed and quality
   - Standard workflow
   - Best for general use

3. **Quality Mode** (target: 2.0 asks/sec)
   - Prioritize quality
   - Slower but thorough
   - Best for complex analysis

---

## Metrics Explained

### Ask Rate (Questions/Second)

Measures throughput - how many questions can be processed per second.

**Target:** 5.0 questions/second (peak mode)

**Factors:**
- Question complexity
- Response time
- Context size
- Model performance
- System load

### Flow Efficiency (0-1 Scale)

Combined metric considering:
- **Rate Efficiency** (40%): Current rate vs target
- **Response Efficiency** (40%): Response time vs target
- **Consistency** (20%): Low variance in response times

**Target:** >0.8 (80% efficiency)

### Optimization Score (0-100)

Overall workflow health score:
- **Rate Performance** (40 points): Rate vs target
- **Flow Efficiency** (40 points): Efficiency score
- **Bottleneck Penalty** (20 points): Fewer bottlenecks = better

**Target:** >80/100

---

## Optimization Strategies

### Rate Optimization

1. **Batch Questions**: Group related questions together
2. **Use @ask Mode**: Optimized for quick queries
3. **Pre-load Context**: Reduce setup time
4. **Cache Common Patterns**: Reuse known solutions
5. **Reduce Context Size**: Faster processing

### Response Time Optimization

1. **Use Lighter Models**: Faster for simple questions
2. **Reduce Context Window**: Less data to process
3. **Enable Response Caching**: Reuse responses
4. **Use Streaming Responses**: Start showing results immediately
5. **Optimize Prompt Length**: Shorter prompts = faster responses

### Flow Optimization

1. **Reduce Context Switching**: Stay in same mode
2. **Pipeline Processing**: Process multiple items in parallel
3. **Async Operations**: Non-blocking workflows
4. **Background Tasks**: Move non-critical work to background

---

## Integration Points

### Cursor Agent Modes

- Tracks which mode (agent, plan, debug, ask) is used
- Recommends mode selection for optimization
- Integrates with `cursor_agent_modes.json`

### Cursor Workspace Mode

- Adapts to workspace vs non-workspace mode
- Adjusts optimization targets based on mode
- Integrates with workspace mode manager

### R5 Living Context Matrix

- Uses R5 for context pre-loading
- Tracks context usage patterns
- Optimizes context selection

### NAS Proxy Cache

- Caches common question patterns
- Stores optimization metrics
- Enables fast retrieval

---

## Workflow Phases

### 1. Analysis Phase

- **Target Duration**: 5 seconds
- **Optimization**: Parallel analysis, cached context, incremental processing

### 2. Question Phase (@ask)

- **Target Duration**: 2 seconds
- **Optimization**: Batch questions, pre-load context, stream responses

### 3. Implementation Phase

- **Target Duration**: 10 seconds
- **Optimization**: Parallel execution, incremental updates, background processing

### 4. Review Phase

- **Target Duration**: 3 seconds
- **Optimization**: Automated checks, parallel review, template matching

---

## Bottleneck Detection

The system automatically identifies bottlenecks:

1. **High Response Time**: Response time exceeds target
2. **Low Ask Rate**: Rate below 50% of target
3. **Mode Inefficiency**: Using slow modes (debug, plan) too frequently
4. **Context Switching**: Frequent mode changes
5. **Large Context Size**: Context too large for fast processing

---

## Real-Time Monitoring

### Metrics Dashboard

Run `--optimize` to see real-time dashboard:
```
📊 IDE Workflow Optimization Summary
============================================================
Current Ask Rate: 3.45/s
Target Rate: 5.0/s
Rate Efficiency: 69.0%
Peak Mode: ❌ No
Optimization Score: 72.5/100
Flow Efficiency: 78.5%
```

### Recommendations Display

When bottlenecks are detected, recommendations are shown:
```
📋 Recommendations:
  question:
    - Batch related questions together
    - Use @ask mode for quick queries
    - Pre-load context to reduce setup time
```

---

## Best Practices

### For Peak Ask Rate

1. **Use @ask Mode**: Optimized for questions
2. **Batch Related Questions**: Group similar queries
3. **Keep Context Small**: Use focused context
4. **Use Cached Responses**: Leverage caching
5. **Stream Responses**: Start showing results immediately

### For Flow Efficiency

1. **Stay in Same Mode**: Avoid frequent switching
2. **Pre-load Context**: Prepare context ahead of time
3. **Pipeline Operations**: Process in parallel
4. **Monitor Metrics**: Track performance regularly
5. **Adjust Targets**: Tune based on your workflow

---

## Files

1. ✅ `scripts/python/ide_workflow_optimizer.py` - Main optimizer
2. ✅ `config/ide_workflow_optimization.json` - Configuration
3. ✅ `docs/system/IDE_WORKFLOW_OPTIMIZATION.md` - This document

---

**Version:** 1.0.0  
**Last Updated:** 2025-12-27  
**Status:** ✅ **COMPLETE**

