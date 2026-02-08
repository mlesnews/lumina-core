# RoamWise Atlas - Quick Reference

**Hybrid WOW-Atlas/DEFCON Global Map Quick Lookup**

---

## 🎯 Top 3 Essential Threats

| # | Threat | DEFCON | Type | Threat Score | Ambush | Blindside |
|---|--------|--------|------|--------------|--------|-----------|
| 1 | **TRIAGE Cascade Failure** | ⚫ 1 | 🎯 AMBUSH | 95% | 85% | 75% |
| 2 | **PROCESS Deadlock** | ⚫ 1 | 👁️ BLINDSIDE | 90% | 80% | 70% |
| 3 | **@CoA Coordination Breakdown** | ⚫ 1 | 🔗 COORDINATION_GAP | 98% | 90% | 85% |

---

## 🗺️ DEFCON Levels

| Level | Icon | Status | Threat Level |
|-------|------|--------|--------------|
| DEFCON 5 | 🟢 | Normal readiness | Safe |
| DEFCON 4 | 🟡 | Increased readiness | Low |
| DEFCON 3 | 🟠 | Increased above normal | Moderate |
| DEFCON 2 | 🔴 | Next step to nuclear war | High |
| DEFCON 1 | ⚫ | Maximum readiness | Critical |

---

## 🎯 Hot-Spot Types

| Type | Icon | Description | Risk |
|------|------|-------------|------|
| AMBUSH | 🎯 | High ambush potential | Surprise attack |
| BLINDSIDE | 👁️ | High blindside potential | Side/rear attack |
| DEAD_END | 🚫 | Path termination | No progress |
| MISDIRECTION | 🔀 | Wrong direction | Off-course |
| PITFALL | ⚠️ | Subtle trap | Hidden danger |
| FORK | 🍴 | Multiple paths | Decision point |
| COORDINATION_GAP | 🔗 | Agent coordination failure | Breakdown |

---

## 🏔️ Terrain Types

| Terrain | Icon | Elevation | Threat Level | Use Case |
|---------|------|-----------|--------------|----------|
| HIGH_GROUND | ⛰️ | High (Z: 80-100) | Low | Optimal paths |
| PLATEAU | 🏔️ | Medium (Z: 50-80) | Moderate | Standard ops |
| VALLEY | 🏞️ | Low (Z: 25-50) | Elevated | Challenging |
| RAVINE | 🕳️ | Very Low (Z: 0-25) | High | Danger zones |

---

## 📊 Quick Commands

### Visualize Atlas
```bash
# ASCII (default)
python scripts/python/roamwise_atlas_visualization.py --visualize

# JSON
python scripts/python/roamwise_atlas_visualization.py --visualize --format json

# Markdown
python scripts/python/roamwise_atlas_visualization.py --visualize --format markdown
```

### Get Threats
```bash
python scripts/python/roamwise_atlas_visualization.py --get-threats
```

### Journal Event
```bash
python scripts/python/roamwise_atlas_visualization.py \
  --journal "action" "Title" "Description" "tag1,tag2,tag3"
```

---

## 🛡️ Cover-Our-Arses Checklist

### For TRIAGE Cascade Failure
- [ ] Priority validation layer
- [ ] Routing redundancy
- [ ] Agent availability checks
- [ ] Failure rate monitoring
- [ ] Human intervention capability

### For PROCESS Deadlock
- [ ] Pre-execution dependency validation
- [ ] Timeout enforcement
- [ ] Cycle detection
- [ ] Force unlock mechanism
- [ ] Process isolation capability

### For @CoA Coordination Breakdown
- [ ] Agent health monitoring
- [ ] Communication redundancy
- [ ] State verification
- [ ] Conflict detection
- [ ] Graceful degradation
- [ ] Complete action logging

---

## 🔍 Path Analysis Quick Lookup

### Risk Levels

| Ambush Risk | Blindside Risk | Action |
|-------------|----------------|--------|
| >70% | >70% | 🔴 CRITICAL - Add validation, check dependencies |
| 50-70% | 50-70% | 🟠 HIGH - Add checkpoints, validate assumptions |
| <50% | <50% | 🟢 SAFE - Standard monitoring |

### Path Issues

| Issue | Detection | Mitigation |
|-------|-----------|------------|
| **Fork** | Multiple paths from node | Decision point, choose optimal |
| **Dead-End** | No connections from node | Backtrack, find alternate path |
| **Misdirection** | Tag mismatch | Verify tags, correct course |
| **Pitfall** | High threat in moderate terrain | Add validation, increase monitoring |

---

## 📋 Layer Quick Reference

### Layer 1: Operational Terrain
- **Purpose:** Operational path mapping
- **Nodes:** @JARVIS, @DOIT, @RR, @TRIAGE, @PROCESS, @CoA
- **Focus:** Execution paths, workflow

### Layer 2: Threat Topography
- **Purpose:** Threat level mapping
- **Nodes:** Threat hot-spots, danger zones
- **Focus:** DEFCON levels, threat scores

### Layer 3: Inference Network
- **Purpose:** Decision and validation nodes
- **Nodes:** Decision points, validation checkpoints
- **Focus:** Logic flow, validation

### Layer 4: Agent Deployment
- **Purpose:** @CoA organization
- **Nodes:** Agent positions, coordination points
- **Focus:** Agent coordination, delegation

---

## 🎯 Threat #1: TRIAGE Cascade Failure

**Location:** (25.0, 25.0, 30.0)  
**Affected:** @TRIAGE, @DOIT, @JARVIS

**Quick Mitigation:**
1. Enable fallback priority system
2. Activate redundant routing
3. Check agent availability
4. Monitor failure rate
5. Prepare manual override

---

## 🎯 Threat #2: PROCESS Deadlock

**Location:** (35.0, 35.0, 20.0)  
**Affected:** @PROCESS, @CoA, @AI2AI

**Quick Mitigation:**
1. Run deadlock detection
2. Check timeouts
3. Validate dependencies
4. Prepare break-glass protocol
5. Isolate if needed

---

## 🎯 Threat #3: @CoA Coordination Breakdown

**Location:** (15.0, 15.0, 10.0)  
**Affected:** @CoA, @AI2AI, @AGENT2AGENT, @JARVIS

**Quick Mitigation:**
1. Check agent heartbeats
2. Sync agent states
3. Resolve conflicts
4. Isolate failing agents
5. Prepare emergency shutdown
6. Enable audit trail

---

**Tags:** #ROAMWISE #ATLAS #QUICK_REFERENCE #DEFCON #THREATS #TRIAGE #PROCESS #CoA @JARVIS @LUMINA
