# Multi-Environment Session Resumption

## Overview

The multi-environment session resumption system processes incomplete agent chat sessions across all workspace environments with dynamic resource balancing and memory monitoring.

## Features

- **Multi-Environment Support**: Automatically discovers and processes sessions from all workspace environments
- **Centralized Tracking**: All resumed sessions are tracked in `.lumina/data/resumed_sessions/` to avoid duplicates
- **Memory Monitoring**: Tracks both CPU and memory usage, dynamically adjusting batch sizes
- **Dynamic Scaling**: Automatically adjusts batch sizes and delays based on system load
- **Continuous Mode**: Can run continuously until all sessions are processed
- **Slow Mode**: Processes sessions slowly over time for background operation

## Discovered Environments

The system automatically discovers environments by looking for directories with `data/r5_living_matrix/sessions/`:

- `.lumina` - Primary workspace
- `cedarbrook-financial-services_llc-env` - CFS workspace
- `cedarbrook-financial-services_llc-env_portable` - Portable CFS workspace
- `cfs-llc-env` - CFS workspace variant
- Any other directories with session data

## Usage

### Basic Usage (Single Run)

```bash
python scripts/python/resume_sessions_multi_env.py --max-sessions 20
```

### Slow Background Processing

```bash
python scripts/python/resume_sessions_multi_env.py --max-sessions 20 --slow-mode
```

### Continuous Mode (Process All Over Time)

```bash
python scripts/python/resume_sessions_multi_env.py --max-sessions 20 --slow-mode --continuous
```

### Custom Resource Limits

```bash
python scripts/python/resume_sessions_multi_env.py \
  --max-sessions 20 \
  --slow-mode \
  --continuous \
  --target-memory 70 \
  --max-memory 85 \
  --target-cpu 60 \
  --max-cpu 75
```

## Options

- `--max-sessions N`: Maximum sessions to process per run (default: None = all)
- `--slow-mode`: Enable slow mode (longer delays between batches)
- `--continuous`: Run continuously until all sessions are processed
- `--target-memory N`: Target memory percentage (default: 70)
- `--max-memory N`: Maximum memory percentage before throttling (default: 85)
- `--target-cpu N`: Target CPU percentage (default: 60)
- `--max-cpu N`: Maximum CPU percentage before throttling (default: 75)
- `--recent-only`: Only process recent sessions (skip older ones)
- `--projects-root PATH`: Root directory for all projects (default: ~/Dropbox/my_projects)

## How It Works

1. **Discovery**: Scans all directories in the projects root for `data/r5_living_matrix/sessions/`
2. **Tracking**: Loads all already-resumed session IDs from centralized location
3. **Filtering**: Finds incomplete sessions (< 3 messages) excluding already-resumed ones
4. **Batching**: Groups sessions into batches with dynamic sizing based on system load
5. **Processing**: Processes batches with resource monitoring and automatic throttling
6. **Centralization**: Saves all resumed sessions to `.lumina/data/resumed_sessions/`

## Resource Management

- **CPU Monitoring**: Tracks CPU usage and adjusts batch sizes
- **Memory Monitoring**: Tracks memory usage (more critical, extra conservative)
- **Spike Prediction**: Predicts resource spikes and pauses proactively
- **Dynamic Delays**: Adjusts delays between batches based on current load
- **Automatic Throttling**: Pauses when resources exceed limits

## Session Identification

Sessions are identified by their `session_id` field or filename. The system:
- Tracks resumed sessions by ID to prevent duplicates
- Records the original environment for each resumed session
- Processes sessions chronologically (oldest first)

## Background Processing

For long-running background processing:

```bash
# Start in background (Windows)
Start-Process python -ArgumentList "scripts\python\resume_sessions_multi_env.py --max-sessions 20 --slow-mode --continuous --target-memory 70 --max-memory 85" -WindowStyle Hidden

# Or use task scheduler / cron for scheduled runs
```

## Current Status

As of last run:
- **Total incomplete sessions**: 324 across all environments
- **Processed**: 20 sessions
- **Remaining**: ~304 sessions
- **Environments**: fvh (308), scripts (16), .lumina (0)

## Future Enhancements

- NAS centralization: All agent history should eventually be centralized on NAS
- Cross-environment deduplication: Better handling of duplicate sessions across environments
- Priority-based processing: Process important sessions first
- Progress persistence: Resume processing after interruption

