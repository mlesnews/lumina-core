# Mistral's Codestral - 100% Free Autocomplete Integration Guide

**Date**: 2026-01-28
**Status**: ✅ IMPLEMENTED
**Ticket**: T000003062
**Model**: Codestral (code-specific model)
**Pricing**: Generous free tier available

---

## Executive Summary

This guide documents the integration of **Mistral's Codestral** for 100% free inline and prompt autocomplete in VS Code and Cursor IDE. Codestral is Mistral's dedicated code completion model with a generous free tier API.

### Key Benefits

- ✅ **100% Free** - Generous free tier for code completion
- ✅ **Code-Specific** - Trained specifically for code generation
- ✅ **Fast Inference** - Optimized for real-time autocomplete
- ✅ **Multiple Languages** - Supports Python, JavaScript, TypeScript, and more
- ✅ **Inline Completion** - Real-time suggestions as you type
- ✅ **Prompt Autocomplete** - AI-powered code generation

---

## Prerequisites

### 1. Mistral API Key

Your Mistral API key is already stored in Azure Key Vault:

| Secret Name | Vault | Environment Variable |
|-------------|-------|---------------------|
| `mistral-api-key` | `jarvis-lumina` | `MISTRAL_API_KEY` |

**To retrieve your API key:**

```powershell
# Option 1: From Azure Key Vault (Production)
az keyvault secret show --vault-name jarvis-lumina --name mistral-api-key --query value -o tsv

# Option 2: From Environment Variable (Development)
$env:MISTRAL_API_KEY
```

### 2. Continue Extension

Install the Continue extension for VS Code or Cursor:

- **VS Code**: [Continue - AI Coding Assistant](https://marketplace.visualstudio.com/items?itemName=Continue.continue)
- **Cursor**: Built-in Continue integration or install from extension marketplace

### 3. Environment Setup

Add to your environment or `.env` file:

```bash
# .env file
MISTRAL_API_KEY=your_api_key_here
```

**Windows PowerShell:**
```powershell
# Set environment variable persistently
[Environment]::SetEnvironmentVariable("MISTRAL_API_KEY", "your_api_key_here", "User")
```

---

## Configuration

### 1. Continue Extension Configuration

Edit `.continue/config.yaml` to add Codestral provider:

```yaml
# .continue/config.yaml

# ... existing config ...

models:
  - name: codestral
    provider: mistral
    model: codestral-latest
    apiKey: ${env:MISTRAL_API_KEY}
    # Context window
    contextLength: 32768
    # Temperature for autocomplete (lower = more deterministic)
    temperature: 0.2
    # Max tokens for completions
    maxTokens: 256

# ... rest of config ...
```

### 2. VS Code settings.json

Configure inline autocomplete settings:

```json
// .vscode/settings.json
{
  // Continue extension settings
  "continue.enableInlineAutocomplete": true,
  "continue.enableTabAutocomplete": true,
  "continue.autocompleteOn": true,

  // Quick suggestions
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },

  // Suggestion delay (ms)
  "editor.suggestOnTriggerCharacters": true,
  "editor.suggestDelay": 0,

  // Snippet suggestions
  "editor.snippetSuggestions": "top",

  // Enable inline suggestions
  "editor.inlineSuggest.enabled": true,

  // Word based suggestions
  "editor.wordBasedSuggestions": "currentDocument",

  // Parameter hints
  "editor.parameterHints.enabled": true
}
```

### 3. Cursor IDE settings.json

Cursor-specific autocomplete configuration:

```json
// .cursor/settings.json
{
  // Continue extension for Cursor
  "continue.enableInlineAutocomplete": true,
  "continue.enableTabAutocomplete": true,

  // Cursor AI autocomplete
  "cursorai.autocomplete.enabled": true,
  "cursorai.autocomplete.earlyAccess": true,

  // Tab completion
  "editor.tabCompletion": "on",

  // Inline suggestions
  "editor.inlineSuggest.enabled": true,

  // Ghost text styling
  "editor.inlineSuggest.showColors": true,

  // Suggestion frequency
  "editor.suggest.showMethods": true,
  "editor.suggest.showFunctions": true,
  "editor.suggest.showConstructors": true,
  "editor.suggest.showFields": true,
  "editor.suggest.showVariables": true,
  "editor.suggest.showClasses": true,
  "editor.suggest.showStructs": true,
  "editor.suggest.showInterfaces": true,
  "editor.suggest.showModules": true,
  "editor.suggest.showProperties": true,
  "editor.suggest.showEvents": true,
  "editor.suggest.showOperators": true,
  "editor.suggest.showUnits": true,
  "editor.suggest.showValues": true,
  "editor.suggest.showConstants": true,
  "editor.suggest.showEnums": true,
  "editor.suggest.showEnumMembers": true,
  "editor.suggest.showKeywords": true,
  "editor.suggest.showWords": true,
  "editor.suggest.showColors": true,
  "editor.suggest.showFiles": true,
  "editor.suggest.showReferences": true,
  "editor.suggest.showFolders": true,
  "editor.suggest.showTypeParameters": true,
  "editor.suggest.showSnippets": true
}
```

### 4. Model-Specific Settings

Optimize Codestral for autocomplete:

```yaml
# .continue/config.yaml - Autocomplete optimized

models:
  - name: codestral-autocomplete
    provider: mistral
    model: codestral-latest
    apiKey: ${env:MISTRAL_API_KEY}

    # Optimized for autocomplete
    contextLength: 16384  # Smaller context for faster autocomplete
    temperature: 0.1      # Low temperature for deterministic completions
    maxTokens: 128        # Shorter completions for inline suggestions
    topP: 0.95            # Nucleus sampling
    frequencyPenalty: 0.0 # No penalty for repeating tokens
    presencePenalty: 0.0  # No penalty for new tokens

    # Stream for real-time suggestions
    stream: true

    # Only use for autocomplete (not chat)
    roles:
      - autocomplete
      - inline-completion
```

---

## Usage

### 1. Inline Autocomplete

Type code normally and Codestral will suggest completions:

```python
# Start typing and see suggestions
def calculate_fibonacci(n):
    if n <= 1:
        return n
    # Codestral suggests: return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
```

**Keyboard Shortcuts:**

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Next suggestion | `Ctrl + ]` | `Cmd + ]` |
| Previous suggestion | `Ctrl + [` | `Cmd + [` |

### 2. Prompt Autocomplete

Use Continue's chat for code generation:

1. Open Continue sidebar (`Ctrl/Cmd + L`)
2. Type your request:

```
Generate a Python function to validate email addresses using regex
```

3. Codestral generates the code
4. Click "Insert" to add to your file

### 3. Multi-Line Autocomplete

For larger code blocks, use the "Generate" command:

1. Highlight empty lines or comment describing desired code
2. Press `Ctrl/Cmd + Enter` (Continue inline chat)
3. Describe what you want
4. Codestral generates the code

---

## Language Support

Codestral supports 80+ programming languages. Key supported languages:

| Language | Support Level |
|----------|---------------|
| Python | ✅ Excellent |
| JavaScript | ✅ Excellent |
| TypeScript | ✅ Excellent |
| Java | ✅ Excellent |
| C/C++ | ✅ Good |
| C# | ✅ Good |
| Go | ✅ Good |
| Rust | ✅ Good |
| PHP | ✅ Good |
| Ruby | ✅ Good |
| Swift | ✅ Good |
| Kotlin | ✅ Good |
| SQL | ✅ Good |
| HTML/CSS | ✅ Good |
| Shell/Bash | ✅ Good |

---

## Optimization Tips

### 1. Context Optimization

```yaml
# .continue/config.yaml
models:
  - name: codestral-fast
    provider: mistral
    model: codestral-latest
    apiKey: ${env:MISTRAL_API_KEY}

    # Fast mode for quick autocomplete
    contextLength: 8192
    temperature: 0.1
    maxTokens: 64

  - name: codestral-accurate
    provider: mistral
    model: codestral-latest
    apiKey: ${env:MISTRAL_API_KEY}

    # Accurate mode for complex completions
    contextLength: 32768
    temperature: 0.2
    maxTokens: 256
```

### 2. Debounce Settings

Reduce API calls for better performance:

```json
// VS Code settings.json
{
  "continue.debounceMs": 150,  // Wait 150ms after typing stops
  "continue.minCharacters": 3  // Only trigger after 3 characters
}
```

### 3. File Type Filtering

Enable autocomplete only for specific file types:

```yaml
# .continue/config.yaml
autocomplete:
  languageMapping:
    python: codestral
    javascript: codestral
    typescript: codestral
    java: codestral

  exclude:
    - "*.md"     # Don't autocomplete in markdown
    - "*.txt"    # Don't autocomplete in text files
    - "*.json"   # Let JSON schema handle this
```

---

## Troubleshooting

### 1. API Key Issues

**Problem**: `401 Unauthorized` error

**Solution**:
```powershell
# Verify API key is correct
az keyvault secret show --vault-name jarvis-lumina --name mistral-api-key --query value -o tsv

# Test API key
$apiKey = az keyvault secret show --vault-name jarvis-lumina --name mistral-api-key --query value -o tsv
Invoke-RestMethod -Uri "https://api.mistral.ai/v1/models" -Headers @{ Authorization = "Bearer $apiKey" }
```

### 2. No Suggestions Appearing

**Problem**: Autocomplete not showing suggestions

**Solution**:
1. Check if Continue extension is enabled
2. Verify model configuration in `.continue/config.yaml`
3. Check VS Code settings:

```json
{
  "editor.inlineSuggest.enabled": true,
  "editor.quickSuggestions.other": true,
  "continue.enableInlineAutocomplete": true
}
```

### 3. Slow Suggestions

**Problem**: Suggestions take too long

**Solution**:
1. Reduce context length
2. Increase debounce time
3. Use `codestral-latest` model (optimized for speed)
4. Check network latency

```powershell
# Test API latency
Measure-Command {
    Invoke-RestMethod -Uri "https://api.mistral.ai/v1/chat/completions" `
        -Method Post `
        -Headers @{ Authorization = "Bearer $env:MISTRAL_API_KEY" } `
        -ContentType "application/json" `
        -Body '{"model":"codestral-latest","messages":[{"role":"user","content":"print"}],"max_tokens":10}'
}
```

### 4. Connection Errors

**Problem**: `ECONNREFUSED` or timeout errors

**Solution**:
1. Check internet connection
2. Verify API endpoint: `https://api.mistral.ai/v1`
3. Check firewall/proxy settings

### 5. Quality Issues

**Problem**: Poor suggestion quality

**Solution**:
1. Increase context (more code above cursor)
2. Adjust temperature (lower = more accurate)
3. Add comments describing desired code
4. Use more specific prompts

---

## API Reference

### Endpoint

```
POST https://api.mistral.ai/v1/chat/completions
```

### Request Format

```json
{
  "model": "codestral-latest",
  "messages": [
    {
      "role": "system",
      "content": "You are a code completion assistant. Complete the code based on the context."
    },
    {
      "role": "user",
      "content": "def fibonacci(n):\n    if n <= 1:\n        return n\n"
    }
  ],
  "temperature": 0.2,
  "max_tokens": 128,
  "stream": true
}
```

### Response Format

```json
{
  "id": "gen-123",
  "object": "chat.completion",
  "created": 1706467200,
  "model": "codestral-latest",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "        return fibonacci(n-1) + fibonacci(n-2)\n\nprint(fibonacci(10))"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 18,
    "total_tokens": 43
  }
}
```

---

## Free Tier Limits

| Metric | Free Tier Limit |
|--------|-----------------|
| Requests per minute | ~50 |
| Tokens per minute | ~100,000 |
| Requests per day | ~2,000 |
| Max context length | 128K tokens |

**Note**: Limits may vary. Check [Mistral API docs](https://docs.mistral.ai/) for current limits.

---

## Related Documentation

- [Continue Extension Docs](https://docs.continue.dev/)
- [Mistral API Documentation](https://docs.mistral.ai/)
- [Azure Key Vault Integration](docs/system/AZURE_KEY_VAULT_SECURITY.md)
- [Secret Management Guidelines](.kilocode/rules/secrets.md)
- [Cursor IDE Configuration](.cursor/settings.json)
- [VS Code Settings](.vscode/settings.json)

---

## Quick Reference

### Setup Commands

```powershell
# 1. Get API key from Azure Key Vault
$apiKey = az keyvault secret show --vault-name jarvis-lumina --name mistral-api-key --query value -o tsv

# 2. Set environment variable
[Environment]::SetEnvironmentVariable("MISTRAL_API_KEY", $apiKey, "User")

# 3. Restart VS Code/Cursor
```

### Configuration Files

| File | Purpose |
|------|---------|
| `.continue/config.yaml` | Continue extension configuration |
| `.vscode/settings.json` | VS Code autocomplete settings |
| `.cursor/settings.json` | Cursor IDE autocomplete settings |

### Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Open Continue | `Ctrl + L` | `Cmd + L` |
| Inline chat | `Ctrl + I` | `Cmd + I` |

---

**Document Version**: 1.0.0
**Last Updated**: 2026-01-28T07:33:00Z
**Maintained By**: @JARVIS @LUMINA @Kilocode
**Ticket**: T000003062
