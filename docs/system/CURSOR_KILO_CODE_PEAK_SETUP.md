# Cursor IDE - Kilo Code + @Peak Patterns Setup Guide

## Overview

This guide provides step-by-step instructions for configuring **Cursor IDE** with **Kilo Code** and **@Peak patterns** for maximum utilization.

## Prerequisites

1. **Cursor IDE** installed
2. **Ollama** running with Iron Legion models
3. **Kilo Code extension** (if available) or manual configuration

## Quick Setup

### 1. Install Required Models

Ensure Ollama is running and has the required models:

```bash
ollama pull codellama:13b
ollama pull llama3.2:11b
ollama pull qwen2.5-coder:1.5b-base
```

Verify Ollama is accessible:
```bash
curl http://localhost:11437/api/tags
```

### 2. Configure Cursor Settings

The configuration files are already created:
- `.cursor/settings.json` - Main Cursor settings
- `.cursor/kilo_code_config.json` - Kilo Code specific configuration

**Location**: These files should be in your workspace root or Cursor's config directory.

### 3. Verify Configuration

Check that the following are enabled in `.cursor/settings.json`:

```json
{
  "kilocode.enabled": true,
  "kilocode.peakIntegration.enabled": true,
  "kilocode.watcherUtau.enabled": true,
  "kilocode.r5Integration.enabled": true
}
```

## Configuration Details

### MCP (Model Context Protocol) Integration

**Hub Configuration** (Aligned with Docker MCP config):
- **Hub Endpoint**: `http://localhost:8080`
- **Health Check**: `http://localhost:8080/health`
- **Unified Management**: `true`
- **Cursor Adapter Port**: `8083`

**Kilo Code MCP Endpoint**:
- **Endpoint**: `http://localhost:8080/assistants/kilo_code`
- **Status**: `active`
- **Priority**: `high`

### Kilo Code Settings

**Base Configuration**:
- **Enabled**: `true`
- **Auto Trigger**: `true`
- **Suggestion Delay**: `100ms`
- **Max Suggestions**: `5`
- **Context Window**: `8192 tokens` (128k available via MCP)

### Iron Legion (Local LLM)

**Connection** (Aligned with Docker MCP config):
- **Base URL**: `http://localhost:11437` (Load Balancer)
- **Primary Endpoint**: `http://localhost:11434`
- **Load Balancer**: `http://localhost:11437`
- **API Type**: `ollama`
- **Timeout**: `120 seconds`
- **Temperature**: `0.2` (focused)
- **Max Tokens**: `8192`
- **Iron Legion Primary**: `true`

**Models** (Aligned with MCP config):
- **Primary**: `codellama:13b` (Mark II - coding specialty)
- **Fallback**: `llama3.2:11b` (Mark I - general)
- **Secondary**: `llama3.2:11b`
- **Lightweight**: `qwen2.5-coder:1.5b-base` (quick completions)

### @Peak Pattern Integration

**Enabled Features** (Aligned with MCP config):
- ✅ Peak enabled (`peak_enabled: true`)
- ✅ Pattern extraction
- ✅ Nutrient-dense solutions
- ✅ Small footprint
- ✅ Reusability
- ✅ Documentation
- ✅ Maximum utilization
- ✅ Force multiplier

**Pattern Registry**:
- **Path**: `data/peak_patterns/peak_pattern_registry.json`
- **Storage**: `data/peak_patterns/patterns/`
- **Auto-apply**: `true`

**MCP Capabilities**:
- Codebase indexing
- Semantic search
- Code generation
- Code analysis
- 128k context window

### The Watcher Utau Integration

**Research System**:
- **Enabled**: `true`
- **Auto Research**: `true`
- **Research Depth**: `maximum`
- **Sparks Generation**: `true`

### R5 Living Context Matrix

**Context Aggregation**:
- **Enabled**: `true`
- **Use Living Context Matrix**: `true`
- **Aggregate Chat Sessions**: `true`
- **Extract Peak Patterns**: `true`
- **Data Path**: `data/r5_living_matrix/`

## Manual Configuration (If Extension Not Available)

If Kilo Code extension is not available in Cursor, you can configure it manually:

### 1. Create Cursor Settings

Create or edit `.cursor/settings.json` in your workspace:

```json
{
  "kilocode.enabled": true,
  "kilocode.llm.baseUrl": "http://localhost:11437",
  "kilocode.peakIntegration.enabled": true
}
```

### 2. Configure via Environment Variables

Set environment variables for Kilo Code:

```bash
export KILO_CODE_ENABLED=true
export KILO_CODE_LLM_URL=http://localhost:11437
export KILO_CODE_PEAK_ENABLED=true
```

### 3. Use Configuration File

Point Kilo Code to the configuration file:

```json
{
  "kilocode.configPath": "${workspaceFolder}/.cursor/kilo_code_config.json"
}
```

## Usage

### Inline Completions

Kilo Code will automatically suggest code using @Peak patterns:

1. Start typing code
2. Kilo Code suggests completions based on @Peak patterns
3. Accept suggestions with `Tab` or `Enter`

### Chat Assistant

Access Kilo Code chat assistant:

1. Open Cursor chat (usually `Ctrl+L` or `Cmd+L`)
2. Ask questions or request code generation
3. Kilo Code uses @Peak patterns and R5 context

### Code Actions

Use code actions for:
- Refactoring with @Peak patterns
- Documentation generation
- Test generation
- Pattern extraction

### Pattern Extraction

To extract a @Peak pattern from code:

1. Annotate code with `@Peak: description`
2. Kilo Code automatically extracts and registers pattern
3. Watcher Utau researches the pattern
4. Pattern becomes available for reuse

## Verification

### Check Kilo Code Status

Run the verification script:

```bash
python scripts/python/verify_coding_assistants_setup.py
```

### Test @Peak Patterns

1. Create a test file with `@Peak` annotation
2. Verify pattern is extracted
3. Check `data/peak_patterns/patterns/` for registered pattern
4. Verify Watcher Utau research in `data/peak_patterns/research/`

### Test R5 Integration

1. Use Cursor chat
2. Verify session is aggregated in `data/r5_living_matrix/sessions/`
3. Check for pattern extraction in aggregated data

## Troubleshooting

### Kilo Code Not Working

1. **Check Ollama Connection**:
   ```bash
   curl http://localhost:11437/api/tags
   ```

2. **Verify Models**:
   ```bash
   ollama list
   ```

3. **Check Cursor Settings**:
   - Verify `.cursor/settings.json` exists
   - Check `kilocode.enabled` is `true`

### @Peak Patterns Not Working

1. **Check Pattern Registry**:
   - Verify `data/peak_patterns/peak_pattern_registry.json` exists
   - Check pattern storage directory exists

2. **Verify Integration**:
   - Check `kilocode.peakIntegration.enabled` is `true`
   - Verify pattern paths are correct

### R5 Integration Issues

1. **Check R5 System**:
   - Verify `scripts/python/r5_living_context_matrix.py` exists
   - Check R5 configuration in `config/r5/`

2. **Verify Data Directory**:
   - Ensure `data/r5_living_matrix/` exists
   - Check write permissions

## Best Practices

1. **Always Use @Peak Patterns**:
   - Let Kilo Code extract and reuse patterns
   - Build on existing patterns
   - Document new patterns

2. **Leverage R5 Context**:
   - Use chat sessions to build context
   - Aggregate knowledge over time
   - Reference living context matrix

3. **Monitor Watcher Utau**:
   - Review research reports
   - Check @sparks for insights
   - Act on recommendations

4. **Optimize for Local LLM**:
   - Use Iron Legion for all code generation
   - Only use cloud AI when explicitly approved
   - Maintain air-gapped security

## Configuration Files

### Main Configuration

- **`.cursor/settings.json`**: Main Cursor settings with Kilo Code configuration (MCP aligned)
- **`.cursor/kilo_code_config.json`**: Kilo Code specific configuration (MCP aligned)
- **`.cursor/mcp_config.json`**: MCP configuration for Cursor (Docker aligned)
- **`config/kilo_code_optimized_config.json`**: Project-wide Kilo Code configuration
- **`cedarbrook-financial-services_llc-env/universal-mcp-config/config.json`**: Universal MCP Docker config

### Pattern System

- **`data/peak_patterns/peak_pattern_registry.json`**: Pattern registry
- **`data/peak_patterns/patterns/`**: Individual pattern files
- **`data/peak_patterns/sparks/`**: Generated @sparks
- **`data/peak_patterns/research/`**: Watcher Utau research reports

### R5 System

- **`data/r5_living_matrix/sessions/`**: Chat session data
- **`data/r5_living_matrix/aggregated/`**: Aggregated knowledge
- **`config/r5/r5_config.json`**: R5 system configuration

## Status

✅ **Configuration Complete**
- Cursor settings configured
- Kilo Code integration enabled
- @Peak patterns enabled
- Watcher Utau integration enabled
- R5 integration enabled

**Next Steps**:
1. Verify Ollama is running
2. Test inline completions
3. Test chat assistant
4. Extract first @Peak pattern
5. Monitor Watcher Utau research

---

**Last Updated**: 2024-12-19
**Version**: 1.0.0
**IDE**: Cursor
**Maintained By**: Cedarbrook Financial Services LLC

