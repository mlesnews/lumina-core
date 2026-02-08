# JARVIS Proactive IDE Troubleshooter

## Overview

Proactively troubleshoots IDE errors, warnings, and notifications at first onset. Detects #patterns in behavior/actions = intent, breaks down to basic building blocks, simulates fixes, and applies proven solutions using @peak @ff.

## Features

### Pattern Recognition (#patterns)
- Detects patterns in error behavior/actions = intent
- Breaks down to basic building blocks
- Maps to proven fix strategies

### Simulation Before Application
- Simulates fixes before applying
- Validates success rate
- Only applies proven patterns (>75% success rate)

### @FF Keyboard Shortcuts
- Uses function keys and shortcuts for automation
- Cursor IDE specific shortcuts
- Universal VSCode shortcuts

### Proactive Monitoring
- Continuous monitoring for errors/warnings
- Auto-detection at first onset
- Auto-fix for high-confidence patterns

## Error Patterns

### Syntax Errors
- **Pattern**: Missing Colon
- **Intent**: Add missing colon to fix syntax
- **Building Blocks**: detect_missing_colon, locate_line, insert_colon
- **@FF**: F2 (Rename/Edit symbol)
- **Success Rate**: 95%

### Type Errors
- **Pattern**: Type Mismatch
- **Intent**: Fix type mismatch
- **Building Blocks**: detect_type_error, identify_expected_type, fix_type
- **@FF**: F12 (Go to definition)
- **Success Rate**: 85%

### Import Errors
- **Pattern**: Import Error
- **Intent**: Fix missing import
- **Building Blocks**: detect_missing_import, find_module, add_import
- **@FF**: Ctrl+Shift+P (Command palette)
- **Success Rate**: 90%

### Undefined Variable
- **Pattern**: Undefined Variable
- **Intent**: Fix undefined variable
- **Building Blocks**: detect_undefined, find_definition, fix_reference
- **@FF**: F12, Shift+F12 (Go to definition/references)
- **Success Rate**: 80%

### Unused Variable
- **Pattern**: Unused Variable
- **Intent**: Remove or use unused variable
- **Building Blocks**: detect_unused, check_usage, remove_or_fix
- **@FF**: Ctrl+K Ctrl+X (Trim whitespace)
- **Success Rate**: 75%

### Lint Errors
- **Pattern**: Lint Error
- **Intent**: Fix linting issue
- **Building Blocks**: detect_lint, identify_rule, apply_fix
- **@FF**: Ctrl+Alt+F (Format document)
- **Success Rate**: 70%

### Format Errors
- **Pattern**: Format Error
- **Intent**: Fix formatting
- **Building Blocks**: detect_format, identify_issue, format_code
- **@FF**: Ctrl+Alt+F, Ctrl+K Ctrl+F (Format document/selection)
- **Success Rate**: 95%

### Config Errors
- **Pattern**: Config Error
- **Intent**: Fix configuration
- **Building Blocks**: detect_config_error, validate_config, fix_config
- **@FF**: Ctrl+, (Settings)
- **Success Rate**: 80%

### Dependency Errors
- **Pattern**: Dependency Error
- **Intent**: Install missing dependency
- **Building Blocks**: detect_missing_dep, identify_package, install_package
- **@FF**: Ctrl+` (Terminal)
- **Success Rate**: 90%

## Usage

### CLI

```bash
# Detect errors
python scripts/python/jarvis_proactive_ide_troubleshooter.py --detect

# Check specific file
python scripts/python/jarvis_proactive_ide_troubleshooter.py --detect --file scripts/python/myfile.py

# Start monitoring
python scripts/python/jarvis_proactive_ide_troubleshooter.py --monitor

# Show status
python scripts/python/jarvis_proactive_ide_troubleshooter.py --status

# Simulate fix
python scripts/python/jarvis_proactive_ide_troubleshooter.py --simulate <error_id>

# Apply fix
python scripts/python/jarvis_proactive_ide_troubleshooter.py --fix <error_id>
```

### Python API

```python
from jarvis_proactive_ide_troubleshooter import JARVISProactiveIDETroubleshooter
from pathlib import Path

# Initialize
project_root = Path(__file__).parent.parent.parent
troubleshooter = JARVISProactiveIDETroubleshooter(project_root)

# Detect errors
errors = troubleshooter.detect_errors()

# Simulate fix
for error in errors:
    simulation = troubleshooter.simulate_fix(error)
    if simulation.get("success") and simulation["simulation"]["success_rate"] > 0.75:
        # Apply fix
        result = troubleshooter.apply_fix(error)
        print(f"Fixed: {error.file_path}:{error.line}")

# Start monitoring
troubleshooter.start_monitoring()
```

## Workflow

1. **Detection**: Continuously monitor for errors/warnings
2. **Pattern Matching**: Match error to known pattern
3. **Intent Extraction**: Extract intent from pattern
4. **Building Blocks**: Break down to basic building blocks
5. **Simulation**: Simulate fix before applying
6. **Validation**: Check success rate (>75% for auto-fix)
7. **Application**: Apply fix using @FF shortcuts
8. **Verification**: Verify fix was successful

## Configuration

Configuration file: `config/ide_error_patterns.json`

### Pattern Structure
```json
{
  "pattern_id": "syntax_missing_colon",
  "pattern_name": "Missing Colon",
  "regex": "expected ':'|missing colon|SyntaxError.*:",
  "category": "syntax",
  "intent": "Add missing colon to fix syntax",
  "building_blocks": [
    "detect_missing_colon",
    "locate_line",
    "insert_colon"
  ],
  "fix_strategy": "insert_text",
  "ff_shortcuts": ["F2"],
  "proven": true,
  "success_rate": 0.95
}
```

## Integration

### With Cursor IDE
- Uses Cursor-specific shortcuts
- Integrates with Cursor's lint system
- Respects Cursor's error reporting

### With VSCode
- Uses universal VSCode shortcuts
- Compatible with VSCode extensions
- Works with standard VSCode diagnostics

## Tags

@CURSOR @IDE #TROUBLESHOOTING #PATTERNS #PEAK #FF #PROACTIVE
