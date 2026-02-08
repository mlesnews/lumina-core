# Local AI with R5 Lattice Escalation

## Overview

The system is configured to **prefer local AI models** and use the **R5 decisioning lattice** to escalate to cloud AI only when local models cannot handle complex decisions.

## Architecture

```
┌─────────────┐
│  Local AI   │ ← PRIMARY (Always tried first)
│  (Ollama)   │
└──────┬──────┘
       │
       │ If fails/complex
       ▼
┌─────────────┐
│ R5 Lattice  │ ← DECISIONING (Evaluates if escalation needed)
│  Decision   │
└──────┬──────┘
       │
       │ If R5 decides to escalate
       ▼
┌─────────────┐
│  AIQ        │ ← AI QUORUM (Consensus mechanism)
│  Quorum     │
└──────┬──────┘
       │
       ├─→ Jedi Council (JC) ← Standard AIQ consensus
       │
       └─→ Jedi High Council (JHC) ← Critical decisions
              │
              │ If JHC approves
              ▼
       ┌─────────────┐
       │  Cloud AI   │ ← FALLBACK (Only via R5 → AIQ → JHC)
       │ (OpenAI/etc) │
       └─────────────┘
```

## Configuration

**File**: `config/local_ai_r5_escalation_config.json`

### Key Settings

- **`preference: "local_ai"`** - Local AI is preferred
- **`local_ai.enabled: true`** - Local AI is primary
- **`r5_escalation.enabled: true`** - R5 lattice escalation enabled
- **`cloud_ai_fallback.only_on_escalation: true`** - Cloud AI only used when R5 escalates

## Escalation Flow

1. **Try Local AI First**
   - System attempts decision with local models (llama3.2:11b, etc.)
   - If successful → Return result

2. **Evaluate Complexity**
   - If local AI fails or complexity threshold exceeded
   - System evaluates via R5 decisioning lattice

3. **R5 Lattice Decision**
   - R5 living context matrix evaluates:
     - Decision complexity
     - Local model capability
     - Confidence threshold
     - Resource availability

4. **AIQ Quorum (If R5 Escalates)**
   - **Jedi Council (JC)**: Standard AIQ consensus
     - Multiple AI providers consulted
     - Quorum of 3 providers
     - Consensus threshold: 70%
   - **Jedi High Council (JHC)**: Critical decisions
     - Final approval authority
     - Required for cloud AI escalation
     - Highest level of review

5. **Cloud AI Escalation (If JHC Approves)**
   - Only if Jedi High Council approves
   - Cloud AI handles complex decision
   - Result returned with full escalation metadata

6. **Return Result**
   - Result returned with escalation path:
     - Local AI → R5 → AIQ (JC/JHC) → Cloud AI

## R5 Lattice Integration

The R5 decisioning lattice uses:
- **R5 Living Context Matrix** (`r5_living_context_matrix.py`)
- **R5 Service** (`api_r5_service.py`)
- **Decision Tree** (`universal_decision_tree.py`)

### Escalation Triggers

- `local_model_failure` - Local AI cannot process
- `complexity_threshold_exceeded` - Decision too complex
- `confidence_below_threshold` - Low confidence in local result
- `timeout_exceeded` - Local AI timeout
- `r5_decision_required` - R5 explicitly requires escalation

## AIQ (AI Quorum) Integration

AIQ achieves consensus through:
- **Jedi Council (JC)** (`jarvis_aiq_jedi_council_integration.py`)
  - Standard AIQ consensus
  - Quorum of 3 providers
  - For moderate complexity decisions
- **Jedi High Council (JHC)** (`jarvis_escalate_jedi_high_council.py`)
  - Critical decision approval
  - Final authority for cloud AI escalation
  - Highest level review

### AIQ Flow

1. **R5 Escalates to AIQ**
   - R5 determines AIQ needed
   - Routes to Jedi Council (JC)

2. **Jedi Council (JC) Consensus**
   - Multiple cloud AI providers consulted
   - Quorum reached (3 providers)
   - Consensus calculated

3. **Jedi High Council (JHC) Review**
   - If critical or cloud AI needed
   - JHC reviews and approves
   - Final authority for escalation

## Local AI Models

**Primary**: `llama3.2:11b`
**Fallback**: `codellama:13b`
**Lightweight**: `qwen2.5-coder:1.5b-base`

**Base URL**: `http://10.17.17.11:3001`
**Load Balancer**: `http://10.17.17.11:3000`

## Cloud AI Fallback

Cloud AI is **optional** and only used when:
1. Local AI fails
2. R5 lattice decides escalation is needed
3. Cloud AI credentials are configured

### To Add Cloud AI Fallback (Optional)

```bash
# Add OpenAI fallback
python scripts/python/configure_cloud_ai_decisioning.py --setup openai --interactive

# Or Anthropic
python scripts/python/configure_cloud_ai_decisioning.py --setup anthropic --interactive
```

## Monitoring

The system tracks:
- Local AI usage
- R5 escalation decisions
- Cloud AI fallback usage
- All escalations are logged

## Benefits

✅ **Local First** - Uses local resources when possible
✅ **Cost Effective** - Cloud AI only when needed
✅ **Smart Escalation** - R5 lattice makes intelligent decisions
✅ **No Resource Waste** - Cloud AI not used unnecessarily
✅ **Fallback Safety** - Cloud AI available for complex cases

## Testing

```bash
# Check system load
python scripts/python/aiq_fallback_decisioning.py --check-load

# Test decisioning
python scripts/python/aiq_fallback_decisioning.py --decision "test decision"

# Check R5 integration
python scripts/python/configure_local_ai_with_r5_escalation.py --check
```

## Next Steps

1. ✅ Configuration created
2. ⏳ Integrate R5 lattice into AIQ fallback decisioning
3. ⏳ Test escalation flow
4. ⏳ (Optional) Add cloud AI fallback credentials
