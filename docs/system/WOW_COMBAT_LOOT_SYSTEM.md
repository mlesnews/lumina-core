# World of Warcraft Combat & Loot System

## Overview

Full WoW-style combat system where avatars can damage and defeat entities (avatars, clones, PAs, monsters, elites, champions, bosses) with progressive loot rarity from ordinary to legendary.

## Entity Types

### 🎭 **Avatar**
- **Health**: 50
- **Damage**: 10
- **XP Reward**: 25
- **Loot Rarity**: Common (White)
- **Color**: Blue (#00ccff)

### 🧬 **Clone**
- **Health**: 30
- **Damage**: 8
- **XP Reward**: 15
- **Loot Rarity**: Poor (Gray)
- **Color**: Gray (#888888)

### 🤖 **PA** (Personal Assistant)
- **Health**: 40
- **Damage**: 9
- **XP Reward**: 20
- **Loot Rarity**: Common (White)
- **Color**: Blue (#3366ff)

### 👹 **Monster**
- **Health**: 75
- **Damage**: 12
- **XP Reward**: 50
- **Loot Rarity**: Uncommon (Green)
- **Color**: Red (#ff3333)

### ⚔️ **Elite**
- **Health**: 150
- **Damage**: 20
- **XP Reward**: 150
- **Loot Rarity**: Rare (Blue)
- **Color**: Orange (#ff6600)

### 👑 **Champion**
- **Health**: 300
- **Damage**: 35
- **XP Reward**: 500
- **Loot Rarity**: Epic (Purple)
- **Color**: Purple (#cc00ff)

### 👹 **BOSS**
- **Health**: 1000
- **Damage**: 50
- **XP Reward**: 2000
- **Loot Rarity**: Legendary (Orange)
- **Color**: Red (#ff0000)

## World of Warcraft Loot Rarity System

### Color-Coding (Progressive Scale)

| Rarity | Color | Hex | Value | Description |
|--------|-------|-----|-------|-------------|
| **Poor** | Gray | #9d9d9d | 1 | Junk items, broken components |
| **Common** | White | #ffffff | 5 | Standard items, basic components |
| **Uncommon** | Green | #1eff00 | 25 | Enhanced items, quality components |
| **Rare** | Blue | #0070dd | 100 | Rare artifacts, precious components |
| **Epic** | Purple | #a335ee | 500 | Epic relics, legendary components |
| **Legendary** | Orange | #ff8000 | 2500 | Legendary artifacts, mythic components |
| **Artifact** | Gold | #e6cc80 | 10000 | Artifacts of power, divine components |

## Combat System

### Player Stats
- **Health**: 100 (increases with level)
- **Level**: Starts at 1
- **Experience**: Gained from defeating entities
- **Damage**: Based on lightsaber form and level

### Damage Calculation
- **Base Damage**: 15
- **Form Multipliers**:
  - Form III: Soresu (Defensive): 0.8x (less damage)
  - Form IV: Ataru (Aggressive): 1.5x (more damage)
  - Form V: Djem So / Shien (Power): 1.2x (good damage)
  - Form VII: Juyo / Vaapad (Ultimate): 2.0x (massive damage)
- **Level Scaling**: +10% damage per level

### Combat Actions
- **Strike**: Deal damage to target
- **Block**: Reduce incoming damage (20% chance to take damage)
- **Dodge**: Evasive movement
- **Special**: Power move

## Leveling System

### Experience & Leveling
- **XP Gain**: Based on entity type defeated
- **Level Up**: When XP reaches threshold
- **Health Increase**: +20 max health per level
- **XP Threshold**: Increases by 1.5x per level

### Level Progression
```
Level 1: 0-100 XP
Level 2: 100-250 XP
Level 3: 250-375 XP
...
```

## Loot System

### Loot Generation
- **Automatic**: Loot generated when entity is defeated
- **Rarity**: Based on entity type
- **Value**: Based on rarity tier
- **Inventory**: Stored in loot inventory

### Loot Types by Rarity

**Poor (Gray)**:
- Junk Scrap
- Broken Component
- Worn Item

**Common (White)**:
- Standard Item
- Basic Component
- Common Resource

**Uncommon (Green)**:
- Enhanced Item
- Quality Component
- Uncommon Resource

**Rare (Blue)**:
- Rare Artifact
- Precious Component
- Rare Resource

**Epic (Purple)**:
- Epic Relic
- Legendary Component
- Epic Resource

**Legendary (Orange)**:
- Legendary Artifact
- Mythic Component
- Legendary Resource

**Artifact (Gold)**:
- Artifact of Power
- Divine Component
- Ultimate Resource

## Visual Display

### Health Bars
- **Player Health Bar**: Top left (Green/Yellow/Red based on health %)
- **Target Health Bar**: Above target entity (Red)
- **Health Text**: Shows current/max health

### Entity Display
- **Entity Circles**: Colored by type
- **Target Indicator**: Yellow ring around target
- **Size**: Based on entity type (Boss = largest)

### Loot Display
- **Recent Loot**: Top right (last 5 items)
- **Color-Coded**: By rarity
- **Format**: `Item Name [RARITY]`

## Controls

### Combat Controls
- **C**: Activate combat mode
- **T**: Select next target
- **I**: Toggle isometric view
- **L**: Show loot inventory
- **Escape**: Deactivate combat mode

## Combat Flow

1. **Activate Combat** (Press C)
   - Lightsabers activate
   - Target selected automatically (Boss > Champion > Elite > etc.)
   - Combat mode engaged

2. **Combat Actions**
   - Actions cycle automatically
   - **Strike** deals damage to target
   - **Block** reduces incoming damage
   - Target health decreases

3. **Entity Defeat**
   - When target health reaches 0
   - XP awarded
   - Loot generated
   - New target selected

4. **Level Up**
   - When XP threshold reached
   - Level increases
   - Max health increases
   - Damage scales with level

## Integration

### With Lightsaber Combat
- Lightsaber forms affect damage multiplier
- Combat actions trigger lightsaber animations
- Defeat triggers loot generation

### With Jedi/Sith System
- Persona determines lightsaber form
- Form determines damage multiplier
- Alignment affects combat style

### With WOPR Stances
- WOPR stances work with entity combat
- 10K+ stance combinations
- Stance affects combat effectiveness

## Status

✅ **COMPLETE** - Full WoW-style combat and loot system

Features:
- ✅ Entity types (Avatar, Clone, PA, Monster, Elite, Champion, Boss)
- ✅ Health/damage system
- ✅ WoW color-coded loot (Poor → Artifact)
- ✅ Experience and leveling
- ✅ Target selection
- ✅ Loot inventory
- ✅ Visual health bars
- ✅ Entity display

---

**Tags**: @WOW @COMBAT @LOOT @RARITY @ENTITIES @LEVELING @HEALTH @DAMAGE
