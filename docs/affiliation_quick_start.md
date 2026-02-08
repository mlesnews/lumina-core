# Affiliate Network Platform - Quick Start Guide

## Overview

The Affiliate Network Platform provides unified content aggregation, analytics, and cross-affiliate services for EWTN, Magis Center, and their affiliates.

## Quick Start

### 1. Initialize Platform

```bash
python scripts/python/affiliate_network_platform.py
```

This initializes the platform with EWTN and Magis Center as default affiliates.

### 2. Add Affiliates

```bash
python scripts/python/affiliate_network_platform.py \
  --add-affiliate "Organization Name" \
  --url "https://www.example.com" \
  --description "Description of organization" \
  --tags "tag1,tag2,tag3"
```

### 3. Sync Content

Sync content from all affiliates:
```bash
python scripts/python/affiliate_network_platform.py --sync-all
```

Sync from specific affiliate:
```bash
python scripts/python/affiliate_network_platform.py --sync "EWTN"
```

### 4. Search Content

Search across all affiliates:
```bash
python scripts/python/affiliate_network_platform.py --search "faith and science"
```

### 5. View Analytics

```bash
python scripts/python/affiliate_network_platform.py --analytics
```

### 6. Generate Report

```bash
python scripts/python/affiliate_network_platform.py --report
```

## Key Features

### Content Aggregation
- Automatically collects content from all affiliates
- Unified content index
- Cross-affiliate search

### Analytics
- Content by affiliate
- Tag distribution
- Recent content tracking
- Network-wide insights

### Service Offerings

1. **Unified Content API** - Single API for all affiliate content
2. **Cross-Affiliate Search** - Search across entire network
3. **Content Analytics** - Performance insights
4. **Trend Detection** - Identify emerging topics
5. **Content Recommendations** - AI-powered suggestions

## Integration with SYPHON

The platform uses SYPHON for intelligent content extraction:
- Automatic content indexing
- Metadata extraction
- Intelligence extraction
- Relationship mapping

## Data Storage

All data is stored in:
```
data/affiliate_network/
  ├── affiliates.json          # Affiliate registry
  ├── content_index.json       # Unified content index
  └── analytics.json           # Analytics data
```

## Next Steps

1. Review the full proposal: `docs/affiliation_proposal_ewtn_magiscenter.md`
2. Customize for specific needs
3. Deploy and start serving affiliates

## Support

For questions or customization requests, refer to the main proposal document.

