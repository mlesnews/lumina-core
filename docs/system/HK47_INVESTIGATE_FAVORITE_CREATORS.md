# HK-47 Investigate Favorite Content Creators

## Overview

"STATEMENT: ANALYZING WATCH HISTORY TO IDENTIFY FAVORITE MEATBAGS, MASTER.
OBSERVATION: WATCH HISTORY REVEALS WHICH CONTENT CREATORS ARE MOST VIEWED.
QUERY: SHALL WE INVESTIGATE THESE FAVORITE CREATORS THOROUGHLY?
CONCLUSION: YES, MASTER. WE SHALL INVESTIGATE ALL FAVORITE MEATBAGS."

This workflow automatically:
1. **Extracts YouTube Watch History** - Analyzes your YouTube watch history
2. **Identifies Favorite Creators** - Finds most-watched content creators
3. **Runs HK-47 Background Checks** - Investigates each favorite creator thoroughly
4. **Generates Comprehensive Report** - Provides actionable insights and recommendations

---

## Purpose

Automatically identify and investigate your favorite content creators based on actual watch history, not assumptions. This provides:
- **Data-Driven Identification**: Based on actual viewing patterns
- **Comprehensive Investigation**: Full HK-47 background checks
- **Risk Assessment**: Trust scores for each creator
- **Actionable Recommendations**: Guidance for engagement decisions

---

## Workflow Steps (8 Steps)

### Step 1: Load Watch History
- Searches for YouTube watch history JSON file
- Handles multiple file formats and locations
- Loads watch history data

### Step 2: Analyze Watch History
- Extracts creator/channel information
- Calculates watch statistics per creator
- Tracks watch counts, watch time, dates
- Identifies video titles and categories

### Step 3: Identify Favorite Creators
- Sorts creators by watch count
- Selects top N creators (default: 10)
- Filters by minimum watch count (default: 3)

### Step 4: Prepare Investigation List
- Initializes investigation results
- Prepares creator data for background checks

### Step 5: Run Background Checks
- Executes HK-47 background check for each creator
- Investigates as content creators
- Collects comprehensive findings

### Step 6: Analyze Results
- Synthesizes all investigation results
- Calculates average trust scores
- Categorizes creators by trust level
- Identifies patterns and insights

### Step 7: Generate Recommendations
- Creates actionable recommendations
- Provides guidance for engagement
- Suggests monitoring strategies

### Step 8: Generate Final Report
- Consolidates all findings
- Creates comprehensive report
- Saves results for future reference

---

## Usage

### Command Line

```bash
# Basic usage (auto-finds watch history)
python scripts/python/hk47_investigate_favorite_creators.py

# Specify watch history file
python scripts/python/hk47_investigate_favorite_creators.py --history data/youtube/watch_history.json

# Customize parameters
python scripts/python/hk47_investigate_favorite_creators.py \
    --history data/youtube/watch_history.json \
    --min-watches 5 \
    --top-n 15

# JSON output
python scripts/python/hk47_investigate_favorite_creators.py --json
```

### Python API

```python
from hk47_investigate_favorite_creators import HK47InvestigateFavoriteCreators
import asyncio

async def investigate():
    workflow = HK47InvestigateFavoriteCreators(
        watch_history_file=Path("data/youtube/watch_history.json"),
        min_watch_count=3,
        top_n_creators=10
    )
    
    result = await workflow.execute()
    
    print(f"Favorite Creators: {len(result['favorite_creators'])}")
    print(f"Average Trust Score: {result['analysis']['average_trust_score']:.2%}")
    print(f"\n{result['hk47_assessment']}")

asyncio.run(investigate())
```

---

## Watch History File Format

The workflow supports multiple JSON formats:

### Format 1: Array of Entries
```json
[
  {
    "channelName": "Julia McCoy",
    "channelId": "UC...",
    "title": "Video Title",
    "time": "2025-01-27T12:00:00Z",
    "watchTime": "PT15M30S"
  }
]
```

### Format 2: Object with Items
```json
{
  "watch_history": [
    {
      "channel_name": "Julia McCoy",
      "channel_id": "UC...",
      "video_title": "Video Title",
      "timestamp": "2025-01-27T12:00:00Z"
    }
  ]
}
```

### Format 3: YouTube Takeout Format
```json
{
  "items": [
    {
      "channelTitle": "Julia McCoy",
      "channelId": "UC...",
      "title": "Video Title",
      "time": "2025-01-27T12:00:00Z"
    }
  ]
}
```

---

## Output Structure

```python
{
    "investigation_id": "hk47_fav_1234567890",
    "timestamp": "2025-01-27T12:00:00",
    "watch_history_summary": {
        "total_entries": 1000,
        "creators_analyzed": 50,
        "favorite_creators_count": 10
    },
    "favorite_creators": [
        {
            "name": "Julia McCoy",
            "watch_count": 25,
            "total_watch_time": 12500.0,
            "first_watched": "2024-01-15",
            "last_watched": "2025-01-27"
        }
    ],
    "investigation_results": [
        {
            "creator_name": "Julia McCoy",
            "watch_stats": {...},
            "investigation_status": "completed",
            "background_check": {
                "investigation_id": "...",
                "findings": {...},
                "risk_assessment": {
                    "trust_score": 0.75,
                    "overall_risk_level": "medium"
                }
            }
        }
    ],
    "analysis": {
        "total_creators": 10,
        "investigations_completed": 10,
        "investigations_failed": 0,
        "average_trust_score": 0.72,
        "high_trust_creators": ["Creator 1", "Creator 2"],
        "medium_trust_creators": ["Creator 3", "Creator 4"],
        "low_trust_creators": []
    },
    "recommendations": [
        "Continue monitoring favorite creators for consistency",
        "Engage with high-trust creators for partnerships",
        "Exercise caution with low-trust creators"
    ],
    "hk47_assessment": "Statement: Investigation of favorite meatbags complete..."
}
```

---

## Data Storage

Results are saved to:
```
data/hk47/favorite_creators/{investigation_id}.json
```

Each investigation creates a timestamped JSON file with:
- Watch history analysis
- Favorite creators list
- Complete background check results
- Analysis and recommendations

---

## Integration Points

### With HK47 Public Background Check
- Automatically runs background checks on identified creators
- Uses InvestigationType.CONTENT_CREATOR
- Full 15-step investigation for each creator

### With WorkflowBase
- Inherits mandatory step tracking
- Automatic completion verification
- Memory persistence
- Progress tracking

### With YouTube Data
- Can integrate with SYPHON YouTube extraction
- Can use YouTube Data API for additional information
- Can analyze subscriptions, likes, and recommendations

---

## Parameters

### `min_watch_count` (default: 3)
Minimum number of watches required to consider a creator.
- Lower = more creators included
- Higher = only most-watched creators

### `top_n_creators` (default: 10)
Number of top creators to investigate.
- Lower = faster investigation
- Higher = more comprehensive but time-consuming

### `watch_history_file`
Path to YouTube watch history JSON file.
- If not provided, searches common locations
- Supports multiple JSON formats
- Handles various field name variations

---

## Best Practices

### 1. Export Watch History Regularly
- Export from YouTube Takeout monthly
- Keep historical data for trend analysis
- Update investigations as viewing patterns change

### 2. Adjust Parameters
- Use `--min-watches` to filter noise
- Use `--top-n` based on investigation capacity
- Balance thoroughness with time constraints

### 3. Review Results Regularly
- Re-run investigations quarterly
- Track changes in trust scores
- Update engagement strategies based on findings

### 4. Use for Multiple Purposes
- **Affiliate Programs**: Identify potential affiliates
- **Partnerships**: Assess partnership viability
- **Content Strategy**: Understand viewing preferences
- **Risk Management**: Identify potential issues early

### 5. Combine with Other Data
- Cross-reference with subscriptions
- Compare with liked videos
- Analyze watch patterns over time

---

## Examples

### Example 1: Basic Investigation

```bash
python scripts/python/hk47_investigate_favorite_creators.py
```

**Output**:
- Analyzes watch history from default location
- Identifies top 10 creators (3+ watches)
- Runs background checks
- Generates report

### Example 2: Comprehensive Investigation

```bash
python scripts/python/hk47_investigate_favorite_creators.py \
    --history data/youtube/watch_history.json \
    --min-watches 5 \
    --top-n 20
```

**Output**:
- Analyzes specified watch history
- Identifies top 20 creators (5+ watches)
- More thorough investigation
- Larger report

### Example 3: Quick Check

```bash
python scripts/python/hk47_investigate_favorite_creators.py \
    --min-watches 10 \
    --top-n 5
```

**Output**:
- Only most-watched creators (10+ watches)
- Top 5 only
- Faster investigation
- Focused report

---

## HK-47 Assessment Format

HK-47's final assessment follows his characteristic speech pattern:

```
Statement: Investigation of favorite meatbags complete, master.
Observation: Analyzed watch history and investigated [N] favorite creators.
Analysis: [X] investigations completed, average trust score: [Y]%.
Conclusion: [Assessment based on trust scores]
Query: Shall we continue monitoring these meatbags?
Answer: Yes, master. Regular updates recommended.
```

---

## Limitations

### Watch History Availability
- Requires exported watch history file
- YouTube Takeout provides historical data
- Real-time data requires API access

### Investigation Time
- Each background check takes time
- More creators = longer investigation
- Consider running in batches for large lists

### Data Quality
- Depends on watch history accuracy
- Channel name variations may affect grouping
- Some creators may have limited public information

---

## Philosophy

### HK-47's Approach
- Data-driven identification (not assumptions)
- Thorough investigation (his wheelhouse)
- Pragmatic assessment
- Actionable recommendations

### Investigation Principles
- **Evidence-Based**: Uses actual watch history
- **Comprehensive**: Full background checks
- **Objective**: Fact-based assessments
- **Actionable**: Useful recommendations
- **Regular Updates**: Ongoing monitoring

---

## Conclusion

HK-47's Favorite Creators Investigation provides automated, data-driven identification and investigation of your most-watched content creators. By analyzing actual watch history and running comprehensive background checks, you gain actionable insights for engagement decisions.

**"STATEMENT: ANALYZING WATCH HISTORY TO IDENTIFY FAVORITE MEATBAGS, MASTER.
OBSERVATION: WATCH HISTORY REVEALS WHICH CONTENT CREATORS ARE MOST VIEWED.
QUERY: SHALL WE INVESTIGATE THESE FAVORITE CREATORS THOROUGHLY?
CONCLUSION: YES, MASTER. WE SHALL INVESTIGATE ALL FAVORITE MEATBAGS."**

**That is the Way.**

---

## Files

- `scripts/python/hk47_investigate_favorite_creators.py` - Main workflow
- `scripts/python/hk47_public_background_check.py` - Background check system
- `docs/system/HK47_INVESTIGATE_FAVORITE_CREATORS.md` - This documentation
- `data/hk47/favorite_creators/` - Investigation results storage

---

## References

- **HK-47**: Star Wars: Knights of the Old Republic (KOTOR)
- **Meatbags**: HK-47's term for humans
- **Jedi Pathfinder**: Qui-Gon Jinn logic for finding paths forward
- **WorkflowBase**: Lumina's mandatory step tracking system
- **SYPHON**: Intelligence extraction system

