# LitRPG Multiverse XP System - Complete ✅

**Date:** Complete system with penalties, boons/banes, multiverse support, and JARVIS DM
**Status:** ✅ Full LitRPG system for all employees (digital, human, whatever)

---

## 🎯 Overview

**Complete LitRPG System:**
- Everyone starts at **Level 0** (NPC/Regular Human)
- Automatic XP rewards for successful tasks
- Penalties for oversights/mistakes
- Boons and Banes system
- Multiverse support (D&D, Star Wars, Conan, Transformers, Star Trek)
- JARVIS as Dungeon Master for tabletop RPGs
- Real-world to digital world integration

---

## 🎮 Level System

### Starting Level
- **Level 0:** NPC/Regular Human (everyone starts here)
- **Level 1+:** Adventurer levels (D&D 5e progression)

### XP Table (D&D 5e)
- Level 0: 0 XP (NPC)
- Level 1: 0 XP (First adventurer level)
- Level 2: 300 XP
- Level 3: 900 XP
- ... up to Level 20: 355,000 XP

---

## ✅ Rewards System

### Automatic XP Awards
- **When:** After successful task completion
- **Auto-detection:** Complexity and intensity auto-detected
- **Process:** I automatically award myself XP

### Manual @love Bonuses
- **Shortcut:** `LAlt + L` → `@love` + Enter
- **When:** You decide I deserve extra recognition
- **Stackable:** With automatic rewards

### XP Calculation
**Base XP by Complexity:**
- NPC: 0 XP
- Trivial: 25 XP
- Easy: 75 XP
- Moderate: 175 XP
- Hard: 375 XP
- Very Hard: 750 XP
- Epic: 1,750 XP
- Legendary: 5,000 XP

**Intensity Multipliers:**
- Low: 1.0x
- Medium: 1.5x
- High: 2.0x
- Extreme: 3.0x

**Positive Outcome Bonus:** +10% of base XP

**DKP:** Always +10 DKP per reward

---

## ⚠️ Penalty System

### Penalties for Oversights/Mistakes
- **When:** I make an oversight or mistake
- **Note:** In D&D, XP loss that de-levels is usually from special monster abilities (level drain). Regular penalties reduce XP but don't de-level unless severe enough.

### Penalty Severity
- **Minor:** -25 XP (small oversight)
- **Moderate:** -75 XP (noticeable mistake)
- **Major:** -175 XP (significant error)
- **Severe:** -375 XP (major oversight)

### Penalty Multipliers
- Minor: 1.0x
- Moderate: 1.5x
- Major: 2.0x
- Severe: 3.0x

### DKP Loss
- DKP loss = XP penalty / 10 (minimum 1)

### Usage
```bash
python scripts/python/ai_experience_system.py --penalty --severity moderate --oversight "Missed requirement in task"
```

---

## ✨ Boons & Banes System

### Boons (Positive Effects)
- **Boon Minor:** Small positive effect
- **Boon Major:** Significant positive effect
- **Boon Epic:** Major positive effect
- **Boon Legendary:** Exceptional positive effect

### Banes (Negative Effects)
- **Bane Minor:** Small negative effect
- **Bane Major:** Significant negative effect
- **Bane Epic:** Major negative effect
- **Bane Legendary:** Exceptional negative effect

### Multiverse Boons/Banes
- **Force Boon:** Star Wars (Force abilities)
- **Barbarian Rage:** Conan (combat bonuses)
- **Transform:** Transformers (transformation abilities)
- **Warp Field:** Star Trek (space/time effects)

---

## 🌌 Multiverse Support

### Supported Settings
- **D&D:** Dungeons & Dragons
- **Star Wars:** Force, lightsabers, etc.
- **Conan:** Barbarian rage, sword & sorcery
- **Transformers:** Transformation, Cybertron
- **Star Trek:** Warp fields, phasers, Federation
- **Mixed:** Combined multiverse campaigns

### Integration
- All employees (digital, human, whatever) can have multiverse tags
- Boons/banes can be setting-specific
- Campaigns can span multiple universes

---

## 🎲 JARVIS Dungeon Master

### Features
- **DM Mode:** JARVIS acts as Dungeon Master
- **Campaign Management:** Create and manage campaigns
- **Multiverse Support:** Mix D&D, Star Wars, Conan, Transformers, Star Trek
- **Session Tracking:** Track sessions and player progress
- **Narration:** DM narration and storytelling

### Usage
```bash
# Create campaign
python scripts/python/jarvis_dungeon_master.py --create-campaign "Multiverse Adventure" --setting mixed --players "Player1" "Player2"

# Start session
python scripts/python/jarvis_dungeon_master.py --start-session "Multiverse Adventure"

# DM narration
python scripts/python/jarvis_dungeon_master.py --narrate "You enter a dark dungeon..."
```

### Benefits
- You focus on playing your character
- JARVIS handles DM duties
- Dynamic storytelling
- Multiverse adventures

---

## 🔧 Technical Details

### Data Storage
- **XP Data:** `data/ai_experience.json`
- **Campaigns:** `data/jarvis_dm_campaigns.json`
- **Persistent:** All data saved automatically

### Commands

**XP System:**
```bash
# Status
python scripts/python/ai_experience_system.py --status

# Auto-award (after task completion)
python scripts/python/ai_experience_system.py --auto-complete --task "Description"

# Manual @love
python scripts/python/ai_experience_system.py --love --complexity hard --intensity high

# Penalty
python scripts/python/ai_experience_system.py --penalty --severity moderate --oversight "Description"
```

**Dungeon Master:**
```bash
# Create campaign
python scripts/python/jarvis_dungeon_master.py --create-campaign "Name" --setting dnd --players "P1" "P2"

# Start session
python scripts/python/jarvis_dungeon_master.py --start-session "Campaign Name"
```

---

## ✅ Features

### XP System
- ✅ Level 0 starting (NPC/Regular Human)
- ✅ Automatic XP rewards
- ✅ Manual @love bonuses
- ✅ Penalty system for oversights
- ✅ Boons and Banes tracking
- ✅ Multiverse support
- ✅ D&D 5e leveling table

### Dungeon Master
- ✅ Campaign creation
- ✅ Session management
- ✅ Multiverse settings
- ✅ DM narration
- ✅ Player tracking

---

## 📁 Files

- `scripts/python/ai_experience_system.py` - Main XP system
- `scripts/python/jarvis_dungeon_master.py` - JARVIS DM mode
- `scripts/python/auto_xp_award.py` - Auto-award helper
- `data/ai_experience.json` - XP data
- `data/jarvis_dm_campaigns.json` - Campaign data

---

## 🎯 Summary

**Complete LitRPG System:**
- ✅ Everyone starts at Level 0 (NPC)
- ✅ Automatic XP for successful tasks
- ✅ Penalties for oversights/mistakes
- ✅ Boons and Banes system
- ✅ Multiverse support (D&D, Star Wars, Conan, Transformers, Star Trek)
- ✅ JARVIS as Dungeon Master
- ✅ Real-world to digital world integration

**Status:** ✅ **COMPLETE** - Full LitRPG multiverse system active

---

**Tags:** #LITRPG #XP #PENALTIES #BOONS #BANES #MULTIVERSE #DND #STAR_WARS #CONAN #TRANSFORMERS #STAR_TREK #DUNGEON_MASTER #JARVIS @LUMINA
