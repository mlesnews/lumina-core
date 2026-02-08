# Time Tracking Systems Comparison - LUMINA

## Overview

LUMINA project uses multiple time tracking systems to monitor different aspects of development activity. This document compares statistics across all available tracking systems.

## Tracking Systems

### 1. WakaTime - Coding Time Tracking

**Purpose**: Tracks actual coding time across all projects and languages

**What it tracks**:
- Time spent coding in editors
- Languages used
- Projects worked on
- Editors/IDEs used
- Operating systems
- Daily/weekly/monthly summaries

**Data Source**:
- WakaTime API
- Automatic tracking via IDE plugins

**Access**:
- Dashboard: https://wakatime.com/dashboard
- API: https://wakatime.com/api/v1
- Badges: https://wakatime.com/share

**Integration**:
- ✅ Configured in LUMINA
- ✅ API client: `scripts/python/wakatime_integration.py`
- ✅ Badge updater: `scripts/python/update_wakatime_badges.py`

**Metrics Available**:
- Total coding hours (all time, last 7/30 days, etc.)
- Daily average hours
- Top languages by time
- Top projects by time
- Editor usage statistics
- Best coding day
- Time breakdown by file type

---

### 2. Cursor IDE - Session Tracking

**Purpose**: Tracks IDE usage, sessions, and interactions

**What it tracks**:
- IDE sessions
- Agent chat sessions
- File operations
- Extension usage
- Workspace state

**Data Source**:
- Cursor workspace files (`.cursor/workspace.json`)
- Session files in `data/agent_sessions/`
- Agent chat sessions in `data/agent_chat_sessions/`
- AI chat summaries in `data/ai_chat_summaries/`

**Access**:
- Workspace configuration: `.cursor/workspace.json`
- Session data: `data/agent_sessions/*.json`
- Chat summaries: `data/ai_chat_summaries/*.json`

**Integration**:
- ⚠️ Limited API access (Cursor may track internally)
- ✅ Session files available for analysis
- ✅ Chat summaries tracked

**Metrics Available**:
- Session count
- Agent chat session count
- Chat summary count
- Workspace configuration
- Layout state

**Note**: Cursor IDE may track usage internally, but detailed statistics may not be accessible via API. Session files provide some insight into IDE usage patterns.

---

### 3. AI Token Request Tracker

**Purpose**: Tracks AI interactions, token usage, and request patterns

**What it tracks**:
- AI request counts
- Token usage per provider
- Request success/failure rates
- Token budgets
- Agent-specific usage
- Master/Padawan learning patterns

**Data Source**:
- Configuration: `config/ai_token_request_tracker.json`
- Request logs: `.lumina/logs/ai_requests/`

**Access**:
- Config file: `config/ai_token_request_tracker.json`
- Logs directory: `.lumina/logs/ai_requests/`

**Integration**:
- ✅ Fully configured
- ✅ Tracks multiple AI providers
- ✅ Master/Padawan learning system integration

**Metrics Available**:
- Total requests (successful/failed)
- Total tokens used
- Average tokens per request
- Success rate
- Token budgets per provider
- Daily/monthly limits
- Agent-specific usage

**Providers Tracked**:
- GitHub Copilot
- Llama 3.2:3b (local)
- Azure AI
- And more...

---

### 4. GitLens Followup Automation

**Purpose**: Tracks Git operations and followup automation

**What it tracks**:
- Git followup actions
- Commit patterns
- Repository interactions

**Data Source**:
- Followup history: `data/gitlens_followup_automation/followup_history.jsonl`

**Access**:
- History file: `data/gitlens_followup_automation/followup_history.jsonl`

**Integration**:
- ✅ GitLens extension integrated
- ✅ Followup automation active

**Metrics Available**:
- Followup count
- Git operation patterns

---

## Comparison Script

A comprehensive comparison script is available to analyze all systems:

```bash
# Run comparison (requires WAKATIME_API_KEY for full WakaTime stats)
python scripts/python/time_tracking_comparison.py [range] [save_option]

# Examples:
python scripts/python/time_tracking_comparison.py all_time
python scripts/python/time_tracking_comparison.py last_30_days
python scripts/python/time_tracking_comparison.py last_7_days no-save
```

**Arguments**:
- `range`: WakaTime time range (`all_time`, `last_7_days`, `last_30_days`, `last_year`)
- `save_option`: `no-save` to skip saving output file

**Output**:
- Console: Formatted comparison report
- JSON file: `data/time_tracking/comparison_[timestamp].json`

---

## System Comparison Matrix

| System | Time Tracking | Session Tracking | Token Tracking | Git Tracking | API Access |
|--------|--------------|------------------|----------------|-------------|------------|
| **WakaTime** | ✅ Coding time | ❌ | ❌ | ❌ | ✅ Full API |
| **Cursor IDE** | ⚠️ Limited | ✅ Sessions | ❌ | ❌ | ⚠️ Limited |
| **AI Token Tracker** | ❌ | ✅ AI sessions | ✅ Tokens | ❌ | ✅ Config-based |
| **GitLens** | ❌ | ❌ | ❌ | ✅ Git ops | ⚠️ File-based |

---

## Key Metrics Summary

### Coding Time (WakaTime)
- **Total Hours**: Available via API
- **Daily Average**: Calculated from WakaTime data
- **Top Languages**: Python, JavaScript, etc.
- **Top Projects**: LUMINA and others

### IDE Usage (Cursor)
- **Session Count**: From session files
- **Chat Sessions**: Agent interactions
- **Workspace State**: Layout and configuration

### AI Interactions (Token Tracker)
- **Total Requests**: Tracked in config
- **Token Usage**: Per provider
- **Success Rate**: Request outcomes
- **Budgets**: Daily/monthly limits

### Git Operations (GitLens)
- **Followup Count**: Automation actions
- **Patterns**: Commit and operation trends

---

## Data Aggregation

The comparison script aggregates data from all systems to provide:

1. **Unified View**: All systems in one report
2. **Cross-System Analysis**: Compare metrics across systems
3. **Trend Analysis**: Historical patterns
4. **Gap Identification**: Missing or unavailable data

---

## Recommendations

### For Complete Time Tracking:

1. **WakaTime Setup**:
   - ✅ Already configured
   - Set `WAKATIME_API_KEY` environment variable
   - Enable project sharing for badges

2. **Cursor IDE**:
   - ⚠️ Limited API access
   - Use session files for manual analysis
   - Consider Cursor's internal analytics if available

3. **AI Token Tracker**:
   - ✅ Fully configured
   - Monitor token budgets regularly
   - Review request patterns

4. **GitLens**:
   - ✅ Active
   - Review followup history periodically

### Integration Opportunities:

1. **Unified Dashboard**: Combine all metrics in one view
2. **Automated Reports**: Generate weekly/monthly summaries
3. **Alerting**: Notify on budget thresholds or anomalies
4. **Visualization**: Create charts comparing systems

---

## Usage Examples

### Get WakaTime Stats Only

```python
from scripts.python.wakatime_integration import WakaTimeAPI
import os

api_key = os.getenv("WAKATIME_API_KEY")
client = WakaTimeAPI(api_key)
stats = client.get_stats("last_30_days")
print(f"Total hours: {stats['data']['total_seconds'] / 3600:.2f}")
```

### Run Full Comparison

```python
from scripts.python.time_tracking_comparison import TimeTrackingComparison
from pathlib import Path

project_root = Path(".")
comparison_tool = TimeTrackingComparison(project_root)
comparison = comparison_tool.compare_all_systems()
comparison_tool.print_comparison(comparison)
```

### Access Individual Systems

```python
# WakaTime
wakatime_stats = comparison_tool.get_wakatime_stats()

# Cursor
cursor_stats = comparison_tool.get_cursor_stats()

# AI Token Tracker
ai_stats = comparison_tool.get_ai_token_tracker_stats()

# GitLens
gitlens_stats = comparison_tool.get_gitlens_stats()
```

---

## Future Enhancements

1. **Real-time Dashboard**: Web-based dashboard showing all metrics
2. **Automated Alerts**: Budget and threshold notifications
3. **Historical Analysis**: Long-term trend analysis
4. **Export Options**: CSV, PDF reports
5. **Integration APIs**: REST API for external access

---

## Related Documentation

- [WakaTime Sharing Setup](WAKATIME_SHARING_SETUP.md)
- [WakaTime Quick Start](WAKATIME_QUICK_START.md)
- [AI Token Request Tracker Config](../config/ai_token_request_tracker.json)

---

**Last Updated**: 2026-01-09
**Maintained by**: LUMINA Team
