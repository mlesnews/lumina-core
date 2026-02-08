# Bridge Executive Command Deck - Quick Reference

**Naval/Maritime Tactical Warfare Command Center**

---

## 🚀 Quick Start

```python
from bridge_executive_command_deck import (
    BridgeExecutiveCommandDeck,
    BridgeStation,
    OperationalDomain,
    TacticalStatus
)

# Initialize Bridge
bridge = BridgeExecutiveCommandDeck()

# Get status
status = bridge.get_bridge_status_display()
```

---

## 📢 Bridge Orders

### Issue Order

```python
order = bridge.issue_bridge_order(
    station=BridgeStation.CAPTAIN,  # or TACTICAL_OFFICER, etc.
    order_type="tactical",
    command="Engage defensive posture",
    parameters={"priority": "high"},
    priority=8
)
```

### Bridge Stations

- **CAPTAIN**: Executive command
- **TACTICAL_OFFICER**: Tactical operations
- **NAVIGATION_OFFICER**: Navigation
- **COMMUNICATIONS_OFFICER**: Communications
- **ENGINEERING_OFFICER**: Systems
- **INTELLIGENCE_OFFICER**: Intelligence
- **WEAPONS_OFFICER**: Operations
- **SCIENCE_OFFICER**: Analysis

---

## 🚨 Tactical Assessment

### Assess Situation

```python
situation = bridge.assess_tactical_situation(
    domain=OperationalDomain.SPACE,
    description="Threat detected",
    threats=["Unknown vessel"],
    assets=["Defense systems"]
)
```

### Operational Domains

- **TERRESTRIAL**: Earth operations
- **MARITIME**: Ocean/sea operations
- **AEROSPACE**: Air/space operations
- **SPACE**: Space operations
- **DEEP_SPACE**: Deep space operations

### Tactical Status

- **GREEN**: All clear
- **YELLOW**: Caution
- **ORANGE**: Alert
- **RED**: Critical
- **BLACK**: Emergency

---

## 🌍 Domain Operations

### Set Domain

```python
bridge.set_operational_domain(OperationalDomain.SPACE)
```

---

## 📊 Status Display

```python
status = bridge.get_bridge_status_display()
# Returns: domain, tactical_status, stations, active_orders, threats, etc.
```

---

## 🔗 Integration

- **Command & Control**: Tactical operations
- **Governance**: Executive decisions
- **Communications**: All communications
- **Intelligence**: Data collection

---

**Tags:** #BRIDGE #QUICK_REFERENCE #NAVAL #TACTICAL #COMMAND
