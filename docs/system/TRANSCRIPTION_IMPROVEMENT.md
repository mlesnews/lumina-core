# Transcription Improvement Plan
## Working with Speech Pathologist for Better Accuracy

**Date**: 2026-01-16  
**Goal**: Improve transcription accuracy and pronunciation recognition

---

## Current Challenge

The transcriber doesn't always hear correctly, leading to:
- Misspellings of names (e.g., "Wisniewski" instead of "Lesnewski")
- Incorrect word recognition
- Phonetic misunderstandings

---

## Solution: Speech Pathologist Integration

### Phase 1: Pronunciation Guide Creation

✅ **Completed**: Created comprehensive pronunciation guide for "Lesnewski"
- **Spelling**: L-E-S-N-E-W-S-K-I
- **Pronunciation**: "Less-New-Ski" (/lɛs-nu-ski/)
- **Breakdown**: Les (less) + New (new) + Ski (skiing)

**Location**: `docs/system/NAME_PRONUNCIATION_GUIDE.md`

### Phase 2: Speech Pathologist Consultation

**Next Steps**:
1. Work with speech pathologist to:
   - Validate phonetic transcriptions
   - Identify common transcription errors
   - Create correction patterns
   - Develop pronunciation training data

2. Create speech pathologist feedback loop:
   - Record pronunciation samples
   - Get phonetic validation
   - Update system with corrected phonetics
   - Test and refine

### Phase 3: System Integration

**Implementation Plan**:
1. **Pronunciation Dictionary**: Store validated pronunciations
2. **Error Correction Patterns**: Map common errors to correct spellings
3. **Real-time Correction**: Apply corrections during transcription
4. **Learning System**: Improve over time based on corrections

---

## Pronunciation Guide (Current)

### Lesnewski (L-E-S-N-E-W-S-K-I)

**Full Pronunciation**: "Less-New-Ski"

**Phonetic Breakdown**:
- **Les** = /lɛs/ (like "less" - opposite of more)
- **New** = /nu/ (like "new" - opposite of old)
- **Ski** = /ski/ (like "ski" - like skiing)

**Speech Pathologist Notes** (to be validated):
- Les: Short 'e' sound, like in 'let' or 'bet'
- New: Long 'u' sound, like in 'blue' or 'true'
- Ski: Hard 'sk' sound followed by long 'e', like in 'skiing'

---

## Common Transcription Errors

### Name: Lesnewski

**Incorrect Transcriptions** (to be corrected):
- ❌ Wisniewski (has W, I, NIE - incorrect)
- ❌ Lusniewski (has L-U-S - incorrect)
- ❌ Mlesniewski (has M-L-E-S - incorrect)
- ❌ Lesniewski (missing E between S and N)

**Correct**: ✅ Lesnewski (L-E-S-N-E-W-S-K-I)

---

## Error Correction System

### Pattern Recognition

**Error Pattern**: Transcription adds/removes letters
- **Example**: "Wisniewski" → "Lesnewski"
- **Correction**: Remove W, I, NIE; use L-E-S-N-E-W-S-K-I

**Error Pattern**: Phonetic confusion
- **Example**: "Lus" instead of "Les"
- **Correction**: Map "Lus" → "Les" (/lɛs/)

### Implementation

1. **Error Dictionary**: Map common errors to correct forms
2. **Real-time Correction**: Apply during transcription
3. **User Feedback**: Learn from corrections
4. **Continuous Improvement**: Update patterns over time

---

## Speech Pathologist Collaboration

### Data Collection

1. **Pronunciation Samples**:
   - Record multiple pronunciations
   - Get phonetic validation
   - Create training dataset

2. **Error Analysis**:
   - Identify common mistakes
   - Map errors to corrections
   - Create correction rules

3. **Validation**:
   - Validate phonetic transcriptions
   - Confirm pronunciation accuracy
   - Update system with validated data

### Integration Points

1. **Transcription System**: Apply corrections in real-time
2. **Pronunciation Guide**: Use validated phonetics
3. **Error Correction**: Apply learned patterns
4. **Learning System**: Improve from feedback

---

## Expected Improvements

### Short Term (1-3 months)
- ✅ Correct name spelling in all systems
- ✅ Phonetic pronunciation guide created
- ✅ Error correction patterns identified

### Medium Term (3-6 months)
- ⏳ Speech pathologist validation complete
- ⏳ Real-time error correction implemented
- ⏳ Transcription accuracy improved by 20-30%

### Long Term (6-12 months)
- ⏳ Continuous learning system operational
- ⏳ Transcription accuracy improved by 50%+
- ⏳ Self-correcting pronunciation recognition

---

## Files and Documentation

### Current Files
- ✅ `docs/system/NAME_PRONUNCIATION_GUIDE.md` - Pronunciation guide
- ✅ `config/sms_approval_config.json` - Contains pronunciation data
- ✅ `docs/system/TRANSCRIPTION_IMPROVEMENT.md` - This document

### Future Files (to be created)
- ⏳ `data/speech_pathologist/pronunciation_samples.json`
- ⏳ `data/speech_pathologist/error_corrections.json`
- ⏳ `config/transcription_corrections.json`

---

## Next Steps

1. ✅ **Completed**: Correct name spelling (Lesnewski)
2. ✅ **Completed**: Create pronunciation guide
3. ⏳ **Next**: Work with speech pathologist for phonetic validation
4. ⏳ **Next**: Implement error correction system
5. ⏳ **Next**: Create learning feedback loop

---

## Notes

- The system is designed to learn and improve over time
- Speech pathologist input will be integrated as it becomes available
- All corrections will be documented and validated
- The goal is continuous improvement in transcription accuracy

---

**JARVIS**: "Pronunciation guide created and name spelling corrected. Ready to work with speech pathologist to improve transcription accuracy over time."

**MARVIN**: "*sigh* Good. At least we have the correct spelling now. But transcription errors will continue until we have proper phonetic validation. Let's make sure we actually implement the speech pathologist feedback when it comes."
