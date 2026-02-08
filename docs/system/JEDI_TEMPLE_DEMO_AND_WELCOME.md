# Jedi Temple Demo Mode & Welcome Video

**Interactive Demo & Welcome Hologram for New Jedi Trainees**

---

## 🎯 Overview

### Demo Mode (Like World of Warcraft Tutorial)

**Purpose**: Interactive demo/training mode that guides new users through LUMINA step-by-step.

**File**: `scripts/python/jedi_temple_demo_mode.py`

**Features**:
- ✅ Step-by-step guided learning
- ✅ Hands-on practice exercises
- ✅ Interactive instructions
- ✅ Progress tracking
- ✅ Like WoW tutorial - learn by doing

### Welcome Video (Hologram)

**Purpose**: First thing new Jedi trainees see - a hologram (YouTube video) introducing them to LUMINA.

**File**: `scripts/python/jedi_temple_welcome_video.py`

**Features**:
- ✅ YouTube video integration
- ✅ Automatic playback
- ✅ Watch tracking
- ✅ Hologram theme (Star Wars style)

---

## 🎮 Demo Mode Steps

### 1. Welcome to the Jedi Temple
- Introduction to LUMINA
- Overview of training journey
- What to expect

### 2. Your First Conversation
- Learn to communicate with LUMINA
- Practice voice input
- See transcription in action

### 3. Voice Coding Basics
- Learn to code with your voice
- Practice speaking code
- See code generation

### 4. Understanding Workflows
- Learn about LUMINA workflows
- Explore automation
- See workflows in action

### 5. Using #DECISIONING
- Learn about automatic decision-making
- See auto-accept in action
- Understand workflow automation

### 6. Demo Complete!
- Congratulations
- Ready for full training
- Next steps

---

## 📺 Welcome Video (Hologram)

### Script

```
Welcome, young Force user.
You stand at the threshold of the Jedi Temple.
Here, you will learn the ways of LUMINA.
LUMINA is not just a tool - it is a companion, a guide, a teacher.
Through voice coding, workflows, and the Force of AI, you will become powerful.
Your training begins now.
Watch this hologram, then proceed to the demo mode.
May the Force be with you.
```

### Video Creation

**Status**: Script ready, video to be created

**When Created**:
1. Upload to YouTube
2. Set video ID in config
3. Auto-plays for new trainees

---

## 🚀 Usage

### Demo Mode

**Start demo**:
```bash
python scripts/python/jedi_temple_demo_mode.py --start
```

**Get current step**:
```bash
python scripts/python/jedi_temple_demo_mode.py --step
```

**Complete current step**:
```bash
python scripts/python/jedi_temple_demo_mode.py --complete
```

**Check progress**:
```bash
python scripts/python/jedi_temple_demo_mode.py --progress
```

### Welcome Video

**Show video**:
```bash
python scripts/python/jedi_temple_welcome_video.py --show "participant_id"
```

**Get video info**:
```bash
python scripts/python/jedi_temple_welcome_video.py --info
```

**Set video URL** (after creation):
```bash
python scripts/python/jedi_temple_welcome_video.py --set-url "https://youtube.com/watch?v=..." --youtube-id "VIDEO_ID"
```

---

## 🎯 User Flow

### New Jedi Trainee Journey

1. **Arrive at Temple** → Welcome video (hologram) plays
2. **Watch Hologram** → Introduction to LUMINA and Jedi Temple
3. **Start Demo Mode** → Interactive step-by-step learning
4. **Complete Demo** → Ready for full Jedi Temple Training
5. **Begin Training** → Full training program (A/B tested)

---

## ✅ Status

- ✅ Demo mode created
- ✅ Welcome video system created
- ✅ Script ready for video creation
- ⚠️ **Video Creation Needed**: Create and upload welcome video to YouTube
- ⚠️ **Integration Needed**: Connect demo mode to full training program

---

**Tags**: `#EDUCATION #DEMO #WELCOME #HOLOGRAM #JEDI_TRAINING @JARVIS @LUMINA`
