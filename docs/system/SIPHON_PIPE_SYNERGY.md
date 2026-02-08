# SIPHON & PIPE - Perfect Synergy

**Two commands, one workflow. Designed to work together seamlessly.**

#JARVIS #LUMINA #SYPHON #PIPE #SYNERGY

---

## Overview

**SIPHON** and **PIPE** are complementary commands designed for perfect synergy:

- **SIPHON**: Extract intelligence from sources
- **PIPE**: Process data through workflows

Together: `siphon <source> | pipe <pipe_name> | <destination>`

---

## Design Philosophy

### Complementary Commands

- **SIPHON** = First stage (extract)
- **PIPE** = Processing stage (transform, analyze, store)
- **Together** = Complete workflow

### Shared Architecture

- Both use `PipeContext` for data flow
- Both use `SyphonStage` for extraction
- Both support Unix-style piping
- Both use same output/input formats

### Perfect Integration

- SIPHON outputs JSON optimized for PIPE
- PIPE automatically detects SIPHON output
- Seamless data flow between commands
- No data transformation needed

---

## Usage Patterns

### Pattern 1: Classic Unix Piping

```bash
siphon email:"hvac OR furnace" | pipe hvac_email
```

**Flow:**
1. SIPHON extracts emails
2. Outputs JSON to stdout
3. PIPE reads from stdin
4. Processes through pipe stages
5. Outputs results

### Pattern 2: Explicit Source

```bash
pipe hvac_email --source email:"hvac OR furnace"
```

**Flow:**
1. PIPE uses internal SIPHON stage
2. Siphons from source
3. Processes through stages
4. Outputs results

### Pattern 3: Chain Multiple Pipes

```bash
siphon email:"query" | pipe hvac_email | pipe analyze | file:results.json
```

**Flow:**
1. SIPHON extracts
2. First PIPE processes
3. Second PIPE processes
4. Outputs to file

---

## Data Flow

### SIPHON Output Format

```json
{
  "success": true,
  "source_type": "email",
  "source": "hvac OR furnace",
  "siphoned_data": {
    "emails": [...],
    "total_emails": 5,
    "syphon_extracted": 3
  },
  "metadata": {...},
  "warnings": [],
  "errors": []
}
```

### PIPE Input Detection

PIPE automatically detects SIPHON output:
- Checks for `siphoned_data` key
- Extracts data for pipe context
- Preserves metadata
- Flags as `_from_siphon` for tracking

### PIPE Context Structure

```python
PipeContext(
    data={
        "siphoned_data": {...},  # From siphon
        "source_type": "email",   # From siphon
        "_from_siphon": True      # Flag
    }
)
```

---

## Integration Points

### 1. Shared SyphonStage

Both commands use the same `SyphonStage` class:
- Consistent extraction logic
- Same source types supported
- Same configuration format

### 2. PipeContext

Both use `PipeContext` for data:
- Standardized data structure
- Metadata preservation
- Error/warning tracking

### 3. Output Format

SIPHON outputs JSON by default:
- Optimized for PIPE consumption
- Structured data format
- Easy to parse

### 4. Error Handling

Both handle errors gracefully:
- SIPHON errors don't break PIPE
- PIPE can handle missing data
- Clear error messages

---

## Best Practices

### 1. Use Unix-Style Piping

```bash
# ✅ Good - explicit separation
siphon email:"query" | pipe hvac_email

# ✅ Also good - PIPE handles siphon internally
pipe hvac_email --source email:"query"
```

### 2. Consistent Format

```bash
# ✅ Good - JSON for machine processing
siphon email:"query" --format json | pipe hvac_email

# ⚠️  Less ideal - text format may need conversion
siphon email:"query" --format text | pipe hvac_email
```

### 3. Error Handling

```bash
# ✅ Good - check siphon success first
siphon email:"query" && pipe hvac_email

# ✅ Good - pipe handles siphon errors
siphon email:"query" | pipe hvac_email
```

---

## Examples

### Example 1: Email Processing

```bash
# Siphon emails, pipe through HVAC processing
siphon email:"hvac OR furnace" | pipe hvac_email --destination file:results.json
```

### Example 2: Filesystem Processing

```bash
# Siphon files, pipe through document processing
siphon filesystem:/path/to/docs | pipe document_processor
```

### Example 3: Multi-Stage Processing

```bash
# Siphon → Process → Analyze → Store
siphon email:"query" | pipe hvac_email | pipe analyze | file:final.json
```

### Example 4: Conditional Processing

```bash
# Only pipe if siphon succeeds
siphon email:"query" && pipe hvac_email
```

---

## Technical Details

### SIPHON Command

- **Purpose**: Extract from sources
- **Output**: JSON with `siphoned_data`
- **Format**: Optimized for PIPE
- **Integration**: Seamless with PIPE

### PIPE Command

- **Purpose**: Process through workflows
- **Input**: JSON from SIPHON or direct source
- **Detection**: Auto-detects SIPHON output
- **Integration**: Seamless with SIPHON

### Shared Components

- `SyphonStage`: Extraction logic
- `PipeContext`: Data structure
- `PipeStage`: Processing stages
- Output formats: JSON, text, yaml

---

## Synergy Benefits

### 1. Separation of Concerns

- SIPHON: Extraction only
- PIPE: Processing only
- Clear responsibilities

### 2. Composability

- Chain commands together
- Mix and match sources
- Flexible workflows

### 3. Reusability

- Use SIPHON output with any PIPE
- Use PIPE with any SIPHON source
- Modular design

### 4. Testability

- Test SIPHON independently
- Test PIPE independently
- Test together

---

## Summary

**SIPHON** and **PIPE** are designed for perfect synergy:

- ✅ **Complementary**: Each has clear purpose
- ✅ **Integrated**: Seamless data flow
- ✅ **Composable**: Work together naturally
- ✅ **Consistent**: Shared architecture
- ✅ **Powerful**: Unix-style flexibility

**Two commands, one workflow. Perfect synergy.**

---

**Status**: ✅ **SYNERGY COMPLETE - SIPHON & PIPE work together seamlessly**
