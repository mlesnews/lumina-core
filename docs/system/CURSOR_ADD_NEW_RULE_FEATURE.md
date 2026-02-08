# Cursor IDE "+ADD NEW RULE?" Feature Integration

**Date:** January 9, 2025  
**Request ID:** 708664e1-ed25-4177-97df-3ae470d07e04  
**Feature:** Cursor IDE "+ADD NEW RULE?" UI Feature

---

## Overview

Cursor IDE has introduced a new **"+ADD NEW RULE?"** feature that allows users to add rules directly from the UI. This document describes how to integrate and use this feature with the LUMINA project.

---

## Feature Description

The "+ADD NEW RULE?" feature in Cursor IDE allows you to:
- Add new rules directly from the Cursor IDE interface
- Rules are automatically added to `.cursorrules` file
- Rules are immediately available to the AI assistant
- Rules persist across sessions

---

## Integration Script

### `cursor_add_new_rule_integration.py`

A Python script that integrates with the "+ADD NEW RULE?" feature to:
- Parse existing `.cursorrules` file
- Add new rules programmatically
- Suggest rules based on project context
- Track rule additions
- Export rule templates

### Usage

```bash
# Add a new rule
python scripts/python/cursor_add_new_rule_integration.py --add-rule "Always use type hints in Python"

# Add rule to specific section
python scripts/python/cursor_add_new_rule_integration.py --add-rule "Use async/await" --section "javascript"

# Get rule suggestions
python scripts/python/cursor_add_new_rule_integration.py --suggest

# Parse existing rules
python scripts/python/cursor_add_new_rule_integration.py --parse

# Show rule statistics
python scripts/python/cursor_add_new_rule_integration.py --stats

# Export rules template
python scripts/python/cursor_add_new_rule_integration.py --export-template
```

---

## How to Use "+ADD NEW RULE?" in Cursor IDE

### Method 1: Via UI (Recommended)

1. **Open Cursor IDE**
2. **Look for "+ADD NEW RULE?" button/prompt** in the chat interface
3. **Click "+ADD NEW RULE?"**
4. **Enter your rule** in the text field
5. **Save** - Rule is automatically added to `.cursorrules`

### Method 2: Via Chat

1. **Type in Cursor chat:** "Add a new rule: [your rule text]"
2. **Cursor IDE will prompt** to add the rule
3. **Confirm** the addition

### Method 3: Programmatically

Use the integration script to add rules:

```bash
python scripts/python/cursor_add_new_rule_integration.py --add-rule "Your rule here"
```

---

## Rule Categories

### Code Style Rules
- Always use type hints in Python functions
- Use descriptive variable names
- Follow PEP 8 style guide
- Add docstrings to all functions and classes

### Project-Specific Rules
- Use lumina_logger for all logging
- Include tags in file headers
- Follow LUMINA project structure
- Use Path objects instead of strings for file paths

### Security Rules
- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate all user inputs
- Use secure authentication methods

### Testing Rules
- Write unit tests for all new functions
- Use pytest for Python tests
- Maintain >80% code coverage
- Test error cases and edge conditions

### Documentation Rules
- Update README when adding features
- Document all public APIs
- Include usage examples in docstrings
- Keep CHANGELOG updated

---

## Rule Format

Rules in `.cursorrules` can be:
- **Simple text rules:** "Always use type hints"
- **Sectioned rules:** Organized under `# Section Name`
- **Context-specific rules:** Rules that apply to specific file types or areas

### Example `.cursorrules` Structure

```
# Python Rules
Always use type hints in Python functions
Follow PEP 8 style guide
Add docstrings to all functions

# Project Rules
Use lumina_logger for all logging
Include tags in file headers
Follow LUMINA project structure

# Security Rules
Never commit API keys or secrets
Use environment variables for sensitive data
```

---

## Best Practices

### 1. Be Specific
❌ Bad: "Write good code"  
✅ Good: "Always use type hints for function parameters and return types"

### 2. Be Actionable
❌ Bad: "Code should be clean"  
✅ Good: "Use descriptive variable names that explain their purpose"

### 3. Be Consistent
- Use similar formatting for similar rules
- Group related rules together
- Use clear section headers

### 4. Review Regularly
- Periodically review rules for relevance
- Remove outdated rules
- Update rules as project evolves

---

## Integration with LUMINA

### Automatic Rule Tracking

The integration script automatically:
- Creates backups before adding rules
- Logs all rule additions
- Tracks rule statistics
- Suggests rules based on project context

### Rule Logs

Rule additions are logged to:
```
data/cursor_rules/rule_additions.jsonl
```

### Rule Statistics

Get statistics about your rules:
```bash
python scripts/python/cursor_add_new_rule_integration.py --stats
```

---

## Rule Suggestions

The integration script can suggest rules based on:
- **File type** (Python, JavaScript, TypeScript, etc.)
- **Project area** (docs, scripts, config, etc.)
- **Existing rules** (avoids duplicates)
- **Project templates** (pre-defined rule templates)

### Get Suggestions

```bash
# General suggestions
python scripts/python/cursor_add_new_rule_integration.py --suggest

# Context-specific (via script modification)
# Add context parameter for file-specific suggestions
```

---

## Troubleshooting

### Rule Not Appearing

1. **Check `.cursorrules` file exists**
   ```bash
   ls -la .cursorrules
   ```

2. **Verify rule was added**
   ```bash
   python scripts/python/cursor_add_new_rule_integration.py --parse
   ```

3. **Check Cursor IDE settings**
   - Ensure `.cursorrules` is not excluded
   - Restart Cursor IDE if needed

### Rule Not Working

1. **Check rule format** - Rules should be clear and specific
2. **Verify rule location** - Rules should be in workspace root `.cursorrules`
3. **Check for conflicts** - Multiple rules shouldn't contradict each other

### Integration Script Issues

1. **Check Python path**
   ```bash
   python --version
   ```

2. **Verify dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Check file permissions**
   - Ensure write access to `.cursorrules`
   - Ensure write access to `data/cursor_rules/`

---

## Examples

### Example 1: Add Python Rule

```bash
python scripts/python/cursor_add_new_rule_integration.py \
  --add-rule "Always use f-strings for string formatting in Python" \
  --section "python"
```

### Example 2: Add Security Rule

```bash
python scripts/python/cursor_add_new_rule_integration.py \
  --add-rule "Never hardcode API keys or secrets in code" \
  --section "security"
```

### Example 3: Get Suggestions

```bash
python scripts/python/cursor_add_new_rule_integration.py --suggest
```

Output:
```
💡 Suggested Rules:
  1. Always use type hints in Python functions
  2. Use descriptive variable names
  3. Follow PEP 8 style guide
  4. Add docstrings to all functions and classes
  5. Use lumina_logger for all logging
  ...
```

---

## Related Documentation

- [Cursor IDE Lumina Settings](./CURSOR_IDE_LUMINA_SETTINGS.md)
- [AI Guidance Complete Framework](./AI_GUIDANCE_COMPLETE_FRAMEWORK.md)
- [AI Guidance Quick Reference](./AI_GUIDANCE_QUICK_REFERENCE.md)

---

## Next Steps

1. **Try the feature:** Use "+ADD NEW RULE?" in Cursor IDE
2. **Add project-specific rules:** Customize rules for LUMINA project
3. **Review existing rules:** Parse and review current `.cursorrules`
4. **Get suggestions:** Use the integration script for rule suggestions
5. **Export template:** Create rule templates for other projects

---

**Last Updated:** January 9, 2025  
**Request ID:** 708664e1-ed25-4177-97df-3ae470d07e04  
**Status:** ✅ Integration Script Created
