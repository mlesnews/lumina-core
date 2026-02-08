# Kenny Roast and Repair (RR) System

## Overview

**#RR** - Rest, Roast, and Repair technique for granular focus in Kenny development.

A systematic approach to developing Kenny into the JARVIS we want, using a three-phase process:

1. **REST**: Pause, observe, analyze current state
2. **ROAST**: Critically identify issues, problems, gaps
3. **REPAIR**: Fix issues systematically, one at a time

## Purpose

Enable granular focus on Kenny's development by:
- Systematically identifying issues across all categories
- Prioritizing fixes by severity
- Tracking repair progress
- Building a knowledge base of issues and solutions

## Usage

### Basic Workflow

```python
from kenny_roast_and_repair import KennyRoastAndRepair, RoastCategory

rr = KennyRoastAndRepair()

# 1. REST: Observe current state
session = rr.rest("Analyzing Kenny's visual and behavioral state")

# 2. ROAST: Identify issues
rr.roast(
    RoastCategory.VISUAL,
    "Kenny appears as orange Froot Loop instead of solid circle",
    severity="high",
    evidence=["Programmatic analysis shows 96.8% ring ratio"]
)

rr.roast(
    RoastCategory.BEHAVIORAL,
    "Kenny stops moving after initial movement",
    severity="medium",
    evidence=["User reports Kenny 'came to rest in bottom right corner'"]
)

# 3. REPAIR: Fix issues
rr.repair(repair_action="Implemented component-based design system")

# Save session
rr.save_session()
```

### Categories

- **VISUAL**: Appearance, sprite, rendering
- **BEHAVIORAL**: Movement, actions, state machine
- **FUNCTIONAL**: Features, capabilities
- **INTEGRATION**: Collaboration, ecosystem
- **PERFORMANCE**: Speed, responsiveness
- **QUALITY**: Bugs, errors, edge cases

### Severity Levels

- **critical**: Blocks core functionality
- **high**: Significant impact on user experience
- **medium**: Noticeable but workaround exists
- **low**: Minor issue, cosmetic

## Integration with Kenny Development

The RR system helps systematically develop Kenny by:

1. **Identifying Issues**: Granular focus on specific problems
2. **Prioritizing Fixes**: By severity and category
3. **Tracking Progress**: Session-based tracking of issues and repairs
4. **Building Knowledge**: Historical record of issues and solutions

## Short Tag

**#RR** - Use in chat to reference Roast and Repair workflow

Examples:
- `#RR Rest: Let's observe Kenny's current state`
- `#RR Roast: What issues do we see?`
- `#RR Repair: Fix the Froot Loop issue`

## Module

- **File**: `scripts/python/kenny_roast_and_repair.py`
- **Class**: `KennyRoastAndRepair`
- **Data**: `data/kenny_rr_sessions/`

## Status

✅ **System Created**: Ready for use
✅ **Short Tag Added**: #RR registered
✅ **Documentation**: Complete

---

**Last Updated**: 2025-01-05
**Purpose**: Granular focus for developing Kenny into JARVIS
