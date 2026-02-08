# @PEAK Text Processor

**Combines AWK, SED, and Perl into unified @peak text processing system**

The @peak vision: Maximum power, minimum footprint, nutrient-dense solutions.

#PEAK #AWK #SED #PERL #TEXT-PROCESSING #SYPHON #PIPE

---

## Overview

The **@PEAK Text Processor** unifies the best of Unix/Linux POSIX shell scripting tools:

- **AWK**: Pattern scanning and field processing
- **SED**: Stream editing and transformation
- **Perl**: Powerful regex and text manipulation

**All combined into one @peak system** with perfect synergy with `siphon` and `pipe` commands.

---

## Philosophy

**@PEAK = Maximum Power + Minimum Footprint + Nutrient-Dense Solutions**

- **AWK Logic**: Field-based processing, pattern-action pairs
- **SED Logic**: Stream editing, substitution, deletion
- **Perl Logic**: Advanced regex, text manipulation
- **Unified**: All three combined in one system
- **Synergy**: Works seamlessly with siphon/pipe

---

## Features

### AWK-Style Processing

- Pattern scanning with regex
- Field processing (delimiter-based)
- Pattern-action pairs
- Line number tracking
- Field count (NF)

### SED-Style Processing

- Stream editing
- Substitution (s/pattern/replacement/flags)
- Deletion (/pattern/d)
- Print (/pattern/p)
- Multiple commands per line

### Perl-Style Processing

- Advanced regex operations
- Substitution (s/pattern/replacement/)
- Transliteration (tr/from/to/)
- Modifiers (g, i, m, s, x)

### Unified @PEAK Mode

- All three modes combined
- Sequential processing: AWK → SED → Perl
- Maximum power, minimum footprint
- Nutrient-dense solutions

---

## Usage

### Command-Line Interface

```bash
# AWK-style field processing
peak_text --mode awk --field-delimiter "," --input file.csv

# SED-style substitution
peak_text --mode sed --sed-command "s/old/new/g" --input file.txt

# Perl-style regex
peak_text --mode perl --perl-expr "s/pattern/replacement/g" --input file.txt

# Unified @peak mode (all three combined)
peak_text --mode unified --input file.txt

# Perfect synergy with siphon/pipe
siphon email:"query" | peak_text --mode unified | pipe hvac_email

# Process from stdin
cat file.txt | peak_text --sed-command "s/old/new/g"
```

### Python API

```python
from scripts.python.peak_text_processor import PeakTextProcessor
from pathlib import Path

# Create processor
processor = PeakTextProcessor(project_root=Path("."))

# Set mode
processor.mode = ProcessingMode.UNIFIED  # @peak mode

# Add SED substitution
processor.add_sed_substitute("old", "new", flags="g")

# Process file
results = processor.process_file(Path("input.txt"))

# Or process stream
for line in processor.process_stream(input_stream):
    print(line)
```

### Pipe Stage Integration

```python
from scripts.python.pipes.peak_text_stage import PeakTextStage

# Create stage
stage = PeakTextStage(
    name="peak_text",
    mode="unified",
    sed_commands=["s/old/new/g"],
    perl_expressions=["s/pattern/replacement/"]
)

# Use in pipe
pipe.add_stage(stage)
```

---

## Processing Modes

### AWK Mode

**Pattern scanning and field processing**

```bash
peak_text --mode awk --field-delimiter " " --input file.txt
```

**Features:**
- Field-based processing
- Pattern-action pairs
- Line number tracking
- Field count (NF)

### SED Mode

**Stream editing and transformation**

```bash
peak_text --mode sed --sed-command "s/old/new/g" --input file.txt
```

**Features:**
- Substitution
- Deletion
- Print
- Multiple commands

### Perl Mode

**Advanced regex and text manipulation**

```bash
peak_text --mode perl --perl-expr "s/pattern/replacement/g" --input file.txt
```

**Features:**
- Advanced regex
- Substitution
- Transliteration
- Modifiers

### Unified @PEAK Mode

**All three combined - maximum power**

```bash
peak_text --mode unified --input file.txt
```

**Processing Order:**
1. AWK-style pattern scanning
2. SED-style stream editing
3. Perl-style regex manipulation

**Result:** Maximum power, minimum footprint, nutrient-dense solutions.

---

## Examples

### Example 1: AWK-Style Field Processing

```bash
# Process CSV file, extract first and third fields
peak_text --mode awk --field-delimiter "," --awk-pattern "^[0-9]+" --input data.csv
```

### Example 2: SED-Style Substitution

```bash
# Replace all occurrences of "old" with "new"
peak_text --mode sed --sed-command "s/old/new/g" --input file.txt
```

### Example 3: Perl-Style Regex

```bash
# Advanced regex substitution
peak_text --mode perl --perl-expr "s/(\d+)-(\d+)/$2-$1/g" --input file.txt
```

### Example 4: Unified @PEAK Mode

```bash
# Combine all three modes
peak_text --mode unified \
  --field-delimiter "," \
  --sed-command "s/old/new/g" \
  --perl-expr "s/pattern/replacement/g" \
  --input file.txt
```

### Example 5: Perfect Synergy with Siphon/Pipe

```bash
# Siphon emails, process with @peak, pipe through workflow
siphon email:"hvac OR furnace" | \
  peak_text --mode unified --sed-command "s/old/new/g" | \
  pipe hvac_email
```

### Example 6: Process Siphoned Data

```python
from scripts.python.peak_text_processor import PeakTextProcessor

processor = PeakTextProcessor(project_root=Path("."))
processor.mode = ProcessingMode.UNIFIED

# Process siphoned data
siphoned_data = {
    "items": [
        {"content": "Line 1: old text"},
        {"content": "Line 2: old text"}
    ]
}

processed = processor.process_siphoned_data(siphoned_data)
# Result: processed items with "old" replaced with "new"
```

---

## Integration with Siphon/Pipe

### Perfect Synergy

The @PEAK Text Processor is designed for perfect synergy with `siphon` and `pipe` commands:

```bash
# Classic Unix-style piping
siphon email:"query" | peak_text --mode unified | pipe hvac_email

# Process siphoned data
siphon filesystem:/path | peak_text --sed-command "s/old/new/g" | pipe document_processor
```

### Pipe Stage

Use `PeakTextStage` in pipes:

```python
from scripts.python.pipes.peak_text_stage import PeakTextStage

# Create pipe with @peak text processing
pipe.add_stage(PeakTextStage(
    name="peak_text",
    mode="unified",
    sed_commands=["s/old/new/g"]
))
```

---

## Technical Details

### Processing Flow

1. **Input**: Text lines or siphoned data
2. **AWK Processing**: Pattern scanning, field processing
3. **SED Processing**: Stream editing, substitution
4. **Perl Processing**: Advanced regex manipulation
5. **Output**: Processed text lines

### Field Processing

- **Delimiter**: Configurable (default: space)
- **Field Numbers**: 1-indexed (AWK-style)
- **Output Delimiter**: Configurable

### Pattern Matching

- **AWK**: Regex patterns with action functions
- **SED**: Regex patterns with commands
- **Perl**: Advanced regex with modifiers

### Performance

- **Stream Processing**: Processes line-by-line (memory efficient)
- **Lazy Evaluation**: Only processes when needed
- **Minimal Footprint**: Small memory usage
- **Maximum Power**: All three tools combined

---

## Best Practices

### 1. Use Unified Mode for Maximum Power

```bash
# ✅ Best - unified @peak mode
peak_text --mode unified --input file.txt
```

### 2. Chain with Siphon/Pipe

```bash
# ✅ Excellent - perfect synergy
siphon email:"query" | peak_text --mode unified | pipe hvac_email
```

### 3. Use Appropriate Mode for Task

```bash
# ✅ AWK for field processing
peak_text --mode awk --field-delimiter "," --input data.csv

# ✅ SED for simple substitution
peak_text --mode sed --sed-command "s/old/new/g" --input file.txt

# ✅ Perl for advanced regex
peak_text --mode perl --perl-expr "s/pattern/replacement/g" --input file.txt
```

### 4. Process Streams for Large Files

```bash
# ✅ Memory efficient
cat large_file.txt | peak_text --mode unified --sed-command "s/old/new/g"
```

---

## Summary

The **@PEAK Text Processor** combines:

- ✅ **AWK**: Pattern scanning and field processing
- ✅ **SED**: Stream editing and transformation
- ✅ **Perl**: Advanced regex and text manipulation
- ✅ **Unified**: All three combined in @peak mode
- ✅ **Synergy**: Perfect integration with siphon/pipe

**Maximum power, minimum footprint, nutrient-dense solutions.**

---

**Status**: ✅ **@PEAK TEXT PROCESSOR READY**

**Tags**: #PEAK #AWK #SED #PERL #TEXT-PROCESSING #SYPHON #PIPE
