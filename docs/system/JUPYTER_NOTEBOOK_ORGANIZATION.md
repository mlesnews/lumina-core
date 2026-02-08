# Jupyter Notebook Organization Strategy

**Date**: 2025-01-24
**Decision Status**: APPROVED by @AIQ
**Decision ID**: `jupyter_notebook_location_20250124`

## Decision Summary

**Location**: `D:\Dropbox\my_projects\data\jupyter/`

**Decision**: Store Jupyter notebooks in project directory structure
**Recommendation**: @AIQ System
**Confidence**: 0.92 (HIGH)
**Status**: ✅ Implemented

## Rationale

### Why Project Directory?

1. **Resource-Aware Integration**: Seamless access to memory, R5, holocron modules
2. **Automatic Library Access**: `scripts/python/` automatically in Python path
3. **Development Workflow**: Notebooks close to code being analyzed
4. **Team Collaboration**: Shared via project repository
5. **Dropbox Sync**: Automatic multi-device access
6. **Project Context**: Access to configs, data, docs automatically

### Score: 9.2/10

## Configuration

### Directory Structure

```
D:\Dropbox\my_projects\
├── data/
│   └── jupyter/              # Notebooks stored here
│       ├── Resource_Aware_System_Integration.ipynb
│       ├── R5_Living_Context_Matrix.ipynb
│       └── ...
├── scripts/
│   └── python/               # Library modules (automatically in path)
│       ├── memory_manager.py
│       ├── resource_aware_context.py
│       ├── holocron_query.py
│       └── r5_living_context_matrix.py
└── config/
    └── jupyter/
        └── nas_config.json   # Jupyter configuration
```

### Jupyter Configuration

**Config File**: `C:\Users\mlesn\.jupyter\jupyter_labconfig.py`

Key settings:
- Notebook directory: `D:\Dropbox\my_projects\data\jupyter`
- Python path automatically includes:
  - `D:\Dropbox\my_projects`
  - `D:\Dropbox\my_projects\scripts`
  - `D:\Dropbox\my_projects\scripts\python`

### Access

- **Local**: http://localhost:8888
- **NAS**: http://10.17.17.32:8888

## Version Control Strategy

### Git Configuration

The `.gitignore` is configured to:
- ✅ **Track**: Notebook files (`.ipynb`)
- ❌ **Exclude**: Checkpoints (`.ipynb_checkpoints/`)
- ❌ **Exclude**: Cache (`.jupyter/`)
- ❌ **Exclude**: Large outputs (optional, if needed)

### Best Practices

1. **Small Notebooks**: Track in git for collaboration
2. **Large Notebooks**: Use git-lfs if needed
3. **Outputs**: Exclude large outputs (images, data files) from git
4. **Checkpoints**: Always excluded (auto-generated)

## Resource-Aware Integration

### Automatic Access

All notebooks automatically have access to:

```python
# These imports work automatically:
from memory_manager import MemoryManager, MemoryType, get_memory_manager
from resource_aware_context import ResourceAwareContextChecker, should_use_ai
from holocron_query import HolocronQueryEngine
from r5_living_context_matrix import R5LivingContextMatrix
```

### Example Usage

See sample notebook: `data/jupyter/Resource_Aware_System_Integration.ipynb`

## Backup Strategy

### Primary Backup
- **Dropbox Sync**: Automatic backup via Dropbox
- **Multi-Device**: Syncs across all devices
- **Version History**: Dropbox keeps version history

### Secondary Backup
- **Project Backup**: Included in project backup strategy
- **NAS Backup**: Can include notebooks in NAS backup (via project)

## Alternatives Considered

### Option 2: NAS Direct Storage
- **Score**: 6.6/10
- **Rejected**: Poor resource-aware integration, network dependency

### Option 3: Separate Directory
- **Score**: 6.4/10
- **Rejected**: Integration complexity, disconnected workflow

## Maintenance

### Regular Tasks
- Monitor notebook directory size
- Clean up old notebooks if needed
- Review `.gitignore` for large outputs
- Ensure resource-aware modules are accessible

### Troubleshooting

**Issue**: Can't import modules
**Solution**: Check Python path in Jupyter config

**Issue**: Notebooks too large for git
**Solution**: Use git-lfs or exclude large outputs

**Issue**: Network access issues
**Solution**: Use local path (localhost:8888)

## Decision Log

Full decision analysis: `data/aiq_decisions/jupyter_notebook_location_decision_20250124.json`

---

**Status**: ✅ APPROVED and IMPLEMENTED
**Next Review**: As needed
**Owner**: @AIQ System

