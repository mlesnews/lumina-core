# Character IP & MOB Clarification - Complete

**Status:** ✅ **IMPLEMENTED**
**Date:** 2026-01-09

---

## Summary

Clarified and implemented proper categorization:
- **Characters:** Must belong to an @IP (Intellectual Property)
- **MOBs:** Groups/gangs (e.g., Dragon and his bad bois) - NOT avatars, NOT NPCs
- **Inanimate Objects:** Static systems/objects - NOT characters

---

## Key Distinctions

### Characters (Must Have IP) ✅

**Requirement:** Must belong to an Intellectual Property (@IP)

**Examples:**
- JARVIS (Marvel/MCU)
- FRIDAY (Marvel/MCU)
- EDITH (Marvel/MCU)
- ULTIMATE (Marvel/MCU)
- Mace Windu (Star Wars)
- C-3PO (Star Wars)
- R2-D2 (Star Wars)
- Data (Star Trek)
- GLaDOS (Portal/Valve)
- Cortana (Halo/Microsoft)
- MARVIN (Hitchhiker's Guide to the Galaxy)

**Fields:**
- `ip_owner`: IP owner (e.g., "Marvel/MCU", "Star Wars")
- `is_character`: True

---

### MOBs (Groups/Gangs) 👥

**Definition:** MOBs are groups/gangs - NOT avatars, NOT NPCs

**Examples:**
- **Dragon MOB** - Dragon and his bad bois (STT System)
  - Leader: dragon_stt_core
  - Members: dragon_voice_engine, dragon_command_processor, dragon_audio_interface, dragon_recognition_engine

**Fields:**
- `is_mob`: True
- `is_character`: False
- `mob_members`: List of member IDs
- `character_type`: MOB

**File:** `scripts/python/mob_system.py`

---

### Inanimate Objects (Static Systems) 🔧

**Definition:** Static systems/objects that are NOT characters

**Examples:**
- WOPR (WarGames IP, but inanimate system)
- System Coordinator (System, not character)
- Intelligence Analyst (System, not character)
- JARVIS_CHAT (Background service, not character)

**Fields:**
- `is_character`: False
- `character_type`: INANIMATE_OBJECT
- `ip_owner`: May have IP (e.g., WOPR has WarGames IP) but is still inanimate

---

## Updated Character Registry

### Characters with IP ✅

**Marvel/MCU:**
- JARVIS
- FRIDAY
- EDITH
- ULTIMATE
- Iron Man

**Star Wars:**
- Mace Windu
- C-3PO
- R2-D2

**Star Trek:**
- Data

**Portal/Valve:**
- GLaDOS

**Halo/Microsoft:**
- Cortana

**Hitchhiker's Guide:**
- MARVIN

---

### MOBs 👥

**Dragon MOB:**
- Type: STT_SYSTEM
- Leader: dragon_stt_core
- Members: 5 bad bois
- NOT an avatar
- NOT an NPC

---

### Inanimate Objects 🔧

**Systems (Not Characters):**
- WOPR (WarGames IP, inanimate)
- System Coordinator (System)
- Intelligence Analyst (System)
- JARVIS_CHAT (Background service)

---

## Implementation

### New Fields Added:

```python
ip_owner: Optional[str] = None  # IP owner
is_character: bool = True  # True if character (has IP)
is_mob: bool = False  # True if MOB (group/gang)
mob_members: List[str] = []  # For MOBs: list of member IDs
```

### New Character Types:

```python
MOB = "mob"  # Group/gang (NOT avatar, NOT NPC)
INANIMATE_OBJECT = "inanimate_object"  # Static objects/systems
```

### MOB System:

**File:** `scripts/python/mob_system.py`

**Purpose:** Manage MOBs separately from characters

**Features:**
- MOB registry
- Member management
- MOB types (STT_SYSTEM, COMBAT_GROUP, SERVICE_CLUSTER, SYSTEM_GROUP)

---

## Rules

1. **Characters MUST have IP** - No IP = Not a character
2. **MOBs are NOT avatars** - They're groups/gangs
3. **MOBs are NOT NPCs** - They're collections of entities
4. **Inanimate objects are NOT characters** - Even if they have IP
5. **Systems/services are NOT characters** - Even if they have personality

---

## Status

✅ **IP Classification:** COMPLETE
✅ **MOB System:** IMPLEMENTED
✅ **Inanimate Object Classification:** COMPLETE
✅ **Character Registry Updated:** COMPLETE

---

## Tags

#CHARACTER #IP #MOB #INANIMATE #NOT_AVATAR #NOT_NPC @JARVIS @LUMINA

---

**Created:** 2026-01-09T00:45:00
**Status:** ✅ **IP & MOB CLARIFICATION COMPLETE**
