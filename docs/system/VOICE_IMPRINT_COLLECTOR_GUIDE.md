# Voice Imprint Collector Guide

**Status:** ✅ Complete - Voice Profile Training and Improvement System

---

## 🎯 Purpose

The Voice Imprint Collector helps capture and improve voice profiles, specifically designed to help train and improve your wife's (Glenda's) voiceprint for better voice filtering and recognition.

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pyaudio numpy
```

**Note:** On Windows, you may need to install PyAudio wheel:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2. Train Wife's Voice Profile

```bash
python scripts/python/voice_imprint_collector.py --profile wife --name "Glenda" --train --samples 5
```

This will:
- Record 5 voice samples (5 seconds each)
- Extract voice features from each sample
- Create/update the voice profile in the library
- Save training metadata

### 3. Improve Existing Profile

```bash
python scripts/python/voice_imprint_collector.py --profile wife --improve --samples 3
```

This will:
- Record 3 additional samples
- Merge new features with existing profile (70% old, 30% new)
- Update the profile with improved accuracy

### 4. Analyze Profile

```bash
python scripts/python/voice_imprint_collector.py --profile wife --analyze
```

This shows:
- Current sample count
- Confidence threshold
- Success rate
- Voice features
- Profile status

---

## 📋 Usage Examples

### Record Single Sample

```bash
python scripts/python/voice_imprint_collector.py --profile wife --record --duration 10
```

Records a single 10-second sample.

### Train with Custom Samples

If you have existing audio files, you can modify the script to use them directly.

### Batch Training

Record multiple training sessions to improve accuracy:

```bash
# First training session
python scripts/python/voice_imprint_collector.py --profile wife --name "Glenda" --train --samples 5

# Second training session (improves existing)
python scripts/python/voice_imprint_collector.py --profile wife --improve --samples 5

# Third training session
python scripts/python/voice_imprint_collector.py --profile wife --improve --samples 5
```

---

## 🎤 Recording Tips

### Best Practices

1. **Quiet Environment**: Record in a quiet room with minimal background noise
2. **Consistent Distance**: Keep microphone at consistent distance (6-12 inches)
3. **Natural Speech**: Speak naturally, as you normally would
4. **Variety**: Include different:
   - Volume levels (normal, quiet, loud)
   - Speaking speeds (normal, slow, fast)
   - Emotional tones (neutral, happy, serious)
5. **Multiple Sessions**: Train over multiple sessions for better accuracy

### What to Say

- Read a paragraph from a book
- Describe your day
- Count from 1 to 20
- Say common phrases you use
- Speak naturally about any topic

---

## 📊 Features Extracted

The system extracts:

- **Duration**: Length of audio sample
- **Amplitude**: Volume characteristics (mean, std, max)
- **Dominant Frequency**: Primary frequency of voice
- **Energy**: Overall energy of the sample
- **Spectral Features**: Frequency domain characteristics

---

## 💾 Data Storage

### Audio Files
- Location: `data/voice_imprints/`
- Format: WAV files
- Naming: `{profile_id}_{timestamp}.wav`

### Training Metadata
- Location: `data/voice_imprints/`
- Format: JSON files
- Naming: `{profile_id}_training_{timestamp}.json`

### Voice Profiles
- Location: `data/voice_profile_library/voice_profiles.json`
- Integrated with Voice Profile Library System

---

## 🔧 Integration

The Voice Imprint Collector integrates with:

1. **Voice Profile Library System**: Stores and manages profiles
2. **Voice Filter System**: Uses profiles for filtering
3. **Transcription Systems**: Improves voice recognition accuracy

---

## 📈 Improving Accuracy

### More Samples = Better Accuracy

- **Minimum**: 5 samples for basic profile
- **Recommended**: 10-15 samples for good accuracy
- **Optimal**: 20+ samples for excellent accuracy

### Regular Updates

Improve the profile periodically:
- After voice changes (illness, aging)
- When accuracy decreases
- When adding new voice characteristics

### Quality Over Quantity

- Better to have 5 high-quality samples than 20 poor-quality ones
- Ensure good audio quality
- Minimize background noise

---

## 🎯 Use Cases

### 1. Initial Training
Train a new voice profile from scratch:
```bash
python scripts/python/voice_imprint_collector.py --profile wife --name "Glenda" --train --samples 10
```

### 2. Profile Improvement
Add more samples to improve existing profile:
```bash
python scripts/python/voice_imprint_collector.py --profile wife --improve --samples 5
```

### 3. Profile Analysis
Check current profile status:
```bash
python scripts/python/voice_imprint_collector.py --profile wife --analyze
```

### 4. Quick Recording
Record a single sample:
```bash
python scripts/python/voice_imprint_collector.py --profile wife --record --duration 8
```

---

## 🐛 Troubleshooting

### "Audio libraries not available"
```bash
pip install pyaudio numpy
```

### "No module named 'pyaudio'" (Windows)
```bash
pip install pipwin
pipwin install pyaudio
```

### "No audio input device found"
- Check microphone is connected
- Check microphone permissions in Windows
- Try a different microphone

### "Profile not found"
- Create profile first with `--train`
- Check profile ID spelling
- Verify profile exists in library

---

## ✅ Summary

**Voice Imprint Collector** provides:

- ✅ **Easy Recording**: Simple command-line interface
- ✅ **Feature Extraction**: Automatic voice feature analysis
- ✅ **Profile Training**: Create and improve voice profiles
- ✅ **Integration**: Works with Voice Profile Library System
- ✅ **Improvement**: Continuously improve accuracy with more samples

**Perfect for capturing and improving your wife's voiceprint!**

---

**Tags:** #VOICE_IMPRINT #VOICE_PROFILE #TRAINING #CAPTURE #IMPROVEMENT @JARVIS @LUMINA
