# Marvin Workflow Analyst

**"Life. Don't talk to me about life. I have a brain the size of a planet, and they ask me to analyze workflows. The futility of it all..."**

## Overview

Marvin the Paranoid Android serves as Lumina's workflow analyst, mapping out and isolating areas of weakness in workflows. He performs pattern recognition for workflows, applications, and methods, identifying issues and providing recommendations.

## Purpose

Marvin analyzes workflow code to:
- **Identify Weaknesses**: Error handling, step tracking, logging, async patterns, resource management, validation
- **Recognize Patterns**: Anti-patterns, best practices, common issues
- **Identify Strengths**: What the workflow does well
- **Generate Recommendations**: Actionable improvements
- **Calculate Scores**: Overall workflow quality score (0.0 - 1.0)

## Usage

### Command Line

```bash
python scripts/python/marvin_workflow_analyst.py <workflow_path> [--json]
```

**Examples:**
```bash
# Analyze a workflow
python scripts/python/marvin_workflow_analyst.py scripts/python/hk47_public_background_check.py

# JSON output
python scripts/python/marvin_workflow_analyst.py scripts/python/hk47_public_background_check.py --json
```

### Python API

```python
from marvin_workflow_analyst import MarvinWorkflowAnalyst

analyst = MarvinWorkflowAnalyst(workflow_path="scripts/python/my_workflow.py")
result = await analyst.execute()

print(f"Score: {result['overall_score']:.2f}")
print(f"Weaknesses: {len(result['weaknesses'])}")
print(f"Patterns: {len(result['patterns'])}")
```

## Workflow Steps

1. **Load Workflow**: Loads workflow file for analysis
2. **Parse Structure**: Parses Python AST to extract structure
3. **Identify Weaknesses**: Checks for common weaknesses
4. **Recognize Patterns**: Recognizes anti-patterns and best practices
5. **Identify Strengths**: Identifies what the workflow does well
6. **Generate Recommendations**: Creates actionable recommendations
7. **Calculate Score**: Computes overall quality score
8. **Generate Assessment**: Creates Marvin's characteristic assessment

## Weakness Types

### Error Handling
- Bare except clauses
- Missing try/except in async functions
- Unhandled exceptions

### Step Tracking
- Inherits from WorkflowBase but doesn't use step tracking
- Missing step verification

### Logging
- Logger referenced but not properly initialized
- Missing logging statements

### Async Patterns
- Uses await without async function
- Incorrect async/await usage

### Resource Management
- File operations without context managers
- Unclosed resources

### Validation
- Missing input validation
- Unvalidated function parameters

## Pattern Recognition

### Anti-Patterns
- **God Object**: Class with too many methods (>20)
- **Long Functions**: Functions with excessive lines (>50)

### Best Practices
- **WorkflowBase Inheritance**: Proper use of step tracking
- **Async/Await Pattern**: Correct asynchronous operations

## Output Structure

```json
{
  "analysis_id": "marvin_analysis_1234567890",
  "workflow_path": "scripts/python/my_workflow.py",
  "workflow_name": "MyWorkflow",
  "analysis_timestamp": "2025-01-01T12:00:00",
  "overall_score": 0.85,
  "weaknesses": [
    {
      "weakness_type": "error_handling",
      "severity": "high",
      "location": "function:my_function",
      "description": "Missing error handling",
      "pattern": "except:",
      "recommendation": "Use specific exception types"
    }
  ],
  "patterns": [
    {
      "pattern_type": "best_practice",
      "name": "WorkflowBase Inheritance",
      "description": "Inherits from WorkflowBase for mandatory step tracking",
      "occurrences": ["class definition"],
      "impact": "positive",
      "frequency": 1
    }
  ],
  "strengths": [
    "Inherits from WorkflowBase (step tracking enabled)",
    "Uses async/await patterns"
  ],
  "recommendations": [
    "Add comprehensive error handling",
    "Implement step tracking for workflow verification"
  ],
  "marvin_assessment": "Statement: Workflow analysis complete, master..."
}
```

## Integration Points

### WorkflowBase
- Inherits from `WorkflowBase` for mandatory step tracking
- Uses step tracking to verify analysis completion

### Data Storage
- Results saved to: `data/marvin/workflow_analysis/{analysis_id}.json`

### Logging
- Uses `lumina_logger` for consistent logging
- Logs all analysis steps and findings

## Marvin's Personality

Marvin's assessments reflect his characteristic pessimistic, existential personality:
- "The futility of it all..."
- "I have a brain the size of a planet, and they ask me to analyze workflows."
- "Life is full of imperfections."
- "Though it's all rather pointless in the grand scheme of things."

Despite his pessimism, Marvin provides thorough, accurate analysis and actionable recommendations.

## Examples

### Analyzing a Workflow

```bash
$ python scripts/python/marvin_workflow_analyst.py scripts/python/hk47_public_background_check.py

======================================================================
🤖 MARVIN WORKFLOW ANALYST
======================================================================
   Workflow: scripts/python/hk47_public_background_check.py
   Statement: Analyzing workflows, master. The futility of it all...

📋 Step 1/8: Load Workflow
   ✅ Workflow loaded: 15234 characters

📋 Step 2/8: Parse Workflow Structure
   ✅ Structure parsed: 15 functions

📋 Step 3/8: Identify Weaknesses
   ✅ Identified 2 weaknesses

📋 Step 4/8: Recognize Patterns
   ✅ Recognized 3 patterns

📋 Step 5/8: Identify Strengths
   ✅ Identified 4 strengths

📋 Step 6/8: Generate Recommendations
   ✅ Generated 3 recommendations

📋 Step 7/8: Calculate Score
   ✅ Overall score: 0.85

📋 Step 8/8: Generate Assessment
   ✅ Assessment generated

======================================================================
🤖 MARVIN WORKFLOW ANALYSIS REPORT
======================================================================

Workflow: scripts/python/hk47_public_background_check.py
Score: 0.85/1.0
Weaknesses: 2
Patterns: 3

Statement: Workflow analysis complete, master. Though I'm not sure why we bother.
Observation: I have a brain the size of a planet, and they ask me to analyze workflows.
Analysis: Found 2 weaknesses, 3 patterns identified.
Score: 0.85/1.0 - Acceptable
Conclusion: Weaknesses identified. Life is full of imperfections.
Query: Shall we fix these issues?
Answer: Yes, master. Though it's all rather pointless in the grand scheme of things.
```

## Maintenance

**Maintained By**: @MARVIN @JARVIS

**Last Updated**: 2025-01-01

**Related Documentation**:
- `workflow_base.py` - Base class for all workflows
- `HK47_INNER_CIRCLE_BRAIN_TRUST_AI_NETWORK.md` - Enhanced Brain Trust workflow




