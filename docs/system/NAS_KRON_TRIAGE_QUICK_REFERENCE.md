# NAS @KRONSCHEDULER @TRIAGE/@BAU - Quick Reference

**Quick lookup for coordinated scheduled events**

---

## 🎯 Priority Levels

| Priority | Icon | Schedule Alignment | Window | Strategy |
|----------|------|-------------------|--------|----------|
| **CRITICAL** | 🔴 | Keep original | 0-15 min | Parallel |
| **HIGH** | 🟠 | :00, :15, :30, :45 | 0-30 min | Batch |
| **MEDIUM** | 🟡 | :00, :30 | 0-60 min | Batch |
| **LOW** | 🟢 | :00 | 0-60 min | Sequence |

---

## 📦 BAU Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Critical** | Watchdog, security | Watchdog, Guarddog, Security checks |
| **Standard** | Daily operations | Daily work cycle, Routine tasks |
| **Maintenance** | Updates, cleanup | Extension updates, Cleanup |
| **Monitoring** | Health checks | Connection health, Performance |

---

## 🚀 Quick Commands

### Coordinate Events
```bash
python scripts/python/nas_kron_triage_coordinator.py --coordinate
```

### @SYPHON Analysis
```bash
python scripts/python/nas_kron_triage_coordinator.py --syphon
```

### Generate Schedule
```bash
python scripts/python/nas_kron_triage_coordinator.py --generate-schedule
```

### List Events
```bash
python scripts/python/nas_kron_triage_coordinator.py --list-events
```

### List Groups
```bash
python scripts/python/nas_kron_triage_coordinator.py --list-groups
```

---

## 🔄 Coordination Flow

```
1. @SYPHON extracts patterns
2. Apply TRIAGE/BAU priorities
3. Align schedules to coincide
4. Apply dynamic scaling
5. Create collation groups
6. Generate coordinated schedule
```

---

## 📊 Schedule Alignment Examples

### Before
```
0 2 * * *     (2 AM)
0 3 * * *     (3 AM)
*/15 * * * *  (Every 15 min)
```

### After (Coordinated)
```
0 2 * * *           (2 AM - MEDIUM)
0,30 2 * * *        (2:00, 2:30 - HIGH)
0,15,30,45 * * * *  (Every 15 min - HIGH)
```

---

## 🎯 Collation Group Strategies

| Strategy | Use Case | Execution |
|----------|----------|-----------|
| **Parallel** | CRITICAL events | Run simultaneously |
| **Batch** | 2-3 events | Run together |
| **Sequence** | 4+ events | Run in order |

---

**Tags:** #NAS #KRONSCHEDULER #TRIAGE #BAU #QUICK_REFERENCE @JARVIS @LUMINA
