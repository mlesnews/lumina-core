# IMVA Comprehensive System

## Overview

The IMVA (Iron Man Virtual Assistant) Comprehensive System makes IMVA as robust and comprehensive as ACE. It includes:

- **Multiple Armor Variants**: Mark V, Mark III, Mark VI, Mark VII, Mark XLII, Mark L, Hulkbuster
- **Tony Stark Character States**: Casual, Business, Workshop, Suiting Up
- **Rich Action System**: 18+ actions including combat, movement, transformation, gestures
- **State Management**: Comprehensive state system with transitions
- **Event System**: Event-driven architecture for extensibility

## Quick Start

### List Available Options

```bash
# List all armors
python scripts/python/imva_comprehensive_manager.py --list-armors

# List all Tony Stark variants
python scripts/python/imva_comprehensive_manager.py --list-tony

# List all actions
python scripts/python/imva_comprehensive_manager.py --list-actions
```

### Launch IMVA

```bash
# Launch with specific armor
python scripts/python/imva_comprehensive_manager.py --launch mark_v

# Launch with Tony variant
python scripts/python/imva_comprehensive_manager.py --launch tony_casual
```

### Control IMVA

```bash
# Set outfit
python scripts/python/imva_comprehensive_manager.py --outfit mark_vi

# Perform action
python scripts/python/imva_comprehensive_manager.py --action flying

# Check status
python scripts/python/imva_comprehensive_manager.py --status
```

## Available Armors

### Mark V - Suitcase Suit
- **Type**: Portable armor
- **Features**: Briefcase transformation, quick deployment, lightweight
- **Launch**: `--launch mark_v`

### Mark III
- **Type**: Classic armor
- **Features**: Full weapons, flight, classic red and gold
- **Launch**: `--launch mark_iii`

### Mark VI
- **Type**: Improved armor
- **Features**: Triangular arc reactor, enhanced weapons
- **Launch**: `--launch mark_vi`

### Mark VII
- **Type**: Portable advanced armor
- **Features**: Portable suit-up, advanced weapons
- **Launch**: `--launch mark_vii`

### Mark XLII - Autonomous Prehensile
- **Type**: Autonomous armor
- **Features**: Remote assembly, prehensile, advanced AI
- **Launch**: `--launch mark_xlii`

### Mark L - Bleeding Edge
- **Type**: Nanotechnology armor
- **Features**: Nanotech, instant deployment, shape-shifting
- **Launch**: `--launch mark_l`

### Hulkbuster - Mark XLIV
- **Type**: Heavy combat armor
- **Features**: Massive size, heavy weapons, reinforced
- **Launch**: `--launch hulkbuster`

## Tony Stark Variants

### Tony Casual
- **Type**: Casual clothing
- **Features**: Human form, casual clothing, no armor
- **Launch**: `--launch tony_casual`

### Tony Business
- **Type**: Business attire
- **Features**: Human form, business suit, no armor
- **Launch**: `--launch tony_business`

### Tony Workshop
- **Type**: Workshop gear
- **Features**: Human form, workshop clothing, tools
- **Launch**: `--launch tony_workshop`

### Tony Suiting Up
- **Type**: Transformation state
- **Features**: Human form, partial armor, transformation
- **Launch**: `--launch tony_suit_up`

## Available Actions

### Movement Actions
- `walking` - Walking animation
- `flying` - Flight with repulsors (requires armor)
- `landing` - Landing from flight (requires armor)

### Combat Actions
- `repulsor_blast` - Firing repulsor beams (requires armor)
- `unibeam` - Chest arc reactor beam (requires armor)
- `combat_stance` - Ready for combat (requires armor)

### Transformation Actions
- `suit_up` - Armor deployment (requires Tony)
- `suit_down` - Armor removal (requires armor)

### Activity Actions
- `working` - Working on something
- `thinking` - Deep thought pose
- `scanning` - Environmental scan (requires armor)

### Emotion Actions
- `celebrating` - Victory celebration

### Gesture Actions
- `pointing` - Pointing gesture
- `thumbs_up` - Approval gesture
- `wave` - Waving gesture

### State Actions
- `idle` - Standing idle
- `sleeping` - Resting/sleeping
- `damaged` - Armor damage state (requires armor)
- `notifying` - Notification alert

## State System

IMVA has a comprehensive state system:

- `IDLE` - Standing idle
- `WALKING` - Walking
- `FLYING` - Flying
- `WORKING` - Working
- `THINKING` - Thinking
- `SLEEPING` - Sleeping
- `NOTIFYING` - Notifying
- `SUITING_UP` - Suiting up
- `SUITING_DOWN` - Suiting down
- `COMBAT` - Combat mode
- `DAMAGED` - Damaged state
- `CELEBRATING` - Celebrating
- `SCANNING` - Scanning

## Configuration Files

### `config/imva_armors_config.json`
Contains all armor and Tony Stark variant definitions.

### `config/imva_actions_config.json`
Contains all action definitions and requirements.

## Programmatic Usage

```python
from imva_comprehensive_manager import IMVAComprehensiveManager, IMVAState

# Initialize manager
manager = IMVAComprehensiveManager()

# Set outfit
manager.set_outfit("mark_v")

# Perform action
manager.perform_action("flying")

# Set state
manager.set_state(IMVAState.FLYING)

# Register event handler
def on_state_changed(data):
    print(f"State changed: {data['old_state']} → {data['new_state']}")

manager.register_event_handler("state_changed", on_state_changed)

# Launch assistant
manager.launch_assistant("mark_v")
```

## Extending the System

### Adding a New Armor

1. Add armor definition to `config/imva_armors_config.json`
2. Create assistant file in `scripts/python/`
3. Follow the pattern from existing armors

### Adding a New Action

1. Add action definition to `config/imva_actions_config.json`
2. Implement animation in assistant files
3. Register action requirements

### Adding a New Tony Variant

1. Add variant definition to `config/imva_armors_config.json`
2. Create assistant file in `scripts/python/`
3. Follow the pattern from existing variants

## Integration with JARVIS

IMVA integrates with the JARVIS role system:

- IMVA can be activated as a JARVIS role
- Actions can trigger JARVIS behaviors
- State changes can notify JARVIS systems

## Comparison with ACE

IMVA now matches ACE in comprehensiveness:

| Feature | ACE | IMVA |
|---------|-----|------|
| Multiple Variants | ✅ | ✅ |
| Action System | ✅ | ✅ |
| State Management | ✅ | ✅ |
| Event System | ✅ | ✅ |
| Character States | ✅ | ✅ |
| Outfit Management | ✅ | ✅ |

## Future Enhancements

- Voice integration
- Gesture recognition
- AI-driven behavior
- Multi-assistant coordination
- Advanced animations
- Physics simulation
