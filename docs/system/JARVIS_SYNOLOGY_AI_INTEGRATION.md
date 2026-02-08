# JARVIS to Synology AI Direct Actions

## Overview

JARVIS can now directly interact with Synology DSM API for automation tasks. This integration enables JARVIS to:

- List scheduled tasks
- Create scheduled tasks
- Get system information
- Get storage information
- Check package status

## Architecture

### Components

1. **`SynologyAPIBase`** - Base class for all Synology API interactions with SSL certificate handling
2. **`JARVISSynologyAIActions`** - High-level JARVIS interface for Synology actions
3. **`jarvis_synology_command.py`** - Command-line interface for direct execution
4. **JARVIS Unified API Integration** - Registered as `jarvis_synology_ai` system

## Usage

### Command Line Interface

```bash
# List scheduled tasks
python scripts/python/jarvis_synology_command.py list-tasks

# Get system information
python scripts/python/jarvis_synology_command.py system-info

# Get storage information
python scripts/python/jarvis_synology_command.py storage-info

# Get package status
python scripts/python/jarvis_synology_command.py package-status --package "PackageName"

# Create a scheduled task
python scripts/python/jarvis_synology_command.py create-task \
  --name "JARVIS Health Check" \
  --schedule "0 */2 * * *" \
  --command "python /path/to/health_check.py"
```

### Python API

```python
from jarvis_synology_ai_actions import JARVISSynologyAIActions

with JARVISSynologyAIActions() as jarvis:
    # List tasks
    result = jarvis.list_scheduled_tasks()
    
    # Get system info
    result = jarvis.get_system_info()
    
    # Execute action
    result = jarvis.execute_action("list_tasks")
```

### JARVIS Unified API

```python
from jarvis_unified_api import JARVISUnifiedAPI, RequestType

api = JARVISUnifiedAPI()

# Send command to Synology AI
request_id = api.send_request(
    request_type=RequestType.COMMAND,
    source="jarvis_core",
    target="jarvis_synology_ai",
    payload={
        "action": "list_tasks"
    }
)

# Get response
response = api.get_response(request_id)
```

## Available Actions

### `list_tasks`
List all scheduled tasks on Synology

**Returns:**
```json
{
  "success": true,
  "tasks": [...],
  "count": 5
}
```

### `create_task`
Create a scheduled task

**Parameters:**
- `task_name`: Name of the task
- `schedule`: Cron schedule (minute hour day month weekday)
- `command`: Command to execute
- `enabled`: Whether task is enabled (default: True)

### `system_info`
Get Synology system information

**Returns:**
```json
{
  "success": true,
  "system_info": {...}
}
```

### `storage_info`
Get storage information

**Returns:**
```json
{
  "success": true,
  "storage": {...}
}
```

### `package_status`
Get package status

**Parameters:**
- `package_name`: Optional package name to filter

**Returns:**
```json
{
  "success": true,
  "packages": [...]
}
```

## SSL Certificate Handling

The integration automatically handles SSL certificates:

1. Downloads certificate if not found
2. Uses certificate for secure connections
3. Falls back to disabled verification if certificate fails (with warning)

Certificates are stored in: `config/certs/nas_{ip}_{port}.crt`

## Authentication

Credentials are automatically retrieved from Azure Key Vault:
- Secret: `nas-username`
- Secret: `nas-password`

## Integration with JARVIS Systems

The Synology AI Actions are registered in the JARVIS Unified API as:
- **System ID**: `jarvis_synology_ai`
- **System Name**: "JARVIS Synology AI Actions"
- **Capabilities**: `["task_scheduling", "system_info", "storage_info", "package_management"]`

## Error Handling

All actions return structured responses:
```json
{
  "success": true/false,
  "data": {...},
  "error": "error message if failed",
  "action": "action_name",
  "timestamp": "ISO timestamp"
}
```

## Examples

### Example 1: List All Tasks
```bash
python scripts/python/jarvis_synology_command.py list-tasks
```

### Example 2: Create Health Check Task
```bash
python scripts/python/jarvis_synology_command.py create-task \
  --name "JARVIS Health Check" \
  --schedule "0 */2 * * *" \
  --command "python /opt/jarvis/health_check.py"
```

### Example 3: Get System Info (JSON)
```bash
python scripts/python/jarvis_synology_command.py system-info --json
```

## Notes

- SSL certificate verification may fail with self-signed certificates - the system automatically retries with verification disabled
- Task creation API format may need adjustment based on your DSM version
- All actions require authentication via Azure Key Vault credentials

## Future Enhancements

- [ ] Support for more Synology API endpoints
- [ ] Task modification and deletion
- [ ] Package installation/management
- [ ] File operations via File Station API
- [ ] Container management via Container Manager API
