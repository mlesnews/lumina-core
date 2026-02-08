# 🔍 JARVIS Diagnostic Module Overview

## Module Structure

The diagnostic module (`src/cfservices/services/jarvis_core/diagnostics.py`) provides universal diagnostic and troubleshooting capabilities for JARVIS.

### Core Components

#### 1. **Data Classes**

- **`DiagnosticResult`**: Result of a diagnostic check
  - `success: bool` - Whether the check succeeded
  - `data: Dict[str, Any]` - Diagnostic data
  - `message: str` - Human-readable message
  - `errors: List[str]` - List of errors encountered
  - `warnings: List[str]` - List of warnings

- **`TroubleshootingResult`**: Result of troubleshooting analysis
  - `success: bool` - Whether troubleshooting succeeded
  - `issues: List[str]` - List of issues found
  - `recommendations: List[str]` - List of recommendations
  - `actions_taken: List[Dict[str, Any]]` - Actions executed
  - `diagnostics: Dict[str, Any]` - Full diagnostic data
  - `message: str` - Summary message

#### 2. **Spy Classes** (Abstract Base: `DiagnosticSpy`)

All spy classes inherit from `DiagnosticSpy` and implement the `spy()` method.

##### **`WindowsKeyboardSpy`**
🔍 Detects keyboard lock states
- **Capabilities:**
  - Num Lock state (ON/OFF)
  - Caps Lock state (ON/OFF)
  - Scroll Lock state (ON/OFF)
  - FN Lock state (UNKNOWN - not directly detectable)
- **Methods:**
  - Uses Windows API `GetKeyState()`
  - PowerShell verification
- **Usage:**
```python
spy = WindowsKeyboardSpy()
result = await spy.spy(target="keyboard_locks")
# Returns: DiagnosticResult with lock_states data
```

##### **`WindowsServiceSpy`**
🔍 Detects Windows service states
- **Capabilities:**
  - Service status (Found/Not Found/Error)
  - Service details (Name, Status, StartType)
- **Methods:**
  - PowerShell `Get-Service` command
- **Usage:**
```python
spy = WindowsServiceSpy()
result = await spy.spy(
    target="services",
    service_names=["ArmouryCrateService", "ROGLiveService"]
)
# Returns: DiagnosticResult with services data
```

##### **`WindowsProcessSpy`**
🔍 Detects Windows process states
- **Capabilities:**
  - Process status (Running/Not Running/Error)
  - Process details (ProcessName, Id, Path)
- **Methods:**
  - PowerShell `Get-Process` command
- **Usage:**
```python
spy = WindowsProcessSpy()
result = await spy.spy(
    target="processes",
    process_names=["ArmouryCrateControlInterface", "ArmouryCrate"]
)
# Returns: DiagnosticResult with processes data
```

#### 3. **Troubleshooter Class**

🔧 Universal troubleshooting and decision-making engine

**Features:**
- Gathers information using spy functions
- Analyzes issues using custom analyzers
- Generates recommendations
- Executes fixes using fixer functions
- **Research & Escalation** (if enabled):
  - Conducts external research for complex issues
  - Escalates issues that need deeper investigation
  - Synthesizes research findings into recommendations

**Initialization:**
```python
troubleshooter = Troubleshooter(
    logger=logger,
    spies=[keyboard_spy, service_spy, process_spy],
    analyzers=[custom_analyzer],
    fixers={"toggle_lock": toggle_lock_fixer},
    enable_research=True  # Enable research and escalation
)
```

**Usage:**
```python
result = await troubleshooter.troubleshoot(
    spy_targets=["keyboard_locks", "services", "processes"],
    auto_fix=True
)
# Returns: TroubleshootingResult
```

#### 4. **Factory Functions**

##### **`create_keyboard_troubleshooter()`**
Creates a pre-configured troubleshooter for keyboard control issues.

**Features:**
- Pre-configured with `WindowsKeyboardSpy`, `WindowsServiceSpy`, `WindowsProcessSpy`
- Includes keyboard-specific analyzer
- Ready to use for keyboard troubleshooting

**Usage:**
```python
troubleshooter = create_keyboard_troubleshooter(
    logger=logger,
    service_names=["ArmouryCrateService"],
    process_names=["ArmouryCrateControlInterface"],
    fixers={"toggle_lock": toggle_lock_fixer}
)
```

## Integration with Research Module

The diagnostic module integrates with the **Research Module** (`src/cfservices/services/jarvis_core/research.py`) for:

1. **External Research**: Web search, documentation lookup, forum search
2. **Escalation**: Automatic escalation for complex issues
3. **Synthesis**: Converting research findings into actionable recommendations

**Research Flow:**
```
Issue Detected → Escalation Check → Research Conducted → Findings Synthesized → Recommendations Added
```

## Usage Examples

### Example 1: Check Keyboard Locks
```python
from src.cfservices.services.jarvis_core.diagnostics import WindowsKeyboardSpy

spy = WindowsKeyboardSpy()
result = await spy.spy(target="keyboard_locks")

if result.success:
    lock_states = result.data["lock_states"]
    print(f"Num Lock: {lock_states['num_lock']['state']}")
    print(f"Caps Lock: {lock_states['caps_lock']['state']}")
```

### Example 2: Full Troubleshooting
```python
from src.cfservices.services.jarvis_core.diagnostics import (
    WindowsKeyboardSpy,
    WindowsServiceSpy,
    WindowsProcessSpy,
    Troubleshooter
)

# Create spies
keyboard_spy = WindowsKeyboardSpy()
service_spy = WindowsServiceSpy()
process_spy = WindowsProcessSpy()

# Create troubleshooter
troubleshooter = Troubleshooter(
    spies=[keyboard_spy, service_spy, process_spy],
    enable_research=True
)

# Run troubleshooting
result = await troubleshooter.troubleshoot(
    spy_targets=["keyboard_locks", "services", "processes"],
    auto_fix=False
)

# Review results
print(f"Issues: {result.issues}")
print(f"Recommendations: {result.recommendations}")
```

### Example 3: Using Factory Function
```python
from src.cfservices.services.jarvis_core.diagnostics import create_keyboard_troubleshooter

troubleshooter = create_keyboard_troubleshooter(
    service_names=["ArmouryCrateService"],
    process_names=["ArmouryCrateControlInterface"]
)

result = await troubleshooter.troubleshoot(auto_fix=True)
```

## Integration Points

### Armoury Crate Integration
The diagnostic module is integrated into `ArmouryCrateIntegration`:

- **`_spy_keyboard_lock_states()`**: Uses `WindowsKeyboardSpy`
- **`_spy_armoury_crate_state()`**: Uses `WindowsServiceSpy` and `WindowsProcessSpy`
- **`_troubleshoot_keyboard_control()`**: Uses all spies + research engine

### Research Integration
When research is enabled:
- Complex issues trigger automatic research
- Research findings are synthesized into recommendations
- Escalation decisions are made based on confidence scores

## Extension Points

### Custom Spy Classes
```python
class CustomSpy(DiagnosticSpy):
    async def spy(self, target: str, **kwargs) -> DiagnosticResult:
        # Your spy logic here
        return DiagnosticResult(
            success=True,
            data={"custom": "data"},
            message="Custom spy result"
        )
```

### Custom Analyzers
```python
def custom_analyzer(diagnostics: Dict[str, Any]) -> List[str]:
    issues = []
    # Analyze diagnostics and return issues
    return issues

troubleshooter = Troubleshooter(
    analyzers=[custom_analyzer]
)
```

### Custom Fixers
```python
async def custom_fixer(issue: str) -> Dict[str, Any]:
    # Fix logic here
    return {"success": True, "message": "Fixed"}

troubleshooter = Troubleshooter(
    fixers={"custom_issue": custom_fixer}
)
```

## Best Practices

1. **Use Factory Functions**: Use `create_keyboard_troubleshooter()` for common use cases
2. **Enable Research**: Set `enable_research=True` for complex troubleshooting
3. **Custom Analyzers**: Create domain-specific analyzers for better issue detection
4. **Error Handling**: Always check `result.success` before using data
5. **Logging**: Use logger for debugging and monitoring

## Related Modules

- **`research.py`**: Research and escalation engine
- **`armoury_crate.py`**: Integration using diagnostics
- **`diagnostics.py`**: This module

## Tags

`#diagnostic` `#module` `#spy` `#troubleshooting` `#decisioning` `@jarvis`
