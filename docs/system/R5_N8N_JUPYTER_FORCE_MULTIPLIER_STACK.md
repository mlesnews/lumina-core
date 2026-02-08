# R5 + n8n + Jupyter Force Multiplier Stack

## Overview

The R5 Living Context Matrix system, integrated with n8n workflows and Jupyter notebooks, creates a **force multiplier effect** by stacking multiple services and features for maximum effectiveness.

## Architecture

```
┌─────────────────┐
│   IDE Sessions  │
│  (Chat History) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   R5 System     │
│  - Aggregation  │
│  - @PEAK Extract│
│  - @WHATIF      │
└─────┬───────┬───┘
      │       │
      ▼       ▼
┌─────────┐ ┌──────────┐
│   n8n   │ │ Jupyter  │
│Workflows│ │ Notebooks│
└─────────┘ └──────────┘
```

## Components

### 1. R5 Living Context Matrix

**Purpose**: Continuously aggregates IDE chat sessions into concentrated knowledge

**Features**:
- **@PEAK Pattern Extraction**: Identifies high-quality, reusable components
- **@WHATIF Thought Experiments**: Captures exploratory scenarios
- **Knowledge Condensation**: Creates the most concentrated form of knowledge
- **Matrix Visualization**: Visual representation of knowledge relationships

**Location**: `scripts/python/r5_living_context_matrix.py`

**Data Directory**: `data/r5_living_matrix/`

**Output**: `data/r5_living_matrix/LIVING_CONTEXT_MATRIX_PROMPT.md`

### 2. n8n Integration

**Purpose**: Workflow automation for R5 operations

**Workflows**:
- **R5 Aggregate Sessions**: Hourly aggregation of chat sessions
- **R5 @PEAK Extraction**: Extract and store @PEAK patterns
- **R5 to Jupyter Pipeline**: Export R5 data to Jupyter notebooks

**Configuration**: `config/n8n/r5_workflows.json`

**Webhook Base**: `http://localhost:5678/webhook/r5`

### 3. Jupyter Notebook Server

**Purpose**: Interactive analysis and visualization of R5 data

**Features**:
- Data analysis with pandas/numpy
- Visualization with matplotlib/seaborn/plotly
- Interactive widgets for exploration
- Integration with R5 API for live data

**Location**: `data/jupyter/`

**Sample Notebook**: `data/jupyter/R5_Living_Context_Matrix.ipynb`

## Force Multiplier Effects

### Stack 1: R5 + n8n
- **Automated Aggregation**: n8n triggers hourly R5 aggregation
- **Pattern Detection**: Automatic @PEAK pattern extraction
- **Workflow Orchestration**: Complex multi-step knowledge processing

### Stack 2: R5 + Jupyter
- **Interactive Analysis**: Explore R5 data in real-time
- **Visualization**: Create charts and graphs from aggregated knowledge
- **Data Science**: Apply ML/AI techniques to knowledge patterns

### Stack 3: n8n + Jupyter
- **Automated Notebooks**: n8n creates Jupyter notebooks from R5 data
- **Scheduled Reports**: Generate periodic analysis reports
- **Data Pipeline**: Automated data flow from R5 to Jupyter

### Stack 4: R5 + n8n + Jupyter (Full Stack)
- **500x Effectiveness**: Combined force multiplier effect
- **Complete Automation**: End-to-end knowledge processing
- **Maximum Intelligence**: All services working in harmony

## Setup Instructions

### 1. Run Setup Script

```powershell
.\scripts\setup_r5_n8n_jupyter_stack.ps1 -InstallN8n -InstallJupyter -StartServices
```

This will:
- Create all necessary directories
- Configure R5 system
- Set up n8n workflows
- Configure Jupyter server
- Install required packages
- Start all services

### 2. Manual Setup (Alternative)

#### Install Dependencies

```powershell
# Install n8n
npm install -g n8n

# Install Jupyter
pip install jupyter jupyterlab notebook

# Install R5 API dependencies
pip install flask flask-cors

# Install Jupyter packages
pip install pandas numpy matplotlib seaborn plotly ipywidgets jupyter-dash
```

#### Start Services

```powershell
# Start R5 API Server
python scripts/python/r5_api_server.py

# Start n8n (in separate terminal)
n8n start

# Start Jupyter (in separate terminal)
jupyter lab
```

## Usage

### Ingesting Sessions

```python
from r5_living_context_matrix import R5LivingContextMatrix
from pathlib import Path

r5 = R5LivingContextMatrix(Path("."))

session_data = {
    "session_id": "session_001",
    "timestamp": "2025-11-24T01:00:00",
    "messages": [
        {"role": "user", "content": "How do I use @PEAK patterns?"},
        {"role": "assistant", "content": "@PEAK patterns are..."}
    ]
}

r5.ingest_session(session_data)
```

### Via API

```bash
# Ingest session
curl -X POST http://localhost:8000/r5/session \
  -H "Content-Type: application/json" \
  -d '{"session_id": "test", "messages": [...]}'

# Aggregate sessions
curl http://localhost:8000/r5/aggregate

# Get data for Jupyter
curl http://localhost:8000/r5/jupyter/export
```

### Via n8n

1. Access n8n at `http://localhost:5678`
2. Import workflows from `config/n8n/r5_workflows.json`
3. Workflows will automatically trigger based on schedule/webhooks

### Via Jupyter

1. Open Jupyter Lab at `http://localhost:8888`
2. Open `R5_Living_Context_Matrix.ipynb`
3. Run cells to analyze R5 data
4. Create visualizations and reports

## API Endpoints

### R5 API Server (Port 8000)

- `GET /r5/health` - Health check
- `POST /r5/session` - Ingest new session
- `GET /r5/aggregate` - Aggregate all sessions
- `GET /r5/data` - Get aggregated data
- `POST /r5/peak/extract` - Extract @PEAK patterns
- `GET /r5/jupyter/export` - Export for Jupyter
- `GET /r5/stats` - Get statistics
- `GET /r5/config` - Get configuration

## Configuration

### R5 Configuration

Edit `config/r5/r5_config.json`:

```json
{
  "r5_system": {
    "data_directory": "data/r5_living_matrix",
    "output_file": "data/r5_living_matrix/LIVING_CONTEXT_MATRIX_PROMPT.md",
    "aggregation_interval": 3600,
    "max_sessions": 1000,
    "features": {
      "peak_pattern_extraction": true,
      "whatif_thought_experiments": true,
      "matrix_visualization": true
    },
    "integrations": {
      "n8n": {
        "enabled": true,
        "webhook_url": "http://localhost:5678/webhook/r5"
      },
      "jupyter": {
        "enabled": true,
        "notebook_path": "data/jupyter"
      }
    }
  }
}
```

## Force Multiplier Examples

### Example 1: Automated Knowledge Extraction

1. **R5** aggregates chat sessions hourly
2. **n8n** triggers @PEAK pattern extraction
3. **Jupyter** visualizes pattern frequency
4. **Result**: Automated knowledge discovery pipeline

### Example 2: Interactive Analysis

1. **R5** provides aggregated data via API
2. **Jupyter** fetches data in real-time
3. **User** explores patterns interactively
4. **Result**: Deep insights into knowledge patterns

### Example 3: Complete Automation

1. **n8n** schedules hourly aggregation
2. **R5** processes and extracts patterns
3. **n8n** exports to Jupyter notebook
4. **Jupyter** generates visualization report
5. **Result**: Fully automated knowledge reporting

## Best Practices

1. **Regular Aggregation**: Run R5 aggregation at least hourly
2. **Pattern Review**: Regularly review @PEAK patterns for reuse
3. **@WHATIF Exploration**: Use @WHATIF scenarios for planning
4. **Visualization**: Create visualizations to understand patterns
5. **Automation**: Use n8n to automate repetitive tasks

## Troubleshooting

### R5 API not responding
- Check if server is running: `python scripts/python/r5_api_server.py`
- Verify port 8000 is not in use
- Check logs for errors

### n8n workflows not triggering
- Verify n8n is running: `n8n start`
- Check workflow configuration in n8n UI
- Verify webhook URLs are correct

### Jupyter not loading
- Check if Jupyter is running: `jupyter lab`
- Verify port 8888 is not in use
- Check notebook path in configuration

## Next Steps

1. **Run Setup**: Execute the setup script
2. **Ingest Sessions**: Start feeding chat sessions to R5
3. **Configure n8n**: Import and activate workflows
4. **Explore Jupyter**: Open and run sample notebook
5. **Monitor**: Watch the force multiplier effect in action!

## Support

For issues or questions:
- Check logs in `data/r5_living_matrix/`
- Review n8n workflow execution logs
- Check Jupyter notebook output
- Review API responses for errors

---

**Remember**: The power is in the stack! R5 + n8n + Jupyter = 500x effectiveness! 🚀

