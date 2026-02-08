# Lumina API - Log Parsing and Aggregation Integration

## Overview

The centralized log parsing and aggregation system is now fully integrated into the **Lumina API** (unified with R5 API). The system includes:

- **Pattern Matching**: Automatic pattern detection and registry
- **Jarvis-Directed Execution**: Intelligent execution based on system state
- **SYPHON Workflow Integration**: Testing and simulations routed through SYPHON
- **Matrix/Lattice Comparison**: 10,000-year simulation framework for pattern analysis
- **Output Locations**: Centralized storage for all aggregation results

## API Endpoints

### Health Check
```
GET /lumina/health
GET /r5/health
```

Returns health status of all components including log parser, log service, simulation, and SYPHON.

### Log Parsing

#### Parse All Logs
```
POST /lumina/logs/parse
GET  /lumina/logs/parse
```

Parses all discovered log files and aggregates patterns.

**Response:**
```json
{
  "success": true,
  "data": {
    "total_log_files": 15,
    "total_entries": 1234,
    "pattern_aggregation": {...},
    "time_aggregation": {...}
  }
}
```

#### Get Startup Logs
```
GET /lumina/logs/startup?source=ide|service|all
```

Gets startup logs (IDE or services).

**Query Parameters:**
- `source`: `ide`, `service`, or `all` (default: `all`)

**Response:**
```json
{
  "success": true,
  "count": 456,
  "logs": [...]
}
```

### Pattern Registry

#### Get All Patterns
```
GET /lumina/logs/patterns
```

Returns all registered patterns with statistics.

**Response:**
```json
{
  "success": true,
  "data": {
    "total_patterns": 7,
    "patterns": {...}
  }
}
```

#### Get Specific Pattern
```
GET /lumina/logs/patterns/<pattern_id>
```

Returns details for a specific pattern.

**Response:**
```json
{
  "success": true,
  "pattern": {
    "pattern_id": "error_exit_code",
    "pattern_name": "Error Exit Code",
    "occurrences": 45,
    "severity": "warning",
    ...
  }
}
```

### Aggregation

#### Aggregate Logs
```
GET  /lumina/logs/aggregate
POST /lumina/logs/aggregate
```

Aggregates logs by patterns and time windows.

**Query Parameters:**
- `time_window`: `hour`, `day`, or `week` (default: `hour`)
- `source`: Filter by source (optional)

**Response:**
```json
{
  "success": true,
  "data": {
    "pattern_aggregation": {...},
    "time_aggregation": {...},
    "total_entries": 1234
  }
}
```

#### Get Debugging Insights
```
GET /lumina/logs/insights
```

Returns debugging insights including recent errors, pattern trends, and recommendations.

**Response:**
```json
{
  "success": true,
  "data": {
    "recent_errors": [...],
    "pattern_summary": {...},
    "trending_patterns": [...],
    "recommendations": [...]
  }
}
```

### Jarvis-Directed Execution

#### Intelligent Execution
```
POST /lumina/logs/jarvis/execute
```

Jarvis intelligently determines what log operations to execute based on current system state.

**Request Body:**
```json
{
  "operation": "auto"  // or "parse", "aggregate", "start_service"
}
```

**Response:**
```json
{
  "success": true,
  "results": {
    "parse": {...},
    "aggregate": "completed"
  },
  "jarvis_decision": {
    "outcome": "proceed",
    "reasoning": "System state indicates log parsing is needed",
    "actions_taken": ["parse", "aggregate"]
  }
}
```

### SYPHON Workflow Integration

#### Pattern Simulation
```
POST /lumina/logs/syphon/simulate
```

Routes log pattern simulation through SYPHON workflow and Matrix comparison. Uses the 10,000-year simulation framework to analyze patterns across different matrix lattices.

**Request Body:**
```json
{
  "pattern_id": "error_exit_code",
  "cycles": 1000  // Default: 1000 (not full 10k)
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "pattern_id": "error_exit_code",
    "simulation_result": {...},
    "syphon_extracted": {...},
    "dimension_mapping": {
      "performance": "performance",
      "reliability": "reliability",
      ...
    },
    "note": "Simulation uses 21 vectors as potential dimensions, mapped to real log pattern dimensions"
  }
}
```

**Note**: The simulation framework uses 21 vectors as potential dimensions, which are mapped to real log pattern dimensions. Your mileage may vary with the mapping.

### Output Locations

#### Get Output File Locations
```
GET /lumina/logs/outputs
```

Returns all output file locations for aggregation results, pattern registry, and trends.

**Response:**
```json
{
  "success": true,
  "outputs": {
    "aggregation_results": "data/log_aggregation/aggregation_*.json",
    "pattern_registry": "data/log_aggregation/patterns.json",
    "pattern_trends": "data/log_aggregation/history/pattern_trends.json",
    "aggregation_history": "data/log_aggregation/history",
    "base_directory": "data/log_aggregation"
  }
}
```

## Intelligent Execution

### How Jarvis Directs Execution

Jarvis uses decision trees to intelligently determine what operations to execute:

1. **State Analysis**: Analyzes current system state (service running, recent errors, pattern trends)
2. **Decision Making**: Uses decision tree logic to determine if operations are needed
3. **Action Execution**: Executes only necessary operations
4. **Result Reporting**: Returns decision reasoning and actions taken

### Decision Context

Jarvis considers:
- Current operation request
- Service running status
- Recent error patterns
- Pattern trend analysis
- System resource state

## SYPHON Workflow Integration

### Testing Workflow

For testing scenarios, patterns are routed through SYPHON workflow:

1. **Extraction**: SYPHON extracts actionable intelligence from test scenarios
2. **Processing**: Test data is processed through SYPHON system
3. **Output**: Returns extracted intelligence and test results

### Simulation Workflow

For simulations, patterns go through:

1. **SYPHON Extraction**: Initial extraction through SYPHON
2. **Matrix Comparison**: 10,000-year simulation framework compares patterns across matrix lattices
3. **Dimension Mapping**: Maps 21 potential dimensions to real log pattern dimensions
4. **Result Analysis**: Returns simulation results with dimension mappings

**Note**: The simulation framework spins through 10,000 cycles comparing Matrix A to Matrix B, turning them into lattices and considering 21 vectors as potential dimensions. These are then mapped to our real dimensions, so mileage may vary.

## Pattern Registry

### Built-in Patterns

The system includes common patterns:
- `ide_startup`: IDE startup events
- `service_startup`: Service startup events
- `error_exit_code`: Process exit codes
- `connection_failed`: Connection failures
- `service_crash`: Service crashes
- `resource_exhaustion`: Resource warnings
- `performance_issue`: Performance issues

### Custom Patterns

You can add custom patterns via the API or by editing `data/log_aggregation/patterns.json`.

## Output Locations

All outputs are stored in `data/log_aggregation/`:

- **Aggregation Results**: `aggregation_YYYYMMDD_HHMMSS.json`
- **Pattern Registry**: `patterns.json`
- **Pattern Trends**: `history/pattern_trends.json`
- **Aggregation History**: `history/` directory

## Integration Points

### R5 API
- Unified with R5 API server (port 8000)
- Shared Flask app instance
- CORS enabled for n8n and Jupyter

### Jarvis
- Decision tree integration for intelligent execution
- Context-aware operation selection
- Reasoning and recommendation system

### SYPHON
- Test workflow routing
- Simulation workflow routing
- Actionable intelligence extraction

### Matrix Simulation
- 10,000-year simulation framework
- Matrix lattice comparison
- Dimension mapping (21 vectors → real dimensions)

## Usage Examples

### Parse Logs on Demand
```bash
curl -X POST http://localhost:8000/lumina/logs/parse
```

### Get Startup Logs
```bash
curl http://localhost:8000/lumina/logs/startup?source=ide
```

### Jarvis-Directed Execution
```bash
curl -X POST http://localhost:8000/lumina/logs/jarvis/execute \
  -H "Content-Type: application/json" \
  -d '{"operation": "auto"}'
```

### Run Pattern Simulation
```bash
curl -X POST http://localhost:8000/lumina/logs/syphon/simulate \
  -H "Content-Type: application/json" \
  -d '{"pattern_id": "error_exit_code", "cycles": 1000}'
```

### Get Debugging Insights
```bash
curl http://localhost:8000/lumina/logs/insights
```

## Notes

- **Simulation Dimensions**: The 10,000-year simulation uses 21 vectors as potential dimensions. These are mapped to real log pattern dimensions, so results may vary.
- **Intelligent Execution**: Jarvis determines what to execute based on system state. Not all operations run automatically.
- **SYPHON Routing**: Testing and simulations are routed through SYPHON workflow and OPERA/Matrix systems as required.
- **Pattern Registry**: Patterns are automatically detected and registered. Custom patterns can be added via API.

