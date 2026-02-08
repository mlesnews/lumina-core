# JARVIS Core: Collated Features & Functionality (Lumina Integration)

**Date:** December 9, 2025
**Source:** Universal IDE-CA Analysis (VS Code, Cursor, Extensions)
**Target:** `lumina/src/cfservices/services/jarvis_core`

## 1. Overview
This document defines the "Collated Features & Functionality" (@ff) extracted from the "Universal IDE-CA" standard. These features represent the intersection of capabilities found in optimized VS Code and Cursor environments, now being standardized into the `jarvis` core within the `lumina` ecosystem.

## 2. Core Feature Modules

### 2.1 Context Intelligence Module (`jarvis.core.context`)
*Derived from: `kilocode.context` (VS Code) & Cursor Context Window*

**Functionality:**
- **Sliding Window Context:** Manages a dynamic context window (4k-8k tokens) that prioritizes active files, recent edits, and project structure.
- **Entity Graphing:** Automatically maps relationships between classes and functions (inspired by `pylance` and `typescript-language-features`).
- **Holocron Integration:** Direct connection to the project's "Holocron" (knowledge base) for retrieving long-term context.

**Implementation Plan:**
- Create `ContextManager` class in `lumina/src/cfservices/services/jarvis_core/context.py`.
- Implement `prioritize_context(chunks: List[Chunk]) -> List[Chunk]` algorithm.

### 2.2 Pattern Recognition & Application (`jarvis.core.patterns`)
*Derived from: `kilocode.peakPatterns` & `kilocode.codeGeneration`*

**Functionality:**
- **Pattern Registry:** A "Living" database of successful coding patterns (`peak_pattern_registry.json`).
- **Auto-Extraction:** Analyzes successful code completions to identify and save new patterns.
- **Pattern Enforcement:** Validates generated code against known "Peak Patterns" before presentation.

**Implementation Plan:**
- Create `PatternRegistry` class in `lumina/src/cfservices/services/jarvis_core/patterns.py`.
- Implement `extract_pattern(code: str) -> Pattern` and `validate_pattern(code: str, pattern: Pattern) -> bool`.

### 2.3 Unified MCP Orchestrator (`jarvis.core.mcp`)
*Derived from: `kilocode.mcp` & `mcp.hub`*

**Functionality:**
- **Tool Routing:** Centralized routing of requests to appropriate tools (Docker, Git, File System).
- **Health Monitoring:** Continuous "Heartbeat" checks for all connected MCP servers (Iron Legion, Lumina).
- **Protocol Translation:** Translates high-level user intents into specific MCP tool calls.

**Implementation Plan:**
- Create `MCPOrchestrator` class in `lumina/src/cfservices/services/jarvis_core/mcp.py`.
- Implement `route_request(intent: str) -> ToolCall`.

### 2.4 Resilience & Security Engine (`jarvis.core.security`)
*Derived from: `kilocode.security` (Killswitch)*

**Functionality:**
- **Operational Modes:** State machine managing "Normal", "Air Gap", "Dormant", and "Degraded" modes.
- **Permission Gating:** Requires explicit approval for high-risk actions (file deletion, external API calls).
- **Audit Logging:** Immutable logging of all actions taken by the agent.

**Implementation Plan:**
- Create `SecurityEngine` class in `lumina/src/cfservices/services/jarvis_core/security.py`.
- Implement `check_permission(action: Action) -> bool` and `set_mode(mode: OperationalMode)`.

### 2.5 Multi-Model Intelligence (`jarvis.core.intelligence`)
*Derived from: `kilocode.llm` (Iron Legion)*

**Functionality:**
- **Adaptive Model Selection:** Routes tasks to the most appropriate model (e.g., `codellama` for code, `llama3` for reasoning).
- **Load Balancing:** Distributes requests across the Iron Legion cluster.
- **Fallback Logic:** Automatically retries with a different model/node upon failure.

**Implementation Plan:**
- Create `IntelligenceManager` class in `lumina/src/cfservices/services/jarvis_core/intelligence.py`.
- Implement `select_model(task: Task) -> ModelConfig`.

## 3. Integration with Lumina
These core modules will reside in `lumina/src/cfservices/services/jarvis_core/` and will be exposed to the rest of the Lumina ecosystem via the `JarvisService` facade.

```python
# Example Structure
lumina/
  src/
    cfservices/
      services/
        jarvis_core/
          __init__.py
          context.py
          patterns.py
          mcp.py
          security.py
          intelligence.py
```

## 4. Next Steps
1.  Scaffold the `jarvis_core` directory structure.
2.  Implement the base classes for each module.
3.  Connect `jarvis_core` to the existing `lumina` service loader.
