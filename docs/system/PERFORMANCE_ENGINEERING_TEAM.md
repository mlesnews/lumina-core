# Performance Engineering & Capacity Management Team (DYNO-PE)

**Mission**: Find and maintain optimal performance across the unified compute fabric through systematic testing, measurement, and tuning.

## Team Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│              PERFORMANCE ENGINEERING TEAM (DYNO-PE)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    PE-LEAD: JARVIS-PE                          │ │
│  │     Performance Strategy | DYNO Authorization | Capacity Plan  │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                              │                                      │
│     ┌────────────────────────┼────────────────────────┐            │
│     │                        │                        │            │
│     ▼                        ▼                        ▼            │
│ ┌──────────┐          ┌──────────────┐         ┌──────────────┐   │
│ │UATU-     │          │PROVING-      │         │GOLDILOCKS    │   │
│ │METRICS   │          │GROUND        │         │(PE-TUNE)     │   │
│ │Analyst   │          │Stress Tester │         │Tuner         │   │
│ └──────────┘          └──────────────┘         └──────────────┘   │
│     │                        │                        │            │
│     └────────────────────────┼────────────────────────┘            │
│                              ▼                                      │
│                    ┌──────────────────┐                            │
│                    │   V3-VERIFY      │                            │
│                    │   QA Validator   │                            │
│                    └──────────────────┘                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## The Goldilocks Zone

**Definition**: The optimal operating range where the system is neither overloaded (TOO_HOT) nor underutilized (TOO_COLD).

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GOLDILOCKS ZONE SPECTRUM                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  🥶 TOO_COLD          🐻 GOLDILOCKS           🔥 TOO_HOT           │
│  ──────────────────────────────────────────────────────────────    │
│  |        |                |    ████████████████    |        |     │
│  0%      25%              40%         55%         70%      100%    │
│           ▲                           ▲                     ▲      │
│     MIN VIABLE              OPTIMAL TARGET          MAX SAFE       │
│                                                                     │
│  Indicators:                                                        │
│  ───────────                                                        │
│  TOO_COLD:     CPU < 20%, Memory < 30%, Cursor < 1000MB            │
│  GOLDILOCKS:   CPU 40-70%, Memory 40-60%, Cursor 2000-4000MB       │
│  TOO_HOT:      CPU > 85%, Memory > 80%, Cursor > 6000MB            │
│                OR any ECONNRESET errors                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## DYNO Testing Framework

### Phase 1: BASELINE (Current State)
- Establish performance metrics at 50% capacity
- Duration: 24 hours of stable operation
- Success: Zero ECONNRESET errors

### Phase 2: RAMP_UP (Find MAX)
- Gradually increase load: 60% → 70% → 80% → 90% → 100%
- Hold each level for 30 minutes
- Identify breaking point

### Phase 3: RAMP_DOWN (Find MIN)
- Decrease load: 50% → 40% → 30% → 25% → 20%
- Identify minimum functional capacity

### Phase 4: GOLDILOCKS_CALIBRATION
- Calculate optimal = (MIN + MAX) / 2 with 20% headroom
- Fine-tune configuration

### Phase 5: BURN_IN
- Extended 48-hour test at Goldilocks capacity
- Production-like workload
- Must pass with zero errors

## Commands

```powershell
# Check current status
python scripts/python/dyno_performance_test.py --status

# Run baseline test (5 minutes)
python scripts/python/dyno_performance_test.py --mode baseline --duration 5

# Run ramp-up test
python scripts/python/dyno_performance_test.py --mode ramp_up

# Calibrate Goldilocks zone
python scripts/python/dyno_performance_test.py --mode calibrate

# Full test sequence
python scripts/python/dyno_performance_test.py --mode full

# Emergency abort (reset to 50%)
python scripts/python/dyno_performance_test.py --abort

# Generate report
python scripts/python/dyno_performance_test.py --report
```

## D&D Min-Maxing Framework

**LUMINA Principle**: *Reuse old logic, apply to new situations*

Just like optimizing a D&D character build:
- **Dump Stats**: Resources we can minimize without breaking functionality
- **Primary Stats**: Critical resources that must be maximized
- **Character Build**: System configuration tuned for optimal performance

### Stat Mappings

| D&D Stat | System Resource | Goldilocks Range |
|----------|-----------------|------------------|
| **STR** | CPU Capacity | 40-70% |
| **CON** | Memory (Cursor) | 2000-4000 MB |
| **DEX** | Response Time | 50-200 ms |
| **INT** | AI Tokens/sec | 20-100 tps |
| **WIS** | Error Handling | 0 errors/hour |
| **CHA** | User Experience | Smooth/Instant |

### Observed Baselines

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT CAPACITY DISCOVERY                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  OBSERVED:  5 concurrent agents = practical comfort MAX             │
│                                                                     │
│  VARIANCE:  HIGH - single request can spawn many sub-agents         │
│                                                                     │
│  INTENSITY SPECTRUM:                                                │
│  ─────────────────────────────────────────────────────────────────  │
│  |  MIN: Light request     |████████████████████| MAX: Heavy + subs │
│  |  (minimal resources)    |      UNKNOWN       | (needs discovery) │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Recovery Modes (D&D Analogy)

| D&D Rest Type | System Action | Recovery Level |
|---------------|---------------|----------------|
| **Long Rest** | Full Cursor restart | Full HP restore |
| **Short Rest** | Window reload (`Ctrl+Shift+P`) | Hit dice healing |
| **Hit Dice** | Surgical optimization (`-KillHeavy`) | Partial recovery |

## Bank Terminology Mapping

| LUMINA Term | Bank/Enterprise Term |
|-------------|---------------------|
| Performance Engineering Team | Capacity Management / Performance CoE |
| DYNO Mode | Load Testing / Stress Testing |
| Goldilocks Zone | Optimal Operating Range / Target Utilization |
| Burn-in Testing | Soak Testing / Endurance Testing |
| Ramp Up | Load Ramp / Stepped Load Test |
| Baseline | Performance Baseline / Reference Benchmark |
| TOO_HOT | Capacity Breach / Resource Exhaustion |
| TOO_COLD | Underutilized / Over-provisioned |
| Min-Maxing | Optimization Analysis / Constraint Tuning |

## Integration Points

- **System Capacity Governor**: `config/system_capacity.json`
- **Health Check System**: `scripts/python/lumina_debug_health_check.py`
- **Cursor Recovery**: `scripts/cursor_health_recovery.ps1`
- **ULTRON Cluster**: `config/ultron_cluster_selection.json`

## Current Status

**As of 2026-01-13:**
- Mode: PERFORMANCE_TUNING (50%)
- DYNO Ready: ❌ NO
- Blocking Items:
  - NAS Migration: 🟡 PARTIAL
  - Spacehog Battle: ⏳ PENDING
  - ECONNRESET 24h Zero: 🔴 RED (errors occurring)
  - ULTRON Cluster: 🟡 YELLOW
