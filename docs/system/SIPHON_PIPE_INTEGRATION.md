# SIPHON & PIPE Integration

**Two commands, perfect synergy. Designed to work together seamlessly.**

#JARVIS #LUMINA #SYPHON #PIPE #INTEGRATION

---

## Design Principles

### Complementary Commands

- **SIPHON**: Extract intelligence from sources
- **PIPE**: Process data through workflows
- **Together**: Complete Unix-style workflow

### Shared Components

- `SyphonStage`: Used by both commands
- `PipeContext`: Shared data structure
- JSON format: Optimized for interoperability
- Error handling: Consistent across both

---

## Integration Points

### 1. Data Format

**SIPHON Output:**
```json
{
  "success": true,
  "source_type": "email",
  "siphoned_data": {...},
  "metadata": {...}
}
```

**PIPE Input Detection:**
- Automatically detects `siphoned_data` key
- Extracts data for pipe context
- Preserves metadata
- Flags as `_from_siphon` for tracking

### 2. Unix-Style Piping

```bash
siphon email:"query" | pipe hvac_email
```

**Flow:**
1. SIPHON outputs JSON to stdout
2. PIPE reads from stdin
3. PIPE detects siphon format
4. PIPE processes seamlessly

### 3. Shared SyphonStage

Both commands use the same `SyphonStage`:
- Consistent extraction logic
- Same source types
- Same configuration

---

## Usage Examples

### Example 1: Classic Piping

```bash
siphon email:"hvac OR furnace" | pipe hvac_email
```

### Example 2: Chain Multiple Pipes

```bash
siphon email:"query" | pipe hvac_email | pipe analyze
```

### Example 3: Conditional Processing

```bash
siphon email:"query" && pipe hvac_email
```

---

## Synergy Benefits

1. **Separation of Concerns**: SIPHON extracts, PIPE processes
2. **Composability**: Chain commands naturally
3. **Reusability**: Use SIPHON output with any PIPE
4. **Consistency**: Shared architecture and formats

---

**Status**: ✅ **PERFECT SYNERGY - SIPHON & PIPE work together seamlessly**
