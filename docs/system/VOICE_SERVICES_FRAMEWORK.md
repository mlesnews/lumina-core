# Voice Services Framework - ElevenLabs Primary with Fallbacks

**Date**: 2026-01-14  
**Status**: 📋 **FRAMEWORK DEFINITION**  
**Tags**: `#VOICE_SERVICES` `#ELEVENLABS` `#FRAMEWORK` `#FALLBACK` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Framework Strategy

**Primary**: **ElevenLabs** for all voice services  
**Fallbacks**: Multiple fallback providers for reliability

**Policy**: Use ElevenLabs as the primary voice service, with automatic fallback to alternative providers when ElevenLabs is unavailable or fails.

---

## 🏗️ Architecture

### Primary: ElevenLabs

**Why ElevenLabs**:
- ✅ High-quality, natural voice synthesis
- ✅ JARVIS voice character support
- ✅ Multilingual support
- ✅ Voice cloning capabilities
- ✅ Low latency
- ✅ Good API reliability

**Configuration**:
- **API Key**: Azure Key Vault (`elevenlabs-api-key`)
- **Config File**: `config/elevenlabs_config.json`
- **Voice ID**: JARVIS voice (auto-detected or configured)
- **Model**: `eleven_multilingual_v2` (default)

**Implementation**: `scripts/python/jarvis_elevenlabs_voice.py`

---

## 🔄 Fallback Strategy

### Fallback Chain

```
1. ElevenLabs (Primary)
   ↓ (if unavailable/fails)
2. Windows Speech API (TTS)
   ↓ (if unavailable/fails)
3. Azure Cognitive Services (Speech)
   ↓ (if unavailable/fails)
4. Google Cloud TTS
   ↓ (if unavailable/fails)
5. System Default TTS
```

### Fallback Triggers

**Automatic Fallback When**:
- ❌ ElevenLabs API key not available
- ❌ ElevenLabs API returns error
- ❌ ElevenLabs API timeout
- ❌ ElevenLabs quota exceeded
- ❌ Network connectivity issues
- ❌ ElevenLabs service unavailable

**Manual Fallback**:
- User preference override
- Cost optimization mode
- Offline mode

---

## 📋 Fallback Providers

### 1. Windows Speech API (TTS)

**Priority**: 2 (First Fallback)

**Pros**:
- ✅ Built into Windows (no API key needed)
- ✅ Offline capability
- ✅ Low latency
- ✅ Free

**Cons**:
- ⚠️ Lower quality than ElevenLabs
- ⚠️ Limited voice options
- ⚠️ Windows-only

**Implementation**: `pyttsx3` or Windows SAPI

**Usage**:
```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I am JARVIS")
engine.runAndWait()
```

---

### 2. Azure Cognitive Services (Speech)

**Priority**: 3 (Second Fallback)

**Pros**:
- ✅ High quality
- ✅ Neural voices available
- ✅ Multilingual support
- ✅ Good reliability

**Cons**:
- ⚠️ Requires API key (Azure Key Vault)
- ⚠️ Cost per request
- ⚠️ Requires internet

**Configuration**:
- **API Key**: Azure Key Vault (`azure-speech-api-key`)
- **Region**: Configured in Azure

**Implementation**: `azure.cognitiveservices.speech`

---

### 3. Google Cloud TTS

**Priority**: 4 (Third Fallback)

**Pros**:
- ✅ High quality
- ✅ Wide language support
- ✅ Neural voices

**Cons**:
- ⚠️ Requires API key (Azure Key Vault)
- ⚠️ Cost per request
- ⚠️ Requires internet

**Configuration**:
- **API Key**: Azure Key Vault (`google-tts-api-key`)

**Implementation**: `google-cloud-texttospeech`

---

### 4. System Default TTS

**Priority**: 5 (Last Resort)

**Pros**:
- ✅ Always available
- ✅ No configuration needed
- ✅ Free

**Cons**:
- ⚠️ Lowest quality
- ⚠️ Platform-dependent

**Implementation**: Platform-specific TTS

---

## 🔧 Implementation

### Voice Service Manager

**Create**: `scripts/python/jarvis_voice_service_manager.py`

**Features**:
- Primary: ElevenLabs
- Automatic fallback chain
- Error handling and retry logic
- Logging and transparency
- Cost tracking

**Decision Tree**: Use `ai_fallback` tree from `config/ai_decision_tree.json`

---

### Voice Service Interface

```python
class VoiceService:
    """Base voice service interface"""
    
    def speak(self, text: str) -> bool:
        """Speak text - returns True if successful"""
        pass
    
    def is_available(self) -> bool:
        """Check if service is available"""
        pass
    
    def get_quality(self) -> float:
        """Get service quality score (0.0-1.0)"""
        pass
```

---

### Voice Service Manager

```python
class VoiceServiceManager:
    """Manages voice services with fallback"""
    
    def __init__(self):
        self.services = [
            ElevenLabsVoiceService(),      # Primary
            WindowsTTSVoiceService(),      # Fallback 1
            AzureSpeechVoiceService(),     # Fallback 2
            GoogleTTSVoiceService(),        # Fallback 3
            SystemTTSVoiceService()        # Fallback 4
        ]
    
    def speak(self, text: str) -> bool:
        """Speak with automatic fallback"""
        for service in self.services:
            if service.is_available():
                try:
                    if service.speak(text):
                        logger.info(f"✅ Spoke using {service.name}")
                        return True
                except Exception as e:
                    logger.warning(f"⚠️  {service.name} failed: {e}")
                    continue
        
        logger.error("❌ All voice services failed")
        return False
```

---

## 📊 Configuration

### Voice Service Priority

**Config File**: `config/voice_services_config.json`

```json
{
  "version": "1.0.0",
  "primary": "elevenlabs",
  "fallbacks": [
    {
      "provider": "windows_tts",
      "priority": 2,
      "enabled": true
    },
    {
      "provider": "azure_speech",
      "priority": 3,
      "enabled": true,
      "api_key_secret": "azure-speech-api-key"
    },
    {
      "provider": "google_tts",
      "priority": 4,
      "enabled": true,
      "api_key_secret": "google-tts-api-key"
    },
    {
      "provider": "system_tts",
      "priority": 5,
      "enabled": true
    }
  ],
  "settings": {
    "auto_fallback": true,
    "retry_on_failure": true,
    "max_retries": 3,
    "timeout_seconds": 10
  }
}
```

---

## 🔄 Integration Points

### With Existing Systems

**JARVIS Voice Integration**:
- `jarvis_elevenlabs_voice.py` → Use VoiceServiceManager
- Automatic fallback on ElevenLabs failure
- Transparent to existing code

**Voice Interface System**:
- `voice_interface_system.py` → Use VoiceServiceManager
- Seamless fallback for TTS

**Passive/Active Voice**:
- `passive_active_voice_system.py` → Use VoiceServiceManager
- Fallback for voice output

---

## 📈 Benefits

### Reliability
- ✅ Always have a voice service available
- ✅ Automatic failover
- ✅ No single point of failure

### Quality
- ✅ Best quality when ElevenLabs available
- ✅ Acceptable quality with fallbacks
- ✅ Graceful degradation

### Cost Optimization
- ✅ Use free fallbacks when possible
- ✅ Track costs per provider
- ✅ Optimize provider selection

### Transparency
- ✅ Log which provider was used
- ✅ Track fallback usage
- ✅ Monitor service health

---

## 🚀 Implementation Steps

### Phase 1: Voice Service Manager

1. **Create** `jarvis_voice_service_manager.py`
2. **Implement** base VoiceService interface
3. **Implement** ElevenLabs service (primary)
4. **Implement** Windows TTS fallback
5. **Add** automatic fallback logic

### Phase 2: Additional Fallbacks

6. **Implement** Azure Speech fallback
7. **Implement** Google TTS fallback
8. **Implement** System TTS fallback
9. **Add** configuration file

### Phase 3: Integration

10. **Update** `jarvis_elevenlabs_voice.py` to use manager
11. **Update** `voice_interface_system.py` to use manager
12. **Update** other voice systems
13. **Add** logging and monitoring

### Phase 4: Optimization

14. **Add** cost tracking
15. **Add** quality metrics
16. **Add** health monitoring
17. **Tune** fallback logic

---

## 📝 Decision Flow

```
User Request → Voice Output Needed
    ↓
Check ElevenLabs Available?
    ├─ Yes → Use ElevenLabs
    │   ├─ Success → ✅ Done
    │   └─ Failure → Fallback
    └─ No → Fallback
    ↓
Check Windows TTS Available?
    ├─ Yes → Use Windows TTS
    │   ├─ Success → ✅ Done
    │   └─ Failure → Fallback
    └─ No → Fallback
    ↓
Check Azure Speech Available?
    ├─ Yes → Use Azure Speech
    │   ├─ Success → ✅ Done
    │   └─ Failure → Fallback
    └─ No → Fallback
    ↓
Check Google TTS Available?
    ├─ Yes → Use Google TTS
    │   ├─ Success → ✅ Done
    │   └─ Failure → Fallback
    └─ No → Fallback
    ↓
Use System TTS (Last Resort)
    ├─ Success → ✅ Done
    └─ Failure → ❌ Error
```

---

## 🔧 Configuration Example

### Voice Service Manager Usage

```python
from jarvis_voice_service_manager import VoiceServiceManager

manager = VoiceServiceManager()

# Speak with automatic fallback
success = manager.speak("Hello, I am JARVIS")

if success:
    print("✅ Voice output successful")
else:
    print("❌ All voice services failed")
```

---

## 📊 Monitoring

### Metrics to Track

- **Provider Usage**: Which provider was used
- **Fallback Rate**: How often fallback occurs
- **Success Rate**: Per-provider success rate
- **Latency**: Per-provider latency
- **Cost**: Per-provider cost
- **Quality**: Per-provider quality score

### Logging

**Log All**:
- Provider selection
- Fallback events
- Success/failure
- Latency
- Errors

**Location**: `data/voice_services/logs/`

---

## 🎯 Next Steps

1. **Create Voice Service Manager**:
   ```bash
   python scripts/python/jarvis_voice_service_manager.py
   ```

2. **Implement Fallbacks**:
   - Windows TTS
   - Azure Speech
   - Google TTS
   - System TTS

3. **Integrate with Existing Systems**:
   - Update `jarvis_elevenlabs_voice.py`
   - Update `voice_interface_system.py`
   - Update other voice systems

4. **Add Monitoring**:
   - Logging
   - Metrics
   - Health checks

---

## 📝 Summary

**Framework**: ElevenLabs Primary + Fallbacks

**Strategy**:
- ✅ ElevenLabs as primary (best quality)
- ✅ Automatic fallback chain (reliability)
- ✅ Multiple fallback providers (redundancy)
- ✅ Transparent to existing code (easy integration)

**Benefits**:
- Reliability (always have voice)
- Quality (best when available)
- Cost optimization (use free when possible)
- Transparency (know which provider used)

---

**Status**: 📋 **FRAMEWORK DEFINED**  
**Priority**: 🔴 **HIGH** - Voice services reliability  
**Next Action**: Create `jarvis_voice_service_manager.py`  
**Tags**: `#VOICE_SERVICES` `#ELEVENLABS` `#FRAMEWORK` `#FALLBACK` `@LUMINA` `@JARVIS` `#PEAK`
