# WOPR Experiment Framework
A/B Control and Experiment Creation and Comparison

## Overview

WOPR can create A (control) and B (experiment) scenarios, run them through the pipeline, and compare outcomes to the current situation. This enables systematic testing and validation of changes before deployment.

## Features

- **A/B Experiment Creation**: Create control (A) and experiment (B) scenarios
- **Current Situation Capture**: Capture baseline state before experiments
- **Pipeline Execution**: Run scenarios through SYPHON workflow, log parsing, and Matrix comparison
- **Outcome Comparison**: Compare A and B results with detailed metrics
- **WOPR Integration**: Fully integrated into WOPR workflow pipeline

## Workflow

### 1. Capture Current Situation
Before creating an experiment, capture the current situation as a baseline:

```bash
POST /wopr/experiments/capture
```

**Response:**
```json
{
  "success": true,
  "situation": {
    "timestamp": "2025-01-28T10:00:00",
    "system_state": {},
    "log_patterns": {
      "total_patterns": 7,
      "patterns": {...}
    },
    "metrics": {}
  }
}
```

### 2. Create Experiment
Create an A/B experiment with control and experiment configurations:

```bash
POST /wopr/experiments/create
```

**Request Body:**
```json
{
  "name": "Log Parsing Optimization",
  "description": "Test optimized log parsing vs current implementation",
  "control_config": {
    "log_parser": "current",
    "aggregation": "standard",
    "pattern_detection": "basic"
  },
  "experiment_config": {
    "log_parser": "optimized",
    "aggregation": "enhanced",
    "pattern_detection": "advanced"
  },
  "capture_current": true
}
```

**Response:**
```json
{
  "success": true,
  "experiment_id": "550e8400-e29b-41d4-a716-446655440000",
  "message": "Experiment created through WOPR workflow"
}
```

### 3. Run Experiment
Run the experiment through the WOPR pipeline:

```bash
POST /wopr/experiments/{experiment_id}/run
```

**Request Body:**
```json
{
  "duration": 60.0  // Duration in seconds for each scenario
}
```

**Response:**
```json
{
  "success": true,
  "experiment_id": "550e8400-e29b-41d4-a716-446655440000",
  "comparison": {
    "experiment_id": "550e8400-e29b-41d4-a716-446655440000",
    "control_result": {
      "scenario_id": "..._control",
      "scenario_type": "control",
      "metrics": {
        "log_entries": 1234,
        "patterns_matched": 5,
        "success": true
      },
      "patterns": {...},
      "duration": 2.5
    },
    "experiment_result": {
      "scenario_id": "..._experiment",
      "scenario_type": "experiment",
      "metrics": {
        "log_entries": 1100,
        "patterns_matched": 3,
        "success": true
      },
      "patterns": {...},
      "duration": 2.1
    },
    "differences": {
      "log_entries": {
        "control": 1234,
        "experiment": 1100,
        "difference": -134,
        "difference_percent": -10.86
      },
      "patterns_matched": {
        "control": 5,
        "experiment": 3,
        "difference": -2,
        "difference_percent": -40.0
      }
    },
    "recommendations": [
      "Experiment has 2 fewer error patterns",
      "Experiment produced fewer log entries",
      "Experiment (B) appears to be better"
    ],
    "winner": "experiment",
    "confidence": 0.8
  }
}
```

### 4. Get Experiment Details
Retrieve experiment information:

```bash
GET /wopr/experiments/{experiment_id}
```

### 5. List Experiments
List all experiments:

```bash
GET /wopr/experiments
```

## Pipeline Flow

When an experiment runs, it goes through the WOPR pipeline:

### 1. Scenario Configuration
- Control (A) scenario configuration is applied
- Experiment (B) scenario configuration is applied

### 2. SYPHON Workflow
- Scenarios are processed through SYPHON workflow
- Actionable intelligence is extracted
- Test data is routed through SYPHON system

### 3. Log Parsing and Aggregation
- Logs are parsed during scenario execution
- Patterns are detected and aggregated
- Metrics are collected

### 4. Matrix Comparison
- Scenarios are analyzed through Matrix/lattice comparison
- 10,000-year simulation framework is used (accelerated)
- Patterns are compared across different dimensions

### 5. Result Comparison
- Control and experiment results are compared
- Differences are calculated
- Winner is determined with confidence score
- Recommendations are generated

## Comparison Metrics

The framework compares:

- **Log Patterns**: Number and severity of patterns detected
- **Error Counts**: Number of errors in each scenario
- **Log Entry Counts**: Total log entries generated
- **Success Rates**: Whether scenarios completed successfully
- **Performance Metrics**: Duration, resource usage, etc.
- **Pattern Matches**: Patterns detected in each scenario

## Winner Determination

The framework determines a winner based on:

1. **Error Patterns**: Fewer error patterns = better
2. **Log Volume**: Fewer unnecessary logs = better
3. **Success Rate**: Successful completion = better
4. **Performance**: Faster execution = better

Confidence score is calculated based on the strength of differences.

## Integration Points

### WOPR Workflow
- Experiments are created and managed through WOPR
- Results are stored in `data/wopr_plans/experiments/`
- Status tracking integrated with WOPR operations

### SYPHON Workflow
- Scenarios are routed through SYPHON for testing
- Actionable intelligence is extracted
- Test data is processed through SYPHON system

### Log Parsing
- Logs are parsed during scenario execution
- Patterns are detected and aggregated
- Metrics are collected for comparison

### Matrix Comparison
- Scenarios are analyzed through Matrix/lattice framework
- 10,000-year simulation is used (accelerated)
- Patterns are compared across dimensions

## Usage Examples

### Create and Run Experiment

```python
import requests

# Capture current situation
response = requests.post("http://localhost:8000/wopr/experiments/capture")
current = response.json()["situation"]

# Create experiment
experiment_data = {
    "name": "Log Parsing Optimization",
    "description": "Test optimized vs current",
    "control_config": {"log_parser": "current"},
    "experiment_config": {"log_parser": "optimized"},
    "capture_current": True
}
response = requests.post(
    "http://localhost:8000/wopr/experiments/create",
    json=experiment_data
)
experiment_id = response.json()["experiment_id"]

# Run experiment
response = requests.post(
    f"http://localhost:8000/wopr/experiments/{experiment_id}/run",
    json={"duration": 60.0}
)
comparison = response.json()["comparison"]

print(f"Winner: {comparison['winner']}")
print(f"Confidence: {comparison['confidence']}")
print(f"Recommendations: {comparison['recommendations']}")
```

### Command Line Usage

```bash
# Capture current situation
python scripts/python/wopr_experiment_framework.py --capture

# Create experiment
python scripts/python/wopr_experiment_framework.py --create

# Run experiment
python scripts/python/wopr_experiment_framework.py --run <experiment_id>

# List experiments
python scripts/python/wopr_experiment_framework.py --list

# Show experiment
python scripts/python/wopr_experiment_framework.py --show <experiment_id>
```

## Output Locations

Experiments are stored in:
- `data/wopr_plans/experiments/{experiment_id}.json`

Each experiment file contains:
- Experiment metadata
- Control scenario (A) configuration
- Experiment scenario (B) configuration
- Current situation baseline
- Comparison results (after running)

## Notes

- **Pipeline Integration**: All experiments go through the WOPR workflow pipeline
- **SYPHON Routing**: Testing scenarios are routed through SYPHON workflow
- **Matrix Comparison**: Scenarios are analyzed through Matrix/lattice framework
- **Current Situation**: Baseline is captured before experiments for comparison
- **Cross the Bridge**: As you mentioned, we'll handle implementation details as we come to them

## Future Enhancements

- Real-time scenario execution
- More sophisticated comparison algorithms
- Statistical significance testing
- Multi-variant experiments (A/B/C/D...)
- Automated experiment recommendations
- Integration with deployment pipelines

