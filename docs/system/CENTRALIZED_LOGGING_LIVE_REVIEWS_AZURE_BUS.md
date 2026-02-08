# Centralized Logging & Live Reviews via Azure Service Bus

**Date**: 2025-01-27  
**Status**: ✅ **ARCHITECTURE DEFINED**  
**Tag**: `@triage` `#logging` `#azure-bus` `#live-reviews` `@aiq` `#jedi-council` `#3-5-7-escalation`

---

## Executive Summary

**Centralized logging architecture** where all app/system logs feed through Azure Service Bus (async) for live reviews, instant replay, @AIQ and Jedi-Council analysis, with dynamic tiered scaling and live lookback capabilities.

---

## Part 1: Centralized Logging Architecture

### 1.1 Logging Flow via Azure Service Bus

```
┌─────────────────────────────────────────────────────────────┐
│              All Apps/Systems (Front-End & Back-End)        │
│                                                             │
│  • Lumina Services                                          │
│  • JARVIS Components                                        │
│  • Droid Actor System                                      │
│  • R5 Living Context Matrix                                │
│  • @v3 Verification                                         │
│  • Workflow Executions                                      │
│  • IDE Integrations                                        │
│  • External APIs                                           │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │   Centralized Logger           │
        │   (Standardized Format)        │
        └───────────────┬───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │   Azure Service Bus            │
        │   Topic: system.logging        │
        │   (Async Pub/Sub)              │
        └───────────────┬───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Live Review │ │ @AIQ Review │ │Jedi-Council │
│  (Front-End)│ │  (Back-End) │ │  (Analysis) │
└─────────────┘ └─────────────┘ └─────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │   Dynamic Tiered Scaling       │
        │   (Live Lookback Analysis)    │
        └───────────────────────────────┘
```

### 1.2 Log Message Structure

```json
{
  "log_id": "uuid",
  "timestamp": "ISO timestamp",
  "source": {
    "app": "lumina|jarvis|r5|v3|droid|workflow",
    "component": "component_name",
    "instance_id": "instance_uuid",
    "tier": "frontend|backend|service|api"
  },
  "level": "DEBUG|INFO|WARNING|ERROR|CRITICAL",
  "message": "Log message",
  "context": {
    "session_id": "session_uuid",
    "workflow_id": "workflow_uuid",
    "user_id": "user_uuid",
    "correlation_id": "correlation_uuid"
  },
  "metadata": {
    "performance": {
      "duration_ms": 123,
      "memory_mb": 45.2,
      "cpu_percent": 12.5
    },
    "environment": {
      "host": "hostname",
      "environment": "dev|staging|prod"
    },
    "tags": ["@lumina", "@jarvis", "#workflow", "#error"]
  },
  "stack_trace": "optional stack trace",
  "escalation_level": 0  // 0-7 (3-5-7 rule)
}
```

---

## Part 2: Live Review System

### 2.1 Front-End Hooks

**Real-Time Dashboard**:
- Live log stream from Azure Service Bus
- Filter by app, component, level, tier
- Real-time metrics and alerts
- Instant replay capability

**Front-End Integration**:
```javascript
// Front-end hook for live log streaming
class LiveLogReviewer {
  constructor(serviceBusClient) {
    this.client = serviceBusClient;
    this.subscription = "frontend-live-review";
  }
  
  subscribeToLogs(filters = {}) {
    // Subscribe to system.logging topic
    this.client.subscribe_to_topic(
      "system.logging",
      this.subscription,
      (logMessage) => {
        if (this.matchesFilters(logMessage, filters)) {
          this.displayLog(logMessage);
          this.updateMetrics(logMessage);
          this.checkEscalation(logMessage);
        }
      }
    );
  }
  
  instantReplay(timeRange, filters = {}) {
    // Query historical logs for replay
    return this.queryLogs(timeRange, filters);
  }
}
```

### 2.2 Back-End Hooks

**Back-End Processing**:
- Log aggregation and analysis
- Pattern detection
- Anomaly detection
- Performance monitoring
- Escalation triggers

**Back-End Integration**:
```python
# Back-end hook for log processing
class BackendLogProcessor:
    def __init__(self, service_bus_client):
        self.client = service_bus_client
        self.subscription = "backend-log-processor"
        
    def subscribe_to_logs(self):
        """Subscribe to logs for processing"""
        self.client.subscribe_to_topic(
            "system.logging",
            self.subscription,
            self.process_log
        )
    
    def process_log(self, log_message: Dict[str, Any]):
        """Process log message"""
        # Analyze log
        analysis = self.analyze_log(log_message)
        
        # Check for patterns
        patterns = self.detect_patterns(log_message)
        
        # Check escalation
        escalation = self.check_escalation(log_message)
        
        # Update metrics
        self.update_metrics(log_message, analysis)
```

---

## Part 3: @AIQ Review System

### 3.1 @AIQ (AI Quorum) System

**Purpose**: AI-driven log analysis and decision-making

**Capabilities**:
- Real-time log analysis
- Pattern recognition
- Anomaly detection
- Predictive analysis
- Decision recommendations
- Escalation suggestions

**@AIQ Integration**:
```python
class AIQReviewSystem:
    def __init__(self, service_bus_client):
        self.client = service_bus_client
        self.subscription = "aiq-review"
        self.ai_models = self.load_ai_models()
        
    def subscribe_to_logs(self):
        """Subscribe to logs for AIQ review"""
        self.client.subscribe_to_topic(
            "system.logging",
            self.subscription,
            self.aiq_review
        )
    
    def aiq_review(self, log_message: Dict[str, Any]):
        """AIQ review of log message"""
        # AI analysis
        analysis = self.ai_analyze(log_message)
        
        # Pattern detection
        patterns = self.detect_ai_patterns(log_message)
        
        # Decision recommendation
        decision = self.recommend_decision(log_message, analysis)
        
        # Escalation check (3-5-7 rule)
        escalation = self.check_escalation_rule(log_message, analysis)
        
        # Publish AIQ review
        self.publish_aiq_review(log_message, analysis, decision, escalation)
```

### 3.2 @AIQ Review Output

```json
{
  "aiq_review_id": "uuid",
  "log_id": "original_log_uuid",
  "timestamp": "ISO timestamp",
  "analysis": {
    "severity": "low|medium|high|critical",
    "category": "performance|error|security|anomaly",
    "confidence": 0.85,
    "patterns_detected": ["pattern1", "pattern2"],
    "anomaly_score": 0.72
  },
  "recommendations": [
    {
      "action": "scale_up",
      "reason": "High CPU usage detected",
      "confidence": 0.88
    }
  ],
  "escalation": {
    "level": 3,
    "reason": "3-5-7 rule triggered",
    "escalate_to": "jedi-council"
  }
}
```

---

## Part 4: Jedi-Council Review System

### 4.1 Jedi-Council (Multi-AI Consensus)

**Purpose**: Multi-AI consensus review for critical decisions

**Composition**:
- Multiple AI models (Iron Legion cluster)
- Consensus voting mechanism
- Escalation coordination
- Final decision authority

**Jedi-Council Integration**:
```python
class JediCouncilReviewSystem:
    def __init__(self, service_bus_client, aiq_system):
        self.client = service_bus_client
        self.aiq = aiq_system
        self.subscription = "jedi-council-review"
        self.council_members = self.load_council_members()  # Multiple AI models
        
    def subscribe_to_escalations(self):
        """Subscribe to escalations from @AIQ"""
        self.client.subscribe_to_topic(
            "aiq.escalations",
            self.subscription,
            self.jedi_council_review
        )
    
    def jedi_council_review(self, escalation_message: Dict[str, Any]):
        """Jedi-Council consensus review"""
        # Get all council member opinions
        opinions = []
        for member in self.council_members:
            opinion = member.review(escalation_message)
            opinions.append(opinion)
        
        # Consensus voting
        consensus = self.vote_consensus(opinions)
        
        # Final decision
        decision = self.make_decision(consensus, escalation_message)
        
        # Publish Jedi-Council decision
        self.publish_jedi_decision(escalation_message, consensus, decision)
```

### 4.2 Jedi-Council Decision Output

```json
{
  "jedi_decision_id": "uuid",
  "escalation_id": "escalation_uuid",
  "timestamp": "ISO timestamp",
  "council_consensus": {
    "vote_count": 5,
    "agreement_percentage": 0.85,
    "majority_decision": "scale_up",
    "member_opinions": [
      {"member": "codellama:13b", "opinion": "scale_up", "confidence": 0.92},
      {"member": "llama3.2:11b", "opinion": "scale_up", "confidence": 0.88},
      {"member": "mixtral-8x7b", "opinion": "scale_up", "confidence": 0.95}
    ]
  },
  "final_decision": {
    "action": "scale_up",
    "target_tier": "backend",
    "scale_factor": 1.5,
    "confidence": 0.92,
    "reasoning": "Consensus: High CPU usage requires scaling"
  },
  "execution": {
    "status": "approved",
    "executor": "dynamic-scaling-system",
    "estimated_completion": "2025-01-27T12:00:00Z"
  }
}
```

---

## Part 5: 3-5-7 Escalation Rule

### 5.1 Escalation Levels

**3-5-7 Rule**: Progressive escalation based on severity and consensus

```
Level 0: No escalation (handled locally)
Level 1: Component-level review
Level 2: System-level review
Level 3: @AIQ review (AI analysis)
Level 4: @AIQ + Pattern detection
Level 5: Jedi-Council review (multi-AI consensus)
Level 6: Jedi-Council + Human oversight
Level 7: Critical escalation (human intervention required)
```

### 5.2 Escalation Triggers

```python
class EscalationRule357:
    def check_escalation(self, log_message: Dict[str, Any], analysis: Dict[str, Any]) -> int:
        """Determine escalation level using 3-5-7 rule"""
        escalation_level = 0
        
        # Level 3: @AIQ Review
        if analysis.get("severity") in ["high", "critical"]:
            escalation_level = 3
        elif analysis.get("anomaly_score", 0) > 0.7:
            escalation_level = 3
        
        # Level 5: Jedi-Council Review
        if escalation_level == 3:
            if analysis.get("confidence", 0) < 0.8:
                escalation_level = 5  # Need consensus
            elif analysis.get("patterns_detected", []):
                if len(analysis["patterns_detected"]) > 2:
                    escalation_level = 5  # Multiple patterns need consensus
        
        # Level 7: Critical (Human Intervention)
        if analysis.get("severity") == "critical":
            if analysis.get("impact_score", 0) > 0.9:
                escalation_level = 7  # Critical - human required
        
        return escalation_level
```

### 5.3 Escalation Flow

```
Log Event → Level 0 (Local)
    ↓ (if severity > threshold)
Level 3 (@AIQ Review)
    ↓ (if confidence < 0.8 or multiple patterns)
Level 5 (Jedi-Council Review)
    ↓ (if critical severity + high impact)
Level 7 (Human Intervention)
```

---

## Part 6: Dynamic Tiered Scaling with Live Lookback

### 6.1 Tiered Scaling Architecture

**Tiers**:
- **Tier 1**: Front-End (UI, widgets, dashboards)
- **Tier 2**: Back-End Services (APIs, processing)
- **Tier 3**: Data Layer (databases, caches)
- **Tier 4**: Infrastructure (compute, storage, network)

### 6.2 Live Lookback Analysis

**Lookback Windows**:
- **Real-Time**: Last 1 minute
- **Short-Term**: Last 5 minutes
- **Medium-Term**: Last 15 minutes
- **Long-Term**: Last 1 hour
- **Historical**: Last 24 hours

**Lookback Analysis**:
```python
class DynamicTieredScaling:
    def __init__(self, service_bus_client):
        self.client = service_bus_client
        self.lookback_windows = {
            "realtime": 60,      # 1 minute
            "short": 300,        # 5 minutes
            "medium": 900,       # 15 minutes
            "long": 3600,        # 1 hour
            "historical": 86400  # 24 hours
        }
        
    def analyze_live_lookback(self, tier: str, window: str = "medium"):
        """Analyze logs with live lookback"""
        lookback_seconds = self.lookback_windows[window]
        cutoff_time = datetime.now() - timedelta(seconds=lookback_seconds)
        
        # Query logs from Azure Service Bus (with lookback)
        logs = self.query_logs(
            tier=tier,
            start_time=cutoff_time,
            end_time=datetime.now()
        )
        
        # Analyze metrics
        metrics = self.calculate_metrics(logs)
        
        # Determine scaling action
        scaling_action = self.determine_scaling_action(metrics, tier)
        
        return scaling_action
    
    def determine_scaling_action(self, metrics: Dict, tier: str) -> Dict:
        """Determine scaling action based on metrics"""
        cpu_avg = metrics.get("cpu_avg", 0)
        memory_avg = metrics.get("memory_avg", 0)
        error_rate = metrics.get("error_rate", 0)
        latency_p95 = metrics.get("latency_p95", 0)
        
        # Scaling thresholds
        if cpu_avg > 80 or memory_avg > 85 or error_rate > 0.05:
            return {
                "action": "scale_up",
                "tier": tier,
                "scale_factor": 1.5,
                "reason": f"High resource usage: CPU={cpu_avg}%, Memory={memory_avg}%, Errors={error_rate}"
            }
        elif cpu_avg < 30 and memory_avg < 40 and error_rate < 0.01:
            return {
                "action": "scale_down",
                "tier": tier,
                "scale_factor": 0.75,
                "reason": f"Low resource usage: CPU={cpu_avg}%, Memory={memory_avg}%, Errors={error_rate}"
            }
        else:
            return {
                "action": "maintain",
                "tier": tier,
                "reason": "Resource usage within normal range"
            }
```

### 6.3 Live Lookback via Azure Service Bus

**Service Bus Topics for Lookback**:
- `system.logging.realtime` - Real-time logs (1 minute lookback)
- `system.logging.short` - Short-term logs (5 minutes lookback)
- `system.logging.medium` - Medium-term logs (15 minutes lookback)
- `system.logging.long` - Long-term logs (1 hour lookback)
- `system.logging.historical` - Historical logs (24 hours lookback)

**Lookback Query**:
```python
def query_logs_lookback(
    tier: str,
    window: str,
    filters: Dict[str, Any] = None
) -> List[Dict[str, Any]]:
    """Query logs with live lookback from Azure Service Bus"""
    topic_name = f"system.logging.{window}"
    subscription_name = f"lookback-{tier}-{window}"
    
    # Subscribe to topic with lookback window
    logs = []
    service_bus_client.subscribe_to_topic(
        topic_name,
        subscription_name,
        lambda msg: logs.append(msg) if matches_filters(msg, filters, tier) else None
    )
    
    return logs
```

---

## Part 7: Integration Points

### 7.1 Front-End Integration

**Hooks**:
- Real-time log streaming
- Live metrics dashboard
- Instant replay interface
- Escalation alerts
- Scaling status display

### 7.2 Back-End Integration

**Hooks**:
- Log aggregation
- Pattern detection
- Anomaly detection
- Performance monitoring
- Escalation processing
- Scaling execution

### 7.3 Azure Service Bus Topics

**Topics**:
- `system.logging` - All logs (main topic)
- `system.logging.realtime` - Real-time logs
- `system.logging.short` - Short-term logs
- `system.logging.medium` - Medium-term logs
- `system.logging.long` - Long-term logs
- `system.logging.historical` - Historical logs
- `aiq.reviews` - @AIQ review results
- `jedi-council.decisions` - Jedi-Council decisions
- `scaling.actions` - Scaling actions

**Queues**:
- `log-processing-queue` - Log processing
- `aiq-review-queue` - @AIQ review queue
- `jedi-council-queue` - Jedi-Council review queue
- `scaling-execution-queue` - Scaling execution queue

---

## Part 8: Implementation Status

### Current State

**✅ Defined**:
- Azure Service Bus architecture
- Log message structure
- @AIQ system concept
- Jedi-Council concept
- 3-5-7 escalation rule
- Dynamic tiered scaling concept

**⚠️ Pending Implementation**:
- Centralized logging integration
- Live review front-end hooks
- @AIQ review system implementation
- Jedi-Council review system implementation
- 3-5-7 escalation rule implementation
- Dynamic tiered scaling with live lookback

---

## Part 9: Next Steps

### Priority 1: Centralized Logging
1. Integrate all apps/systems with Azure Service Bus logging
2. Standardize log message format
3. Create logging topics and subscriptions

### Priority 2: Live Review System
1. Implement front-end hooks for live log streaming
2. Implement back-end hooks for log processing
3. Create instant replay capability

### Priority 3: @AIQ & Jedi-Council
1. Implement @AIQ review system
2. Implement Jedi-Council consensus system
3. Integrate with Iron Legion cluster

### Priority 4: 3-5-7 Escalation
1. Implement escalation rule logic
2. Create escalation topics and queues
3. Integrate with @AIQ and Jedi-Council

### Priority 5: Dynamic Tiered Scaling
1. Implement live lookback analysis
2. Create scaling decision engine
3. Integrate with Azure Service Bus for lookback queries

---

**Status**: ✅ **ARCHITECTURE DEFINED**  
**Tag**: `@triage` `#logging` `#azure-bus` `#live-reviews` `@aiq` `#jedi-council` `#3-5-7-escalation`  
**Last Updated**: 2025-01-27  
**Maintained By**: Cedarbrook Financial Services LLC


