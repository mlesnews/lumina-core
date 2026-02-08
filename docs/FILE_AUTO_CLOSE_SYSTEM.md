# File Auto-Close System

## Overview

The File Auto-Close System automatically closes files in Cursor/VSCode after 30 minutes unless they are pinned, using intelligent @V3 and @JARVIS decisioning to determine when files should remain open.

## Problem Solved

**Before**: Files remain open indefinitely, cluttering the workspace and consuming memory.

**After**: Intelligent automatic file management that:
- Closes unused files after 30 minutes
- Allows pinning important files to prevent auto-close
- Uses AI decisioning to evaluate file importance
- Provides manual control and status monitoring

## Architecture

### 1. File Auto-Close Manager (`file_auto_close_manager.py`)

**Core Python System:**
- Tracks all open files with timestamps and metadata
- Manages pinning/unpinning of files
- Implements V3 + JARVIS decision algorithms
- Provides CLI interface for management

**Key Features:**
- 30-minute auto-close timer (configurable)
- File session persistence across restarts
- Comprehensive logging and error handling
- Background monitoring capabilities

### 2. File Pin Manager (`file_pin_manager.py`)

**CLI Interface:**
- `pin <file> [--reason "reason"]` - Pin a file
- `unpin <file>` - Unpin a file
- `list` - Show all pinned files
- `status [file]` - Show pin status

### 3. VSCode Extension (`vscode-extensions/file-auto-close/`)

**Extension Features:**
- Native VSCode integration for file closing
- Context menu options for pinning/unpinning
- Real-time file monitoring
- Configuration through VSCode settings

**Commands:**
- `Lumina: Pin File` - Pin current file
- `Lumina: Unpin File` - Unpin current file
- `Lumina: Close File` - Manually close file
- `Lumina: Show Status` - Display system status
- `Lumina: Evaluate File` - Run V3+JARVIS evaluation

## Decision Engine

### V3 Decisioning
**Factors Considered:**
- File age (older = more likely to close)
- Idle time (longer idle = more likely to close)
- File type importance (source files = less likely to close)
- Location context (src/ vs docs/ vs tests/)
- File size and modification status

**Algorithm:**
```python
score = 0
if age_minutes > 60: score += 0.4
if idle_minutes > 30: score += 0.3
if file_type in ['python', 'js', 'ts']: score -= 0.2
if in_src_directory: score -= 0.1
should_close = score >= threshold  # 0.7 default
```

### JARVIS Override
**Critical Indicators (Prevent Close):**
- File currently being edited
- File has unsaved changes
- File is a dependency of open files
- File contains active TODO/FIXME comments

**Auto-Close Indicators (Force Close):**
- File open for more than 2 hours
- File is temporary/cache/backup
- File is very old and idle

## Usage

### 1. Automatic Operation
The system runs automatically in the background:
- Monitors all open files
- Checks every 60 seconds (configurable)
- Auto-closes eligible files after 30 minutes
- Shows notifications when closing files

### 2. Manual Control

**VSCode Tasks:**
- `File Auto-Close: Status` - View current status
- `File Auto-Close: Report` - Generate detailed report
- `File Auto-Close: Process Now` - Force immediate check
- `File Auto-Close: Monitor (Background)` - Start monitoring

**VSCode Extension:**
- Right-click file → "Lumina: Pin File"
- Editor title menu → "Lumina: Evaluate File"
- Command Palette → "Lumina: Show Status"

### 3. CLI Management
```bash
# Pin a file
python scripts/python/file_pin_manager.py pin "path/to/file.py" --reason "Working on this"

# Check status
python scripts/python/file_pin_manager.py status

# List pinned files
python scripts/python/file_pin_manager.py list
```

## Configuration

### VSCode Settings
```json
{
  "luminaFileAutoClose.enabled": true,
  "luminaFileAutoClose.autoCloseMinutes": 30,
  "luminaFileAutoClose.checkIntervalSeconds": 60,
  "luminaFileAutoClose.jarvisOverrideEnabled": true,
  "luminaFileAutoClose.v3ConfidenceThreshold": 0.7,
  "luminaFileAutoClose.showNotifications": true
}
```

### System Configuration
The system also respects configuration in `config/task_error_manager_config.yaml` for integration with other JARVIS systems.

## File Session Data

### Storage Location
- `data/file_management/active_files.json` - Current file sessions
- `data/file_management/pinned_files.json` - Pinned file list

### Session Metadata
Each file session tracks:
- File path and workspace
- Open and last access timestamps
- Pin status and reason
- File type and importance score
- Decision context and history

## Integration with JARVIS Ecosystem

### @V3 Integration
- Uses V3 confidence scoring for initial evaluation
- Considers file metadata and workspace context
- Provides structured decision context

### @JARVIS Override
- Applies sophisticated heuristics for override decisions
- Considers editing state and dependencies
- Provides human-readable reasoning

### Troubleshooting Integration
- Files with active TODO/FIXME are protected
- Dependency analysis prevents closing related files
- Context-aware decision making

## Benefits

### 1. Workspace Management
- Prevents workspace clutter
- Maintains focus on active files
- Automatic cleanup of unused files

### 2. Resource Efficiency
- Reduces memory usage from open files
- Improves IDE performance
- Prevents editor tab overflow

### 3. Intelligent Decisions
- Learns from file usage patterns
- Considers file importance and context
- Provides manual override capabilities

### 4. Seamless Integration
- Works with existing VSCode workflows
- Integrates with JARVIS ecosystem
- Provides comprehensive monitoring

## Safety Features

### Protection Mechanisms
- Pinned files are never auto-closed
- Files with unsaved changes are protected
- Currently edited files remain open
- Critical files (dependencies) are preserved

### Recovery Options
- Files can be manually reopened
- Pinning prevents future auto-close
- Status monitoring shows all decisions
- Comprehensive logging for troubleshooting

## Monitoring & Maintenance

### Status Monitoring
```bash
python scripts/python/file_auto_close_manager.py status
```

**Output:**
```
Active Files: 12, Pinned: 3, Recently Closed: 5
Auto-close after: 30 minutes
```

### Detailed Reporting
```bash
python scripts/python/file_auto_close_manager.py report
```

Generates markdown report with:
- Active file sessions
- Pin status and reasons
- Age and idle time statistics
- Decision history

### Performance Metrics
- Files processed per cycle
- Close success rate
- Decision accuracy tracking
- Memory usage monitoring

## Extension Installation

### 1. Compile Extension
```bash
cd vscode-extensions/file-auto-close
npm install
npm run compile
```

### 2. Install Extension
- Open VSCode
- Run "Extensions: Install from VSIX"
- Select `lumina-file-auto-close-1.0.0.vsix`

### 3. Alternative: Development Mode
```bash
cd vscode-extensions/file-auto-close
npm run watch
# Then use "Extensions: Install Extension from Location"
```

## Troubleshooting

### Common Issues

**Files Not Auto-Closing:**
- Check if files are pinned
- Verify extension is enabled
- Check VSCode settings configuration

**Extension Not Loading:**
- Ensure TypeScript compilation succeeded
- Check VSCode version compatibility
- Review extension logs

**Decision Errors:**
- Check JARVIS override settings
- Review V3 confidence threshold
- Examine file session metadata

### Debug Mode
Enable detailed logging:
```bash
# Check extension logs in VSCode developer console
# View file session data in data/file_management/
# Use CLI status commands for real-time monitoring
```

## Future Enhancements

### Planned Features
- **Machine Learning**: Learn from user behavior patterns
- **Cross-Workspace Sync**: Share pin status across machines
- **Advanced Dependencies**: Deep dependency analysis
- **Performance Metrics**: Detailed usage analytics
- **Custom Rules**: User-defined close rules

### Integration Points
- Git integration (close files not in current branch)
- Project context awareness
- Team collaboration features
- External tool integration

## Summary

The File Auto-Close System transforms file management from manual chore to intelligent automation. By combining V3 decisioning with JARVIS override capabilities, it provides a sophisticated yet user-friendly solution for maintaining clean, efficient workspaces while preserving access to important files.

The system seamlessly integrates with the existing JARVIS ecosystem, providing both automated operation and comprehensive manual control for optimal workspace management.



