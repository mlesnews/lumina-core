# SYPHON Intelligence Deduplication System

## Overview

Prevents extraction of duplicate intelligence unless there are substantial major/minor updates. Uses content hashing and similarity analysis to detect duplicates and updates.

## Deduplication Strategy

### Intelligence Hashing

#### Primary Hash (Full Intelligence Hash)
- **Purpose**: Detect exact duplicates
- **Fields Hashed**:
  - Content
  - Title
  - Summary
  - URL
  - Source
- **Algorithm**: SHA256
- **Use Case**: Exact duplicate detection

#### Content Hash (Change Detection)
- **Purpose**: Detect content changes for update detection
- **Fields Hashed**: Content only
- **Algorithm**: SHA256
- **Use Case**: Major/minor update detection

### Duplicate Detection

#### Exact Duplicate
- **Condition**: Same primary hash AND same content hash
- **Action**: Skip extraction
- **Logging**: `⏭️ Skipped duplicate intelligence`

#### No Substantial Update
- **Condition**: Same primary hash BUT content similarity >95%
- **Action**: Skip extraction
- **Reason**: Changes are too minor (<5% difference)
- **Logging**: `⏭️ Skipped duplicate intelligence`

### Update Detection

#### Major Update
- **Condition**: Content similarity <70%
- **Action**: Extract and process
- **Update Type**: `major`
- **Logging**: `✅ MAJOR update: [title]`
- **Use Case**: Significant content changes, new information

#### Minor Update
- **Condition**: Content similarity 70-95%
- **Action**: Extract and process
- **Update Type**: `minor`
- **Logging**: `✅ MINOR update: [title]`
- **Use Case**: Moderate content changes, corrections, additions

#### New Intelligence
- **Condition**: No existing hash found
- **Action**: Extract and process
- **Update Type**: `new`
- **Logging**: `✅ New intelligence: [title]`
- **Use Case**: Completely new intelligence

## Similarity Calculation

### Method
1. Convert content to lowercase
2. Split into word sets
3. Calculate intersection of word sets
4. Similarity = `common_words / max(old_words, new_words)`

### Thresholds
- **>95% similarity**: No substantial update (skip)
- **70-95% similarity**: Minor update (extract)
- **<70% similarity**: Major update (extract)

## Intelligence Tracking

### Hash Registry
- **File**: `data/syphon_source_sweeps_scans/intelligence_hashes.json`
- **Structure**:
  ```json
  {
    "hash": {
      "source_id": "internal_email_all",
      "timestamp": "2026-01-10T14:30:22",
      "version": 2,
      "content_hash": "abc123...",
      "content": "First 500 chars...",
      "title": "Intelligence Title",
      "url": "https://...",
      "update_type": "major"
    }
  }
  ```

### Version Tracking
- **Initial**: Version 1
- **Major Update**: Version increments
- **Minor Update**: Version increments
- **Purpose**: Track intelligence evolution

## Integration

### With Scan Results
- **Metadata**: Includes `duplicates_skipped` and `updates_found`
- **Intelligence**: Only new/updated intelligence included
- **Logging**: Deduplication stats logged per scan

### With Unified Queue
- **Filtered Intelligence**: Only new/updated intelligence added to queue
- **Metadata**: Includes update type and version
- **Priority**: Major updates may have higher priority

### With Holocron Archive
- **Storage**: Only new/updated intelligence stored
- **Versioning**: Intelligence versions tracked
- **Efficiency**: Reduces storage and processing overhead

## Usage

### Automatic Deduplication
Deduplication happens automatically during scans:
```python
sweeps_scans = SyphonSourceSweepsScans()
result = sweeps_scans.scan_source("external_web_sources", ScanType.QUICK)

# Result includes deduplication stats
print(f"Intelligence extracted: {result.intelligence_extracted}")
print(f"Duplicates skipped: {result.metadata['duplicates_skipped']}")
print(f"Updates found: {result.metadata['updates_found']}")
```

### Manual Duplicate Check
```python
intelligence_data = {
    "content": "...",
    "title": "...",
    "url": "..."
}

is_duplicate, existing_hash, update_type = sweeps_scans._check_intelligence_duplicate(
    intelligence_data, "source_id"
)

if is_duplicate:
    print("Exact duplicate - skip")
elif update_type:
    print(f"{update_type.upper()} update - extract")
else:
    print("New intelligence - extract")
```

## Statistics

### Deduplication Metrics
- **Total Registered**: All intelligence hashes tracked
- **Unique Intelligence**: Unique content hashes
- **Duplicates Prevented**: Total - Unique
- **Efficiency**: Percentage of duplicates prevented

### Update Distribution
- **New Intelligence**: Count of new intelligence
- **Major Updates**: Count of major updates
- **Minor Updates**: Count of minor updates
- **Skipped**: Count of skipped duplicates

## Benefits

### Efficiency
- **Reduced Processing**: Skip duplicate extraction
- **Reduced Storage**: Only store new/updated intelligence
- **Reduced Network**: Skip redundant downloads

### Quality
- **Update Tracking**: Track intelligence evolution
- **Version Control**: Intelligence versioning
- **Change Detection**: Detect substantial changes

### Performance
- **Faster Scans**: Skip duplicate processing
- **Lower Resource Usage**: Reduced CPU/memory
- **Better Prioritization**: Focus on new/updated intelligence

## Configuration

### Similarity Thresholds
- **No Update Threshold**: 95% (configurable)
- **Minor Update Threshold**: 70% (configurable)
- **Major Update Threshold**: <70% (configurable)

### Hash Storage
- **Content Preview**: First 500 characters stored
- **Full Content Hash**: SHA256 hash of full content
- **Metadata**: Title, URL, source stored

## Status

✅ **COMPLETE** - Intelligence deduplication system

Features:
- ✅ Content hashing (primary + content)
- ✅ Duplicate detection
- ✅ Update detection (major/minor)
- ✅ Similarity calculation
- ✅ Version tracking
- ✅ Hash registry persistence
- ✅ Automatic deduplication
- ✅ Statistics and reporting

---

**Tags**: @SYPHON @DEDUPLICATION @INTELLIGENCE @HASHING @UPDATES @EFFICIENCY
