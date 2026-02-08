# Shell Selection Guide: PowerShell vs Bash/Korn

## Overview
Guidance on when to use PowerShell vs Bash/Korn shell for different tasks in the LUMINA project.

## Current Environment
- **OS**: Windows 10/11
- **Primary Shell**: PowerShell (recommended for Windows)
- **Alternative**: Bash/Korn (via WSL or Git Bash)

## When to Use PowerShell

### ✅ Use PowerShell For:

1. **Windows-Specific Operations**
   - Windows service management
   - Windows registry access
   - Windows event logs
   - Windows-specific file operations
   - Windows path handling

2. **Native Windows Integration**
   - .NET integration
   - COM objects
   - Windows Management Instrumentation (WMI)
   - Active Directory operations

3. **Project-Specific Scripts**
   - LUMINA project scripts (most are PowerShell)
   - Windows startup scripts
   - Windows automation scripts

4. **AI Assistant Commands**
   - AI-executed commands (default to PowerShell)
   - Terminal commands in Cursor IDE
   - Automated workflows

5. **Venv Management**
   - Venv activation (PowerShell profile handles this)
   - Python environment setup
   - Package management

### Example PowerShell Use Cases:
```powershell
# Windows service management
Get-Service | Where-Object {$_.Status -eq "Running"}

# File operations with Windows paths
Get-ChildItem -Path "C:\Users\mlesn\Dropbox\my_projects\.lumina" -Recurse

# Venv activation
. venv\Scripts\Activate.ps1

# Project scripts
python scripts/python/your_script.py
```

## When to Use Bash/Korn

### ✅ Use Bash/Korn For:

1. **Cross-Platform Scripts**
   - Scripts that need to run on Linux/Mac
   - Docker container operations
   - CI/CD pipelines (often Linux-based)

2. **Unix-Style Operations**
   - Unix command-line tools (grep, awk, sed)
   - Unix-style path handling
   - Shell scripting with Unix conventions

3. **WSL Operations**
   - WSL (Windows Subsystem for Linux) interactions
   - Linux-specific operations
   - Docker operations (often Linux-based)

4. **Git Operations**
   - Git Bash for Git-specific workflows
   - Unix-style Git commands
   - Cross-platform Git scripts

5. **Legacy Scripts**
   - Existing bash/korn scripts
   - Scripts from Linux/Mac environments

### Example Bash/Korn Use Cases:
```bash
# Unix-style operations
grep -r "pattern" scripts/

# Docker operations
docker-compose up -d

# WSL operations
wsl ls -la

# Git operations (Git Bash)
git status
```

## Decision Matrix

| Task Type | Recommended Shell | Reason |
|-----------|------------------|--------|
| Windows automation | PowerShell | Native Windows integration |
| Python scripts | PowerShell | Venv activation, Windows paths |
| AI commands | PowerShell | Default, venv support |
| Docker operations | Bash/Korn | Often Linux-based |
| Cross-platform scripts | Bash/Korn | Unix compatibility |
| Git operations | Either | Both work, Git Bash preferred |
| WSL operations | Bash/Korn | Linux environment |
| Windows services | PowerShell | Native Windows |
| File operations (Windows) | PowerShell | Windows path handling |
| File operations (Unix-style) | Bash/Korn | Unix conventions |

## Best Practices

### 1. Default to PowerShell
- **Primary choice** for Windows development
- Better Windows integration
- Venv support built-in
- Project scripts are PowerShell

### 2. Use Bash/Korn When:
- Working with Docker/Linux containers
- Need Unix-style tools
- Cross-platform compatibility required
- WSL operations

### 3. Consistency
- **AI commands**: Always use PowerShell (unless specifically needed otherwise)
- **Project scripts**: PowerShell (already established)
- **Docker/WSL**: Bash/Korn (Linux environment)

### 4. Path Handling
- **PowerShell**: Use Windows paths (`C:\Users\...`)
- **Bash/Korn**: Use Unix-style paths (`/c/Users/...` or WSL paths)

## Current Project Status

### PowerShell (Primary)
- ✅ PowerShell profile configured
- ✅ Venv auto-activation
- ✅ Windows integration
- ✅ AI command execution
- ✅ Project scripts

### Bash/Korn (Secondary)
- ⚠️ Available via WSL/Git Bash
- ⚠️ Use for Docker/Linux operations
- ⚠️ Cross-platform scripts

## Recommendations for @op

1. **Default to PowerShell** for all Windows operations
2. **Use Bash/Korn** only when:
   - Working with Docker/Linux
   - Cross-platform scripts needed
   - Unix tools required
3. **AI commands**: Always PowerShell (venv support)
4. **Project scripts**: PowerShell (consistency)

## Migration Notes

If you have bash/korn scripts:
- Keep them for cross-platform use
- Consider PowerShell equivalents for Windows-only operations
- Document which shell is required

## Troubleshooting

### PowerShell Issues
- Check execution policy: `Get-ExecutionPolicy`
- Check venv activation: `$env:VIRTUAL_ENV`
- Check profile: `Test-Path $PROFILE`

### Bash/Korn Issues
- Check WSL: `wsl --status`
- Check Git Bash: Available in Git for Windows
- Path conversions: Use `wslpath` for conversions
