# Grammarly CLI - Command Line Grammar & Spell Checker

**Date**: 2025-01-24  
**Status**: ✅ **READY**  
**Command**: "WHIP US UP A GRAMMARLY CLI"

---

## Overview

Full-featured command-line interface for grammar and spell checking, integrated with MANUS Auto-Grammarly.

---

## Features

- ✅ **Text checking** - Check text from command line
- ✅ **File checking** - Check and correct files
- ✅ **Batch processing** - Check multiple files at once
- ✅ **Interactive mode** - Real-time checking
- ✅ **JSON output** - Machine-readable output
- ✅ **Detailed corrections** - Show what was corrected
- ✅ **In-place editing** - Modify files directly
- ✅ **MANUS integration** - Uses MANUS Auto-Grammarly engine

---

## Installation

The CLI uses MANUS Auto-Grammarly, which requires:

```bash
pip install pyspellchecker language_tool_python
```

---

## Usage

### Check Text

```bash
# Basic text check
python scripts/python/grammarly_cli.py --text "DOUBLE ONTANDRAS"

# With details
python scripts/python/grammarly_cli.py --text "DOUBLE ONTANDRAS" --details

# JSON output
python scripts/python/grammarly_cli.py --text "DOUBLE ONTANDRAS" --json
```

**Output**:
```
📄 Original: DOUBLE ONTANDRAS
✅ Corrected: DOUBLE ENTENDRES
🔧 Corrections: 1

Details:
  1. ONTANDRAS → ENTENDRES (known_typo)
```

### Check File

```bash
# Check a file (creates .corrected version)
python scripts/python/grammarly_cli.py --file document.txt

# Check file in place (modifies original)
python scripts/python/grammarly_cli.py --file document.txt --in-place

# Specify output file
python scripts/python/grammarly_cli.py --file document.txt --output fixed.txt
```

### Batch Processing

```bash
# Check multiple files
python scripts/python/grammarly_cli.py --files file1.txt file2.txt file3.txt

# Output to directory
python scripts/python/grammarly_cli.py --files *.txt --output-dir corrected/

# In-place batch editing
python scripts/python/grammarly_cli.py --files *.txt --in-place
```

### Interactive Mode

```bash
# Start interactive mode
python scripts/python/grammarly_cli.py --interactive
```

**Interactive Commands**:
- `quit` or `exit` - Exit interactive mode
- `clear` - Clear screen
- `help` - Show help

---

## Options

### Input Options (mutually exclusive)

- `--text`, `-t` - Text to check
- `--file`, `-f` - File to check
- `--files` - Multiple files to check
- `--interactive`, `-i` - Interactive mode

### Output Options

- `--output`, `-o` - Output file path
- `--output-dir` - Output directory for batch processing
- `--in-place` - Modify file in place
- `--json` - Output as JSON
- `--details`, `-d` - Show detailed corrections
- `--quiet`, `-q` - Quiet mode (minimal output)

---

## Examples

### Example 1: Quick Text Check

```bash
$ python scripts/python/grammarly_cli.py --text "DOUBLE ONTANDRAS"

📄 Original: DOUBLE ONTANDRAS
✅ Corrected: DOUBLE ENTENDRES
```

### Example 2: File Correction

```bash
$ python scripts/python/grammarly_cli.py --file README.md --in-place

✅ Corrected: README.md
   Corrections: 3
```

### Example 3: Batch Processing

```bash
$ python scripts/python/grammarly_cli.py --files *.md --output-dir corrected/

📊 Batch Processing Results
   Total: 5
   Processed: 5
   Corrected: 3
   Errors: 0
```

### Example 4: JSON Output

```bash
$ python scripts/python/grammarly_cli.py --text "test" --json

{
  "original": "test",
  "corrected": "test",
  "corrections_count": 0,
  "corrections": [],
  "changed": false
}
```

### Example 5: Interactive Mode

```bash
$ python scripts/python/grammarly_cli.py --interactive

======================================================================
📝 Grammarly CLI - Interactive Mode
======================================================================
Enter text to check (or 'quit' to exit)
Commands:
  'quit' or 'exit' - Exit interactive mode
  'clear' - Clear screen
  'help' - Show this help
======================================================================

📝 Enter text: DOUBLE ONTANDRAS

📄 Original: DOUBLE ONTANDRAS
✅ Corrected: DOUBLE ENTENDRES
🔧 Corrections: 1

Details:
  1. ONTANDRAS → ENTENDRES (known_typo)

📝 Enter text: quit

👋 Goodbye!
```

---

## Integration

### With MANUS Auto-Grammarly

The CLI uses MANUS Auto-Grammarly for all corrections:
- Known typos dictionary
- Spell checking (pyspellchecker)
- Grammar checking (language_tool_python)

### With AI Coordination

Can be integrated with JARVIS AI Coordination for system-wide grammar checking.

---

## Status

**Current**: ✅ **READY**

- ✅ Text checking: ACTIVE
- ✅ File checking: ACTIVE
- ✅ Batch processing: ACTIVE
- ✅ Interactive mode: ACTIVE
- ✅ JSON output: ACTIVE
- ✅ MANUS integration: ACTIVE

---

**"WHIP US UP A GRAMMARLY CLI"**

**DONE. Full-featured Grammarly CLI ready to use.**

