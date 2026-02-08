# MANUS User Control Guide

## Complete User Control Over MANUS

This guide provides complete control over all MANUS operations from the user perspective.

---

## Overview

The **MANUS User Control Interface** gives you full control over:

- ✅ **Status Management** - Check MANUS status and health
- ✅ **Task Execution** - Execute any MANUS task
- ✅ **Resource Provisioning** - Provision Azure resources
- ✅ **Configuration** - Manage MANUS configuration
- ✅ **NEO Browser Control** - Control NEO browser through MANUS
- ✅ **Monitoring** - View logs and task status
- ✅ **Automation** - Execute automated workflows

---

## Quick Start

```bash
# Get MANUS status
python scripts/python/manus_user_control_interface.py --status

# View help
python scripts/python/manus_user_control_interface.py --help
```

---

## Command Reference

### Status Commands

```bash
# Get current status
python scripts/python/manus_user_control_interface.py --status

# Check MANUS health
python scripts/python/manus_user_control_interface.py --check
```

### Task Execution

```bash
# Provision Azure Speech service
python scripts/python/manus_user_control_interface.py --provision azure_speech

# Execute a script
python scripts/python/manus_user_control_interface.py --execute "python scripts/my_script.py"

# Execute a command
python scripts/python/manus_user_control_interface.py --execute "az account show"
```

### NEO Browser Control

```bash
# Launch NEO browser
python scripts/python/manus_user_control_interface.py --neo-launch "https://elevenlabs.io"

# Get cookies for domain
python scripts/python/manus_user_control_interface.py --neo-cookies "elevenlabs.io"

# Automated ElevenLabs setup
python scripts/python/manus_user_control_interface.py --neo-elevenlabs
```

### Configuration Management

```bash
# Get current configuration
python scripts/python/manus_user_control_interface.py --config-get

# Update configuration
python scripts/python/manus_user_control_interface.py --configure '{"log_level": "DEBUG", "task_timeout": 600}'

# Reset configuration
python scripts/python/manus_user_control_interface.py --config-reset
```

### Monitoring

```bash
# View recent logs
python scripts/python/manus_user_control_interface.py --logs 50

# List active tasks
python scripts/python/manus_user_control_interface.py --tasks
```

---

## Python API Usage

### Basic Usage

```python
from manus_user_control_interface import MANUSUserControl

# Initialize
control = MANUSUserControl()

# Get status
status = control.get_status()
print(status)

# Execute task
result = control.execute_task(
    MANUSTaskType.PROVISION,
    {"resource_type": "azure_speech"}
)
print(result)

# Control NEO browser
result = control.control_neo_browser(
    "launch",
    {"url": "https://elevenlabs.io"}
)
print(result)
```

### Advanced Usage

```python
from manus_user_control_interface import MANUSUserControl, MANUSTaskType

control = MANUSUserControl()

# Update configuration
control.update_config({
    "log_level": "DEBUG",
    "task_timeout": 600,
    "max_concurrent_tasks": 10
})

# Execute multiple tasks
results = []
results.append(control.execute_task(
    MANUSTaskType.PROVISION,
    {"resource_type": "azure_speech"}
))
results.append(control.execute_task(
    MANUSTaskType.EXECUTE,
    {"script": "scripts/my_script.py", "args": ["--verbose"]}
))

# Monitor tasks
for task in control.list_tasks():
    print(f"Task {task['id']}: {task['status']}")

# Get logs
logs = control.get_logs(limit=100)
for log in logs:
    print(f"[{log['timestamp']}] {log['level']}: {log['message']}")
```

---

## Configuration

### Default Configuration

```json
{
  "azure_key_vault": "jarvis-lumina",
  "azure_resource_group": "jarvis-lumina-rg",
  "azure_location": "eastus",
  "workspace_path": "/path/to/workspace",
  "log_level": "INFO",
  "auto_start": false,
  "task_timeout": 300,
  "max_concurrent_tasks": 5
}
```

### Configuration File Location

- **Default:** `config/manus_user_control.json`
- **Custom:** Specify via `MANUSUserControl(config_file=Path("custom/config.json"))`

---

## Task Types

### MANUSTaskType.PROVISION

Provision resources (Azure services, etc.)

```python
control.execute_task(
    MANUSTaskType.PROVISION,
    {"resource_type": "azure_speech"}
)
```

### MANUSTaskType.CONFIGURE

Update configuration

```python
control.execute_task(
    MANUSTaskType.CONFIGURE,
    {"config": {"log_level": "DEBUG"}}
)
```

### MANUSTaskType.EXECUTE

Execute scripts or commands

```python
control.execute_task(
    MANUSTaskType.EXECUTE,
    {"script": "scripts/my_script.py", "args": ["--verbose"]}
)
```

### MANUSTaskType.MONITOR

Monitor system status

```python
control.execute_task(
    MANUSTaskType.MONITOR,
    {"monitor_type": "status"}
)
```

### MANUSTaskType.STATUS

Get status information

```python
control.execute_task(
    MANUSTaskType.STATUS,
    {}
)
```

---

## NEO Browser Control

### Available Actions

- **launch** - Launch browser with URL
- **close** - Close browser
- **navigate** - Navigate to URL
- **cookies** - Get cookies for domain
- **elevenlabs_setup** - Automated ElevenLabs setup

### Examples

```python
# Launch browser
control.control_neo_browser("launch", {"url": "https://elevenlabs.io"})

# Get cookies
cookies = control.control_neo_browser("cookies", {"domain": "elevenlabs.io"})

# Automated setup
result = control.control_neo_browser("elevenlabs_setup")
if result.get("success"):
    print(f"API Key: {result['api_key']}")
```

---

## Logging & Monitoring

### View Logs

```python
# Get all logs (last 100)
logs = control.get_logs()

# Get logs by level
error_logs = control.get_logs(level="ERROR")
warning_logs = control.get_logs(level="WARNING")

# Get limited logs
recent_logs = control.get_logs(limit=50)
```

### Task Monitoring

```python
# List all tasks
tasks = control.list_tasks()

# Get specific task
task = control.get_task("task_id_here")

# Cancel task
control.cancel_task("task_id_here")
```

---

## Common Workflows

### Workflow 1: Provision Azure Speech

```bash
python scripts/python/manus_user_control_interface.py --provision azure_speech
```

### Workflow 2: Setup ElevenLabs

```bash
python scripts/python/manus_user_control_interface.py --neo-elevenlabs
```

### Workflow 3: Execute Custom Script

```bash
python scripts/python/manus_user_control_interface.py --execute "python scripts/my_script.py --arg value"
```

### Workflow 4: Monitor System

```bash
# Check status
python scripts/python/manus_user_control_interface.py --status

# View logs
python scripts/python/manus_user_control_interface.py --logs 100

# List tasks
python scripts/python/manus_user_control_interface.py --tasks
```

---

## Error Handling

### Common Errors

**Error: "MANUS-NEO integration not available"**
- Solution: Ensure `manus_neo_integration.py` is in the Python path

**Error: "Azure CLI not found"**
- Solution: Install Azure CLI and ensure it's in PATH

**Error: "Task timeout"**
- Solution: Increase `task_timeout` in configuration

**Error: "Configuration file not found"**
- Solution: Configuration will use defaults, or create the file manually

---

## Best Practices

1. **Check Status First** - Always check MANUS status before executing tasks
2. **Monitor Tasks** - Use `--tasks` to monitor running tasks
3. **Review Logs** - Check logs if tasks fail
4. **Configuration** - Store custom configuration in `config/manus_user_control.json`
5. **Error Handling** - Always check `success` field in results

---

## Integration Examples

### Example 1: Automated Resource Provisioning

```python
from manus_user_control_interface import MANUSUserControl, MANUSTaskType

control = MANUSUserControl()

# Provision Azure Speech
result = control.execute_task(
    MANUSTaskType.PROVISION,
    {"resource_type": "azure_speech"}
)

if result["success"]:
    print("✅ Azure Speech provisioned")
else:
    print(f"❌ Failed: {result.get('error')}")
```

### Example 2: Complete ElevenLabs Setup

```python
control = MANUSUserControl()

# Launch browser and setup ElevenLabs
result = control.control_neo_browser("elevenlabs_setup")

if result.get("success"):
    api_key = result["api_key"]
    print(f"✅ API Key retrieved: {api_key[:20]}...")
    
    if result.get("vault_stored"):
        print("✅ Stored in Azure Key Vault")
    else:
        print("⚠️  Manual storage required")
```

### Example 3: Batch Operations

```python
control = MANUSUserControl()

tasks = [
    {"type": MANUSTaskType.PROVISION, "data": {"resource_type": "azure_speech"}},
    {"type": MANUSTaskType.EXECUTE, "data": {"script": "scripts/test.py"}},
    {"type": MANUSTaskType.MONITOR, "data": {"monitor_type": "status"}},
]

results = []
for task in tasks:
    result = control.execute_task(task["type"], task["data"])
    results.append(result)
    print(f"{task['type'].value}: {result['success']}")
```

---

## Troubleshooting

### Issue: Commands Not Working

1. Check Python path: `python --version`
2. Check script location: Ensure you're in the workspace root
3. Check dependencies: `pip install -r requirements.txt`

### Issue: Azure Commands Failing

1. Check Azure login: `az account show`
2. Check permissions: Ensure you have access to Key Vault
3. Check resource group: Verify resource group exists

### Issue: NEO Browser Not Working

1. Check NEO installation: Verify NEO browser is installed
2. Check paths: Ensure NEO paths are correct
3. Check permissions: Ensure file system access

---

**Last Updated:** 2025-01-30  
**Version:** 1.0  
**Status:** OPERATIONAL

