# 🧠 Smart Adaptive Unlock System

## Overview

The Smart Unlock System is an intelligent, learning-based system that adapts to discover and unlock keyboard locks (FN and Windows keys) through multiple adaptive strategies.

## Features

### 1. **UI Element Discovery**
- **OCR Text Recognition**: Uses pytesseract to find text elements like "Device", "System Configuration", "Function Key", etc.
- **Color Analysis**: Detects interactive elements by analyzing button colors
- **Edge Detection**: Identifies UI boundaries and elements

### 2. **Adaptive Navigation**
- Uses discovered UI elements to navigate intelligently
- Tries multiple strategies based on what it finds
- Learns successful paths for future use

### 3. **Adaptive Registry Search**
- Dynamically searches all ASUS registry paths
- Finds lock-related values automatically
- Modifies discovered values to unlock

### 4. **Learning System**
- Saves discovered paths to `data/smart_unlock_config.json`
- Reuses successful navigation paths
- Tracks failed attempts to avoid repetition

## Usage

```bash
python scripts/python/jarvis_unlock_smart.py
```

## How It Works

1. **Discovery Phase**: Scans Armoury Crate UI using OCR, color analysis, and edge detection
2. **Navigation Phase**: Uses discovered elements to navigate to lock settings
3. **Registry Phase**: Searches and modifies registry values automatically
4. **Application Phase**: Restarts services to apply changes
5. **Learning Phase**: Saves successful paths for future use

## Requirements

```bash
pip install pyautogui pygetwindow pytesseract pillow
```

## Configuration

Learned paths are saved in `data/smart_unlock_config.json`:
```json
{
  "last_discovery": {
    "device_menu": [[x, y], ...],
    "system_config": [[x, y], ...],
    "lock_toggles": [[x, y], ...]
  }
}
```

## Future Enhancements

- Machine learning for UI element recognition
- Screenshot comparison to detect changes
- Automated testing of unlock success
- Multi-strategy execution with voting
- Cloud-based learning from multiple systems
