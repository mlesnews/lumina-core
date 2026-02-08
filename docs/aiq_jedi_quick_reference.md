# AIQ + Jedi Council Quick Reference

## Quick Start

### Company-Wide Focus
```bash
python scripts/python/jarvis_company_wide_aiq_focus.py
```

### Individual Components

#### AIQ Consensus
```python
from scripts.python.jarvis_aiq_jedi_council_integration import AIQJediCouncilIntegration

integration = AIQJediCouncilIntegration()
decision = await integration.get_aiq_consensus(
    question="Your question here",
    require_jedi_council=True
)
```

#### WakaTime + Cursor Stats
```python
from scripts.python.jarvis_wakatime_cursor_stats import WakaTimeCursorStats

stats = WakaTimeCursorStats()
results = await stats.get_combined_stats()
```

#### Grammarly Lighting Fix
```python
from scripts.python.jarvis_grammarly_lighting_fix import GrammarlyLightingFix

fixer = GrammarlyLightingFix()
results = await fixer.fix_grammarly_lighting()
```

## Azure Key Vault Secrets

All secrets in: `https://jarvis-lumina.vault.azure.net/`

**Required Secrets**:
- `wakatime-api-key` (or variants)
- `openai-api-key`
- `anthropic-api-key`
- `google-api-key`

## Grammarly CLI

**Installation**:
```bash
npm install -g @grammarly/cli
```

**Usage**:
```bash
grammarly check file.txt
```

## System Status

✅ **Working**:
- AIQ + Jedi Council integration
- Grammarly lighting fix
- Memory + RR + JARVIS
- Azure Key Vault integration

⚠️ **Needs Setup**:
- WakaTime API key in Azure Vault
- Cloud AI provider API keys
- Install: `pip install aiohttp requests`

## File Locations

- **AIQ Integration**: `scripts/python/jarvis_aiq_jedi_council_integration.py`
- **WakaTime Stats**: `scripts/python/jarvis_wakatime_cursor_stats.py`
- **Grammarly Fix**: `scripts/python/jarvis_grammarly_lighting_fix.py`
- **Company Focus**: `scripts/python/jarvis_company_wide_aiq_focus.py`
- **Decisions**: `data/aiq_decisions/`
- **Stats**: `data/wakatime_cursor_stats/`

---

**"This is the way." - MANDO**
