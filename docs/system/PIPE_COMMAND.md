# PIPE Command

**Unix-style pipe command for ALL AI Chat workflows and ALL LUMINA workflows**

Like Unix pipes, but repurposed for ALL LUMINA workflows.

#JARVIS #LUMINA #PIPES #COMMAND #UNIX #ALL-WORKFLOWS

---

## Overview

The `pipe` command works like Unix pipes for **ALL LUMINA workflows**:

```
siphon <source> | pipe <pipe_name> | <destination>
```

**Philosophy**: Best programming logic, repurposed for ALL AI Chat workflows and ALL LUMINA workflows.

**Scope**: Works with ANY LUMINA workflow pipe - not just HVAC.

---

## Basic Usage

### List All Available Pipes

```bash
pipe --list
```

Shows all available pipes across ALL LUMINA workflows.

### Simple Pipe Execution

```bash
pipe hvac_email
```

Executes the `hvac_email` pipe with default settings.

**Works with ANY pipe name** - not just HVAC.

### Pipe with Source

```bash
pipe hvac_email --source email:"hvac OR furnace"
```

Siphons from email source, then pipes through `hvac_email`.

### Unix-Style Piping

```bash
siphon email:"hvac OR furnace" | pipe hvac_email
```

Classic Unix-style: siphon feeds into pipe.

### Pipe to File

```bash
pipe hvac_email --destination file:results.json
```

Pipes results to a file.

### Pipe to Stdout

```bash
pipe hvac_email --destination stdout
# or
pipe hvac_email --destination -
```

Pipes results to stdout (default behavior).

---

## Command Syntax

```
pipe <pipe_name> [--source <source>] [--destination <destination>] [options]
```

### Arguments

- **pipe_name**: Name of pipe to execute
  - `hvac_email` or `hvac` - HVAC email processing pipe

### Options

- `--source <source>`: Source to siphon from
  - `email:"query"` - Email source with query
  - `filesystem:/path` - Filesystem source with path
  - `database:connection` - Database source
  - `api:url` - API source

- `--destination <destination>`: Where to pipe results
  - `stdout` or `-` - Standard output (default)
  - `file:path` - File path
  - Just a path - Treated as file path

- `--format <format>`: Output format
  - `json` - JSON format (default)
  - `text` - Plain text
  - `yaml` - YAML format

### Pipe-Specific Options

#### HVAC Email Pipe

- `--query <query>`: Custom email search query
- `--days <days>`: Days to search back
- `--budget <budget>`: Budget for comparison

---

## Examples

### Example 1: Basic HVAC Email Pipe

```bash
pipe hvac_email
```

Processes HVAC emails with default settings.

### Example 2: Custom Query

```bash
pipe hvac_email --query "from:fletcher" --days 30
```

Searches for emails from Fletcher in last 30 days.

### Example 3: Custom Budget

```bash
pipe hvac_email --budget 15000
```

Uses $15,000 budget for comparison.

### Example 4: Unix-Style Piping

```bash
# Siphon emails, pipe through HVAC pipe, save to file
siphon email:"hvac OR furnace" | pipe hvac_email --destination file:results.json
```

### Example 5: Chain Multiple Pipes

```bash
# Siphon → Pipe → Another Pipe → Destination
siphon email:"hvac" | pipe hvac_email | pipe analyze | file:final.json
```

---

## How It Works

### 1. Input Stage

**From stdin** (Unix-style piping):
```bash
siphon email:"query" | pipe hvac_email
```

**From --source option**:
```bash
pipe hvac_email --source email:"query"
```

**From direct input**:
```bash
echo '{"data": "..."}' | pipe hvac_email
```

### 2. Processing Stage

Pipe executes all stages:
1. SYPHON - Extract from source
2. TRANSFORM - Transform data
3. ANALYZE - Analyze data
4. STORE - Store results

### 3. Output Stage

**To stdout** (default):
```bash
pipe hvac_email
```

**To file**:
```bash
pipe hvac_email --destination file:results.json
```

**To another pipe**:
```bash
pipe hvac_email | pipe analyze
```

---

## Perfect Synergy with Siphon

The `pipe` command is designed for **perfect synergy** with the `siphon` command:

```bash
# Classic Unix-style piping (perfect synergy!)
siphon email:"hvac OR furnace" | pipe hvac_email

# Siphon to file, then pipe
siphon email:"hvac OR furnace" > emails.json
cat emails.json | pipe hvac_email

# Or use pipe's internal siphon
pipe hvac_email --source email:"hvac OR furnace"
```

**Key Synergy Features:**
- ✅ `siphon` outputs JSON optimized for `pipe`
- ✅ `pipe` automatically detects `siphon` output format
- ✅ Seamless data flow between commands
- ✅ No data transformation needed
- ✅ Complementary commands: `siphon` extracts, `pipe` processes

See also: [SIPHON_PIPE_SYNERGY.md](SIPHON_PIPE_SYNERGY.md) for complete synergy documentation.

---

## Programmatic Usage

### In Python

```python
from scripts.python.pipe import pipe_command

# Execute pipe
result = pipe_command(
    pipe_name="hvac_email",
    source="email:hvac OR furnace",
    destination="file:results.json",
    query="from:fletcher",
    days=30
)
```

### In AI Chat

Just say:
- "pipe hvac_email"
- "siphon email:hvac | pipe hvac_email"
- "pipe hvac_email --query from:fletcher"

---

## Available Pipes

### Discover Pipes

```bash
pipe --list
```

Lists ALL available pipes across ALL LUMINA workflows.

### Built-in Pipes

1. **hvac_email** (or **hvac**)
   - HVAC email processing pipe
   - Stages: SYPHON → EXTRACT → ANALYZE → COMPARE → STORE
   - Options: `--query`, `--days`, `--budget`

### Custom Pipes

Create custom pipes in `data/pipes/<pipe_name>/pipe_config.json`

**Any LUMINA workflow can have a pipe** - financial, documents, calendar, tasks, etc.

---

## Error Handling

The pipe command:
- Returns exit code 0 on success
- Returns exit code 1 on failure
- Logs errors to stderr
- Outputs results to stdout (or destination)

---

## Best Practices

### 1. Use Unix-Style Piping

```bash
siphon <source> | pipe <pipe_name> | <destination>
```

### 2. Chain Pipes

```bash
siphon email:"query" | pipe hvac_email | pipe analyze | file:results.json
```

### 3. Use File Destinations

```bash
pipe hvac_email --destination file:results.json
```

### 4. Use JSON Format for Machine Processing

```bash
pipe hvac_email --format json
```

### 5. Use Text Format for Human Reading

```bash
pipe hvac_email --format text
```

---

## Philosophy

**"Best programming logic, repurposed for ALL AI Chat workflows and ALL LUMINA workflows"**

- Unix pipes: `command1 | command2 | command3`
- LUMINA pipes: `siphon source | pipe pipe_name | destination`
- Same concept, different domain
- Programmatic, composable, powerful
- **Perfect synergy**: `siphon` extracts, `pipe` processes - complementary commands
- **Works with ALL LUMINA workflows** - not just one use case

---

## Summary

The `pipe` command provides:

- ✅ **Unix-style syntax**: Familiar, powerful
- ✅ **AI workflow integration**: Works in chat
- ✅ **Composable**: Chain pipes together
- ✅ **Flexible**: Multiple sources and destinations
- ✅ **Programmatic**: Use in code or chat

**Just like Unix pipes, but for AI workflows.**

---

**Status**: ✅ **READY - Pipe command operational**
