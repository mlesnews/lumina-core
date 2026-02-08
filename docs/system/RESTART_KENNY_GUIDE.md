# Restart Kenny Guide

**Date**: 2026-01-04  
**Status**: ✅ **READY**  
**Tags**: #KENNY #RESTART #WRAPPER #UTILITY @JARVIS @LUMINA

---

## Overview

The `restart_kenny.py` script is a wrapper that:
1. Kills any running Kenny processes
2. Waits for processes to terminate
3. Restarts Kenny with new code and any specified arguments

---

## Usage

```bash
python scripts/python/restart_kenny.py [kenny_args...]
```

All arguments are passed through to `kenny_imva_enhanced.py`.

---

## Examples

### Basic Restart
```bash
python scripts/python/restart_kenny.py
```
- Kills current Kenny
- Restarts with default settings (60px size)

### Match Ace's Size
```bash
python scripts/python/restart_kenny.py --match-ace
```
- Kills current Kenny
- Detects Ace's size and matches it

### Custom Size
```bash
python scripts/python/restart_kenny.py --size 60
```
- Kills current Kenny
- Restarts with 60px size

### Small Size
```bash
python scripts/python/restart_kenny.py --small-size
```
- Kills current Kenny
- Restarts with small avatar size (30px)

### Scale Factor
```bash
python scripts/python/restart_kenny.py --scale 1.0
```
- Kills current Kenny
- Restarts with scale factor 1.0 (default 60px)

### With Learning
```bash
python scripts/python/restart_kenny.py --match-ace --learn-aces
```
- Kills current Kenny
- Matches Ace's size
- Enables learning from Ace

---

## What It Does

1. **Kill Current Processes**
   - Finds all running Kenny/IMVA processes
   - Terminates them gracefully
   - Force kills if needed

2. **Wait for Termination**
   - Waits 1 second for processes to fully terminate
   - Ensures clean restart

3. **Restart Kenny**
   - Starts `kenny_imva_enhanced.py` with specified arguments
   - Runs in foreground (blocking)
   - Press Ctrl+C to stop

---

## When to Use

- After code changes to Kenny
- To apply new settings/arguments
- To verify fixes/changes
- To restart after crashes
- To change Kenny's size/behavior

---

## Notes

- **Foreground Execution**: Script runs in foreground (blocks until stopped)
- **Keyboard Interrupt**: Press Ctrl+C to stop Kenny
- **Clean Restart**: Always kills old processes first
- **Argument Passing**: All arguments passed through to Kenny

---

**Status**: ✅ **READY TO USE**

**Tags**: #KENNY #RESTART #WRAPPER #UTILITY #DOCS @JARVIS @LUMINA
