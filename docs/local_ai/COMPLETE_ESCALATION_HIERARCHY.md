# Complete Escalation Hierarchy: Local AI → R5 → AIQ (JC/JHC) → Cloud AI

## Overview

The complete decision-making hierarchy prioritizes local AI and uses intelligent escalation through R5 Lattice and AIQ (AI Quorum) via Jedi Council and Jedi High Council.

## Complete Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    DECISION REQUEST                          │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   LOCAL AI    │ ← PRIMARY (Always first)
                    │   (Ollama)    │
                    │ llama3.2:11b  │
                    └───────┬───────┘
                            │
                    ┌───────┴───────┐
                    │               │
            ✅ Success      ❌ Fails/Complex
                    │               │
                    │               ▼
                    │       ┌───────────────┐
                    │       │  R5 LATTICE   │ ← DECISIONING
                    │       │   Evaluation  │
                    │       └───────┬───────┘
                    │               │
                    │       ┌───────┴───────┐
                    │       │               │
                    │   ✅ Can Handle   ❌ Needs Escalation
                    │       │               │
                    │       │               ▼
                    │       │       ┌───────────────┐
                    │       │       │  AIQ QUORUM   │ ← AI QUORUM
                    │       │       │   Requested   │
                    │       │       └───────┬───────┘
                    │       │               │
                    │       │       ┌───────┴───────┐
                    │       │       │               │
                    │       │   Standard      Critical
                    │       │       │               │
                    │       │       ▼               ▼
                    │       │   ┌─────────┐   ┌─────────────┐
                    │       │   │   JC     │   │     JHC     │
                    │       │   │  Jedi    │   │  Jedi High  │
                    │       │   │ Council │   │   Council   │
                    │       │   └────┬────┘   └──────┬──────┘
                    │       │        │               │
                    │       │        │               │
                    │       │        └───────┬───────┘
                    │       │                │
                    │       │        ┌────────┴────────┐
                    │       │        │  JHC Approves   │
                    │       │        │  Cloud AI?      │
                    │       │        └────────┬────────┘
                    │       │                 │
                    │       │        ┌────────┴────────┐
                    │       │        │                │
                    │       │    ✅ Yes           ❌ No
                    │       │        │                │
                    │       │        ▼                │
                    │       │   ┌──────────┐           │
                    │       │   │  CLOUD   │           │
                    │       │   │    AI    │           │
                    │       │   │(OpenAI/  │           │
                    │       │   │Anthropic)│           │
                    │       │   └────┬─────┘           │
                    │       │        │                 │
                    │       └────────┴─────────────────┘
                    │                │
                    └────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ RETURN RESULT │
                    │  (with path)  │
                    └───────────────┘
```

## Hierarchy Levels

### Level 1: Local AI (PRIMARY)
- **Always tried first**
- Models: `llama3.2:11b`, `codellama:13b`, `qwen2.5-coder:1.5b-base`
- Base URL: `http://10.17.17.11:3001`
- **If successful** → Return result immediately

### Level 2: R5 Lattice (DECISIONING)
- **Evaluates complexity** when local AI fails
- Uses R5 Living Context Matrix
- Determines if escalation needed
- **If can handle** → Return result
- **If complex** → Escalate to AIQ

### Level 3: AIQ Quorum (CONSENSUS)

#### 3a. Jedi Council (JC)
- **Standard AIQ consensus**
- Quorum: 3 providers
- Consensus threshold: 70%
- For moderate complexity decisions
- **If consensus reached** → Return result

#### 3b. Jedi High Council (JHC)
- **Critical decision approval**
- Final authority for cloud AI escalation
- Highest level review
- **If approves cloud AI** → Escalate to Level 4
- **If denies** → Return with JC consensus

### Level 4: Cloud AI (FALLBACK)
- **Only via JHC approval**
- Providers: OpenAI, Anthropic, Azure OpenAI
- Handles complex decisions
- **Return result** with full escalation path

## Configuration

**File**: `config/local_ai_r5_escalation_config.json`

### Key Settings

```json
{
  "preference": "local_ai",
  "local_ai": {
    "enabled": true,
    "preferred": true,
    "primary": true
  },
  "r5_escalation": {
    "enabled": true,
    "lattice_decisioning": true
  },
  "aiq_quorum": {
    "enabled": true,
    "jedi_council": {
      "enabled": true,
      "abbreviation": "JC"
    },
    "jedi_high_council": {
      "enabled": true,
      "abbreviation": "JHC"
    }
  },
  "cloud_ai_fallback": {
    "requires_aiq_approval": true,
    "requires_jedi_high_council": true
  }
}
```

## Escalation Rules

1. **Local AI Always First** - No exceptions
2. **R5 Evaluates Complexity** - Before any escalation
3. **AIQ for Consensus** - When multiple opinions needed
4. **JC for Standard** - Moderate complexity
5. **JHC for Critical** - Cloud AI approval required
6. **Cloud AI Last Resort** - Only with JHC approval

## Benefits

✅ **Local First** - Maximizes local resource usage
✅ **Smart Escalation** - R5 evaluates intelligently
✅ **Consensus Mechanism** - AIQ ensures quality
✅ **Governance** - JC/JHC provide oversight
✅ **Cost Control** - Cloud AI only when necessary
✅ **Transparency** - Full escalation path tracked

## Monitoring

All escalations are logged with:
- Escalation level reached
- Path taken (Local → R5 → AIQ → Cloud)
- JC/JHC decisions
- Cloud AI usage (if any)

## Examples

### Example 1: Simple Decision
```
Local AI → ✅ Success → Return
```

### Example 2: Moderate Complexity
```
Local AI → ❌ Fails
R5 Lattice → Evaluates → Escalate to AIQ
AIQ (JC) → Consensus → ✅ Return
```

### Example 3: Critical Decision
```
Local AI → ❌ Fails
R5 Lattice → Evaluates → Escalate to AIQ
AIQ (JC) → Consensus → Escalate to JHC
JHC → ✅ Approves Cloud AI
Cloud AI → ✅ Handles → Return
```

## Next Steps

1. ✅ Configuration complete
2. ⏳ Integrate R5 → AIQ → JC/JHC flow
3. ⏳ Test escalation paths
4. ⏳ (Optional) Add cloud AI credentials for fallback
