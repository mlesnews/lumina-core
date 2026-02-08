# @ask Ticket Collation System

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#SYPHON` `#COLLATION` `#DATABASE` `@JARVIS` `@LUMINA`

---

## Overview

The @ask Ticket Collation System creates **database-ready collated data** that links:
- **@ask directives** (Request IDs)
- **Helpdesk ticket numbers**
- **GitLens ticket/PR numbers**
- **Relevant @tags** for context enhancement
- **@syphon pattern extraction**
- **Delegation and follow-up flags**
- **Team/individual assignments**

This system enables powerful **queries and cross-referencing** across all ticket systems.

---

## Core Components

### 1. Database Schema

**Location**: `data/ask_ticket_collation/ask_tickets.db`

**SQLite Database** with the following structure:

- **Primary Table**: `ask_tickets`
- **Indexes**: Fast queries on helpdesk_ticket, gitlens_ticket, gitlens_pr, status, assigned_team, assigned_individual, delegation_flag, requires_follow_up
- **JSON Fields**: tags, mentions, hashtags, syphon_patterns, syphon_intelligence, related_asks, related_tickets, metadata

### 2. AskTicketRecord Model

**Data Model** with all collated information:

```python
@dataclass
class AskTicketRecord:
    # Core identifiers
    ask_id: str  # @ask directive / Request ID
    helpdesk_ticket: Optional[str]
    gitlens_ticket: Optional[str]
    gitlens_pr: Optional[str]
    
    # Tags and context
    tags: List[str]  # All @tags and #tags
    mentions: List[str]  # @mentions
    hashtags: List[str]  # #hashtags
    
    # @syphon pattern extraction
    syphon_patterns: List[str]
    syphon_intelligence: Dict[str, Any]
    
    # Delegation and follow-up
    delegation_flag: str
    requires_follow_up: bool
    
    # Assignment
    assigned_team: Optional[str]
    assigned_individual: Optional[str]
    
    # Status and priority
    status: str
    priority: str
```

---

## Features

### 1. Automatic Tag Extraction

**Extracts**:
- `@mentions` - System mentions (@jarvis, @r5, @v3, etc.)
- `#hashtags` - Concept tags (#peak, #decisioning, etc.)
- **All tags** - Combined list for comprehensive context

### 2. @syphon Pattern Extraction

**Patterns Detected**:
- **Workflow patterns** - Workflow/process/automation related
- **System integration patterns** - Integration with JARVIS, R5, V3, etc.
- **Error resolution patterns** - Error/fix/bug/issue related
- **Feature development patterns** - Add/create/implement/new feature
- **Optimization patterns** - Optimize/improve/enhance/performance

**Intelligence Extracted**:
- Extracted patterns
- Insights
- Actionable items

### 3. Delegation and Follow-up Flagging

**Delegation Flags**:
- `NONE` - No delegation needed
- `PENDING` - Delegation pending
- `DELEGATED` - Already delegated
- `FOLLOW_UP_REQUIRED` - Follow-up required
- `ESCALATED` - Escalated to higher priority

**Automatic Detection**:
- Delegation indicators: `@delegate`, `@assign`, `@helpdesk`, `@team`
- Escalation indicators: `@escalate`, `#urgent`, `#critical`, `#priority`
- Follow-up indicators: `@followup`, `@follow_up`, `@track`, `@monitor`

### 4. Team/Individual Assignment

**Automatic Team Assignment** based on tags:
- `@jarvis` → JARVIS_TEAM
- `@r5` → R5_TEAM
- `@v3` → V3_TEAM
- `@marvin` → MARVIN_TEAM
- `@helpdesk` → HELPDESK_TEAM
- `@aimlsea` → AIMLSEA_TEAM
- `@systems` → SYSTEMS_TEAM
- `@devops` → DEVOPS_TEAM
- **Default**: HELPDESK_TEAM

### 5. Query and Cross-Reference API

**Query Capabilities**:
- Query by @ask ID
- Query by helpdesk ticket
- Query by GitLens ticket
- Query by GitLens PR
- Query by status
- Query by assigned team/individual
- Query by delegation flag
- Query by follow-up requirement
- Query by tag (searches all tag fields)

**Cross-Reference**:
- Find all related records across ticket systems
- Auto-detect identifier type
- Return comprehensive relationship mapping

---

## Usage Examples

### 1. Collate an @ask with Tickets

```python
from ask_ticket_collation_system import AskTicketCollationSystem

system = AskTicketCollationSystem()

record = system.collate_ask(
    ask_id="cd5eb779-d000-4f45-8ea5-a0de9b47d07e",
    ask_text="@ask @jarvis @r5 #peak optimize workflow X",
    helpdesk_ticket="TICKET-20260112-0001",
    gitlens_ticket="#123",
    gitlens_pr="PR#456",
    source="/fix_command"
)
```

### 2. Query Records

```python
# Query by @ask ID
records = system.query(ask_id="cd5eb779-d000-4f45-8ea5-a0de9b47d07e")

# Query by helpdesk ticket
records = system.query(helpdesk_ticket="TICKET-20260112-0001")

# Query by assigned team
records = system.query(assigned_team="JARVIS_TEAM")

# Query by tag
records = system.query(tag="jarvis")

# Query by follow-up requirement
records = system.query(requires_follow_up=True)
```

### 3. Cross-Reference

```python
# Cross-reference by any identifier
results = system.cross_reference("cd5eb779-d000-4f45-8ea5-a0de9b47d07e")
results = system.cross_reference("TICKET-20260112-0001")
results = system.cross_reference("#123")
results = system.cross_reference("PR#456")
```

### 4. Integration with Request ID Tracking

```python
from ask_ticket_integration import AskTicketIntegration

integration = AskTicketIntegration()

result = integration.track_and_collate(
    request_id="cd5eb779-d000-4f45-8ea5-a0de9b47d07e",
    ask_text="@ask @jarvis @r5 #peak optimize workflow X",
    helpdesk_ticket="TICKET-20260112-0001",
    gitlens_ticket="#123",
    gitlens_pr="PR#456"
)
```

### 5. Command Line Usage

```bash
# Collate an @ask
python scripts/python/ask_ticket_collation_system.py \
    --collate "cd5eb779-d000-4f45-8ea5-a0de9b47d07e" \
    "@ask @jarvis @r5 #peak optimize workflow X" \
    "TICKET-20260112-0001" \
    "#123" \
    "PR#456"

# Query by @ask ID
python scripts/python/ask_ticket_collation_system.py \
    --query "cd5eb779-d000-4f45-8ea5-a0de9b47d07e"

# Cross-reference
python scripts/python/ask_ticket_collation_system.py \
    --cross-ref "TICKET-20260112-0001"

# Export all to JSON
python scripts/python/ask_ticket_collation_system.py \
    --export
```

---

## Database Queries

### SQL Examples

```sql
-- Find all @asks for a helpdesk ticket
SELECT * FROM ask_tickets WHERE helpdesk_ticket = 'TICKET-20260112-0001';

-- Find all pending follow-ups
SELECT * FROM ask_tickets WHERE requires_follow_up = 1 AND status = 'pending';

-- Find all @asks assigned to a team
SELECT * FROM ask_tickets WHERE assigned_team = 'JARVIS_TEAM';

-- Find all @asks with a specific tag
SELECT * FROM ask_tickets WHERE tags LIKE '%"jarvis"%';

-- Find all escalated @asks
SELECT * FROM ask_tickets WHERE delegation_flag = 'escalated';

-- Cross-reference: Find all related records
SELECT * FROM ask_tickets 
WHERE helpdesk_ticket = 'TICKET-20260112-0001'
   OR gitlens_ticket = '#123'
   OR gitlens_pr = 'PR#456';
```

---

## Integration Points

### @JARVIS Integration
- JARVIS can query collated data for workflow decisions
- Automatic assignment to JARVIS_TEAM when @jarvis tag detected

### @R5 Integration
- R5 can aggregate patterns from syphon_intelligence
- Knowledge aggregation from collated records

### @SYPHON Integration
- Automatic pattern extraction from @ask text
- Intelligence stored in syphon_intelligence field

### Request ID Tracking Integration
- Seamless integration with track_request_id.py
- Shared diagnostic and collation data

### GitLens Integration
- Automatic linking with GitLens tickets and PRs
- Follow-up automation integration

### Helpdesk Integration
- Automatic ticket number assignment
- Team/individual routing based on tags

---

## Data Export

### JSON Export

```python
# Export all records to JSON
output_path = system.export_to_json()
```

**Export Format**:
```json
{
  "exported_at": "2026-01-12T15:30:00",
  "total_records": 150,
  "records": [
    {
      "ask_id": "cd5eb779-d000-4f45-8ea5-a0de9b47d07e",
      "helpdesk_ticket": "TICKET-20260112-0001",
      "gitlens_ticket": "#123",
      "gitlens_pr": "PR#456",
      "tags": ["jarvis", "r5", "peak"],
      "syphon_patterns": ["workflow_pattern", "optimization_pattern"],
      "assigned_team": "JARVIS_TEAM",
      "requires_follow_up": true,
      ...
    }
  ]
}
```

---

## Benefits

### 1. Comprehensive Tracking
- **Single source of truth** for all ticket relationships
- **Complete context** with tags, patterns, and intelligence
- **Full traceability** across systems

### 2. Powerful Queries
- **Fast queries** with indexed database
- **Cross-referencing** across all ticket systems
- **Flexible filtering** by any field

### 3. Automated Workflows
- **Automatic tag extraction** and pattern detection
- **Intelligent assignment** based on tags
- **Delegation flagging** for follow-up management

### 4. Database-Ready
- **SQLite database** for immediate use
- **Easy migration** to PostgreSQL/MySQL if needed
- **JSON export** for backup and analysis

---

## Status

✅ **ACTIVE** - System is operational and ready for use

**Next Steps**:
1. Integrate with existing @ask processing workflows
2. Set up automated collation for new @ask directives
3. Create dashboards for query visualization
4. Set up automated exports for reporting

---

**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#SYPHON` `#COLLATION` `#DATABASE` `@JARVIS` `@LUMINA` `#PEAK`
