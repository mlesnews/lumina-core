# Bidirectional Chain-of-Command System

## Overview

**Top-down direct supervision and management of the entire company:**
- **BOTH sides of business** (Technical AND Business)
- **ALL divisions** covered
- **Chain-of-command works BOTH ways as a pipe** (bidirectional)
- Like "chain-of-thought" in programming - information flows both directions

## Architecture

### Bidirectional Pipe Model

```
TOP-DOWN (Directives):
@jarvis → @c3po → @r2d2 → Subordinate
  ↓         ↓        ↓
Directive Directive Directive

BOTTOM-UP (Reports):
Subordinate → @r2d2 → @c3po → @jarvis
     ↑          ↑        ↑
   Report    Report   Report
```

### Chain-of-Command Flow

**Top-Down (Supervisor → Manager → Subordinate):**
1. Supervisor creates directive
2. Directive flows down through chain
3. Each level acknowledges and executes
4. Results flow back up

**Bottom-Up (Subordinate → Manager → Supervisor):**
1. Subordinate reports status
2. Manager aggregates reports
3. Manager reports to supervisor
4. Supervisor receives complete picture

## Components

### 1. Directive System (`bidirectional_chain_of_command.py`)
- **Directive**: Top-down command from supervisor
- **Priority**: Critical, High, Normal, Low
- **Type**: Task, Project, Strategic, Operational, Urgent
- **Chain Path**: Tracks full path through hierarchy
- **Acknowledgment**: Recipients acknowledge receipt
- **Execution**: Track execution and results

### 2. Chain-of-Command Pipe
- **Bidirectional**: Both top-down and bottom-up
- **Technical Side**: Technical leads included
- **Business Side**: Business leads included
- **All Divisions**: Complete coverage
- **Active Tracking**: Pending, Active, Completed states

### 3. Integration with Supervision
- Integrated into `team_management_supervision.py`
- Processes directives during supervision cycles
- Routes reports through chain-of-command

## Features

### Top-Down Directives Include:
- Directive ID (DIR-YYYYMMDDHHMMSS-XXX)
- From supervisor
- To recipient (manager or subordinate)
- Type and priority
- Title, description, action required
- Division and team
- Technical and business leads
- Due date
- Chain-of-command path
- Acknowledgment and execution tracking

### Bottom-Up Reports Include:
- Task status from subordinates
- Progress percentage
- Blockers and issues
- Completion status
- Aggregated by managers
- Sent to supervisors

### Both Sides Covered:
- **Technical Side**: Technical leads, engineers, developers
- **Business Side**: Business leads, managers, coordinators
- **All Divisions**: Every division has chain-of-command pipes

## Usage

### Create Directive (Top-Down):
```python
from bidirectional_chain_of_command import BidirectionalChainOfCommand

chain = BidirectionalChainOfCommand()
directive = chain.create_directive(
    from_supervisor="@jarvis",
    to_recipient="@c3po",
    title="Ensure All Teams Report Status",
    description="All managers must report status to their supervisors.",
    action_required="Process all manager reports.",
    directive_type="operational",
    priority="high"
)
```

### Acknowledge Directive:
```python
chain.acknowledge_directive("DIR-20260110011500-JAR", "@c3po")
```

### Execute Directive:
```python
chain.execute_directive("DIR-20260110011500-JAR", "@c3po", "Completed successfully")
```

### Get Pending Directives:
```python
pending = chain.get_pending_directives("@c3po")
```

### Process All Pipes:
```bash
python bidirectional_chain_of_command.py --process-pipes
```

## Data Locations

- **Directives**: `data/chain_of_command/directives/`
- **Pipes**: `data/chain_of_command/pipes/`
- **Reports**: `data/team_management/reports/` (bottom-up)

## Status

✅ **ACTIVE** - Bidirectional chain-of-command operational
- Top-down directives flowing
- Bottom-up reports flowing
- Both technical and business sides covered
- All divisions included
- Works like chain-of-thought: bidirectional pipe

**Tags**: #MANAGEMENT #SUPERVISION #CHAIN_OF_COMMAND #BIDIRECTIONAL #REQUIRED @PEAK @JARVIS @LUMINA @RR @DOIT
