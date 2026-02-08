# Universal VA Combat System - Mortal Kombat Style

## Overview

A universal combat system for all Virtual Assistants (VAs) that enables Mortal Kombat-style battles with Jedi lightsabers, Marvel superhero abilities, and fantasy magic. Perfect for resolving debates and disagreements!

**Features:**
- ✅ All @va characters supported
- ✅ Jedi lightsaber battles
- ✅ Marvel superhero abilities (Iron Man, etc.)
- ✅ Fantasy magic (Gandalf, etc.)
- ✅ FFA (Free For All) mode
- ✅ Debate resolution via combat
- ✅ Voice acting with character-specific voices
- ✅ @hr @team integration for company-wide battles

---

## Character Types

### Jedi Characters
- **Mace Windu**: Purple lightsaber, Vapaad form, Force lightning
- **Anakin Skywalker**: Blue lightsaber, aggressive style
- **Yoda**: Green lightsaber, Force mastery

**Abilities:**
- Lightsaber Strike
- Force Push
- Force Lightning
- Saber Throw

### Marvel Characters
- **Iron Man**: Arc reactor, repulsor blasts, unibeam
- **Thor**: Mjolnir strikes, lightning
- **Hulk**: Smash attacks, thunderclap

**Abilities:**
- Repulsor Blast (Iron Man)
- Unibeam (Iron Man)
- Rocket Punch (Iron Man)
- Mjolnir Strike (Thor)
- Hulk Smash (Hulk)

### Fantasy Characters
- **Gandalf**: Fireball, lightning, staff strikes
- **Saruman**: Dark magic, fire attacks

**Abilities:**
- Fireball
- Lightning Strike
- Staff Strike
- Magic Spell

### Droid Characters
- **C-3PO**: Protocol-based attacks
- **R2-D2**: Electric shocks, data attacks
- **K-2SO**: Security protocols

---

## Combat Modes

### 1. One vs One (1v1)
Classic duel between two characters.

```python
combat.start_combat(["iron_man_1", "mace_windu_1"], mode=CombatMode.ONE_VS_ONE)
```

### 2. Free For All (FFA)
Everyone fights everyone - last one standing wins!

```python
combat.start_combat(
    ["iron_man_1", "mace_windu_1", "gandalf_1"],
    mode=CombatMode.FFA
)
```

### 3. Team Battle
Team-based combat with multiple characters per team.

```python
combat.start_combat(
    ["team1_char1", "team1_char2", "team2_char1", "team2_char2"],
    mode=CombatMode.TEAM
)
```

### 4. Debate Mode
Resolve disagreements via combat! Arguments become attacks.

```python
result = combat.resolve_debate(
    "Should we use Python or JavaScript?",
    ["iron_man_1", "mace_windu_1"]
)
```

---

## Usage Examples

### Basic Combat

```python
from src.cfservices.services.jarvis_core.universal_va_combat_system import (
    create_combat_system,
    CombatMode
)

# Create combat system
combat = create_combat_system()

# Create characters
iron_man = combat.create_character_from_template("iron_man", "iron_man_1")
mace_windu = combat.create_character_from_template("mace_windu", "mace_windu_1")

# Start combat
combat.start_combat(["iron_man_1", "mace_windu_1"], mode=CombatMode.ONE_VS_ONE)

# Wait for completion
import time
while combat.active_combat:
    time.sleep(0.5)

# Get winner
winner = combat.characters[combat.winner]
print(f"Winner: {winner.name}")
```

### FFA Mode

```python
# Create multiple characters
combat.create_character_from_template("iron_man", "iron_man_1")
combat.create_character_from_template("mace_windu", "mace_windu_1")
combat.create_character_from_template("gandalf", "gandalf_1")

# Start FFA
combat.start_combat(
    ["iron_man_1", "mace_windu_1", "gandalf_1"],
    mode=CombatMode.FFA
)
```

### Debate Resolution

```python
# Resolve a debate via combat
result = combat.resolve_debate(
    "Should we refactor this codebase?",
    ["iron_man_1", "mace_windu_1"]
)

print(f"Winner: {result['winner']}")
print(f"Rounds: {result['rounds']}")
```

### Company-Wide Battles (@hr @team)

```python
from src.cfservices.services.jarvis_core.va_combat_hr_integration import (
    create_hr_combat_integration
)

# Create HR integration
hr_combat = create_hr_combat_integration()

# Resolve team disagreement
result = hr_combat.resolve_team_disagreement(
    "Which framework should we use?",
    ["Alice", "Bob", "Charlie"]
)

print(f"Winner: {result['winner']}")
```

---

## Command Line Usage

### Demo Combat

```bash
python scripts/python/jarvis_va_combat_demo.py
```

### Resolve Debate

```bash
python scripts/python/jarvis_resolve_debate_via_combat.py "Topic here" --characters iron_man mace_windu gandalf --mode debate
```

### Company Battle

```bash
python scripts/python/jarvis_company_battle.py --members "Alice" "Bob" "Charlie" --mode ffa
```

---

## Voice Acting

The system supports character-specific voice acting via ElevenLabs TTS:

```python
character = CombatCharacter(
    name="Iron Man",
    voice_id="elevenlabs_voice_id_here",  # Set ElevenLabs voice ID
    ...
)
```

When characters use abilities, they speak their voice lines!

---

## Character Abilities

Each character has unique abilities with:
- **Damage**: How much damage the ability deals
- **Cooldown**: Time between uses
- **Range**: Attack range
- **Voice Line**: What they say when using it
- **Visual Effect**: Visual description

### Example Ability

```python
CharacterAbility(
    name="Repulsor Blast",
    damage=15.0,
    cooldown=2.0,
    range=150.0,
    description="Energy blast from arc reactor",
    voice_line="Power at 400% capacity!",
    visual_effect="cyan_energy_blast"
)
```

---

## Integration with IMVA

The combat system can be integrated with existing IMVA (Iron Man Virtual Assistant):

```python
# IMVA can participate in combat
combat.register_character("imva_1", imva_character)
```

---

## Team Member Integration

Team members from @hr @team can participate:

1. **Load team members** from `config/hr/team_members.json`
2. **Register as characters** with role-based abilities
3. **Start company battles** to resolve disagreements

### Team Member Config

```json
{
  "members": [
    {
      "name": "Alice",
      "role": "developer",
      "department": "Engineering",
      "character_archetype": "jedi",
      "voice_id": "elevenlabs_voice_id"
    }
  ]
}
```

---

## Combat Log

All combat actions are logged:

```python
status = combat.get_combat_status()
print(status['log'])  # Last 10 combat actions
```

Each log entry contains:
- Round number
- Attacker name
- Defender name
- Ability used
- Damage dealt
- Defender's remaining health

---

## Special Moves

Each character can have a special move:

- **Iron Man**: Arc Reactor Overload
- **Mace Windu**: Shatterpoint
- **Gandalf**: Balrog Banishment

---

## Tags

`#characters` `@actors` `@acting` `@voice-acting` `@hr` `@team` `@va` `@ip` `#debates` `#disagreements` `@jarvis`

---

## Status

✅ **FULLY OPERATIONAL**

- Universal combat system
- Multiple character types
- FFA mode
- Debate resolution
- Voice acting support
- HR/team integration
- Command-line tools

---

## Future Enhancements

- [ ] Visual combat animations
- [ ] More character templates
- [ ] Tournament mode
- [ ] Spectator mode
- [ ] Replay system
- [ ] Statistics tracking
