# Enhanced Desktop Combat System

## Overview

The Enhanced Desktop Combat System transforms the entire PC desktop into a battleground where Virtual Assistants (VAs) and characters can engage in combat with LitRPG leveling, XP tracking, random monsters, strategic alliances, and epic sound effects.

## Features

### ✅ Desktop-Wide Battleground
- **Entire PC Desktop**: Characters can move anywhere on the desktop
- **Real-time Movement**: Characters move toward enemies or allies
- **Position Tracking**: All character positions tracked in real-time
- **Distance-Based Combat**: Combat effectiveness based on proximity

### ✅ LitRPG Leveling System
- **XP System**: Characters gain XP from wins, kills, and participation
- **Leveling**: Characters level up with exponential XP requirements
- **Stat Bonuses**: Each level provides stat bonuses (10% per level)
- **Win/Loss Tracking**: Complete combat history tracked
- **Kill/Death Ratio**: Tracks kills and deaths

### ✅ Random Monster Spawns
- **Monster Types**: Goblins, Orcs, Dragons, Demons, Minions
- **Random Spawning**: Monsters spawn randomly on desktop
- **XP Rewards**: Defeating monsters grants XP
- **Dynamic Difficulty**: Different monster types have different stats

### ✅ Strategy: "Enemy of My Enemy is My Friend"
- **Temporary Alliances**: Characters can form alliances against common enemies
- **Alliance Duration**: Alliances last 30 seconds
- **Strategic Targeting**: Characters prioritize alliance targets
- **Dynamic Alliances**: Alliances can form and break during combat

### ✅ Epic Combat Sound Effects
- **Hit Sounds**: Sound effects for successful attacks
- **Critical Hits**: Special sounds for critical damage
- **Victory/Defeat**: Epic sounds for battle outcomes
- **Level Up**: Celebratory sounds for leveling
- **Monster Spawn**: Alert sounds for monster appearances
- **Alliance Formation**: Sound for alliance creation

### ✅ Dynamic Resource Scaling
- **CPU/RAM Monitoring**: Tracks system utilization
- **Auto-Scaling**: Adjusts combat resources based on system load
- **75% Limit**: Keeps utilization under 75%
- **Performance Optimization**: Maximizes performance when resources available

### ✅ IMVA Solid Appearance
- **Full Opacity**: IMVA now uses 255 alpha (fully solid, identical to ACVA)
- **No Transparency Issues**: Matches ACVA's solid appearance exactly
- **Visual Consistency**: Both VAs appear equally solid

## Usage

### Start Desktop Battle

```python
from src.cfservices.services.jarvis_core.desktop_combat_integration import DesktopCombatIntegration
from src.cfservices.services.jarvis_core.universal_combat_system import CombatMode

integration = DesktopCombatIntegration()

# Start desktop FFA battle
battle = integration.start_desktop_battle(
    character_ids=["iron_man", "mace_windu", "gandalf"],
    mode=CombatMode.FREE_FOR_ALL,
    enable_monsters=True,
    enable_alliances=True
)

# Execute combat rounds
while integration.active_battle:
    round_result = integration.execute_desktop_combat_round()
    if round_result.get("status") == "ended":
        break
```

### Form Alliance

```python
# Form alliance against common enemy
alliance = integration.form_alliance_against_enemy(
    character_ids=["iron_man", "mace_windu"],
    enemy_id="gandalf"
)
```

### Check Character Stats

```python
# Get character stats including level and XP
stats = integration.enhanced_combat.get_character_stats("iron_man")
print(f"Level: {stats['level']}")
print(f"XP: {stats['xp']}/{stats['xp_to_next']}")
print(f"Wins: {stats['wins']} | Losses: {stats['losses']}")
```

### View Leaderboard

```python
# Get top 10 characters
leaderboard = integration.enhanced_combat.get_leaderboard(limit=10)
for i, entry in enumerate(leaderboard, 1):
    print(f"{i}. {entry['name']} - Level {entry['level']} - {entry['total_xp']} XP")
```

## XP and Leveling

### XP Sources
- **Win**: 50 base XP + (opponent level × 10) bonus
- **Kill**: Additional XP for defeating opponent
- **Monster Kill**: XP based on monster type
- **Participation**: 10 XP for participating in battle

### Leveling Formula
- **Level 1**: 100 XP required
- **Level 2**: 150 XP required (1.5×)
- **Level 3**: 225 XP required (1.5×)
- **Exponential Growth**: Each level requires 1.5× previous level's XP

### Stat Bonuses
- **Per Level**: +10% to all stats
- **Level 10**: +90% stat bonus
- **Level 20**: +190% stat bonus

## Monster Types

| Monster | Health | Attack | XP Reward |
|---------|--------|--------|-----------|
| Minion  | 30     | 5      | 15        |
| Goblin  | 50     | 10     | 25        |
| Orc     | 80     | 15     | 40        |
| Demon   | 150    | 25     | 75        |
| Dragon  | 200    | 30     | 100       |

## Alliance Strategies

### Enemy of My Enemy
- Characters form alliance against common enemy
- Alliance lasts 30 seconds
- Characters prioritize attacking alliance target
- Can break if one character is defeated

### Team Up
- Multiple characters form team
- Work together against other teams
- Share XP from victories

### Betray
- Character can betray alliance
- Attack former ally
- Gain bonus XP for betrayal

## Sound Effects

### Available Sounds
- **Hit**: 600 Hz, 100ms
- **Critical**: 800 Hz → 1000 Hz pattern
- **Ability**: 500 Hz, 300ms
- **Victory**: 800 Hz → 1000 Hz → 1200 Hz pattern
- **Defeat**: 300 Hz, 500ms
- **Level Up**: 1000 Hz → 1200 Hz → 1500 Hz pattern
- **Monster Spawn**: 300 Hz, 300ms
- **Alliance**: 500 Hz, 200ms

## Dynamic Resource Scaling

### Scaling Algorithm
```
IF utilization > 75%:
    REDUCE resources to 60% of current
ELIF utilization < 45%:
    INCREASE resources to 130% of current
ELSE:
    MAINTAIN current resources
```

### Resource Types
- Combat thread count
- Monster spawn rate
- Sound effect frequency
- Position update rate
- Animation frame rate

## IMVA Solid Appearance Fix

### Changes Made
- **Alpha Value**: Changed from 240 to 255 (fully opaque)
- **Visual Match**: Now identical to ACVA's solid appearance
- **No Transparency**: Fully solid, no see-through effect

### Code Location
```python
# scripts/python/ironman_virtual_assistant.py
alpha_value = 255  # Maximum opacity (fully solid, identical to ACVA)
```

## Integration Points

### IMVA Integration
- IMVA can participate in desktop battles
- Moves around desktop during combat
- Visual combat animations
- Health bar display

### ACVA Integration
- ACVA can be detected and targeted
- Position tracking for combat
- Alliance formation possible

### HR/Team Integration
- All @company members can participate
- Team-based battles
- Department vs department
- Company-wide tournaments

## Future Enhancements

- [ ] Visual combat animations on desktop
- [ ] Particle effects for abilities
- [ ] Mini-map showing all positions
- [ ] Tournament brackets
- [ ] Guild/Team system
- [ ] Equipment system
- [ ] Skill trees
- [ ] Boss battles
- [ ] Daily challenges
- [ ] Achievement system

## Tags

`#COMBAT` `#DESKTOP` `#BATTLEGROUND` `#LITRPG` `#XP` `#LEVELING` `#MONSTERS` `#STRATEGY` `#SOUNDS` `@VA` `@ACTORS` `@HR` `@TEAM` `@COMPANY` `@JARVIS`
