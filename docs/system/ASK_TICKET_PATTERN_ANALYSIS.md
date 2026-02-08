# @ask Ticket Pattern Analysis & Recurrence Reporting

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#ASK` `#PATTERNS` `#RECURRENCE` `#ANALYSIS` `#SYPHON` `@JARVIS` `@LUMINA`

---

## Overview

The @ask Ticket Pattern Analyzer identifies **recurrences**, collates **similar tickets**, and extracts **patterns** for reporting and systemic issue detection. This enables:

- **Recurrence reporting** by area (team, tag, pattern type)
- **Similar ticket collation** to identify patterns
- **Systemic issue detection** across teams and time periods
- **Actionable insights** and recommendations

---

## Features

### 1. Recurrence Detection

**Identifies recurring patterns** in tickets:
- Groups tickets by @syphon patterns
- Calculates frequency and time span
- Identifies affected teams
- Determines severity (low, medium, high, critical)

**Recurrence Types**:
- **Pattern-based recurrences** - Same @syphon patterns
- **Tag-based recurrences** - Common tags across tickets
- **Team-based recurrences** - Recurring issues in specific teams
- **Time-based recurrences** - Clustered occurrences in time windows

### 2. Similar Ticket Detection

**Finds similar tickets** using text similarity:
- Calculates similarity scores between ticket texts
- Groups similar tickets together
- Identifies common keywords and tags
- Detects potential duplicates or related issues

**Similarity Metrics**:
- Text similarity (sequence matching)
- Keyword overlap
- Tag overlap
- Pattern overlap

### 3. Area-Based Analysis

**Analyzes recurrences by area**:
- **By Team** - Recurrences within specific teams
- **By Tag** - Recurrences with specific tags
- **By Pattern** - Recurrences of specific pattern types

### 4. Systemic Issue Detection

**Identifies systemic issues**:
- High-frequency patterns (5+ occurrences)
- Multi-team impact
- Cross-cutting concerns
- Root cause candidates

---

## Usage Examples

### 1. Generate Recurrence Report

```python
from ask_ticket_pattern_analyzer import AskTicketPatternAnalyzer

analyzer = AskTicketPatternAnalyzer()

# Generate report for last 30 days
report = analyzer.generate_recurrence_report(time_period_days=30)

# Generate report for specific team
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="JARVIS_TEAM",
    area_type="team"
)

# Generate report for specific tag
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="jarvis",
    area_type="tag"
)

# Generate report for specific pattern
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="error_resolution_pattern",
    area_type="pattern"
)
```

### 2. Collate Similar Tickets

```python
# Get pattern groups from report
pattern_groups = report.pattern_groups

# Collate similar tickets for a pattern
for pattern_group in pattern_groups:
    if pattern_group.pattern_type == "similarity":
        collated = analyzer.collate_similar_tickets(pattern_group)
        print(f"Pattern: {pattern_group.pattern_name}")
        print(f"Common tags: {collated['collated_analysis']['common_tags']}")
        print(f"Top keywords: {collated['collated_analysis']['top_keywords']}")
```

### 3. Command Line Usage

```bash
# Generate recurrence report for last 30 days
python scripts/python/ask_ticket_pattern_analyzer.py --report 30

# Generate report for specific team
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --area "JARVIS_TEAM" \
    --area-type team

# Generate report for specific tag
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --area "jarvis" \
    --area-type tag

# Collate similar tickets for a pattern
python scripts/python/ask_ticket_pattern_analyzer.py \
    --collate "pattern_error_resolution_pattern_0"

# Save report to specific file
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --output "reports/recurrence_20260112.json"
```

---

## Report Structure

### RecurrenceReport

```python
@dataclass
class RecurrenceReport:
    report_id: str
    generated_at: str
    time_period: str
    total_tickets: int
    unique_patterns: int
    pattern_groups: List[PatternGroup]
    area_breakdown: Dict[str, Any]
    top_recurrences: List[Dict[str, Any]]
    systemic_issues: List[Dict[str, Any]]
```

### PatternGroup

```python
@dataclass
class PatternGroup:
    pattern_id: str
    pattern_name: str
    pattern_type: str  # recurrence, similarity, systemic
    tickets: List[str]  # List of ask_ids
    common_tags: List[str]
    common_patterns: List[str]
    frequency: int
    first_occurrence: str
    last_occurrence: str
    affected_teams: List[str]
    severity: str  # low, medium, high, critical
    insights: List[str]
    recommendations: List[str]
```

---

## Report Output

### JSON Report Format

```json
{
  "report_id": "recurrence_20260112_153000",
  "generated_at": "2026-01-12T15:30:00",
  "time_period": "Last 30 days",
  "total_tickets": 150,
  "unique_patterns": 25,
  "pattern_groups": [
    {
      "pattern_id": "pattern_error_resolution_pattern_0",
      "pattern_name": "error_resolution_pattern Recurrence",
      "pattern_type": "recurrence",
      "tickets": ["ask_id_1", "ask_id_2", "ask_id_3"],
      "common_tags": ["error", "fix", "jarvis"],
      "common_patterns": ["error_resolution_pattern"],
      "frequency": 15,
      "first_occurrence": "2026-01-01T10:00:00",
      "last_occurrence": "2026-01-12T14:00:00",
      "affected_teams": ["JARVIS_TEAM", "SYSTEMS_TEAM"],
      "severity": "high",
      "insights": [
        "Pattern 'error_resolution_pattern' occurred 15 times",
        "Affects 2 team(s): JARVIS_TEAM, SYSTEMS_TEAM",
        "Time span: 12 days",
        "Frequency: 37.50 occurrences per month"
      ],
      "recommendations": [
        "Investigate root cause of recurring error_resolution_pattern pattern",
        "Consider systemic fix for error_resolution_pattern issues",
        "Coordinate across teams: JARVIS_TEAM, SYSTEMS_TEAM"
      ]
    }
  ],
  "area_breakdown": {
    "by_team": {
      "JARVIS_TEAM": {
        "count": 45,
        "tickets": ["ask_id_1", "ask_id_2", ...]
      }
    },
    "by_tag": {
      "jarvis": {
        "count": 30,
        "tickets": ["ask_id_1", "ask_id_2", ...]
      }
    },
    "by_pattern": {
      "error_resolution_pattern": {
        "count": 15,
        "tickets": ["ask_id_1", "ask_id_2", ...]
      }
    }
  },
  "top_recurrences": [...],
  "systemic_issues": [...]
}
```

---

## Analysis Capabilities

### 1. Recurrence Analysis

**Identifies**:
- How often patterns recur
- Time span of recurrences
- Frequency per month
- Affected teams

**Severity Levels**:
- **Critical**: 10+ occurrences
- **High**: 5-9 occurrences
- **Medium**: 3-4 occurrences
- **Low**: 2 occurrences

### 2. Similarity Analysis

**Detects**:
- Text similarity between tickets
- Common keywords
- Overlapping tags
- Potential duplicates

**Similarity Threshold**: 70% (configurable)

### 3. Area Breakdown

**Breaks down by**:
- **Team** - Tickets per team
- **Tag** - Tickets per tag
- **Pattern** - Tickets per pattern type

### 4. Systemic Issues

**Identifies**:
- High-frequency patterns (5+ occurrences)
- Multi-team impact
- Cross-cutting concerns
- Root cause candidates

---

## Use Cases

### 1. Team Performance Analysis

```python
# Analyze recurrences for JARVIS_TEAM
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="JARVIS_TEAM",
    area_type="team"
)

# Identify top recurring issues
for recurrence in report.top_recurrences:
    if "JARVIS_TEAM" in recurrence["affected_teams"]:
        print(f"Issue: {recurrence['pattern_name']}")
        print(f"Frequency: {recurrence['frequency']}")
        print(f"Recommendations: {recurrence['recommendations']}")
```

### 2. Tag-Based Pattern Analysis

```python
# Analyze recurrences for @jarvis tag
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="jarvis",
    area_type="tag"
)

# Find common patterns
for pattern_group in report.pattern_groups:
    if "jarvis" in pattern_group.common_tags:
        print(f"Pattern: {pattern_group.pattern_name}")
        print(f"Common tags: {pattern_group.common_tags}")
```

### 3. Systemic Issue Detection

```python
# Generate full report
report = analyzer.generate_recurrence_report(time_period_days=30)

# Identify systemic issues
for issue in report.systemic_issues:
    print(f"Systemic Issue: {issue['pattern_name']}")
    print(f"Frequency: {issue['frequency']}")
    print(f"Affected Teams: {issue['affected_teams']}")
    print(f"Severity: {issue['severity']}")
    print(f"Recommendations: {issue['recommendations']}")
```

### 4. Similar Ticket Collation

```python
# Get pattern groups
report = analyzer.generate_recurrence_report(time_period_days=30)

# Collate similar tickets
for pattern_group in report.pattern_groups:
    if pattern_group.pattern_type == "similarity":
        collated = analyzer.collate_similar_tickets(pattern_group)
        
        print(f"\nSimilar Tickets Group: {pattern_group.pattern_name}")
        print(f"Total tickets: {collated['collated_analysis']['total_tickets']}")
        print(f"Common tags: {collated['collated_analysis']['common_tags']}")
        print(f"Top keywords: {collated['collated_analysis']['top_keywords']}")
        print(f"Affected teams: {collated['collated_analysis']['affected_teams']}")
```

---

## Integration Points

### @SYPHON Integration
- Uses @syphon patterns for grouping
- Extracts intelligence from pattern groups
- Identifies actionable items

### @JARVIS Integration
- JARVIS can query recurrence reports
- Automatic pattern detection for workflow decisions
- Systemic issue alerts

### @R5 Integration
- R5 aggregates patterns from reports
- Knowledge aggregation from recurrence analysis
- Pattern library updates

### Database Integration
- Queries collation system database
- Cross-references tickets
- Generates reports from stored data

---

## Benefits

### 1. Proactive Issue Detection
- **Identify recurring issues** before they become critical
- **Detect systemic problems** early
- **Prevent escalation** through pattern recognition

### 2. Resource Optimization
- **Identify common patterns** for automation
- **Consolidate similar tickets** for efficiency
- **Focus efforts** on high-impact areas

### 3. Team Performance
- **Track team-specific patterns** for improvement
- **Identify training needs** based on recurrences
- **Measure improvement** over time

### 4. Root Cause Analysis
- **Group similar issues** for investigation
- **Identify common factors** across tickets
- **Generate actionable recommendations**

---

## Status

✅ **ACTIVE** - System is operational and ready for use

**Next Steps**:
1. Set up automated recurrence reporting
2. Create dashboards for visualization
3. Integrate with alerting system
4. Set up scheduled pattern analysis

---

**Tags**: `#ASK` `#PATTERNS` `#RECURRENCE` `#ANALYSIS` `#SYPHON` `@JARVIS` `@LUMINA` `#PEAK`
