# Company-Wide AIQ + Jedi Council Focus

## Overview

All company resources applied to singular focus on **@AIQ + #JEDICOUNCIL / #JEDIHIGHCOUNCIL** with curated cloud AI providers for Lumina @PEAK performance.

## System Architecture

### Core Components

1. **AIQ (AI Quorum) System**
   - Multi-provider consensus mechanism
   - Cloud AI provider integration
   - Decision logging and tracking

2. **Jedi Council Review**
   - Standard review for important decisions
   - Quality assurance
   - Pattern validation

3. **Jedi High Council Escalation**
   - Critical decisions
   - High-priority issues
   - Strategic guidance

4. **Cloud AI Providers (Curated)**
   - OpenAI GPT-4 (Priority: 10)
   - Anthropic Claude (Priority: 9)
   - Google Gemini (Priority: 8)

5. **WakaTime + Cursor Statistics**
   - Development time tracking
   - IDE usage analytics
   - Performance metrics

6. **Memory + RR + JARVIS Integration**
   - R5 Living Context Matrix
   - Enhanced Memory
   - JARVIS oversight

## Usage

### Company-Wide Focus

```bash
python scripts/python/jarvis_company_wide_aiq_focus.py
```

This executes:
1. AIQ + Jedi Council integration
2. WakaTime + Cursor statistics
3. Grammarly lighting fix
4. Memory + RR + JARVIS integration

### AIQ Consensus

```python
from scripts.python.jarvis_aiq_jedi_council_integration import AIQJediCouncilIntegration

integration = AIQJediCouncilIntegration()

decision = await integration.get_aiq_consensus(
    question="What is the best approach for Lumina peak performance?",
    require_jedi_council=True,
    require_high_council=False
)
```

### WakaTime + Cursor Stats

```python
from scripts.python.jarvis_wakatime_cursor_stats import WakaTimeCursorStats

stats = WakaTimeCursorStats()
results = await stats.get_combined_stats()
```

## Cloud AI Provider Configuration

### Provider Selection Criteria

1. **Performance** - Response time, quality
2. **Capabilities** - Code, reasoning, multimodal
3. **Reliability** - Uptime, consistency
4. **Cost** - API pricing, efficiency
5. **Security** - Data handling, compliance

### Provider Priority

- **OpenAI GPT-4**: Priority 10 (highest)
  - Best for: Code, reasoning, analysis
  - API Key: `openai-api-key` (Azure Vault)

- **Anthropic Claude**: Priority 9
  - Best for: Reasoning, safety, long-context
  - API Key: `anthropic-api-key` (Azure Vault)

- **Google Gemini**: Priority 8
  - Best for: Multimodal, code, reasoning
  - API Key: `google-api-key` (Azure Vault)

## Jedi Council Review Process

### Standard Jedi Council

- Reviews AIQ consensus decisions
- Validates quality and patterns
- Provides strategic guidance
- Required for important decisions

### Jedi High Council

- Escalation for critical issues
- Strategic decisions
- High-priority triage
- Final approval authority

## WakaTime Integration

### API Key Management

- **Source**: Azure Key Vault
- **Secret Names**: 
  - `wakatime-api-key`
  - `wakatime_api_key`
  - `WakaTime-API-Key`
  - `WAKATIME_API_KEY`

### Statistics Collected

- Development time (total seconds)
- Languages used
- Projects worked on
- Daily/weekly summaries
- Combined with Cursor IDE stats

## Cursor IDE Statistics

### Data Collected

- Cursor settings
- Keyboard shortcuts
- Extension usage
- Configuration state

### Integration Points

- `.cursor/settings.json`
- `config/cursor_ide_keyboard_shortcuts.json`
- Extension registry

## Grammarly Integration

### Lighting Fix

- Detects Grammarly processes
- Fixes lights that brighten after Grammarly usage
- Disables external lighting

### CLI Mode

- Checks for Grammarly CLI installation
- Installation: `npm install -g @grammarly/cli`
- Provides CLI access for automation

## Memory + RR + JARVIS

### R5 Living Context Matrix

- Aggregates IDE chat sessions
- Extracts @PEAK patterns
- Generates living context matrix

### Enhanced Memory

- Persistent storage (`enhanced_memory.db`)
- Session history
- Knowledge aggregation

### JARVIS Oversight

- Workflow execution
- Quality assurance
- System coordination

## Peak Performance Optimization

### Focus Areas

1. **AIQ Consensus** - Best decisions through multi-provider consensus
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

## Configuration

### Azure Key Vault Secrets

All secrets stored in Azure Key Vault:
- `openai-api-key`
- `anthropic-api-key`
- `google-api-key`
- `wakatime-api-key`
- All other API keys

### Provider Configuration

```json
{
  "providers": [
    {
      "name": "OpenAI GPT-4",
      "enabled": true,
      "priority": 10,
      "api_key_secret_name": "openai-api-key"
    }
  ]
}
```

## Decision Logging

### Storage

- Location: `data/aiq_decisions/`
- Format: JSON
- Naming: `aiq_YYYYMMDD_HHMMSS.json`

### Contents

- Decision ID
- Timestamp
- Question
- Consensus
- Confidence
- Providers consulted
- Jedi Council review status

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

## Future Enhancements

1. **Advanced Consensus Algorithms**
   - Weighted voting
   - Confidence scoring
   - Provider reliability tracking

2. **Jedi Council AI Agents**
   - Automated review agents
   - Quality scoring
   - Pattern validation

3. **Provider Performance Tracking**
   - Response time metrics
   - Quality scores
   - Cost optimization

4. **Real-time Statistics**
   - Live WakaTime tracking
   - Cursor usage monitoring
   - Performance dashboards

---

**"This is the way." - MANDO**
