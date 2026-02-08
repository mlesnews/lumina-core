# 📹🎤 MDV Conference Call - Advanced MDV with Audio & Camera

## Overview

**MDV Conference Call** is an enhanced version of MDV that includes:
- **All standard MDV features** (desktop video feed)
- **Audio capture** (microphone)
- **IR camera** (primary) - watching expressions and movements
- **Normal camera** (fallback)
- **Hybrid mode** (both cameras for testing)
- **Expression and movement tracking**

## Features

### 1. Desktop Video Feed (Standard MDV)
- Screenshot capture
- Video recording
- Vision control
- Desktop area extrapolation

### 2. Audio Capture
- Microphone input
- Real-time audio streaming
- Background audio capture
- PyAudio integration

### 3. Camera System

**IR Camera (Primary):**
- Infrared camera for expression/movement tracking
- Primary camera for operator observation
- Better for low-light conditions
- Enhanced expression detection

**Normal Camera (Fallback):**
- Standard webcam
- Used if IR camera unavailable
- Backup option
- Standard RGB capture

**Hybrid Mode:**
- Both cameras active simultaneously
- Testing and comparison mode
- Dual feed for enhanced tracking
- Best of both worlds

### 4. Expression & Movement Tracking
- Face detection
- Expression analysis
- Movement tracking
- MediaPipe integration
- Real-time processing

## Camera Modes

### IR Only (Primary)
```python
conference_call = JARVISMDVConferenceCall(camera_mode=CameraMode.IR_ONLY)
```

- Uses IR camera as primary
- Falls back to normal camera if IR unavailable
- Best for expression tracking

### Normal Only (Fallback)
```python
conference_call = JARVISMDVConferenceCall(camera_mode=CameraMode.NORMAL_ONLY)
```

- Uses normal camera only
- Fallback mode
- Standard RGB capture

### Hybrid (Testing)
```python
conference_call = JARVISMDVConferenceCall(camera_mode=CameraMode.HYBRID)
```

- Both cameras active
- Testing and comparison
- Enhanced tracking capabilities

## Usage

### Automatic Activation

MDV Conference Call can be activated automatically:

```python
from jarvis_auto_mdv_activator import auto_activate_mdv_on_submit

# Basic MDV
result = auto_activate_mdv_on_submit()

# MDV Conference Call (IR camera)
result = auto_activate_mdv_on_submit(conference_call_mode=True, camera_mode="ir_only")

# MDV Conference Call (Hybrid mode)
result = auto_activate_mdv_on_submit(conference_call_mode=True, camera_mode="hybrid")
```

### Direct Usage

```python
from jarvis_mdv_conference_call import JARVISMDVConferenceCall, CameraMode

# Create conference call system
conference_call = JARVISMDVConferenceCall(camera_mode=CameraMode.IR_ONLY)

# Activate
result = conference_call.activate_conference_call()

# Stop when done
conference_call.stop_conference_call()
```

### CLI

```bash
# Activate MDV Conference Call (IR camera)
python scripts/python/jarvis_mdv_conference_call.py --activate --camera-mode ir_only

# Activate with normal camera
python scripts/python/jarvis_mdv_conference_call.py --activate --camera-mode normal_only

# Activate hybrid mode
python scripts/python/jarvis_mdv_conference_call.py --activate --camera-mode hybrid
```

## Architecture

```
MDV Conference Call
│
├── Desktop Video Feed (MDV)
│   ├── Screenshot Capture
│   ├── Video Recording
│   └── Vision Control
│
├── Audio Capture
│   ├── Microphone Input
│   ├── Real-time Streaming
│   └── Background Capture
│
├── Camera System
│   ├── IR Camera (Primary)
│   ├── Normal Camera (Fallback)
│   └── Hybrid Mode (Both)
│
└── Expression & Movement Tracking
    ├── Face Detection
    ├── Expression Analysis
    └── Movement Tracking
```

## Why IR Camera?

**Infrared Camera Advantages:**
- Better expression detection
- Works in low-light conditions
- Enhanced movement tracking
- More accurate operator observation
- Better for facial analysis

**Fallback Strategy:**
- IR camera primary
- Normal camera fallback
- Hybrid mode for testing
- Automatic switching if IR unavailable

## Dependencies

### Required
- `opencv-python` - Camera capture
- `pyaudio` - Audio capture

### Optional
- `mediapipe` - Expression/movement tracking
- `speech_recognition` - Speech processing

### Installation

```bash
pip install opencv-python pyaudio
pip install mediapipe  # Optional, for tracking
```

## Status

✅ **MDV Conference Call** system created
✅ **Audio capture** implemented
✅ **IR camera** (primary) support
✅ **Normal camera** (fallback) support
✅ **Hybrid mode** implemented
✅ **Expression tracking** framework
✅ **Movement tracking** framework
⚠️  **Hardware detection** needs enhancement
⚠️  **IR camera detection** needs hardware-specific implementation

## Next Steps

- [ ] Enhance IR camera detection (hardware-specific)
- [ ] Improve expression tracking accuracy
- [ ] Add movement tracking algorithms
- [ ] Test hybrid mode performance
- [ ] Add camera switching logic
- [ ] Integrate with VLM for expression analysis
- [ ] Add audio processing pipeline
- [ ] Create conference call dashboard

## Testing

**Camera Mode Testing:**
1. Test IR camera detection
2. Test normal camera fallback
3. Test hybrid mode
4. Compare expression tracking between modes
5. Test automatic switching

**Expression Tracking Testing:**
1. Test face detection accuracy
2. Test expression recognition
3. Test movement tracking
4. Compare IR vs normal camera results

---

**Tags:** #MDV #CONFERENCE_CALL #AUDIO #CAMERA #IR #EXPRESSION_TRACKING #MOVEMENT_TRACKING @JARVIS @LUMINA
