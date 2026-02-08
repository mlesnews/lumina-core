# JEDI Holocron Management Procedures

**Date**: 2025-01-27  
**Classification**: OPERATIONAL PROCEDURES  
**Status**: 🟢 ACTIVE  
**Owner**: Jocasta Nu (Specialized AI Agent)  
**Tags**: `#jedi-management`, `#holocron-lifecycle`, `#operational-procedures`

---

## Executive Summary

**Holocron Management Procedures** define how to create, maintain, validate, archive, and utilize Holocrons within the JEDI Archives system. These procedures ensure consistent quality, proper metadata, efficient storage, and seamless integration with WOPR and Jupyter.

**Key Responsibilities**:

- **Creation**: Generate Holocrons from extracted features
- **Validation**: Ensure quality and security standards
- **Archival**: Store in JEDI Archives with metadata
- **Maintenance**: Update, organize, optimize
- **Utilization**: Support queries and access
- **Synchronization**: Keep WOPR and R5 in sync

---

## 1. Holocron Creation Procedures

### 1.1 Automatic Creation (via WOPR)

**Trigger**: WOPR Monitor detects new feature extraction  
**Procedure Owner**: Automated via WOPR_Monitor  
**Timing**: Real-time (immediate upon detection)

```python
# PROCEDURE: Create Holocron Automatically
def wopr_create_holocron(extracted_feature):
    """
    Create Holocron automatically when WOPR detects new feature
    """
    # Step 1: Generate Holocron ID
    holocron_id = generate_holocron_id()  # hol_YYYYMMDD_###
    
    # Step 2: Extract metadata automatically
    metadata = {
        "id": holocron_id,
        "name": extracted_feature.title,
        "type": determine_type(extracted_feature),  # document, notebook, analysis
        "domain": extracted_feature.domain,
        "created": datetime.now().isoformat(),
        "priority": determine_priority(extracted_feature),
        "status": "CREATED",
        "source": extracted_feature.source,  # PRIVATE, PUBLIC, INTERNAL
        "extracted_by": "WOPR_Monitor",
        "extraction_method": "wopr_extraction",
        "tags": extract_tags(extracted_feature),
        "validation": {
            "validated": False,
            "validation_method": None,
            "validation_date": None
        }
    }
    
    # Step 3: Create Holocron wrapper
    holocron = {
        "id": holocron_id,
        "metadata": metadata,
        "content": extracted_feature.content,
        "resource_metrics": initialize_metrics(extracted_feature)
    }
    
    # Step 4: Save Holocron to temporary location
    temp_path = save_to_temp(holocron)
    
    # Step 5: Queue for validation
    validation_queue.add(holocron_id)
    
    # Step 6: Log creation event
    log_event("holocron_created", {
        "id": holocron_id,
        "name": metadata["name"],
        "domain": metadata["domain"],
        "priority": metadata["priority"]
    })
    
    return holocron_id
```

### 1.2 Manual Creation

**When**: For non-extracted knowledge (historical documents, procedures)  
**Procedure Owner**: Knowledge Manager / Curator  
**Timing**: As needed

**Steps**:

1. **Identify Source Material**
   - Locate document, notebook, or analysis
   - Verify completeness and relevance
   - Check for duplicate existing Holocrons

2. **Prepare Content**
   - Format document if needed (.md, .ipynb, .json)
   - Ensure file size is reasonable (<1 GB)
   - Verify all links and references work

3. **Create Metadata**

   ```json
   {
     "name": "Document Name",
     "type": "document|notebook|analysis",
     "domain": "ai_defense|financial_analysis|crypto|resource",
     "priority": "CRITICAL|HIGH|MEDIUM|LOW",
     "source": "INTERNAL|MANUAL_ENTRY",
     "tags": ["tag1", "tag2"],
     "description": "Brief description of content"
   }
   ```

4. **Assign to Domain Folder**

   ```bash
   # Move to appropriate domain
   cp /path/to/file data/holocron/[DOMAIN]/[SUBDOMAIN]/[FILENAME]
   ```

5. **Register in Index**
   - Add entry to HOLOCRON_INDEX.json
   - Include all metadata
   - Set status to CREATED

6. **Submit for Validation**
   - Queue for WOPR validation
   - Add to validation workflow

---

## 2. Validation Procedures

### 2.1 WOPR Validation Process

**Owner**: WOPR_Validate module  
**Frequency**: Continuous (real-time)  
**Time**: ~5-15 minutes per Holocron

**Validation Steps**:

```python
def wopr_validate_holocron(holocron_id):
    """
    Validate Holocron meets quality and security standards
    """
    holocron = load_holocron(holocron_id)
    validation_report = {
        "id": holocron_id,
        "timestamp": datetime.now().isoformat(),
        "checks": {}
    }
    
    # CHECK 1: Metadata Completeness
    validation_report["checks"]["metadata"] = {
        "passed": verify_metadata_complete(holocron),
        "timestamp": datetime.now().isoformat(),
        "notes": "All required fields present" if True else "Missing fields"
    }
    
    # CHECK 2: Security Scan
    validation_report["checks"]["security"] = {
        "passed": run_security_scan(holocron),
        "threats_found": security_scan_result.get("threats", []),
        "severity": "CRITICAL|HIGH|MEDIUM|LOW|NONE"
    }
    
    # CHECK 3: Content Quality
    validation_report["checks"]["quality"] = {
        "passed": check_content_quality(holocron),
        "readability_score": calculate_readability(holocron),
        "completeness_score": calculate_completeness(holocron),
        "notes": "Analysis of quality metrics"
    }
    
    # CHECK 4: Source Verification
    validation_report["checks"]["source"] = {
        "passed": verify_source_authenticity(holocron),
        "source_verified": True,
        "source_type": "PRIVATE|PUBLIC|INTERNAL"
    }
    
    # CHECK 5: Format Validation
    validation_report["checks"]["format"] = {
        "passed": validate_format(holocron),
        "file_type": holocron.get("type"),
        "encoding": "UTF-8",
        "size_mb": holocron.get("size_mb")
    }
    
    # CHECK 6: Dependency Check (if applicable)
    validation_report["checks"]["dependencies"] = {
        "passed": check_dependencies(holocron),
        "missing_deps": [],
        "notes": "All dependencies available"
    }
    
    # DECISION: Pass or Fail
    all_checks_passed = all(c["passed"] for c in validation_report["checks"].values())
    
    if all_checks_passed:
        # PASSED: Mark as ACTIVE
        holocron["metadata"]["status"] = "ACTIVE"
        holocron["metadata"]["validation"] = {
            "validated": True,
            "validation_method": "WOPR_Validate",
            "validation_date": datetime.now().isoformat(),
            "validator": "WOPR_Validate",
            "validation_report": validation_report
        }
        log_event("validation_passed", {"id": holocron_id})
        return True
    else:
        # FAILED: Mark as REJECTED
        holocron["metadata"]["status"] = "REJECTED"
        holocron["metadata"]["validation_errors"] = [
            c["notes"] for c in validation_report["checks"].values() if not c["passed"]
        ]
        log_event("validation_failed", {
            "id": holocron_id,
            "errors": holocron["metadata"]["validation_errors"]
        })
        return False
```

### 2.2 Validation Checklist

```markdown
## Holocron Validation Checklist

### Metadata
- [ ] All required fields present (id, name, type, domain, created, priority)
- [ ] Domain is valid (ai_defense, financial_analysis, crypto, resource)
- [ ] Priority is appropriate (CRITICAL, HIGH, MEDIUM, LOW)
- [ ] Tags are descriptive (3-5 tags minimum)
- [ ] Source is verified (PRIVATE, PUBLIC, INTERNAL)

### Security
- [ ] No malicious code detected
- [ ] No sensitive data exposed
- [ ] No hard-coded credentials
- [ ] No external API keys
- [ ] No unauthorized data references

### Quality
- [ ] Content is complete and coherent
- [ ] Grammar and spelling checked
- [ ] Technical accuracy verified
- [ ] Format is consistent
- [ ] File size is reasonable (<1 GB)

### Technical
- [ ] File format is valid (MD, IPYNB, JSON, PDF, etc.)
- [ ] All links and references work
- [ ] Code (if present) executes without errors
- [ ] Dependencies are available
- [ ] Version information is current

### Completeness
- [ ] All referenced documents included
- [ ] All code snippets are complete
- [ ] All data files are present
- [ ] All metadata is filled in
- [ ] Summary/abstract is provided

### Status
- [ ] Passes all checks? YES / NO
- [ ] Ready for archival? YES / NO
- [ ] Any concerns or warnings? (List below)

---
Validated by: [Agent Name]
Validation Date: [ISO Date]
Validation Report ID: [ID]
```

---

## 3. Archival Procedures

### 3.1 Archival Workflow

**Owner**: Jocasta Nu (Archival Agent)  
**Trigger**: Validation PASSED  
**Process**: Automated with logging

```python
def jocasta_nu_archive_holocron(holocron_id):
    """
    Archive validated Holocron to JEDI Archives
    Coordinated with WOPR Coordinate
    """
    
    holocron = load_holocron(holocron_id)
    archival_report = {
        "id": holocron_id,
        "timestamp": datetime.now().isoformat(),
        "steps": []
    }
    
    # STEP 1: Determine Storage Location
    storage_path = determine_storage_path(
        domain=holocron["metadata"]["domain"],
        type=holocron["metadata"]["type"],
        priority=holocron["metadata"]["priority"]
    )
    
    archival_report["steps"].append({
        "step": "determine_location",
        "path": storage_path,
        "status": "SUCCESS"
    })
    
    # STEP 2: Create Directory Structure
    create_directory_structure(storage_path)
    
    archival_report["steps"].append({
        "step": "create_directories",
        "path": storage_path,
        "status": "SUCCESS"
    })
    
    # STEP 3: Save Holocron Content
    final_path = save_holocron_to_archive(holocron, storage_path)
    
    archival_report["steps"].append({
        "step": "save_content",
        "path": final_path,
        "size_mb": holocron.get("size_mb"),
        "status": "SUCCESS"
    })
    
    # STEP 4: Create Metadata File
    metadata_path = save_metadata_file(holocron, final_path)
    
    archival_report["steps"].append({
        "step": "save_metadata",
        "path": metadata_path,
        "status": "SUCCESS"
    })
    
    # STEP 5: Update Master Index
    update_holocron_index(holocron, final_path)
    
    archival_report["steps"].append({
        "step": "update_index",
        "index_path": "data/holocron/HOLOCRON_INDEX.json",
        "status": "SUCCESS"
    })
    
    # STEP 6: Ingest to R5 (Living Context Matrix)
    r5_session_id = ingest_to_r5(holocron)
    
    holocron["metadata"]["r5_integration"] = {
        "ingested": True,
        "session_id": r5_session_id,
        "ingestion_date": datetime.now().isoformat(),
        "searchable": True,
        "accessible": True
    }
    
    archival_report["steps"].append({
        "step": "r5_ingestion",
        "session_id": r5_session_id,
        "status": "SUCCESS"
    })
    
    # STEP 7: Finalize Status
    holocron["metadata"]["status"] = "ARCHIVED"
    holocron["metadata"]["archived_date"] = datetime.now().isoformat()
    holocron["metadata"]["archived_by"] = "Jocasta_Nu"
    
    archival_report["steps"].append({
        "step": "finalize_status",
        "status": "ARCHIVED",
        "status": "SUCCESS"
    })
    
    # STEP 8: Log Archival Event
    log_event("holocron_archived", {
        "id": holocron_id,
        "name": holocron["metadata"]["name"],
        "path": final_path,
        "r5_session": r5_session_id,
        "report": archival_report
    })
    
    # STEP 9: Send Confirmation to WOPR
    wopr_synchronize.holocron_archived(holocron_id, final_path)
    
    archival_report["status"] = "COMPLETE"
    archival_report["final_path"] = final_path
    
    return archival_report
```

### 3.2 Storage Location Rules

```python
def determine_storage_path(domain, type, priority):
    """Determine where to store Holocron"""
    
    base_path = Path("data/holocron")
    
    # RULE 1: By Domain
    domain_path = {
        "ai_defense": "ai_defense",
        "financial_analysis": "financial_analysis",
        "crypto_analysis": "crypto_analysis",
        "resource_management": "resource_management"
    }.get(domain, "research_archives")
    
    # RULE 2: By Subdomain (Type-based)
    type_map = {
        "document": "documents",
        "notebook": "notebooks",
        "analysis": "analysis",
        "procedure": "procedures",
        "intelligence_feed": "feeds"
    }
    
    subdomain = type_map.get(type, "misc")
    
    # RULE 3: Priority affects retention
    # (All stored the same, but metadata tracks priority)
    
    # RESULT: data/holocron/[DOMAIN]/[SUBDOMAIN]/
    return base_path / domain_path / subdomain
```

---

## 4. Maintenance Procedures

### 4.1 Daily Maintenance (Automated)

**Time**: 00:00 UTC (midnight)  
**Owner**: Automated Jocasta Nu task  
**Duration**: 5-10 minutes

```bash
#!/bin/bash
# Daily Maintenance Script

# 1. Validate index integrity
python scripts/python/jedi_archives/validate_index.py

# 2. Update access statistics
python scripts/python/jedi_archives/update_access_stats.py

# 3. Check for orphaned files
python scripts/python/jedi_archives/check_orphaned_files.py

# 4. Verify R5 sync status
python scripts/python/jedi_archives/verify_r5_sync.py

# 5. Log daily metrics
python scripts/python/jedi_archives/log_daily_metrics.py

echo "Daily maintenance complete"
```

### 4.2 Weekly Maintenance

**Time**: Every Friday 18:00 UTC  
**Owner**: WOPR Monitor  
**Duration**: 20-30 minutes

```python
def weekly_maintenance():
    """Weekly JEDI Archives maintenance"""
    
    # 1. Full index rebuild
    rebuild_holocron_index()
    
    # 2. Identify unused items
    unused = identify_unused_holocrons(access_threshold=0, days=30)
    for item in unused:
        mark_for_review(item)
    
    # 3. Archive old items
    old_items = find_items(status="ACTIVE", older_than_days=365)
    for item in old_items:
        move_to_cold_storage(item)
    
    # 4. Optimize storage
    optimize_storage()
    
    # 5. Generate statistics
    stats = generate_statistics()
    save_statistics(stats)
    
    # 6. Send report
    send_weekly_report(stats)
```

### 4.3 Monthly Review

**Time**: First Friday of month, 15:00 UTC  
**Owner**: Curator (Jocasta Nu oversees)  
**Duration**: 1 hour

**Review Checklist**:

- [ ] Total Holocrons count
- [ ] Storage utilization (GB, cost)
- [ ] Most accessed items
- [ ] Least accessed items
- [ ] REJECTED items (reason analysis)
- [ ] R5 integration status
- [ ] Performance metrics
- [ ] Cost summary
- [ ] Recommendations for optimization
- [ ] Archive health check

---

## 5. Query & Access Procedures

### 5.1 Basic Query

```python
# Procedure: Query JEDI Archives via R5
from r5_living_context_matrix import R5LivingContextMatrix

r5 = R5LivingContextMatrix(project_root)

# Query 1: Search by keyword
results = r5.search("threat analysis", domain="ai_defense")

# Query 2: Search by tag
results = r5.search_by_tag("defense")

# Query 3: Search by domain
results = r5.search_by_domain("financial_analysis")

# Query 4: Get all CRITICAL items
results = r5.search_by_priority("CRITICAL")

# Query 5: Get recently created items
results = r5.search_recent(days=7)
```

### 5.2 Advanced Query

```python
# Procedure: Advanced query with filters
import json
from pathlib import Path

def advanced_query(domain=None, priority=None, status="ACTIVE", 
                  accessed_within_days=None):
    """Advanced query with multiple filters"""
    
    with open("data/holocron/HOLOCRON_INDEX.json") as f:
        index = json.load(f)
    
    results = index["holocrons"]
    
    # Filter by domain
    if domain:
        results = [h for h in results if h["domain"] == domain]
    
    # Filter by priority
    if priority:
        results = [h for h in results if h["priority"] == priority]
    
    # Filter by status
    results = [h for h in results if h["status"] == status]
    
    # Filter by access date
    if accessed_within_days:
        cutoff = datetime.now() - timedelta(days=accessed_within_days)
        results = [h for h in results 
                  if datetime.fromisoformat(h["last_accessed"]) > cutoff]
    
    return results
```

### 5.3 Access Logging

Every access to a Holocron is logged:

```python
def access_holocron(holocron_id):
    """Track access to Holocron"""
    
    # Load Holocron
    holocron = load_holocron(holocron_id)
    
    # Increment access count
    holocron["metadata"]["access_count"] += 1
    holocron["metadata"]["last_accessed"] = datetime.now().isoformat()
    
    # Log access event
    log_event("holocron_accessed", {
        "id": holocron_id,
        "name": holocron["metadata"]["name"],
        "domain": holocron["metadata"]["domain"],
        "access_count": holocron["metadata"]["access_count"]
    })
    
    # Return Holocron
    return holocron
```

---

## 6. Update Procedures

### 6.1 Update Holocron Content

**When**: Content needs update/revision  
**Owner**: Original creator or authorized person  
**Process**:

1. **Load Current Version**

   ```python
   holocron = load_holocron("hol_20250127_001")
   ```

2. **Modify Content**
   - Edit document, notebook, or data
   - Preserve metadata
   - Update modification timestamp

3. **Validate Changes**
   - Run WOPR validation (abbreviated)
   - Check for security issues
   - Verify links/references still work

4. **Update Index**

   ```python
   update_holocron_index(holocron, {
       "modified": datetime.now().isoformat(),
       "modified_by": "User/Agent",
       "change_summary": "Brief description of changes"
   })
   ```

5. **Sync to R5**
   - Update R5 ingestion
   - Invalidate caches
   - Update search index

### 6.2 Version Control

**For Notebooks**: Use built-in Jupyter versioning  
**For Documents**: Maintain versions in naming

```
- Document_v1.0.md (original)
- Document_v1.1.md (minor update)
- Document_v2.0.md (major revision)
```

---

## 7. Decommissioning Procedures

### 7.1 Mark as Deprecated

```python
def deprecate_holocron(holocron_id, reason):
    """Mark Holocron as deprecated"""
    
    holocron = load_holocron(holocron_id)
    
    holocron["metadata"]["status"] = "DEPRECATED"
    holocron["metadata"]["deprecation"] = {
        "date": datetime.now().isoformat(),
        "reason": reason,
        "replacement_id": None,  # If applicable
        "archived_for_retention": True
    }
    
    save_holocron(holocron)
    log_event("holocron_deprecated", {"id": holocron_id, "reason": reason})
```

### 7.2 Archive to Cold Storage

```python
def archive_to_cold_storage(holocron_id):
    """Move old Holocron to cold storage"""
    
    holocron = load_holocron(holocron_id)
    
    # Move to archive location
    cold_storage_path = Path("data/holocron/archive/") / datetime.now().strftime("%Y/%m/")
    move_file(holocron["path"], cold_storage_path)
    
    # Update metadata
    holocron["metadata"]["archived_to_cold_storage"] = {
        "date": datetime.now().isoformat(),
        "original_path": holocron["path"],
        "cold_storage_path": str(cold_storage_path)
    }
    
    save_holocron(holocron)
```

### 7.3 Delete (After Retention)

```python
def delete_holocron_permanent(holocron_id):
    """Permanently delete after retention period"""
    
    # Default retention: 12 months for ACTIVE, 6 months for DEPRECATED
    holocron = load_holocron(holocron_id)
    created = datetime.fromisoformat(holocron["metadata"]["created"])
    
    retention_days = 365 if holocron["metadata"]["status"] == "ACTIVE" else 180
    delete_after = created + timedelta(days=retention_days)
    
    if datetime.now() >= delete_after:
        # Delete from filesystem
        delete_file(holocron["path"])
        
        # Remove from index
        remove_from_index(holocron_id)
        
        # Remove from R5
        remove_from_r5(holocron_id)
        
        # Log deletion
        log_event("holocron_deleted_permanent", {"id": holocron_id})
```

---

## 8. Emergency Procedures

### 8.1 Index Corruption

**Symptom**: Index file damaged, inaccessible  
**Response**:

```bash
# Step 1: Create backup of corrupted index
cp data/holocron/HOLOCRON_INDEX.json data/holocron/HOLOCRON_INDEX.json.corrupted

# Step 2: Rebuild from physical files
python scripts/python/jedi_archives/rebuild_index_from_files.py

# Step 3: Verify new index
python scripts/python/jedi_archives/validate_index.py

# Step 4: Compare with backups
python scripts/python/jedi_archives/compare_with_backup.py

# Step 5: If successful, log incident
echo "Index rebuilding complete - verify all Holocrons present"
```

### 8.2 Orphaned Files

**Symptom**: Files in archive without index entry  
**Response**:

```python
def fix_orphaned_files():
    """Identify and re-register orphaned files"""
    
    # Find all files in archive
    files_on_disk = set(find_all_files("data/holocron/"))
    
    # Find all files in index
    with open("data/holocron/HOLOCRON_INDEX.json") as f:
        index = json.load(f)
    
    files_in_index = set(h["path"] for h in index["holocrons"])
    
    # Find orphans
    orphans = files_on_disk - files_in_index
    
    # Re-register each orphan
    for file_path in orphans:
        print(f"Re-registering: {file_path}")
        # Create minimal metadata
        # Re-run validation
        # Add back to index
```

### 8.3 R5 Sync Loss

**Symptom**: Holocrons not searchable in R5  
**Response**:

```bash
# Step 1: Check R5 connection
python scripts/python/jedi_archives/test_r5_connection.py

# Step 2: Force re-ingestion
python scripts/python/jedi_archives/reingest_to_r5.py

# Step 3: Verify sync
python scripts/python/jedi_archives/verify_r5_completeness.py

# Step 4: Update index
python scripts/python/jedi_archives/update_r5_status.py
```

---

## 9. Automation Scripts

### 9.1 Create Holocron (Automated)

Location: `scripts/python/jedi_archives/holocron_manager.py`

```bash
# Create new Holocron
python scripts/python/jedi_archives/holocron_manager.py create \
  --name "Analysis Name" \
  --domain ai_defense \
  --type document \
  --priority HIGH \
  --source PRIVATE

# Create from existing file
python scripts/python/jedi_archives/holocron_manager.py import \
  --file /path/to/file \
  --domain financial_analysis \
  --type notebook
```

### 9.2 Query Holocrons (Automated)

```bash
# Search
python scripts/python/jedi_archives/query_engine.py search \
  --query "threat analysis" \
  --domain ai_defense

# List by priority
python scripts/python/jedi_archives/query_engine.py list \
  --priority CRITICAL \
  --status active

# Get statistics
python scripts/python/jedi_archives/query_engine.py stats \
  --domain all
```

### 9.3 Validation (Automated)

```bash
# Validate single Holocron
python scripts/python/jedi_archives/metadata_validator.py validate \
  --id hol_20250127_001

# Validate all
python scripts/python/jedi_archives/metadata_validator.py validate_all

# Generate report
python scripts/python/jedi_archives/metadata_validator.py report
```

---

## 10. Training & Examples

### 10.1 Training Exercises

1. **Create first Holocron** (manual)
   - Pick a document
   - Create metadata
   - Archive it
   - Verify in index

2. **Query JEDI Archives** (via R5)
   - Search by keyword
   - Filter by priority
   - Access result

3. **Manage Holocron** (update, access tracking)
   - Load existing Holocron
   - Modify metadata
   - Verify changes

4. **Handle validation failure**
   - Deliberately create invalid Holocron
   - Observe validation failure
   - Correct issues
   - Re-validate successfully

---

## 11. Quick Reference

### Common Commands

```bash
# List all CRITICAL items
jedi query --priority CRITICAL

# Search for items
jedi search "keyword" --domain ai_defense

# Get Holocron details
jedi get hol_20250127_001

# Update Holocron
jedi update hol_20250127_001 --priority HIGH

# Deprecate Holocron
jedi deprecate hol_20250127_001 --reason "Superseded by v2"

# Generate report
jedi report --period weekly
```

---

**Status**: 🟢 DOCUMENTED & READY  
**Last Updated**: 2025-01-27  
**Owner**: Jocasta Nu (AI Agent)  
**Next Review**: 2025-02-10

**"Through consistent procedures, knowledge is preserved. Through Jocasta Nu's guidance, order prevails in the Archives."**
