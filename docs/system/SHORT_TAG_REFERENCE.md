# Short-Tag Reference Guide

**Date**: 2025-01-27  
**Status**: ✅ **COMPLETE REFERENCE**  
**Tag**: `@triage` `#documentation` `#short-tags`  
**Type**: Chat Metatagging Shorthand

---

## Overview

Short-tags are a **chat metatagging shorthand** used throughout the Lumina | JARVIS ecosystem. They provide quick references to systems, processes, and concepts for efficient AI contextual chat confidence & context handling.

**Format**:
- `@tags` - Mentions (systems, people, processes)
- `#hashtags` - Categories (processes, principles, quality)

**Purpose**: Chat metatagging shorthand for:
- Quick system references
- Context building in conversations
- AI confidence & context handling
- Efficient communication shorthand

---

## @v3 - Verification Logic

### Definition

**@v3** = **V3 Verification Logic** - Workflow validation and verification system

### Purpose

**Three V's**: Verify, Validate, Verify (again)
- **V1**: Verify (initial check)
- **V2**: Validate (relevance check)
- **V3**: Verify (truth check - final verification)

### Characteristics

- **Always part of global workflow** - Runs before main workflow execution
- **Workflow validation** - Ensures workflows are correct before execution
- **Quality assurance** - Provides verification for astromech droid operations
- **Auto-verify enabled** - Automatically verifies workflows
- **Verification required** - Workflows must pass verification

### Integration

- **All droids use @v3** - Every droid has @v3 verification enabled
- **Pre-workflow execution** - Runs before any workflow starts
- **Post-workflow verification** - Verifies results after execution
- **Global verification system** - Coordinates verification across all systems

### Usage

```python
from v3_verification import V3Verification, V3VerificationConfig

config = V3VerificationConfig(
    enabled=True,
    auto_verify=True,
    verification_required=True
)

verifier = V3Verification(config)
passed, results = verifier.run_full_verification(workflow_data)
```

### Location

- **Module**: `scripts/python/v3_verification.py`
- **Class**: `V3Verification`
- **Config**: `V3VerificationConfig`

### When to Use @v3

- Before executing any workflow
- When validating droid operations
- When ensuring quality standards
- When coordinating multi-droid workflows
- When escalating to JARVIS

---

## @r5 - R5 Living Context Matrix

### Definition

**@r5** = **R5 Living Context Matrix** - Knowledge aggregation and context condensation system

### Purpose

**R5-D4 Astromech Droid** - "Keeper of the living context matrix"
- **Knowledge aggregation** - Continuously aggregates IDE chat sessions
- **Context condensation** - Creates the most concentrated form of knowledge
- **Pattern extraction** - Extracts @PEAK patterns from sessions
- **Thought experiments** - Captures @WHATIF scenarios
- **Force multiplier** - Stacks with n8n and Jupyter for maximum effectiveness

### Characteristics

- **Living document** - Continuously updated with new knowledge
- **Session aggregation** - Aggregates all IDE chat sessions
- **Pattern recognition** - Identifies reusable patterns (@PEAK)
- **Knowledge condensation** - Creates concentrated knowledge matrix
- **API server** - Provides API access to aggregated knowledge

### Integration

- **n8n workflows** - Automated aggregation workflows
- **Jupyter notebooks** - Analysis and visualization
- **IDE sessions** - Aggregates all chat sessions
- **@PEAK extraction** - Extracts high-quality patterns
- **@WHATIF scenarios** - Captures thought experiments

### Usage

```python
from r5_living_context_matrix import R5LivingContextMatrix

r5 = R5LivingContextMatrix(project_root)
r5.aggregate_sessions()
r5.extract_peak_patterns()
r5.generate_living_context_matrix()
```

### Location

- **Module**: `scripts/python/r5_living_context_matrix.py`
- **Class**: `R5LivingContextMatrix`
- **API Server**: `scripts/python/r5_api_server.py`
- **Data Directory**: `data/r5_living_matrix/`
- **Output**: `data/r5_living_matrix/LIVING_CONTEXT_MATRIX_PROMPT.md`

### When to Use @r5

- When aggregating knowledge from chat sessions
- When extracting reusable patterns
- When building context for decision-making
- When querying aggregated knowledge
- When accessing the living context matrix

---

## @grep - Pattern Search Tool

### Definition

**@grep** = **grep tool** - Pattern search and matching (WINS - highest precedence)

### Purpose

**Pattern Search Tool** - Primary tool for pattern matching and search operations
- **Highest precedence** - Primary tool reference in tag hierarchy
- **Pattern matching** - Search for patterns in code and files
- **Context building** - Find relevant code and systems

### Characteristics

- **WINS!** - Highest precedence in tag hierarchy
- **Primary tool** - Use for actual grep operations
- **Pattern search** - Search for patterns in codebase
- **Context weights** - High AI weight (0.9), high context weight (1.0)

### Precedence

**Order of Precedence**:
1. `@grep` - Highest precedence (WINS!)
2. `#syphon` - Lower ranked alias
3. `#patterns` - Lowest ranked, concepts

### Usage

```bash
@grep "pattern" file
@grep "self\.(stats|health|state)" scripts/python
```

### When to Use @grep

- For pattern searches in codebase
- When finding systems with specific patterns
- When searching for code patterns
- When building context from code structure

---

## #syphon - grep Alias

### Definition

**#syphon** = **grep alias** - Lower ranked synonym for grep

### Purpose

**Alias for grep** - `@syphon` loses "@" and gains "#" when lower ranked
- **Lower precedence** - Use as concept/alias reference
- **Longer synonym** - Alternative way to refer to grep
- **Concept reference** - Use when referring to grep as a concept

### Characteristics

- **Precedence 2** - Lower than @grep
- **Alias** - Alternative name for grep
- **Concept reference** - Use for lower priority searches

### Usage

```bash
#syphon "pattern" scripts/python
```

### When to Use #syphon

- When referring to grep as a concept
- For lower priority pattern searches
- As an alias/synonym for grep operations

---

## #patterns - Pattern Concepts

### Definition

**#patterns** = **Pattern concepts** - General pattern matching that pipes to @grep

### Purpose

**Pattern Concepts** - General pattern matching definitions
- **Lowest precedence** - Concepts that need execution
- **Pipe to @grep** - Must be piped to @grep (or #syphon) for execution
- **Pattern definitions** - Define patterns before searching

### Characteristics

- **Precedence 3** - Lowest in tag hierarchy
- **Concepts** - Pattern definitions, not execution
- **Pipes to @grep** - Needs @grep for actual search
- **Pattern library** - Store pattern definitions

### Usage

```
#patterns → @grep "pattern" | awk "pattern" | perl
Define #patterns then pipe to @grep for execution
```

### When to Use #patterns

- When defining pattern concepts
- When discussing pattern matching
- When patterns need to be executed via @grep
- When building pattern libraries

---

## Pattern Tag Hierarchy

### Order of Precedence

1. **`@grep`** - WINS! Highest precedence
   - Primary tool reference
   - Use for actual grep operations
   - Highest context weight

2. **`#syphon`** - Lower ranked alias
   - Alias for grep
   - Use as concept reference
   - Lower priority searches

3. **`#patterns`** - Lowest ranked concepts
   - Pattern definitions
   - Pipe to @grep for execution
   - Pattern concepts only

### Relationship

```
#patterns → @grep → results → processing
```

Pattern concepts (`#patterns`) are piped to execution tools (`@grep` or `#syphon`) to produce results.

---

## Short-Tag System

### Tag Types

**@tags (Mentions)**:
- `@lumina` - Project Lumina ecosystem
- `@jarvis` - J.A.R.V.I.S. system
- `@v3` - V3 Verification Logic
- `@r5` - R5 Living Context Matrix
- `@grep` - Pattern search tool (WINS - highest precedence)
- `@c3po` - C-3PO Protocol Droid (Helpdesk Coordinator)
- `@helpdesk` - Helpdesk system location

**#hashtags (Categories)**:
- `#peak` - PEAK quality standards
- `#decisioning` - Decision-making process
- `#audit` - Audit process
- `#triage` - Triage/assessment process
- `#TOYSAAC` - Think Of Yourself As A Customer
- `#syphon` - grep alias (lower ranked)
- `#patterns` - Pattern concepts (pipe to @grep)

### Context Weights

Each tag has context weights:
- **context_weight**: Overall importance (0.0-1.0)
- **ai_weight**: AI agent weighting
- **human_weight**: Human weighting

### Integration with Memory

Short-tags integrate with:
- **Memory Manager** - Stores tag context
- **Resource-Aware Context** - Checks tag context before AI queries
- **R5 System** - Aggregates tag usage
- **Holocron Archive** - References tag-based knowledge

---

## Relationship Between @v3 and @r5

### @v3 → @r5 Flow

1. **@v3 verifies** workflow before execution
2. **Workflow executes** (if @v3 passes)
3. **@r5 aggregates** session knowledge
4. **@r5 extracts** @PEAK patterns
5. **@r5 generates** living context matrix

### Combined Usage

```python
# @v3 verifies workflow
from v3_verification import V3Verification
verifier = V3Verification()
passed, results = verifier.run_full_verification(workflow_data)

if passed:
    # Execute workflow
    execute_workflow(workflow_data)
    
    # @r5 aggregates knowledge
    from r5_living_context_matrix import R5LivingContextMatrix
    r5 = R5LivingContextMatrix(project_root)
    r5.aggregate_session(session_data)
    r5.extract_peak_patterns()
```

---

## Quick Reference

| Tag | Type | Meaning | Usage | Precedence |
|-----|------|---------|-------|-----------|
| `@grep` | Mention | Pattern search tool | Pattern searches | 1 (WINS!) |
| `@v3` | Mention | V3 Verification Logic | Workflow validation | - |
| `@r5` | Mention | R5 Living Context Matrix | Knowledge aggregation | - |
| `@lumina` | Mention | Project Lumina | Ecosystem reference | - |
| `@jarvis` | Mention | J.A.R.V.I.S. system | System reference | - |
| `@c3po` | Mention | C-3PO Protocol Droid | Helpdesk coordinator | - |
| `@helpdesk` | Mention | Helpdesk location | Where droids work | - |
| `#syphon` | Hashtag | grep alias | Pattern search (alias) | 2 |
| `#patterns` | Hashtag | Pattern concepts | Pattern definitions | 3 |
| `#peak` | Hashtag | PEAK quality | Quality standards | - |
| `#decisioning` | Hashtag | Decision-making | Decision process | - |
| `#audit` | Hashtag | Audit process | Assessment | - |
| `#triage` | Hashtag | Triage/assessment | Evaluation | - |

---

## Examples

### Using @v3

```
"Before executing this workflow, @v3 verification is required"
"@v3 verified the workflow before execution"
"All workflows must pass @v3 verification"
```

### Using @r5

```
"@r5 aggregated the session knowledge"
"Check @r5 for aggregated patterns"
"@r5 extracted @PEAK patterns from the session"
"Query @r5 for context on this topic"
```

### Combined Usage

```
"@v3 verified the workflow, then @r5 aggregated the knowledge"
"After @v3 verification, @r5 extracted @PEAK patterns"
"@r5 can access @v3 verification results for context"
```

---

## Configuration

**Short-Tag Registry**: `config/shortag_registry.json`

**Current Tags**:
- `@jarvis` - J.A.R.V.I.S. system
- `@aiq` - AI Quorum system
- `@lumina` - Project Lumina ecosystem
- `@v3` - V3 Verification Logic
- `@r5` - R5 Living Context Matrix
- `@grep` - Pattern search tool (WINS - highest precedence)
- `#decisioning` - Decision-making process
- `#TOYSAAC` - Think Of Yourself As A Customer
- `#peak` - PEAK quality standards
- `#syphon` - grep alias (lower ranked)
- `#patterns` - Pattern concepts (pipe to @grep)

---

## Adding Tags to Registry

To add `@v3` and `@r5` to the registry:

```json
{
  "@v3": {
    "type": "mention",
    "category": "system",
    "description": "V3 Verification Logic - Workflow validation and verification",
    "context_weight": 1.0,
    "ai_weight": 0.8,
    "human_weight": 0.2
  },
  "@r5": {
    "type": "mention",
    "category": "system",
    "description": "R5 Living Context Matrix - Knowledge aggregation and context condensation",
    "context_weight": 1.0,
    "ai_weight": 0.9,
    "human_weight": 0.1
  }
}
```

---

**Last Updated**: 2025-01-27  
**Status**: ✅ Complete Reference  
**Maintained By**: Lumina Project Team

