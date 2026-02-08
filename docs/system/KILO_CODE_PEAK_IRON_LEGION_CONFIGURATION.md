# Kilo Code @Peak Iron Legion Configuration

## Overview

This document describes the complete setup and configuration for **Kilo Code** with **@Peak custom-tailored solutions** and **Iron Legion** local LLM cluster integration. This configuration maximizes Kilo Code's potential across all IDEs, with **Cursor** as the primary IDE.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Kilo Code (Primary)                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Iron Legion (Local LLM Cluster)               │  │
│  │  Complete Loadout (7 models):                        │  │
│  │  • codellama:13b (Primary code generation)            │  │
│  │  • llama3.2:11b (Secondary general)                   │  │
│  │  • qwen2.5-coder:1.5b-base (Lightweight quick)        │  │
│  │  • llama3 (General purpose)                           │  │
│  │  • mistral (General reasoning)                        │  │
│  │  • mixtral-8x7b (High complexity)                     │  │
│  │  • gemma-2b (Lightweight fallback)                    │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              @Peak Pattern Integration                │  │
│  │  • Nutrient-dense solutions                          │  │
│  │  • Small footprint                                   │  │
│  │  • Reusable components                               │  │
│  │  • Pattern extraction                                │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         R5 Living Context Matrix Integration         │  │
│  │  • Aggregated knowledge                              │  │
│  │  • Chat session condensation                         │  │
│  │  • Pattern extraction                                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
         │
         ├─→ Cursor (Primary IDE)
         ├─→ VS Code (Secondary)
         ├─→ JetBrains (Supported)
         └─→ Neovim (Supported)
```

## Configuration Files

### 1. Kilo Code Optimized Configuration
**Location**: `config/kilo_code_optimized_config.json`

**Key Settings**:
- **Primary LLM**: Iron Legion at `http://localhost:3000` (Lumina LLM Cluster)
- **Models**: Complete loadout of 7 models with roles and responsibilities
  - codellama:13b (primary code generation)
  - llama3.2:11b (secondary general)
  - qwen2.5-coder:1.5b-base (lightweight quick)
  - llama3 (general purpose)
  - mistral (general reasoning)
  - mixtral-8x7b (high complexity)
  - gemma-2b (lightweight fallback)
- **@Peak Integration**: Enabled
- **R5 Integration**: Enabled
- **Cursor Priority**: 1 (Primary IDE)
- **Air Gap Mode**: Enabled (prefer local, block cloud unless approved)

### 2. Coding Assistants Registry
**Location**: `config/coding_assistants_registry.json`

**Registered Assistants**:
1. **Kilo Code** (Priority 1, Active)
2. **Continue** (Priority 2, Active)
3. **Cline** (Priority 3, Active)
4. **GitHub Copilot** (Priority 4, Standby, requires approval)
5. **AWS CodeWhisperer** (Priority 5, Standby, requires approval)

### 3. Multi-IDE Optimal Settings
**Location**: `config/multi_ide_optimal_settings.json`

**IDE Priorities**:
- **Cursor**: Priority 1 (Primary)
- **VS Code**: Priority 2 (Secondary)
- **JetBrains**: Priority 3 (Supported)
- **Neovim**: Priority 4 (Supported)

### 4. LLM Orchestration
**Location**: `config/llm_orchestration_config.json`

**Braintrust Collective**:
- Coordinates multiple coding assistants
- Kilo Code as primary orchestrator
- Continue and Cline as secondary/tertiary assistants
- Cloud assistants excluded from air-gapped system

## Setup Instructions

### Prerequisites

1. **Ollama Installed and Running**
   ```bash
   # Verify Ollama is running
   curl http://localhost:11437/api/tags
   ```

2. **Iron Legion Models Installed** (Complete Loadout - 7 models)
   ```bash
   # Primary models
   ollama pull codellama:13b
   ollama pull llama3.2:11b
   ollama pull qwen2.5-coder:1.5b-base
   
   # Additional models
   ollama pull llama3
   ollama pull mistral
   ollama pull mixtral-8x7b
   ollama pull gemma-2b
   ```
   
   **Or use IDM for downloads** (recommended for large files):
   ```powershell
   .\scripts\powershell\download_all_7_models_idm.ps1
   ```

3. **Python Dependencies**
   ```bash
   pip install requests  # For verification script
   ```

### Cursor IDE Setup (Primary)

1. **Install Kilo Code Extension**
   - Open Cursor
   - Go to Extensions
   - Search for "Kilo Code"
   - Install the extension

2. **Configure Iron Legion Connection**
   - Open Cursor Settings
   - Navigate to Kilo Code settings
   - Set base URL: `http://localhost:11437`
   - Select primary model: `codellama:13b`

3. **Enable @Peak Patterns**
   - In Kilo Code settings, enable "Peak Integration"
   - Enable "Pattern Extraction"
   - Enable "Use Existing Patterns"

4. **Enable R5 Integration**
   - Enable "R5 Living Context Matrix"
   - Enable "Aggregate Chat Sessions"
   - Set context window to 8192 tokens

5. **Set as Primary Assistant**
   - In Cursor settings, set Kilo Code as primary coding assistant
   - Configure Continue and Cline as secondary/tertiary assistants

### VS Code Setup (Secondary)

1. **Install Kilo Code Extension**
   ```bash
   code --install-extension kilocode.kilocode
   ```

2. **Configure Settings**
   - Open `.vscode/settings.json`
   - Add Kilo Code configuration (see `config/multi_ide_optimal_settings.json`)

3. **Enable Features**
   - Enable inline completion
   - Enable chat assistant
   - Enable code actions

### JetBrains Setup

1. **Install Kilo Code Plugin**
   - Open JetBrains IDE
   - Go to Plugins
   - Search for "Kilo Code"
   - Install and restart

2. **Configure Connection**
   - Open Settings → Tools → Kilo Code
   - Set Iron Legion URL: `http://localhost:11437`
   - Select model: `codellama:13b`

### Neovim Setup

1. **Install Plugin**
   ```lua
   -- In your Neovim config
   use 'kilocode/kilocode.nvim'
   ```

2. **Configure**
   ```lua
   require('kilocode').setup({
     base_url = "http://localhost:11437",
     model = "codellama:13b",
     peak_patterns = true,
     r5_integration = true
   })
   ```

## Verification

Run the verification script to check your setup:

```bash
python scripts/python/verify_coding_assistants_setup.py
```

The script will verify:
- ✅ Configuration files exist
- ✅ Kilo Code configuration is valid
- ✅ Iron Legion connection is working
- ✅ Required models are available
- ✅ IDE-specific settings are configured
- ✅ @Peak integration is enabled
- ✅ R5 integration is enabled

## Maximizing Potential

### For Cursor (Primary IDE)

1. **Use Kilo Code as Primary Assistant**
   - Set Kilo Code as default for all code generation
   - Use Continue and Cline for alternative perspectives

2. **Enable All Features**
   - ✅ Inline completion
   - ✅ Chat assistant
   - ✅ Code actions
   - ✅ Refactoring
   - ✅ Documentation generation
   - ✅ Test generation

3. **Leverage @Peak Patterns**
   - Let Kilo Code extract reusable patterns
   - Reference existing patterns in codebase
   - Build nutrient-dense, small-footprint solutions

4. **Use R5 Living Context Matrix**
   - Aggregate all chat sessions
   - Extract patterns from conversations
   - Build comprehensive knowledge base

5. **Optimize Context Window**
   - Set to 8192 tokens for maximum context
   - Include open files, recent files, project structure
   - Use git history for better understanding

### Performance Optimization

1. **Caching**
   - Enable pattern caching
   - Enable context caching
   - Set TTL to 3600 seconds

2. **Batch Requests**
   - Enable batch processing
   - Use parallel processing when safe
   - Implement lazy loading

3. **Model Selection** (Decision-Making Framework)
   - **High complexity**: `codellama:13b` or `mixtral-8x7b`
   - **Medium complexity**: `llama3.2:11b`, `llama3`, or `mistral`
   - **Low complexity**: `qwen2.5-coder:1.5b-base` or `gemma-2b`
   - **Code generation**: `codellama:13b` (primary) or `qwen2.5-coder:1.5b-base` (quick)
   - **Reasoning/analysis**: `mistral` or `mixtral-8x7b`
   - See `config/ollama_model_mapping.json` for complete decision framework

### Security

1. **Air Gap Mode**
   - Prefer local LLM (Iron Legion)
   - Block cloud AI unless explicitly approved
   - Maintain control over all AI interactions

2. **Killswitch**
   - Configure killswitch modes
   - Default to "normal" mode
   - Have graceful degradation paths

## Troubleshooting

### Iron Legion Not Connecting

1. **Check Ollama Status**
   ```bash
   ollama serve
   ```

2. **Verify Port**
   - Default: `http://localhost:11437`
   - Check if port is in use

3. **Check Models**
   ```bash
   ollama list
   ```

### Kilo Code Not Working in Cursor

1. **Check Extension Status**
   - Verify extension is installed and enabled
   - Check for extension errors

2. **Verify Configuration**
   - Check `config/kilo_code_optimized_config.json`
   - Verify Cursor settings match configuration

3. **Check Logs**
   - View Kilo Code logs: `logs/kilo_code.log`
   - Check Cursor developer console

### @Peak Patterns Not Working

1. **Verify Integration**
   - Check `peak_integration.enabled` in config
   - Verify pattern extraction is enabled

2. **Check Pattern Storage**
   - Verify pattern storage location
   - Check pattern extraction logs

### R5 Integration Issues

1. **Verify R5 System**
   - Check R5 API server is running
   - Verify R5 configuration

2. **Check Context Matrix**
   - Verify `data/r5_living_matrix/` exists
   - Check context aggregation logs

## Best Practices

1. **Always Use @Peak Patterns**
   - Let Kilo Code extract and reuse patterns
   - Build on existing patterns
   - Document new patterns

2. **Leverage R5 Living Context**
   - Aggregate all IDE chat sessions
   - Build comprehensive knowledge base
   - Use context for better code generation

3. **Optimize for Local LLM**
   - Use Iron Legion for all code generation
   - Only use cloud AI when explicitly approved
   - Maintain air-gapped security

4. **Use Multiple Assistants**
   - Kilo Code for primary generation
   - Continue for alternative suggestions
   - Cline for conversational coding

5. **Monitor Performance**
   - Track usage metrics
   - Monitor error rates
   - Optimize based on performance data

## Status

✅ **Configuration Complete**
- All configuration files created
- Verification script available
- Documentation complete

**Next Steps**:
1. Run verification script
2. Install Kilo Code in Cursor
3. Configure Iron Legion connection
4. Enable @Peak and R5 integrations
5. Start maximizing potential!

---

**Last Updated**: 2024-12-19
**Version**: 1.0.0
**Maintained By**: Cedarbrook Financial Services LLC

