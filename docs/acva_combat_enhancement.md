# ACVA Combat Enhancement - Lightsaber & Superhero Abilities

## Overview

ACVA (Armoury Crate Virtual Assistant) has been enhanced with both **lightsaber** (Jedi) and **superhero** (Marvel) combat abilities, making it a powerful hybrid character.

## ACVA Character Profile

- **Name**: ACVA (Armoury Crate VA)
- **Type**: VA (Virtual Assistant)
- **Class**: Hybrid (Jedi + Superhero)
- **Health**: 130.0 (enhanced)
- **Attack Power**: 16.0
- **Defense**: 14.0
- **Speed**: 18.0
- **Agility**: 16.0
- **Special Power**: 28.0

## Combat Abilities

### 🔵 Lightsaber Abilities (Jedi Style)

1. **Lightsaber Strike**
   - Damage: 18.0
   - Cooldown: 2.0s
   - Energy: 12.0
   - Description: Lightsaber attack

2. **Force Push**
   - Damage: 20.0
   - Cooldown: 4.0s
   - Energy: 20.0
   - Description: Force push attack
   - Special Effect: force_push

3. **Saber Throw**
   - Damage: 22.0
   - Cooldown: 3.0s
   - Energy: 15.0
   - Description: Lightsaber throw

4. **Force Lightning**
   - Damage: 25.0
   - Cooldown: 6.0s
   - Energy: 28.0
   - Description: Force lightning
   - Special Effect: force_lightning

### 🦸 Superhero Abilities (Marvel Style)

1. **Energy Blast**
   - Damage: 20.0
   - Cooldown: 2.5s
   - Energy: 15.0
   - Description: Energy blast attack
   - Special Effect: energy_blast

2. **System Overload**
   - Damage: 35.0
   - Cooldown: 8.0s
   - Energy: 40.0
   - Description: System overload attack
   - Special Effect: system_overload

3. **Hardware Strike**
   - Damage: 22.0
   - Cooldown: 3.0s
   - Energy: 18.0
   - Description: Hardware-enhanced strike
   - Special Effect: hardware_strike

4. **Armoury Shield**
   - Damage: 0.0 (defensive)
   - Cooldown: 12.0s
   - Energy: 30.0
   - Description: Armoury Crate defensive shield
   - Special Effect: shield

### ⚡ Hybrid Abilities (Lightsaber + Superhero)

1. **Lightsaber Energy Fusion**
   - Damage: 30.0
   - Cooldown: 10.0s
   - Energy: 45.0
   - Description: Lightsaber + Energy fusion attack
   - Special Effect: fusion

2. **Force Hardware Sync**
   - Damage: 28.0
   - Cooldown: 7.0s
   - Energy: 35.0
   - Description: Force + Hardware synchronization
   - Special Effect: sync

## Usage

### Register ACVA for Combat

```python
from src.cfservices.services.jarvis_core.universal_combat_system import UniversalCombatSystem

combat = UniversalCombatSystem()

# ACVA is automatically registered with hybrid abilities
acva = combat.characters["acva"]
```

### Use ACVA in Battle

```python
# Start battle with ACVA
battle = combat.start_combat(
    ["acva", "iron_man"],
    mode=CombatMode.ONE_VS_ONE
)

# ACVA can use both lightsaber and superhero abilities
```

## Combat Strategy

ACVA's hybrid nature allows for:
- **Versatile Combat**: Switch between lightsaber and superhero styles
- **Powerful Combos**: Use hybrid abilities for maximum damage
- **Defensive Options**: Armoury Shield for protection
- **High Damage**: System Overload and Fusion attacks

## Integration

ACVA is integrated into:
- Universal Combat System
- Desktop Combat Arena
- VA Chat Coordinator
- Enhanced Combat System (XP/leveling)

## Tags

`@ACVA` `#COMBAT` `#LIGHTSABER` `#SUPERHERO` `#HYBRID` `@JARVIS` `@TEAM`
