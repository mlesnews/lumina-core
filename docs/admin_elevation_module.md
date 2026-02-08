# JARVIS Admin Elevation Module

## Overview

Comprehensive admin elevation utilities for Windows. Provides functions to check admin status, request elevation, and run commands with admin privileges.

## Features

- ✅ Check admin status
- ✅ Request elevation via UAC prompt
- ✅ Run PowerShell commands with admin privileges
- ✅ Service management (start, stop, set startup type)
- ✅ Registry operations
- ✅ Scheduled task creation
- ✅ Context manager for admin operations
- ✅ Automatic elevation request and exit

## Usage

### Basic Usage

```python
from scripts.python.jarvis_admin_elevation import AdminElevation, is_admin, require_admin

# Check if running as admin
if is_admin():
    print("Running as admin")
else:
    print("Not running as admin")

# Request elevation
AdminElevation.request_elevation()

# Run PowerShell command as admin
result = AdminElevation.run_powershell_as_admin("Get-Service -Name 'ArmouryCrateService'")
```

### Service Management

```python
from scripts.python.jarvis_admin_elevation import AdminElevation

# Set service startup type
AdminElevation.set_service_startup_type("ArmouryCrateService", "Manual")

# Start service
AdminElevation.start_service("ArmouryCrateService")

# Stop service
AdminElevation.stop_service("ArmouryCrateService")
```

### Registry Operations

```python
from scripts.python.jarvis_admin_elevation import AdminElevation

# Set registry value
AdminElevation.set_registry_value(
    "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
    "MyApp",
    "C:\\Path\\To\\App.exe",
    "String"
)
```

### Scheduled Tasks

```python
from scripts.python.jarvis_admin_elevation import AdminElevation

# Create scheduled task
AdminElevation.create_scheduled_task(
    task_name="MyTask",
    command="python",
    arguments="C:\\script.py",
    trigger="AtLogon"
)

# Create recurring task (every 5 minutes)
AdminElevation.create_scheduled_task(
    task_name="MyRecurringTask",
    command="python",
    arguments="C:\\script.py",
    interval=5
)
```

### Context Manager

```python
from scripts.python.jarvis_admin_elevation import require_admin

# Use context manager for admin operations
with require_admin("service management"):
    # Code that requires admin
    AdminElevation.start_service("MyService")
```

### Automatic Elevation

```python
from scripts.python.jarvis_admin_elevation import ensure_admin_or_exit
from pathlib import Path

# Ensure admin or request elevation and exit
ensure_admin_or_exit(
    script_path=Path(__file__).resolve(),
    message="Admin privileges required for this operation"
)

# If we get here, we have admin privileges
print("Running with admin privileges")
```

## API Reference

### AdminElevation Class

#### Static Methods

**`is_admin() -> bool`**
- Check if current process is running with admin privileges
- Returns: True if admin, False otherwise

**`request_elevation(script_path: Optional[Path] = None, args: Optional[List[str]] = None) -> bool`**
- Request admin elevation via UAC prompt
- Returns: True if elevation was requested, False if already admin

**`run_powershell_as_admin(command: str, timeout: int = 30) -> Dict[str, Any]`**
- Run PowerShell command with admin privileges
- Returns: Dict with success, stdout, stderr, returncode, admin

**`run_command_as_admin(command: List[str], timeout: int = 30) -> Dict[str, Any]`**
- Run command with admin privileges using runas
- Returns: Dict with success, stdout, stderr, returncode, admin

**`set_service_startup_type(service_name: str, startup_type: str = "Manual") -> Dict[str, Any]`**
- Set Windows service startup type (requires admin)
- startup_type: "Automatic", "Manual", or "Disabled"
- Returns: Dict with success status

**`start_service(service_name: str) -> Dict[str, Any]`**
- Start Windows service (requires admin)
- Returns: Dict with success status

**`stop_service(service_name: str) -> Dict[str, Any]`**
- Stop Windows service (requires admin)
- Returns: Dict with success status

**`set_registry_value(registry_path: str, name: str, value: Any, value_type: str = "String") -> Dict[str, Any]`**
- Set registry value (requires admin)
- value_type: "String", "DWord", "QWord", etc.
- Returns: Dict with success status

**`create_scheduled_task(task_name: str, command: str, arguments: str = "", trigger: str = "AtLogon", interval: Optional[int] = None) -> Dict[str, Any]`**
- Create Windows scheduled task (requires admin)
- trigger: "AtLogon", "Daily", "Weekly", etc.
- interval: Interval in minutes (for recurring tasks)
- Returns: Dict with success status

**`require_admin(context: str = "operation")`**
- Context manager that ensures admin privileges
- Usage: `with AdminElevation.require_admin("service management"): ...`

**`ensure_admin_or_exit(script_path: Optional[Path] = None, message: Optional[str] = None) -> None`**
- Ensure admin privileges or request elevation and exit
- If not admin, requests elevation and exits current process

### Convenience Functions

**`is_admin() -> bool`**
- Check if running as admin

**`require_admin(context: str = "operation")`**
- Context manager for admin operations

**`ensure_admin_or_exit(script_path: Optional[Path] = None, message: Optional[str] = None) -> None`**
- Ensure admin or request elevation and exit

**`run_powershell_as_admin(command: str, timeout: int = 30) -> Dict[str, Any]`**
- Run PowerShell command as admin

**`set_service_startup_type(service_name: str, startup_type: str = "Manual") -> Dict[str, Any]`**
- Set service startup type

**`start_service(service_name: str) -> Dict[str, Any]`**
- Start service

**`stop_service(service_name: str) -> Dict[str, Any]`**
- Stop service

## Examples

### Example 1: Service Management Script

```python
#!/usr/bin/env python3
from scripts.python.jarvis_admin_elevation import AdminElevation, ensure_admin_or_exit
from pathlib import Path

# Ensure admin
ensure_admin_or_exit(Path(__file__).resolve())

# Manage services
AdminElevation.set_service_startup_type("MyService", "Manual")
AdminElevation.start_service("MyService")
```

### Example 2: Registry Modification

```python
from scripts.python.jarvis_admin_elevation import AdminElevation

# Set registry value
result = AdminElevation.set_registry_value(
    "HKLM:\\SOFTWARE\\MyApp",
    "Setting",
    "Value",
    "String"
)

if result["success"]:
    print("Registry value set successfully")
```

### Example 3: Scheduled Task Creation

```python
from scripts.python.jarvis_admin_elevation import AdminElevation

# Create task that runs on login
result = AdminElevation.create_scheduled_task(
    task_name="MyStartupTask",
    command="python",
    arguments="C:\\Scripts\\startup.py",
    trigger="AtLogon"
)

# Create recurring task (every 5 minutes)
result = AdminElevation.create_scheduled_task(
    task_name="MyRecurringTask",
    command="python",
    arguments="C:\\Scripts\\monitor.py",
    interval=5
)
```

### Example 4: Context Manager

```python
from scripts.python.jarvis_admin_elevation import require_admin

# Use context manager
with require_admin("service management") as has_admin:
    if has_admin:
        # Perform admin operations
        AdminElevation.start_service("MyService")
    else:
        print("Admin privileges not available")
```

## Integration

### With Smart Lighting System

```python
from scripts.python.jarvis_smart_lighting_with_admin import SmartLightingWithAdmin
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sync = SmartLightingWithAdmin(project_root)
result = sync.setup_smart_lighting()  # Automatically requests admin if needed
```

## Notes

- **UAC Prompts**: Requesting elevation will show a UAC prompt to the user
- **Service Management**: Requires admin privileges to modify service startup types
- **Registry Operations**: HKLM registry modifications require admin privileges
- **Scheduled Tasks**: Creating system-level scheduled tasks requires admin privileges
- **Error Handling**: All methods return Dict with success status and error information
- **Logging**: All operations are logged for debugging

## Troubleshooting

### "Access is denied" errors
- Ensure script is running with admin privileges
- Use `ensure_admin_or_exit()` to automatically request elevation

### UAC prompt not appearing
- Check UAC settings in Windows
- Verify script is not already running as admin

### Services not starting
- Check service dependencies
- Verify service exists and is not disabled
- Check Windows Event Viewer for service errors

### Registry operations failing
- Verify registry path is correct
- Check if registry key exists
- Ensure proper value type is specified

## Files

- **`scripts/python/jarvis_admin_elevation.py`**: Main admin elevation module
- **`scripts/python/jarvis_smart_lighting_with_admin.py`**: Example integration
- **`docs/admin_elevation_module.md`**: This documentation
