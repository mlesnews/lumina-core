# KAIJU IRON LEGION - Actual Model File Names Reference

## 🎯 Purpose

This document shows the **actual file names** for Ollama LLM models used in KAIJU IRON LEGION, so you can easily identify model types by their file names.

## 📂 Ollama Model Storage Structure

### File System Layout
```
~/.ollama/models/
├── blobs/                    # Actual model files (by SHA256 digest)
│   ├── sha256-{digest}       # Raw model binary files
│   └── ...
└── manifests/                # Model tags/names mapping
    ├── {model_name}          # JSON manifest pointing to blobs
    └── ...
```

### How Ollama Stores Models

1. **Blobs Directory**: Contains actual model binary files
   - File name: SHA256 digest of the file content
   - Example: `sha256-dde5aa3fc5ffc17176b5e8bdc82f587b24b2678c6c66101bf7da77af9f7ccdff`
   - These are the actual LLM model files

2. **Manifests Directory**: Contains model name mappings
   - File name: Model tag (e.g., `llama3.2:3b`)
   - Contains JSON pointing to blob files
   - This is what you reference in code/config

## 🔍 How to Identify Model Files

### Method 1: Using the Script

```bash
# Show all models with actual file names
python scripts/python/show_ollama_model_files.py report

# Show filesystem structure
python scripts/python/show_ollama_model_files.py files

# Simple list
python scripts/python/show_ollama_model_files.py list
```

### Method 2: Direct Ollama Commands

```bash
# List all models
ollama list

# Show model details including file paths
ollama show llama3.2:3b

# Show modelfile (shows actual blob path)
ollama show llama3.2:3b --modelfile
```

### Method 3: Check Filesystem

```bash
# Windows
dir %USERPROFILE%\.ollama\models\blobs

# Linux/Mac
ls ~/.ollama/models/blobs
```

## 📋 Actual Model File Names

### Current Models (Example from System)

| Model Tag | Actual File Name (SHA256) | Size | Location |
|-----------|---------------------------|------|----------|
| `llama3.2:3b` | `sha256-dde5aa3fc5ffc17176b5e8bdc82f587b24b2678c6c66101bf7da77af9f7ccdff` | 1.88 GB | `C:\Users\mlesn\.ollama\models\blobs\` |

### Expected KAIJU IRON LEGION Models

| Model Tag | Purpose | Expected File Pattern |
|-----------|---------|----------------------|
| `codellama:13b` | Mark I - Primary code generation | `sha256-{digest}` |
| `llama3.2:11b` | Mark II - Secondary general | `sha256-{digest}` |
| `qwen2.5-coder:1.5b-base` | Mark III - Lightweight quick | `sha256-{digest}` |
| `llama3:8b` | Mark IV - General purpose | `sha256-{digest}` |
| `mistral:7b` | Mark V - General reasoning | `sha256-{digest}` |
| `mixtral:8x7b` | Mark VI - High complexity | `sha256-{digest}` |
| `gemma:2b` | Mark VII - Lightweight fallback | `sha256-{digest}` |

## 🔧 Model Name Validation

### Valid Model Name Formats

Ollama uses the format: `{name}:{tag}` or `{name}`

Examples:
- ✅ `llama3.2:3b` (name:tag)
- ✅ `llama3.2:11b`
- ✅ `codellama:13b`
- ✅ `qwen2.5-coder:1.5b-base`
- ✅ `mistral:7b`

Invalid formats:
- ❌ `llama3.2-11b` (use colon, not dash)
- ❌ `llama3_2:11b` (use dot, not underscore)
- ❌ `Llama3.2:11b` (case sensitive)

### Common Model Naming Patterns

#### Llama Models
- `llama3:8b` - Llama 3 8B
- `llama3:70b` - Llama 3 70B
- `llama3.1:8b` - Llama 3.1 8B
- `llama3.1:70b` - Llama 3.1 70B
- `llama3.2:3b` - Llama 3.2 3B
- `llama3.2:11b` - Llama 3.2 11B

#### CodeLlama Models
- `codellama:7b` - CodeLlama 7B
- `codellama:13b` - CodeLlama 13B
- `codellama:34b` - CodeLlama 34B

#### Qwen Models
- `qwen2.5:7b` - Qwen 2.5 7B
- `qwen2.5-coder:1.5b` - Qwen 2.5 Coder 1.5B
- `qwen2.5-coder:7b` - Qwen 2.5 Coder 7B

#### Mistral Models
- `mistral:7b` - Mistral 7B
- `mixtral:8x7b` - Mixtral 8x7B

#### Gemma Models
- `gemma:2b` - Gemma 2B
- `gemma:7b` - Gemma 7B

## 🛠️ Fixing Invalid Model Errors

### Step 1: Validate Current Models

```bash
# Run validation report
python scripts/python/fix_kaiju_iron_legion_models.py report
```

### Step 2: Check Actual Available Models

```bash
# List models with actual file names
python scripts/python/show_ollama_model_files.py report
```

### Step 3: Fix Configuration Files

```bash
# Automatically fix model references in code
python scripts/python/fix_kaiju_iron_legion_models.py fix
```

### Step 4: Pull Missing Models

If models are missing, pull them:

```bash
# Pull expected Iron Legion models
ollama pull codellama:13b
ollama pull llama3.2:11b
ollama pull qwen2.5-coder:1.5b-base
ollama pull llama3:8b
ollama pull mistral:7b
ollama pull mixtral:8x7b
ollama pull gemma:2b
```

## 📊 Model File Identification

### Understanding the Digest

The SHA256 digest in the file name is a unique identifier for the model file:
- Format: `sha256-{64 character hex string}`
- Example: `sha256-dde5aa3fc5ffc17176b5e8bdc82f587b24b2678c6c66101bf7da77af9f7ccdff`
- Purpose: Ensures file integrity and uniqueness

### Finding Model Type from File Name

The blob file name alone doesn't tell you the model type. You need to:

1. **Check the manifest**: Look in `~/.ollama/models/manifests/{model_name}`
2. **Query Ollama API**: Use `ollama show {model_name}`
3. **Check modelfile**: The modelfile contains the FROM reference

### Example: Identifying a Model

```bash
# Step 1: List all models
ollama list

# Step 2: Get model details
ollama show llama3.2:3b

# Output shows:
# - Digest (file identifier)
# - Size
# - Modelfile (which blob file it uses)
# - Parameters
```

## 🔗 Integration with Code

### In Python Code

```python
import requests

# Get model details
response = requests.post(
    "http://localhost:11434/api/show",
    json={"name": "llama3.2:3b"}
)
model_info = response.json()

# Access file information
digest = model_info.get("digest")
size = model_info.get("size")
modelfile = model_info.get("modelfile")
```

### Model Name Best Practices

1. **Always use the exact tag name** from `ollama list`
2. **Case sensitive**: `llama3.2:3b` ≠ `Llama3.2:3b`
3. **Use colon separator**: `name:tag` format
4. **Validate before use**: Check if model exists before referencing

## 📝 Configuration File Updates

### Update KAIJU IRON LEGION Monitor

The monitor script should reference models using their **actual Ollama tag names**:

```python
IRON_LEGION_MODELS = {
    "codellama:13b": {...},              # ✅ Correct
    "llama3.2:11b": {...},               # ✅ Correct
    "qwen2.5-coder:1.5b-base": {...},    # ✅ Correct
    # NOT: "llama3.2-11b"                # ❌ Wrong format
    # NOT: "llama3_2:11b"                # ❌ Wrong format
}
```

### Update Peak AI Orchestrator

```python
model_id="codellama:13b",    # ✅ Correct
model_id="llama3.2:11b",     # ✅ Correct
```

## 🚀 Quick Reference Commands

```bash
# Show all models with file names
python scripts/python/show_ollama_model_files.py report

# Validate Iron Legion models
python scripts/python/fix_kaiju_iron_legion_models.py report

# Fix model references
python scripts/python/fix_kaiju_iron_legion_models.py fix

# Check Ollama directly
ollama list
ollama show {model_name}
```

## 🎯 Summary

- **Model Tags**: Use exact names from `ollama list` (e.g., `llama3.2:3b`)
- **File Names**: SHA256 digests in `~/.ollama/models/blobs/`
- **Manifests**: Model name mappings in `~/.ollama/models/manifests/`
- **Validation**: Always validate model names before using in code
- **Fixing**: Use the fix script to update configuration files automatically

---

**Last Updated**: 2025-12-27
**Tools**: `show_ollama_model_files.py`, `fix_kaiju_iron_legion_models.py`
