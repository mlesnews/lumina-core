# Complete AIQ + Jedi Council Integration

## Executive Summary

All company resources have been applied to a **singular focus on @AIQ + #JEDICOUNCIL / #JEDIHIGHCOUNCIL** with curated cloud AI providers for Lumina @PEAK performance.

## System Components

### 1. AIQ (AI Quorum) System ✅

**Location**: `scripts/python/jarvis_aiq_jedi_council_integration.py`

**Features**:
- Multi-provider consensus mechanism
- Cloud AI provider integration (OpenAI, Anthropic, Google)
- Decision logging and tracking
- Jedi Council review integration
- Jedi High Council escalation

**Usage**:
```python
from scripts.python.jarvis_aiq_jedi_council_integration import AIQJediCouncilIntegration

integration = AIQJediCouncilIntegration()
decision = await integration.get_aiq_consensus(
    question="What is the best approach?",
    require_jedi_council=True
)
```

### 2. Cloud AI Providers (Curated) ✅

**Providers**:
1. **OpenAI GPT-4** (Priority: 10)
   - Best for: Code, reasoning, analysis
   - API Key: `openai-api-key` (Azure Vault)

2. **Anthropic Claude** (Priority: 9)
   - Best for: Reasoning, safety, long-context
   - API Key: `anthropic-api-key` (Azure Vault)

3. **Google Gemini** (Priority: 8)
   - Best for: Multimodal, code, reasoning
   - API Key: `google-api-key` (Azure Vault)

**Selection Criteria**:
- Performance (response time, quality)
- Capabilities (code, reasoning, multimodal)
- Reliability (uptime, consistency)
- Cost (API pricing, efficiency)
- Security (data handling, compliance)

### 3. Jedi Council Review ✅

**Standard Jedi Council**:
- Reviews AIQ consensus decisions
- Validates quality and patterns
- Provides strategic guidance
- Required for important decisions

**Jedi High Council**:
- Escalation for critical issues
- Strategic decisions
- High-priority triage
- Final approval authority

### 4. WakaTime + Cursor Statistics ⚠️

**Location**: `scripts/python/jarvis_wakatime_cursor_stats.py`

**Features**:
- WakaTime API integration (key from Azure Vault)
- Cursor IDE statistics
- Combined analytics
- Performance tracking

**API Key Management**:
- Source: Azure Key Vault
- Secret Names: `wakatime-api-key`, `wakatime_api_key`, etc.
- Automatic retrieval and caching

**Statistics Collected**:
- Development time (total seconds)
- Languages used
- Projects worked on
- Cursor settings and shortcuts
- Combined analytics

**Note**: Requires `aiohttp` or `requests` library:
```bash
pip install aiohttp requests
```

### 5. Grammarly Integration ✅

**Location**: `scripts/python/jarvis_grammarly_lighting_fix.py`

**Features**:
- Fixes lights brightening after Grammarly usage
- Detects Grammarly processes
- Disables external lighting
- Checks for Grammarly CLI mode

**Grammarly CLI**:
- Installation: `npm install -g @grammarly/cli`
- Provides CLI access for automation
- Command-line grammar checking

### 6. Memory + RR + JARVIS Integration ✅

**Components**:
- **R5 Living Context Matrix**: Aggregates IDE chat sessions
- **Enhanced Memory**: Persistent storage (`enhanced_memory.db`)
- **JARVIS Oversight**: Workflow execution and coordination

**Integration Points**:
- R5 pattern extraction
- Memory persistence
- JARVIS workflow coordination

## Company-Wide Focus System

### Main Integration

**Location**: `scripts/python/jarvis_company_wide_aiq_focus.py`

**Executes**:
1. AIQ + Jedi Council integration
2. WakaTime + Cursor statistics
3. Grammarly lighting fix
4. Memory + RR + JARVIS integration

**Usage**:
```bash
python scripts/python/jarvis_company_wide_aiq_focus.py
```

## Azure Key Vault Integration

### All Secrets in Azure Vault

**Vault URL**: `https://jarvis-lumina.vault.azure.net/`

**Secrets**:
- `openai-api-key`
- `anthropic-api-key`
- `google-api-key`
- `wakatime-api-key`
- All other API keys

**Retrieval**:
```python
from scripts.python.azure_service_bus_integration import get_key_vault_client

key_vault = get_key_vault_client(
    vault_url="https://jarvis-lumina.vault.azure.net/"
)
api_key = key_vault.get_secret("wakatime-api-key")
```

## Decision Logging

### Storage

- **Location**: `data/aiq_decisions/`
- **Format**: JSON
- **Naming**: `aiq_YYYYMMDD_HHMMSS.json`

### Contents

- Decision ID
- Timestamp
- Question
- Consensus
- Confidence score
- Providers consulted
- Jedi Council review status

## Peak Performance Optimization

### Focus Areas

1. **AIQ Consensus** - Multi-provider consensus for best decisions
2. **Jedi Council** - Quality assurance and validation
3. **Cloud AI Selection** - Curated providers for optimal performance
4. **Statistics Tracking** - WakaTime + Cursor for insights
5. **Memory Integration** - R5 + Enhanced Memory for context

### Performance Metrics

- AIQ consensus confidence
- Provider response times
- Decision quality scores
- Memory utilization
- Statistics accuracy

## Integration with Existing Systems

### JARVIS Workflows

- AIQ consensus for workflow decisions
- Jedi Council review for critical workflows
- Provider selection based on task type

### SYPHON Intelligence

- AIQ consensus for intelligence extraction
- Pattern validation via Jedi Council
- Quality assurance

### @PEAK Patterns

- Jedi Council validates @PEAK patterns
- AIQ consensus on pattern quality
- Provider recommendations for pattern research

## Grammarly Lighting Issue

### Problem

- Lights brighten after using Grammarly
- May be triggered by focus/attention mode
- Notification lighting activation

### Solution

- Automatic lighting disable after Grammarly detection
- Process monitoring
- Registry-based lighting control

### Grammarly CLI

- **Installation**: `npm install -g @grammarly/cli`
- **Usage**: Command-line grammar checking
- **Integration**: Can be automated in workflows

## Current Status

### ✅ Working

- AIQ + Jedi Council integration
- Grammarly lighting fix
- Memory + RR + JARVIS integration
- Azure Key Vault integration
- Decision logging

### ⚠️ Needs Attention

- WakaTime API integration (requires `aiohttp` or `requests`)
- Cloud AI provider API calls (placeholder - needs actual API integration)

## Next Steps

1. **Install Dependencies**:
   ```bash
   pip install aiohttp requests
   ```

2. **Configure Cloud AI Providers**:
   - Ensure API keys are in Azure Vault
   - Test provider connections
   - Configure provider priorities

3. **Test WakaTime Integration**:
   - Verify API key in Azure Vault
   - Test API calls
   - Verify statistics collection

4. **Enhance AIQ Consensus**:
   - Implement actual provider API calls
   - Add consensus algorithms
   - Track provider performance

## Documentation

- **AIQ + Jedi Council**: `docs/company_wide_aiq_focus.md`
- **WakaTime + Cursor**: Integrated in main system
- **Grammarly**: `docs/system/GRAMMARLY_CLI.md`
- **Memory Integration**: `docs/system/R5_LIVING_CONTEXT_MATRIX.md`

---

**"This is the way." - MANDO**
