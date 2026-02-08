# Universal Combat System - Mortal Kombat Style

## Overview

A comprehensive combat system for all Virtual Assistants (VAs), characters, and company members. Supports Jedi lightsaber battles, Marvel superhero abilities, wizard magic, and FFA (Free For All) mode. Can be used for resolving debates and disagreements.

## Features

- ✅ **Jedi Lightsaber Battles**: Mace Windu, other Jedi characters
- ✅ **Marvel Superhero Abilities**: Iron Man, and more
- ✅ **Wizard Magic**: Gandalf and other wizards
- ✅ **VA Characters**: JARVIS and other virtual assistants
- ✅ **FFA Mode**: Free For All battles with multiple participants
- ✅ **Debate Resolution**: Resolve team debates through combat
- ✅ **Voice Acting**: Character-specific voice lines
- ✅ **HR/Team Integration**: All @company members can participate

## Characters

### Default Characters

1. **Iron Man** (Marvel)
   - Type: Marvel Superhero
   - Abilities: Repulsor Blast, Unibeam, Rocket Barrage, Flight Strike
   - Voice: Robert Downey Jr.
   - Special: Arc Reactor, Flight

2. **Mace Windu** (Jedi)
   - Type: Jedi Master
   - Abilities: Force Push, Vaapad Strike, Force Lightning Deflection, Force Crush
   - Voice: Samuel L. Jackson
   - Lightsaber: Purple (#7B2CBF)
   - Special: Vaapad Form, Force Mastery

3. **Gandalf the Grey** (Wizard)
   - Type: Wizard
   - Abilities: Magic Missile, Lightning Strike, Shield Spell, Gandalf's Fireworks
   - Voice: Ian McKellen
   - Special: Staff, Pipe

4. **JARVIS** (VA)
   - Type: Virtual Assistant
   - Abilities: System Analysis, Precision Strike, Defensive Protocol, Coordination Boost
   - Voice: Paul Bettany
   - Special: AI Level, Butler, Loyalty

## Combat Modes

### 1. One vs One (1v1)
Classic duel between two characters.

```python
battle = combat_system.start_battle(
    character_ids=["iron_man", "mace_windu"],
    mode=CombatMode.ONE_VS_ONE
)
```

### 2. Free For All (FFA)
Multiple characters battle until one remains.

```python
battle = combat_system.start_battle(
    character_ids=["iron_man", "mace_windu", "gandalf", "jarvis"],
    mode=CombatMode.FREE_FOR_ALL
)
```

### 3. Team Battle
Teams of characters battle each other.

```python
battle = combat_system.start_battle(
    character_ids=["iron_man", "mace_windu", "gandalf"],
    mode=CombatMode.TEAM_BATTLE
)
```

### 4. Debate Resolution
Resolve team debates through combat.

```python
result = combat_system.resolve_debate(
    character_ids=["iron_man", "mace_windu", "gandalf"],
    debate_topic="Should we use Python or JavaScript?",
    rounds=5
)
```

## Usage

### Basic Combat

```python
from src.cfservices.services.jarvis_core.universal_combat_system import (
    UniversalCombatSystem,
    CombatMode
)

# Initialize system
combat = UniversalCombatSystem()

# Start 1v1 battle
battle = combat.start_battle(
    character_ids=["iron_man", "mace_windu"],
    mode=CombatMode.ONE_VS_ONE
)

# Execute abilities
combat.execute_ability(
    battle_id=battle["battle_id"],
    character_id="iron_man",
    ability_name="Repulsor Blast",
    target_id="mace_windu"
)

# Check battle status
status = combat.get_battle_status(battle["battle_id"])
```

### Debate Resolution

```python
# Resolve a team debate
result = combat.resolve_debate(
    character_ids=["iron_man", "mace_windu", "gandalf"],
    debate_topic="Which framework should we use?",
    rounds=5
)

print(f"Winner: {result['winner_name']}")
```

### Interactive Arena

```bash
python scripts/python/jarvis_combat_arena.py
```

## Adding Custom Characters

```python
from src.cfservices.services.jarvis_core.universal_combat_system import (
    Character,
    CharacterType,
    Ability
)

# Create custom character
custom_char = Character(
    character_id="custom_hero",
    name="Custom Hero",
    character_type=CharacterType.MARVEL,
    max_health=120.0,
    abilities=[
        Ability(
            name="Custom Attack",
            damage=30.0,
            cooldown=3.0,
            energy_cost=20.0,
            description="Custom ability",
            voice_line="Custom voice line!"
        )
    ]
)

# Register character
combat.register_character(custom_char)
```

## Integration with VAs

The combat system integrates with IMVA and other VAs:

```python
from scripts.python.jarvis_combat_integration import CombatIntegration

integration = CombatIntegration()

# Register VA for combat
integration.register_va_character(
    va_instance=imva_instance,
    character_id="iron_man_va",
    name="Iron Man VA"
)

# Start VA battle
battle = integration.start_va_battle(
    va_character_ids=["iron_man_va", "jarvis_va"],
    mode=CombatMode.ONE_VS_ONE
)
```

## Voice Acting

Each ability can have a voice line that plays when used:

```python
ability = Ability(
    name="Repulsor Blast",
    damage=25.0,
    cooldown=2.0,
    energy_cost=15.0,
    description="Energy blast",
    voice_line="I am Iron Man!"  # Plays when ability is used
)
```

## HR/Team Integration

All @company members can participate in combat for:
- **Debate Resolution**: Resolve team disagreements
- **Decision Making**: Use combat to make decisions
- **Team Building**: Fun team activities

```python
# Resolve team debate
result = integration.resolve_team_debate(
    team_members=["team_member_1", "team_member_2", "team_member_3"],
    debate_topic="Which approach should we take?",
    rounds=5
)
```

## Character Abilities

### Ability System

Each character has abilities with:
- **Damage**: Damage dealt to opponent
- **Cooldown**: Time before ability can be used again
- **Energy Cost**: Energy required to use ability
- **Special Effects**: Deflect, shield, analyze, boost, etc.
- **Voice Lines**: Character-specific voice lines

### Energy System

Characters have energy that regenerates over time. Abilities cost energy to use.

### Health System

Characters have health that decreases when damaged. When health reaches 0, character is defeated.

## Battle Logging

All battles are logged with:
- Round number
- Turn number
- Character actions
- Damage dealt
- Voice lines
- Timestamps

## Future Enhancements

- [ ] More characters (Spider-Man, Captain America, etc.)
- [ ] Visual combat animations
- [ ] Real-time voice acting integration
- [ ] Team formation system
- [ ] Tournament mode
- [ ] Character progression/leveling
- [ ] Custom ability creation UI

## Tags

`#CHARACTERS` `#ACTING` `#VOICE-ACTING` `#DEBATES` `#DISAGREEMENTS` `@VA` `@ACTORS` `@HR` `@TEAM` `@COMPANY` `@JARVIS`


## Overview

The Universal Combat System allows all Virtual Assistants (VAs) and characters to engage in combat, from Jedi lightsaber battles to Marvel superhero fights, fantasy magic duels, and even debate resolution.

## Features

### Character Types

- **Jedi**: Lightsaber combat, Force abilities (Mace Windu, Anakin, Yoda)
- **Marvel**: Superhero abilities (Iron Man, Thor, Hulk)
- **Fantasy**: Magic spells (Gandalf, Saruman)
- **Droids**: Tech-based attacks (C-3PO, R2-D2, K-2SO)
- **Custom**: Register your own characters

### Combat Modes

1. **1v1**: Traditional one-on-one battle
2. **Free-For-All (FFA)**: All vs all combat
3. **Team Battle**: Team-based combat
4. **Debate Mode**: Resolve disagreements using combat mechanics

### Special Features

- **Voice Acting Integration**: Characters can have voice actors for @voice-acting
- **HR/Team Enhancement**: Characters can have HR profiles for @hr @team integration
- **Combat History**: Track all combat actions
- **Special Abilities**: Each character has unique abilities with cooldowns and energy costs

## Usage

### Quick Combat Examples

```python
from src.cfservices.services.jarvis_core.universal_combat_system import (
    UniversalCombatSystem,
    CombatMode
)

# Create combat system
combat = UniversalCombatSystem()

# 1v1 Battle
result = combat.start_combat(["iron_man", "mace_windu"], CombatMode.ONE_VS_ONE)

# Execute rounds
while combat.active_combat:
    round_result = combat.execute_combat_round()
    if round_result.get("status") == "ended":
        break

# Get winner
final = combat._end_combat()
print(f"Winner: {final['winner']}")
```

### FFA Mode

```python
# Free-for-all with multiple characters
result = combat.start_combat(
    ["iron_man", "mace_windu", "gandalf", "thor"],
    CombatMode.FREE_FOR_ALL
)
```

### Debate Resolution

```python
# Resolve a debate/disagreement
debate_result = combat.resolve_debate(
    "Should we use Python or JavaScript?",
    ["iron_man", "mace_windu", "gandalf"]
)

print(f"Winner: {debate_result['winner']}")
print(f"Resolution: {debate_result['resolution']}")
```

### Register Custom Character

```python
from src.cfservices.services.jarvis_core.universal_combat_system import (
    CharacterType,
    CharacterStats,
    CombatAbility
)

# Create custom character
custom_char = combat.register_character(
    character_id="custom_hero",
    name="Custom Hero",
    character_type=CharacterType.CUSTOM,
    character_class="Warrior",
    stats=CharacterStats(
        max_health=120.0,
        attack_power=15.0,
        defense=10.0
    ),
    abilities=[
        CombatAbility("custom_attack", 20.0, 3.0, 15.0, "Custom attack", CharacterType.CUSTOM)
    ],
    voice_actor="John Doe",  # For @voice-acting
    hr_profile={"team": "Engineering", "role": "Developer"}  # For @hr @team
)
```

## Character Abilities

### Jedi Abilities
- Lightsaber Strike
- Force Push
- Force Lightning
- Force Choke
- Saber Throw

### Marvel Abilities
- **Iron Man**: Repulsor Blast, Unibeam, Rocket Punch, Flight Attack, Nanotech Shield
- **Thor**: Mjolnir Strike, Lightning Blast, Thunder Clap, God Blast
- **Hulk**: Hulk Smash, Thunderclap, Ground Stomp, Rage Boost

### Fantasy Abilities
- Fireball
- Lightning Bolt
- Ice Shard
- Magic Missile
- Shield

## Integration Points

### IMVA Integration
The combat system can be integrated with IMVA (Iron Man Virtual Assistant) for visual combat displays.

### Voice Acting
Characters can have voice actors assigned for voice lines during combat.

### HR/Team Enhancement
Characters can have HR profiles for team-based combat and role-playing.

### Debate Resolution
Use combat mechanics to resolve disagreements and debates in a fun, engaging way.

## Examples

### Famous Matchups

1. **Iron Man vs Mace Windu**: Technology vs The Force
2. **Gandalf vs Saruman**: Good vs Evil magic
3. **Jedi FFA**: Mace Windu vs Anakin vs Yoda
4. **Marvel vs Fantasy**: Iron Man vs Gandalf

### Debate Examples

- "Python vs JavaScript"
- "Cloud vs On-Premise"
- "Agile vs Waterfall"
- "Monolith vs Microservices"

## Scripts

- `jarvis_combat_arena.py`: Interactive combat arena
- `jarvis_quick_combat.py`: Quick battle examples

## Tags

`#combat` `#va` `#characters` `#actors` `#voice-acting` `@hr` `@team` `@company` `@jarvis`
