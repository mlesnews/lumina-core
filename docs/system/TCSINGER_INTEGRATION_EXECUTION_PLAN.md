# TCSinger Integration Execution Plan

## Goal
Get AI singing synthesis working for "Danny Boy" duet using TCSinger (zero-shot singing voice synthesis).

## Current Status
✅ TCSinger repository cloned to `models/singing_synthesis/TCSinger`
✅ Integration framework created (`jarvis_ai_singing_synthesis.py`)
✅ Duet system updated to use AI singing when available
✅ Phoneme conversion implemented
✅ Note-to-MIDI conversion implemented
✅ Prompt audio detection implemented
✅ Checkpoints directory structure created
⏳ Need to download pre-trained models from HuggingFace
⏳ Need to complete full inference implementation

## Execution Steps

### Step 1: Analyze TCSinger Structure (5 min)
- [ ] Read README.md to understand setup
- [ ] Check requirements.txt for dependencies
- [ ] Identify where pre-trained models go
- [ ] Find inference/example code

### Step 2: Install Dependencies (10 min)
- [ ] Install PyTorch (if not already installed)
- [ ] Install TCSinger requirements
- [ ] Verify all dependencies work

### Step 3: Get Pre-trained Models (15 min)
- [ ] Check if models are in repository
- [ ] Download pre-trained models (if needed)
- [ ] Verify model files are in correct location

### Step 4: Implement Integration (30 min)
- [ ] Study TCSinger inference code
- [ ] Implement `_sing_with_tcsinger2()` method
- [ ] Map lyrics + melody to TCSinger format
- [ ] Handle voice style parameters (tenor vs tenor2)
- [ ] Return audio in correct format (WAV bytes)

### Step 5: Test Integration (15 min)
- [ ] Test single phrase generation
- [ ] Test with "Danny Boy" lyrics
- [ ] Verify audio quality
- [ ] Check voice characteristics

### Step 6: Integrate with Duet System (10 min)
- [ ] Verify duet system calls AI singing
- [ ] Test JARVIS voice (tenor 1)
- [ ] Test Wanda voice (tenor 2)
- [ ] Test harmony/duet

### Step 7: Progressive Refinement (Ongoing)
- [ ] Fine-tune voice characteristics
- [ ] Adjust pitch accuracy
- [ ] Improve naturalness
- [ ] Perfect duet harmony

## Expected Timeline
- **Total**: ~85 minutes for basic working version
- **Phase 1 (Steps 1-6)**: Get it working
- **Phase 2 (Step 7)**: Progressive improvements

## Success Criteria
- ✅ TCSinger generates singing audio
- ✅ "Danny Boy" duet uses AI singing (not formant synthesis)
- ✅ Voices sound realistic (not robotic)
- ✅ Two voices sing in harmony

## Fallback Plan
If TCSinger setup is too complex:
- Try So-VITS-SVC (easier setup)
- Or DiffSinger (higher quality, slower)
- Keep formant synthesis as backup

## Next Action
Start with Step 1: Analyze TCSinger structure
