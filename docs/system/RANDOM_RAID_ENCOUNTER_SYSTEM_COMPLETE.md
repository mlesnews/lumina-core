# Random Raid Encounter System - Complete

**Status:** ✅ **IMPLEMENTED**
**Date:** 2026-01-09
**Version:** V3.2

---

## Summary

Implemented random outlier fight system with macro raids and low spawn rate.
Special handling for lightsaber duels (half probability unless Force user from Star Wars).

---

## Features

### 1. Random Encounter Spawning

**Base Spawn Rates:**
- **Base Spawn Rate:** 0.1% (0.001 probability)
- **Lightsaber Duel Rate:** 0.05% (0.0005 probability) - Half of base
- **Force User Lightsaber Rate:** 0.2% (0.002 probability) - Higher for Force users

**Encounter Types:**
- **MACRO_RAID** - Large-scale raid encounters
- **LIGHTSABER_DUEL** - Lightsaber duels (Force users)
- **COMBAT_ENCOUNTER** - Standard combat
- **BOSS_FIGHT** - Boss-level encounters
- **ELITE_SHOWDOWN** - Elite vs Elite

---

## Force User Detection

**Force User Criteria:**
- Must be from **Star Wars IP**
- Name, character_id, or lore contains Force user keywords:
  - "jedi"
  - "sith"
  - "force"
  - "mace"
  - "anakin"
  - "ace"

**Current Force Users:**
- **ACE** (Star Wars) - Combat Virtual Assistant
- **Mace Windu** (Star Wars) - Jedi Master

---

## Spawn Rate Logic

### Lightsaber Duels

1. **Check for Force User Lightsaber Duel (0.2%):**
   - If Force users available → Higher probability
   - Spawns lightsaber duel between Force users

2. **Check for Standard Lightsaber Duel (0.05%):**
   - Half of base spawn rate
   - Only if Force users available

### Macro Raids

- **Base Spawn Rate (0.1%):**
  - Raid Leader (JARVIS) vs random Champions/Elites
  - 1-3 opponents selected randomly

---

## Encounter Cooldown

- **Minimum Cooldown:** 5 minutes (300 seconds)
- Prevents encounter spam
- Ensures encounters are rare and meaningful

---

## Implementation

### RandomRaidEncounterSystem Class

**Key Methods:**
- `check_for_encounter()` - Check if encounter should spawn
- `is_force_user(character)` - Detect Force users
- `_create_lightsaber_duel()` - Create lightsaber duel
- `_create_macro_raid()` - Create macro raid
- `get_encounter_history()` - Get recent encounters
- `get_encounter_stats()` - Get statistics

**Usage:**

```python
from random_raid_encounter_system import RandomRaidEncounterSystem
from character_avatar_registry import CharacterAvatarRegistry

registry = CharacterAvatarRegistry()
encounter_system = RandomRaidEncounterSystem(registry)

# Check for encounter
encounter = encounter_system.check_for_encounter()
if encounter:
    print(f"Encounter spawned: {encounter['description']}")
```

---

## Encounter Structure

### Lightsaber Duel

```python
{
    "type": "lightsaber_duel",
    "timestamp": "2026-01-09T01:06:23.934755",
    "combatants": [
        {
            "character_id": "mace_windu",
            "name": "Mace Windu",
            "ip_owner": "Star Wars",
            "hierarchy_level": "champion"
        },
        {
            "character_id": "ace",
            "name": "ACE",
            "ip_owner": "Star Wars",
            "hierarchy_level": "champion"
        }
    ],
    "description": "⚔️ LIGHTSABER DUEL: Mace Windu vs ACE",
    "spawn_rate_used": 0.002
}
```

### Macro Raid

```python
{
    "type": "macro_raid",
    "timestamp": "2026-01-09T01:06:23.934755",
    "raid_leader": {
        "character_id": "jarvis",
        "name": "JARVIS",
        "hierarchy_level": "raid_leader"
    },
    "opponents": [
        {
            "character_id": "friday",
            "name": "FRIDAY",
            "ip_owner": "Marvel/MCU",
            "hierarchy_level": "champion"
        }
    ],
    "description": "🎮 MACRO RAID: JARVIS vs FRIDAY",
    "spawn_rate_used": 0.001
}
```

---

## Statistics

**Encounter Tracking:**
- Last 100 encounters stored
- Statistics by type
- Force user duel count
- Macro raid count

**Example Stats:**

```python
{
    "total_encounters": 1,
    "by_type": {
        "lightsaber_duel": 1
    },
    "force_user_duels": 1,
    "macro_raids": 0
}
```

---

## Integration Points

**Potential Integration:**
- GUI combat visualization
- Audio/visual effects
- Character animation triggers
- Combat outcome tracking
- XP/rewards system
- Achievement system

---

## Configuration

**Spawn Rates (Configurable):**
- `base_spawn_rate`: 0.001 (0.1%)
- `lightsaber_duel_rate`: 0.0005 (0.05%)
- `force_user_lightsaber_rate`: 0.002 (0.2%)

**Cooldown:**
- `encounter_cooldown`: 300.0 seconds (5 minutes)

---

## Test Results

**10,000 Check Simulation:**
- Encounters Spawned: 1
- Lightsaber Duels: 1
- Macro Raids: 0

**Force Users Detected:**
- ACE (Star Wars)
- Mace Windu (Star Wars)

**First Encounter:**
- Type: Lightsaber Duel
- Combatants: Mace Windu vs ACE
- Spawn Rate: 0.2% (Force user rate)

---

## Status

✅ **Random Encounter System:** IMPLEMENTED
✅ **Force User Detection:** WORKING
✅ **Lightsaber Duel Logic:** COMPLETE
✅ **Macro Raid System:** COMPLETE
✅ **Spawn Rate Control:** CONFIGURED
✅ **Cooldown System:** ACTIVE

---

## Tags

#RAID #ENCOUNTER #COMBAT #LIGHTSABER #FORCE_USER #MACRO_RAID @JARVIS @LUMINA

---

**Created:** 2026-01-09T01:06:23
**Status:** ✅ **RANDOM RAID ENCOUNTER SYSTEM COMPLETE**
