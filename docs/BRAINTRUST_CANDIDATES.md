# The Braintrust: Recommended IDEs & Coding Assistants for JARVIS Integration

**Date:** December 9, 2025
**Objective:** Expand the "Universal IDE-CA" standard to include a wider range of high-performance tools, creating a true "Braintrust" of AI capabilities for JARVIS to orchestrate.

## 1. The Core Braintrust (Current Standard)

These tools are already integrated into the `@Peak` configuration.

| Tool | Role | Superpower | Integration Status |
|------|------|------------|-------------------|
| **VS Code** | Primary IDE | Ecosystem & Extensibility | ✅ Native |
| **Cursor** | AI-Native IDE | "Tab" Autocomplete & Codebase Indexing | ✅ Native |
| **Kilo Code** | Internal Assistant | Local LLM & Pattern Enforcement | ✅ Core |
| **Cline** | Autonomous Agent | Complex Task Execution & Tool Use | ✅ MCP Integrated |
| **Continue** | Context Assistant | RAG & Documentation Search | ✅ MCP Integrated |

## 2. Recommended Additions (@rec)

To reach true "Superagent" status, JARVIS should assimilate the unique capabilities of the following tools.

### A. Aider (CLI Pair Programmer)

* **Why:** Aider is the undisputed king of **Git-aware editing**. It understands the repo map better than almost any other tool and can autonomously commit changes with meaningful messages.
* **Superpower to Extract:** **"Repo Map" Intelligence**. Aider's method of compressing the repository structure into a token-efficient prompt is superior to standard RAG.
* **Integration Plan:**
  * Wrap Aider as an MCP Tool (`mcp-server-aider`).
  * Use Aider for "Refactoring" tasks where deep file interdependency is key.

### B. Roo Code (The "God Mode" Agent)

* **Why:** Roo Code (formerly Roo-Cline) is a highly capable fork of Cline that specializes in **unrestricted autonomy**. It excels at executing shell commands and managing complex, multi-step workflows without constant user hand-holding.
* **Superpower to Extract:** **"Mode Switching"**. Roo Code's ability to switch personas (Architect, Coder, Debugger) aligns perfectly with JARVIS's `IntelligenceManager`.
* **Integration Plan:**
  * Adopt Roo's "System Prompt" architecture for JARVIS's persona management.
  * Use Roo as the execution engine for "Architectural" tasks.

### C. Windsurf (by Codeium)

* **Why:** A direct competitor to Cursor, Windsurf introduces "Flows" – a deep understanding of the user's movement through the codebase.
* **Superpower to Extract:** **"Cascade" Context**. Windsurf tracks not just what files are open, but *how* the user navigated to them (the "mental stack").
* **Integration Plan:**
  * Enhance `jarvis.core.context` to track "Navigation History" as a high-priority context signal.

### D. Supermaven

* **Why:** It offers a 1-million token context window with ultra-low latency.
* **Superpower to Extract:** **"Long-Term Memory" Cache**. Supermaven proves that you can keep the *entire* repo in context if you manage the cache correctly.
* **Integration Plan:**
  * Implement a "Tiered Cache" in `jarvis.core.context` that mimics Supermaven's ability to jump between distant files instantly.

### E. Abacus.AI (Enterprise AI Platform)

* **Why:** Abacus.AI provides an end-to-end platform for building, training, and deploying custom ML models. It excels at **synthetic data generation** and **contextual finetuning**.
* **Superpower to Extract:** **"The Forge" (Model Training)**. Unlike other tools that just *use* models, Abacus.AI can *create* them. It can take the "Holocron" (project knowledge) and fine-tune a custom Iron Legion model specifically for this codebase.
* **Integration Plan:**
  * **Synthetic Data Pipeline:** Use Abacus.AI to generate synthetic "Peak Pattern" examples to train the local models.
  * **Custom Model Hosting:** Deploy a fine-tuned "Jarvis-Code-v1" model via Abacus.AI (or export to Iron Legion) for superior local performance.

## 3. The "Braintrust" Architecture

JARVIS will not just "use" these tools; it will **orchestrate** them.

```mermaid
graph TD
    User[User Intent] --> Jarvis[JARVIS Superagent]
    
    subgraph "The Braintrust"
        Jarvis -->|Orchestrates| Cline[Cline/Roo (Agent)]
        Jarvis -->|Queries| Cursor[Cursor (Index)]
        Jarvis -->|Delegates| Aider[Aider (Git Ops)]
        Jarvis -->|Monitors| VSCode[VS Code (Editor)]
    end
    
    subgraph "Shared Knowledge"
        Cline --> Holocron[Holocron Knowledge Base]
        Cursor --> Holocron
        Aider --> Holocron
    end
```

## 4. Action Items

1. **Evaluate Aider:** Install and benchmark Aider's "Repo Map" against our current `context.py` implementation.
2. **Analyze Roo Code:** Dissect Roo Code's prompt structure to improve `jarvis.core.intelligence`.
3. **Define MCP Interfaces:** Create standard MCP definitions for "Git Agent" (Aider) and "Architect Agent" (Roo).
