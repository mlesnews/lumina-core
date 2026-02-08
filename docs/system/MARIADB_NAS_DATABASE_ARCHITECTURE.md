# MariaDB@NAS Database Architecture

**Date:** 2026-01-09  
**Standing Order:** @DB[#DATABASE] = MariaDB@NAS (OEM)  
**Tags:** #JARVIS @LUMINA @DB #DATABASE #MARIADB #NAS

---

## Standing Order

**@DB[#DATABASE] = MariaDB@NAS**

This is the one and only @DB type we at LUMINA have chosen as our OEM.

**Unless modified, this standing order applies now and in the future.**

---

## Multi-Database Architecture

**Multiple databases is actually a good idea, if we silo systems separately.**

### Siloed Databases

Each system/category gets its own database on MariaDB@NAS:

1. **@HELPDESK** - `helpdesk` database
   - Helpdesk system database
   - Tickets, workflows, routing

2. **@HOLOGRAM** - `hologram` database
   - Metadata linking to Jupyter Notebooks
   - Internal URL management
   - Notebook relationships

3. **@ONE_RING** - `master_todo` database
   - Master TODO List - The One Ring Blueprint
   - Living document sync

4. **@HOLOCRON** - `holocron` database
   - Holocron Jupyter Notebook database
   - Additional holocron data

5. **Additional Systems** - As needed
   - Each system gets its own database
   - Siloed for separation of concerns

---

## Architecture

### MariaDB@NAS Connection

**Host:** `10.17.17.32` (DS1821PLUS)  
**Hostname:** `DS1821PLUS.lesnewski.local`  
**Port:** `3306`  
**OEM:** MariaDB

### Database Registry

**File:** `config/lumina_db_registry.json`

**Structure:**
```json
{
  "oem_database": "MariaDB@NAS",
  "nas_host": "10.17.17.32",
  "nas_hostname": "DS1821PLUS.lesnewski.local",
  "databases": {
    "helpdesk": {
      "name": "helpdesk",
      "system": "@HELPDESK",
      "description": "Helpdesk system database",
      "created": true,
      "tables": []
    },
    "hologram": {
      "name": "hologram",
      "system": "@HOLOGRAM",
      "description": "Metadata linking to Jupyter Notebooks",
      "created": true,
      "tables": [
        "notebook_metadata",
        "notebook_links",
        "internal_urls"
      ]
    },
    "master_todo": {
      "name": "master_todo",
      "system": "@ONE_RING",
      "description": "Master TODO List - The One Ring Blueprint",
      "created": true,
      "tables": ["master_todos"]
    }
  }
}
```

---

## @HOLOGRAM Database

**Purpose:** Metadata linking to Jupyter Notebooks

### Tables

1. **`notebook_metadata`**
   - Notebook path, name
   - Jupyter URL
   - Internal URL (for linking)
   - Metadata JSON
   - Timestamps

2. **`notebook_links`**
   - Source notebook → Target notebook
   - Link types
   - Relationships

3. **`internal_urls`**
   - Internal URLs
   - Linked to notebooks
   - Descriptions

### Usage

```python
from jarvis_siloed_databases import JARVISSiloedDatabases, DatabaseSystem

manager = JARVISSiloedDatabases()
conn = manager.get_connection(DatabaseSystem.HOLOGRAM)

# Link notebook to internal URL
cursor = conn.cursor()
cursor.execute("""
    INSERT INTO notebook_metadata 
    (notebook_path, notebook_name, internal_url)
    VALUES (%s, %s, %s)
""", ("path/to/notebook.ipynb", "Notebook Name", "internal://notebook/123"))
```

---

## @HELPDESK Database

**Purpose:** Helpdesk system

**Tables:** (To be defined based on helpdesk requirements)

---

## Connection Management

### Standard Connection

```python
from jarvis_mariadb_nas_connection import get_mariadb_connection

# Connect to specific database
conn = get_mariadb_connection("helpdesk")
```

### Siloed Database Access

```python
from jarvis_siloed_databases import JARVISSiloedDatabases, DatabaseSystem

manager = JARVISSiloedDatabases()

# Get connection for system
conn = manager.get_connection(DatabaseSystem.HELPDESK)
conn = manager.get_connection(DatabaseSystem.HOLOGRAM)
conn = manager.get_connection(DatabaseSystem.MASTER_TODO)
```

---

## Setup

### Initialize Databases

```bash
# Setup @HOLOGRAM database
python scripts/python/jarvis_siloed_databases.py --setup-hologram

# Setup @HELPDESK database
python scripts/python/jarvis_siloed_databases.py --setup-helpdesk

# Show registry
python scripts/python/jarvis_siloed_databases.py --registry
```

### Test Connection

```bash
python scripts/python/jarvis_mariadb_nas_connection.py --test helpdesk
python scripts/python/jarvis_mariadb_nas_connection.py --list-databases
```

---

## Benefits of Siloed Databases

1. **Separation of Concerns**
   - Each system isolated
   - Independent schemas
   - Clear boundaries

2. **Scalability**
   - Can scale individual databases
   - Optimize per system
   - Independent backups

3. **Security**
   - Per-database permissions
   - Isolated access
   - Reduced attack surface

4. **Maintenance**
   - Independent updates
   - System-specific optimizations
   - Clear ownership

---

## Migration from SQLite

The system maintains backward compatibility with SQLite as a fallback:

1. **Primary:** MariaDB@NAS
2. **Fallback:** SQLite (if MariaDB unavailable)

This ensures smooth transition and reliability.

---

## Summary

- **@DB[#DATABASE] = MariaDB@NAS** (OEM, standing order)
- **Multiple databases** for siloed systems
- **@HELPDESK** - Helpdesk system
- **@HOLOGRAM** - Metadata linking to Jupyter Notebooks
- **@ONE_RING** - Master TODO List
- **Additional systems** as needed

**All on MariaDB@NAS, siloed for separation of concerns.**

---

**Tags:** #JARVIS @LUMINA @DB #DATABASE #MARIADB #NAS @HELPDESK @HOLOGRAM
