# @ask Ticket Holocron Middleware

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#HOLOCRON` `#MIDDLEWARE` `#VALIDATION` `#JUPYTER` `@JARVIS` `@LUMINA`

---

## Overview

The @ask Ticket Holocron Middleware provides **data validation and shaping** using:
- **Jupyter notebook server on NAS** as middleware processing layer
- **@holocrons** to mold and shape data before database propagation

**Data Flow**:
```
@ask → Jupyter Notebook Server (NAS) → @Holocron Validation/Shaping → Database
```

---

## Architecture

### Data Flow Pipeline

```
┌─────────────┐
│   @ask      │
│   Data      │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│ Jupyter Notebook Server  │
│      (NAS)               │
│  http://10.17.17.32:8888 │
│                          │
│  - Data Processing       │
│  - Transformation        │
│  - Initial Validation    │
└──────┬───────────────────┘
       │
       ▼
┌─────────────────────────┐
│   @Holocron Validation  │
│                         │
│  - Shape Validation     │
│  - Field Validation     │
│  - Pattern Matching     │
│  - Data Correction      │
│  - Data Shaping         │
└──────┬───────────────────┘
       │
       ▼
┌─────────────────────────┐
│   Database              │
│   (SQLite)              │
│                         │
│  - Validated Data       │
│  - Shaped Data          │
│  - Holocron Insights    │
└─────────────────────────┘
```

---

## Features

### 1. Jupyter Notebook Server Integration

**Purpose**: Process data through Jupyter notebook server on NAS before validation

**Location**: `http://10.17.17.32:8888`

**Capabilities**:
- Data preprocessing
- Initial transformation
- Data enrichment
- Format normalization

**Status**: Placeholder for production integration

### 2. @Holocron Validation

**Purpose**: Validate data against holocron shapes before database propagation

**Validation Types**:
- **Required Fields**: Check all required fields present
- **Field Types**: Validate field types match expected types
- **Pattern Matching**: Validate patterns (e.g., ticket numbers, UUIDs)
- **Length Validation**: Check min/max lengths
- **Data Correction**: Automatically correct common issues

### 3. @Holocron Data Shaping

**Purpose**: Mold and shape data using holocron transformation rules

**Transformation Rules**:
- **Trim Whitespace**: Remove leading/trailing whitespace
- **Normalize Unicode**: Normalize unicode characters
- **Lowercase**: Convert to lowercase
- **Remove Duplicates**: Remove duplicate items from lists
- **Sort**: Sort list items

### 4. Automatic Correction

**Correction Types**:
- **Add Required Fields**: Add missing required fields with defaults
- **Type Conversion**: Convert types (e.g., string to list)
- **Pattern Fixing**: Fix patterns (e.g., add TICKET- prefix)
- **Truncation**: Truncate fields that exceed max length

### 5. Holocron Insights

**Purpose**: Consult @holocron for additional validation rules and insights

**Insights Include**:
- Holocron shape references
- Validation rule sources
- Data quality recommendations
- Pattern matching results

---

## Holocron Shapes

### Default @ask Ticket Shape

```python
HolocronShape(
    shape_id="ask_ticket",
    shape_name="@ask Ticket Data Shape",
    required_fields=["ask_id", "ask_text", "created_at"],
    field_types={
        "ask_id": "str",
        "ask_text": "str",
        "helpdesk_ticket": "str",
        "gitlens_ticket": "str",
        "gitlens_pr": "str",
        "tags": "list",
        "syphon_patterns": "list",
        "assigned_team": "str",
        "status": "str",
        "priority": "str"
    },
    validation_rules={
        "ask_id": {
            "pattern": r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
            "required": True
        },
        "ask_text": {
            "min_length": 5,
            "max_length": 5000,
            "required": True
        },
        "helpdesk_ticket": {
            "pattern": r"^TICKET-\d{8}-\d{4}$",
            "required": False
        }
    },
    transformation_rules={
        "ask_text": {
            "trim_whitespace": True,
            "normalize_unicode": True
        },
        "tags": {
            "lowercase": True,
            "remove_duplicates": True,
            "sort": True
        }
    },
    holocron_reference="@holocron/ask_ticket_validation"
)
```

---

## Usage Examples

### 1. Process @ask Through Middleware

```python
from ask_ticket_holocron_middleware import AskTicketHolocronMiddleware

middleware = AskTicketHolocronMiddleware(
    jupyter_nas_url="http://10.17.17.32:8888"
)

# Process @ask through middleware
record, validation = middleware.process_through_middleware(
    ask_id="cd5eb779-d000-4f45-8ea5-a0de9b47d07e",
    ask_text="@ask @jarvis @r5 #peak optimize workflow X",
    helpdesk_ticket="TICKET-20260112-0001",
    gitlens_ticket="#123",
    gitlens_pr="PR#456"
)

print(f"Valid: {validation.valid}")
print(f"Corrected: {validation.corrected}")
print(f"Corrections: {len(validation.corrections)}")
print(f"Holocron insights: {validation.holocron_insights}")
```

### 2. Command Line Usage

```bash
# Process @ask through middleware
python scripts/python/ask_ticket_holocron_middleware.py \
    --process "cd5eb779-d000-4f45-8ea5-a0de9b47d07e" \
    "@ask @jarvis @r5 #peak optimize workflow X" \
    "TICKET-20260112-0001" \
    "#123" \
    "PR#456"
```

### 3. Integration with Collation System

```python
from ask_ticket_holocron_middleware import AskTicketHolocronMiddleware
from ask_ticket_integration import AskTicketIntegration

# Use middleware for validation before collation
middleware = AskTicketHolocronMiddleware()

# Process through middleware first
record, validation = middleware.process_through_middleware(
    ask_id="new-request-id",
    ask_text="@ask @jarvis fix error",
    helpdesk_ticket="TICKET-20260112-0002"
)

# Data is now validated and shaped, ready for database
```

---

## Validation Process

### Step 1: Jupyter Processing (Optional)

- Send data to Jupyter notebook server on NAS
- Execute notebook cells for processing
- Receive processed data back

### Step 2: Holocron Validation

1. **Check Required Fields**: Ensure all required fields present
2. **Validate Field Types**: Check types match expected types
3. **Pattern Matching**: Validate patterns (UUIDs, ticket numbers, etc.)
4. **Length Validation**: Check min/max lengths
5. **Generate Corrections**: Create correction list for invalid data

### Step 3: Apply Corrections

- Add missing required fields
- Convert types
- Fix patterns
- Truncate long fields
- Re-validate after corrections

### Step 4: Shape Data

- Apply transformation rules
- Trim whitespace
- Normalize unicode
- Lowercase tags
- Remove duplicates
- Sort lists

### Step 5: Consult @Holocron

- Query holocron for additional insights
- Get validation rule references
- Retrieve data quality recommendations

### Step 6: Propagate to Database

- Only propagate if validation passes
- Include holocron insights in metadata
- Store validation results

---

## Benefits

### 1. Data Quality Assurance

- **Validation before database**: Catch errors early
- **Automatic correction**: Fix common issues automatically
- **Pattern enforcement**: Ensure data follows expected patterns

### 2. Data Consistency

- **Holocron shapes**: Consistent data structure
- **Transformation rules**: Standardized data format
- **Type safety**: Ensure correct data types

### 3. @Holocron Integration

- **Leverage holocron knowledge**: Use existing validation rules
- **Shape data**: Mold data according to holocron templates
- **Insights**: Get holocron-based recommendations

### 4. Middleware Processing

- **Jupyter integration**: Process data through notebooks
- **NAS-based**: Centralized processing on NAS
- **Scalable**: Can handle large volumes

---

## Configuration

### Jupyter NAS Configuration

```python
jupyter_nas_url = "http://10.17.17.32:8888"
```

### Holocron Directory

```python
holocron_dir = "data/holocron/"
```

### Holocron Shapes File

```json
{
  "ask_ticket": {
    "shape_id": "ask_ticket",
    "shape_name": "@ask Ticket Data Shape",
    "required_fields": ["ask_id", "ask_text", "created_at"],
    "field_types": {...},
    "validation_rules": {...},
    "transformation_rules": {...}
  }
}
```

---

## Status

✅ **ACTIVE** - Middleware is operational

**Components**:
1. ✅ Jupyter notebook server integration (placeholder)
2. ✅ @Holocron validation system
3. ✅ Data shaping and transformation
4. ✅ Automatic correction
5. ✅ Database propagation

**Next Steps**:
1. Implement actual Jupyter notebook server integration
2. Create additional holocron shapes
3. Enhance validation rules
4. Add more transformation rules
5. Integrate with existing @ask processing workflows

---

**Tags**: `#ASK` `#HELPDESK` `#GITLENS` `#HOLOCRON` `#MIDDLEWARE` `#VALIDATION` `#JUPYTER` `@JARVIS` `@LUMINA` `#PEAK`
