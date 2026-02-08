# @ask Ticket System - Complete Overview

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#SYPHON` `#COLLATION` `#PATTERNS` `#DATABASE` `@JARVIS` `@LUMINA`

---

## System Architecture

The @ask Ticket System provides **complete ticket tracking, collation, and pattern analysis** across all ticket systems:

```
┌─────────────────────────────────────────────────────────────┐
│                    @ask Ticket System                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐    ┌──────────────────┐            │
│  │ Request ID       │    │ Ticket           │            │
│  │ Tracking         │───▶│ Collation        │            │
│  │                  │    │                  │            │
│  │ - Track IDs      │    │ - Link @ask      │            │
│  │ - Diagnostics    │    │ - Helpdesk       │            │
│  │ - Error tracking │    │ - GitLens        │            │
│  └──────────────────┘    │ - Tags           │            │
│                           │ - @syphon        │            │
│                           │ - Assignment     │            │
│                           └──────────────────┘            │
│                                    │                       │
│                                    ▼                       │
│                           ┌──────────────────┐            │
│                           │ Pattern           │            │
│                           │ Analyzer          │            │
│                           │                  │            │
│                           │ - Recurrences     │            │
│                           │ - Similar tickets │            │
│                           │ - Area analysis   │            │
│                           │ - Systemic issues │            │
│                           └──────────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Complete Workflow

### 1. Ticket Creation & Collation

```python
from ask_ticket_integration import AskTicketIntegration

integration = AskTicketIntegration()

# Track and collate @ask with tickets
result = integration.track_and_collate(
    request_id="cd5eb779-d000-4f45-8ea5-a0de9b47d07e",
    ask_text="@ask @jarvis @r5 #peak optimize workflow X",
    helpdesk_ticket="TICKET-20260112-0001",
    gitlens_ticket="#123",
    gitlens_pr="PR#456"
)
```

**What happens**:
1. Request ID is tracked with diagnostics
2. @ask is collated with helpdesk and GitLens tickets
3. Tags are extracted (@jarvis, @r5, #peak)
4. @syphon patterns are extracted
5. Ticket is assigned to team (JARVIS_TEAM)
6. Delegation flags are set
7. All data is stored in database

### 2. Pattern Analysis & Recurrence Reporting

```python
from ask_ticket_pattern_analyzer import AskTicketPatternAnalyzer

analyzer = AskTicketPatternAnalyzer()

# Generate recurrence report
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="JARVIS_TEAM",  # Optional: filter by area
    area_type="team"     # team, tag, or pattern
)

# Collate similar tickets
for pattern_group in report.pattern_groups:
    if pattern_group.pattern_type == "similarity":
        collated = analyzer.collate_similar_tickets(pattern_group)
        print(f"Common tags: {collated['collated_analysis']['common_tags']}")
        print(f"Top keywords: {collated['collated_analysis']['top_keywords']}")
```

**What happens**:
1. Queries all tickets in time period
2. Groups by patterns, tags, teams
3. Identifies recurrences
4. Finds similar tickets
5. Detects systemic issues
6. Generates insights and recommendations

---

## Reporting on Recurrences by Area

### Example: Team Recurrence Report

```python
# Analyze recurrences for JARVIS_TEAM
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="JARVIS_TEAM",
    area_type="team"
)

print(f"Total tickets: {report.total_tickets}")
print(f"Unique patterns: {report.unique_patterns}")

# Top recurrences
for recurrence in report.top_recurrences:
    print(f"\nPattern: {recurrence['pattern_name']}")
    print(f"Frequency: {recurrence['frequency']} occurrences")
    print(f"Severity: {recurrence['severity']}")
    print(f"Affected teams: {recurrence['affected_teams']}")
    print(f"Recommendations: {recurrence['recommendations']}")
```

### Example: Tag-Based Recurrence Report

```python
# Analyze recurrences for @jarvis tag
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="jarvis",
    area_type="tag"
)

# Area breakdown
print("Tag Breakdown:")
for tag, data in report.area_breakdown["by_tag"].items():
    print(f"  {tag}: {data['count']} tickets")
```

### Example: Pattern-Based Recurrence Report

```python
# Analyze recurrences for error_resolution_pattern
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="error_resolution_pattern",
    area_type="pattern"
)

# Systemic issues
for issue in report.systemic_issues:
    print(f"\nSystemic Issue: {issue['pattern_name']}")
    print(f"Frequency: {issue['frequency']}")
    print(f"Affected Teams: {issue['affected_teams']}")
    print(f"Insights: {issue['insights']}")
    print(f"Recommendations: {issue['recommendations']}")
```

---

## Collating Similar Tickets to Identify Patterns

### Similar Ticket Detection

```python
# Generate report
report = analyzer.generate_recurrence_report(time_period_days=30)

# Find similar tickets
for pattern_group in report.pattern_groups:
    if pattern_group.pattern_type == "similarity":
        # Collate similar tickets
        collated = analyzer.collate_similar_tickets(pattern_group)
        
        print(f"\n📋 Similar Tickets Group: {pattern_group.pattern_name}")
        print(f"   Total tickets: {collated['collated_analysis']['total_tickets']}")
        print(f"   Common tags: {collated['collated_analysis']['common_tags']}")
        print(f"   Common patterns: {collated['collated_analysis']['common_patterns']}")
        print(f"   Top keywords: {collated['collated_analysis']['top_keywords']}")
        print(f"   Affected teams: {collated['collated_analysis']['affected_teams']}")
        print(f"   Time span: {collated['collated_analysis']['time_span_days']} days")
        
        # Extract pattern insights
        print(f"\n   Pattern Insights:")
        for insight in pattern_group.insights:
            print(f"     - {insight}")
        
        print(f"\n   Recommendations:")
        for rec in pattern_group.recommendations:
            print(f"     - {rec}")
```

### Pattern Extraction from Similar Tickets

```python
# Get all similar ticket groups
similar_groups = [
    pg for pg in report.pattern_groups
    if pg.pattern_type == "similarity"
]

# Extract patterns
for group in similar_groups:
    collated = analyzer.collate_similar_tickets(group)
    
    # Identify pattern
    common_tags = collated['collated_analysis']['common_tags']
    top_keywords = collated['collated_analysis']['top_keywords']
    
    print(f"\n🔍 Pattern Identified:")
    print(f"   Pattern: {', '.join(common_tags[:3])}")
    print(f"   Keywords: {', '.join(top_keywords[:5])}")
    print(f"   Frequency: {group.frequency} occurrences")
    print(f"   Severity: {group.severity}")
    
    # Recommendations for pattern
    if group.severity in ["high", "critical"]:
        print(f"\n   ⚠️  Action Required:")
        print(f"     - Investigate root cause")
        print(f"     - Consider automation/template")
        print(f"     - Coordinate across teams: {', '.join(group.affected_teams)}")
```

---

## Database Queries for Pattern Analysis

### SQL Queries

```sql
-- Find all tickets with a specific pattern
SELECT * FROM ask_tickets 
WHERE syphon_patterns LIKE '%"error_resolution_pattern"%';

-- Find recurring patterns (appears 3+ times)
SELECT 
    syphon_patterns,
    COUNT(*) as frequency,
    GROUP_CONCAT(ask_id) as ticket_ids
FROM ask_tickets
GROUP BY syphon_patterns
HAVING frequency >= 3
ORDER BY frequency DESC;

-- Find tickets with common tags
SELECT 
    tags,
    COUNT(*) as frequency,
    GROUP_CONCAT(ask_id) as ticket_ids
FROM ask_tickets
GROUP BY tags
HAVING frequency >= 2
ORDER BY frequency DESC;

-- Find systemic issues (high frequency, multiple teams)
SELECT 
    assigned_team,
    syphon_patterns,
    COUNT(*) as frequency
FROM ask_tickets
WHERE syphon_patterns IS NOT NULL
GROUP BY assigned_team, syphon_patterns
HAVING frequency >= 5
ORDER BY frequency DESC;
```

---

## Command Line Examples

### Generate Recurrence Reports

```bash
# Full report (last 30 days)
python scripts/python/ask_ticket_pattern_analyzer.py --report 30

# Team-specific report
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --area "JARVIS_TEAM" \
    --area-type team

# Tag-specific report
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --area "jarvis" \
    --area-type tag

# Pattern-specific report
python scripts/python/ask_ticket_pattern_analyzer.py \
    --report 30 \
    --area "error_resolution_pattern" \
    --area-type pattern
```

### Collate Similar Tickets

```bash
# Collate similar tickets for a pattern
python scripts/python/ask_ticket_pattern_analyzer.py \
    --collate "pattern_error_resolution_pattern_0"
```

---

## Integration Workflow

### Complete End-to-End Example

```python
from ask_ticket_integration import AskTicketIntegration
from ask_ticket_pattern_analyzer import AskTicketPatternAnalyzer

# 1. Track and collate new @ask
integration = AskTicketIntegration()
result = integration.track_and_collate(
    request_id="new-request-id",
    ask_text="@ask @jarvis @r5 #peak fix connection error",
    helpdesk_ticket="TICKET-20260112-0002",
    gitlens_ticket="#124"
)

# 2. Generate recurrence report
analyzer = AskTicketPatternAnalyzer()
report = analyzer.generate_recurrence_report(
    time_period_days=30,
    area="JARVIS_TEAM",
    area_type="team"
)

# 3. Identify patterns
for pattern_group in report.pattern_groups:
    if pattern_group.frequency >= 3:
        print(f"Recurring pattern: {pattern_group.pattern_name}")
        print(f"Frequency: {pattern_group.frequency}")
        print(f"Recommendations: {pattern_group.recommendations}")

# 4. Collate similar tickets
similar_groups = [
    pg for pg in report.pattern_groups
    if pg.pattern_type == "similarity"
]

for group in similar_groups:
    collated = analyzer.collate_similar_tickets(group)
    print(f"\nSimilar tickets: {collated['collated_analysis']['total_tickets']}")
    print(f"Common tags: {collated['collated_analysis']['common_tags']}")
```

---

## Benefits

### 1. Comprehensive Tracking
- **Single source of truth** for all ticket relationships
- **Complete context** with tags, patterns, and intelligence
- **Full traceability** across systems

### 2. Pattern Recognition
- **Identify recurrences** before they become critical
- **Detect similar tickets** for consolidation
- **Extract patterns** for automation opportunities

### 3. Area-Specific Analysis
- **Team performance** tracking
- **Tag-based** pattern analysis
- **Pattern-type** recurrence detection

### 4. Systemic Issue Detection
- **High-frequency** pattern identification
- **Multi-team** impact analysis
- **Root cause** candidates

### 5. Actionable Insights
- **Automated recommendations** based on patterns
- **Severity classification** for prioritization
- **Team coordination** suggestions

---

## Status

✅ **ACTIVE** - Complete system operational

**Components**:
1. ✅ Request ID Tracking
2. ✅ Ticket Collation System
3. ✅ Pattern Analyzer
4. ✅ Recurrence Reporting
5. ✅ Similar Ticket Collation
6. ✅ Area-Based Analysis

**Next Steps**:
1. Set up automated recurrence reporting
2. Create dashboards for visualization
3. Integrate with alerting system
4. Set up scheduled pattern analysis

---

**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#SYPHON` `#COLLATION` `#PATTERNS` `#RECURRENCE` `#DATABASE` `@JARVIS` `@LUMINA` `#PEAK`
