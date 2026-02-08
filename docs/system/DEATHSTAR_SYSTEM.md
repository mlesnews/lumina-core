# DEATHSTAR - Ultimate Text Processing Power

**The #deathstar represents ULTIMATE POWER - the peak of text processing capabilities.**

Combines the best of AWK, SED, and PERL into one unified battlestation.

#JARVIS #LUMINA #DEATHSTAR #AWK #SED #PERL #ULTIMATE-POWER #PEAK

---

## Overview

**DEATHSTAR** is the ultimate text processing system for LUMINA. It combines:

- **AWK**: Pattern scanning, field processing, data extraction
- **SED**: Stream editing, text transformation, pattern substitution
- **PERL**: Powerful regex, text manipulation, advanced scripting

**Philosophy**: Best programming logic, unified into one battlestation.

**Power Level**: 🌌 **ULTIMATE** - Maximum strength in the Galactic Multiversal Empire

---

## Design Principles

### 1. Native Power First

DEATHSTAR uses native tools when available:
- Native AWK (if available) - maximum AWK power
- Native SED (if available) - maximum SED power
- Native PERL (if available) - maximum PERL power

### 2. Python Fallback

If native tools aren't available, DEATHSTAR provides Python emulation:
- AWK emulation with field processing
- SED emulation with regex substitution
- PERL emulation with advanced regex

### 3. Combined Mode

**ULTIMATE POWER**: Combine all three modes in sequence:
- AWK → SED → PERL
- Maximum processing power
- The true DEATHSTAR

---

## Modes

### AWK Mode

**Pattern scanning and field processing**

```bash
# Extract first field
deathstar --awk --awk-action '{print $1}' input.txt

# Pattern matching
deathstar --awk --awk-pattern '/pattern/' --awk-action '{print $0}' input.txt

# Field separator
deathstar --awk -F ',' --awk-action '{print $1, $3}' input.txt
```

**AWK Power:**
- Field processing (`$1`, `$2`, `NF`, etc.)
- Pattern matching (`/regex/`)
- Built-in variables (`NR`, `NF`, `FS`, `RS`)
- Arithmetic and string operations

### SED Mode

**Stream editing and text transformation**

```bash
# Substitution
deathstar --sed --sed-substitute 'old/new/g' input.txt

# Delete lines
deathstar --sed --sed-delete '/pattern/' input.txt

# Multiple commands
deathstar --sed --sed-substitute 'old1/new1/g' --sed-substitute 'old2/new2/g' input.txt
```

**SED Power:**
- Pattern substitution (`s/pattern/replacement/flags`)
- Line deletion (`d`)
- Line printing (`p`)
- Address ranges (`1,5` or `/pattern/`)
- Multiple commands

### PERL Mode

**Powerful regex and text manipulation**

```bash
# Regex substitution
deathstar --perl --perl-expression 's/pattern/replacement/g' input.txt

# With modifiers
deathstar --perl --perl-expression 's/pattern/replacement/gi' --perl-modifiers 'gi' input.txt
```

**PERL Power:**
- Powerful regex
- Text manipulation
- Advanced pattern matching
- String operations
- Variable interpolation

### COMBINED Mode (ULTIMATE POWER!)

**Combine all three modes in sequence**

```bash
# AWK → SED → PERL
deathstar --combined \
  --awk-action '{print $1}' \
  --sed-substitute 'old/new/g' \
  --perl-expression 's/pattern/replacement/g' \
  input.txt
```

**COMBINED Power:**
- Maximum processing power
- All three tools in sequence
- Ultimate text transformation
- The true DEATHSTAR

---

## Integration with LUMINA

### With SIPHON

```bash
# Siphon emails, process with DEATHSTAR
siphon email:"query" | deathstar --perl --perl-expression 's/pattern/replacement/g'
```

### With PIPE

```bash
# Siphon → DEATHSTAR → Pipe
siphon email:"query" | deathstar --sed --sed-substitute 'old/new/g' | pipe hvac_email
```

### As Pipe Stage

DEATHSTAR can be used as a pipe stage:

```python
from scripts.python.pipes.deathstar_stage import DeathstarStage
from scripts.python.deathstar_processor import ProcessingMode

# Create DEATHSTAR stage
deathstar_stage = DeathstarStage(
    name="text_processing",
    mode=ProcessingMode.SED,
    config={
        "commands": [
            {
                "command": "s",
                "pattern": "old",
                "replacement": "new",
                "flags": "g"
            }
        ]
    }
)
```

---

## Usage Examples

### Example 1: Extract Email Addresses (AWK)

```bash
# Extract email addresses from text
cat emails.txt | deathstar --awk --awk-action '{if (match($0, /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/)) print substr($0, RSTART, RLENGTH)}'
```

### Example 2: Clean Log Files (SED)

```bash
# Remove timestamps and clean log format
deathstar --sed --sed-substitute '^\[.*?\] //' --sed-substitute '/DEBUG/d' logs.txt
```

### Example 3: Transform JSON (PERL)

```bash
# Transform JSON structure
deathstar --perl --perl-expression 's/"old_key"/"new_key"/g' data.json
```

### Example 4: Complete Pipeline (COMBINED)

```bash
# Ultimate power: Extract → Transform → Process
siphon email:"query" | \
  deathstar --combined \
    --awk-action '{print $1, $3}' \
    --sed-substitute 'old/new/g' \
    --perl-expression 's/pattern/replacement/g' | \
  pipe hvac_email
```

---

## API Usage

### Python API

```python
from scripts.python.deathstar_processor import DeathstarProcessor, ProcessingMode, SEDCommand

# Initialize DEATHSTAR
processor = DeathstarProcessor()

# AWK processing
result = processor.process_awk(
    input_text="field1 field2 field3",
    action="{print $1, $3}",
    field_separator=r'\s+'
)

# SED processing
commands = [
    SEDCommand(
        command="s",
        pattern="old",
        replacement="new",
        flags="g"
    )
]
result = processor.process_sed(input_text, commands)

# PERL processing
result = processor.process_perl(
    input_text,
    expression="s/pattern/replacement/g"
)

# COMBINED mode (ultimate power!)
result = processor.process_combined(
    input_text,
    awk_action="{print $1}",
    sed_commands=commands,
    perl_expression="s/pattern/replacement/g"
)
```

---

## Performance

### Native Tools

When native tools are available:
- **Maximum performance** - uses optimized native binaries
- **Full feature support** - all AWK/SED/PERL features
- **Production ready** - battle-tested tools

### Python Emulation

When native tools aren't available:
- **Cross-platform** - works everywhere Python works
- **Good performance** - optimized Python regex
- **Feature complete** - core functionality preserved

---

## Best Practices

### 1. Use Native Tools When Available

```bash
# Check availability
deathstar --check-tools

# Use native mode for maximum power
deathstar --awk --native input.txt
```

### 2. Chain with SIPHON and PIPE

```bash
# Perfect synergy
siphon email:"query" | deathstar --sed 's/old/new/g' | pipe hvac_email
```

### 3. Use COMBINED Mode for Complex Processing

```bash
# Ultimate power for complex transformations
deathstar --combined \
  --awk-action '{print $1}' \
  --sed-substitute 'old/new/g' \
  --perl-expression 's/pattern/replacement/g' \
  input.txt
```

### 4. Test Each Stage Separately

```bash
# Test AWK
deathstar --awk --awk-action '{print $1}' input.txt

# Test SED
deathstar --sed --sed-substitute 'old/new/g' input.txt

# Test PERL
deathstar --perl --perl-expression 's/pattern/replacement/g' input.txt

# Then combine
deathstar --combined ...
```

---

## Technical Details

### AWK Implementation

- **Native**: Uses system `awk` command
- **Emulation**: Python-based field processing and pattern matching
- **Features**: Field variables, pattern matching, built-in variables

### SED Implementation

- **Native**: Uses system `sed` command
- **Emulation**: Python `re` module for regex substitution
- **Features**: Substitution, deletion, address ranges

### PERL Implementation

- **Native**: Uses system `perl` command
- **Emulation**: Python `re` module for regex
- **Features**: Regex substitution, modifiers, pattern matching

### COMBINED Implementation

- **Sequential processing**: AWK → SED → PERL
- **Configurable order**: Customize processing sequence
- **Maximum power**: All three tools in one pipeline

---

## Status

✅ **DEATHSTAR OPERATIONAL** - Ultimate text processing power available

**Features:**
- ✅ AWK mode (native + emulation)
- ✅ SED mode (native + emulation)
- ✅ PERL mode (native + emulation)
- ✅ COMBINED mode (ultimate power!)
- ✅ Pipe stage integration
- ✅ SIPHON/PIPE synergy
- ✅ Cross-platform support

**Power Level**: 🌌 **ULTIMATE** - Maximum strength in the Galactic Multiversal Empire

---

**See Also:**
- [PIPE_COMMAND.md](PIPE_COMMAND.md) - Pipe command documentation
- [SIPHON_PIPE_SYNERGY.md](SIPHON_PIPE_SYNERGY.md) - Synergy documentation
- [PIPE_SYSTEM.md](PIPE_SYSTEM.md) - Pipe system documentation
