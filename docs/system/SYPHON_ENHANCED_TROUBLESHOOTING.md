# SYPHON-Enhanced Troubleshooting System

## Overview

Re-engineered troubleshooting module with SYPHON intelligence extraction. Integrates proactive troubleshooting logic (pattern recognition, building blocks, simulation, @FF automation) with SYPHON intelligence extraction.

## Architecture

### Components

1. **SYPHON Troubleshooting Extractor** (`syphon/troubleshooting_extractor.py`)
   - Extracts intelligence from troubleshooting sessions
   - Pattern recognition (#patterns)
   - Building blocks breakdown
   - Fix strategies and success rates
   - @FF keyboard shortcuts tracking
   - Proven patterns extraction

2. **JARVIS SYPHON-Enhanced Troubleshooting** (`jarvis_syphon_enhanced_troubleshooting.py`)
   - Main troubleshooting orchestrator
   - Integrates proactive troubleshooter
   - Integrates universal workflow troubleshooting
   - SYPHON intelligence extraction
   - Pattern recognition and intent extraction
   - Simulation before application
   - @FF automation

3. **Proactive IDE Troubleshooter** (`jarvis_proactive_ide_troubleshooter.py`)
   - Pattern detection (#patterns)
   - Building blocks breakdown
   - Simulation before application
   - @FF keyboard shortcuts

4. **Universal Workflow Troubleshooting** (`universal_workflow_troubleshooting.py`)
   - Roast/repair evaluation
   - Decision-making
   - AIQ consensus
   - Jedi Council approval

## Features

### Pattern Recognition (#patterns)
- Detects error patterns in behavior/actions
- Extracts intent from patterns
- Identifies building blocks
- Maps patterns to proven solutions

### Building Blocks Breakdown
- Breaks down errors into basic components
- Identifies root causes
- Maps to fix strategies

### Simulation
- Simulates fixes before applying
- Calculates success rates
- Validates fix strategies
- Only applies high-confidence fixes (>75%)

### @FF Keyboard Shortcuts
- Tracks keyboard shortcuts used
- Automates fix application
- Integrates with IDE shortcuts

### SYPHON Intelligence Extraction
- Extracts actionable intelligence
- Identifies proven patterns
- Tracks fix success rates
- Builds knowledge base

## Usage

### Basic Troubleshooting

```python
from jarvis_syphon_enhanced_troubleshooting import JARVISSyphonEnhancedTroubleshooting

troubleshooter = JARVISSyphonEnhancedTroubleshooting()

error_data = {
    "error_id": "error_001",
    "error_type": "syntax_error",
    "message": "Syntax error in file",
    "file_path": "test.py",
    "line": 10,
    "column": 5
}

result = troubleshooter.troubleshoot_with_syphon(
    error_data,
    mode="on_error",
    level="standard"
)

print(f"Patterns detected: {len(result.patterns_detected)}")
print(f"Intent: {result.intent_extracted}")
print(f"Simulation success rate: {result.simulation_success_rate:.0%}")
print(f"Fix applied: {result.fix_success}")
print(f"Actionable intelligence: {len(result.actionable_intelligence)}")
```

### CLI Usage

```bash
# Basic troubleshooting
python scripts/python/jarvis_syphon_enhanced_troubleshooting.py

# With error file
python scripts/python/jarvis_syphon_enhanced_troubleshooting.py \
    --error-file error_data.json \
    --mode on_error \
    --level standard

# With error JSON
python scripts/python/jarvis_syphon_enhanced_troubleshooting.py \
    --error-json '{"error_id": "test", "message": "Error message"}' \
    --mode on_error \
    --level deep
```

## Integration

### With Proactive Troubleshooter

The enhanced troubleshooting automatically uses the proactive troubleshooter for:
- Pattern detection
- Building blocks extraction
- Simulation
- Fix application

### With Universal Troubleshooting

Integrates universal workflow troubleshooting for:
- Roast/repair evaluation
- Decision-making
- AIQ consensus
- Jedi Council approval

### With SYPHON System

Extracts intelligence via SYPHON:
- Actionable items
- Tasks
- Decisions
- Intelligence/insights
- Proven patterns

## Data Flow

1. **Error Detection** → Proactive troubleshooter detects errors
2. **Pattern Recognition** → Identifies patterns and intent
3. **Building Blocks** → Breaks down into components
4. **Simulation** → Simulates fix and calculates success rate
5. **Universal Evaluation** → Roast/repair and decision-making
6. **Fix Application** → Applies fix if simulation successful (>75%)
7. **SYPHON Extraction** → Extracts intelligence from troubleshooting session
8. **Result Storage** → Saves result with all intelligence

## Intelligence Extraction

### Extracted Data

- **Patterns**: Error patterns detected
- **Intent**: Intent extracted from patterns
- **Building Blocks**: Basic components identified
- **Fix Strategies**: Fix strategies and success rates
- **@FF Shortcuts**: Keyboard shortcuts used
- **Actionable Items**: Items requiring action
- **Tasks**: Tasks identified
- **Decisions**: Decisions made
- **Intelligence**: Insights and proven patterns

### Proven Patterns

Patterns with >75% success rate are marked as "proven" and:
- Auto-applied for similar errors
- Tracked in knowledge base
- Used for future troubleshooting

## Configuration

### SYPHON Configuration

```python
from syphon.core import SYPHONConfig, SubscriptionTier

config = SYPHONConfig(
    project_root=Path("/path/to/project"),
    subscription_tier=SubscriptionTier.ENTERPRISE,
    enable_self_healing=True
)
```

### Troubleshooting Modes

- `pre`: Pre-workflow evaluation
- `post`: Post-workflow evaluation
- `continuous`: Continuous evaluation
- `on_error`: Evaluation on error (default)

### Evaluation Levels

- `basic`: Quick evaluation
- `standard`: Standard evaluation (default)
- `deep`: Deep analysis
- `jedi_council`: Full Jedi Council approval

## Tags

@SYPHON #TROUBLESHOOTING #PATTERNS #PEAK #FF #INTELLIGENCE #PROACTIVE #SIMULATION
