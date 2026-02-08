# 🔄 Kenny Experiment - Build-Deploy-Activate (B-D-A) System

## Overview

**Kenny B-D-A Experiment** provides an automated workflow for continuous iterative experimentation with Kenny:

- **BUILD**: Build/compile/prepare Kenny enhancements
- **DEPLOY**: Deploy Kenny to desktop
- **ACTIVATE**: Activate and run Kenny

## Phases

### 1. BUILD Phase

**Purpose:**
- Verify dependencies (tkinter, PIL, numpy)
- Check Kenny files exist
- Validate components
- Prepare configurations

**Checks:**
- Dependencies (tkinter, Pillow, numpy)
- Kenny files (kenny_imva_enhanced.py, kenny_sprite_components.py)
- Components (KennySpriteComponents)
- Configurations (data directories)

### 2. DEPLOY Phase

**Purpose:**
- Stop existing Kenny processes
- Prepare deployment environment
- Set up window management
- Initialize systems

**Actions:**
- Stop existing Kenny processes
- Prepare environment
- Setup window management
- Initialize systems

### 3. ACTIVATE Phase

**Purpose:**
- Start Kenny process
- Verify window visibility
- Monitor initial state

**Activates:**
- Kenny process
- Window visibility
- Initial state verification

## Usage

### Execute All Phases (B-D-A)

```python
from kenny_bda_experiment import KennyBDAExperiment, KennyBDAPhase

kenny_bda = KennyBDAExperiment()

# Execute full B-D-A workflow
result = kenny_bda.execute_bda(phase=KennyBDAPhase.ALL)
```

### Individual Phases

```python
# BUILD only
result = kenny_bda.build()

# DEPLOY only
result = kenny_bda.deploy()

# ACTIVATE only
result = kenny_bda.activate()
```

### CLI

```bash
# Execute all phases
python scripts/python/kenny_bda_experiment.py --all

# Individual phases
python scripts/python/kenny_bda_experiment.py --build
python scripts/python/kenny_bda_experiment.py --deploy
python scripts/python/kenny_bda_experiment.py --activate

# Check status
python scripts/python/kenny_bda_experiment.py --status
```

## Workflow

```
BUILD Phase
    ↓
    ├── Check Dependencies
    ├── Check Kenny Files
    ├── Validate Components
    └── Prepare Configurations
    ↓
DEPLOY Phase
    ↓
    ├── Stop Existing Processes
    ├── Prepare Environment
    ├── Setup Window Management
    └── Initialize Systems
    ↓
ACTIVATE Phase
    ↓
    ├── Start Kenny Process
    ├── Verify Window Visibility
    └── Check Initial State
    ↓
✅ Kenny Running on Desktop
```

## Continuous Experimentation

The Kenny B-D-A system enables continuous iterative experimentation:

1. **Make Changes**: Modify Kenny code/components
2. **BUILD**: Verify everything is ready
3. **DEPLOY**: Put changes in place
4. **ACTIVATE**: Run and test Kenny
5. **Observe**: See results on desktop
6. **Iterate**: Repeat with improvements

## Integration with Kenny Experiment

This B-D-A system integrates with:
- `kenny_imva_enhanced.py` - Main Kenny implementation
- `kenny_sprite_components.py` - Component system
- `find_and_show_kenny_window.py` - Window management
- `kill_kenny_processes.py` - Process management

## Status

✅ **Kenny B-D-A System** created  
✅ **BUILD phase** implemented  
✅ **DEPLOY phase** implemented  
✅ **ACTIVATE phase** implemented  
✅ **CLI** interface available  
✅ **Documentation** complete  

## Philosophy

**"Build, Deploy, Activate - Continuous Experimentation"**

- **BUILD**: Ensure everything is ready
- **DEPLOY**: Put everything in place
- **ACTIVATE**: Turn everything on
- **Automated**: One command does it all
- **Iterative**: Continuous improvement cycle
- **Reliable**: Each phase validates before proceeding

---

**Tags:** #KENNY #BDA #EXPERIMENT #BUILD #DEPLOY #ACTIVATE #CONTINUOUS_IMPROVEMENT @JARVIS @LUMINA
