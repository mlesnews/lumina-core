# JARVIS Threat & Criticality-Based Routing System - LUMINA-WIDE

**Date:** 2026-01-17  
**Status:** ✅ **ACTIVE**  
**Tags:** `#DECISIONING_SYSTEM` `#THREAT` `#CRITICALITY` `#ROUTING` `#LUMINA` `#ULTRON` `#IRON_LEGION` `#METRICS`

---

## 🎯 Purpose

Routes decisions across **all LUMINA clusters** (ULTRON, Iron Legion, MILLENNIUM_FALCON, etc.) based on **threat**, **criticality**, **severity**, **intensity**, **temperature**, and other metrics. Tracks metrics over time for analysis.

**This is LUMINA-wide routing, not specific to Iron Legion or KAIJU.**

---

## 🛡️ Routing Logic

### Priority Levels

1. **Low Priority** → **JARVIS solves solo** (no Iron Legion)
   - Metrics < 0.3
   - Simple tasks JARVIS can handle independently

2. **Medium Priority** → **JARVIS solves solo OR engages agents/clusters**
   - Metrics 0.3-0.6
   - JARVIS decides based on intensity/temperature:
     - Higher intensity/temperature → Engage clusters (ULTRON Local, MILLENNIUM_FALCON, Mark III, Mark VII)
     - Lower intensity → JARVIS solo

3. **High/Critical Priority** → **Requires 3-5-7-9 escalation**
   - Metrics >= 0.6
   - Routes to appropriate clusters/nodes based on escalation level:
     - **Level 3** (Low escalation) → ULTRON Local, Mark III, Mark VII (AIQ consensus)
     - **Level 5** (Medium escalation) → ULTRON KUBE, Iron Legion, Mark II, Mark IV (JC standard)
     - **Level 7** (High escalation) → ULTRON Cluster, Iron Legion, Mark I, Mark V (JC urgent)
     - **Level 9** (Critical escalation) → ULTRON Cluster, Iron Legion, Mark VI (JHC critical)

---

## 📊 Metrics Tracked

The system tracks the following metrics over time:

- **Criticality** (0.0-1.0): How critical the situation is
- **Threat Level** (0.0-1.0): Severity of threat
- **Severity** (0.0-1.0): Overall severity assessment
- **Intensity** (0.0-1.0): Intensity of the situation
- **Temperature** (0.0-1.0): Urgency/heat of the situation
- **Customer Impact** (0.0-1.0): Impact on customers (HIGHEST PRIORITY - 15% weight)
- **Risk Score** (0.0-1.0): Overall risk assessment
- **Custom Metrics**: Additional metrics as needed

### Metric Weights

- Criticality: 25%
- Threat Level: 20%
- Severity: 15%
- Intensity: 10%
- Temperature: 10%
- **Customer Impact: 15%** (Higher weight - highest priority)
- Risk Score: 5%

---

## 🔄 Integration with SYPHON Escalation

The system integrates with **SYPHON Threat & Risk Escalation** for 3-5-7-9 escalation:

- **Level 3**: Low escalation → AIQ consensus → Mark III, Mark VII
- **Level 5**: Medium escalation → JC standard → Mark II, Mark IV
- **Level 7**: High escalation → JC urgent → Mark I, Mark V
- **Level 9**: Critical escalation → JHC critical → Mark VI

---

## 📋 Usage

### Basic Routing

```python
from scripts.python.jarvis_threat_criticality_routing import JARVISThreatCriticalityRouter

router = JARVISThreatCriticalityRouter()

# Assess metrics
metrics = router.assess_metrics(
    criticality=0.7,
    threat_level=0.6,
    severity=0.5,
    intensity=0.4,
    temperature=0.3,
    customer_impact=0.8,
    risk_score=0.5
)

# Route decision
decision = router.route_decision(metrics)

print(f"Routing: {decision.routing.value}")
print(f"Target Cluster: {decision.target_cluster}")
print(f"Target Node: {decision.target_node}")
print(f"Endpoint: {decision.target_endpoint}")
print(f"Reasoning: {decision.reasoning}")
```

### With SYPHON Assessments

```python
from scripts.python.syphon_threat_risk_escalation import (
    CustomerImpactAssessment,
    CustomerImpactLevel,
    ThreatAssessment,
    ThreatSeverity
)

# Create assessments
customer_impact = CustomerImpactAssessment(
    impact_id="impact_001",
    level=CustomerImpactLevel.HIGH,
    description="Service degradation affecting customers",
    affected_customers=500
)

threat = ThreatAssessment(
    threat_id="threat_001",
    threat_type="security",
    severity=ThreatSeverity.MEDIUM,
    description="Potential security issue",
    confidence=0.7
)

# Assess and route
metrics = router.assess_metrics(
    customer_impact_obj=customer_impact,
    threat_assessment=threat
)

decision = router.route_decision(
    metrics,
    customer_impact_obj=customer_impact,
    threat_assessment=threat
)
```

### Get Metrics Over Time

```python
# Get metrics for last 7 days
metrics_data = router.get_metrics_over_time(days=7)

# Get specific metric over time
criticality_data = router.get_metrics_over_time(days=30, metric_name="criticality")
```

---

## 🎯 Cluster & Node Mapping

### By Priority

- **Low**: None (JARVIS solo)
- **Medium**: ULTRON Local, MILLENNIUM_FALCON, Mark III (Quick), Mark VII (Fallback)
- **High**: ULTRON KUBE, Iron Legion, Mark II (General), Mark IV (Balanced), Mark V (Reasoning)
- **Critical**: ULTRON Cluster, Iron Legion, Mark I (Code Expert), Mark VI (Complex Expert)

### By Escalation Level

- **Level 3**: ULTRON Local, Mark III, Mark VII (AIQ consensus)
- **Level 5**: ULTRON KUBE, Iron Legion, Mark II, Mark IV (JC standard)
- **Level 7**: ULTRON Cluster, Iron Legion, Mark I, Mark V (JC urgent)
- **Level 9**: ULTRON Cluster, Iron Legion, Mark VI (JHC critical)

### Available Clusters

- **ULTRON Local**: `http://localhost:11434`
- **ULTRON KUBE**: `http://localhost:11435`
- **ULTRON Cluster**: `http://localhost:11436`
- **Iron Legion**: `http://10.17.17.11:3000`
- **Iron Legion Mark I-VII**: `http://10.17.17.11:3001-3007`
- **MILLENNIUM_FALCON**: `http://localhost:11436`

---

## 📈 Metrics Tracking

All metrics are tracked over time and saved to:
- `data/jarvis_routing/metrics_history.jsonl`
- `data/jarvis_routing/routing_history.jsonl`

Metrics retention: 90 days (configurable)

---

## 🔗 Related Systems

- `syphon_threat_risk_escalation.py` - SYPHON 3-5-7-9 escalation
- `lumina_decisioning_engine.py` - Core decisioning engine
- `ultron_cluster_selection.json` - ULTRON cluster configuration
- `iron_legion_cluster_config.json` - Iron Legion configuration
- `iron_legion_experts_config.json` - Expert node definitions

---

## 🎯 Best Practices

1. **Customer Impact First**: Customer impact has highest priority (15% weight)
2. **Track Metrics**: All metrics are tracked over time for analysis
3. **Escalation Integration**: Use SYPHON escalation for high/critical priorities
4. **Mark Node Selection**: Choose appropriate Mark node based on escalation level
5. **Custom Metrics**: Add custom metrics as needed for specific use cases

---

**Status:** ✅ **JARVIS THREAT & CRITICALITY ROUTING SYSTEM ACTIVE - LUMINA-WIDE**

**Power Recognition:** JARVIS routes decisions across all LUMINA clusters (ULTRON, Iron Legion, MILLENNIUM_FALCON, etc.) based on threat, criticality, and metrics, with automatic escalation to appropriate clusters and nodes.
