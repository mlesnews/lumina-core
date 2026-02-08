# Pattern Tag System - @grep vs #syphon vs #patterns

**Date**: 2025-01-27  
**Status**: ✅ **DOCUMENTED**  
**By**: @JARVIS

## Tag Hierarchy & Precedence

### Order of Precedence (Highest to Lowest)

1. **`@grep`** - WINS! Highest precedence
   - The actual tool/command
   - Direct reference to grep functionality
   - Use for primary pattern searches

2. **`#syphon`** - Lower ranked alias
   - Alias for grep
   - `@syphon` loses "@" and gains "#" when lower ranked
   - Longer synonym for grep operations
   - Use when referring to grep as a concept/pattern

3. **`#patterns`** - Lowest ranked, general pattern matching
   - General pattern matching concept
   - Pipe to `@grep` (or `#syphon`) for execution
   - Use for pattern definitions and concepts

## Usage Rules

### When to Use Each Tag

**`@grep`** - Use when:
- Actually executing grep commands
- Primary tool reference
- Highest priority searches

**`#syphon`** - Use when:
- Referring to grep as a concept
- Lower priority pattern searches
- As an alias/synonym for grep

**`#patterns`** - Use when:
- Defining pattern concepts
- General pattern matching discussions
- Needs to be piped to `@grep` for execution

### Pipe Operations

When working with `#patterns`:

```bash
# Pattern → grep → processing
grep "pattern" | awk "pattern" | perl
```

Or using tags:
```
#patterns → @grep → processing
```

## Example: Persistence Pattern Search

### Using @grep (Highest Precedence)

```bash
@grep "self\.(stats|health|state|count|sequence|history|metrics)\s*=" scripts/python
```

### Using #syphon (Lower Ranked Alias)

```bash
#syphon "persistence pattern" scripts/python
```

### Using #patterns (Concept, Pipe to @grep)

```bash
#patterns → @grep "self\.(stats|health|state)\s*="
```

## Pattern Detection Workflow

1. **Define Pattern** (`#patterns`)
   - Problem pattern: In-memory state, no persistence
   - Solution pattern: Save/load state, history tracking

2. **Search for Pattern** (`@grep` or `#syphon`)
   ```bash
   @grep "self\.(stats|health|state)\s*=" scripts/python
   ```

3. **Process Results** (pipe to other tools)
   ```bash
   @grep "pattern" | awk '{print $1}' | perl -pe 's/old/new/'
   ```

## Tag System Summary

| Tag | Precedence | Usage | Example |
|-----|-----------|-------|---------|
| `@grep` | Highest | Direct tool execution | `@grep "pattern" file` |
| `#syphon` | Medium | Alias/concept for grep | `#syphon "pattern"` |
| `#patterns` | Lowest | Pattern concepts | `#patterns → @grep` |

## Key Rule

**`@grep` WINS!** - Always use `@grep` for actual pattern searches. Use `#syphon` as lower-ranked alias, and `#patterns` for concepts that need to be piped to `@grep`.

---

**Remember**: When you have `#patterns`, pipe it to `@grep` (or `#syphon`) for execution.

