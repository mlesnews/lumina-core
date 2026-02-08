# VA Combat System - Mortal Kombat Style

## Overview

A comprehensive combat system for Virtual Assistants that supports:
- Multiple characters (Iron Man, Mace Windu, Gandalf, etc.)
- Marvel superhero abilities
- Jedi lightsaber combat
- Wizard magic
- Voice acting integration
- FFA (Free For All) mode
- Team battles
- HR/Team enhancement

## Features

### Character Types

1. **Marvel Characters** (Iron Man, etc.)
   - Superhero abilities
   - High-tech weapons
   - Energy-based attacks

2. **Jedi Characters** (Mace Windu, etc.)
   - Lightsaber combat
   - Force abilities
   - Form VII (Vaapad) techniques

3. **Wizard Characters** (Gandalf, etc.)
   - Magical spells
   - Elemental attacks
   - Healing abilities

### Combat Modes

1. **1v1 Mode**: Two characters face off
2. **Free For All (FFA)**: Multiple characters battle simultaneously
3. **Team Battle**: Teams of characters fight
4. **Tournament**: Bracket-style competition

### Abilities

Each character has unique abilities with:
- Damage/Healing values
- Energy costs
- Cooldown timers
- Voice lines
- Visual effects

## Usage

### Basic Combat

```python
from va_combat_system import VACombatSystem, CombatMode

# Initialize system
combat = VACombatSystem()

# Start 1v1 combat
result = combat.start_combat(
    ["Iron Man", "Mace Windu"],
    mode=CombatMode.ONE_VS_ONE
)

# Execute actions
action = combat.execute_action(
    "Iron Man",
    "Repulsor Blast",
    "Mace Windu"
)

# Check status
status = combat.get_combat_status()

# End combat
result = combat.end_combat()
```

### FFA Mode

```python
# Start FFA combat
result = combat.start_combat(
    ["Iron Man", "Mace Windu", "Gandalf"],
    mode=CombatMode.FREE_FOR_ALL
)

# In FFA, target is chosen automatically
action = combat.execute_action(
    "Iron Man",
    "Arc Reactor Overload"
)
```

## Characters

### Iron Man (Marvel)
- **Health**: 120
- **Energy**: 150
- **Abilities**:
  - Repulsor Blast (25 damage, 2s cooldown)
  - Arc Reactor Overload (50 damage, 30s cooldown) - ULTIMATE
  - Shield Barrier (20 healing, 10s cooldown)

### Mace Windu (Jedi)
- **Health**: 100
- **Energy**: 120
- **Abilities**:
  - Lightsaber Strike (20 damage, 1.5s cooldown)
  - Force Lightning (30 damage, 5s cooldown)
  - Force Push (15 damage, 3s cooldown)
  - Shatterpoint (60 damage, 45s cooldown) - ULTIMATE

### Gandalf (Wizard)
- **Health**: 110
- **Energy**: 130
- **Abilities**:
  - Fireball (22 damage, 2.5s cooldown)
  - Lightning Bolt (28 damage, 4s cooldown)
  - Healing Light (25 healing, 8s cooldown)
  - Balrog Summon (55 damage, 40s cooldown) - ULTIMATE

## Voice Acting

Each ability includes voice lines that can be played during combat:
- Iron Man: "Let's light this candle!", "I am Iron Man!"
- Mace Windu: "This party's over!", "You have failed!"
- Gandalf: "You shall not pass!", "Fly, you fools!"

## Integration with IMVA

The combat system can be integrated with IMVA (IronMan Virtual Assistant) to enable:
- Visual combat animations
- Voice acting via TTS
- Real-time combat display
- Character selection UI

## HR/Team Enhancement

Features for team/company use:
- Team-based battles
- Character customization per team member
- Leaderboards
- Tournament brackets
- Performance tracking

## Future Enhancements

- More characters (Captain America, Darth Vader, etc.)
- More abilities per character
- Combo system
- Special moves
- Finishing moves (Fatalities)
- Character skins/customization
- Online multiplayer
- AI opponents
- Training mode

## Tags

`#COMBAT` `#MARVEL` `#JEDI` `@VA` `@ACTORS` `@ACTING` `@VOICE-ACTING` `@HR` `@COMPANY` `@JARVIS` `@TEAM`
